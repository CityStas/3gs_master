/**
 * Reliability core: the deterministic half of the agent guards.
 *
 * Pure logic only - no pi API in this file. `loop-guard.ts` wires it to `tool_call` /
 * `tool_result`; `tests/reliability_parity.mjs` runs it under plain node and compares the
 * answers with `tools/reliability.py`, so the two languages cannot drift.
 *
 * The policy (thresholds, error patterns, next actions) lives in `mcp/reliability.json`,
 * NOT here. Read it once at load, fall back to the baked-in defaults if the file is
 * missing or broken: a guard that throws is a guard that is not guarding.
 *
 * Design rules, in the order they matter:
 *
 *   1. Only FAILED calls are counted. Reads that succeed never touch a counter, so
 *      polling, paginated search and re-reading a file after an edit stay legal.
 *   2. A hard failure cannot be fixed by repeating the identical call. The model must
 *      change the arguments or the tool - which is exactly what the returned `next_action`
 *      says, in the same breath as the block.
 *   3. A transient failure (timeout, dead server, truncated output) gets a bounded retry
 *      instead of an immediate block, because there the retry is often the correct move.
 *   4. Any successful MUTATING call clears every counter. The world may have changed;
 *      a call that failed before can succeed now for a real reason.
 */
import { createHash } from "node:crypto";
import { existsSync, mkdirSync, readFileSync, statSync, appendFileSync, renameSync, unlinkSync } from "node:fs";
import { dirname, isAbsolute, join, relative, resolve, sep } from "node:path";

export type ErrorCode =
  | "REPEATED_TOOL_CALL"
  | "TOOL_CYCLE_DETECTED"
  | "DUPLICATE_SUCCESS"
  | "NO_PROGRESS"
  | "FILE_NOT_FOUND"
  | "PATH_OUTSIDE_SANDBOX"
  | "PERMISSION_DENIED"
  | "INVALID_ARGUMENT"
  | "TIMEOUT"
  | "SERVER_UNAVAILABLE"
  | "OUTPUT_TOO_LARGE"
  | "VALIDATION_FAILED"
  | "WRITE_NOT_VERIFIED"
  | "UNKNOWN";

export interface CodePolicy {
  retryable: boolean;
  next_action: string;
}

export interface Policy {
  loop_guard: {
    enabled: boolean;
    max_identical_failures: number;
    max_identical_failures_transient: number;
    cycle_length: number;
    cycle_repeats: number;
    max_tracked_fingerprints: number;
  };
  duplicate_success: {
    enabled: boolean;
    tools: string[];
    generation_tools: string[];
    max_duplicates: number;
  };
  progress_guard: {
    enabled: boolean;
    block_after_inspections: number;
    require_zero_mutations: boolean;
    inspection_tools: string[];
    inspection_bash_prefixes: string[];
  };
  write_guard: { enabled: boolean; max_bytes: number; max_lines: number; max_rewrites: number };
  write_verification: { enabled: boolean; mtime_freshness_ms: number; tools: string[] };
  path_guard: { enabled: boolean; block_outside_repo: boolean; warn_outside_project: boolean };
  logging: { enabled: boolean; dir: string; max_files: number; max_bytes_per_file: number };
  state: { enabled: boolean; dir: string; max_runs_kept: number };
  errors: { codes: Record<string, CodePolicy>; patterns: [string, string[]][] };
}

