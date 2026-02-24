#!/usr/bin/env python3
"""
Download Xero Central help articles using Playwright (Salesforce LWC site).

Usage:
    python scripts/download_xero.py
    python scripts/download_xero.py --dry-run
    python scripts/download_xero.py --max-pages 50
    python scripts/download_xero.py --workers 6
"""

import argparse
import asyncio
import json
import os
import re
import sys
import time
from pathlib import Path
from xml.etree import ElementTree

import requests
from markdownify import markdownify as md

BASE_DIR = Path(__file__).resolve().parent.parent / "apps" / "user-manuals" / "xero"
SITEMAP_URL = "https://central.xero.com/s/sitemap-topicarticle-1.xml"

# Exclude non-GUI articles: developer-focused, API, release notes, region-specific duplicates
EXCLUDE_PATTERNS = [
    r"-developer",
    r"How-Xero-Developer",
    r"-api-",
    r"product-releases",
    r"Xero-product-releases",
    r"recent-.*-updates$",
]

# Only include US/generic versions of region-specific articles
REGION_SUFFIXES = ["-AU", "-NZ", "-UK", "-IE", "-SG", "-HK", "-MY", "-SA", "-ROW", "-CA"]

EXTRACT_JS = """() => {
    function flattenShadowDOM(node) {
        if (!node) return '';
        if (node.shadowRoot) {
            let parts = [];
            for (let child of node.shadowRoot.childNodes) {
                parts.push(flattenShadowDOM(child));
            }
            return parts.join('');
        }
        if (node.nodeType === 3) return node.textContent;
        if (node.nodeType !== 1) return '';
        const tag = node.tagName.toLowerCase();
        if (['script', 'style', 'svg', 'img'].includes(tag)) return '';
        if (tag.includes('-')) {
            let parts = [];
            for (let child of node.childNodes) {
                parts.push(flattenShadowDOM(child));
            }
            return parts.join('');
        }
        const attrs = [];
        const href = node.getAttribute('href');
        if (href) attrs.push('href="' + href + '"');
        let inner = '';
        for (let child of node.childNodes) {
            inner += flattenShadowDOM(child);
        }
        const attrStr = attrs.length ? ' ' + attrs.join(' ') : '';
        if (['br', 'hr'].includes(tag)) return '<' + tag + '/>';
        return '<' + tag + attrStr + '>' + inner + '</' + tag + '>';
    }

    const articleEl = document.querySelector('c-xc-article-content');
    if (!articleEl || !articleEl.shadowRoot) return {title: '', html: '', text: ''};
    const sr = articleEl.shadowRoot;
    const titleH = sr.querySelector('.title__heading, h1');
    const title = titleH ? titleH.innerText.trim() : '';
    const fullHTML = flattenShadowDOM(articleEl);
    const temp = document.createElement('div');
    temp.innerHTML = fullHTML;
    temp.querySelectorAll('nav, ol.xcReuseableBreadcrumbs').forEach(el => el.remove());
    temp.querySelectorAll('.xc-visually-hidden').forEach(el => el.remove());
    temp.querySelectorAll('.title').forEach(el => el.remove());
    temp.querySelectorAll('.xui-banner-layout').forEach(el => el.remove());
    temp.querySelectorAll('[class*="feedback"], [class*="helpful"], [class*="still-have-questions"]').forEach(el => el.remove());
    temp.querySelectorAll('p').forEach(p => { if (!p.textContent.trim()) p.remove(); });
    return {
        title: title,
        html: temp.innerHTML,
        text: articleEl.innerText.trim()
    };
}"""


URLS_CACHE = BASE_DIR.parent.parent.parent / "scripts" / ".xero_urls_cache.json"


def get_article_urls():
    """Fetch article URLs from the sitemap, with caching to handle rate limits."""
    # Try to fetch from sitemap first
    try:
        resp = requests.get(SITEMAP_URL, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        }, timeout=30)
        if resp.status_code == 200 and b"<?xml" in resp.content[:100]:
            root = ElementTree.fromstring(resp.content)
            ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
            urls = [loc.text for loc in root.findall(".//s:loc", ns)]
        else:
            print(f"  Sitemap returned {resp.status_code}, trying cache...")
            urls = None
    except Exception as e:
        print(f"  Sitemap fetch failed: {e}, trying cache...")
        urls = None

    # Fall back to cached URLs
    if urls is None:
        if URLS_CACHE.exists():
            urls = json.loads(URLS_CACHE.read_text())
            print(f"  Loaded {len(urls)} URLs from cache")
        else:
            print("ERROR: Cannot fetch sitemap and no cache exists")
            sys.exit(1)
    else:
        # Save to cache for next time
        URLS_CACHE.parent.mkdir(parents=True, exist_ok=True)
        URLS_CACHE.write_text(json.dumps(urls))

    filtered = []
    for url in urls:
        slug = url.split("/article/")[-1] if "/article/" in url else ""
        if not slug:
            continue
        if any(re.search(pat, slug) for pat in EXCLUDE_PATTERNS):
            continue
        skip = False
        for suffix in REGION_SUFFIXES:
            if slug.endswith(suffix):
                skip = True
                break
        if skip:
            continue
        filtered.append(url)

    print(f"Sitemap: {len(urls)} total, {len(filtered)} after filtering")
    return filtered


def url_to_filepath(url):
    slug = url.split("/article/")[-1] if "/article/" in url else ""
    if not slug:
        return None
    return Path(f"{slug}.md")


