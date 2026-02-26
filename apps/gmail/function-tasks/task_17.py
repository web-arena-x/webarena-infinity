import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Check that the Education label no longer exists
    edu_label = next((l for l in state["labels"] if l["name"] == "Education"), None)
    if edu_label:
        return False, "Label 'Education' still exists."

    # Check that emails no longer reference label_8 (the Education label id)
    emails_with_label = [e for e in state["emails"] if "label_8" in e["labels"]]
    if emails_with_label:
        return False, f"Found {len(emails_with_label)} email(s) still referencing 'label_8'."

    return True, "Label 'Education' deleted and removed from all emails."