/** Baked-in fallback. Values copied from mcp/reliability.json; the tests assert equality. */
export const DEFAULT_POLICY: Policy = {
  loop_guard: {
    enabled: true,
    max_identical_failures: 1,
    max_identical_failures_transient: 3,
    cycle_length: 4,
    cycle_repeats: 2,
    max_tracked_fingerprints: 256,
  },
  duplicate_success: {
    enabled: true,
    tools: ["write", "edit"],
    generation_tools: ["write", "edit", "bash", "powershell"],
    max_duplicates: 1,
  },
  write_guard: { enabled: true, max_bytes: 12000, max_lines: 320, max_rewrites: 3 },
  progress_guard: {
    enabled: true,
    block_after_inspections: 20,
    require_zero_mutations: true,
    inspection_tools: ["read", "ls", "grep", "find"],
    inspection_bash_prefixes: [
      "ls", "cat", "sed", "head", "tail", "grep", "rg", "find", "wc", "type", "which",
      "pwd", "echo", "cd", "git status", "git log", "git diff", "dir", "stat", "file", "du",
    ],
  },
  write_verification: { enabled: true, mtime_freshness_ms: 120000, tools: ["write", "edit"] },
  path_guard: { enabled: true, block_outside_repo: true, warn_outside_project: true },
  logging: { enabled: true, dir: "logs/reliability", max_files: 14, max_bytes_per_file: 2097152 },
  state: { enabled: true, dir: "data/reliability", max_runs_kept: 40 },
  errors: {
    codes: {
      REPEATED_TOOL_CALL: {
        retryable: false,
        next_action:
          "Do not repeat this call. Inspect the parent directory, verify the active project, search for the name, or change the arguments.",
      },
      TOOL_CYCLE_DETECTED: {
        retryable: false,
        next_action:
          "Two calls are alternating without progress. Stop both, re-read the last error, and change strategy - a different tool or a different argument.",
      },
      DUPLICATE_SUCCESS: {
        retryable: false,
        next_action: "This exact call already succeeded in the current state. Read the earlier result or move to the next step.",
      },
      NO_PROGRESS: {
        retryable: false,
        next_action:
          "Stop inspecting. Nothing has been written yet: create the first file with `write` (a small one, then extend it with `edit`). Further reads will be refused until something is on disk.",
      },
      FILE_NOT_FOUND: {
        retryable: false,
        next_action: "List the parent directory or search for the filename; do not retry this path unchanged.",
      },
      PATH_OUTSIDE_SANDBOX: {
        retryable: false,
        next_action:
          "Write inside the repository (and inside the active project when there is one). Use an absolute path only when the repository itself is the target.",
      },
      PERMISSION_DENIED: {
        retryable: false,
        next_action:
          "Report the permission boundary and ask for an authorized alternative; repeating the same call will fail identically.",
      },
      INVALID_ARGUMENT: {
        retryable: false,
        next_action: "Correct the arguments against the tool schema. Do not resend the same payload.",
      },
      TIMEOUT: {
        retryable: true,
        next_action: "Check whether the server is healthy before retrying; retry once only if the operation is idempotent.",
      },
      SERVER_UNAVAILABLE: {
        retryable: true,
        next_action: "The MCP server or model endpoint is down. Start or restart it, then retry at most once.",
      },
      OUTPUT_TOO_LARGE: {
        retryable: false,
        next_action:
          "Reduce the payload: ranged read, narrower grep, or split the write into a first chunk plus edits.",
      },
      VALIDATION_FAILED: {
        retryable: false,
        next_action: "Read the validator's actual message and patch the cause; do not resend the same code.",
      },
      WRITE_NOT_VERIFIED: {
        retryable: false,
        next_action:
          "The tool claimed success but the file on disk did not change. Re-read the file and retry the write with correct content.",
      },
      UNKNOWN: {
        retryable: false,
        next_action: "Read the error text and change something before calling again.",
      },
    },
    patterns: [
      ["REPEATED_TOOL_CALL", ["repeated tool call", "already failed identically"]],
      ["TOOL_CYCLE_DETECTED", ["tool cycle"]],
      ["DUPLICATE_SUCCESS", ["already succeeded in this state"]],
      ["NO_PROGRESS", ["nothing has been written yet", "no progress"]],
      ["WRITE_NOT_VERIFIED", ["write not verified"]],
      ["PATH_OUTSIDE_SANDBOX", ["outside the repository", "outside the project", "path escapes", "sandbox"]],
      ["FILE_NOT_FOUND", ["no such file", "cannot find the file", "file not found", "does not exist", "enoent", "not found"]],
      ["PERMISSION_DENIED", ["permission denied", "eacces", "eperm", "access is denied", "access denied", "unauthorized", "forbidden"]],
      ["OUTPUT_TOO_LARGE", ["output token limit", "maximum context", "context length", "too large", "truncated", "exceeds the maximum", "response was cut"]],
      ["TIMEOUT", ["timed out", "timeout", "etimedout", "deadline exceeded"]],
      ["SERVER_UNAVAILABLE", ["econnrefused", "connection refused", "connection reset", "server unavailable", "not connected", "no studios connected", "failed to start", "epipe"]],
      ["VALIDATION_FAILED", ["error ts", "syntax error", "validation failed", "lint error", "failed to parse", "unexpected token", "is not valid json", "exit code 1"]],
      ["INVALID_ARGUMENT", ["invalid argument", "invalid params", "invalid type", "expected string", "must be a", "eisdir", "is a directory", "missing required"]],
    ],
  },
};

