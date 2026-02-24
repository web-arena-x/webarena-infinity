#!/usr/bin/env python3
"""
Download Procore v2 product manuals from https://v2.support.procore.com/product-manuals.

Usage:
    python scripts/download_procore_v2.py
    python scripts/download_procore_v2.py --dry-run
    python scripts/download_procore_v2.py --max-pages 50
"""

import argparse
import os
import re
import sys
import time
from pathlib import Path
from xml.etree import ElementTree

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

BASE_DIR = Path(__file__).resolve().parent.parent / "apps" / "user-manuals" / "procore-v2"

# ---------------------------------------------------------------------------
# HTTP fetcher
# ---------------------------------------------------------------------------

class Fetcher:
    def __init__(self, delay=0.5, max_retries=3):
        self.delay = delay
        self.max_retries = max_retries
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (compatible; MirrorMirrorBot/1.0)",
            "Accept": "text/html,application/xhtml+xml,application/xml",
            "Accept-Language": "en-US,en;q=0.9",
        })
        self._last = 0.0

    def get(self, url, **kwargs):
        elapsed = time.time() - self._last
        if elapsed < self.delay:
            time.sleep(self.delay - elapsed)
        for attempt in range(self.max_retries):
            try:
                self._last = time.time()
                resp = self.session.get(url, timeout=30, **kwargs)
                if resp.status_code == 429:
                    wait = float(resp.headers.get("Retry-After", 5 * (attempt + 1)))
                    print(f"  Rate limited, waiting {wait}s...")
                    time.sleep(wait)
                    continue
                resp.raise_for_status()
                return resp
            except requests.exceptions.RequestException as e:
                if attempt < self.max_retries - 1:
                    wait = 2 ** (attempt + 1)
                    print(f"  Retry {attempt+1}/{self.max_retries} after {wait}s: {e}")
                    time.sleep(wait)
                else:
                    raise
        raise RuntimeError(f"Failed after {self.max_retries} retries: {url}")


# ---------------------------------------------------------------------------
# Sitemap parsing
# ---------------------------------------------------------------------------

def get_product_manual_urls(fetcher):
    """Fetch all product-manual URLs from the sitemap."""
    resp = fetcher.get("https://v2.support.procore.com/sitemap.xml")
    root = ElementTree.fromstring(resp.content)
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = [loc.text for loc in root.findall(".//s:loc", ns)]
    # Filter to product-manuals only, skip the index page and non-tutorial/non-content pages
    manual_urls = [u for u in urls if "/product-manuals/" in u and u != "https://v2.support.procore.com/product-manuals"]
    print(f"Found {len(manual_urls)} product manual URLs in sitemap")
    return manual_urls


# ---------------------------------------------------------------------------
# Content extraction
# ---------------------------------------------------------------------------

def extract_article(html, url):
    """Extract title and markdown content from a Procore v2 page."""
    soup = BeautifulSoup(html, "lxml")

    # Remove nav, header, footer, scripts, styles
    for tag_name in ["script", "style", "noscript", "iframe", "nav", "header", "footer"]:
        for tag in soup.find_all(tag_name):
            tag.decompose()

    # Remove "See Also" section
    see_also = soup.find("section", id="see-also-section")
    if see_also:
        see_also.decompose()

    # Remove breadcrumbs
    for el in soup.select(".breadcrumb, .breadcrumbs, [class*='breadcrumb']"):
        el.decompose()

    # Get title
    h1 = soup.find("h1")
    title = h1.get_text(strip=True) if h1 else "Untitled"

    # Get article content
    article = soup.select_one("article.content, article, main")
    if not article:
        return None, None

    # Remove the h1 from article to avoid duplication
    h1_in_article = article.find("h1")
    if h1_in_article:
        h1_in_article.decompose()

    # Convert to markdown
    content = md(str(article), heading_style="ATX", bullets="-", strip=["img"])
    content = re.sub(r"\n{3,}", "\n\n", content).strip()

    # Skip pages with very little content (index/nav pages)
    if len(content) < 30:
        return None, None

    return title, content


