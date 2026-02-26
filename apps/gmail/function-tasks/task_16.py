import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # The original Receipts label has id label_5
    label = next((l for l in state["labels"] if l["id"] == "label_5"), None)
    if not label:
        return False, "Label with id 'label_5' not found."

    if label["name"] != "Purchase Receipts":
        return False, f"Expected label name 'Purchase Receipts', got '{label['name']}'."

    return True, "Label 'Receipts' renamed to 'Purchase Receipts'."
