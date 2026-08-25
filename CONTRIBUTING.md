# Contributing to Tani

Thanks for your interest in improving Tani!

## Ground rules

1. **Additive by default** — new versions only add classes, never rename or remove existing ones.
2. **Zero-JS first** — prefer CSS-only mechanisms (`:checked`, `:target`, `:focus-within`, `<details>`, `<dialog>`) over scripts.
3. **Logical properties** — use `margin-inline`/`padding-block`/`inset-*` so RTL works for free.
4. **Respect reduced motion** — every new animation needs a `prefers-reduced-motion` story.
5. **One source of truth** — before adding a rule, search the stylesheet. If the selector already exists, extend it instead of appending a competing definition (duplicate definitions are how most of our historical bugs happened).

## Workflow

```bash
git clone https://github.com/TaniCSS/Tani.git
cd Tani
# open index.html in a browser — that's the whole toolchain
```

- Edit `dist/css/tani.css` (the single source file).
- Regenerate the minified build after changes:

```bash
python3 tools/minify.py dist/css/tani.css dist/css/tani.min.css
```

- Run the smoke test if you have Chrome/Chromium available (paths auto-detected):

```bash
python3 tests/smoke_selenium.py
```

## Submitting

1. Fork, then create a feature branch (`feat/my-component` or `fix/issue-123`).
2. Include a live demo built with Tani classes — screenshots are appreciated.
3. Keep PRs focused; one component/fix per PR.
4. Update `README.md` and `index.html` docs when you add user-facing classes.

## Reporting bugs

Open a [GitHub issue](https://github.com/TaniCSS/Tani/issues) with:
- the exact HTML/classes involved,
- browser + version,
- expected vs actual behavior.
