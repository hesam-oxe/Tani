#!/usr/bin/env python3
"""One-shot bug-fix transformer for dist/css/tani.css (v2.3.1 repair pass)."""
import sys, re

PATH = "dist/css/tani.css"
src = open(PATH, encoding="utf-8").read()
orig_len = len(src)
ops = []

def rep(old, new, count=1, tag=""):
    global src
    n = src.count(old)
    if n != count:
        print(f"FAIL [{tag}] expected {count} occurrence(s), found {n}:\n---\n{old[:160]}\n---")
        sys.exit(1)
    src = src.replace(old, new)
    ops.append(tag)

def splice(start, end, keep_end=True, tag="", pad="\n"):
    """Delete text from `start` up to (excluding) `end`."""
    global src
    i = src.find(start)
    j = src.find(end, i + len(start)) if i != -1 else -1
    if i == -1 or j == -1:
        print(f"FAIL [{tag}] splice markers not found (start={i}, end={j})"); sys.exit(1)
    src = src[:i] + pad + src[j:] if not keep_end else src[:i] + src[j:]
    ops.append(tag)

# ── 1. header metadata ──────────────────────────────────────────────
rep("    Version: 2.2.0\n    License: MIT\n    Size: ~55KB raw / ~15KB gzip",
    "    Version: 2.3.1\n    License: MIT\n    Size: see release notes (single stylesheet, no build)",
    1, "header")

# ── 2. missing design tokens (--text / --text-muted) ────────────────
rep("    --light: var(--gray-100); --dark: var(--gray-900);\n",
    "    --light: var(--gray-100); --dark: var(--gray-900);\n"
    "    --text: var(--body-color);\n"
    "    --text-muted: var(--gray-600);\n",
    1, "tokens")

# ── 3. stray v1 .mr-0 inside navbar section ─────────────────────────
rep("\n.mr-0 {\n    margin-inline-end: 0 !important;\n}\n.navbar-toggler:hover",
    "\n.navbar-toggler:hover", 1, "mr-0")

# ── 4. orphan DROPDOWN stub + entire v1 !important spacing block ────
splice("/* ==========================================================================\n"
       "   22. DROPDOWNS (focus-within = zero JS)\n"
       "   ========================================================================== */",
       "/* Text */\n", keep_end=True, tag="v1-spacing", pad="")

# ── 5. duplicate navs/tabs tail + FORMS §13 + PROGRESS §14 + PAGINATION §15 + MODAL §16
splice("/* Navs and Tabs */",
       ".dropdown-item:focus-visible", keep_end=True, tag="dup-sections", pad="")

# keep the unique rules that lived in that range, drop the dups around them
rep(".dropdown-item:focus-visible { outline: 2px solid var(--primary); outline-offset: -2px; color: var(--white); background-color: var(--primary); }\n"
    ".dropdown-divider { height: 0; margin: 0.5rem 0; overflow: hidden; border-block-start: 1px solid var(--border-color); }\n"
    ".dropdown-menu-end",
    ".dropdown-item:focus-visible { outline: 2px solid var(--primary); outline-offset: -2px; color: var(--white); background-color: var(--primary); }\n"
    ".dropdown-menu-end", 1, "dropdown-strays")

# ── 6. §24 progress base duplicates (canonical live at EOF v2.3 block)
rep(".progress { display: flex; height: 1rem; overflow: hidden; font-size: 0.75rem; background-color: var(--gray-200); border-radius: var(--border-radius); }\n"
    ".progress-sm { height: 0.5rem; }",
    ".progress-sm { height: 0.5rem; }", 1, "progress-base")
rep(".progress-bar {\n"
    "    display: flex; flex-direction: column; justify-content: center; overflow: hidden;\n"
    "    color: var(--white); text-align: center; white-space: nowrap; background-color: var(--primary);\n"
    "    transition: width 0.6s ease;\n"
    "}\n"
    ".progress-bar-striped {\n"
    "    background-image: linear-gradient(45deg, oklch(100% 0 0 / 0.15) 25%, transparent 25%, transparent 50%, oklch(100% 0 0 / 0.15) 50%, oklch(100% 0 0 / 0.15) 75%, transparent 75%, transparent);\n"
    "    background-size: 1rem 1rem;\n"
    "}\n"
    ".progress-bar-animated { animation: progress-bar-stripes 1s linear infinite; }\n"
    "@keyframes progress-bar-stripes { 0% { background-position: 1rem 0; } 100% { background-position: 0 0; } }\n"
    ".progress-bar-primary { background-color: var(--primary); }\n",
    ".progress-bar-primary { background-color: var(--primary); }\n", 1, "progress-dup")

