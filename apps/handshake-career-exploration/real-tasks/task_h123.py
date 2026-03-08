"""
Task: An employer's alumni said they 'grew more in my first year than I
expected'. Save their active job with the most applicants and comment on
their feed post about the expanded internship program.

Discovery: Testimonial → Google (emp_01), Sarah Kim.
Google active jobs by applicants: job_02 (2456) > job_01 (1842) > job_22 (1123).
Google feed post about expanded internship: post_01.

Verify:
(1) job_02 in savedJobIds
(2) post_01 has new comment from Maya
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    errors = []
    user = state.get("currentUser", {})

    saved = user.get("savedJobIds", [])
    if "job_02" not in saved:
        errors.append(f"job_02 not in savedJobIds. Current: {saved}")

    posts = state.get("feedPosts", [])
    post_01 = next((p for p in posts if p.get("id") == "post_01"), None)
    if post_01 is None:
        errors.append("post_01 not found.")
    else:
        has_comment = any(
            "maya" in c.get("authorName", "").lower()
            for c in post_01.get("comments", [])
        )
        if not has_comment:
            errors.append("No comment from Maya on post_01.")

    if errors:
        return False, " | ".join(errors)
    return True, (
        "Google identified via testimonial. "
        "Most-applied job (job_02) saved and post_01 commented."
    )
