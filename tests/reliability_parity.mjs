/**
 * Parity harness: run the TypeScript reliability core under plain node and print its
 * answers as JSON, so tests/test_reliability.py can diff them against the Python twin.
 *
 * Why this exists: the live guard is TypeScript (it runs inside pi) and everything else is
 * Python, so the same policy is implemented twice. Two implementations of one policy is a
 * bug waiting to happen - unless something runs both on the same fixture and compares.
 *
 * Node 22 strips TypeScript types natively, so there is no build step and no dependency.
 *
 *   node tests/reliability_parity.mjs
 */
import {
  LoopGuard,
  ProgressGuard,
  SuccessLedger,
  classify,
  fingerprint,
  isInspection,
  loadPolicy,
  stableStringify,
} from "../pi-extensions/reliability-core.ts";

const policy = loadPolicy();

/** Same list as the Python test. If one side gains a case, both do - that is the point. */
const CLASSIFY_CASES = [
  "No such file or directory: world.ts",
  "ENOENT: no such file or directory, open 'x.ts'",
  "EACCES: permission denied, open 'x'",
  "connect ECONNREFUSED 127.0.0.1:8080",
  "the response hit the output token limit",
  "error TS2322: Type 'string' is not assignable to type 'number'",
  "invalid argument: expected string, got number",
  "operation timed out after 300s",
  "EISDIR: illegal operation on a directory, read",
  "write refused: path escapes the sandbox",
  "something entirely new happened",
  "",
];

const classification = CLASSIFY_CASES.map((text) => ({ text, ...classify(text, policy) }));

/** Fingerprint fixtures: key order must not matter, values must. */
const FINGERPRINTS = [
  { toolName: "read", args: { path: "a.ts", limit: 10 }, context: "projects/three/x" },
  { toolName: "read", args: { limit: 10, path: "a.ts" }, context: "projects/three/x" },
  { toolName: "read", args: { path: "a.ts", limit: 20 }, context: "projects/three/x" },
  { toolName: "read", args: { path: "a.ts", limit: 10 }, context: "projects/three/y" },
  { toolName: "rbx-project__read_file", args: { path: "src/init.luau" }, context: "" },
  { toolName: "edit", args: { path: "a.ts", edits: [{ oldText: "x", newText: "y" }] }, context: "" },
  { toolName: "edit", args: { edits: [{ newText: "y", oldText: "x" }], path: "a.ts" }, context: "" },
];

const fingerprints = FINGERPRINTS.map((f) => fingerprint(f));

/**
 * Guard scenarios. Each one is a list of steps; `after` records an outcome, `before`
 * asks for a verdict. The last verdict of each scenario is what gets compared.
 */
function runScenario(steps) {
  const guard = new LoopGuard(policy);
  let verdict = null;
  for (const step of steps) {
    if (step.op === "after") guard.after(step.call, step.isError, step.code ?? null);
    else if (step.op === "before") verdict = guard.before(step.call);
    else if (step.op === "reset") guard.resetOnMutation();
  }
  return verdict ? { decision: verdict.decision, code: verdict.code ?? null } : null;
}

const call = (toolName, args, context = "") => ({ toolName, args, context });
const readA = call("read", { path: "a.ts" });
const readB = call("read", { path: "b.ts" });
const grepX = call("grep", { pattern: "x" });
const bashBuild = call("bash", { command: "npm run build" });

const SCENARIOS = {
  identical_hard_failure: [
    { op: "after", call: readA, isError: true, code: "FILE_NOT_FOUND" },
    { op: "before", call: readA },
  ],
  different_path_after_failure: [
    { op: "after", call: readA, isError: true, code: "FILE_NOT_FOUND" },
    { op: "before", call: readB },
  ],
  transient_budget: [
    { op: "after", call: bashBuild, isError: true, code: "TIMEOUT" },
    { op: "after", call: bashBuild, isError: true, code: "TIMEOUT" },
    { op: "before", call: bashBuild },
  ],
  transient_exhausted: [
    { op: "after", call: bashBuild, isError: true, code: "TIMEOUT" },
    { op: "after", call: bashBuild, isError: true, code: "TIMEOUT" },
    { op: "after", call: bashBuild, isError: true, code: "TIMEOUT" },
    { op: "before", call: bashBuild },
  ],
  cycle_abab: [
    { op: "after", call: readA, isError: true, code: "FILE_NOT_FOUND" },
    { op: "after", call: grepX, isError: true, code: "INVALID_ARGUMENT" },
    { op: "after", call: readA, isError: true, code: "FILE_NOT_FOUND" },
    { op: "before", call: grepX },
  ],
  not_a_cycle: [
    { op: "after", call: readA, isError: true, code: "FILE_NOT_FOUND" },
    { op: "after", call: grepX, isError: true, code: "INVALID_ARGUMENT" },
    { op: "after", call: readB, isError: true, code: "FILE_NOT_FOUND" },
    { op: "before", call: call("grep", { pattern: "y" }) },
  ],
  success_clears_counters: [
    { op: "after", call: readA, isError: true, code: "FILE_NOT_FOUND" },
    { op: "after", call: readA, isError: false },
    { op: "before", call: readA },
  ],
  mutation_clears_counters: [
    { op: "after", call: readA, isError: true, code: "FILE_NOT_FOUND" },
    { op: "reset" },
    { op: "before", call: readA },
  ],
};

const scenarios = Object.fromEntries(
  Object.entries(SCENARIOS).map(([name, steps]) => [name, runScenario(steps)]),
);

