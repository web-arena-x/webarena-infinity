import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Change the default branding theme to Professional Blue."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    settings = state.get("settings", {})
    theme_id = settings.get("defaultBrandingThemeId")

    if theme_id == "theme_2":
        return True, "Default branding theme is set to 'theme_2' (Professional Blue)"
    else:
        return False, f"settings.defaultBrandingThemeId is '{theme_id}', expected 'theme_2'"
