# learnscripting.org

Beginner-friendly articles on Python, Bash, PowerShell and JavaScript scripting. The site is built with [Astro](https://astro.build) as a static site.

## Run it locally

```powershell
npm install
npm run dev
```

Then open http://localhost:4321.

| Command           | What it does                         |
| ----------------- | ------------------------------------ |
| `npm run dev`     | Start the dev server with live reload |
| `npm run build`   | Build the static site into `dist/`   |
| `npm run preview` | Serve the built `dist/` folder       |

## Write a new article

Add a Markdown file to `src/content/articles/`. The file name becomes the URL (`my-post.md` becomes `/articles/my-post/`).

```markdown
---
title: My new article
description: One sentence shown on cards and in search results.
lang: python        # general | python | bash | powershell | javascript
pubDate: 2026-12-01
# step: 6           # optional: adds it to the beginner path, in this order
# draft: true       # optional: only shown in `npm run dev`
---

Your article in Markdown...
```

### Schedule posts ahead of time

Give an article a **future `pubDate`**. It stays hidden on the live site until that date, then goes live on its own. GitHub Actions rebuilds the site every day at 00:30 UTC, which you can change in `deploy.yml`. In `npm run dev` you can still see scheduled posts so you can preview them.

To post every day, write a batch of articles, give each one the next date (`2026-12-01`, `2026-12-02`, …) and push them all at once.

Reading time is calculated automatically. Code blocks get syntax highlighting and a Copy button.

**Callout boxes:** use plain HTML in the Markdown, with blank lines around the inner text:

```html
<div class="callout plain">        <!-- plain | try | warn -->
<p class="callout-title">In plain English</p>

Text in **Markdown** here.

</div>
```

## WordPress import

The old WordPress posts were imported with `scripts/wp_import.py`:

```powershell
python -m pip install --user -r scripts/requirements.txt
```
```powershell
python scripts/wp_import.py "$HOME\Downloads\learnscripting.WordPress.2026-11-25.xml"
```

- Posts go to `src/content/articles/wordpress/` (drafts get `draft: true`), and pages go to `src/content/pages/`.
- Imported posts **keep their old URL** (`/post-name/`). Old `/category/<name>/` links redirect to `/topics/<name>/`.
- Images are saved to `public/images/wp/`. Images that no longer exist anywhere are removed from the posts and listed in `scripts/failed-images.txt`. If you have a backup of `wp-content/uploads`, add `--uploads-dir path\to\uploads` to bring them back.
- Re-running the script **overwrites** everything in those two folders. Once you start editing imported posts by hand, don't run it again.

## Project layout

```
src/
  content/articles/   Markdown articles
  content.config.ts   Article front-matter schema
  data/site.ts        Site name, languages, newsletter URL
  data/articles.ts    Helpers: sorting, beginner path, reading time
  layouts/Base.astro  Page shell (head, header, footer)
  components/         Header, Footer, ArticleCard, HelloTabs, Newsletter
  pages/              Home, /articles, /articles/<slug>, /<language>, /about, 404
  styles/global.css   Design tokens and shared styles
```

## Deploy

`.github/workflows/deploy.yml` builds the site and publishes it to GitHub Pages on every push to `main`. `public/CNAME` points the site at `learnscripting.org`. To switch it on:

1. Push this repo to GitHub.
2. In the repo, go to **Settings → Pages** and set **Source** to **GitHub Actions**.
3. At your domain registrar, point `learnscripting.org` at GitHub Pages: add A records for the apex domain, or a CNAME record for `www`.

## To do

- Set `newsletterAction` in `src/data/site.ts` to your newsletter provider's form URL.
- Fill in the About page with who runs the site.
