// Loaded by pi from this profile's `extensions/` directory - which works no matter
// what the working directory is. The code itself lives in `pi-extensions/` at the repo
// root: ONE copy for all four profiles, so the guard cannot drift per engine. It used to
// sit in `<repo>/.pi/extensions/`, which pi only reads when cwd IS the repo root - a
// session started inside a project folder silently lost it.
export { default } from "../../pi-extensions/engine-gate.ts";
