"""
Task: Save the highest-paid and lowest-paid active internships by hourly
rate. Follow the employer offering the lowest-paid one if you don't
already follow them.

Discovery:
  Highest-paid active internship: job_12 ($60/hr, Anthropic) — already saved.
  Lowest-paid active internship: job_30 ($38/hr, Salesforce).
  Salesforce (emp_19) is not followed.

Verify:
(1) job_12 in savedJobIds
(2) job_30 in savedJobIds
(3) emp_19 in followedEmployerIds
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
    if "job_12" not in saved:
        errors.append("job_12 (highest-paid internship) not in savedJobIds.")
    if "job_30" not in saved:
        errors.append("job_30 (lowest-paid internship) not in savedJobIds.")

    followed = user.get("followedEmployerIds", [])
    if "emp_19" not in followed:
        errors.append("emp_19 (Salesforce) not followed.")

    if errors:
        return False, " | ".join(errors)
    return True, (
        "Highest-paid (job_12, $60/hr) and lowest-paid (job_30, $38/hr) "
        "internships saved. Salesforce followed."
    )
