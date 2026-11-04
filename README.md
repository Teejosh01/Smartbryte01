# SmartBryte01

Responsive homepage for **SmartBryte**, an online school for children. A single static page (`index.html`) — no backend, accounts, payments or extra routes — built to the supplied implementation brief.

## Source materials (`/docs`)

Everything that informed the build lives in this repo:

| File | Role |
|---|---|
| `docs/SmartBryte_Hero_and_Introduction_Content.pdf` | **Single source of truth for all visible copy** (used verbatim) |
| `docs/Lovable_Online_School_Homepage_Build_Brief.pdf` | Implementation brief: scope, exact-copy contract, design synthesis |
| `docs/DESIGN-Quizlet.md` | Design reference — iris-violet accent, card discipline, soft shadows |
| `docs/DESIGN-SuperHi.md` | Design reference — paper-cut shapes, chalk-blue wash, pill components, mono labels |
| `docs/reference-insightpod-*.jpg` | Visual reference — warm cream canvas, editorial scale, amber CTA, dark band |
| `docs/reference-new-school.jpg` | Visual reference — staggered capsule media tiles, floating accents |

## Run it

Any static server works, e.g.:

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

(Equally deployable to GitHub Pages, Netlify, Vercel — just serve the repo root.)

## Structure

- `index.html` — the homepage (header, hero, introduction, footer — the exact sections in the approved copy)
- `assets/styles.css` — the synthesized design system (tokens documented at the top of the file)
- `assets/script.js` — progressive enhancement only: scroll reveals, header elevation, gentle hero parallax

## Implementation notes (from the brief)

- **Copy fidelity:** every visible word comes from the content PDF, unchanged — headings, paragraphs, CTA labels, punctuation and numbers. No copy was taken from the design references.
- **CTA destinations pending:** no URLs were supplied for *"Explore Our Programmes"*, *"Apply Now"* or *"Discover SmartBryte"*. Per the brief they are rendered as honest static buttons with `IMPLEMENTATION NOTE` comments in `index.html`. Swap each `<button>` for an `<a>` (or add the destination) once the real links exist — the `.btn` styles work on both.
- **Imagery:** no school photographs were supplied, so the hero's capsule tiles carry flat illustrated motifs instead of people (reference-image people must never be presented as the school's own students). Each `.tile` in `index.html` is a swappable media slot — drop real photos in and the layout needs no changes.
- **Accessibility:** semantic landmarks, one `h1`, skip link, visible focus states, `prefers-reduced-motion` support, decorative art hidden from assistive tech.
