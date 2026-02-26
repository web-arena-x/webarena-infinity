import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = state.get("settings", {})

    errors = []
    theme = settings.get("theme", "")
    if theme.lower() != "soft":
        errors.append(f"settings.theme is '{theme}', expected 'soft'")

    density = settings.get("density", "")
    if density.lower() != "comfortable":
        errors.append(f"settings.density is '{density}', expected 'comfortable'")

    if errors:
        return False, "; ".join(errors)

    return True, "Task completed successfully."
