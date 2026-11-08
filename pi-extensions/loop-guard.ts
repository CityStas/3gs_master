/**
 * Loop guard: stops a small local model from repeating a call that cannot start working.
 *
 * The failure this exists for, from the pi session logs of 2026-10-12: 47 assistant turns,
 * 20 repeated-failed tool calls, one compaction caught mid-task. The model is not
 * deliberating between those calls - it re-emits the same `read` with the same wrong path,
 * or alternates between two tools that both fail, and burns the context window doing it.
 *
 * Where the guard sits and why:
 *
 *   tool_call   -> block before the call costs a round trip. Cheap, deterministic, and the
 *                  reason string is what the model reads next - so it carries the next
 *                  action, not just "no".
 *   tool_result -> classify the failure, verify that a write/edit actually landed, and
 *                  rewrite the error into the structured contract both pi and a human can
 *                  read. This is also the only place where "success" can be checked
 *                  against the disk instead of against the model's own claim.
 *
 * Nothing here calls a model, and nothing here rewrites a legitimate retry: only FAILED
 * calls are counted, and any successful mutating call clears every counter.
 *
 * Policy: mcp/reliability.json. Logic: reliability-core.ts. This file is only wiring.
 */
import { existsSync, readdirSync } from "node:fs";
import { basename, dirname, join } from "node:path";

import {
  EventLog,
  LoopGuard,
  ProgressGuard,
  SuccessLedger,
  checkPath,
  classify,
  errorPayload,
  fingerprint,
  loadPolicy,
  readProjectContext,
  repoRelative,
  repoRoot,
  resolveToolPath,
  serverOf,
  verifyWrite,
  type ErrorCode,
  type ReliabilityEvent,
} from "./reliability-core.ts";

interface ToolCallEvent {
  type: "tool_call";
  toolCallId: string;
  toolName: string;
  input: Record<string, unknown>;
}

interface ToolResultEvent {
  type: "tool_result";
  toolCallId: string;
  toolName: string;
  input: Record<string, unknown>;
  content: { type: string; text?: string }[];
  isError: boolean;
}

interface ExtensionApi {
  on(event: "session_start", handler: () => void): void;
  on(event: "session_shutdown", handler: () => void): void;
  on(event: "tool_call", handler: (event: ToolCallEvent) => { block?: boolean; reason?: string } | void): void;
  on(event: "tool_result", handler: (event: ToolResultEvent) => { content?: unknown[]; isError?: boolean } | void): void;
  getAllTools(): { name: string; annotations?: { readOnlyHint?: boolean } }[];
}

/** Tools whose `path` argument is a write target and therefore sandbox-checked. */
const MUTATING_PATH_TOOLS = new Set(["write", "edit"]);

/**
 * A success of any of these may have changed the world, so a counter recorded before it
 * is no longer evidence of a loop. Taken from the policy rather than restated here: the
 * ledger and the loop guard must agree on what "mutating" means, or one of them keeps a
 * stale count the other has already invalidated.
 */
function mutatingTools(policy: ReturnType<typeof loadPolicy>): Set<string> {
  return new Set(policy.duplicate_success.generation_tools);
}

/** Tools that read a file by path - the ones worth a "here is what IS there" hint. */
const PATH_TOOLS = new Set(["read", "edit", "write", "ls", "grep", "find"]);