# ── 7. accordion rotate/content glitch ──────────────────────────────
rep('details.accordion-item summary::after { content: "+"; font-size: var(--text-xl); transition: rotate var(--transition-fast); }',
    'details.accordion-item summary::after { content: "+"; font-size: var(--text-xl); }', 1, "acc-trans")
rep("\ndetails.accordion-item[open] summary::after { rotate: 45deg; }\n", "\n", 1, "acc-rotate")

# ── 8. breadcrumb style-stripping override ──────────────────────────
rep(".breadcrumb { display: flex; flex-wrap: wrap; padding: 0; margin: 0; list-style: none; } "
    ".breadcrumb-item + .breadcrumb-item::before { content: '/'; margin: 0 0.5rem; color: var(--text-muted); } "
    ".breadcrumb-item.active { color: var(--text-muted); }\n", "", 1, "breadcrumb")

# ── 9. navbar toggler icon: single source (mask + currentColor) ─────
rep("\n.navbar-toggler-icon {\n"
    "    display: inline-block;\n    width: 1.5em;\n    height: 1.5em;\n    vertical-align: middle;\n"
    "    background-image: url(\"data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 30 30'%3e%3cpath stroke='rgba(0, 0, 0, 0.7)' stroke-linecap='round' stroke-miterlimit='10' stroke-width='2' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e\");\n"
    "    background-repeat: no-repeat;\n    background-position: center;\n    background-size: 100%;\n}\n",
    "", 1, "toggler-base")
rep(".navbar-light .navbar-toggler-icon {\n"
    "    background-image: url(\"data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 30 30'%3e%3cpath stroke='rgba(0, 0, 0, 0.7)' stroke-linecap='round' stroke-miterlimit='10' stroke-width='2' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e\");\n}",
    ".navbar-light .navbar-toggler-icon { color: var(--gray-800); }", 1, "toggler-light")
rep(".navbar-dark .navbar-toggler-icon {\n"
    "    background-image: url(\"data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 30 30'%3e%3cpath stroke='rgba(255, 255, 255, 0.7)' stroke-linecap='round' stroke-miterlimit='10' stroke-width='2' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e\");\n}",
    ".navbar-dark .navbar-toggler-icon { color: oklch(90% 0.01 250); }", 1, "toggler-dark")
rep(".navbar-primary .navbar-toggler-icon {\n"
    "    background-image: url(\"data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 30 30'%3e%3cpath stroke='rgba(255, 255, 255, 0.7)' stroke-linecap='round' stroke-miterlimit='10' stroke-width='2' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e\");\n}",
    ".navbar-primary .navbar-toggler-icon { color: var(--white); }", 1, "toggler-primary")

# brand leftover physical margin
rep(".brand,.navbar-brand{display:inline-flex;align-items:center;gap:.4rem;font-weight:800;font-size:1.15rem;text-decoration:none;color:var(--text)}",
    ".brand,.navbar-brand{display:inline-flex;align-items:center;gap:.4rem;font-weight:800;font-size:1.15rem;text-decoration:none;color:var(--text);margin:0}", 1, "brand-margin")

# ── 10. nav-pills dead hover rule ───────────────────────────────────
rep(".nav-pills .nav-link.active, .nav-pills .nav-link:hover:not(.disabled) { color: var(--white); background-color: var(--primary); }\n"
    ".nav-pills .nav-link:hover:not(.disabled) { background-color: oklch(from var(--primary) l c h / 0.15); color: var(--primary); }",
    ".nav-pills .nav-link.active, .nav-pills .nav-link.active:hover:not(.disabled) { color: var(--white); background-color: var(--primary); }\n"
    ".nav-pills .nav-link:hover:not(.disabled):not(.active) { background-color: oklch(from var(--primary) l c h / 0.15); color: var(--primary); }",
    1, "pills-hover")

