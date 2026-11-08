# Comps Premier Valorant

Página estática con la mejor composición y la alternativa de cada mapa de Premier.

- `index.html` es la página. Usa las fotos de `fotos/`.
- `index_autonomo.html` es la misma página con las fotos incrustadas.
- Para cambiar el contenido, edita `plantilla.html` y ejecuta `python construir.py`.

## Actualizar al inicio de cada acto
1. Edita `plantilla.html` (mapas, comps, cifras).
2. Ejecuta `python construir.py`.
3. `git add -A`, `git commit -m "Acto N"`, `git push`. Vercel publica solo.
