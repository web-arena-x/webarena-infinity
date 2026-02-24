import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify body font size scale is 120."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    val = state.get("themeSettings", {}).get("typography", {}).get("bodyFontSizeScale")
    if val != 120:
        return False, f"Expected bodyFontSizeScale=120, got {val}."

    return True, "Body font size scale is 120%."