export default function loopGuard(pi: ExtensionApi): void {
  const root = repoRoot();
  const policy = loadPolicy(root);
  const log = new EventLog(policy, root);
  const guard = new LoopGuard(policy);
  const ledger = new SuccessLedger(policy);
  const progress = new ProgressGuard(policy);
  const MUTATING = mutatingTools(policy);

  /**
   * Tools the client itself declares read-only (MCP servers set `readOnlyHint`).
   *
   * Read at session start and on `mcp_servers_change`-free cadence: the set only grows
   * when a server connects, and `getAllTools()` is a cheap array copy. Without this a RAG
   * search would count as a mutation, switch the progress guard off, and leave a
   * search-heavy session - the exact shape a 9B model falls into - unguarded.
   */
  let readOnlyTools = new Set<string>();
  const refreshReadOnly = (): void => {
    try {
      readOnlyTools = new Set(
        (pi.getAllTools() ?? [])
          .filter((tool) => tool.annotations?.readOnlyHint === true)
          .map((tool) => tool.name),
      );
    } catch {
      readOnlyTools = new Set();
    }
  };
  const isReadOnly = (name: string): boolean => readOnlyTools.has(name);

  const runId = `pi-${process.pid}-${new Date().toISOString().replace(/[:.]/g, "-")}`;
  /** toolCallId -> start time, for the elapsed column. */
  const started = new Map<string, number>();
  /** toolCallId -> the verdict we would have returned, so tool_result can log it. */
  const notes = new Map<string, string>();
  let staleWarned = false;

  const emit = (event: Partial<ReliabilityEvent> & { tool: string }): void => {
    const ctx = readProjectContext(root);
    log.write({
      ts: new Date().toISOString(),
      run_id: runId,
      client: "pi",
      engine: ctx.engine,
      project: ctx.project ? repoRelative(root, ctx.project) : undefined,
      server: serverOf(event.tool),
      fingerprint: "",
      ok: true,
      ...event,
    } as ReliabilityEvent);
  };

  pi.on("session_start", () => {
    guard.reset();
    ledger.reset();
    progress.reset();
    refreshReadOnly();
    staleWarned = false;
    const ctx = readProjectContext(root);
    if (ctx.stale) {
      process.stderr.write(
        `[loop-guard] the active project is STALE: data/active_project.txt names "${ctx.stale}", ` +
          `which is not a directory. No path is anchored to it; re-run \`dev.cmd <name>\`.\n`,
      );
    }
    emit({ tool: "session", note: `start engine=${ctx.engine}` });
  });

  pi.on("session_shutdown", () => {
    emit({ tool: "session", note: `stop blocked=${guard.blockedCount}` });
    started.clear();
    notes.clear();
  });

  pi.on("tool_call", (event) => {
    const input = (event.input ?? {}) as Record<string, unknown>;
    const ctx = readProjectContext(root);
    started.set(event.toolCallId, Date.now());

    if (ctx.stale && !staleWarned) {
      staleWarned = true;
      // Not a block: a RAG question still works with a dead pointer. It is named once, so
      // the agent knows why every project-relative path it guesses is about to fail.
      notes.set(event.toolCallId, "stale-active-project");
    }

    const fp = fingerprint({ toolName: event.toolName, args: input, context: ctx.project ?? ctx.engine });

    // 1. Sandbox: a mutating call outside the repository is refused outright.
    if (MUTATING_PATH_TOOLS.has(event.toolName) && typeof input.path === "string") {
      const verdict = checkPath(input.path, { cwd: process.cwd(), repo: root, project: ctx.project }, policy);
      if (verdict.decision === "block") {
        emit({
          tool: event.toolName,
          fingerprint: fp,
          ok: false,
          error_code: "PATH_OUTSIDE_SANDBOX",
          decision: "block",
          note: repoRelative(root, verdict.resolved),
        });
        return {
          block: true,
          reason:
            errorPayload("PATH_OUTSIDE_SANDBOX", event.toolName, {
              path: verdict.resolved,
              message: verdict.message,
            }, policy) +
            `\nWrite inside ${root}${ctx.project ? ` (active project: ${repoRelative(root, ctx.project)})` : ""}.`,
        };
      }
      if (verdict.decision === "warn") {
        notes.set(event.toolCallId, `outside-active-project:${repoRelative(root, verdict.resolved)}`);
      }
    }

    // 2. The same mutating call that already succeeded, with nothing changed since.
    const dup = ledger.before({ toolName: event.toolName, args: input, context: ctx.project ?? ctx.engine });
    if (dup.decision === "block") {
      emit({
        tool: event.toolName,
        fingerprint: fp,
        ok: false,
        error_code: "DUPLICATE_SUCCESS",
        decision: "block",
        retry_count: dup.attempts,
      });
      return {
        block: true,
        reason: errorPayload("DUPLICATE_SUCCESS", event.toolName, {
          attempts: dup.attempts,
          message: dup.message,
        }, policy),
      };
    }

    // 3. The same call that already failed, or a two-call cycle that is going nowhere.
    const verdict = guard.before({ toolName: event.toolName, args: input, context: ctx.project ?? ctx.engine });
    if (verdict.decision === "block" && verdict.code) {
      emit({
        tool: event.toolName,
        fingerprint: fp,
        ok: false,
        error_code: verdict.code,
        decision: "block",
        retry_count: verdict.attempts,
      });
      return {
        block: true,
        reason: errorPayload(verdict.code, event.toolName, {
          attempts: verdict.attempts,
          message: verdict.message,
          extra: verdict.code === "REPEATED_TOOL_CALL" ? { retryable: false } : undefined,
        }, policy),
      };
    }

    // 4. Nothing written yet, and a lot of looking. The one failure mode a fingerprint
    //    cannot see: 40 different calls that all amount to re-reading the same files.
    const noProgress = progress.before(
      { toolName: event.toolName, args: input, context: ctx.project ?? ctx.engine },
      isReadOnly(event.toolName),
    );
    if (noProgress.decision === "block" && noProgress.code) {
      emit({
        tool: event.toolName,
        fingerprint: fp,
        ok: false,
        error_code: noProgress.code,
        decision: "block",
        retry_count: noProgress.attempts,
      });
      return {
        block: true,
        reason: errorPayload(noProgress.code, event.toolName, {
          attempts: noProgress.attempts,
          message: noProgress.message,
        }, policy),
      };
    }
    return;
  });

  pi.on("tool_result", (event) => {
    const input = (event.input ?? {}) as Record<string, unknown>;
    const ctx = readProjectContext(root);
    const elapsed = started.has(event.toolCallId) ? Date.now() - (started.get(event.toolCallId) ?? 0) : undefined;
    started.delete(event.toolCallId);
    const note = notes.get(event.toolCallId);
    notes.delete(event.toolCallId);

    const fp = fingerprint({ toolName: event.toolName, args: input, context: ctx.project ?? ctx.engine });
    const text = (event.content ?? [])
      .map((part) => (part && typeof part.text === "string" ? part.text : ""))
      .join("\n");

    // --- postcondition: a write/edit that did not land is NOT a success ---------------
    if (!event.isError && policy.write_verification.enabled && policy.write_verification.tools.includes(event.toolName)) {
      if (typeof input.path === "string") {
        const target = resolveToolPath(input.path, process.cwd());
        const expected =
          event.toolName === "write" && typeof input.content === "string"
            ? Buffer.byteLength(input.content, "utf8")
            : undefined;
        const check = verifyWrite(target, { expectedBytes: expected }, policy);
        if (!check.ok) {
          emit({
            tool: event.toolName,
            fingerprint: fp,
            elapsed_ms: elapsed,
            ok: false,
            error_code: "WRITE_NOT_VERIFIED",
            decision: "verify",
            verification: "failed",
            note: repoRelative(root, target),
          });
          const payload = errorPayload("WRITE_NOT_VERIFIED", event.toolName, {
            path: repoRelative(root, target),
            message: check.message,
          }, policy);
          return {
            isError: true,
            content: [
              ...(event.content ?? []),
              { type: "text", text: `\n\n${payload}` },
            ],
          };
        }
        emit({
          tool: event.toolName,
          fingerprint: fp,
          elapsed_ms: elapsed,
          ok: true,
          decision: "verify",
          verification: `ok ${check.bytes ?? 0}b`,
          note: note ?? repoRelative(root, target),
        });
        // A verified mutation moves the world on: nothing counted before it is a fact now.
        guard.resetOnMutation();
        ledger.after({ toolName: event.toolName, args: input, context: ctx.project ?? ctx.engine }, false);
        progress.after(
          { toolName: event.toolName, args: input, context: ctx.project ?? ctx.engine },
          false,
          isReadOnly(event.toolName),
        );
        return;
      }
    }

    if (!event.isError) {
      guard.after({ toolName: event.toolName, args: input, context: ctx.project ?? ctx.engine }, false, null);
      // A successful `bash`/`write`/`edit` invalidates every count: the failed call it
      // followed may now work for a real reason (a dependency installed, a file written).
      if (MUTATING.has(event.toolName)) guard.resetOnMutation();
      ledger.after({ toolName: event.toolName, args: input, context: ctx.project ?? ctx.engine }, false);
      progress.after(
        { toolName: event.toolName, args: input, context: ctx.project ?? ctx.engine },
        false,
        isReadOnly(event.toolName),
      );
      emit({
        tool: event.toolName,
        fingerprint: fp,
        elapsed_ms: elapsed,
        ok: true,
        note: note,
      });
      return;
    }

    // --- failure: classify, count, and hand back something actionable ----------------
    const cls = classify(text, policy);
    guard.after({ toolName: event.toolName, args: input, context: ctx.project ?? ctx.engine }, true, cls.code);
    progress.after(
      { toolName: event.toolName, args: input, context: ctx.project ?? ctx.engine },
      true,
      isReadOnly(event.toolName),
    );

    const extra: Record<string, unknown> = {};
    if (cls.code === "FILE_NOT_FOUND" && typeof input.path === "string") {
      Object.assign(extra, recoveryHint(resolveToolPath(input.path, process.cwd()), root));
    }

    emit({
      tool: event.toolName,
      fingerprint: fp,
      elapsed_ms: elapsed,
      ok: false,
      error_code: cls.code,
      decision: "classify",
      note: note,
    });

    const payload = errorPayload(cls.code, event.toolName, {
      path: typeof input.path === "string" ? repoRelative(root, resolveToolPath(input.path, process.cwd())) : undefined,
      message: firstLine(text) || cls.next_action,
      extra: Object.keys(extra).length ? extra : undefined,
    }, policy);

    // Additive, not a replacement: the server's own message stays first, the contract is
    // appended. A client that ignores the JSON still sees the original error.
    return {
      content: [...(event.content ?? []), { type: "text", text: `\n\n${payload}` }],
    };
  });
}

