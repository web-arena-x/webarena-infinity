import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    email = next(
        (e for e in state["emails"] if e["subject"] == "SaaS Platform Q1 Pricing Update"),
        None,
    )
    if not email:
        return False, "Email 'SaaS Platform Q1 Pricing Update' not found."

    # label_3 is the "Finance" label
    finance_label = next((l for l in state["labels"] if l["name"] == "Finance"), None)
    if not finance_label:
        return False, "Finance label not found in state."

    if finance_label["id"] not in email["labels"]:
        return False, f"Email does not have the 'Finance' label (expected '{finance_label['id']}' in {email['labels']})."

    return True, "Finance label applied to email 'SaaS Platform Q1 Pricing Update'."
