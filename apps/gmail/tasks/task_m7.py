import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = state.get("settings", {})
    categories_enabled = settings.get("categoriesEnabled", {})
    social = categories_enabled.get("social")

    if social is False:
        return True, "Task completed successfully."
    else:
        return False, f"settings.categoriesEnabled.social is {social}, expected false."
