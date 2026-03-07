import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})
    timezone = str(settings.get("timezone", ""))

    if ("Los_Angeles" in timezone or "Pacific" in timezone or timezone == "PT"):
        return True, f"Primary timezone changed to Pacific Time ({timezone})."

    return False, f"Expected timezone to be Pacific Time (containing 'Los_Angeles' or 'Pacific' or 'PT'), got '{timezone}'."
