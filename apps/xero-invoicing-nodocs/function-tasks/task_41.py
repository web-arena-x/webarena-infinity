import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = state["settings"]
    if settings.get("defaultBrandingThemeId") != "theme_2":
        return False, f"Expected 'theme_2' (Professional Blue), got '{settings.get('defaultBrandingThemeId')}'"
    return True, "Default branding theme changed to Professional Blue."
