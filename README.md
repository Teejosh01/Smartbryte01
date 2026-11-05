# SmartBryte

One responsive school homepage. Plain HTML and CSS, native FAQ accordions,
local images, system fonts. No packages, build step or JavaScript runtime.

## Preview

```sh
python3 -m http.server 8000 --bind 0.0.0.0
```

Open http://localhost:8000. Check phone, tablet and desktop widths.

## Validate

```sh
python3 -m unittest discover -s tests
```

Checks HTML nesting, landmarks, local assets, anchors, FAQ/programme counts,
static-first behaviour, sample disclosures and Vercel configuration.

## Edit

- `index.html`: content and semantic structure.
- `assets/styles.css`: tokens, components and two responsive breakpoints.
- `assets/images/`: optimized local JPEGs.
- `docs/`: original content PDFs and historical design references.

The owner requested a simpler design and shorter copy in November 2026,
replacing the earlier verbatim-PDF presentation requirement. Programme details,
age ranges and FAQ answers remain; repeated labels, promotional taglines,
introductory section summaries and ornamental graphics were removed.

## Deploy

Vercel: connect this repository, select production branch `main`, use the
Other/static framework preset and repository root. `vercel.json` explicitly
sets static output to `.` without a build command. Merging to `main` triggers
production deployment **if the project's Git integration is enabled**.
Deployment success must be checked in Vercel; a Git merge alone is not proof.

For Netlify or GitHub Pages, serve the repository root as a static site.

## Before accepting applications

No application URL has been supplied. Enrolment links lead to the availability
notice, and programme cards have no nonfunctional buttons. Replace that notice
with an application link when the owner supplies a real destination.

The three testimonial quotes are owner-approved fictional samples, explicitly
labelled on the page. All six portraits/photos are AI-generated fictional people,
not SmartBryte families. Replace them with verified testimonials and consented
photography before marketing the page as evidence of actual student outcomes.
Verify school operational claims, certificates and tuition details before launch.
