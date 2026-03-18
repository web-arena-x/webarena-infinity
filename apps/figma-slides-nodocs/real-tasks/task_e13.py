import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Expected HTTP 200, got {resp.status_code}"
    state = resp.json()
    presentations = state.get("presentations", [])
    pres = next((p for p in presentations if p.get("id") == "pres_007"), None)
    if pres is None:
        return False, "Presentation pres_007 (Client Proposal — TechVentures Redesign) not found"
    share_settings = pres.get("shareSettings", {})
    shared_with = share_settings.get("sharedWith", [])
    if "user_007" not in shared_with:
        return True, "user_007 (David Kim) is not in pres_007 shareSettings.sharedWith as expected"
    return False, f"Expected user_007 to be removed from pres_007 shareSettings.sharedWith, but found user_007 in {shared_with}"
