/**
 * `@file` in a user message is an IDE convention, not a pi feature.
 *
 * Observed live, 2026-11-08, session `01a1bbee`, project `projects/three/test-space`:
 * the user typed `выполни @moon_exploration_site_prompt.md`, the token reached the model
 * verbatim, and the model built the path itself -
 *
 *     read { path: "F:/.../test-space/@moon_exploration_site_prompt.md" }
 *     -> ENOENT: no such file or directory, access 'F:\...\test-space\@moon_...md'
 *
 * pi's own path helper does strip a leading `@` (`stripAtPrefix` in utils/paths.js), but
 * only a LEADING one. As soon as the model prepends the cwd, the `@` sits in the middle of
 * the string, survives normalization, and the read fails. On a local 9B model that costs a
 * whole turn: it re-ran `ls`, noticed the real name, and read the file on the second try -
 * 90 seconds to recover from a character.
 *
 * So the repair happens where it is cheap: before the tool runs. Every path argument of the
 * file tools loses a segment-leading `@` **only if the corrected path exists on disk**, so a
 * file that is genuinely named `@something` (npm scopes, `@types`, a literal `@` in a name)
 * is never rewritten into a path that does not exist.
 *
 * Bash is deliberately NOT touched: a command line can hold `@` for a dozen legitimate
 * reasons (scp targets, npm scopes, here-docs), and rewriting it blindly breaks more than it
 * fixes.
 *
 * Why an extension and not a prompt rule: the failure is mechanical and happens before the
 * model can read any instruction. Telling a 9B model "remember that @ is not part of the
 * filename" does not survive a 22k-token context; removing the `@` does.
 */
import { existsSync } from "node:fs";
import { resolve } from "node:path";

/** Tools whose `path` argument is a single filesystem path. */
const PATH_TOOLS = new Set(["read", "ls", "find", "grep", "write", "edit"]);

/**
 * Drop a segment-leading `@` from `p` when the result exists. Returns null when there is
 * nothing to fix, which is the common case and must stay a no-op.
 */
export function fixAtPath(p: string, cwd: string): string | null {
  if (!p || !p.includes("@")) return null;
  const cut = Math.max(p.lastIndexOf("/"), p.lastIndexOf("\\"));
  const head = p.slice(0, cut + 1);
  const tail = p.slice(cut + 1);
  if (!tail.startsWith("@") || tail.length < 2) return null;
  const fixed = head + tail.slice(1);
  return existsSync(resolve(cwd, fixed)) ? fixed : null;
}

interface ToolCallEvent {
  toolName: string;
  input: Record<string, unknown>;
}

interface ExtensionApi {
  on(event: "session_start", handler: () => void): void;
  on(
    event: "tool_call",
    handler: (event: ToolCallEvent) => void,
  ): void;
}

export default function atMention(pi: ExtensionApi): void {
  let cwd = process.cwd();

  pi.on("session_start", () => {
    cwd = process.cwd();
  });

  pi.on("tool_call", (event) => {
    if (!PATH_TOOLS.has(event.toolName)) return;
    const input = event.input ?? {};
    const raw = typeof input.path === "string" ? input.path : "";
    const fixed = fixAtPath(raw, cwd);
    if (fixed) input.path = fixed;
  });
}
