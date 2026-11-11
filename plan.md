# Rebuild Plan: balvindersingh.com

Personal site and consulting storefront for Balvinder Singh, repositioned from
"generic Data Expert portfolio" to "Data Engineer -> LLM / AI Engineer and Consultant".

## 0. Current state (verified, Nov 2026)

Facts confirmed by inspecting the repo before the reset:

- Old stack: Jekyll on the `github-pages` gem, portfolYOU-style scaffolding
  (`_config.yml`, `Gemfile`, `_layouts/`, `_includes/`, `_sass/`, `_data/`, collections).
- Hosting: GitHub Pages user-site repo (`iAmBalvinder/iambalvinder.github.io`)
  with custom domain via `CNAME` (`balvindersingh.com`, `www.balvindersingh.com`).
- Content reality: `_posts/` and `_projects/` contained only dot-prefixed (hidden)
  portfolYOU sample files (e.g. `.2015-09-25-how-to-undo-your-git-failure.md`);
  only `pages/about.md` had real prose. Nothing content-wise needed salvaging.
- CI/CD: no `.github/workflows/` existed. The site relied on GitHub Pages' default
  Jekyll build.
- Only real assets: `assets/resume.pdf`, `images/01.jpg` (headshot), `assets/favicon.ico`.

### What was done in the reset

| Action | Detail |
| --- | --- |
| Archived | Tag `legacy-jekyll` pushed to origin (full old site, recoverable at any time) |
| Kept | `.git/` (history intact), `CNAME` (moved to `public/`), `assets/resume.pdf` -> `public/assets/`, `images/01.jpg` -> `public/images/`, `favicon.ico` -> `public/` (placeholder until rebrand) |
| Wiped | All Jekyll scaffolding: `_config.yml`, `Gemfile`, layouts/includes/sass, `_data/`, empty `_posts/` + `_projects/`, `articles/`, `pages/`, `index.html`, `404.html`, `search.json`, `docs/`, `.DS_Store` |
| Note | No `LICENSE` file ever existed in this repo. Add an MIT license in Phase 1 if desired (irrelevant for a personal site but harmless) |

## 1. Finalized tech stack

**Astro (v7 current) + TypeScript (strict) + Tailwind CSS 4 + pnpm, deployed to GitHub Pages via GitHub Actions.**

Verified against the 2026 ecosystem:

- Astro is at v6 (Rust-based Markdown core, faster builds; Content Layer API for
  file-based collections). MIT-licensed. Astro's parent company was acquired by
  Cloudflare in Jan 2026, but Astro remains open source and host-agnostic - no lock-in.
- Tailwind v4 is integrated natively as a Vite plugin (`@tailwindcss/vite`).
  The old `@astrojs/tailwind` integration is deprecated - do not use it.
- Official deploy path: `withastro/action@v6` + `actions/deploy-pages@v5`
  (`actions/checkout@v7`), Node 24.
- Forms: Formspree or Basin (static-friendly) in Phase 3; Calendly link as CTA.
  No backend required in v1.
- Analytics: defer to Phase 3; if added, prefer privacy-first (Plausible or
  self-hosted Umami) over GA4 to avoid consent-banner complexity.

### Decision log (alternatives considered and rejected)

| Option | Verdict | Reason |
| --- | --- | --- |
| Astro 6 | **Chosen** | Content-first, zero JS by default, content collections with typed frontmatter, MDX when needed, fast builds, great Core Web Vitals out of the box |
| Keep Jekyll | Rejected | Aging toolchain, slower design iteration, weaker component model; only advantage is zero migration effort, which no longer applies |
| Next.js | Rejected | App-first, ships a React runtime; overkill for a brochure/consulting site with no dynamic needs |
| Eleventy / Hugo | Rejected | Both excellent, but Eleventy lacks built-in content/component ergonomics and Hugo requires Go-template fluency; Astro's TS + collections model is more maintainable here |
| Headless CMS (Sanity/Contentful) | Rejected for v1 | Cost and complexity; file-based content in git is fully sufficient and consulting-friendly |
| Framer / Webflow | Rejected | Subscription cost + lock-in; undermines the engineering credibility the site is meant to project |

### Non-goals for v1

- Headless CMS, auth, dashboards, server endpoints, or heavy client-side interactivity.
- Client-side site search (old `search.json` dropped; revisit with Pagefind if the
  writing section grows past ~50 posts).
- Newsletter infrastructure (link out to Buttondown/Substack instead).