def slugify(text):
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def url_to_filepath(url):
    """Convert a URL to a file path."""
    path = url.replace("https://v2.support.procore.com/product-manuals/", "")
    path = path.rstrip("/")
    if not path:
        return None
    return Path(path + ".md")


def write_article(output_dir, filepath, title, source_url, content):
    """Write a markdown article to disk."""
    full_path = output_dir / filepath
    full_path.parent.mkdir(parents=True, exist_ok=True)

    header = f"# {title}\n\nSource: {source_url}\n\n---\n\n"
    # Avoid duplicate title
    title_pattern = re.compile(r"^#\s+" + re.escape(title) + r"\s*\n", re.IGNORECASE)
    clean_content = title_pattern.sub("", content).strip()

    full_path.write_text(header + clean_content, encoding="utf-8")
    return full_path


# ---------------------------------------------------------------------------
# Link rewriting
# ---------------------------------------------------------------------------

def rewrite_links(output_dir, url_to_path):
    """Rewrite internal links to relative paths."""
    md_files = list(output_dir.rglob("*.md"))
    for md_file in md_files:
        content = md_file.read_text(encoding="utf-8")
        original = content
        current_dir = md_file.parent.relative_to(output_dir)

        def _rewrite(m):
            text = m.group(1)
            url = m.group(2)
            url_base = url.split("#")[0].split("?")[0].rstrip("/")
            if url_base in url_to_path:
                target = Path(url_to_path[url_base])
                try:
                    rel = os.path.relpath(target, current_dir)
                except ValueError:
                    rel = str(target)
                fragment = ""
                if "#" in url:
                    fragment = "#" + url.split("#", 1)[1]
                return f"[{text}]({rel}{fragment})"
            return m.group(0)

        content = re.sub(r'\[([^\]]*)\]\(([^)]+)\)', _rewrite, content)
        if content != original:
            md_file.write_text(content, encoding="utf-8")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Download Procore v2 product manuals")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--max-pages", type=int, default=0, help="Max pages to download (0=all)")
    parser.add_argument("--delay", type=float, default=0.3)
    args = parser.parse_args()

    fetcher = Fetcher(delay=args.delay)
    urls = get_product_manual_urls(fetcher)

    if args.max_pages > 0:
        urls = urls[:args.max_pages]

    if not args.dry_run:
        BASE_DIR.mkdir(parents=True, exist_ok=True)

    stats = {"downloaded": 0, "skipped": 0, "errors": 0}
    url_to_path = {}

    for i, url in enumerate(urls):
        filepath = url_to_filepath(url)
        if not filepath:
            stats["skipped"] += 1
            continue

        if args.dry_run:
            print(f"  [DRY RUN] {filepath}")
            stats["downloaded"] += 1
            continue

        try:
            resp = fetcher.get(url)
        except Exception as e:
            print(f"  Error fetching {url}: {e}")
            stats["errors"] += 1
            continue

        if "text/html" not in resp.headers.get("content-type", ""):
            stats["skipped"] += 1
            continue

        title, content = extract_article(resp.text, url)
        if not title or not content:
            stats["skipped"] += 1
            continue

        url_clean = url.rstrip("/")
        url_to_path[url_clean] = str(filepath)
        write_article(BASE_DIR, filepath, title, url_clean, content)
        stats["downloaded"] += 1

        if stats["downloaded"] % 100 == 0:
            print(f"  ... {stats['downloaded']} / {len(urls)} pages downloaded ({stats['skipped']} skipped, {stats['errors']} errors)")

    print(f"\nDone: {stats['downloaded']} downloaded, {stats['skipped']} skipped, {stats['errors']} errors")

    # Rewrite links
    if not args.dry_run and url_to_path:
        print("Rewriting internal links...")
        rewrite_links(BASE_DIR, url_to_path)
        print("Done rewriting links")


if __name__ == "__main__":
    main()
