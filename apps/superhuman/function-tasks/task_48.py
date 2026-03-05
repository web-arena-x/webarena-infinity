import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that scheduling auto-drafts have been disabled."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()

    try:
        scheduling = state["settings"]["autoDrafts"]["scheduling"]
    except (KeyError, TypeError) as e:
        return False, f"Could not find settings.autoDrafts.scheduling: {e}"

    if scheduling is False:
        return True, "Scheduling auto-drafts are disabled."
    return False, f"Expected settings.autoDrafts.scheduling to be False, got {scheduling!r}."
