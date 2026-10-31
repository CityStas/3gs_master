/**
 * Engine gate: exposes only the MCP servers of the engine the active project declares.
 *
 * The active project is read from data/active_project.txt (written by agent.cmd), and its
 * engine from <project>/engine.json. Four engines, four surfaces:
 *
 *   threejs (default) - nothing is registered here. `threejs-rag` and `assets` come from
 *                       pi-home-three/mcp.json, which is the profile agent.cmd picks.
 *   godot             - MCP server `godot` (gdmaster stack) when the Godot stack is runnable,
 *                       plus `godot-ai` (editor bridge) while something listens on :8001.
 *   unity             - MCP servers `unity-rag` and `unity-project` (unimaster stack), plus
 *                       `assets` pointed at <project>/Assets/Generated, plus `unity-editor`
 *                       (the official Unity MCP bridge) while the editor has the project open.
 *   roblox            - nothing is registered here either: `rbx-rag`, `rbx-project`,
 *                       `roblox-studio` (Studio's own MCP server) and `assets` all come from
 *                       pi-home-roblox/mcp.json. What this gate adds is the *check* - the
 *                       one failure mode of that profile is a Studio MCP server that is
 *                       installed but has nothing to talk to, and it must be named on
 *                       stderr instead of looking like a broken agent.
 *
 * Skills and the system prompt are NOT handled here: they live in the engine profile
 * (pi-home-three / pi-home-godot / pi-home-unity / pi-home-roblox), chosen by agent.cmd
 * via PI_CODING_AGENT_DIR.
 *
 * Why an extension and not a prompt rule: a model reads "do not use godot_* tools" and
 * still sees them in its tool list. Registering the server only when it applies removes
 * the tools from the list, so the wrong API cannot be called at all.
 *
 * A missing stack (no venv, no folder) skips that engine's server and writes a warning to
 * stderr. Nothing else fails.
 *
 * **A pointer is a hint, never a fact.** `projects/games/` is user data: games get created,
 * renamed and deleted while `data/active_project.txt` still names the old one. So the
 * marker is validated on every session start, and a DEAD one is reported instead of being
 * resolved into a path that is not on disk. Without that check `readEngine` returned null
 * for a deleted project and the gate silently selected engine=threejs - the wrong tool
 * surface, with nothing on stderr to say so.
 */
import { existsSync, readFileSync, statSync } from "node:fs";
import { connect } from "node:net";
import { join, resolve } from "node:path";

interface RegisteredServerConfig {
  command: string;
  args: string[];
  cwd: string;
  env: Record<string, string>;
  exposure: "direct" | "deferred" | "hidden" | "codemode";
  timeout: number;
  description: string;
}

interface ExtensionApi {
  on(event: "session_start", handler: () => void | Promise<void>): void;
  on(
    event: "resources_discover",
    handler: () => { skillPaths?: string[] },
  ): void;
  registerMcpServer(name: string, config: RegisteredServerConfig): void;
  unregisterMcpServer(name: string): void;
}

const GODOT_NAME = "godot";
const GODOT_AI_NAME = "godot-ai";
const GODOT_AI_PORT = 8001;
const UNITY_RAG_NAME = "unity-rag";
const UNITY_PROJECT_NAME = "unity-project";
const UNITY_EDITOR_NAME = "unity-editor";
const ASSETS_NAME = "assets";

/**
 * Repo root. pi starts in the repo root (agent.cmd does cd /d), so cwd is the anchor.
 * GS_ROOT overrides it when a session is started from somewhere else.
 */
const REPO = resolve(process.env.GS_ROOT ?? process.cwd());
const GODOT_HOME = join(REPO, "godot");
const UNITY_HOME = join(REPO, "unity");
/** The shared venv: `threejs` and `unimaster` both run from it (mcp + numpy only). */
const VENV_PY = process.env.UNITY_PYTHON ?? join(REPO, ".venv", "Scripts", "python.exe");

/**
 * x_life is the one project whose skill is scoped to the PROJECT, not to the engine: it is
 * a research project that happens to use Three.js, and its rules (a creature with no tools,
 * a from-scratch plastic core, a hash-chained lineage) are meaningless in any other
 * Three.js session. So the skill is contributed here, only while that project is active,
 * instead of being copied into `pi-home-three/skills/` where every game would inherit it.
 */
const XLIFE_PROJECT = join(REPO, "projects", "research", "x_life");
const XLIFE_SKILLS = join(REPO, "x_life_arch", "skills");

