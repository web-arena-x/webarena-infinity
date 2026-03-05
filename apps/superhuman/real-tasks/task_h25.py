"""Task H25: Apply the Urgent label to Brian Scott's MSA contract redlines email, not the legal hold."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    emails_by_id = {e["id"]: e for e in state.get("emails", [])}

    # email_003 = MSA contract redlines — should have Urgent label (label_7)
    email_003 = emails_by_id.get("email_003")
    if email_003 is None:
        return False, "email_003 not found in state."

    labels_003 = email_003.get("labels", [])
    if "label_7" not in labels_003:
        return False, f"email_003 missing Urgent label (label_7), has labels {labels_003}."

    return True, "email_003 (MSA contract redlines) has Urgent label applied."
