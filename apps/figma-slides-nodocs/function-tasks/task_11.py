import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    presentations = state.get("presentations", [])
    match = [p for p in presentations if p.get("title") == "Q1 2026 Product Roadmap"]
    if not match:
        return False, "No presentation found with title 'Q1 2026 Product Roadmap'."

    pres = match[0]
    allow_editing = pres.get("shareSettings", {}).get("allowEditing")
    if allow_editing is not True:
        return False, f"Expected shareSettings.allowEditing to be true, got {allow_editing}."

    return True, "Editing enabled on 'Q1 2026 Product Roadmap'."
