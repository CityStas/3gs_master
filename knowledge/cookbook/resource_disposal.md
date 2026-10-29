# Resource disposal

Long-lived applications should explicitly dispose GPU resources that are no longer needed: geometries, materials and textures, plus render targets and addon-specific resources where applicable.

Do not equate removing an Object3D from the scene graph with releasing its GPU memory.
