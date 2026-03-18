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

    # pres_001 (Q1 Product Roadmap) sharedWith=[user_002, user_003, user_004]
    # pres_003 should now include those users plus existing user_001
    required_users = {"user_001", "user_002", "user_003", "user_004"}
    ss = pitch.get("shareSettings", {})
    shared_with = ss.get("sharedWith", [])
    shared_ids = set(shared_with)

    missing_users = required_users - shared_ids
    if missing_users:
        errors.append(f"sharedWith missing users from Q1 Roadmap: {missing_users}")

    # visibility should be team
    vis = ss.get("visibility")
    if vis != "team":
        errors.append(f"visibility is {vis!r}, expected 'team'")

    if errors:
        return False, f"pres_003 (Series B Fundraising Pitch) issues: {'; '.join(errors)}"

    return True, "Series B Fundraising Pitch now shares Q1 Roadmap's members and has team visibility."
