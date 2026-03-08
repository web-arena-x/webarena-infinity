"""
Task: The student who posted a FAANG interview study plan in the feed also
answered a Q&A question about system design resources. Mark that Q&A
answer as helpful and like their feed post.

Discovery: FAANG study plan → Kevin O'Brien (post_08).
System design Q&A → qa_06, answered by Kevin O'Brien (ans_09).

Verify:
(1) ans_09 helpful > 56 (seed value)
(2) post_08 likes > 534 (seed value)
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    errors = []

    questions = state.get("qaQuestions", [])
    qa_06 = next((q for q in questions if q.get("id") == "qa_06"), None)
    if qa_06 is None:
        errors.append("qa_06 not found.")
    else:
        ans_09 = next(
            (a for a in qa_06.get("answers", []) if a.get("id") == "ans_09"),
            None,
        )
        if ans_09 is None:
            errors.append("ans_09 not found in qa_06.")
        elif ans_09.get("helpful", 0) <= 56:
            errors.append(
                f"ans_09 helpful not incremented. "
                f"Expected > 56, got {ans_09.get('helpful')}"
            )

    posts = state.get("feedPosts", [])
    post_08 = next((p for p in posts if p.get("id") == "post_08"), None)
    if post_08 is None:
        errors.append("post_08 not found.")
    elif post_08.get("likes", 0) <= 534:
        errors.append(
            f"post_08 likes not incremented. "
            f"Expected > 534, got {post_08.get('likes')}"
        )

    if errors:
        return False, " | ".join(errors)
    return True, (
        "Kevin O'Brien identified via FAANG post and system design Q&A. "
        "ans_09 marked helpful, post_08 liked."
    )
