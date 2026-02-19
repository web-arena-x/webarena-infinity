import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify communication preferences: changelog=false, tips=false, productUpdates=true."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    comms = state.get("communicationPreferences", {})

    changelog = comms.get("changelog")
    tips = comms.get("tips")
    product = comms.get("productUpdates")

    if changelog is not False:
        return False, f"Expected changelog=false, got {changelog}."
    if tips is not False:
        return False, f"Expected tips=false, got {tips}."
    if product is not True:
        return False, f"Expected productUpdates=true, got {product}."

    return True, "Communication preferences updated correctly."
