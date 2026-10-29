# Three.js RAG AI Rules

1. Не выдумывать API, классы, методы или addon imports.
2. Не считать WebGL и WebGPU взаимозаменяемыми.
3. Для current code предпочитать ESM imports.
4. Не использовать старые `THREE.*` global-script examples как default, если проект использует modules.
5. Для GLTFLoader, OrbitControls и других addons проверять addon import path.
6. При конфликте project code vs generic docs сначала исследовать project code, затем проверить official docs.
7. При migration issue проверять migration guide для целевой версии.