/**
 * Duplicate-success scenarios. `gen` steps only bump the state version (a successful
 * `bash`), so the ledger has to see them without recording them as duplicates.
 */
function runLedger(steps) {
  const ledger = new SuccessLedger(policy);
  let verdict = null;
  for (const step of steps) {
    if (step.op === "after") ledger.after(step.call, step.isError ?? false);
    else verdict = ledger.before(step.call);
  }
  return verdict ? { decision: verdict.decision, code: verdict.code ?? null } : null;
}

const writeA = call("write", { path: "a.ts", content: "x" });
const editA = call("edit", { path: "a.ts", edits: [{ oldText: "x", newText: "y" }] });

const LEDGER_SCENARIOS = {
  write_twice: [
    { op: "after", call: writeA },
    { op: "before", call: writeA },
  ],
  write_bash_write: [
    { op: "after", call: writeA },
    { op: "after", call: bashBuild },
    { op: "before", call: writeA },
  ],
  bash_twice_is_allowed: [
    { op: "after", call: bashBuild },
    { op: "before", call: bashBuild },
  ],
  edit_after_write_is_a_different_call: [
    { op: "after", call: writeA },
    { op: "before", call: editA },
  ],
  a_failed_write_records_nothing: [
    { op: "after", call: writeA, isError: true },
    { op: "before", call: writeA },
  ],
};

const ledger = Object.fromEntries(
  Object.entries(LEDGER_SCENARIOS).map(([name, steps]) => [name, runLedger(steps)]),
);

/** Inspection classification fixtures - the input to the progress guard. */
const INSPECTION_CASES = [
  ["read", { path: "a.ts" }],
  ["ls", { path: "." }],
  ["grep", { pattern: "x" }],
  ["bash", { command: "ls -la" }],
  ["bash", { command: "cd projects/three/x && sed -n '1,60p' file.ts" }],
  ["bash", { command: "cat a && grep -n x b" }],
  ["bash", { command: "npm run build" }],
  ["bash", { command: "cd repo && python -c \"print(1)\"" }],
  ["bash", { command: "ls && npm install" }],
  ["write", { path: "a.ts", content: "x" }],
  ["bash", { command: "" }],
];

const inspection = INSPECTION_CASES.map(([tool, args]) => ({
  tool,
  args,
  inspection: isInspection(tool, args, policy),
}));

/** Progress scenarios: N inspections, then one more inspection, then a write. */
function runProgress(steps) {
  const guard = new ProgressGuard(policy);
  let verdict = null;
  for (const step of steps) {
    if (step.op === "after") guard.after(step.call, step.isError ?? false, step.readOnly ?? false);
    else verdict = guard.before(step.call, step.readOnly ?? false);
  }
  return verdict ? { decision: verdict.decision, code: verdict.code ?? null } : null;
}

const inspect = call("bash", { command: "ls -la projects/three/test-space" });
const inspectAgain = call("bash", { command: "sed -n '1,40p' a.ts" });
const writes = call("write", { path: "a.ts", content: "x" });

const many = (n, c) => Array.from({ length: n }, () => ({ op: "after", call: c }));

const progress = {
  blocks_after_the_budget: runProgress([
    ...many(policy.progress_guard.block_after_inspections, inspect),
    { op: "before", call: inspectAgain },
  ]),
  allows_a_write_after_the_budget: runProgress([
    ...many(policy.progress_guard.block_after_inspections, inspect),
    { op: "before", call: writes },
  ]),
  silent_before_the_budget: runProgress([
    ...many(policy.progress_guard.block_after_inspections - 1, inspect),
    { op: "before", call: inspectAgain },
  ]),
  stops_counting_once_something_was_written: runProgress([
    { op: "after", call: writes },
    ...many(policy.progress_guard.block_after_inspections + 5, inspect),
    { op: "before", call: inspectAgain },
  ]),
  // A read-only MCP tool (readOnlyHint) counts as inspection even though its name is not
  // in the policy's list - otherwise a search-heavy session disables the guard.
  read_only_mcp_tool_counts_as_inspection: runProgress([
    ...Array.from({ length: policy.progress_guard.block_after_inspections }, () => ({
      op: "after",
      call: call("mcp__threejs_rag__threejs_rag_search", { query: "terrain" }),
      readOnly: true,
    })),
    { op: "before", call: call("mcp__threejs_rag__threejs_rag_search", { query: "craters" }), readOnly: true },
  ]),
  // A non-write MCP tool used to count as progress and disarm the guard. Now it is
  // neutral: the guard keeps counting and still blocks. Live evidence - `node --version`
  // and `python tool.py --help` did this on the moon-exploration run.
  a_non_write_tool_is_neutral_and_does_not_disarm_the_guard: runProgress([
    ...many(policy.progress_guard.block_after_inspections, inspect),
    { op: "after", call: call("mcp__assets__asset_image", { prompt: "moon" }), readOnly: false },
    { op: "after", call: call("bash", { command: "node --version" }), readOnly: false },
    { op: "before", call: inspectAgain },
  ]),
  a_failed_write_is_not_progress: runProgress([
    ...many(policy.progress_guard.block_after_inspections, inspect),
    { op: "after", call: writes, isError: true },
    { op: "before", call: inspectAgain },
  ]),
};

process.stdout.write(
  JSON.stringify(
    {
      policy_source: "mcp/reliability.json",
      stable_stringify: stableStringify({ b: 1, a: [2, { d: 4, c: 3 }] }),
      classification,
      fingerprints,
      scenarios,
      ledger,
      inspection,
      progress,
    },
    null,
    2,
  ) + "\n",
);
