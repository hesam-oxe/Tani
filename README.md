<div align="center">

# 🚀 Tani CSS Framework

### The Advanced Zero-JS, Zero-Build CSS Framework

[![Version](https://img.shields.io/badge/version-2.3.1-orange?style=for-the-badge&logo=semver)](https://github.com/TaniCSS/Tani/releases)
[![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)](LICENSE)
[![Size](https://img.shields.io/badge/min-~183KB-green?style=for-the-badge)](https://github.com/TaniCSS/Tani)
[![Size](https://img.shields.io/badge/gzip-~32KB-green?style=for-the-badge)](https://github.com/TaniCSS/Tani)
[![CSS Modern](https://img.shields.io/badge/CSS-Modern%202026-purple?style=for-the-badge)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![Zero JS](https://img.shields.io/badge/Zero-JS%20Components-red?style=for-the-badge)](#-god-mode-features)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=for-the-badge)](CONTRIBUTING.md)

**A lightweight, utility-first CSS framework with God Mode features that no other framework offers.**

[📖 Documentation](#-documentation) • [🚀 Quick Start](#-quick-start) • [✨ Features](#-god-mode-features) • [📊 Comparison](#-comparison) • [🎯 Examples](#-examples) • [🤝 Contributing](CONTRIBUTING.md)

</div>

---

## 🆕 What's New in v2.3.1 (bug-fix release)

A full audit of the stylesheet and docs. Highlights:

- 🐛 **Fixed** `.animate-pulse-slow` (referenced keyframes that didn't exist), gradient utilities (`from/to` now have fallbacks, `via-*` actually works via `color-mix`), `.drop-shadow` (now consumed by the `.filter` chain), and the `backdrop-blur-*` regression (standalone again, still composable with `.backdrop`)
- 🐛 **Fixed** undefined `--text` / `--text-muted` tokens that silently broke navbar brands, sidebar links, floating labels, `.lead`, figure captions
- ✨ **Real zero-JS wiring**: mobile navbar toggle (`navbar-toggle-check` checkbox pattern), offcanvas open/close + backdrop (`offcanvas-check`), toast close button (`toast:has(.toast-hide-check:checked)` via `:has()`)
- 🧹 **Deduplicated**: forms/modal/pagination/progress/nav sections existed 2–3× each with conflicting values — one canonical definition now wins everywhere
- 📐 **One spacing scale**: `m-1…m-12` now use the design-token scale (0.25 → 3rem, monotonic) consistently across base and responsive-prefixed utilities
- ♻️ Removed ~800 lines of dead/duplicate rules; minified build regenerated from source (`tools/minify.py`)
- 🌐 RTL-safe divide utilities restored to logical properties; tooltips gained a non-colliding `data-tooltip-pos` attribute; tabs support up to 6 panels; `.display-1..3` added

---

## 🆕 What's New in v2.3.0

The "completeness" release — closing the gap with Tailwind v4, Bootstrap 5, and Bulma, plus full RTL / dark / a11y coverage:

- ✅ **Logical spacing** — `ms-/me-/ps-/pe-*` (RTL-safe margins & padding)
- ✅ **Full Sizing scale** — numeric `w-/h-*` (1–96), `size-*`, `min-w/h-*`, `max-w/h-*` (prose/sm–2xl/screen)
- ✅ **Filters** — `blur`, `brightness`, `contrast`, `grayscale`, `invert`, `saturate`, `sepia`, `hue-rotate` + `backdrop-blur` (combine multiple with the `.filter` / `.backdrop` classes)
- ✅ **Transforms** — per-axis `translate-x/y`, `rotate`, `scale-x/y`, `skew-x/y`, `origin-*`, `transform-gpu`
- ✅ **Transitions** — property variants + full `duration-*` / `delay-*` / `ease-*`
- ✅ **Interactivity** — `appearance-none`, `resize`, `select-*`, `will-change-*`, `cursor-*`, `pointer-events-*`
- ✅ **Typography scale** — `tracking-*` / `leading-*` / `text-wrap` / `truncate` / `font-*`
- ✅ **Backgrounds & gradients** — `bg-cover/contain`, `bg-clip-text`, `bg-gradient-to-*` + `from/via/to-*`
- ✅ **Borders & divide** — `border-*` styles, `border-x/y-*`, `divide-x/y` + color variants
- ✅ **Form validation** — `is-valid` / `.valid-feedback` (symmetric with `is-invalid`)
- ✅ **Components** — `figure`, floating labels, full `offcanvas` (4 sides + backdrop), `progress` striped/animated, `table` striped/bordered/sm
- ✅ **Animations library** — `ping`, `flash`, `heart-beat`, `fade-in-*`, `zoom-*`, `slide-in-*`, `shake`, `float`, `spin-slow` (+ reduced-motion safe)
- ✅ **Responsive display** at `md / lg / xl / xxl`

---

## 🎯 Overview

Tani is a **next-generation CSS framework** that combines the best of modern CSS features with a utility-first approach. Built with **2026 standards**, it includes features that **no other framework offers**:

- ✅ **Scroll-Driven Animations** (Pure CSS, no JS)
- ✅ **Container Queries** (Component-aware responsiveness)
- ✅ **OKLCH Color System** (Perceptually uniform colors with auto-generated variants)
- ✅ **Zero-JS Components** (Modal, Accordion, Dropdown, Tabs, Tooltip, Offcanvas, Toast using native HTML/CSS)
- ✅ **Native Dark Mode** (System-preference based, zero JS)
- ✅ **RTL/LTR Support** (Logical Properties, built-in)
- ✅ **Fluid Typography** (clamp-based scaling, no media queries)
- ✅ **Debug Mode** (Visual layout inspector)
- ✅ **GPU-Accelerated Utilities** (Hardware-accelerated animations)
- ✅ **Anchor Positioning** (Smart tooltips without JS)
- ✅ **Complete Grid System** (12-col, spans, placement)
- ✅ **Skeletons, Avatars, Stat Cards, Timeline, Steps**
- ✅ **Print & High-Contrast support**

---

## ⚡ Quick Start

### Installation

**Option 1: CDN**
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/TaniCSS/Tani@v2.3.1/dist/css/tani.min.css">
```

**Option 2: Download**
```html
<link rel="stylesheet" href="./dist/css/tani.css">
```

**Option 3: NPM (Coming Soon)**
```bash
npm install tanicss
```

### Basic Usage

```html
<!DOCTYPE html>
<html lang="en" class="dark-mode">   <!-- or omit the class to follow the OS setting -->
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./dist/css/tani.css">
</head>
<body>
    <div class="container">
        <h1 class="text-center">Hello, Tani!</h1>
        <button class="btn btn-primary">Click Me</button>
    </div>
</body>
</html>
```

---

## 🔥 God Mode Features

### 1. 🌊 Scroll-Driven Animations

Animate elements as they scroll into view — **no JavaScript required**!

```html
<div class="card tani-fade-in">
    This card fades in as you scroll down
</div>

<div class="card tani-scale-in">
    This card scales up as you scroll
</div>
```

```css
/* How it works (built into Tani) */
.tani-fade-in {
    animation: taniFadeIn linear both;
    animation-timeline: view();
    animation-range: entry 0% cover 40%;
}
```

**Browser Support:** Chrome 115+, Edge 115+

---

### 2. 📦 Container Queries

Components adapt based on their **container size**, not viewport:

```css
.card {
    container-type: inline-size;
    container-name: tani-card;
}

@container tani-card (min-width: 400px) {
    .card-horizontal-layout {
        display: grid;
        grid-template-columns: 1fr 2fr;
    }
}
```

**Use Case:** A card component that displays vertically in a sidebar and horizontally in main content — without writing separate media queries.

---

### 3. 🎨 OKLCH Color System

Perceptually uniform colors with **automatic hover states**:

```css
:root {
    --primary: oklch(70% 0.18 70);
    --primary-hover: oklch(from var(--primary) calc(l - 8%) c h);
}

.btn-primary:hover {
    background-color: var(--primary-hover);
}
```

**Benefits:**
- Better color accuracy than HEX/RGB
- Automatic variant generation
- Zero extra code for hover states
- Perfect dark mode compatibility

---

### 4. ⚡ Zero-JS Components

Modals, accordions, dropdowns and offcanvas panels work **without JavaScript**:

```html
<!-- Pure-CSS modal (:target — zero JS) -->
<a class="btn btn-primary" href="#myModal">Open Modal</a>

<dialog id="myModal" class="modal">          <!-- native <dialog> also supported -->
    <div class="modal-content">
        <h3>Modal Title</h3>
        <p>Modal content here...</p>
        <a class="btn btn-secondary" href="#">Close</a>
    </div>
</dialog>
```

```html
<!-- Native Accordion (using <details>) -->
<details class="accordion-item">
    <summary>Click to expand</summary>
    <div>
        <p>Content here...</p>
    </div>
</details>
```

**Benefits:**
- Works even with JavaScript disabled
- Better accessibility (keyboard navigation built-in)
- Smaller bundle size
- Progressive enhancement

---

### 5. 🌙 Native Dark Mode

Automatically adapts to system preferences — **no toggle needed**:

```css
@media (prefers-color-scheme: dark) {
    :root:not(.light-mode) {
        --body-bg: oklch(15% 0.01 250);
        --body-color: oklch(95% 0.01 250);
    }
}
```

Just include Tani, and dark mode works automatically based on the user's OS settings. Force either mode with the `dark-mode` / `light-mode` classes on `<html>`.

---

### 6. 🌐 RTL/LTR Support

Built-in support for right-to-left languages using **Logical Properties**:

```css
.container {
    margin-inline: auto; /* Works in both LTR and RTL */
    padding-inline: 1rem;
}

.text-start {
    text-align: start; /* left in LTR, right in RTL */
}
```

**Usage:**
```html
<!-- For RTL languages (Arabic, Hebrew, Persian, etc.) -->
<html lang="ar" dir="rtl">
    <!-- Your content -->
</html>
```

**No extra RTL stylesheet needed!**

---

### 7. 📏 Fluid Typography

Smooth scaling from mobile to 4K using `clamp()`:

```css
:root {
    --text-base: clamp(1rem, 0.95rem + 0.25vw, 1.125rem);
    --text-2xl: clamp(1.5rem, 1.2rem + 1.5vw, 2.25rem);
}
```

---

### 8. 🐛 Debug Mode

Visual layout inspector for debugging:

```html
<body class="tani-debug">
    <!-- Your content -->
</body>
```

Adds colored outlines to all elements for easy debugging of spacing, alignment, and layout issues.

---

### 9. 🎯 Anchor Positioning

Smart tooltips that automatically find the best position:

```css
.tooltip {
    position: absolute;
    position-anchor: --trigger;
    top: anchor(bottom);
    left: anchor(center);
    position-try-fallbacks: flip-block, flip-inline;
}
```

---

### 10. 🚀 GPU-Accelerated Utilities

Hardware-accelerated animations for 60fps performance:

```html
<div class="tani-gpu">
    <!-- Smooth 60fps animations -->
</div>

<div class="tani-content-visibility">
    <!-- Optimized rendering for long lists -->
</div>
```

---

## 📊 Comparison

| Feature | Tani 2.3 | Tailwind v4 | Bootstrap 5 | Bulma |
|---------|----------|-------------|-------------|-------|
| **Scroll-Driven Animations** | ✅ | ❌ | ❌ | ❌ |
| **Container Queries** | ✅ | ✅ | ❌ | ❌ |
| **OKLCH Colors** | ✅ | ✅ | ❌ | ❌ |
| **Ships interactive components with no JS runtime** | ✅ | ❌ | ❌ (JS bundle) | ❌ (JS bundle) |
| **Native RTL/LTR** | ✅ | ⚠️ Plugin | ⚠️ Partial | ✅ |
| **Native Dark Mode** | ✅ | ✅ | ✅ | ❌ |
| **Debug Mode** | ✅ | ❌ | ❌ | ❌ |
| **Anchor Positioning** | ✅ | ❌ | ❌ | ❌ |
| **Grid System** | ✅ | ✅ | ✅ | ✅ |
| **Skeletons & Avatars** | ✅ | Manual | ❌ | ❌ |
| **Timeline & Steps** | ✅ | Manual | ❌ | ❌ |
| **Build step required** | ❌ None | ✅ CLI (or CDN play) | ❌ (CDN) | ❌ (CDN) |

*Honest footnote:* Tailwind ships no components at all (it's a utility language), so the "zero-JS components" row compares Tani against frameworks that ship component libraries requiring JavaScript runtimes.

---

## 🎨 Components

### Buttons

```html
<button class="btn btn-primary">Primary</button>
<button class="btn btn-secondary">Secondary</button>
<button class="btn btn-outline-primary">Outline</button>
<button class="btn btn-primary btn-lg">Large</button>
<button class="btn btn-primary btn-rounded">Rounded</button>
```

### Cards

```html
<div class="card">
    <div class="card-body">
        <h5 class="card-title">Card Title</h5>
        <p class="card-text">Card content...</p>
        <a href="#" class="btn btn-primary">Go somewhere</a>
    </div>
</div>
```

### Alerts

```html
<div class="alert alert-success" role="alert">
    <strong>Success!</strong> Operation completed.
</div>
```

### Forms

```html
<form>
    <div class="form-group">
        <label class="form-label" for="email">Email</label>
        <input type="email" id="email" class="form-control" placeholder="name@example.com">
    </div>
    <button type="submit" class="btn btn-primary">Submit</button>
</form>
```

### Tables

```html
<table class="table table-striped table-hover">
    <thead>
        <tr>
            <th>#</th>
            <th>Name</th>
            <th>Email</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>John Doe</td>
            <td>john@example.com</td>
        </tr>
    </tbody>
</table>
```

### Navigation (with zero-JS mobile menu)

The toggler is a `<label>` for a hidden checkbox placed before `.navbar-collapse`. Checking it opens the menu below `lg`; at `≥992px` the bar is always expanded.

```html
<nav class="navbar navbar-expand-lg navbar-dark">
    <div class="container-fluid">
        <a class="navbar-brand" href="#">Tani</a>
        <input type="checkbox" id="navToggle" class="navbar-toggle-check">
        <label class="navbar-toggler" for="navToggle">
            <span class="navbar-toggler-icon"></span>
        </label>
        <div class="collapse navbar-collapse">
            <ul class="navbar-nav">
                <li class="nav-item"><a class="nav-link active" href="#">Home</a></li>
                <li class="nav-item"><a class="nav-link" href="#">Features</a></li>
            </ul>
        </div>
    </div>
</nav>
```

### Modals (Zero-JS)

`:target` opens it, navigating back closes it — or use the native `<dialog>` element if you don't mind one `showModal()` call.

```html
<a class="btn btn-primary" href="#myModal">Open</a>

<dialog id="myModal" class="modal">
    <div class="modal-content">
        <div class="modal-header">
            <h5 class="modal-title">Modal Title</h5>
            <a class="btn-close" href="#" aria-label="Close"></a>
        </div>
        <div class="modal-body">
            <p>Modal content here...</p>
        </div>
    </div>
</dialog>
```

### Accordions (Zero-JS)

```html
<details class="accordion-item">
    <summary>Section 1</summary>
    <div>
        <p>Content for section 1...</p>
    </div>
</details>
```

---

## 🛠️ Utility Classes

### Spacing

The spacing scale is token-driven and monotonic: **0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 2, 2.5, 3 rem** for steps `0 1 2 3 4 5 6 8 10 12` (+ `auto`, `px`). The same scale applies to responsive-prefixed variants.

```html
<div class="m-3">Margin 0.75rem</div>
<div class="p-4">Padding 1rem</div>
<div class="mt-2 mb-3">Margin top 0.5rem, bottom 0.75rem</div>
<div class="mx-auto">Centered horizontally</div>
<div class="ms-4 me-4">RTL-safe logical margins (16px)</div>
```

> **Note:** `ms-/me-/ps-/pe-*` are the full-scale logical (RTL-aware) families. The legacy physical-named `ml-/mr-/pl-/pr-*` map onto inline start/end and cover steps 0–12 + auto.

### Display

```html
<div class="d-flex justify-content-center align-items-center">
    Centered content
</div>
```

### Text

```html
<p class="text-center text-primary">Centered primary text</p>
<p class="text-muted">Muted text</p>
<p class="text-start">Start-aligned (RTL-aware)</p>
```

### Colors

```html
<div class="bg-primary text-white p-3">Primary background</div>
<div class="bg-success text-white p-3">Success background</div>
```

### Gradients

```html
<div class="bg-gradient-to-r from-primary to-gold p-3">Primary → Gold</div>
<div class="bg-gradient-to-b from-primary via-danger to-gold p-3">With a via stop</div>
```

## 📐 Grid & Flexbox

```html
<!-- 12-column grid -->
<div class="grid grid-cols-3 gap-4">
    <div class="card">One</div>
    <div class="card">Two</div>
    <div class="card">Three</div>
</div>

<!-- Spans -->
<div class="grid grid-cols-4 gap-3">
    <div class="col-span-2">Wide</div>
    <div class="col-span-1">Narrow</div>
    <div class="col-span-1">Narrow</div>
</div>

<!-- Flexbox helpers -->
<div class="d-flex justify-content-between align-items-center gap-3">
    <div class="flex-1">Grows</div>
    <div>Static</div>
</div>
```

## 🆕 Zero-JS Components

### Tabs (via `:checked`, up to 6 panels)

```html
<div class="tabs">
    <input id="t1" class="tab-input" type="radio" name="tabs" checked>
    <label for="t1" class="tab-label">Home</label>
    <input id="t2" class="tab-input" type="radio" name="tabs">
    <label for="t2" class="tab-label">Profile</label>
    <div class="tab-panels">
        <div class="tab-panel">Home content</div>
        <div class="tab-panel">Profile content</div>
    </div>
</div>
```

### Tooltips (via `data-tooltip` + optional position)

The attribute value is the tooltip text; position is a separate attribute so it never collides with your copy:

```html
<button class="btn btn-primary" data-tooltip="I'm a tooltip">Hover me</button>
<button data-tooltip="I'm below" data-tooltip-pos="bottom">Bottom</button>
<button data-tooltip="I'm after" data-tooltip-pos="end">End</button>
```

### Toggle Switch

```html
<div class="form-check form-switch">
    <input class="form-check-input" type="checkbox" id="s1" checked>
    <label class="form-check-label" for="s1">Enable</label>
</div>
```

### Offcanvas (zero-JS, all four sides)

A checkbox placed before the panel and backdrop wires open/close + dimming with no scripts:

```html
<label class="btn btn-primary" for="ocToggle">Open panel</label>
<input type="checkbox" id="ocToggle" class="offcanvas-check">
<div class="offcanvas offcanvas-start" id="myPanel">
    <div class="offcanvas-header">
        <h5 class="offcanvas-title">Menu</h5>
        <label class="btn-close" for="ocToggle" aria-label="Close"></label>
    </div>
    <div class="offcanvas-body">Panel content…</div>
</div>
<div class="offcanvas-backdrop"></div>
```

Also available via `:target` (legacy) or a `.show` class (for JS apps).

### Toasts (zero-JS dismiss)

```html
<div class="toast show toast-success">
    <input type="checkbox" class="toast-hide-check" id="toastHide">
    <div class="toast-header"><strong>Saved</strong>
        <label class="toast-close" for="toastHide" aria-label="Dismiss">&times;</label>
    </div>
    <div class="toast-body">Everything worked.</div>
</div>
```

## 🧩 Data Components

### Skeletons

```html
<div class="skeleton skeleton-text"></div>
<div class="skeleton skeleton-circle" style="width: 3rem; height: 3rem"></div>
```

### Avatars

```html
<div class="avatar avatar-status">JB</div>
<div class="avatar avatar-status offline">SW</div>
<div class="avatar-group">
    <div class="avatar">JB</div>
    <div class="avatar">+9</div>
</div>
```

### Stat Cards / Timeline / Steps

```html
<div class="stat">
    <div class="stat-icon">📈</div>
    <div>
        <p class="stat-label">Revenue</p>
        <div class="stat-value">$24,500</div>
        <span class="stat-change stat-up">↑ 12.4%</span>
    </div>
</div>

<ul class="timeline">
    <li class="timeline-item">
        <div class="timeline-marker marker-done">✓</div>
        <div class="timeline-content"><h4>Shipped</h4></div>
    </li>
</ul>

<ol class="steps">
    <li class="step step-done"><span class="step-label">Account</span></li>
    <li class="step step-active"><span class="step-label">Profile</span></li>
</ol>
```

---

## 🌐 Browser Support

Tani supports all modern browsers:

- ✅ Chrome (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Edge (latest)
- ✅ Opera (latest)

**Note:** Some advanced features (Scroll-Driven Animations, Anchor Positioning) require very modern browsers and degrade gracefully. Filters/backdrop effects compose via the explicit `.filter` / `.backdrop` classes (same contract as Tailwind).

### Responsive breakpoints

Min-width prefixed utilities follow this table (`sm-flex`, `md-grid-cols-12`, `xl-mt-4`, …):

| Prefix | Min width |
|--------|-----------|
| `sm-`  | 640px |
| `md-`  | 768px |
| `lg-`  | 992px |
| `xl-`  | 1200px |
| `xxl-` | 1400px |

Legacy max-width helpers (`d-sm-none`, `d-xs-block`, applied *below* 768px / 576px) are kept for backwards compatibility but are deprecated — prefer the prefixed system above.

---

## 📖 Documentation

Full documentation is included in this repository — open `index.html` in your browser for the complete interactive documentation with live examples, playground, templates and search.

---

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) before submitting a pull request.

### Development Setup

```bash
# Clone the repository
git clone https://github.com/TaniCSS/Tani.git

# Navigate to the directory
cd Tani

# Open index.html in your browser
open index.html
```

After editing `dist/css/tani.css`, rebuild the minified file:

```bash
python3 tools/minify.py dist/css/tani.css dist/css/tani.min.css
```

### What to Contribute

- 🐛 Bug fixes
- ✨ New components
- 📝 Documentation improvements
- 🎨 Design enhancements
- 🌍 Translations
- ⚡ Performance optimizations

---

## 📦 Release history (recent)

- **v2.3.1** — full audit: fixed broken animations/gradients/filters, deduplicated conflicting sections, unified spacing scale, real zero-JS navbar/offcanvas/toast wiring, portable test-suite paths
- **v2.3.0** — completeness release (logical spacing, sizing scale, filters/transforms, gradients, validation, offcanvas, animations, responsive display)
- **v2.2.0** — Popover, Carousel, Animations, Container Queries, Subgrid, premium polish
- **v2.1.x** — utility library + first ten zero-JS components

---

## 📝 License

Tani is licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

- Built with modern CSS standards (2026)
- Inspired by Tailwind CSS, Bootstrap, and Bulma
- Thanks to all contributors who help make Tani better

---

## 📬 Contact

- **GitHub Issues:** [Report a bug](https://github.com/TaniCSS/Tani/issues)
- **Discussions:** [Ask a question](https://github.com/TaniCSS/Tani/discussions)

---

<div align="center">

**Made with ❤️ for the web community**

**If you find Tani useful, please consider giving it a ⭐ star!**

[⭐ Star this repo](https://github.com/TaniCSS/Tani) • [🍔 Fork this repo](https://github.com/TaniCSS/Tani/fork)

</div>
