"""Import a WordPress export (WXR .xml) into the Astro site.

Usage (from the project root):
    python -m pip install --user -r scripts/requirements.txt
    python scripts/wp_import.py path/to/learnscripting.WordPress.xml [--no-images]
        [--uploads-dir path/to/backup/wp-content/uploads]

What it does:
  * published + draft posts  -> src/content/articles/wordpress/<slug>.md
  * published pages          -> src/content/pages/<slug>.md
  * <img> files              -> public/images/wp/   (links rewritten). Images are taken
                                 from --uploads-dir when given, else downloaded. Images that
                                 can't be found are removed (listed in scripts/failed-images.txt).
  * category map for old /category/<name>/ URLs -> src/data/wp-categories.json

Imported posts keep their old URL (/<slug>/). Re-running is safe: files are
overwritten and images that were already downloaded are skipped.
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import hashlib
import html
import json
import os
import re
import sys
import unicodedata
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString
from markdownify import MarkdownConverter

ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / "src" / "content" / "articles" / "wordpress"
PAGES_DIR = ROOT / "src" / "content" / "pages"
IMG_DIR = ROOT / "public" / "images" / "wp"
CAT_MAP_FILE = ROOT / "src" / "data" / "wp-categories.json"

SITE_HOSTS = ("learnscripting.org", "www.learnscripting.org")
SKIP_PAGES = {"sample-page"}
# Slugs used by the new site's own routes; an imported item may not take them.
RESERVED = {"python", "bash", "powershell", "javascript", "articles", "about", "topics",
            "category", "images", "404", "sitemap-index"}

NS = {
    "wp": "http://wordpress.org/export/1.2/",
    "content": "http://purl.org/rss/1.0/modules/content/",
    "excerpt": "http://wordpress.org/export/1.2/excerpt/",
    "dc": "http://purl.org/dc/elements/1.1/",
}

# WordPress category name -> nicer display name. Anything not listed is kept as-is.
CATEGORY_RENAME = {
    "Java Script": "JavaScript",
    "ANSIBLE": "Ansible",
    "Html": "HTML",
    "Postgresql": "PostgreSQL",
    "PythonSelenium": "Python Selenium",
}
DROP_CATEGORIES = {"Uncategorized", "Uncategorised"}

# Display category -> the site's language tracks.
CATEGORY_TO_LANG = {
    "Python": "python",
    "Django": "python",
    "Pytest": "python",
    "Python Selenium": "python",
    "Shell Scripting": "bash",
    "Linux": "bash",
    "JavaScript": "javascript",
}

# Display category -> code-fence language when a block doesn't say.
CATEGORY_TO_CODE = {
    "Python": "python", "Django": "python", "Pytest": "python", "Python Selenium": "python",
    "Machine Learning": "python", "Shell Scripting": "bash", "Linux": "bash",
    "JavaScript": "javascript", "Groovy": "groovy", "Java": "java", "C++": "cpp", "C": "c",
    "Go": "go", "HTML": "html", "CSS": "css", "PostgreSQL": "sql", "Database": "sql",
    "Ansible": "yaml", "Ruby": "ruby", "VB Scripting": "vb", "Selenium": "java",
}
ENLIGHTER_LANG = {"shell": "bash", "js": "javascript", "generic": "", "raw": "", "csharp": "csharp",
                  "cpp": "cpp", "c": "c", "java": "java", "python": "python", "sql": "sql",
                  "html": "html", "css": "css", "xml": "xml", "json": "json", "yaml": "yaml",
                  "groovy": "groovy", "go": "go", "ruby": "ruby", "php": "php", "powershell": "powershell"}

BLOCK_TAGS = r"(?:table|thead|tfoot|caption|col|colgroup|tbody|tr|td|th|div|dl|dd|dt|ul|ol|li|pre|form|map|area|blockquote|address|math|style|p|h[1-6]|hr|fieldset|legend|section|article|aside|hgroup|header|footer|nav|figure|figcaption|details|menu|summary)"
LT = "\uE000"  # placeholder for a literal "<" in text (so Markdown doesn't read it as HTML)


# ---------------------------------------------------------------- helpers

def text(item, tag):
    return item.findtext(tag, default="", namespaces=NS) or ""


def slugify(value: str) -> str:
    value = urllib.parse.unquote(value)
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    value = re.sub(r"[^a-zA-Z0-9]+", "-", value).strip("-").lower()
    return value[:90].strip("-") or "untitled"


def fix_mojibake(s: str) -> str:
    """The export contains U+FFFD where curly quotes / nbsp were lost."""
    s = re.sub(r"(?<=[A-Za-z])\uFFFD(?=[A-Za-z])", "\u2019", s)
    return s.replace("\uFFFD", " ")


def iso_date(local: str, gmt: str) -> str | None:
    for value, tz in ((gmt, timezone.utc), (local, None)):
        if value and not value.startswith("0000"):
            dt = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
            if tz:
                return dt.replace(tzinfo=tz).strftime("%Y-%m-%dT%H:%M:%SZ")
            return dt.strftime("%Y-%m-%dT%H:%M:%S")
    return None


def yaml_str(s: str) -> str:
    return json.dumps(s, ensure_ascii=False)


def is_site_url(url: str) -> bool:
    host = urllib.parse.urlparse(url).netloc.lower()
    return host in SITE_HOSTS


# ---------------------------------------------------------------- images

def image_filename(url: str) -> str:
    path = urllib.parse.urlparse(url).path
    stem, ext = os.path.splitext(os.path.basename(urllib.parse.unquote(path)))
    ext = ext.lower() if ext.lower() in {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".avif"} else ".jpg"
    digest = hashlib.sha1(url.encode()).hexdigest()[:8]
    return f"{slugify(stem)[:60]}-{digest}{ext}"


UPLOADS_DIR: Path | None = None


def from_backup(url: str, dest: Path) -> bool:
    """Copy a /wp-content/uploads/ image from a local backup folder, if we have one."""
    path = urllib.parse.unquote(urllib.parse.urlparse(url).path)
    if UPLOADS_DIR is None or "/wp-content/uploads/" not in path:
        return False
    rel = path.split("/wp-content/uploads/", 1)[1]
    full = re.sub(r"-\d+x\d+(\.\w+)$", r"", rel)  # "photo-300x200.jpg" -> "photo.jpg"
    for candidate in (rel, full):
        src = UPLOADS_DIR / candidate
        if src.is_file():
            dest.write_bytes(src.read_bytes())
            return True
    return False


def download_image(url: str) -> tuple[str, str | None]:
    """Returns (url, local public path or None on failure)."""
    name = image_filename(url)
    dest = IMG_DIR / name
    if dest.exists() and dest.stat().st_size > 0:
        return url, f"/images/wp/{name}"
    if from_backup(url, dest):
        return url, f"/images/wp/{name}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (site-migration script)"})
        with urllib.request.urlopen(req, timeout=20) as resp:
            ctype = resp.headers.get("Content-Type", "")
            data = resp.read()
        if not ctype.startswith("image/") or not data:
            return url, None
        dest.write_bytes(data)
        return url, f"/images/wp/{name}"
    except Exception:
        return url, None


def collect_image_urls(bodies: list[str]) -> set[str]:
    urls = set()
    for body in bodies:
        for m in re.finditer(r"<img[^>]+?src=[\"']([^\"']+)[\"']", body, flags=re.I):
            url = html.unescape(m.group(1)).strip()
            if url.startswith("//"):
                url = "https:" + url
            if url.startswith("http"):
                urls.add(url)
    return urls


# ---------------------------------------------------------------- content

def autop(body: str) -> str:
    """Minimal port of WordPress' wpautop() for classic-editor posts."""
    pres: list[str] = []

    def keep(m):
        pres.append(m.group(0))
        return f"\n\n<!--PRE{len(pres) - 1}-->\n\n"

    body = re.sub(r"<pre[\s\S]*?</pre>", keep, body, flags=re.I)
    body = body.replace("\r\n", "\n")
    out = []
    for chunk in re.split(r"\n\s*\n", body):
        chunk = chunk.strip()
        if not chunk:
            continue
        if re.match(rf"^<!--PRE\d+-->$", chunk) or re.match(rf"^</?{BLOCK_TAGS}[\s>/]", chunk, flags=re.I):
            out.append(chunk)
        else:
            out.append("<p>" + chunk.replace("\n", "<br />\n") + "</p>")
    body = "\n\n".join(out)
    return re.sub(r"<!--PRE(\d+)-->", lambda m: pres[int(m.group(1))], body)


