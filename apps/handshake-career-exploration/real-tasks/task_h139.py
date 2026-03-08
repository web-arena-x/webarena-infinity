"""
Task: Update your career interests: remove 'UX Designer' from your roles,
add 'DevOps Engineer' and 'Cloud Engineer'. Change your career community
to 'Engineering'. Then save both active jobs from the only employer in the
Artificial Intelligence industry.

Discovery: AI industry → Anthropic (emp_15). Active jobs: job_12, job_29.

Verify:
(1) 'UX Designer' not in roles
(2) 'DevOps Engineer' in roles
(3) 'Cloud Engineer' in roles
(4) careerCommunity == 'Engineering'
(5) job_12, job_29 in savedJobIds
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    errors = []
    user = state.get("currentUser", {})
    ci = user.get("careerInterests", {})

    roles = ci.get("roles", [])
    if "UX Designer" in roles:
        errors.append("'UX Designer' still in roles.")
    if "DevOps Engineer" not in roles:
        errors.append("'DevOps Engineer' not in roles.")
    if "Cloud Engineer" not in roles:
        errors.append("'Cloud Engineer' not in roles.")

    community = ci.get("careerCommunity")
    if community != "Engineering":
        errors.append(
            f"careerCommunity is '{community}', expected 'Engineering'."
        )

    saved = user.get("savedJobIds", [])
    for jid in ["job_12", "job_29"]:
        if jid not in saved:
            errors.append(f"{jid} not in savedJobIds.")

    if errors:
        return False, " | ".join(errors)
    return True, (
        "Career interests updated: UX Designer removed, DevOps/Cloud added, "
        "community set to Engineering. Both Anthropic jobs saved."
    )
