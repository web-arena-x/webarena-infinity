"""Task E11: Switch to compact display density."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    try:
        density = state["settings"]["general"]["density"]
    except (KeyError, TypeError) as e:
        return False, f"Could not read settings.general.density: {e}"

    if density != "compact":
        return False, f"density is '{density}' — expected 'compact'"

    return True, "Display density is set to 'compact'."
