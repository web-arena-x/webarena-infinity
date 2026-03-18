import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to get state: {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])

    pres_map = {p["id"]: p for p in presentations}
    if "pres_012" not in pres_map:
        return False, "pres_012 (Q4 2025 Revenue Analysis) not found in state."

    p = pres_map["pres_012"]
    errors = []

    # All 8 users should be in sharedWith
    all_users = {
        "user_001", "user_002", "user_003", "user_004",
        "user_005", "user_006", "user_007", "user_008"
    }
    ss = p.get("shareSettings", {})
    shared_with = ss.get("sharedWith", [])
    shared_ids = set(shared_with)

    missing_users = all_users - shared_ids
    if missing_users:
        errors.append(f"sharedWith missing users: {missing_users}")

    # visibility should be organization
    vis = ss.get("visibility")
    if vis != "organization":
        errors.append(f"visibility is {vis!r}, expected 'organization'")

    # allowComments should be true
    if not ss.get("allowComments"):
        errors.append("allowComments is not true")

    # allowEditing should be true
    if not ss.get("allowEditing"):
        errors.append("allowEditing is not true")

    if errors:
        return False, f"pres_012 (Q4 2025 Revenue Analysis) issues: {'; '.join(errors)}"

    return True, "Q4 2025 Revenue Analysis is shared with all 8 users, organization visibility, comments and editing enabled."
