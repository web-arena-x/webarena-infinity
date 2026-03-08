"""
Task: The only unanswered Q&A question is about finance recruiting timelines.
Answer it with your advice, then follow both employers in the Finance
industry.

Discovery: qa_10 has 0 answers (asked by UPenn student about summer 2027
finance recruiting). Finance employers: JPMorgan (emp_02), Goldman (emp_06).

Verify:
(1) qa_10 has at least one answer from Maya
(2) emp_02 in followedEmployerIds
(3) emp_06 in followedEmployerIds
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    errors = []
    user = state.get("currentUser", {})

    questions = state.get("qaQuestions", [])
    qa_10 = next((q for q in questions if q.get("id") == "qa_10"), None)
    if qa_10 is None:
        errors.append("qa_10 not found.")
    else:
        has_answer = any(
            "maya" in a.get("authorName", "").lower()
            for a in qa_10.get("answers", [])
        )
        if not has_answer:
            errors.append("No answer from Maya on qa_10.")

    followed = user.get("followedEmployerIds", [])
    if "emp_02" not in followed:
        errors.append("emp_02 (JPMorgan) not followed.")
    if "emp_06" not in followed:
        errors.append("emp_06 (Goldman Sachs) not followed.")

    if errors:
        return False, " | ".join(errors)
    return True, (
        "Unanswered question (qa_10) answered. "
        "Both Finance employers followed."
    )
