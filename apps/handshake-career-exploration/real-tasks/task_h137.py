"""
Task: Find the Q&A question asked by a student from Morehouse College.
The answer mentions several diversity programs, one of which matches the
subject of an unread message you received. Read that message and bookmark
the feed post by the student who answered the Q&A question.

Discovery:
  Morehouse → qa_11 (Derek Williams).
  Answer: ans_13 by Aisha Mohammed, mentions 'Apple Pathways'.
  Unread message: msg_08 (Apple Pathways invitation), isRead=false.
  Aisha Mohammed's feed post: post_06 (NSBE conference).

Verify:
(1) msg_08 isRead
(2) post_06 bookmarked
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    errors = []

    messages = state.get("messages", [])
    msg_08 = next((m for m in messages if m.get("id") == "msg_08"), None)
    if msg_08 is None:
        errors.append("msg_08 not found.")
    elif not msg_08.get("isRead"):
        errors.append("msg_08 not marked as read.")

    posts = state.get("feedPosts", [])
    post_06 = next((p for p in posts if p.get("id") == "post_06"), None)
    if post_06 is None:
        errors.append("post_06 not found.")
    elif not post_06.get("bookmarked"):
        errors.append("post_06 not bookmarked.")

    if errors:
        return False, " | ".join(errors)
    return True, (
        "Morehouse Q&A (qa_11) → Apple Pathways → msg_08 read. "
        "Aisha Mohammed's post (post_06) bookmarked."
    )
