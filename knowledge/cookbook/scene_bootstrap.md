# Three.js scene bootstrap

A minimal modern app typically creates a `Scene`, a `PerspectiveCamera` or `OrthographicCamera`, a renderer, appends the renderer canvas, updates the camera/renderer on resize, and runs a render loop.

For module projects prefer:

```js
import * as THREE from 'three';
```

The exact backend should be explicit: `WebGLRenderer` for the compatibility-oriented path or `WebGPURenderer` for WebGPU/TSL work.