type Engine = "godot" | "unity" | "roblox" | "threejs";

function readEngine(projectDir: string): string | null {
  const file = join(projectDir, "engine.json");
  if (!existsSync(file)) return null;
  try {
    const data = JSON.parse(readFileSync(file, "utf8"));
    return typeof data.engine === "string" ? data.engine.toLowerCase() : null;
  } catch {
    return null;
  }
}

function isDirectory(p: string): boolean {
  try {
    return statSync(p).isDirectory();
  } catch {
    return false;
  }
}

/**
 * The active project, resolved from the canonical marker.
 *
 * Returns `path: null, stale: null` when there is no marker (a plain three.js session is a
 * legitimate state), and `path: null, stale: "<raw text>"` when the marker names something
 * that is not a directory - i.e. the project was deleted or renamed. `isDirectory`, not
 * `exists`: a FILE that happens to carry the project's name must not be taken for it.
 */
function activeProject(): { path: string | null; stale: string | null } {
  const marker = join(REPO, "data", "active_project.txt");
  if (!existsSync(marker)) return { path: null, stale: null };
  let rel = "";
  try {
    rel = readFileSync(marker, "utf8").trim();
  } catch {
    return { path: null, stale: null };
  }
  if (!rel) return { path: null, stale: null };
  // `resolve(REPO, rel)` leaves an absolute `rel` alone - same rule as the Python stacks.
  const resolved = resolve(REPO, rel);
  if (!isDirectory(resolved)) return { path: null, stale: rel };
  return { path: resolved, stale: null };
}

/** True if something accepts TCP on 127.0.0.1:port within timeoutMs. */
function portOpen(port: number, timeoutMs = 500): Promise<boolean> {
  return new Promise((done) => {
    const sock = connect({ host: "127.0.0.1", port });
    const finish = (ok: boolean) => {
      sock.destroy();
      done(ok);
    };
    sock.once("connect", () => finish(true));
    sock.once("error", () => finish(false));
    sock.setTimeout(timeoutMs, () => finish(false));
  });
}

function activeEngine(): { project: string | null; engine: Engine; stale: string | null } {
  const { path, stale } = activeProject();
  if (stale) {
    process.stderr.write(
      `[engine-gate] the active project is STALE: data/active_project.txt points at ` +
        `"${stale}", which does not exist - the project was deleted or renamed. ` +
        `No engine servers are registered for it. Re-run \`dev.cmd <name>\` or ` +
        `\`agent.cmd <project>\` to point the system at a live project.\n`,
    );
    return { project: null, engine: "threejs", stale };
  }
  const engine = path ? readEngine(path) : null;
  if (engine === "godot") return { project: path, engine: "godot", stale: null };
  if (engine === "unity") return { project: path, engine: "unity", stale: null };
  if (engine === "roblox") return { project: path, engine: "roblox", stale: null };
  return { project: path, engine: "threejs", stale: null };
}

/** Drop every server this extension can register, so a session never inherits another engine's. */
function clearAll(pi: ExtensionApi): void {
  pi.unregisterMcpServer(GODOT_NAME);
  pi.unregisterMcpServer(GODOT_AI_NAME);
  pi.unregisterMcpServer(UNITY_RAG_NAME);
  pi.unregisterMcpServer(UNITY_PROJECT_NAME);
  pi.unregisterMcpServer(UNITY_EDITOR_NAME);
  pi.unregisterMcpServer(ASSETS_NAME);
}