# ── 11. dropdown-menu.show duplicate line ───────────────────────────
rep("}\n.dropdown-menu.show { display: block; }\n.dropdown:focus-within",
    "}\n.dropdown:focus-within", 1, "dd-show")

# ── 12. toast compact duplicates + zero-JS close (:has) ─────────────
rep(".toast-header strong { margin-inline-end: auto; font-weight: 600; }\n"
    ".toast-body { padding: 0.75rem; word-wrap: break-word; }\n"
    ".toast-close",
    ".toast-close", 1, "toast-dup")
rep(".toast-check:checked ~ .toast .toast-close { pointer-events: auto; }\n",
    ".toast-check:checked ~ .toast .toast-close { pointer-events: auto; }\n\n"
    "/* Zero-JS close: put <input type=\"checkbox\" class=\"toast-hide-check\"> + <label class=\"toast-close\" for=…> inside the toast */\n"
    ".toast-hide-check { position: absolute; opacity: 0; pointer-events: none; }\n"
    ".toast:has(.toast-hide-check:checked) { display: none; }\n",
    1, "toast-has")

# ── 13. zero-JS navbar toggle (checkbox hack) ───────────────────────
rep(".collapse:not(.show) {\n    display: none;\n}\n",
    ".collapse:not(.show) {\n    display: none;\n}\n\n"
    "/* Zero-JS mobile toggle: <input type=\"checkbox\" class=\"navbar-toggle-check\"> placed before .navbar-collapse */\n"
    ".navbar-toggle-check { position: absolute; width: 1px; height: 1px; opacity: 0; margin: -1px; pointer-events: none; }\n"
    ".navbar-toggle-check:checked ~ .navbar-collapse { display: flex !important; flex-direction: column; align-items: stretch; width: 100%; }\n"
    ".navbar-toggle-check:checked ~ .navbar-collapse .navbar-nav { flex-direction: column; width: 100%; }\n"
    "@media (min-width: 992px) {\n"
    "    .navbar-toggle-check:checked ~ .navbar-collapse { flex-direction: row; align-items: center; width: auto; }\n"
    "    .navbar-toggle-check:checked ~ .navbar-collapse .navbar-nav { flex-direction: row; width: auto; }\n"
    "}\n",
    1, "navbar-check")

# ── 14. offcanvas: hide backdrop by default + zero-JS wiring ────────
rep(".offcanvas-backdrop { position: fixed; inset: 0; z-index: 1040; background-color: oklch(0% 0 0 / 0.5); }\n",
    ".offcanvas-backdrop { position: fixed; inset: 0; z-index: 1040; background-color: oklch(0% 0 0 / 0.5); display: none; }\n"
    ".offcanvas.show ~ .offcanvas-backdrop, .offcanvas-backdrop.show { display: block; }\n\n"
    "/* Zero-JS: <input type=\"checkbox\" class=\"offcanvas-check\"> placed before .offcanvas and .offcanvas-backdrop */\n"
    ".offcanvas-check { position: fixed; opacity: 0; pointer-events: none; }\n"
    ".offcanvas-check:checked ~ .offcanvas { transform: none; }\n"
    ".offcanvas-check:checked ~ .offcanvas-backdrop { display: block; }\n",
    1, "offcanvas-check")

# ── 15. tooltips: dedicated position attribute (value no longer collides with text)
rep('[data-tooltip="bottom"]::after, [data-tooltip^="bottom"]::after { bottom: auto; top: calc(100% + 6px); }\n'
    '[data-tooltip="start"]::after, [data-tooltip^="start"]::after { bottom: auto; top: 50%; inset-inline-end: calc(100% + 6px); inset-inline-start: auto; translate: 0 -50%; }\n'
    '[data-tooltip="end"]::after, [data-tooltip^="end"]::after { bottom: auto; top: 50%; inset-inline-start: calc(100% + 6px); translate: 0 -50%; }',
    '[data-tooltip-pos="bottom"]::after { bottom: auto; top: calc(100% + 6px); }\n'
    '[data-tooltip-pos="start"]::after { bottom: auto; top: 50%; inset-inline-end: calc(100% + 6px); inset-inline-start: auto; translate: 0 -50%; }\n'
    '[data-tooltip-pos="end"]::after { bottom: auto; top: 50%; inset-inline-start: calc(100% + 6px); translate: 0 -50%; }',
    1, "tooltip-pos")

