"""
Task: Three employers have closed job listings. Follow the one whose
closed job received the most applicants, and bookmark their feed post.

Discovery:
  Closed jobs: job_03 (JPMorgan, 5210), job_10 (Goldman, 4100),
  job_14 (Bain, 2890). Most applicants → JPMorgan (emp_02).
  JPMorgan feed post: post_15.

Verify:
(1) emp_02 in followedEmployerIds
(2) post_15 bookmarked
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    errors = []
    user = state.get("currentUser", {})

    followed = user.get("followedEmployerIds", [])
    if "emp_02" not in followed:
        errors.append("emp_02 (JPMorgan) not followed.")

    posts = state.get("feedPosts", [])
    post_15 = next((p for p in posts if p.get("id") == "post_15"), None)
    if post_15 is None:
        errors.append("post_15 not found.")
    elif not post_15.get("bookmarked"):
        errors.append("post_15 not bookmarked.")

    if errors:
        return False, " | ".join(errors)
    return True, (
        "JPMorgan identified (closed job with most applicants). "
        "Followed and feed post bookmarked."
    )
