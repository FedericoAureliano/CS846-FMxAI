# CS846: FMxAI

Course notes live in [`index.md`](index.md) and are published as a static site in `docs/`.

## Generating the website

After editing `index.md`, regenerate `docs/index.html`:

```
uv run scripts/build_docs.py
```

This renders `index.md` to a self-contained, GitHub Pages-ready page in `docs/`.

## Decoding scripts

Demo scripts for text decoding strategies live in `src/`:

```
uv run src/how-to.py
uv run src/mask.py
```
