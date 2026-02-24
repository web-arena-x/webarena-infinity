#!/usr/bin/env python3
"""
Download and structure GUI user manuals from various documentation sites.

Usage:
    python scripts/download_manuals.py                  # Download all sites
    python scripts/download_manuals.py --site figma     # Download one site
    python scripts/download_manuals.py --site figma --dry-run  # Preview only
    python scripts/download_manuals.py --list-sites     # List available sites
"""

import argparse
import hashlib
import json
import os
import re
import sys
import time
import urllib.parse
from pathlib import Path
from typing import Optional

import requests
from bs4 import BeautifulSoup, Tag
from markdownify import markdownify as md

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent / "apps" / "user-manuals"

SITE_CONFIGS = {
    "figma": {
        "type": "zendesk",
        "base_url": "https://help.figma.com",
        "locale": "en-us",
        "include_categories": [
            "get-started", "figma-design", "figjam", "figma-slides",
            "figma-sites", "prototyping", "libraries-and-styles",
        ],
        "exclude_keywords": ["api", "developer", "plugin-development", "rest-api", "webhook"],
    },
    "superhuman": {
        "type": "zendesk",
        "base_url": "https://help.superhuman.com",
        "locale": "en-us",
        "include_categories": [
            "guides", "account-setup", "features", "use-cases",
            "getting-started", "superhuman-ai",
        ],
        "exclude_keywords": ["webinar", "billing", "api", "developer", "changelog"],
    },
    "clio": {
        "type": "zendesk",
        "base_url": "https://help.clio.com",
        "locale": "en-us",
        "include_categories": [],  # include all, filter by keywords
        "exclude_keywords": [
            "api", "developer", "sdk", "cli", "integration-backend",
            "webhook", "oauth",
        ],
    },
    "handshake": {
        "type": "zendesk",
        "base_url": "https://support.joinhandshake.com",
        "locale": "en-us",
        "include_categories": [
            "education-partners", "employer", "students", "getting-started",
            "career-center", "career-services",
        ],
        "exclude_keywords": ["api", "developer", "sdk", "sso-configuration"],
    },
    "zendesk": {
        "type": "zendesk",
        "base_url": "https://support.zendesk.com",
        "locale": "en-us",
        "include_categories": [
            "getting-started", "product-guides", "agent-guide",
            "admin-guide", "support", "guide", "explore", "talk",
            "chat", "messaging",
        ],
        "exclude_keywords": [
            "api", "developer", "sdk", "cli", "policies", "updates",
            "changelog", "release-notes", "webhook",
        ],
    },
    "stripe": {
        "type": "html_crawl",
        "start_urls": [
            "https://docs.stripe.com/dashboard/basics",
            "https://docs.stripe.com/dashboard",
            "https://docs.stripe.com/no-code/get-started",
            "https://docs.stripe.com/get-started/account/activate",
        ],
        "allowed_prefixes": [
            "https://docs.stripe.com/dashboard",
            "https://docs.stripe.com/no-code",
            "https://docs.stripe.com/get-started/account",
        ],
        "content_selector": "main",
        "remove_selectors": ["nav", "header", "footer", ".sidebar", ".breadcrumb", "[data-sidebar]"],
        "max_pages": 80,
    },
    "aws": {
        "type": "html_crawl",
        "start_urls": [
            "https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/what-is.html",
        ],
        "allowed_prefixes": ["https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/"],
        "content_selector": "#main-col-body, #main",
        "remove_selectors": ["nav", "header", "footer", ".sidebar", "#nav-panel", ".breadcrumb"],
        "max_pages": 30,
    },
    "kubernetes": {
        "type": "html_crawl",
        "start_urls": [
            "https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/",
        ],
        "allowed_prefixes": [
            "https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard",
        ],
        "content_selector": "main",
        "remove_selectors": ["nav", "header", "footer", ".sidebar", "#sidebar", ".breadcrumb", "#toc"],
        "max_pages": 5,
    },
    "procore": {
        "type": "html_crawl",
        "start_urls": ["https://support.procore.com/"],
        "allowed_prefixes": [
            "https://support.procore.com/getting-started",
            "https://support.procore.com/faq",
            "https://support.procore.com/products",
            "https://support.procore.com/tutorials",
            "https://support.procore.com/certification",
            "https://support.procore.com/references",
        ],
        "content_selector": "article, .content-body, main, #content",
        "remove_selectors": [
            "nav", "header", "footer", ".sidebar", ".breadcrumb",
            "#sidebar", ".navigation", ".toc",
        ],
        "max_pages": 500,
        "exclude_keywords": ["api", "developer", "sdk", "cli", "webhook", "integration-backend"],
    },
    "gmail": {
        "type": "google_support",
        "start_url": "https://support.google.com/mail/?hl=en#topic=7065107",
        "base_url": "https://support.google.com",
        "product_path": "/mail",
        "max_pages": 300,
    },
    "epic": {
        "type": "pdf",
        "pdf_url": "https://downloads.datainterchange.com/Support/Manuals/EPIC/VM-0001-05%20Users%20Guide.pdf",
    },
    "quickbooks": {
        "type": "html_crawl",
        "start_urls": [
            "https://quickbooks.intuit.com/tutorials/",
            "https://quickbooks.intuit.com/payroll/how-to-do-payroll/",
            "https://quickbooks.intuit.com/payroll/how-to-process-payroll/",
        ],
        "allowed_prefixes": [
            "https://quickbooks.intuit.com/tutorials",
            "https://quickbooks.intuit.com/payroll/how-to",
        ],
        "content_selector": "article, .article-body, main, .content",
        "remove_selectors": [
            "nav", "header", "footer", ".sidebar", ".breadcrumb",
            ".related-articles", ".article-footer", ".cta",
        ],
        "max_pages": 100,
        "exclude_keywords": ["api", "developer", "sdk", "cli"],
    },
    "buildium": {
        "type": "html_crawl",
        "start_urls": [
            "https://www.buildium.com/features/",
            "https://www.buildium.com/resource-center/",
        ],
        "allowed_prefixes": [
            "https://www.buildium.com/features",
            "https://www.buildium.com/resource-center",
            "https://www.buildium.com/blog",
        ],
        "content_selector": "article, main, .content, .entry-content",
        "remove_selectors": ["nav", "header", "footer", ".sidebar", ".breadcrumb", ".cta"],
        "max_pages": 100,
        "exclude_keywords": ["api", "developer", "sdk", "pricing", "demo"],
    },
}

