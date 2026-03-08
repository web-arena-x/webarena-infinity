"""
Task: Find the employer with the fewest followers on Handshake. Follow
them, save their active job, and add 'Full-time' to your preferred job
types in career interests.

Discovery: Fewest followers → Startup Grind Labs (emp_20, 420 followers).
Active job: job_21 (Full-Stack Engineer, Full-time).

Verify:
(1) emp_20 in followedEmployerIds
(2) job_21 in savedJobIds
(3) 'Full-time' in careerInterests.jobTypes
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
    if "emp_20" not in followed:
        errors.append("emp_20 (Startup Grind Labs) not followed.")

    saved = user.get("savedJobIds", [])
    if "job_21" not in saved:
        errors.append("job_21 not in savedJobIds.")

    job_types = user.get("careerInterests", {}).get("jobTypes", [])
    if "Full-time" not in job_types:
        errors.append(f"'Full-time' not in jobTypes. Current: {job_types}")

    if errors:
        return False, " | ".join(errors)
    return True, (
        "Startup Grind Labs identified (fewest followers). "
        "Followed, job_21 saved, Full-time added to job types."
    )
