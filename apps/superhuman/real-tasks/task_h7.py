"""Task H7: Delete the Partnership label and add Customer label to inbox emails that had it."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    # Check Partnership label (label_9) is deleted
    labels = state.get("labels", [])
    for label in labels:
        if label.get("id") == "label_9" or label.get("name") == "Partnership":
            return False, f"Partnership label still exists: {label}"

    # Check target emails have Customer label (label_6)
    target_ids = ["email_007", "email_013", "email_041"]
    emails_by_id = {e["id"]: e for e in state.get("emails", [])}

    failures = []
    for eid in target_ids:
        email = emails_by_id.get(eid)
        if email is None:
            failures.append(f"{eid}: not found in state")
            continue
        email_labels = email.get("labels", [])
        if "label_6" not in email_labels:
            failures.append(f"{eid}: missing Customer label (label_6), has labels {email_labels}")

    if failures:
        return False, "Not all former Partnership emails have Customer label: " + "; ".join(failures)

    return True, "Partnership label deleted and Customer label applied to email_007, email_013, email_041."
