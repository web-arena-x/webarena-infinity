import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify new color scheme with all 4 color values."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    schemes = state.get("themeSettings", {}).get("colors", {}).get("schemes", [])

    match = [s for s in schemes
             if s.get("background") == "#1a1a2e"
             and s.get("text") == "#eaeaea"
             and s.get("solidButtonBackground") == "#e94560"
             and s.get("solidButtonLabel") == "#ffffff"]

    if not match:
        return False, "No color scheme found with background '#1a1a2e', text '#eaeaea', solidButtonBackground '#e94560', solidButtonLabel '#ffffff'."

    return True, "Color scheme with all 4 specified colors found."