# ── 16. tabs: support 5–6 panels ────────────────────────────────────
rep(".tab-input:nth-of-type(4):checked ~ .tab-panels .tab-panel:nth-child(4) { display: block; }",
    ".tab-input:nth-of-type(4):checked ~ .tab-panels .tab-panel:nth-child(4),\n"
    ".tab-input:nth-of-type(5):checked ~ .tab-panels .tab-panel:nth-child(5),\n"
    ".tab-input:nth-of-type(6):checked ~ .tab-panels .tab-panel:nth-child(6) { display: block; }",
    1, "tabs-6")

# ── 17. fs-3 odd value ──────────────────────────────────────────────
rep("1.12rem", "1.125rem", 2, "fs-3")

# ── 18. nonsense translate-x-auto ───────────────────────────────────
rep("\n.translate-x-auto { translate: 50%; }", "", 1, "tx-auto")

# ── 19. --tw-* custom props: declare once on :root (inherited) ──────
rep("*, ::before, ::after { --tw-blur: ;", ":root { --tw-blur: ;", 1, "tw-root")

# ── 20. gradients: always-valid fallbacks + working via-* ───────────
GRAD_OLD = """.bg-gradient-to-t { background-image: linear-gradient(to top, var(--tw-gradient-from), var(--tw-gradient-to)); }
.bg-gradient-to-b { background-image: linear-gradient(to bottom, var(--tw-gradient-from), var(--tw-gradient-to)); }
.bg-gradient-to-l { background-image: linear-gradient(to left, var(--tw-gradient-from), var(--tw-gradient-to)); }
.bg-gradient-to-r { background-image: linear-gradient(to right, var(--tw-gradient-from), var(--tw-gradient-to)); }
.bg-gradient-to-tl { background-image: linear-gradient(to top left, var(--tw-gradient-from), var(--tw-gradient-to)); }
.bg-gradient-to-tr { background-image: linear-gradient(to top right, var(--tw-gradient-from), var(--tw-gradient-to)); }
.bg-gradient-to-bl { background-image: linear-gradient(to bottom left, var(--tw-gradient-from), var(--tw-gradient-to)); }
.bg-gradient-to-br { background-image: linear-gradient(to bottom right, var(--tw-gradient-from), var(--tw-gradient-to)); }"""
VIA = "var(--tw-gradient-via, color-mix(in oklab, var(--tw-gradient-from, transparent), var(--tw-gradient-to, transparent)))"
def grad(direction):
    return (f".bg-gradient-to-{direction} {{ background-image: linear-gradient(to {direction}, "
            f"var(--tw-gradient-from, transparent), {VIA}, var(--tw-gradient-to, transparent)); }}")
GRAD_NEW = "\n".join(grad(d) for d in ["top", "bottom", "left", "right", "top left", "top right", "bottom left", "bottom right"])
rep(GRAD_OLD, GRAD_NEW, 1, "gradients")
rep(".bg-gradient { background-image: linear-gradient(var(--tw-gradient-from,transparent),var(--tw-gradient-to,transparent)); }",
    f".bg-gradient {{ background-image: linear-gradient(var(--tw-gradient-from, transparent), {VIA}, var(--tw-gradient-to, transparent)); }}",
    1, "bg-gradient")

# ── 21. .filter chain: consume --tw-drop-shadow ─────────────────────
rep(".filter { filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia); }",
    ".filter { filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow); }",
    1, "filter-chain")

# ── 22. blur utilities: work standalone AND compose via .filter ─────
BLURS = [("blur-0","0"),("blur-sm","4px"),("blur","8px"),("blur-md","12px"),
         ("blur-lg","16px"),("blur-xl","24px"),("blur-2xl","40px"),("blur-3xl","64px")]
for cls, val in BLURS:
    rep(f".{cls} {{ --tw-blur: blur({val}); }}",
        f".{cls} {{ --tw-blur: blur({val}); filter: var(--tw-blur); }}", 1, f"blur:{cls}")

