import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find a filter matching emails from noreply@medium.com
    matching_filter = next(
        (f for f in state["filters"]
         if f["criteria"]["from"] == "noreply@medium.com"),
        None,
    )
    if not matching_filter:
        return False, "Filter with criteria from 'noreply@medium.com' not found."

    # Check that the filter applies the Newsletters label (label_6)
    newsletters_label = next((l for l in state["labels"] if l["name"] == "Newsletters"), None)
    expected_label_id = newsletters_label["id"] if newsletters_label else "label_6"

    if matching_filter["actions"].get("label") != expected_label_id:
        return False, f"Expected filter action label '{expected_label_id}', got '{matching_filter['actions'].get('label')}'."

    if not matching_filter["actions"].get("archive"):
        return False, "Filter action 'archive' (skip inbox) is not enabled."

    return True, "Filter created: from 'noreply@medium.com', apply Newsletters label, archive."
