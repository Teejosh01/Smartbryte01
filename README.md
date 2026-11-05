# SmartBryte01

Responsive homepage for **SmartBryte**, an online school for children. A single static page (`index.html`) — no backend, accounts, payments or extra routes — built to the supplied implementation brief.

## Source materials (`/docs`)

Everything that informed the build lives in this repo:

| File | Role |
|---|---|
| `docs/SmartBryte_Complete_Homepage_Content.pdf` | **Single source of truth for all visible copy** (8 sections, used verbatim) |
| `docs/SmartBryte_Hero_and_Introduction_Content.pdf` | Earlier approved hero + introduction copy (superseded by the complete document) |
| `docs/Lovable_Online_School_Homepage_Build_Brief.pdf` | Implementation brief: scope, exact-copy contract, design synthesis |
| `docs/DESIGN-Quizlet.md` | Design reference — iris-violet accent, card discipline, soft shadows |
| `docs/DESIGN-SuperHi.md` | Design reference — paper-cut shapes, chalk-blue wash, pill components, mono labels |
| `docs/reference-insightpod-*.jpg` | Visual reference — warm cream canvas, editorial scale, amber CTA, dark band |
| `docs/reference-new-school.jpg` | Visual reference — staggered capsule media tiles, floating accents |

## Page structure (all 8 sections from the content document)

1. **Hero** — headline, intro line, both CTAs, "For learners aged 7-22." + capsule artwork
2. **Introduction to SmartBryte** — editorial white card
3. **Why Choose SmartBryte?** — 5 pastel feature cards
4. **Our Programmes** — Junior Learners (7-12), Teen Learners (13-19), Young Adults (20-22)
5. **How SmartBryte Benefits Students** — numbered benefit rows
6. **Testimonials** — heading + intro only (see notes)
7. **Frequently Asked Questions** — accessible native accordion (9 Q&As)
8. **Final Enrolment Call to Action** — violet band + Apply Now

## Run it

Any static server works, e.g.:

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

(Equally deployable to GitHub Pages, Netlify, Vercel — just serve the repo root.)

## Structure

- `index.html` — the homepage (header nav anchors to the real sections)
- `assets/styles.css` — the synthesized design system (tokens documented at the top of the file)
- `assets/script.js` — progressive enhancement only: scroll reveals, header elevation, gentle hero parallax

## Implementation notes (from the brief)

- **Copy fidelity:** every visible word comes from the complete content PDF, unchanged — verified programmatically against the PDF. Section names from the document are used as small eyebrow labels / nav links. Document furniture (page headers, numbers, "Button:" prefixes) is not rendered.
- **CTA wiring:** *"Explore Our Programmes"*, *"Apply Now"* (hero + header) and *"Discover SmartBryte"* now anchor to the matching sections that exist on the page (`#our-programmes`, `#enrol`, `#why-choose-smartbryte`). The three programme buttons (*Explore Junior/Teen Learners, Explore Young Adults*) and the final *"Apply Now"* have no supplied destination yet, so they remain honest static buttons with `IMPLEMENTATION NOTE` comments in `index.html`. The `.btn` styles work unchanged on `<a>` when real URLs exist.
- **Testimonials (SAMPLES — replace before launch):** the content document instructs *"Add verified testimonials from real parents and students once the school has begun operating. Do not publish invented reviews."* At the owner's direction, three drafted sample testimonials (reviewed and approved by the owner on 2026-11-05) are rendered so the design can be judged complete. They are **not real families** — replace the text with genuine, consented testimonials before any public launch. A matching warning lives in a code comment above the section in `index.html`.
- **Editorial note in the PDF:** the document is marked a practice/MVP draft — verify operational claims, tuition details, teacher information and certificates before a public launch.
- **Imagery (AI-generated placeholders — replace before launch):** per the owner's request for photography reflecting an African audience, the hero capsule tiles and testimonial avatars use AI-generated portraits of dark-skinned African learners/parents (`assets/images/`). They are **not SmartBryte students or parents**; swap the six image files for consented photos of real families before a public launch — each `.tile` is a drop-in media slot (portrait orientation, faces near the top work best).
- **Accessibility:** semantic landmarks, one `h1`, skip link, visible focus states, native `<details>` FAQ (keyboard-friendly, no JS required), `prefers-reduced-motion` support, decorative art hidden from assistive tech.
