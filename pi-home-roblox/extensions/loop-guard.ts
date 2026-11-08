// Loaded by pi from this profile's `extensions/` directory - which works no matter
// what the working directory is. The code itself lives in `pi-extensions/` at the repo
// root: ONE copy for all four profiles, so the guard cannot drift per engine.
// Policy: mcp/reliability.json. Diagnostics: `gs reliability`.
export { default } from "../../pi-extensions/loop-guard.ts";
