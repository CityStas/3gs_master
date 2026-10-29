# Loading glTF

Use `GLTFLoader` as an addon:

```js
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

const loader = new GLTFLoader();
const gltf = await loader.loadAsync('/models/example.glb');
scene.add(gltf.scene);
```

If compression is used, configure the matching decoder/loader before loading. Treat asset URLs and public/static directory conventions as project-specific.
