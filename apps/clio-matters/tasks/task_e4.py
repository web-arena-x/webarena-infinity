import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    notification_settings = state.get("notificationSettings")
    if notification_settings is None:
        return False, "No notificationSettings found in application state."

    budget_threshold = notification_settings.get("budget_threshold")
    if budget_threshold is not False:
        return False, f"budget_threshold is {budget_threshold}, expected False."

    return True, "Budget threshold notifications have been turned off."
