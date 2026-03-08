"""
Task: Find all student posts in the feed with at least 3 comments. Like
each of them. Then bookmark the most-liked employer post in the feed.

Discovery:
  Student posts with >= 3 comments:
    post_08 (Kevin O'Brien, 3 comments, likes=534)
    post_14 (David Lee, 3 comments, likes=276)
  Most-liked employer post: post_01 (Google, 342 likes).

Verify:
(1) post_08 likes > 534
(2) post_14 likes > 276
(3) post_01 bookmarked
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    errors = []

    posts = state.get("feedPosts", [])

    post_08 = next((p for p in posts if p.get("id") == "post_08"), None)
    if post_08 is None:
        errors.append("post_08 not found.")
    elif post_08.get("likes", 0) <= 534:
        errors.append(
            f"post_08 likes not incremented. "
            f"Expected > 534, got {post_08.get('likes')}"
        )

    post_14 = next((p for p in posts if p.get("id") == "post_14"), None)
    if post_14 is None:
        errors.append("post_14 not found.")
    elif post_14.get("likes", 0) <= 276:
        errors.append(
            f"post_14 likes not incremented. "
            f"Expected > 276, got {post_14.get('likes')}"
        )

    post_01 = next((p for p in posts if p.get("id") == "post_01"), None)
    if post_01 is None:
        errors.append("post_01 not found.")
    elif not post_01.get("bookmarked"):
        errors.append("post_01 not bookmarked.")

    if errors:
        return False, " | ".join(errors)
    return True, (
        "Student posts with 3+ comments liked. "
        "Most-liked employer post (Google) bookmarked."
    )
