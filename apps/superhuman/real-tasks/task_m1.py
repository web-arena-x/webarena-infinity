"""Task M1: Apply the Project Alpha label to Jamie's Q2 roadmap email."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    emails = state.get("emails", [])
    target = None
    for email in emails:
        if email.get("id") == "email_115":
            target = email
            break

    if target is None:
        return False, "Could not find email_115 (Re: Re: Q2 roadmap prioritization)"

    labels = target.get("labels", [])
    if "label_1" in labels:
        return True, "Project Alpha label (label_1) is applied to email_115"
    return False, f"label_1 (Project Alpha) not found in email_115 labels: {labels}"