function firstLine(text: string): string {
  const line = (text ?? "").split("\n").map((l) => l.trim()).find((l) => l.length > 0) ?? "";
  return line.length > 300 ? `${line.slice(0, 300)}...` : line;
}

/**
 * What the model actually needs after an ENOENT: the nearest directory that DOES exist and
 * a few names in it, plus a case-insensitive near-miss. Deterministic, two syscalls, and
 * worth more than any amount of "please check the path" in a prompt.
 */
function recoveryHint(target: string, root: string): Record<string, unknown> {
  const out: Record<string, unknown> = {};
  let dir = dirname(target);
  for (let hops = 0; hops < 4; hops += 1) {
    if (existsSync(dir)) break;
    const parent = dirname(dir);
    if (parent === dir) break;
    dir = parent;
  }
  if (!existsSync(dir)) return out;
  out.nearest_existing_directory = repoRelative(root, dir);
  try {
    const entries = readdirSync(dir).slice(0, 25);
    out.entries = entries;
    const want = basename(target).toLowerCase();
    const near = entries.find((name) => {
      const lower = name.toLowerCase();
      return lower === want || lower.includes(want) || want.includes(lower.replace(/\.[^.]+$/, ""));
    });
    if (near) out.did_you_mean = near;
    // A name that differs only by case is the single most common miss on Windows.
    for (const name of entries) {
      if (name.toLowerCase() === want && name !== basename(target)) {
        out.case_mismatch = name;
        break;
      }
    }
  } catch {
    /* a listing is a hint, never a failure */
  }
  return out;
}