/** Repository root: GS_ROOT when a launcher set it, else the process cwd (pi starts at the root). */
export function repoRoot(env: NodeJS.ProcessEnv = process.env): string {
  return resolve(env.GS_ROOT ?? process.cwd());
}

/**
 * Load the policy. A broken file is reported once on stderr and replaced by the defaults -
 * the alternative (throwing during extension load) removes every guard for the session.
 */
export function loadPolicy(root: string = repoRoot()): Policy {
  const file = join(root, "mcp", "reliability.json");
  if (!existsSync(file)) return DEFAULT_POLICY;
  try {
    const raw = JSON.parse(readFileSync(file, "utf8")) as Partial<Policy>;
    return mergePolicy(DEFAULT_POLICY, raw);
  } catch (err) {
    process.stderr.write(`[reliability] cannot parse ${file}: ${String(err)} - using defaults\n`);
    return DEFAULT_POLICY;
  }
}

/** Shallow merge per section, so a policy file may carry only the keys it wants to change. */
function mergePolicy(base: Policy, raw: Partial<Policy>): Policy {
  const out = { ...base } as Policy;
  for (const key of Object.keys(base) as (keyof Policy)[]) {
    const value = (raw as Record<string, unknown>)[key];
    if (value && typeof value === "object") {
      out[key] = { ...(base[key] as object), ...(value as object) } as never;
    }
  }
  // `errors` needs its two sub-objects merged separately, not replaced wholesale.
  const errs = (raw.errors ?? {}) as Partial<Policy["errors"]>;
  out.errors = {
    codes: { ...base.errors.codes, ...(errs.codes ?? {}) },
    patterns: (errs.patterns ?? base.errors.patterns) as [string, string[]][],
  };
  return out;
}

// ---------------------------------------------------------------------------
// Error classification
// ---------------------------------------------------------------------------

export interface Classification {
  code: ErrorCode;
  retryable: boolean;
  next_action: string;
}

/**
 * Map raw tool error text to a stable code.
 *
 * `hint` short-circuits the text scan: the guard already knows the code it is about to
 * emit (REPEATED_TOOL_CALL, WRITE_NOT_VERIFIED), and guessing from a message it wrote
 * itself would be silly.
 */
export function classify(message: string, policy: Policy = DEFAULT_POLICY, hint?: ErrorCode): Classification {
  const code = hint ?? matchCode(message ?? "", policy);
  const entry = policy.errors.codes[code] ?? policy.errors.codes.UNKNOWN;
  return { code, retryable: entry.retryable, next_action: entry.next_action };
}

function matchCode(message: string, policy: Policy): ErrorCode {
  const text = message.toLowerCase();
  for (const [code, needles] of policy.errors.patterns) {
    for (const needle of needles) {
      if (text.includes(needle)) return code as ErrorCode;
    }
  }
  return "UNKNOWN";
}

// ---------------------------------------------------------------------------
// Fingerprints
// ---------------------------------------------------------------------------

/**
 * Stable JSON: object keys sorted at every depth, arrays kept in order.
 *
 * Two calls are "the same call" only when this string is equal. Sorting matters because
 * a 9B model re-emits the same arguments in a different key order more often than it
 * emits different arguments, and `{"a":1,"b":2}` vs `{"b":2,"a":1}` is the same call.
 */
export function stableStringify(value: unknown): string {
  if (value === null || typeof value !== "object") return JSON.stringify(value) ?? "null";
  if (Array.isArray(value)) return `[${value.map(stableStringify).join(",")}]`;
  const obj = value as Record<string, unknown>;
  const keys = Object.keys(obj).sort();
  return `{${keys.map((k) => `${JSON.stringify(k)}:${stableStringify(obj[k])}`).join(",")}}`;
}

/** Tool name without the MCP server prefix (`rbx-project__read_file` -> `rbx-project`). */
export function serverOf(toolName: string): string {
  const idx = toolName.indexOf("__");
  return idx > 0 ? toolName.slice(0, idx) : "builtin";
}

export interface FingerprintInput {
  toolName: string;
  args: Record<string, unknown>;
  /** Active project + engine, so the same call in another project is a different call. */
  context?: string;
}

export function fingerprint(input: FingerprintInput): string {
  const material = stableStringify({
    server: serverOf(input.toolName),
    tool: input.toolName,
    args: input.args ?? {},
    ctx: input.context ?? "",
  });
  return createHash("sha1").update(material).digest("hex").slice(0, 16);
}

// ---------------------------------------------------------------------------
// Loop guard
// ---------------------------------------------------------------------------

