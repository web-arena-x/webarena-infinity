"""Task M14: Remove the Customer label from Anita Sharma's DevBridge feedback email."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    emails = state.get("emails", [])
    target = None
    for email in emails:
        if email.get("id") == "email_039":
            target = email
            break

    if target is None:
        return False, "Could not find email_039 (DevBridge integration feedback)"

    labels = target.get("labels", [])
    if "label_6" not in labels:
        return True, "Customer label (label_6) is not present on email_039"
    return False, f"label_6 (Customer) still present in email_039 labels: {labels}"