def html_to_clean_markdown(html_content):
    if not html_content:
        return ""
    html_content = re.sub(r'\s+c-\w+_\w+=""', '', html_content)
    html_content = re.sub(r'\s+data-\w+[-\w]*="[^"]*"', '', html_content)
    content = md(html_content, heading_style="ATX", bullets="-")
    content = re.sub(r"\n{3,}", "\n\n", content).strip()
    content = re.sub(r'[\uE000-\uF8FF]', '', content)
    content = re.sub(r'^Breadcrumbs\s*\n+', '', content)
    content = re.sub(r'^This article is for .*?\n+', '', content, flags=re.MULTILINE)
    lines = content.split('\n')
    cleaned = [line.rstrip() for line in lines]
    return '\n'.join(cleaned)


def write_article(output_dir, filepath, title, source_url, content):
    full_path = output_dir / filepath
    full_path.parent.mkdir(parents=True, exist_ok=True)
    header = f"# {title}\n\nSource: {source_url}\n\n---\n\n"
    title_pattern = re.compile(r"^#\s+" + re.escape(title) + r"\s*\n", re.IGNORECASE)
    clean_content = title_pattern.sub("", content).strip()
    full_path.write_text(header + clean_content, encoding="utf-8")
    return full_path


def rewrite_links(output_dir, url_to_path):
    md_files = list(output_dir.rglob("*.md"))
    for md_file in md_files:
        content = md_file.read_text(encoding="utf-8")
        original = content
        current_dir = md_file.parent.relative_to(output_dir)

        def _rewrite(m):
            text = m.group(1)
            url = m.group(2)
            url_base = url.split("#")[0].split("?")[0].rstrip("/")
            if url_base.startswith("/s/article/"):
                url_base = "https://central.xero.com" + url_base
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


async def extract_article(page, url):
    """Extract article content from a Xero page using async Playwright."""
    try:
        await page.goto(url, wait_until="load", timeout=30000)
    except Exception as e:
        return None, None, None

    try:
        await page.wait_for_selector("c-xc-article-content", timeout=10000)
        await asyncio.sleep(1.5)
    except:
        await asyncio.sleep(0.5)

    result = await page.evaluate(EXTRACT_JS)
    title = result.get("title", "")
    html = result.get("html", "")
    text = result.get("text", "")

    if not title or len(text) < 30:
        return None, None, None
    return title, html, url


async def worker(worker_id, browser, queue, stats, url_to_path, lock):
    """Worker coroutine that processes URLs from the queue."""
    page = await browser.new_page()
    while True:
        try:
            i, url = queue.get_nowait()
        except asyncio.QueueEmpty:
            break

        filepath = url_to_filepath(url)
        if not filepath:
            async with lock:
                stats["skipped"] += 1
            continue

        # Skip already downloaded
        if (BASE_DIR / filepath).exists():
            async with lock:
                stats["skipped_existing"] += 1
                url_to_path[url.rstrip("/")] = str(filepath)
            continue

        try:
            title, html, source_url = await extract_article(page, url)
        except Exception as e:
            async with lock:
                stats["errors"] += 1
            continue

        if not title or not html:
            async with lock:
                stats["skipped"] += 1
            continue

        content = html_to_clean_markdown(html)
        if not content or len(content) < 30:
            async with lock:
                stats["skipped"] += 1
            continue

        async with lock:
            url_to_path[url.rstrip("/")] = str(filepath)
            stats["downloaded"] += 1
            total_done = stats["downloaded"] + stats["skipped"] + stats["errors"] + stats["skipped_existing"]
            if stats["downloaded"] % 25 == 0:
                print(f"  [{stats['downloaded']} downloaded, {stats['skipped_existing']} cached, {stats['skipped']} skipped, {stats['errors']} errors, {total_done} total processed]")

        write_article(BASE_DIR, filepath, title, url, content)

    await page.close()


async def main_async(urls, num_workers):
    from playwright.async_api import async_playwright

    BASE_DIR.mkdir(parents=True, exist_ok=True)

    stats = {"downloaded": 0, "skipped": 0, "errors": 0, "skipped_existing": 0}
    url_to_path = {}
    lock = asyncio.Lock()

    queue = asyncio.Queue()
    for i, url in enumerate(urls):
        queue.put_nowait((i, url))

    print(f"Starting {num_workers} concurrent workers for {len(urls)} URLs...")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        workers = [worker(wid, browser, queue, stats, url_to_path, lock) for wid in range(num_workers)]
        await asyncio.gather(*workers)
        await browser.close()

    print(f"\nDone: {stats['downloaded']} downloaded, {stats['skipped_existing']} already existed, {stats['skipped']} skipped, {stats['errors']} errors")

    if url_to_path:
        print("Rewriting internal links...")
        rewrite_links(BASE_DIR, url_to_path)
        print("Done")


def main():
    parser = argparse.ArgumentParser(description="Download Xero Central help articles")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--max-pages", type=int, default=0, help="Max pages (0=all)")
    parser.add_argument("--workers", type=int, default=6, help="Concurrent browser pages")
    args = parser.parse_args()

    print("Fetching article URLs from sitemap...")
    urls = get_article_urls()

    if args.max_pages > 0:
        urls = urls[:args.max_pages]

    if args.dry_run:
        for url in urls:
            fp = url_to_filepath(url)
            print(f"  [DRY RUN] {fp}")
        print(f"\nTotal: {len(urls)} articles")
        return

    asyncio.run(main_async(urls, args.workers))


if __name__ == "__main__":
    main()
