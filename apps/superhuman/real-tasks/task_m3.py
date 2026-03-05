"""Task M3: Remove the Read Later label from the Pragmatic Engineer newsletter."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    emails = state.get("emails", [])
    target = None
    for email in emails:
        if email.get("id") == "email_029":
            target = email
            break

    if target is None:
        return False, "Could not find email_029 (Pragmatic Engineer newsletter)"

    labels = target.get("labels", [])
    if "label_8" not in labels:
        return True, "Read Later label (label_8) is not present on email_029"
    return False, f"label_8 (Read Later) still present in email_029 labels: {labels}"
