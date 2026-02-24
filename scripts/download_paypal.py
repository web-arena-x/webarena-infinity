#!/usr/bin/env python3
"""
Download PayPal Business help center articles.

Usage:
    python scripts/download_paypal.py
    python scripts/download_paypal.py --dry-run
"""

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

BASE_DIR = Path(__file__).resolve().parent.parent / "apps" / "user-manuals" / "paypal"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9",
    "Accept-Language": "en-US,en;q=0.9",
}

# Topics to crawl (personal topics work; business topics require auth)
PERSONAL_TOPICS = [
    "help_payments_and_transfers_personal",
    "help_disputes_and_limitations_personal",
    "help_account_personal",
    "help_wallet_personal",
    "help_login_and_security_personal",
    "help_seller_tools_personal",
]

# Map personal topics to friendly category names
TOPIC_NAMES = {
    "help_payments_and_transfers_personal": "payments-and-transfers",
    "help_disputes_and_limitations_personal": "disputes-and-limitations",
    "help_account_personal": "my-account",
    "help_wallet_personal": "my-wallet",
    "help_login_and_security_personal": "login-and-security",
    "help_seller_tools_personal": "seller-tools",
}


def slugify(text):
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


# ---------------------------------------------------------------------------
# Article discovery
# ---------------------------------------------------------------------------

def discover_articles(session, delay=1.0):
    """Discover all article IDs from topic pages."""
    articles = {}  # article_id -> {topic_category, subtopic_name}

    for topic_id in PERSONAL_TOPICS:
        url = f"https://www.paypal.com/us/cshelp/topic/{topic_id}"
        time.sleep(delay)
        resp = session.get(url, headers=HEADERS)
        soup = BeautifulSoup(resp.text, "lxml")
        nd = soup.find("script", id="__NEXT_DATA__")
        if not nd:
            print(f"  Warning: No __NEXT_DATA__ for {topic_id}")
            continue

        data = json.loads(nd.string)
        api_data = data.get("props", {}).get("pageProps", {}).get("pageData", {}).get("apiData", {})
        stt = api_data.get("subTopicTree", {}).get("data", [])

        topic_cat = TOPIC_NAMES.get(topic_id, topic_id)
        count = 0
        for subtopic in stt:
            st_name = subtopic.get("topicName", "general")
            for art in subtopic.get("articles", []):
                aid = art.get("articleId", "")
                if aid:
                    articles[aid] = {
                        "topic_category": topic_cat,
                        "subtopic_name": slugify(st_name) if st_name else "general",
                    }
                    count += 1

        print(f"  {topic_id}: {count} articles")

    return articles


# ---------------------------------------------------------------------------
# Article downloading
# ---------------------------------------------------------------------------

def fetch_article(session, article_id, delay=1.0):
    """Fetch a single article by ID and return (title, html_content, source_url)."""
    # PayPal article URLs use a slug format, but we can construct from article ID
    # The slug in URL is: {title-slug}-{article_id}
    # We need to find the actual URL. Let's try the direct article endpoint.
    url = f"https://www.paypal.com/us/cshelp/article/{article_id.lower()}"
    time.sleep(delay)
    resp = session.get(url, headers=HEADERS, allow_redirects=True)

    if resp.status_code != 200:
        return None, None, None

    soup = BeautifulSoup(resp.text, "lxml")
    nd = soup.find("script", id="__NEXT_DATA__")
    if not nd:
        return None, None, None

    data = json.loads(nd.string)
    api_data = data.get("props", {}).get("pageProps", {}).get("pageData", {}).get("apiData", {})
    article_data = api_data.get("article", {}).get("articleContent", {})

    if not article_data:
        return None, None, None

    title = article_data.get("articleTitle", "Untitled")
    html_content = article_data.get("articleContent", "")
    source_url = resp.url

    return title, html_content, source_url


def html_to_clean_markdown(html_content):
    """Convert article HTML to clean markdown."""
    if not html_content:
        return ""

    soup = BeautifulSoup(html_content, "lxml")

    # Remove scripts, styles
    for tag in soup.find_all(["script", "style", "noscript"]):
        tag.decompose()

    content = md(str(soup), heading_style="ATX", bullets="-")
    content = re.sub(r"\n{3,}", "\n\n", content).strip()

    # Remove PUA characters
    content = re.sub(r'[\uE000-\uF8FF]', '', content)

    return content


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
    parser = argparse.ArgumentParser(description="Download PayPal help center articles")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--delay", type=float, default=1.0)
    args = parser.parse_args()

    session = requests.Session()

    print("Discovering articles from topic pages...")
    articles = discover_articles(session, delay=args.delay)
    print(f"Found {len(articles)} unique articles\n")

    if args.dry_run:
        for aid, info in sorted(articles.items()):
            print(f"  [DRY RUN] {info['topic_category']}/{aid}.md")
        return

    BASE_DIR.mkdir(parents=True, exist_ok=True)

    stats = {"downloaded": 0, "skipped": 0, "errors": 0}
    url_to_path = {}

    for i, (article_id, info) in enumerate(sorted(articles.items())):
        try:
            title, html_content, source_url = fetch_article(session, article_id, delay=args.delay)
        except Exception as e:
            print(f"  Error fetching {article_id}: {e}")
            stats["errors"] += 1
            continue

        if not title or not html_content:
            stats["skipped"] += 1
            continue

        content = html_to_clean_markdown(html_content)
        if not content or len(content) < 30:
            stats["skipped"] += 1
            continue

        # Build file path
        category = info["topic_category"]
        title_slug = slugify(title)[:80]
        filepath = Path(category) / f"{article_id.lower()}-{title_slug}.md"

        url_to_path[source_url.rstrip("/")] = str(filepath)
        write_article(BASE_DIR, filepath, title, source_url, content)
        stats["downloaded"] += 1

        if stats["downloaded"] % 50 == 0:
            print(f"  ... {stats['downloaded']} / {len(articles)} downloaded ({stats['skipped']} skipped, {stats['errors']} errors)")

    print(f"\nDone: {stats['downloaded']} downloaded, {stats['skipped']} skipped, {stats['errors']} errors")

    if url_to_path:
        print("Rewriting internal links...")
        rewrite_links(BASE_DIR, url_to_path)
        print("Done")


if __name__ == "__main__":
    main()