## 2. Positioning

- **Core message:** Help teams move from data platforms to production LLM/AI
  systems - reliably, securely, and measurably. The data engineering background is
  the differentiator: most LLM work fails on the data layer, not the model layer.
- **Audience:** engineering leaders, heads of data, startup founders who need
  RAG/eval pipelines and LLM apps that actually reach production.
- **Primary CTA on every page:** book a call / contact.

### Site map

| Page | Purpose |
| --- | --- |
| Home | Value prop, who I help, core offers, proof points, primary CTA |
| Services | Consulting offers: LLM app architecture, RAG + eval pipelines, data-to-AI modernization, LLMOps enablement, strategy and roadmap |
| Case Studies | 2-4 outcome-focused writeups: problem, approach, architecture, impact metrics, stack. Anonymized as needed |
| Writing | Practical posts: LLM engineering, evals, retrieval, data quality for AI, deployment patterns. Builds authority and SEO |
| About | Transition story (data engineering -> AI/LLM systems), principles, experience highlights |
| Contact | CTA, booking link, email/socials, short intake questions |
| 404 | Branded, with links back to key pages |

## 3. Repository layout (target state)

```
.
├── .github/
│   └── workflows/
│       └── deploy.yml            # build + deploy to GitHub Pages
├── public/                       # copied verbatim to dist/
│   ├── CNAME                     # balvindersingh.com (already in place)
│   ├── favicon.ico               # placeholder - replace in Phase 2
│   ├── images/                   # unoptimized images (01.jpg placeholder headshot)
│   └── robots.txt
├── src/
│   ├── assets/                   # images optimized via astro:assets
│   ├── components/               # Header, Footer, Card, Prose, etc.
│   ├── content/
│   │   ├── services/             # one .md per service
│   │   ├── case-studies/         # one .md per case study
│   │   ├── writing/              # blog posts (.md, .mdx optional)
│   │   └── config.ts             # collection + zod schemas (src/content.config.ts in Astro 6)
│   ├── data/
│   │   └── site.ts               # single source of truth: nav, socials, contact, meta
│   ├── layouts/
│   │   ├── Base.astro            # <html>, SEO head, fonts, global styles
│   │   └── Post.astro
│   ├── pages/                    # index.astro, about.astro, contact.astro, 404.astro,
│   │                             # writing/[...slug].astro, case-studies/[...slug].astro
│   └── styles/global.css         # Tailwind v4 entry (@import "tailwindcss"; @theme tokens)
├── astro.config.mjs
├── package.json
├── pnpm-lock.yaml
├── plan.md
└── README.md
```

## 4. Deployment configuration

- `astro.config.mjs`: `site: 'https://balvindersingh.com'`, no `base` (root domain).
- `public/CNAME` ships into `dist/` automatically so the custom domain survives every deploy.
- One-time GitHub settings change: **Settings -> Pages -> Build and deployment ->
  Source: GitHub Actions** (the old "deploy from branch" mode must be switched off).
- Branch note: this repo's default branch is `master` (not `main`). The workflow
  below targets `master`. Optionally rename to `main` later; if so, update the trigger.
- DNS is already pointed at GitHub Pages from the previous site; verify it still
  resolves and that "Enforce HTTPS" is checked in Pages settings after first deploy.

### `.github/workflows/deploy.yml`

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [master]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7
      - uses: withastro/action@v6
        with:
          node-version: 24

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - id: deployment
        uses: actions/deploy-pages@v5
