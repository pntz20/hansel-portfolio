# Portfolio Upgrade Suggestions

Last updated: 2026-07-01
Reference repo: `E:\hansel-portfolio`

## Notes about Hansel
- Starting to integrate AI into his general workflow
- Site focuses on web development + automation engineering
- Currently using an embedded local n8n form for contact

---

## Low Effort / High Impact

- [ ] Replace placeholder social links in footer (`href="#"` for LinkedIn/GitHub) with real profiles.
- [ ] Make contact email consistent across meta tags, footer, and any fallback copy.
- [x] Replace/verify the n8n embed `http://localhost:5678/...` with a public URL or hosted fallback form.
  Implemented `contact.html` using `mailto:` so messages open in the visitor's email client.
- [ ] Update meta title/description/OG copy to reflect current focus.
- [ ] Add `og:image` and `twitter:image`.
- [ ] Ensure `https` for CDNs, external assets, and form embeds; add `rel="noopener"` to external links.

## Medium Effort

- [ ] Extract inline `style="..."` attributes in `index.html` into classes in `style.css` for maintainability.
- [ ] Add a **Projects** section with 3–6 cards: title, outcome, tech tags, and links.
- [ ] Tighten experience bullets to one measurably specific result each.
- [ ] Add a working download flow for the resume PDF, or host a real `.pdf`.
- [ ] Add basic accessibility: skip-to-content link, meaningful button labels, visible focus states.
- [ ] Add preconnect hint for Google Fonts and a solid local fallback font stack.

## Higher Effort / Strongest Upgrades

- [ ] Add a **success metrics summary** near the top (e.g., years active, projects, time saved).
- [ ] Add a minimal **dark mode** toggle/style set.
- [ ] Convert repeated experience-card markup into reusable components via JS or templating.
- [ ] Add a **blog/research** page if AI agent work expands; good signal for recruiters.
- [ ] Add a **testimonials/references** block if permission allows.

---

## Quick Next Steps
1. Start with social/contact/SEO cleanup.
2. Then extract inline styles into `style.css`.
3. Then add the Projects section.
