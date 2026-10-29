# Three.js anti-patterns

- Do not recommend obsolete global `<script src="three.min.js">` patterns to modern module projects.
- Do not import addons from arbitrary CDN paths when the project uses npm package exports.
- Do not assume WebGL and WebGPU materials/renderers have identical shader APIs.
- Do not leak loaders, geometries, textures and materials across scene teardown without disposal policy.
- Do not optimize blindly before identifying CPU/GPU bottlenecks.
