"""
Task: Find all employers with exactly one active job listing. For those
you currently follow, save their job. For those you don't follow, follow
them instead.

Discovery: Employers with exactly 1 active job:
  Followed → save job:
    Stripe (emp_10) → job_09
    Tesla (emp_12) → job_13
  Not followed → follow:
    JPMorgan (emp_02), McKinsey (emp_04), Goldman (emp_06),
    Deloitte (emp_08), Spotify (emp_13), Epic (emp_14),
    Nike (emp_16), Palantir (emp_17), TFA (emp_18),
    Startup Grind Labs (emp_20)

Verify:
(1) job_09, job_13 in savedJobIds
(2) emp_02, emp_04, emp_06, emp_08, emp_13, emp_14, emp_16, emp_17,
    emp_18, emp_20 in followedEmployerIds
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
    for jid in ["job_09", "job_13"]:
        if jid not in saved:
            errors.append(f"{jid} not in savedJobIds.")

    followed = user.get("followedEmployerIds", [])
    must_follow = [
        "emp_02", "emp_04", "emp_06", "emp_08", "emp_13",
        "emp_14", "emp_16", "emp_17", "emp_18", "emp_20",
    ]
    for eid in must_follow:
        if eid not in followed:
            errors.append(f"{eid} not in followedEmployerIds.")

    if errors:
        return False, " | ".join(errors)
    return True, (
        "Employers with 1 active job identified. "
        "Followed employers' jobs saved; unfollowed employers now followed."
    )