export type Decision = "allow" | "block";

export interface GuardVerdict {
  decision: Decision;
  code?: ErrorCode;
  attempts?: number;
  message?: string;
  next_action?: string;
  retryable?: boolean;
}

interface FailureRecord {
  fingerprint: string;
  code: ErrorCode;
  count: number;
  toolName: string;
}

/**
 * Session-scoped loop guard.
 *
 * Counters live in a Map keyed by fingerprint and are dropped at the start of a session
 * and on any successful mutating call. Memory is capped at `max_tracked_fingerprints`;
 * when the cap is hit the oldest entry is evicted, which is enough because a model that
 * has 256 distinct failing calls is not in a loop, it is lost.
 */
export class LoopGuard {
  private failures = new Map<string, FailureRecord>();
  private order: string[] = [];
  /** Last N failing (fingerprint, code) pairs, oldest first - the cycle window. */
  private history: { fingerprint: string; code: ErrorCode }[] = [];
  private blocked = 0;

  private policy: Policy;

  constructor(policy: Policy = DEFAULT_POLICY) {
    this.policy = policy;
  }

  reset(): void {
    this.failures.clear();
    this.order = [];
    this.history = [];
    this.blocked = 0;
  }

  get blockedCount(): number {
    return this.blocked;
  }

  /** Called before the tool runs. Blocks a call that is known to be repeating a hard failure. */
  before(input: FingerprintInput): GuardVerdict {
    if (!this.policy.loop_guard.enabled) return { decision: "allow" };
    const fp = fingerprint(input);

    // Cycle first, repeat second. With `max_identical_failures: 1` the repeat check would
    // otherwise always win and the cycle case would be unreachable - but A -> B -> A -> B is
    // a different failure: neither call is stuck on its own, the PAIR is. That pattern only
    // survives the repeat check when a successful mutation resets the counters between
    // rounds, which is exactly the oscillation worth naming.
    const cycle = this.detectCycle(fp);
    if (cycle) {
      this.blocked += 1;
      const cls = classify("", this.policy, "TOOL_CYCLE_DETECTED");
      return {
        decision: "block",
        code: "TOOL_CYCLE_DETECTED",
        attempts: cycle,
        retryable: false,
        message:
          `${cycle} calls have been alternating between two tools and failing each time - ` +
          `neither one is making progress.`,
        next_action: cls.next_action,
      };
    }

    const record = this.failures.get(fp);
    if (record) {
      const transient = this.isTransient(record.code);
      const limit = transient
        ? this.policy.loop_guard.max_identical_failures_transient
        : this.policy.loop_guard.max_identical_failures;
      if (record.count >= limit) {
        this.blocked += 1;
        const cls = classify("", this.policy, "REPEATED_TOOL_CALL");
        return {
          decision: "block",
          code: "REPEATED_TOOL_CALL",
          attempts: record.count,
          retryable: false,
          message:
            `this exact call to ${record.toolName} has already failed ${record.count}x with ` +
            `${record.code}, and nothing changed in between.`,
          next_action: cls.next_action,
        };
      }
    }
    return { decision: "allow" };
  }

  /** Called after the tool ran. Records a hard failure, forgets a success. */
  after(input: FingerprintInput, isError: boolean, code: ErrorCode | null): void {
    if (!this.policy.loop_guard.enabled) return;
    const fp = fingerprint(input);
    if (!isError) {
      this.forget(fp);
      return;
    }
    const realCode = code ?? "UNKNOWN";
    const record = this.failures.get(fp);
    if (record && record.code === realCode) {
      record.count += 1;
    } else {
      this.remember({ fingerprint: fp, code: realCode, count: 1, toolName: input.toolName });
    }
    this.history.push({ fingerprint: fp, code: realCode });
    const window = this.policy.loop_guard.cycle_length * this.policy.loop_guard.cycle_repeats;
    if (this.history.length > window) this.history.splice(0, this.history.length - window);
  }

  /**
   * A successful mutating call may have changed the world, so no counted FAILURE is a fact
   * any more - a retry can legitimately succeed now. The cycle window is kept on purpose:
   * "read fails, edit succeeds, read fails, edit succeeds, read fails" is an oscillation,
   * and forgetting the shape of it because the edits succeeded is how the loop survives.
   */
  resetOnMutation(): void {
    this.failures.clear();
    this.order = [];
  }

  private isTransient(code: ErrorCode): boolean {
    return code === "TIMEOUT" || code === "SERVER_UNAVAILABLE" || code === "OUTPUT_TOO_LARGE";
  }

