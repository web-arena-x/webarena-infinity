import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify a new color scheme exists with background '#f0e6d3' and text '#1a1a2e'."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    schemes = state.get("themeSettings", {}).get("colors", {}).get("schemes", [])

    # Look for a scheme (beyond the original 5) with the target colors
    match = [s for s in schemes if s.get("background") == "#f0e6d3" and s.get("text") == "#1a1a2e"]
    if not match:
        return False, "No color scheme found with background '#f0e6d3' and text '#1a1a2e'."

    return True, "New color scheme with correct background and text colors found."
