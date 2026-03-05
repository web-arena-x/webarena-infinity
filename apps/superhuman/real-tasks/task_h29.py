"""Task H29: Remove the Read Later label from every email that has it, then delete the label itself."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    failures = []

    # Check label_8 (Read Later) is deleted from labels list
    labels = state.get("labels", [])
    for label in labels:
        if label.get("id") == "label_8" or label.get("name") == "Read Later":
            failures.append(f"Read Later label still exists: {label}")
            break

    # Check no emails still reference label_8
    for email in state.get("emails", []):
        if "label_8" in email.get("labels", []):
            failures.append(f"{email['id']}: still has label_8 in labels")

    if failures:
        return False, "Read Later cleanup failed: " + "; ".join(failures)

    return True, "Read Later label removed from all emails and deleted."
