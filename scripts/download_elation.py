#!/usr/bin/env python3
"""
Download Elation EMR help center articles using Playwright (Salesforce Community site).

Usage:
    python scripts/download_elation.py
    python scripts/download_elation.py --dry-run
    python scripts/download_elation.py --max-pages 50
    python scripts/download_elation.py --workers 6
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

BASE_DIR = Path(__file__).resolve().parent.parent / "apps" / "user-manuals" / "elation"
SITEMAP_URL = "https://help.elationhealth.com/s/sitemap-topicarticle-1.xml"

# Exclude non-GUI articles
EXCLUDE_PATTERNS = [
    r"(?i)api",
    r"(?i)developer",
    r"(?i)sdk",
    r"(?i)webhook",
    r"(?i)data-export-checklist",  # admin/technical
]

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
        if (['script', 'style', 'svg'].includes(tag)) return '';
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

    const selectors = [
        '.forceCommunityArticleContent',
        '.slds-rich-text-editor__output',
        'article',
        '.article-content',
        'main',
    ];

    let contentEl = null;
    let title = '';

    for (const sel of selectors) {
        const el = document.querySelector(sel);
        if (el && el.innerText.trim().length > 100) {
            contentEl = el;
            break;
        }
    }

    // Use document.title (page <title> tag) as the primary title source
    // because the first h1 on Elation pages is often "Contents" (TOC heading)
    title = document.title ? document.title.trim() : '';
    // Strip trailing " - Elation Health" or similar suffixes
    title = title.replace(/\\s*[-|]\\s*Elation.*$/i, '').trim();
    if (!title) {
        const h1 = document.querySelector('h1');
        title = h1 ? h1.innerText.trim() : '';
    }

    if (!contentEl) {
        let best = null;
        let bestLen = 0;
        document.querySelectorAll('div, section, main').forEach(el => {
            const text = el.innerText ? el.innerText.trim() : '';
            if (text.length > bestLen && text.length > 200 && el.children.length < 50) {
                best = el;
                bestLen = text.length;
            }
        });
        contentEl = best;
    }

    if (!contentEl) return {title, html: '', text: ''};

    let html = flattenShadowDOM(contentEl);
    const temp = document.createElement('div');
    temp.innerHTML = html;
    temp.querySelectorAll('nav, header, footer').forEach(el => el.remove());
    temp.querySelectorAll('[class*="breadcrumb"]').forEach(el => el.remove());
    temp.querySelectorAll('[class*="feedback"], [class*="helpful"]').forEach(el => el.remove());
    temp.querySelectorAll('script, style').forEach(el => el.remove());
    temp.querySelectorAll('p').forEach(p => { if (!p.textContent.trim()) p.remove(); });

    return {
        title: title,
        html: temp.innerHTML,
        text: contentEl.innerText ? contentEl.innerText.trim() : ''
    };
}"""


def get_article_urls():
    """Fetch article URLs from the sitemap."""
    resp = requests.get(SITEMAP_URL, headers={
        "User-Agent": "Mozilla/5.0 (compatible; MirrorMirrorBot/1.0)",
    }, timeout=30)
    root = ElementTree.fromstring(resp.content)
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = [loc.text for loc in root.findall(".//s:loc", ns)]

    filtered = []
    for url in urls:
        slug = url.split("/article/")[-1] if "/article/" in url else ""
        if not slug:
            continue
        if any(re.search(pat, slug) for pat in EXCLUDE_PATTERNS):
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
                url_base = "https://help.elationhealth.com" + url_base
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
    """Extract article content from an Elation page using async Playwright."""
    try:
        await page.goto(url, wait_until="load", timeout=30000)
    except Exception as e:
        return None, None, None

    try:
        await page.wait_for_selector(
            "article, main, h1, .article-content, .slds-rich-text-editor__output, .forceCommunityArticleContent",
            timeout=12000
        )
    except:
        pass

    await asyncio.sleep(3)

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
            if stats["downloaded"] % 20 == 0:
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
    parser = argparse.ArgumentParser(description="Download Elation EMR help articles")
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