# ---------------------------------------------------------------------------
# Rate-limited HTTP fetcher
# ---------------------------------------------------------------------------

class RateLimitedFetcher:
    """HTTP fetcher with rate limiting, retries, and polite headers."""

    def __init__(self, delay: float = 1.0, max_retries: int = 3):
        self.delay = delay
        self.max_retries = max_retries
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": (
                "Mozilla/5.0 (compatible; MirrorMirrorBot/1.0; "
                "+https://github.com/mirror-mirror)"
            ),
            "Accept": "text/html,application/xhtml+xml,application/json",
            "Accept-Language": "en-US,en;q=0.9",
        })
        self._last_request_time = 0.0

    def get(self, url: str, **kwargs) -> requests.Response:
        """GET with rate limiting and retries."""
        elapsed = time.time() - self._last_request_time
        if elapsed < self.delay:
            time.sleep(self.delay - elapsed)

        for attempt in range(self.max_retries):
            try:
                self._last_request_time = time.time()
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
                    print(f"  Retry {attempt + 1}/{self.max_retries} after {wait}s: {e}")
                    time.sleep(wait)
                else:
                    raise
        raise RuntimeError(f"Failed after {self.max_retries} retries: {url}")

    def get_json(self, url: str) -> dict:
        """GET and parse JSON response."""
        resp = self.get(url, headers={"Accept": "application/json"})
        return resp.json()


