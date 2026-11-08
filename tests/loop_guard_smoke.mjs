/**
 * Wiring smoke test for pi-extensions/loop-guard.ts.
 *
 * The parity harness tests the core as a library. This one drives the extension the way
 * pi does: a fake `ExtensionAPI` records the handlers, and the test fires `tool_call` /
 * `tool_result` at them with real files on disk. That is the only way to catch a wiring
 * bug - a handler registered for the wrong event, a block that never returns, a
 * verification that inspects the wrong path - none of which the core tests can see.
 *
 * It covers scenarios 1-6 of the brief at the boundary where they actually matter:
 *
 *   1. an existing file in the right project reads cleanly
 *   2. a missing file yields FILE_NOT_FOUND plus a usable recovery hint
 *   3. the identical failing read is then blocked
 *   4. a write that landed passes verification
 *   5. a write that "succeeded" without touching the disk is WRITE_NOT_VERIFIED
 *   6. a write outside the repository is refused
 *
 *   node tests/loop_guard_smoke.mjs
 */
import { existsSync, mkdirSync, mkdtempSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";

const REPO = resolve(import.meta.dirname, "..");
process.env.GS_ROOT = REPO;

// The extension logs every event it sees. Point that at the throwaway directory, so a
// test run never becomes the "last run" a human reads in `gs reliability`.
const logDir = join(REPO, "output", `loopguard-log-${process.pid}`);
process.env.GS_RELIABILITY_LOG_DIR = logDir;

const { default: loopGuard } = await import("../pi-extensions/loop-guard.ts");

/** Minimal stand-in for pi's ExtensionAPI: collects handlers, nothing else. */
function fakePi(tools = []) {
  const handlers = new Map();
  return {
    api: {
      on(event, handler) {
        handlers.set(event, handler);
      },
      getAllTools() {
        return tools;
      },
    },
    fire(event, payload) {
      const handler = handlers.get(event);
      if (!handler) throw new Error(`no handler registered for ${event}`);
      return handler(payload);
    },
    has(event) {
      return handlers.has(event);
    },
  };
}

const failures = [];
function check(name, condition, detail) {
  if (condition) return;
  failures.push(`${name}: ${detail}`);
}

// A read-only MCP tool, exactly as pi reports one: the progress guard has to treat it as
// inspection, or a search-heavy session switches the guard off after the first query.
const pi = fakePi([
  { name: "read", annotations: { readOnlyHint: true } },
  { name: "mcp__threejs_rag__threejs_rag_search", annotations: { readOnlyHint: true } },
  { name: "write", annotations: { readOnlyHint: false } },
]);
loopGuard(pi.api);
pi.fire("session_start", {});

check("session_start registers tool_call", pi.has("tool_call"), "no tool_call handler");
check("session_start registers tool_result", pi.has("tool_result"), "no tool_result handler");

// The work directory lives INSIDE the repo on purpose: a write outside it is refused by
// the sandbox, which is the subject of scenario 6, not something to trip over here.
// `output/` is gitignored, so a crashed run leaves nothing tracked behind.
const workRoot = join(REPO, "output");
mkdirSync(workRoot, { recursive: true });
const work = mkdtempSync(join(workRoot, "loopguard-smoke-"));
const project = join(REPO, "projects", "three", "test-space");
const existing = join(project, "engine.json");
const missing = join(project, "definitely-not-here.ts");
const target = join(work, "written.txt");

const textOf = (result) => (result?.content ?? []).map((p) => p.text ?? "").join("\n");

// --- 1. an existing file: nothing to block ---------------------------------
const readCall = { type: "tool_call", toolCallId: "c1", toolName: "read", input: { path: existing } };
check("existing file is not blocked", !pi.fire("tool_call", readCall)?.block, "the read was blocked");
pi.fire("tool_result", {
  type: "tool_result",
  toolCallId: "c1",
  toolName: "read",
  input: { path: existing },
  content: [{ type: "text", text: '{"engine":"threejs"}' }],
  isError: false,
});

// --- 2. a missing file: FILE_NOT_FOUND + recovery hint ----------------------
const missCall = { type: "tool_call", toolCallId: "c2", toolName: "read", input: { path: missing } };
check("a missing file is not pre-emptively blocked", !pi.fire("tool_call", missCall)?.block, "blocked before the first attempt");
const missResult = pi.fire("tool_result", {
  type: "tool_result",
  toolCallId: "c2",
  toolName: "read",
  input: { path: missing },
  content: [{ type: "text", text: "ENOENT: no such file or directory, open 'definitely-not-here.ts'" }],
  isError: true,
});
const missText = textOf(missResult);
let missPayload = null;
try {
  missPayload = JSON.parse(missText.slice(missText.indexOf("{")));
} catch {
  missPayload = null;
}
check("the error carries a parseable contract", missPayload !== null, `payload was: ${missText.slice(0, 200)}`);
if (missPayload) {
  check("the code is FILE_NOT_FOUND", missPayload.error_code === "FILE_NOT_FOUND", missPayload.error_code);
  check("it is not retryable", missPayload.retryable === false, String(missPayload.retryable));
  check("it names a next action", typeof missPayload.next_action === "string" && missPayload.next_action.length > 10, "no next_action");
  check(
    "it lists what IS in the directory",
    Array.isArray(missPayload.entries) && missPayload.entries.includes("engine.json"),
    `entries=${JSON.stringify(missPayload.entries)}`,
  );
}

// --- 3. the identical failing read is blocked -------------------------------
const repeat = pi.fire("tool_call", { ...missCall, toolCallId: "c3" });
check("the identical retry is blocked", repeat?.block === true, "the repeat was allowed through");
if (repeat?.block) {
  const payload = JSON.parse(repeat.reason.slice(repeat.reason.indexOf("{")));
  check("the block names REPEATED_TOOL_CALL", payload.error_code === "REPEATED_TOOL_CALL", payload.error_code);
  check("the block is not retryable", payload.retryable === false, String(payload.retryable));
}

// --- 4. a write that landed passes verification -----------------------------
const content = "hello moon\n";
writeFileSync(target, content, "utf8");
const writeCall = { type: "tool_call", toolCallId: "c4", toolName: "write", input: { path: target, content } };
check("an in-repo write is not blocked", !pi.fire("tool_call", writeCall)?.block, "a legitimate write was blocked");
const writeResult = pi.fire("tool_result", {
  type: "tool_result",
  toolCallId: "c4",
  toolName: "write",
  input: { path: target, content },
  content: [{ type: "text", text: "wrote 11 bytes" }],
  isError: false,
});
check("a verified write stays a success", !writeResult?.isError, "a real write was marked as failed");

// --- 5. a write that claims success without landing -------------------------
const ghost = join(work, "never-written.txt");
const ghostResult = pi.fire("tool_result", {
  type: "tool_result",
  toolCallId: "c5",
  toolName: "write",
  input: { path: ghost, content: "does not exist\n" },
  content: [{ type: "text", text: "wrote 15 bytes" }],
  isError: false,
});
check("a write that did not land is an error", ghostResult?.isError === true, "the claim was accepted");
check(
  "it is WRITE_NOT_VERIFIED",
  textOf(ghostResult).includes("WRITE_NOT_VERIFIED"),
  textOf(ghostResult).slice(0, 200),
);

// --- 6. a write outside the repository is refused ---------------------------
const outside = join(tmpdir(), "gs-outside-the-repo.txt");
const outsideCall = { type: "tool_call", toolCallId: "c6", toolName: "write", input: { path: outside, content: "x" } };
const outsideVerdict = pi.fire("tool_call", outsideCall);
check("a write outside the repo is blocked", outsideVerdict?.block === true, "the sandbox did not hold");
check(
  "the refusal names PATH_OUTSIDE_SANDBOX",
  (outsideVerdict?.reason ?? "").includes("PATH_OUTSIDE_SANDBOX"),
  outsideVerdict?.reason?.slice(0, 200),
);

// --- 7. an identical successful write is a duplicate ------------------------
// The same call again, with the file still exactly as that write left it.
const dupCall = { type: "tool_call", toolCallId: "c7", toolName: "write", input: { path: target, content } };
const dupVerdict = pi.fire("tool_call", dupCall);
check("an identical repeat write is blocked", dupVerdict?.block === true, "the duplicate was allowed");
check(
  "the refusal names DUPLICATE_SUCCESS",
  (dupVerdict?.reason ?? "").includes("DUPLICATE_SUCCESS"),
  dupVerdict?.reason?.slice(0, 200),
);

// --- 8. the same compiler error, three times, through three different calls ----
// The shape neither of the other guards can see: fingerprints all new, files already
// written. A `bash` that exits 0 but prints a TS error still counts as the same error.
const tscError = "src/globals.d.ts(16,9): error TS1003: Identifier expected.";
const tscCalls = [
  { type: "tool_call", toolCallId: "e1", toolName: "bash", input: { command: "sed -n '10,20p' src/globals.d.ts" } },
  { type: "tool_call", toolCallId: "e2", toolName: "bash", input: { command: "grep -n 'class Vector' src/globals.d.ts" } },
  { type: "tool_call", toolCallId: "e3", toolName: "bash", input: { command: "head -20 src/globals.d.ts" } },
];
for (const [index, call] of tscCalls.entries()) {
  pi.fire("tool_call", call);
  pi.fire("tool_result", {
    type: "tool_result",
    toolCallId: call.toolCallId,
    toolName: "bash",
    input: call.input,
    content: [{ type: "text", text: tscError }],
    isError: false,
    timestamp: Date.now() + index,
  });
}
const repeatCall = {
  type: "tool_call",
  toolCallId: "e4",
  toolName: "bash",
  input: { command: "awk 'NR==16' src/globals.d.ts" },
};
const repeatVerdict = pi.fire("tool_call", repeatCall);
check("the fourth pass at one error is blocked", repeatVerdict?.block === true, "the loop was allowed");
check(
  "the refusal names ERROR_REPEAT",
  (repeatVerdict?.reason ?? "").includes("ERROR_REPEAT"),
  repeatVerdict?.reason?.slice(0, 200),
);

pi.fire("session_shutdown", {});

rmSync(work, { recursive: true, force: true });
rmSync(logDir, { recursive: true, force: true });
if (existsSync(outside)) rmSync(outside, { force: true });

if (failures.length) {
  for (const failure of failures) console.log("FAIL", failure);
  console.log(`\n${failures.length} check(s) failed`);
  process.exit(1);
}
console.log("PASS loop-guard wiring: 8 scenarios, all checks passed");