# ── 23. backdrop utilities: standalone + compose via .backdrop ──────
BD = [("backdrop-blur-0","--tw-backdrop-blur"),("backdrop-blur-sm","--tw-backdrop-blur"),
      ("backdrop-blur","--tw-backdrop-blur"),("backdrop-blur-md","--tw-backdrop-blur"),
      ("backdrop-blur-lg","--tw-backdrop-blur"),("backdrop-blur-xl","--tw-backdrop-blur"),
      ("backdrop-blur-2xl","--tw-backdrop-blur"),("backdrop-blur-3xl","--tw-backdrop-blur"),
      ("backdrop-brightness-50","--tw-backdrop-brightness"),("backdrop-brightness-100","--tw-backdrop-brightness"),
      ("backdrop-brightness-150","--tw-backdrop-brightness"),("backdrop-grayscale","--tw-backdrop-grayscale"),
      ("backdrop-grayscale-0","--tw-backdrop-grayscale"),("backdrop-invert","--tw-backdrop-invert"),
      ("backdrop-invert-0","--tw-backdrop-invert"),("backdrop-opacity-0","--tw-backdrop-opacity"),
      ("backdrop-opacity-50","--tw-backdrop-opacity"),("backdrop-opacity-100","--tw-backdrop-opacity"),
      ("backdrop-saturate-0","--tw-backdrop-saturate"),("backdrop-saturate-100","--tw-backdrop-saturate"),
      ("backdrop-saturate-200","--tw-backdrop-saturate"),("backdrop-sepia","--tw-backdrop-sepia"),
      ("backdrop-sepia-0","--tw-backdrop-sepia")]
import re as _re
for cls, var in BD:
    pat = _re.compile(r"\." + _re.escape(cls) + r" \{ " + _re.escape(var) + r": ([^;}]+); \}")
    m = pat.search(src)
    if not m:
        print(f"FAIL [bd:{cls}] rule not found"); sys.exit(1)
    repl = (f".{cls} {{ {var}: {m.group(1)}; -webkit-backdrop-filter: {var}; backdrop-filter: {var}; }}")
    src = src[:m.start()] + repl + src[m.end():]
ops.append("backdrop-family")

# legacy standalone backdrop definitions (conflicting scales) removed
rep("/* Backdrop blur */\n"
    ".backdrop-blur { backdrop-filter: blur(4px); -webkit-backdrop-filter: blur(4px); }\n"
    ".backdrop-blur-sm { backdrop-filter: blur(2px); -webkit-backdrop-filter: blur(2px); }\n"
    ".backdrop-blur-lg { backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); }\n"
    ".backdrop-blur-xl { backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px); }\n",
    "/* Backdrop blur */\n"
    "/* (standalone .backdrop-blur* utilities are defined in the v2.3 filter section;\n"
    "    combine them with the .backdrop class to layer multiple effects) */\n",
    1, "legacy-backdrop")

# ── 24. divide-* back to logical properties ─────────────────────────
DIV_OLD = """.divide-x > :not([hidden]) ~ :not([hidden]) { border-inline-start-width: 1px; border-inline-start-style: solid; border-inline-start-color: var(--border-color); }
.divide-y > :not([hidden]) ~ :not([hidden]) { border-top-width: 1px; border-top-style: solid; border-top-color: var(--border-color); }
.divide-x-0 > :not([hidden]) ~ :not([hidden]) { border-inline-start-width: 0; } .divide-y-0 > :not([hidden]) ~ :not([hidden]) { border-top-width: 0; }"""
DIV_NEW = """.divide-x > :not([hidden]) ~ :not([hidden]) { border-inline-start-width: 1px; border-inline-start-style: solid; border-inline-start-color: var(--border-color); }
.divide-y > :not([hidden]) ~ :not([hidden]) { border-block-start-width: 1px; border-block-start-style: solid; border-block-start-color: var(--border-color); }
.divide-x-0 > :not([hidden]) ~ :not([hidden]) { border-inline-start-width: 0; } .divide-y-0 > :not([hidden]) ~ :not([hidden]) { border-block-start-width: 0; }"""
rep(DIV_OLD, DIV_NEW, 1, "divide-base")

