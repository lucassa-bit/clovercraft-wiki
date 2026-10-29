# Clover Craft Wiki

Wiki do mod **Clover Craft 0.4.0** (NeoForge 1.21.1). Inclui visualizador 3D dos modelos GeckoLib, sem distribuir arquivos de implementação do mod.

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

Os modelos e texturas em `docs/public/models/` vão no git — são o que o visualizador usa. Arquivos do mod, código descompilado e dados de extração ficam excluídos pelo `.gitignore`.

## Manutenção

```bash
python tools/extract_models.py   # atualiza geos + texturas de uma fonte autorizada
python tools/build_wiki.py       # atualiza os markdowns com uma fonte autorizada
```
