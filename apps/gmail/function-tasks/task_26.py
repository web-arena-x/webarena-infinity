import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    cat_enabled = state["settings"].get("categoriesEnabled", {})
    if cat_enabled.get("social") is not False:
        return False, f"Expected categoriesEnabled.social to be false, got {cat_enabled.get('social')}."

    return True, "Social category tab has been disabled."