  private remember(record: FailureRecord): void {
    if (!this.failures.has(record.fingerprint)) {
      this.order.push(record.fingerprint);
      const cap = this.policy.loop_guard.max_tracked_fingerprints;
      while (this.order.length > cap) {
        const evicted = this.order.shift();
        if (evicted) this.failures.delete(evicted);
      }
    }
    this.failures.set(record.fingerprint, record);
  }

  private forget(fp: string): void {
    this.failures.delete(fp);
    const idx = this.order.indexOf(fp);
    if (idx >= 0) this.order.splice(idx, 1);
  }

  /**
   * A -> B -> A -> B, all four failing. `cycle_length`/`cycle_repeats` from the policy
   * decide the window; the default is a 2-call cycle repeated twice.
   */
  private detectCycle(nextFp: string): number | null {
    const { cycle_length: len, cycle_repeats: reps } = this.policy.loop_guard;
    if (len < 2 || reps < 2) return null;
    const period = Math.max(2, Math.floor(len / reps));
    const need = period * reps;
    const recent = this.history.slice(-(need - 1));
    if (recent.length < need - 1) return null;
    const seq = [...recent.map((h) => h.fingerprint), nextFp];
    // The candidate cycle is the last `period` entries; everything before must repeat it.
    const tail = seq.slice(-period);
    if (new Set(tail).size !== period) return null;
    for (let block = 0; block < reps; block += 1) {
      const slice = seq.slice(seq.length - period * (block + 1), seq.length - period * block);
      if (slice.length !== period) return null;
      for (let i = 0; i < period; i += 1) if (slice[i] !== tail[i]) return null;
    }
    return need;
  }
}

/**
 * Duplicate-success ledger: refuse an identical mutating call that already succeeded while
 * nothing else mutated. The `generation` counter is what makes this safe - `edit` bumps it,
 * so `edit` -> `build` -> `edit` -> `build` is four legal calls, and only `build` -> `build`
 * with no edit in between is refused.
 */
export class SuccessLedger {
  private generation = 0;
  private seen = new Map<string, { generation: number; count: number; toolName: string }>();

  private policy: Policy;

  constructor(policy: Policy = DEFAULT_POLICY) {
    this.policy = policy;
  }

  reset(): void {
    this.generation = 0;
    this.seen.clear();
  }

  get currentGeneration(): number {
    return this.generation;
  }

  private isMutating(toolName: string): boolean {
    return this.policy.duplicate_success.tools.includes(toolName) || this.policy.duplicate_success.tools.includes(serverOf(toolName));
  }

  /** Does a success of this tool invalidate every recorded duplicate? */
  private bumpsGeneration(toolName: string): boolean {
    const list = this.policy.duplicate_success.generation_tools;
    return list.includes(toolName) || list.includes(serverOf(toolName));
  }

  before(input: FingerprintInput): GuardVerdict {
    if (!this.policy.duplicate_success.enabled) return { decision: "allow" };
    if (!this.isMutating(input.toolName)) return { decision: "allow" };
    const fp = fingerprint(input);
    const hit = this.seen.get(fp);
    if (hit && hit.generation === this.generation && hit.count >= this.policy.duplicate_success.max_duplicates) {
      const cls = classify("", this.policy, "DUPLICATE_SUCCESS");
      return {
        decision: "block",
        code: "DUPLICATE_SUCCESS",
        attempts: hit.count,
        retryable: false,
        message: `this exact ${input.toolName} call already succeeded in this state (generation ${this.generation}).`,
        next_action: cls.next_action,
      };
    }
    return { decision: "allow" };
  }

  after(input: FingerprintInput, isError: boolean): void {
    if (!this.policy.duplicate_success.enabled) return;
    if (isError) return;
    // Bump FIRST, then record against the new generation. A `write` therefore stores
    // itself at the version it produced, and a second identical write - which would
    // produce exactly the file that is already there - compares equal and is refused.
    // A `bash` between them advances the version, so the retry becomes legitimate again.
    if (this.bumpsGeneration(input.toolName)) this.generation += 1;
    if (!this.isMutating(input.toolName)) return;
    const fp = fingerprint(input);
    const hit = this.seen.get(fp);
    if (hit && hit.generation === this.generation) hit.count += 1;
    else this.seen.set(fp, { generation: this.generation, count: 1, toolName: input.toolName });
  }
}

// ---------------------------------------------------------------------------
// Progress guard
// ---------------------------------------------------------------------------

