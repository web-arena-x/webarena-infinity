import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    presentations = state.get("presentations", [])
    match = [p for p in presentations if p.get("title") == "Client Proposal \u2014 TechVentures Redesign"]
    if not match:
        return False, "No presentation found with title 'Client Proposal \u2014 TechVentures Redesign'."

    pres = match[0]
    shared_with = pres.get("shareSettings", {}).get("sharedWith", [])
    if "user_003" in shared_with:
        return False, f"Expected 'user_003' to be removed from sharedWith, but it is still present: {shared_with}."

    return True, "Anika Patel (user_003) removed from 'Client Proposal \u2014 TechVentures Redesign' sharing."
