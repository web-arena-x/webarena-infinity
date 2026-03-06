import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    themes = state.get("brandingThemes", [])
    theme = None
    for t in themes:
        if t.get("id") == "theme_retail":
            theme = t
            break

    if theme is None:
        return False, "Branding theme with id 'theme_retail' not found."

    name = theme.get("name", "")
    if name != "Retail Premium":
        return False, f"Theme 'theme_retail' name is '{name}', expected 'Retail Premium'."

    return True, "Retail branding theme renamed to 'Retail Premium'."