/**
 * Is this call pure inspection?
 *
 * `read`/`ls`/`grep`/`find` by name. `bash` by the command it runs: split on `&&`, `;`
 * and `|`, and require EVERY segment to start with a read-only word. `cd repo && sed -n
 * '1,60p' f` is inspection; `cd repo && python -c "..."` is not, because the model is
 * doing something rather than looking at something - and this guard must never be the
 * reason a working step is refused.
 */
export function isInspection(
  toolName: string,
  args: Record<string, unknown>,
  policy: Policy = DEFAULT_POLICY,
): boolean {
  const cfg = policy.progress_guard;
  if (cfg.inspection_tools.includes(toolName)) return true;
  if (toolName !== "bash" && toolName !== "powershell") return false;
  const command = typeof args.command === "string" ? args.command : "";
  if (!command.trim()) return false;
  const segments = command
    .split(/\|\||&&|;|\|/)
    .map((s) => s.trim())
    .filter((s) => s.length > 0);
  if (segments.length === 0) return false;
  return segments.every((segment) => {
    const lower = segment.toLowerCase();
    return cfg.inspection_bash_prefixes.some(
      (prefix) => lower === prefix || lower.startsWith(`${prefix} `),
    );
  });
}

/**
 * Blocks a session that has inspected a lot and produced nothing.
 *
 * The loop guard needs a REPEATED call. Measured live on the moon-exploration brief,
 * ornith-1.5-9b-uncensored made 46 consecutive `bash` inspection calls in 12 minutes -
 * every argument different, so no fingerprint ever repeated - and wrote zero files. The
 * only deterministic signal left is "nothing has been written at all", and that is what
 * this counts.
 *
 * Conservative on purpose: `require_zero_mutations` means the guard switches itself off
 * for the rest of the session the moment one non-inspection call succeeds. An agent that
 * has started producing is never interrupted.
 */
export class ProgressGuard {
  private inspections = 0;
  private mutations = 0;
  private blocked = 0;

  private policy: Policy;

  constructor(policy: Policy = DEFAULT_POLICY) {
    this.policy = policy;
  }

  reset(): void {
    this.inspections = 0;
    this.mutations = 0;
    this.blocked = 0;
  }

  get inspectionCount(): number {
    return this.inspections;
  }

  get mutationCount(): number {
    return this.mutations;
  }

  before(input: FingerprintInput, readOnly = false): GuardVerdict {
    const cfg = this.policy.progress_guard;
    if (!cfg.enabled) return { decision: "allow" };
    if (cfg.require_zero_mutations && this.mutations > 0) return { decision: "allow" };
    if (this.inspections < cfg.block_after_inspections) return { decision: "allow" };
    if (!readOnly && !isInspection(input.toolName, input.args, this.policy)) return { decision: "allow" };
    this.blocked += 1;
    const cls = classify("", this.policy, "NO_PROGRESS");
    return {
      decision: "block",
      code: "NO_PROGRESS",
      attempts: this.inspections,
      retryable: false,
      message:
        `${this.inspections} consecutive inspection calls and nothing written yet. ` +
        `More reading will not turn into a file.`,
      next_action: cls.next_action,
    };
  }

  /**
   * `readOnly` comes from the client, not from the policy: pi reports each tool's
   * `readOnlyHint`, and an MCP search tool declares it. Without that, `threejs_rag_search`
   * would look like a mutation, switch the guard off, and a RAG-heavy session would
   * circle unguarded - which is exactly what a 9B model does with a search tool.
   */
  after(input: FingerprintInput, isError: boolean, readOnly = false): void {
    const cfg = this.policy.progress_guard;
    if (!cfg.enabled) return;
    if (readOnly || isInspection(input.toolName, input.args, this.policy)) {
      this.inspections += 1;
      return;
    }
    this.inspections = 0;
    if (!isError) this.mutations += 1;
  }
}

// ---------------------------------------------------------------------------
// Write verification
// ---------------------------------------------------------------------------

export interface VerifyResult {
  ok: boolean;
  code?: ErrorCode;
  message?: string;
  bytes?: number;
}

/**
 * Check that a write/edit actually landed.
 *
 * `write` carries the full payload, so the byte count is comparable. `edit` only carries a
 * fragment, so the check is existence + a fresh mtime. Both are cheap and both catch the
 * real failure mode: the model announcing a save that never happened.
 */
