import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify new color scheme with gradient and text '#ffffff'."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    schemes = state.get("themeSettings", {}).get("colors", {}).get("schemes", [])

    expected_gradient = "linear-gradient(135deg, #667eea, #764ba2)"
    match = [s for s in schemes
             if s.get("backgroundGradient") == expected_gradient
             and s.get("text") == "#ffffff"]

    if not match:
        return False, f"No color scheme found with gradient '{expected_gradient}' and text '#ffffff'."

    return True, "Color scheme with specified gradient and white text found."
