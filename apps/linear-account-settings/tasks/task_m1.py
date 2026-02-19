import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify that the default home view was changed to 'my_issues'."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    prefs = state.get("preferences", {})
    home_view = prefs.get("defaultHomeView")

    if home_view != "my_issues":
        return False, f"Expected defaultHomeView='my_issues', got '{home_view}'."

    return True, "Default home view successfully changed to 'My Issues'."