export function verifyWrite(
  file: string,
  opts: { expectedBytes?: number; freshnessMs?: number; now?: number } = {},
  policy: Policy = DEFAULT_POLICY,
): VerifyResult {
  const freshness = opts.freshnessMs ?? policy.write_verification.mtime_freshness_ms;
  const now = opts.now ?? Date.now();
  let st;
  try {
    st = statSync(file);
  } catch {
    return { ok: false, code: "WRITE_NOT_VERIFIED", message: `the file does not exist after the call: ${file}` };
  }
  if (!st.isFile()) {
    return { ok: false, code: "WRITE_NOT_VERIFIED", message: `the target is not a regular file: ${file}` };
  }
  if (st.size === 0 && (opts.expectedBytes ?? 0) > 0) {
    return { ok: false, code: "WRITE_NOT_VERIFIED", message: `the file is empty after the call: ${file}` };
  }
  if (typeof opts.expectedBytes === "number" && opts.expectedBytes > 0 && st.size !== opts.expectedBytes) {
    return {
      ok: false,
      code: "WRITE_NOT_VERIFIED",
      message: `the file is ${st.size} bytes but ${opts.expectedBytes} were written: ${file}`,
      bytes: st.size,
    };
  }
  if (now - st.mtimeMs > freshness) {
    return {
      ok: false,
      code: "WRITE_NOT_VERIFIED",
      message: `the file was not modified by this call (mtime is ${Math.round((now - st.mtimeMs) / 1000)}s old): ${file}`,
      bytes: st.size,
    };
  }
  return { ok: true, bytes: st.size };
}

// ---------------------------------------------------------------------------
// Path guard
// ---------------------------------------------------------------------------

export interface PathVerdict {
  decision: "allow" | "block" | "warn";
  resolved: string;
  message?: string;
}

/** Absolute, symlink-free-enough path. `resolve` collapses `..` and `.` before the check. */
export function resolveToolPath(p: string, cwd: string): string {
  return isAbsolute(p) ? resolve(p) : resolve(cwd, p);
}

function inside(child: string, parent: string): boolean {
  const rel = relative(parent, child);
  return rel === "" || (!rel.startsWith("..") && !isAbsolute(rel));
}

/**
 * A mutating call outside the repository is a sandbox escape and is refused. Inside the
 * repository but outside the active project is a legitimate case (the repo's own tools,
 * docs, pi-extensions) and is only logged - blocking it would break editing the harness
 * itself, which is half of what this repository is for.
 */
export function checkPath(
  p: string,
  opts: { cwd: string; repo: string; project?: string | null },
  policy: Policy = DEFAULT_POLICY,
): PathVerdict {
  const resolved = resolveToolPath(p, opts.cwd);
  if (!policy.path_guard.enabled) return { decision: "allow", resolved };
  if (policy.path_guard.block_outside_repo && !inside(resolved, opts.repo)) {
    return {
      decision: "block",
      resolved,
      message: `${resolved} is outside the repository ${opts.repo}`,
    };
  }
  if (policy.path_guard.warn_outside_project && opts.project && !inside(resolved, opts.project)) {
    return { decision: "warn", resolved, message: `${resolved} is inside the repo but outside the active project` };
  }
  return { decision: "allow", resolved };
}

// ---------------------------------------------------------------------------
// Active project
// ---------------------------------------------------------------------------

export interface ProjectContext {
  repo: string;
  project: string | null;
  engine: string;
  engineSource: string;
  stale: string | null;
}

/**
 * Read `data/active_project.txt` and the nearest `engine.json`.
 *
 * Read on every call, never cached: a project can be created, renamed or deleted in the
 * middle of a session, and a cached answer is how the agent ends up writing into a
 * directory that no longer exists.
 */
export function readProjectContext(root: string = repoRoot()): ProjectContext {
  const marker = join(root, "data", "active_project.txt");
  let rel = "";
  try {
    rel = readFileSync(marker, "utf8").trim();
  } catch {
    rel = "";
  }
  if (!rel) return { repo: root, project: null, engine: "threejs", engineSource: "default", stale: null };
  const resolved = resolve(root, rel);
  let isDir = false;
  try {
    isDir = statSync(resolved).isDirectory();
  } catch {
    isDir = false;
  }
  if (!isDir) return { repo: root, project: null, engine: "threejs", engineSource: "default", stale: rel };

  // Walk up to the repo root for the nearest engine.json, exactly like project_layout.py.
  let here = resolved;
  while (true) {
    const engine = readEngineMarker(here);
    if (engine) return { repo: root, project: resolved, engine, engineSource: join(here, "engine.json"), stale: null };
    if (here === root || dirname(here) === here) break;
    here = dirname(here);
  }
  return { repo: root, project: resolved, engine: "threejs", engineSource: "default", stale: null };
}