async function registerGodot(pi: ExtensionApi, project: string | null): Promise<void> {
  // The Godot stack's only third-party deps are mcp / numpy / httpx - all three already in
  // the shared venv - so it runs from there, exactly like Unity does. It used to default to
  // `godot/.venv`, a second 126 MB venv with the same interpreter and the same packages;
  // that duplicate was removed on 2026-10-12 and this fallback is what keeps engine=godot
  // working without it (verified: `gdmaster.mcp.policy_gateway` imports cleanly on .venv).
  // GODOT_PYTHON still wins when a genuinely separate godot venv exists.
  const py = process.env.GODOT_PYTHON ?? VENV_PY;
  if (!existsSync(py) || !existsSync(GODOT_HOME)) {
    process.stderr.write(
      `[engine-gate] engine=godot but the Godot stack is not runnable (python: ${py}). ` +
        `Set GODOT_PYTHON or create .venv. Godot tools are NOT exposed.\n`,
    );
  } else {
    pi.registerMcpServer(GODOT_NAME, {
      command: py,
      args: ["-m", "gdmaster.mcp.policy_gateway"],
      cwd: GODOT_HOME,
      env: {
        GDM_HOME: GODOT_HOME,
        GDM_PROJECT: project ?? "",
        GODOT_PROJECT_PATH: project ?? "",
      },
      exposure: "direct",
      timeout: 900,
      description:
        "Godot 4.7 only: project inspection, GDScript and .tscn edits, headless validation, " +
        "and Godot RAG. Active only while the active project declares engine=godot.",
    });
  }

  // godot-ai needs the Godot editor with the godot_ai addon listening on 8001.
  // Its HTTP token rotates on each start, so it is read by the server, not stored here.
  if (await portOpen(GODOT_AI_PORT)) {
    pi.registerMcpServer(GODOT_AI_NAME, {
      command: "uvx",
      args: [
        "--isolated",
        "--no-config",
        "--no-env-file",
        "--from",
        "godot-ai==4.1.0",
        "godot-ai",
        "attach",
        "--port",
        String(GODOT_AI_PORT),
        "--ws-port",
        "8002",
      ],
      cwd: REPO,
      env: {},
      exposure: "deferred",
      timeout: 120,
      description:
        "Godot AI editor bridge (godot-ai addon): live editor control, screenshots, game logs. " +
        "Registered only while the Godot editor listens on 127.0.0.1:8001.",
    });
  }
}

async function registerUnity(pi: ExtensionApi, project: string | null): Promise<void> {
  if (!existsSync(VENV_PY)) {
    process.stderr.write(
      `[engine-gate] engine=unity but the shared venv python is missing (${VENV_PY}). ` +
        `Set UNITY_PYTHON or create .venv. Unity tools are NOT exposed.\n`,
    );
    return;
  }
  if (!existsSync(UNITY_HOME)) {
    process.stderr.write(
      `[engine-gate] engine=unity but the Unity stack folder is missing (${UNITY_HOME}). ` +
        `Unity tools are NOT exposed.\n`,
    );
    return;
  }

  const env = {
    UNIM_HOME: UNITY_HOME,
    UNITY_PROJECT: project ?? "",
    UNIM_PROJECT: project ?? "",
  };

  pi.registerMcpServer(UNITY_RAG_NAME, {
    command: VENV_PY,
    args: ["-m", "unimaster.mcp.rag_mcp_server"],
    cwd: UNITY_HOME,
    env,
    exposure: "direct",
    timeout: 300,
    description:
      "Unity knowledge base: hybrid search (dense + BM25, RRF-fused) over the pinned " +
      "6000.3 Manual and ScriptReference, UnityCsReference C#, the cookbook, recipes, " +
      "troubleshooting and anti-patterns, plus the active Unity project indexed as " +
      "source=project.",
  });

  pi.registerMcpServer(UNITY_PROJECT_NAME, {
    command: VENV_PY,
    args: ["-m", "unimaster.mcp.project_mcp_server"],
    cwd: UNITY_HOME,
    env,
    exposure: "direct",
    timeout: 900,
    description:
      "Unity project tools: project info, file listing/reading, C# symbol lookup, " +
      "script write/edit with backups, C# lint plus an editor batch-mode compile gate " +
      "(-executeMethod), and the editor log. Every path is sandboxed to the project root. " +
      "The 900 s timeout covers a batch-mode Unity run.",
  });

  // The asset pipeline is the same ComfyUI stack Three.js and Godot use; only the output
  // root differs. `<project>/Assets/Generated` is inside Assets/ so Unity imports it.
  pi.registerMcpServer(ASSETS_NAME, {
    command: VENV_PY,
    args: ["-m", "threejs.mcp.assets_mcp_server"],
    cwd: REPO,
    env: { THREE_PROJECT_ASSET_ROOT: "Assets/Generated" },
    exposure: "direct",
    timeout: 7200,
    description:
      "Local asset pipeline (ComfyUI sidecar on 127.0.0.1:8188): text-to-image, background " +
      "removal, image-to-3D. For Unity, artefacts land in <project>/Assets/Generated/ so " +
      "Unity imports them. `asset_generate_pack` runs a whole list in one serialised pass.",
  });

  // The official Unity MCP bridge (unity.exe mcp) only does anything while the editor has
  // the project open with com.unity.pipeline installed; the editor writes the port file
  // under Library/Pipeline. Deferred: ~160 tools would swamp a 9B model's tool list.
  const portFile = project ? join(project, "Library", "Pipeline", ".unity-pipeline-port") : "";
  if (portFile && existsSync(portFile)) {
    const cli = process.env.UNITY_CLI ?? "unity";
    pi.registerMcpServer(UNITY_EDITOR_NAME, {
      command: cli,
      args: ["mcp"],
      cwd: REPO,
      env: { UNITY_NO_BANNER: "1", UNITY_NO_PAGER: "1" },
      exposure: "deferred",
      timeout: 120,
      description:
        "Official Unity editor bridge (~160 tools): live editor control, play mode, " +
        "screenshots, scene queries. Registered only while the Unity editor has the active " +
        "project open. Prefer the small `unity-project` surface unless live editor state is " +
        "what you actually need.",
    });
  }
}

