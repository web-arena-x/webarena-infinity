import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    presentations = state.get("presentations", [])
    match = [p for p in presentations if p.get("title") == "Series B Fundraising Pitch"]
    if not match:
        return False, "No presentation found with title 'Series B Fundraising Pitch'."

    pres = match[0]
    shared_with = pres.get("shareSettings", {}).get("sharedWith", [])
    if "user_002" not in shared_with:
        return False, f"Expected 'user_002' in sharedWith, got {shared_with}."

    return True, "Marcus Rivera (user_002) added to 'Series B Fundraising Pitch' sharing."
