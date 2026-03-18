import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    presentations = state.get("presentations", [])
    match = [p for p in presentations if p.get("title") == "Onboarding Training Module"]
    if not match:
        return False, "No presentation found with title 'Onboarding Training Module'."

    pres = match[0]
    share = pres.get("shareSettings", {})

    visibility = share.get("visibility")
    if visibility != "team":
        return False, f"Expected shareSettings.visibility 'team', got '{visibility}'."

    allow_comments = share.get("allowComments")
    if allow_comments is not True:
        return False, f"Expected shareSettings.allowComments to be true, got {allow_comments}."

    return True, "Onboarding Training Module visibility set to 'team' and commenting enabled."
