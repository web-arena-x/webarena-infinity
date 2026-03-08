"""
Task: Create a feed post for 'People at your school' sharing advice about
resume formatting. Then mark as helpful every answer on the Q&A question
about salary negotiation.

Discovery: Salary negotiation Q&A → qa_05.
Answers: ans_07 (helpful=89), ans_08 (helpful=72).

Verify:
(1) New post with audience 'school' and content about resume
(2) ans_07 helpful > 89
(3) ans_08 helpful > 72
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    errors = []

    # Check 1: new school-audience post about resume
    posts = state.get("feedPosts", [])
    user_id = state.get("currentUser", {}).get("id", "")
    found_post = any(
        p.get("authorId") == user_id
        and p.get("audience") == "school"
        and "resume" in p.get("content", "").lower()
        for p in posts
    )
    if not found_post:
        errors.append(
            "No new post from user with audience 'school' mentioning resume."
        )

    # Check 2-3: salary negotiation answers marked helpful
    questions = state.get("qaQuestions", [])
    qa_05 = next((q for q in questions if q.get("id") == "qa_05"), None)
    if qa_05 is None:
        errors.append("qa_05 not found.")
    else:
        for ans_id, seed_helpful in [("ans_07", 89), ("ans_08", 72)]:
            ans = next(
                (a for a in qa_05.get("answers", []) if a.get("id") == ans_id),
                None,
            )
            if ans is None:
                errors.append(f"{ans_id} not found in qa_05.")
            elif ans.get("helpful", 0) <= seed_helpful:
                errors.append(
                    f"{ans_id} helpful not incremented. "
                    f"Expected > {seed_helpful}, got {ans.get('helpful')}"
                )

    if errors:
        return False, " | ".join(errors)
    return True, (
        "School-audience post about resume created. "
        "Both salary negotiation answers marked helpful."
    )