def shortcodes_to_html(body: str) -> str:
    def code(m):
        attrs, inner = m.group(2) or "", m.group(3)
        lang = re.search(r"(?:lang|language)=[\"']?([\w+#-]+)", attrs)
        cls = f' class="language-{lang.group(1).lower()}"' if lang else ""
        return f"<pre><code{cls}>{inner}</code></pre>"

    body = re.sub(r"\[(source|sourcecode|code)((?:\s[^\]]*)?)\]([\s\S]*?)\[/\1\]", code, body)
    body = re.sub(r"\[caption[^\]]*\]([\s\S]*?)\[/caption\]", r"\1", body)
    body = re.sub(r"\[/?(?:embed|gallery)[^\]]*\]", "", body)
    return body


class Converter(MarkdownConverter):
    pass


def to_markdown(body: str, code_lang: str, images: dict[str, str], missing: set[str]) -> str:
    body = fix_mojibake(body)
    is_classic = "<!-- wp:" not in body
    body = re.sub(r"<!--\s*/?wp:[\s\S]*?-->", "", body)
    body = shortcodes_to_html(body)
    if is_classic:
        body = autop(body)

    soup = BeautifulSoup(body, "html.parser")
    for junk in soup.find_all(["script", "style", "noscript"]):
        junk.decompose()

    # Code blocks -> placeholders, filled in after Markdown conversion.
    blocks: list[str] = []
    for pre in soup.find_all("pre"):
        lang = ""
        if pre.get("data-enlighter-language") is not None:
            lang = ENLIGHTER_LANG.get(pre["data-enlighter-language"].lower(), "")
        else:
            code_el = pre.find("code")
            m = re.search(r"language-([\w+#-]+)", " ".join((code_el or pre).get("class", [])))
            if m:
                lang = ENLIGHTER_LANG.get(m.group(1), m.group(1))
            elif "wp-block-code" in pre.get("class", []) or code_el is not None:
                lang = code_lang
        for br in pre.find_all("br"):
            br.replace_with("\n")
        code = pre.get_text().replace("\u00a0", " ").strip("\n")
        if not code.strip():
            pre.decompose()
            continue
        fence = "~~~~" if "```" in code else "```"
        blocks.append(f"{fence}{lang}\n{code}\n{fence}")
        pre.replace_with(soup.new_string(f"\n\nCODEBLOCK{len(blocks) - 1}X\n\n"))

    # Embeds (YouTube etc.) -> a plain link.
    for fig in soup.select("figure.wp-block-embed, figure[class*=wp-block-embed]"):
        url = fig.get_text(" ", strip=True).split(" ")[0]
        if url.startswith("http"):
            new = soup.new_tag("p")
            a = soup.new_tag("a", href=url)
            a.string = "Watch the video" if "youtu" in url else url
            new.append(a)
            fig.replace_with(new)
    for iframe in soup.find_all("iframe"):
        src = iframe.get("src", "")
        if src.startswith("http"):
            a = soup.new_tag("a", href=src)
            a.string = "Open embedded content"
            iframe.replace_with(a)
        else:
            iframe.decompose()

    # Images: point at the downloaded copy.
    for img in soup.find_all("img"):
        src = html.unescape(img.get("src", "")).strip()
        if src.startswith("//"):
            src = "https:" + src
        if src in missing:
            # Gone from the web and not in the backup: drop it rather than show a broken icon.
            parent = img.parent
            img.decompose()
            if parent is not None and parent.name in ("a", "figure", "p") and not parent.get_text(strip=True)                     and not parent.find("img"):
                parent.decompose()
            continue
        img["src"] = images.get(src, src)
        for attr in ("srcset", "sizes", "data-original", "class", "width", "height", "loading"):
            img.attrs.pop(attr, None)
        if not img.get("alt"):
            img["alt"] = ""

    # Links to the old site -> root-relative (same URLs on the new site).
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        if is_site_url(href):
            parsed = urllib.parse.urlparse(href)
            if not parsed.path.startswith("/wp-content/"):
                a["href"] = parsed.path + (f"#{parsed.fragment}" if parsed.fragment else "") or "/"

    # Protect literal "<" in prose so Markdown doesn't treat List<String> as a tag.
    for node in soup.find_all(string=True):
        if isinstance(node, NavigableString) and "<" in node and node.parent.name not in ("code", "pre"):
            node.replace_with(node.replace("<", LT))

    md = Converter(heading_style="ATX", bullets="-", strip=["span"]).convert_soup(soup)

    md = md.replace(LT, "&lt;")
    md = re.sub(r"\\?CODEBLOCK(\d+)X", lambda m: "\n\n" + blocks[int(m.group(1))] + "\n\n", md)
    md = md.replace("\u00a0", " ")
    md = re.sub(r"^(#{1,6})\s*\*\*(.+?)\*\*\s*$", r"\1 \2", md, flags=re.M)  # "## **Title**"
    md = re.sub(r"^#{1,6}\s*$", "", md, flags=re.M)  # empty headings
    md = re.sub(r"[ \t]+\n", "\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip() + "\n"


def summary(md: str, limit: int = 155) -> str:
    plain = re.sub(r"```[\s\S]*?```|~~~~[\s\S]*?~~~~", " ", md)
    plain = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", plain)
    plain = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", plain)
    plain = re.sub(r"[#>*_`|\\-]+", " ", plain)
    plain = html.unescape(re.sub(r"\s+", " ", plain)).strip()
    if len(plain) <= limit:
        return plain or "An article from LearnScripting."
    cut = plain[:limit].rsplit(" ", 1)[0]
    return cut.rstrip(",.;:") + "…"


# ---------------------------------------------------------------- main

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("xml", type=Path)
    ap.add_argument("--no-images", action="store_true", help="don't download images; keep remote URLs")
    ap.add_argument("--uploads-dir", type=Path, help="local backup of wp-content/uploads to copy images from")
    args = ap.parse_args()
    global UPLOADS_DIR
    UPLOADS_DIR = args.uploads_dir

    channel = ET.parse(args.xml).getroot().find("channel")
    authors = {text(a, "wp:author_login"): text(a, "wp:author_display_name")
               for a in channel.findall("wp:author", NS)}
    items = channel.findall("item")

    wanted = []
    for it in items:
        ptype, status = text(it, "wp:post_type"), text(it, "wp:status")
        if ptype == "post" and status in ("publish", "draft"):
            wanted.append(it)
        elif ptype == "page" and status == "publish" and text(it, "wp:post_name") not in SKIP_PAGES:
            wanted.append(it)

    images: dict[str, str] = {}
    missing: set[str] = set()
    if not args.no_images:
        IMG_DIR.mkdir(parents=True, exist_ok=True)
        urls = collect_image_urls([text(it, "content:encoded") for it in wanted])
        print(f"Downloading {len(urls)} images…")
        failed = []
        with cf.ThreadPoolExecutor(max_workers=8) as pool:
            for url, local in pool.map(download_image, sorted(urls)):
                if local:
                    images[url] = local
                else:
                    failed.append(url)
        missing = set(failed)
        print(f"  saved {len(images)}, not found {len(failed)} (removed from posts, see scripts/failed-images.txt)")
        if failed:
            (ROOT / "scripts" / "failed-images.txt").write_text("\n".join(failed) + "\n", encoding="utf-8")

    for d in (POSTS_DIR, PAGES_DIR):
        d.mkdir(parents=True, exist_ok=True)
        for old in d.glob("*.md"):
            old.unlink()

    used: set[str] = set(RESERVED)
    native = {p.stem for p in (ROOT / "src" / "content" / "articles").glob("*.md")}
    used |= native
    cat_map: dict[str, str] = {}
    counts = {"post": 0, "draft": 0, "page": 0}

    for it in wanted:
        ptype, status = text(it, "wp:post_type"), text(it, "wp:status")
        title = fix_mojibake(html.unescape(it.findtext("title") or "")).strip() or "Untitled"
        # Keep the WordPress slug exactly (old URLs must keep working); only clean up odd ones.
        raw = urllib.parse.unquote(text(it, "wp:post_name"))
        slug = raw if re.fullmatch(r"[^\W_]?[\w-]+", raw, flags=re.UNICODE) and len(raw) <= 150 else slugify(raw or title)
        if status == "draft" and not text(it, "wp:post_name"):
            slug = "draft-" + slug
        base, n = slug, 2
        while slug in used:
            slug, n = f"{base}-{n}", n + 1
        used.add(slug)

        cats = []
        for c in it.findall("category"):
            if c.get("domain") != "category" or not c.text:
                continue
            name = CATEGORY_RENAME.get(c.text.strip(), c.text.strip())
            if name in DROP_CATEGORIES:
                continue
            if name not in cats:
                cats.append(name)
            cat_map[c.get("nicename", slugify(name))] = slugify(name)

        lang = next((CATEGORY_TO_LANG[c] for c in cats if c in CATEGORY_TO_LANG), "other")
        code_lang = next((CATEGORY_TO_CODE[c] for c in cats if c in CATEGORY_TO_CODE), "")
        body_md = to_markdown(text(it, "content:encoded"), code_lang, images, missing)

        pub = iso_date(text(it, "wp:post_date"), text(it, "wp:post_date_gmt")) \
            or iso_date(text(it, "wp:post_modified"), text(it, "wp:post_modified_gmt")) \
            or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        upd = iso_date(text(it, "wp:post_modified"), text(it, "wp:post_modified_gmt"))
        excerpt = fix_mojibake(html.unescape(re.sub(r"<[^>]+>", "", text(it, "excerpt:encoded")))).strip()
        author = authors.get(text(it, "dc:creator"), "")
        if author in ("", "master"):
            author = "LearnScripting"

        fm = [
            "---",
            f"title: {yaml_str(title)}",
            f"description: {yaml_str(excerpt or summary(body_md))}",
        ]
        if ptype == "post":
            fm += [
                f"lang: {lang}",
                f"categories: {json.dumps(cats, ensure_ascii=False)}",
                f"author: {yaml_str(author)}",
            ]
        fm += [f"pubDate: {pub}"]
        if upd and upd[:10] != pub[:10]:
            fm.append(f"updatedDate: {upd}")
        fm += ["legacy: true", f"wpId: {int(text(it, 'wp:post_id') or 0)}"]
        if status == "draft":
            fm.append("draft: true")
        fm.append("---")

        out_dir = POSTS_DIR if ptype == "post" else PAGES_DIR
        (out_dir / f"{slug}.md").write_text("\n".join(fm) + "\n\n" + body_md, encoding="utf-8")
        counts["page" if ptype == "page" else ("draft" if status == "draft" else "post")] += 1

    CAT_MAP_FILE.write_text(json.dumps(dict(sorted(cat_map.items())), indent=2) + "\n", encoding="utf-8")
    print(f"Imported {counts['post']} posts, {counts['draft']} drafts, {counts['page']} pages.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
