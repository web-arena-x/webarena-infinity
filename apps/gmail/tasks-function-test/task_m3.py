import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = state.get("settings", {})
    categories = settings.get("categoriesEnabled", {})

    forums_enabled = categories.get("forums")
    updates_enabled = categories.get("updates")

    errors = []
    if forums_enabled is not False:
        errors.append(f"settings.categoriesEnabled.forums is {forums_enabled}, expected False")
    if updates_enabled is not False:
        errors.append(f"settings.categoriesEnabled.updates is {updates_enabled}, expected False")

    if errors:
        return False, "; ".join(errors)

    return True, "Task completed successfully."
