import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})
    ask_ai = settings.get("askAi", {})
    enabled = ask_ai.get("enabled")

    if enabled is not False:
        return False, f"Expected askAi.enabled to be False, got {enabled}."

    return True, "Ask AI is turned off."
