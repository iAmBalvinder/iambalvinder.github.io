# balvindersingh.com

Personal site and consulting storefront for Balvinder Singh - data engineering to
LLM/AI engineering and consulting.

- Build plan: see [plan.md](./plan.md)
- Stack: Astro 6 + TypeScript + Tailwind CSS 4, deployed to GitHub Pages via GitHub Actions
- Legacy: the old Jekyll site is archived on the `legacy-jekyll` tag

## Development

```sh
pnpm install
pnpm dev      # local dev server
pnpm build    # production build to dist/
pnpm preview  # preview the production build
```

Deployment is automatic: push to `master` and the deploy workflow builds and
publishes to GitHub Pages (Source must be set to "GitHub Actions" in repo settings).
