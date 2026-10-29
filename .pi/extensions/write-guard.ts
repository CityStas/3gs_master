/**
 * Guards against the two ways a `write` call loses a whole turn in this repo.
 *
 * Both were observed live in session `01a116ba` and cost minutes of local 9B inference
 * each time, because the turn is thrown away *after* the model has already generated.
 *
 * 1. Oversized write. The response shares a 12288-token ceiling (`maxTokens` in
 *    `pi-home/models.json`) with the thinking block, and JSON string escaping costs
 *    roughly one token per three characters. A 432-line `World.ts` (~28 KB) sat exactly
 *    on that edge and came back as `the response hit the output token limit`, with the
 *    arguments truncated and the file never written. Blocking it up front costs one
 *    tool result instead of a full generation.
 *
 * 2. Rewrite loop. `GlideSystem.ts` was rewritten four times and each attempt
 *    reintroduced the same name collision (a private field `isGliding` alongside a
 *    method `isGliding()`), because a full `write` regenerates every line and carries
 *    nothing over from the attempt before it. After the third rewrite of one path the
 *    loop is not converging, and the useful instruction is "read it and patch it".
 *
 * A blocked call returns an error tool result carrying `reason`, which the model sees
 * verbatim - so each message below says what to do next, not just that it failed.
 *
 * Tune the three constants to taste; they are the whole policy.
 */

/** Content larger than this is refused: it will not fit the response budget. */
const MAX_BYTES = 12000;

/** Same limit expressed in lines, which is what a model can actually count. */
const MAX_LINES = 320;

/** Allow this many rewrites of one path, then insist on `edit` instead. */
const MAX_REWRITES = 3;

interface ToolCallEvent {
  toolName: string;
  input: Record<string, unknown>;
}

interface ToolCallResult {
  block?: boolean;
  reason?: string;
}

interface ExtensionApi {
  on(event: "session_start", handler: () => void): void;
  on(event: "tool_call", handler: (event: ToolCallEvent) => ToolCallResult | void): void;
}

export default function writeGuard(pi: ExtensionApi): void {
  /** path -> number of `write` attempts this session. */
  const attempts = new Map<string, number>();

  pi.on("session_start", () => attempts.clear());

  pi.on("tool_call", (event) => {
    if (event.toolName !== "write") return;

    const input = event.input ?? {};
    const target = typeof input.path === "string" ? input.path : "";
    const content = typeof input.content === "string" ? input.content : "";
    if (content === "") return;

    const lines = content.split("\n").length;
    const bytes = new TextEncoder().encode(content).length;

    if (bytes > MAX_BYTES || lines > MAX_LINES) {
      return {
        block: true,
        reason:
          `write refused: ${lines} lines / ${bytes} bytes is over the budget for a single call ` +
          `(${MAX_LINES} lines / ${MAX_BYTES} bytes).\n` +
          `The response shares a 12288-token ceiling with your thinking, so a file this size ` +
          `gets truncated and the call is rejected outright - the whole turn is lost.\n` +
          `Split it: write the file with its imports, types and first class, then append the ` +
          `remainder with edit calls. Do not retry this write unchanged.`,
      };
    }

    // Only successful, in-budget writes count toward the rewrite loop.
    const seen = (attempts.get(target) ?? 0) + 1;
    attempts.set(target, seen);
    if (seen > MAX_REWRITES) {
      return {
        block: true,
        reason:
          `write refused: this is attempt #${seen} to rewrite ${target} from scratch in this session.\n` +
          `Rewriting a file regenerates every line, so fixes from the previous attempt do not ` +
          `carry over - that is how the same bug survives three rewrites.\n` +
          `read ${target}, find the exact line that is wrong, and change only that line with edit.`,
      };
    }
    return;
  });
}
