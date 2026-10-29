# Clover Craft Wiki

Wiki do mod **Clover Craft 0.4.0** (NeoForge 1.21.1), gerada a partir do JAR descompilado. Inclui viewer 3D dos modelos GeckoLib.

## Local

```bash
npm install
npm run docs:dev
```

http://localhost:5173/

## GitHub Pages

1. Crie um repositório (ex.: `clovercraft-wiki`) e envie este projeto.
2. Em **Settings → Pages → Source** escolha **GitHub Actions**.
3. O workflow `.github/workflows/pages.yml` publica a cada push em `main`.

A URL fica `https://<user>.github.io/<repo>/` (o `base` do VitePress é calculado no CI). Se o repo se chamar `<user>.github.io`, o site sobe na raiz.

Não commite o `.jar` nem `decompiled/` (já estão no `.gitignore`). Os modelos em `docs/public/models/` (~11 MB) vão no git — são o que o viewer usa.

## Regenerar conteúdo

```bash
python tools/extract_models.py   # geos + texturas do JAR
python tools/build_wiki.py       # markdown a partir do descompilado
```
