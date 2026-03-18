import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Change the default due date terms to 30 days after invoice date."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    settings = state.get("settings", {})
    terms = settings.get("defaultDueDateTerms")

    if terms == "30":
        return True, "Default due date terms is set to '30'"
    else:
        return False, f"settings.defaultDueDateTerms is {terms!r}, expected '30'"
