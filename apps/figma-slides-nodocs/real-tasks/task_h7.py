import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to get state: {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])

    pres_map = {p["id"]: p for p in presentations}
    if "pres_003" not in pres_map:
        return False, "pres_003 (Series B Fundraising Pitch) not found in state."

    pitch = pres_map["pres_003"]
    errors = []

    # Check sharedWith contains all editors: user_002, user_003, user_004, user_006, user_008
    # plus existing user_001
    required_users = {"user_001", "user_002", "user_003", "user_004", "user_006", "user_008"}
    ss = pitch.get("shareSettings", {})
    shared_with = ss.get("sharedWith", [])
    shared_ids = set(shared_with)

    missing_users = required_users - shared_ids
    if missing_users:
        errors.append(f"sharedWith is missing users: {missing_users}")

    # Check allowEditing is true
    allow_editing = ss.get("allowEditing")
    if not allow_editing:
        errors.append("allowEditing is not true")

    if errors:
        return False, f"pres_003 (Series B Fundraising Pitch) issues: {'; '.join(errors)}"

    return True, "Series B Fundraising Pitch is shared with all editors and editing is enabled."