/**
 * engine=roblox: everything comes from `pi-home-roblox/mcp.json` (rbx-rag, rbx-project,
 * `roblox-studio`, assets), so this gate registers nothing. What it does is name the two
 * failure modes that otherwise look like a broken agent:
 *
 *   1. the stack folder is missing -> the profile's servers will not start at all;
 *   2. Studio's own MCP binary is missing -> `script_read` / `execute_luau` answer
 *      "no studios connected" no matter what the user does in the editor.
 *
 * Studio's MCP server is a toggle INSIDE Studio (Assistant -> ... -> Manage MCP Servers),
 * so a missing editor is a warning, never an error: the knowledge base still works.
 */
function registerRoblox(project: string | null): void {
  const home = join(REPO, "roblox");
  if (!existsSync(home) || !existsSync(join(home, "rbxmaster"))) {
    process.stderr.write(
      `[engine-gate] engine=roblox but the Roblox stack is missing (${home}). ` +
        `rbx-rag / rbx-project are NOT available; the profile's mcp.json will fail to start them.\n`,
    );
    return;
  }
  const mcpBat = join(process.env.LOCALAPPDATA ?? "", "Roblox", "mcp.bat");
  const studioMcp = process.env.ROBLOX_STUDIO_MCP ?? "";
  if (!studioMcp && !existsSync(mcpBat)) {
    process.stderr.write(
      `[engine-gate] engine=roblox but Roblox Studio's MCP launcher was not found ` +
        `(${mcpBat || "%LOCALAPPDATA%\\Roblox\\mcp.bat"}). The RAG and the file tools work; ` +
        `the live-place tools (script_read, multi_edit, execute_luau) will not. ` +
        `Install Roblox Studio, or set ROBLOX_STUDIO_MCP to StudioMCP.exe.\n`,
    );
  }
  if (!project) {
    process.stderr.write(
      `[engine-gate] engine=roblox with no active project: rbx-project will answer ` +
        `"data/active_project.txt is empty". Pass a project to agent.cmd, or use the RAG only.\n`,
    );
  }
}

export default function engineGate(pi: ExtensionApi): void {
  pi.on("session_start", async () => {
    const { project, engine, stale } = activeEngine();
    clearAll(pi);

    // A stale pointer is a system error, not a threejs session: `activeEngine` has already
    // named the dead path on stderr, and no engine's servers are registered for it.
    if (stale) return;

    if (engine === "godot") {
      await registerGodot(pi, project);
      return;
    }
    if (engine === "unity") {
      await registerUnity(pi, project);
      return;
    }
    if (engine === "roblox") {
      registerRoblox(project);
      return;
    }
    // threejs: `threejs-rag` and `assets` come from pi-home-three/mcp.json.
  });

  // Skills are not added here: each engine has its own profile
  // (pi-home-three/skills, pi-home-godot/skills, pi-home-unity/skills) chosen by agent.cmd.
  //
  // The one exception is x_life, whose skill is project-scoped rather than engine-scoped.
  // It is contributed only while that project is active, so no other Three.js session ever
  // sees it. Same rule as the MCP surface above: a model cannot follow a skill it was
  // never given, and it should not be given one that does not apply.
  pi.on("resources_discover", () => {
    const { path } = activeProject();
    const same = (a: string, b: string) => resolve(a).toLowerCase() === resolve(b).toLowerCase();
    if (path && same(path, XLIFE_PROJECT) && existsSync(XLIFE_SKILLS)) {
      process.stderr.write(`[engine-gate] x_life active: contributing skill path ${XLIFE_SKILLS}\n`);
      return { skillPaths: [XLIFE_SKILLS] };
    }
    return {};
  });
}