rep(".divide-x-2 > :not([hidden]) ~ :not([hidden]) { border-inline-start-width: 2px; } .divide-y-2 > :not([hidden]) ~ :not([hidden]) { border-top-width: 2px; }\n"
    ".divide-y-reverse > :not([hidden]) ~ :not([hidden]) { border-top-width: 0; border-bottom-width: 1px; }",
    ".divide-x-2 > :not([hidden]) ~ :not([hidden]) { border-inline-start-width: 2px; } .divide-y-2 > :not([hidden]) ~ :not([hidden]) { border-block-start-width: 2px; }\n"
    ".divide-y-reverse > :not([hidden]) ~ :not([hidden]) { border-block-start-width: 0; border-block-end-width: 1px; border-block-end-style: solid; }",
    1, "divide-2")

COLORS = ["primary","secondary","success","danger","warning","info","gold"]
for c in COLORS:
    old2 = (f".divide-{c} > :not([hidden]) ~ :not([hidden]) {{ border-inline-start-color: var(--{c}); }}\n"
            f".divide-{c} > :not([hidden]) ~ :not([hidden]) {{ border-top-color: var(--{c}); }}")
    rep(old2, f".divide-{c} > :not([hidden]) ~ :not([hidden]) {{ border-color: var(--{c}); }}", 1, f"divide:{c}")

# ── 25. d-xxl rules accidentally outside the media query ────────────
rep("""  .d-xxl-grid { display: grid !important; }
}
.d-xxl-inline { display: inline !important; }
.d-xxl-inline-block { display: inline-block !important; }
.d-xxl-inline-flex { display: inline-flex !important; }
.d-xxl-none { display: none !important; }
.d-xxl-table { display: table !important; }
.d-xxl-table-row { display: table-row !important; }
.d-xxl-table-cell { display: table-cell !important; }""",
"""  .d-xxl-grid { display: grid !important; }
  .d-xxl-inline { display: inline !important; }
  .d-xxl-inline-block { display: inline-block !important; }
  .d-xxl-inline-flex { display: inline-flex !important; }
  .d-xxl-none { display: none !important; }
  .d-xxl-table { display: table !important; }
  .d-xxl-table-row { display: table-row !important; }
  .d-xxl-table-cell { display: table-cell !important; }
}""", 1, "d-xxl")

# ── 26. triplicated legacy max-width helpers ────────────────────────
LEG = ("@media (max-width: 768px) {\n"
       "    .container { padding-inline: 12px; }\n"
       "    .d-sm-none { display: none !important; } .d-sm-block { display: block !important; }\n"
       "    .d-sm-flex { display: flex !important; } .text-sm-center { text-align: center !important; }\n"
       "}\n"
       "@media (max-width: 576px) {\n"
       "    .d-xs-none { display: none !important; } .d-xs-block { display: block !important; }\n"
       "    .d-xs-flex { display: flex !important; } .text-xs-center { text-align: center !important; }\n"
       "}\n")
rep("\n/* Responsive helpers */\n" + LEG, "\n", 1, "resp-dup-1")
rep("\n/* Legacy max-width helpers (kept for compatibility) */\n" + LEG, "\n", 1, "resp-dup-2")

# ── 27. missing @keyframes pulse ────────────────────────────────────
rep("@keyframes animBounce { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-12px); } }",
    "@keyframes animBounce { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-12px); } }\n\n"
    "@keyframes pulse { 0%, 100% { transform: scale(1); opacity: 1; } 50% { transform: scale(1.06); opacity: 0.85; } }",
    1, "pulse-kf")

# ── 28. missing .display-* utilities (used by docs visualizer) ─────
rep(".fs-4 { font-size: 0.87rem; } .fs-5 { font-size: 0.75rem; }\n",
    ".fs-4 { font-size: 0.87rem; } .fs-5 { font-size: 0.75rem; }\n"
    ".display-1 { font-size: var(--text-6xl); font-weight: 700; line-height: 1.05; letter-spacing: -0.02em; }\n"
    ".display-2 { font-size: var(--text-5xl); font-weight: 700; line-height: 1.1; letter-spacing: -0.02em; }\n"
    ".display-3 { font-size: var(--text-4xl); font-weight: 700; line-height: 1.15; }\n",
    1, "display-utils")

open(PATH, "w", encoding="utf-8").write(src)
print(f"OK — {len(ops)} operations applied. {orig_len} → {len(src)} bytes.")