function readEngineMarker(dir: string): string | null {
  const file = join(dir, "engine.json");
  if (!existsSync(file)) return null;
  try {
    // utf-8-sig equivalent: strip a BOM before parsing.
    const text = readFileSync(file, "utf8").replace(/^\uFEFF/, "");
    const data = JSON.parse(text) as { engine?: string };
    if (typeof data.engine !== "string") return null;
    const raw = data.engine.trim().toLowerCase();
    if (raw === "three") return "threejs";
    return raw;
  } catch {
    return null;
  }
}

// ---------------------------------------------------------------------------
// Structured events
// ---------------------------------------------------------------------------

export interface ReliabilityEvent {
  ts: string;
  run_id: string;
  client: string;
  engine?: string;
  project?: string;
  tool: string;
  server: string;
  fingerprint: string;
  elapsed_ms?: number;
  ok: boolean;
  error_code?: string;
  retry_count?: number;
  decision?: string;
  verification?: string;
  note?: string;
}

/**
 * Append one JSONL line and rotate when the file is too big.
 *
 * Never logs arguments, file contents or prompts - only the fingerprint hash, the tool
 * name and the classification. A log that contains the payload is a second copy of the
 * session, and this one has to stay safe to attach to a bug report.
 */
export class EventLog {
  private policy: Policy;
  private file: string | null = null;
  private dir: string;

  constructor(policy: Policy = DEFAULT_POLICY, root: string = repoRoot()) {
    this.policy = policy;
    // `GS_RELIABILITY_LOG_DIR` exists for tests: the wiring smoke test drives this class
    // for real, and its events must not land in the session log a human reads.
    const override = process.env.GS_RELIABILITY_LOG_DIR;
    const dir = override || policy.logging.dir;
    this.dir = isAbsolute(dir) ? dir : join(root, dir);
  }

  get path(): string {
    return this.file ?? join(this.dir, "unknown.jsonl");
  }

  write(event: ReliabilityEvent): void {
    if (!this.policy.logging.enabled) return;
    try {
      mkdirSync(this.dir, { recursive: true });
      this.file = join(this.dir, `${event.ts.slice(0, 10)}.jsonl`);
      this.rotateIfNeeded();
      appendFileSync(this.file, `${JSON.stringify(event)}\n`, "utf8");
    } catch {
      // Logging must never break a turn.
    }
  }

  private rotateIfNeeded(): void {
    if (!this.file) return;
    let size = 0;
    try {
      size = statSync(this.file).size;
    } catch {
      return;
    }
    if (size < this.policy.logging.max_bytes_per_file) return;
    const stamp = new Date().toISOString().replace(/[:.]/g, "-");
    const rotated = this.file.replace(/\.jsonl$/, `.${stamp}.jsonl`);
    try {
      renameSync(this.file, rotated);
    } catch {
      try {
        unlinkSync(this.file);
      } catch {
        /* ignore */
      }
    }
  }
}

/** Repo-relative POSIX path, so a log line is portable and leaks no absolute paths. */
export function repoRelative(root: string, p: string): string {
  const rel = relative(root, p);
  if (rel.startsWith("..") || isAbsolute(rel)) return p.split(sep).join("/");
  return rel.split(sep).join("/");
}

/**
 * The model-facing error contract (section 4.8 of the brief).
 *
 * Both pi and WorkBuddy read the text form; anything programmatic can parse the JSON.
 * `retryable: false` plus a concrete `next_action` is the whole point: a 9B model that is
 * told "this is not retryable, list the parent directory" changes strategy, while one
 * that sees a bare ENOENT calls `read` again.
 */
export function errorPayload(
  code: ErrorCode,
  operation: string,
  opts: { path?: string; message?: string; attempts?: number; extra?: Record<string, unknown> } = {},
  policy: Policy = DEFAULT_POLICY,
): string {
  const cls = classify("", policy, code);
  const body: Record<string, unknown> = {
    ok: false,
    error_code: code,
    retryable: cls.retryable,
    operation,
    message: opts.message ?? cls.next_action,
    next_action: cls.next_action,
  };
  if (opts.path) body.path = opts.path;
  if (typeof opts.attempts === "number") body.attempts = opts.attempts;
  if (opts.extra) Object.assign(body, opts.extra);
  return JSON.stringify(body);
}
