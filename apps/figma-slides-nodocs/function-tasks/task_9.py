import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    presentations = state.get("presentations", [])
    match = [p for p in presentations if p.get("title") == "Brand Identity Guidelines v2.0"]
    if not match:
        return False, "No presentation found with title 'Brand Identity Guidelines v2.0'."

    pres = match[0]
    visibility = pres.get("shareSettings", {}).get("visibility")
    if visibility != "public":
        return False, f"Expected shareSettings.visibility 'public', got '{visibility}'."

    return True, "Presentation 'Brand Identity Guidelines v2.0' visibility changed to 'public'."