# ---------------------------------------------------------------------------
# HTML to Markdown conversion
# ---------------------------------------------------------------------------

def clean_html(html: str, remove_selectors: Optional[list] = None) -> BeautifulSoup:
    """Parse HTML and remove non-content elements."""
    soup = BeautifulSoup(html, "lxml")

    # Always remove these
    for tag_name in ["script", "style", "noscript", "iframe"]:
        for tag in soup.find_all(tag_name):
            tag.decompose()

    # Remove skip-to-content links
    for a in soup.find_all("a"):
        href = a.get("href", "")
        text = a.get_text(strip=True).lower()
        if "skip to" in text or href.startswith("#main"):
            if len(text) < 30:
                a.decompose()

    # Remove navigation-type elements
    default_remove = [
        "nav", "header", "footer",
        '[role="navigation"]', '[role="banner"]', '[role="contentinfo"]',
        ".breadcrumb", ".breadcrumbs",
    ]
    selectors = (remove_selectors or []) + default_remove
    for sel in selectors:
        for el in soup.select(sel):
            el.decompose()

    return soup


def html_to_markdown(html: str, base_url: str = "",
                     content_selector: str = "",
                     remove_selectors: Optional[list] = None) -> str:
    """Convert HTML to clean markdown."""
    soup = clean_html(html, remove_selectors)

    # Extract content area if selector given
    content = None
    if content_selector:
        for sel in content_selector.split(","):
            sel = sel.strip()
            content = soup.select_one(sel)
            if content:
                break
    if content is None:
        content = soup.find("body") or soup

    # Convert to markdown
    result = md(
        str(content),
        heading_style="ATX",
        bullets="-",
        strip=["img"] if not base_url else [],
    )

    # Clean up excessive blank lines
    result = re.sub(r"\n{3,}", "\n\n", result)
    # Clean up leading/trailing whitespace
    result = result.strip()
    return result