```

## 5. Content model (typed collections)

Schemas enforced with zod in the content config, so bad frontmatter fails the build:

```ts
// case-studies: title, description, publishDate, client (e.g. "Series-B logistics company"),
//   industry, timeframe, services[], stack[], outcomes[{ metric, before?, after }], draft
// services:     title, description, order, deliverables[], timeline, faqs[]?
// writing:      title, description, publishDate, tags[], draft, ogImage?
```

- Drafts are excluded in production builds via `draft: true`.
- RSS via `@astrojs/rss`, sitemap via `@astrojs/sitemap`, both wired to `site`.
- URL convention mirrors the old site where sensible: `/writing/:slug/`,
  `/case-studies/:slug/`, `/services/:slug/`.

## 6. Design system (Tailwind 4)

- Tailwind v4 entry in `src/styles/global.css` with `@theme` design tokens
  (colors, type scale, spacing) - no config file needed.
- Component layer: a small set of Astro components (Header, Footer, Card, Tag,
  CTASection, Prose). No React, no islands in v1 - the site ships zero JS.
- Dark mode via `prefers-color-scheme` (media strategy; no toggle in v1).
- Typography: self-hosted via Fontsource (one variable font + one mono) to avoid
  render-blocking third-party requests.
- Accessibility baseline: WCAG AA contrast, visible focus states, semantic
  landmarks, `prefers-reduced-motion` respected.

## 7. SEO and trust requirements

- Per-page `title`, `description`, canonical URL, Open Graph + Twitter cards.
- Static OG image (1200x630) in Phase 2; auto-generated per-post OG images
  (satori) is a stretch goal, not a v1 requirement.
- JSON-LD: `Person` on about/home, `Article`/`BlogPosting` on posts, `Service` on services.
- `robots.txt` referencing the sitemap; RSS feed linked in the head.
- Trust elements when available: testimonials, logos, GitHub/LinkedIn links,
  downloadable one-page consulting profile (derive from `public/assets/resume.pdf`).

## 8. Phases

### Phase 0 - Reset (done)
Archive tag pushed, Jekyll wiped, assets preserved, this plan written.

### Phase 1 - Scaffold and ship a v1 (done, Nov 2026)
- [x] `pnpm` project: Astro 7.4, TypeScript strict (`astro check` pinned to TS 6 while it lacks TS 7 support), `@tailwindcss/vite`, `@astrojs/sitemap`, `@astrojs/rss`
- [x] `astro.config.mjs` with `site`, integrations, trailingSlash defaults
- [x] Base layout, Header, Footer, design tokens (dark-only palette in v1)
- [x] Home, About, Contact, 404
- [x] `deploy.yml` checked in; flip Pages source to "GitHub Actions" (repo owner step)
- [ ] First successful production deploy on https://balvindersingh.com

Exit criteria met: site builds green, zero JS shipped, RSS + sitemap generated.

### Phase 2 - Content engine (done, Nov 2026)
- [x] Content collections + zod schemas for services, case-studies, writing (`src/content.config.ts`)
- [x] Services page from collection; 4 services defined
- [x] 3 case studies written (problem -> approach -> outcomes; anonymized, metrics are placeholders to be validated against real engagements)
- [x] Writing section: 2 launch posts, RSS with live items, sitemap, pagination (`/writing/[...page].astro`, 8/page)
- [x] SEO pass: meta/canonical/OG components with static OG image (`public/images/og-default.png`, regenerated by `scripts/generate_og.py`), JSON-LD (`Person`, `BlogPosting`, `Article`, `Service`), `favicon.svg` + PNG icons + apple-touch-icon, `robots.txt`
- [ ] Replace placeholder headshot (`public/images/01.jpg`) and resume with final brand assets (owner-provided photography/PDF)

Exit criteria met: 16 pages build green; `pnpm check` reports 0 errors; bad frontmatter fails the build.

Astro 7 gotcha discovered: paginated `props` do not reach `Astro.props` when
pagination lives on a plain `index.astro` route (no dynamic segments). Using the
standard `writing/[...page].astro` rest-param route works correctly. Worth
reporting upstream; not a blocker.

### Phase 3 - Trust and conversion
- [ ] Lead capture: Formspree/Basin form on Contact, Calendly link as primary CTA, mailto fallback
- [ ] Testimonials/logos section (when available)
- [ ] Downloadable one-page consulting profile
- [ ] Analytics (optional, privacy-first: Plausible or Umami)
- [ ] Performance and a11y audit: Lighthouse 95+ on all categories
- [ ] Optional: Lighthouse CI in the workflow, Renovate for dependency updates

Exit criteria: a stranger can understand the offer and book a call in under 2 minutes.

### Phase 4 - Operate
- [ ] Publishing cadence (biweekly writing target), content backlog in repo issues
- [ ] Quarterly dependency and design refresh
- [ ] Revisit stretch goals: MDX in posts, per-post OG images, Pagefind search, newsletter

## 9. Success criteria

- Lighthouse >= 95 across performance, accessibility, best practices, SEO on all templates.
- Zero JavaScript on base pages (no islands until something truly needs it).
- Full page weight under ~200 KB for text pages.
- All SEO tags, sitemap, RSS, and structured data validate.
- Deploy from push-to-`master` in under 3 minutes of CI time.
- Site clearly positions the data -> AI/LLM transition within 10 seconds of landing.
