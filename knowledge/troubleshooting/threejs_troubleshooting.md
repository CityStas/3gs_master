# Three.js troubleshooting

## Black screen

Check renderer creation, canvas size, camera position/frustum, scene visibility, render loop, and console errors. Verify that objects are in front of the camera and that near/far planes are sensible.

## Model missing

Check the network URL, `GLTFLoader` import, server/static directory behavior, decoder paths, and loader error callback. Verify the asset independently.

## Resize bug

Update camera aspect/projection and renderer size in the resize handler. Keep device-pixel-ratio policy explicit.

## Wrong colors

Check color-space/textures, renderer/output color settings and tone mapping for the target version.