def slugify(text: str) -> str:
    """Convert text to a URL-friendly slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def write_article(output_dir: Path, filepath: Path, title: str,
                  source_url: str, content: str, dry_run: bool = False) -> Path:
    """Write a markdown article to disk."""
    full_path = output_dir / filepath
    if dry_run:
        print(f"  [DRY RUN] Would write: {full_path}")
        return full_path

    full_path.parent.mkdir(parents=True, exist_ok=True)

    header = f"# {title}\n\nSource: {source_url}\n\n---\n\n"
    # Avoid duplicate title if content already starts with it
    clean_content = content
    title_pattern = re.compile(r"^#\s+" + re.escape(title) + r"\s*\n", re.IGNORECASE)
    clean_content = title_pattern.sub("", clean_content).strip()

    full_path.write_text(header + clean_content, encoding="utf-8")
    return full_path


def download_image(url: str, output_dir: Path, fetcher: RateLimitedFetcher) -> Optional[str]:
    """Download an image and return relative path, or None on failure."""
    try:
        img_dir = output_dir / "images"
        img_dir.mkdir(parents=True, exist_ok=True)

        # Create filename from URL hash + extension
        parsed = urllib.parse.urlparse(url)
        ext = Path(parsed.path).suffix or ".png"
        name_hash = hashlib.md5(url.encode()).hexdigest()[:12]
        filename = f"{name_hash}{ext}"

        img_path = img_dir / filename
        if img_path.exists():
            return f"images/{filename}"

        resp = fetcher.get(url)
        img_path.write_bytes(resp.content)
        return f"images/{filename}"
    except Exception as e:
        print(f"  Warning: Failed to download image {url}: {e}")
        return None


# ---------------------------------------------------------------------------
# Zendesk Help Center adapter
# ---------------------------------------------------------------------------

def download_zendesk(site_name: str, config: dict, output_dir: Path,
                     fetcher: RateLimitedFetcher, dry_run: bool = False) -> dict:
    """Download articles from a Zendesk Help Center site."""
    base_url = config["base_url"]
    locale = config.get("locale", "en-us")
    include_cats = [s.lower() for s in config.get("include_categories", [])]
    exclude_kw = [s.lower() for s in config.get("exclude_keywords", [])]

    stats = {"categories": 0, "sections": 0, "articles": 0, "skipped": 0, "errors": 0}
    url_to_path = {}  # for link rewriting

    api_base = f"{base_url}/api/v2/help_center/{locale}"

    # 1. Fetch all categories
    print(f"  Fetching categories from {api_base}/categories.json")
    categories = []
    page_url = f"{api_base}/categories.json?per_page=100"
    while page_url:
        try:
            data = fetcher.get_json(page_url)
        except Exception as e:
            print(f"  Error fetching categories: {e}")
            stats["errors"] += 1
            break
        categories.extend(data.get("categories", []))
        page_url = data.get("next_page")

    print(f"  Found {len(categories)} categories")

    # Filter categories
    filtered_cats = []
    for cat in categories:
        cat_slug = slugify(cat.get("name", ""))
        cat_id = cat["id"]

        if include_cats:
            # Check if any include pattern matches
            if not any(inc in cat_slug for inc in include_cats):
                print(f"    Skipping category: {cat['name']} (slug: {cat_slug})")
                stats["skipped"] += 1
                continue

        if any(kw in cat_slug for kw in exclude_kw):
            print(f"    Excluding category: {cat['name']} (keyword match)")
            stats["skipped"] += 1
            continue

        filtered_cats.append(cat)
        print(f"    Including category: {cat['name']}")

    stats["categories"] = len(filtered_cats)

    # 2. For each category, fetch sections
    for cat in filtered_cats:
        cat_slug = slugify(cat["name"])
        cat_id = cat["id"]

        sections = []
        page_url = f"{api_base}/categories/{cat_id}/sections.json?per_page=100"
        while page_url:
            try:
                data = fetcher.get_json(page_url)
            except Exception as e:
                print(f"  Error fetching sections for {cat['name']}: {e}")
                stats["errors"] += 1
                break
            sections.extend(data.get("sections", []))
            page_url = data.get("next_page")

        # 3. For each section, fetch articles
        for sec in sections:
            sec_slug = slugify(sec["name"])
            sec_id = sec["id"]

            if any(kw in sec_slug for kw in exclude_kw):
                print(f"    Excluding section: {sec['name']} (keyword match)")
                stats["skipped"] += 1
                continue

            stats["sections"] += 1

            articles = []
            page_url = f"{api_base}/sections/{sec_id}/articles.json?per_page=100"
            while page_url:
                try:
                    data = fetcher.get_json(page_url)
                except Exception as e:
                    print(f"  Error fetching articles for {sec['name']}: {e}")
                    stats["errors"] += 1
                    break
                articles.extend(data.get("articles", []))
                page_url = data.get("next_page")

            for article in articles:
                art_title = article.get("title", "Untitled")
                art_slug = slugify(art_title)
                art_body = article.get("body", "")
                art_url = article.get("html_url", "")

                if not art_body:
                    stats["skipped"] += 1
                    continue

                # Exclude by keywords in title
                art_lower = art_title.lower()
                if any(kw in art_lower for kw in exclude_kw):
                    stats["skipped"] += 1
                    continue

                # Convert body HTML to markdown
                content = html_to_markdown(art_body, base_url)

                # Build file path
                filepath = Path(cat_slug) / sec_slug / f"{art_slug}.md"
                url_to_path[art_url] = str(filepath)

                write_article(output_dir, filepath, art_title, art_url, content, dry_run)
                stats["articles"] += 1

                if stats["articles"] % 50 == 0:
                    print(f"    ... {stats['articles']} articles downloaded")

    # Rewrite internal links across all files
    if not dry_run and url_to_path:
        rewrite_links_in_dir(output_dir, url_to_path, base_url)

    return stats


# ---------------------------------------------------------------------------
# Static HTML crawl adapter
# ---------------------------------------------------------------------------

def download_html_crawl(site_name: str, config: dict, output_dir: Path,
                        fetcher: RateLimitedFetcher, dry_run: bool = False) -> dict:
    """Crawl static HTML documentation sites."""
    start_urls = config["start_urls"]
    allowed_prefixes = config.get("allowed_prefixes", [])
    content_selector = config.get("content_selector", "main")
    remove_selectors = config.get("remove_selectors", [])
    max_pages = config.get("max_pages", 100)
    exclude_kw = [s.lower() for s in config.get("exclude_keywords", [])]

    stats = {"pages": 0, "skipped": 0, "errors": 0}
    visited = set()
    start_url_set = {u.rstrip("/") for u in start_urls}
    queue = list(start_urls)
    url_to_path = {}

    while queue and stats["pages"] < max_pages:
        url = queue.pop(0)

        # Normalize URL
        parsed = urllib.parse.urlparse(url)
        url_clean = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
        url_clean = url_clean.rstrip("/")

        if url_clean in visited:
            continue
        visited.add(url_clean)

        # Check allowed prefixes (always allow start URLs for link discovery)
        is_start_url = url_clean in start_url_set
        matches_prefix = (
            not allowed_prefixes
            or any(url_clean.startswith(p) for p in allowed_prefixes)
        )
        if not matches_prefix and not is_start_url:
            continue

        try:
            resp = fetcher.get(url_clean)
        except Exception as e:
            print(f"  Error fetching {url_clean}: {e}")
            stats["errors"] += 1
            continue

        content_type = resp.headers.get("content-type", "")
        if "text/html" not in content_type:
            continue

        html = resp.text

        # Extract links first (before cleaning removes nav elements)
        raw_soup = BeautifulSoup(html, "lxml")
        for a_tag in raw_soup.find_all("a", href=True):
            href = a_tag["href"]
            abs_url = urllib.parse.urljoin(url_clean, href)
            abs_url = abs_url.split("#")[0].rstrip("/")
            abs_parsed = urllib.parse.urlparse(abs_url)
            abs_clean = f"{abs_parsed.scheme}://{abs_parsed.netloc}{abs_parsed.path}"
            if abs_clean not in visited:
                if allowed_prefixes and any(abs_clean.startswith(p) for p in allowed_prefixes):
                    queue.append(abs_clean)

        # Skip saving content for start-only pages (hub/landing pages)
        if is_start_url and not matches_prefix:
            continue

        soup = clean_html(html, remove_selectors)

        # Extract title
        title_tag = soup.find("title")
        h1_tag = soup.find("h1")
        title = ""
        if h1_tag:
            title = " ".join(h1_tag.get_text().split())
        elif title_tag:
            title = " ".join(title_tag.get_text().split())
        title = title.split("|")[0].strip() if title else "Untitled"

        # Check exclude keywords
        if any(kw in title.lower() for kw in exclude_kw):
            stats["skipped"] += 1
            continue

        # Convert to markdown
        content = html_to_markdown(html, url_clean, content_selector, remove_selectors)

        if not content or len(content) < 50:
            stats["skipped"] += 1
            continue

        # Build file path from URL path
        url_path = parsed.path.strip("/")
        if not url_path:
            url_path = "index"

        # Remove common prefixes
        for prefix in ["docs/", "help/", "support/", "learn-support/en-us/"]:
            if url_path.startswith(prefix):
                url_path = url_path[len(prefix):]

        # Clean up path
        url_path = url_path.rstrip("/")
        if url_path.endswith(".html"):
            url_path = url_path[:-5]

        filepath = Path(url_path + ".md")
        url_to_path[url_clean] = str(filepath)

        write_article(output_dir, filepath, title, url_clean, content, dry_run)
        stats["pages"] += 1

        if stats["pages"] % 20 == 0:
            print(f"    ... {stats['pages']} pages downloaded")

    # Rewrite internal links
    if not dry_run and url_to_path:
        rewrite_links_in_dir(output_dir, url_to_path, "")

    return stats


# ---------------------------------------------------------------------------
# Google Support adapter (Gmail)
# ---------------------------------------------------------------------------

def download_google_support(site_name: str, config: dict, output_dir: Path,
                            fetcher: RateLimitedFetcher, dry_run: bool = False) -> dict:
    """Download Google Support articles (Gmail)."""
    base_url = config["base_url"]
    product_path = config["product_path"]
    max_pages = config.get("max_pages", 300)

    # Use a slower rate for Google
    fetcher.delay = max(fetcher.delay, 2.0)

    stats = {"pages": 0, "topics": 0, "skipped": 0, "errors": 0}
    visited = set()
    queue = [config["start_url"]]
    url_to_path = {}

    while queue and stats["pages"] < max_pages:
        url = queue.pop(0)

        parsed = urllib.parse.urlparse(url)
        url_clean = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"

        if url_clean in visited:
            continue
        visited.add(url_clean)

        # Must be a product support URL
        if product_path not in parsed.path:
            continue

        try:
            resp = fetcher.get(url_clean, params={"hl": "en"})
        except Exception as e:
            print(f"  Error fetching {url_clean}: {e}")
            stats["errors"] += 1
            continue

        html = resp.text

        # Extract links from RAW HTML before cleaning (Google puts links
        # inside nav-like elements that clean_html removes)
        raw_soup = BeautifulSoup(html, "lxml")
        for a_tag in raw_soup.find_all("a", href=True):
            href = a_tag["href"]
            abs_url = urllib.parse.urljoin(url_clean, href)
            abs_parsed = urllib.parse.urlparse(abs_url)
            abs_clean = f"{abs_parsed.scheme}://{abs_parsed.netloc}{abs_parsed.path}"

            if abs_clean not in visited and product_path in abs_clean:
                if "/answer/" in abs_clean or "/topic/" in abs_clean:
                    queue.append(abs_clean)

        is_answer = "/answer/" in url_clean
        is_topic = "/topic/" in url_clean

        if is_topic:
            stats["topics"] += 1

        if is_answer:
            # Extract article content from cleaned HTML
            soup = clean_html(html)
            content_el = (
                soup.select_one(".article-content")
                or soup.select_one('[itemprop="articleBody"]')
                or soup.select_one("article")
                or soup.select_one("main")
            )

            if not content_el:
                stats["skipped"] += 1
                continue

            title_el = (
                raw_soup.find("h1")
                or raw_soup.find("title")
            )
            title = title_el.get_text(strip=True) if title_el else "Untitled"
            title = title.split(" - ")[0].strip()

            content = md(str(content_el), heading_style="ATX", bullets="-")
            content = re.sub(r"\n{3,}", "\n\n", content).strip()

            if len(content) < 50:
                stats["skipped"] += 1
                continue

            # Extract answer ID for filename
            answer_match = re.search(r"/answer/(\d+)", url_clean)
            answer_id = answer_match.group(1) if answer_match else slugify(title)
            filepath = Path(f"{answer_id}-{slugify(title)}.md")

            url_to_path[url_clean] = str(filepath)
            write_article(output_dir, filepath, title, url_clean, content, dry_run)
            stats["pages"] += 1

            if stats["pages"] % 20 == 0:
                print(f"    ... {stats['pages']} pages downloaded")

    if not dry_run and url_to_path:
        rewrite_links_in_dir(output_dir, url_to_path, base_url)

    return stats


# ---------------------------------------------------------------------------
# PDF adapter (EPIC)
# ---------------------------------------------------------------------------

def download_pdf(site_name: str, config: dict, output_dir: Path,
                 fetcher: RateLimitedFetcher, dry_run: bool = False) -> dict:
    """Download and convert a PDF manual to markdown."""
    import fitz  # PyMuPDF

    pdf_url = config["pdf_url"]
    stats = {"pages": 0, "chapters": 0, "errors": 0}

    if dry_run:
        print(f"  [DRY RUN] Would download PDF from {pdf_url}")
        return stats

    # Download PDF (use browser-like headers since some servers reject bot UAs)
    print(f"  Downloading PDF from {pdf_url}")
    try:
        fetcher.session.headers.update({
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            ),
            "Accept": "application/pdf,*/*",
        })
        resp = fetcher.get(pdf_url)
    except Exception as e:
        print(f"  Error downloading PDF: {e}")
        stats["errors"] += 1
        return stats

    pdf_path = output_dir / "source.pdf"
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_path.write_bytes(resp.content)
    print(f"  PDF saved ({len(resp.content) / 1024 / 1024:.1f} MB)")

    # Extract text with PyMuPDF
    doc = fitz.open(str(pdf_path))
    total_pages = len(doc)
    print(f"  PDF has {total_pages} pages")

    # Extract text per page and build section-aware markdown
    all_text_lines = []
    for page_num in range(total_pages):
        page = doc[page_num]
        text = page.get_text("text")
        stats["pages"] += 1
        for line in text.split("\n"):
            all_text_lines.append(line.strip())

    # Detect section headings using "X.Y.Z\nHeading" pattern
    # where X.Y.Z has at least one dot (to avoid page number confusion)
    sub_section_re = re.compile(r"^(\d+\.\d+(?:\.\d+)*)$")

    output_lines = []
    i = 0
    while i < len(all_text_lines):
        stripped = all_text_lines[i]

        # Match sub-section numbers (e.g., "1.1", "2.3.1") — NOT plain digits
        if sub_section_re.match(stripped) and i + 1 < len(all_text_lines):
            next_line = all_text_lines[i + 1]
            if (next_line
                    and len(next_line) > 2
                    and len(next_line) < 80
                    and "..." not in next_line
                    and next_line[0].isupper()
                    and not next_line[0].isdigit()):
                sec_num = stripped
                heading = next_line
                dot_count = sec_num.count(".")
                level = min(dot_count + 1, 4)
                hashes = "#" * level
                output_lines.append("")
                output_lines.append(f"{hashes} {sec_num} {heading}")
                output_lines.append("")
                i += 2
                continue

        # Skip TOC lines with dot leaders
        if "..." in stripped and stripped[-1].isdigit():
            i += 1
            continue

        output_lines.append(stripped)
        i += 1

    # Clean up excessive blank lines
    content = re.sub(r"\n{3,}", "\n\n", "\n".join(output_lines)).strip()

    # Single output file for this PDF
    chapters = [("epic-users-guide", "EPIC User's Guide", content)]

    # Write chapters to files
    for i, (chapter_slug, title, content) in enumerate(chapters):
        filepath = Path(f"{i + 1:02d}-{chapter_slug}.md")
        write_article(output_dir, filepath, title, pdf_url, content)
        stats["chapters"] += 1

    doc.close()

    # Clean up source PDF
    pdf_path.unlink()

    print(f"  Extracted {stats['chapters']} chapters from {stats['pages']} pages")
    return stats


# ---------------------------------------------------------------------------
# Link rewriting
# ---------------------------------------------------------------------------

def rewrite_links_in_dir(output_dir: Path, url_to_path: dict, base_url: str):
    """Rewrite absolute internal links to relative paths across all markdown files.

    Only rewrites URLs inside markdown link syntax [text](url), preserving
    Source: headers and other plain-text URLs.
    """
    md_files = list(output_dir.rglob("*.md"))

    for md_file in md_files:
        content = md_file.read_text(encoding="utf-8")
        original = content

        current_dir = md_file.parent.relative_to(output_dir)

        # Only rewrite URLs inside markdown link syntax: [text](url)
        def _rewrite_md_link(m):
            text = m.group(1)
            url = m.group(2)
            # Strip fragment/query for lookup
            url_base = url.split("#")[0].split("?")[0].rstrip("/")
            if url_base in url_to_path:
                target_path = Path(url_to_path[url_base])
                try:
                    rel = os.path.relpath(target_path, current_dir)
                except ValueError:
                    rel = str(target_path)
                # Preserve fragment if present
                fragment = ""
                if "#" in url:
                    fragment = "#" + url.split("#", 1)[1]
                return f"[{text}]({rel}{fragment})"
            return m.group(0)

        # Match markdown links: [text](url)
        content = re.sub(r'\[([^\]]*)\]\(([^)]+)\)', _rewrite_md_link, content)

        if content != original:
            md_file.write_text(content, encoding="utf-8")


# ---------------------------------------------------------------------------
# Site dispatch & CLI
# ---------------------------------------------------------------------------

DOWNLOADERS = {
    "zendesk": download_zendesk,
    "html_crawl": download_html_crawl,
    "google_support": download_google_support,
    "pdf": download_pdf,
}


def download_site(site_name: str, dry_run: bool = False,
                  delay: float = 1.0) -> dict:
    """Download a single site's documentation."""
    config = SITE_CONFIGS[site_name]
    site_type = config["type"]
    output_dir = BASE_DIR / site_name

    if not dry_run:
        output_dir.mkdir(parents=True, exist_ok=True)

    fetcher = RateLimitedFetcher(delay=delay)
    downloader = DOWNLOADERS.get(site_type)

    if not downloader:
        print(f"  No downloader for type: {site_type}")
        return {"error": f"Unknown type: {site_type}"}

    return downloader(site_name, config, output_dir, fetcher, dry_run)


