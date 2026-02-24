import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify badges: salePosition='Top right', saleShape='Circle', soldOutPosition='Bottom right'."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    badges = state.get("themeSettings", {}).get("badges", {})

    if badges.get("salePosition") != "Top right":
        return False, f"Expected salePosition='Top right', got '{badges.get('salePosition')}'."

    if badges.get("saleShape") != "Circle":
        return False, f"Expected saleShape='Circle', got '{badges.get('saleShape')}'."

    if badges.get("soldOutPosition") != "Bottom right":
        return False, f"Expected soldOutPosition='Bottom right', got '{badges.get('soldOutPosition')}'."

    return True, "Badges: sale Top right/Circle, sold out Bottom right."
