"""Task M20: Switch the meeting link provider to Zoom."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    settings = state.get("settings", {})
    calendar = settings.get("calendar", {})
    provider = calendar.get("meetingLinkProvider")

    if provider == "zoom":
        return True, "Meeting link provider is set to 'zoom'"
    return False, f"Meeting link provider is '{provider}', expected 'zoom'"