def main():
    parser = argparse.ArgumentParser(
        description="Download and structure GUI user manuals"
    )
    parser.add_argument(
        "--site", type=str, default=None,
        help="Download a specific site only (e.g., figma, stripe)",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Preview what would be downloaded without writing files",
    )
    parser.add_argument(
        "--list-sites", action="store_true",
        help="List all available sites and exit",
    )
    parser.add_argument(
        "--delay", type=float, default=1.0,
        help="Delay between requests in seconds (default: 1.0)",
    )
    args = parser.parse_args()

    if args.list_sites:
        print("Available sites:")
        for name, config in sorted(SITE_CONFIGS.items()):
            print(f"  {name:15s}  ({config['type']})")
        return

    sites = [args.site] if args.site else list(SITE_CONFIGS.keys())

    # Validate site names
    for site in sites:
        if site not in SITE_CONFIGS:
            print(f"Error: Unknown site '{site}'. Use --list-sites to see options.")
            sys.exit(1)

    print(f"{'[DRY RUN] ' if args.dry_run else ''}Downloading {len(sites)} site(s)")
    print(f"Output directory: {BASE_DIR}")
    print()

    results = {}
    for site in sites:
        print(f"=== {site.upper()} ===")
        t0 = time.time()
        try:
            stats = download_site(site, dry_run=args.dry_run, delay=args.delay)
            elapsed = time.time() - t0
            stats["time_seconds"] = round(elapsed, 1)
            results[site] = stats
            print(f"  Done in {elapsed:.1f}s: {stats}")
        except Exception as e:
            results[site] = {"error": str(e)}
            print(f"  FAILED: {e}")
        print()

    # Summary report
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    for site, stats in results.items():
        if "error" in stats:
            print(f"  {site:15s}  ERROR: {stats['error']}")
        else:
            article_count = stats.get("articles", 0) + stats.get("pages", 0) + stats.get("chapters", 0)
            print(f"  {site:15s}  {article_count:>5d} files  ({stats.get('time_seconds', 0)}s)")

    # Write report to file
    report_path = BASE_DIR / "download_report.json"
    if not args.dry_run:
        report_path.write_text(json.dumps(results, indent=2), encoding="utf-8")
        print(f"\nReport saved to {report_path}")


if __name__ == "__main__":
    main()
