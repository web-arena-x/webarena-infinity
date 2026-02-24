import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify revealSectionsOnScroll is enabled."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    val = state.get("themeSettings", {}).get("animations", {}).get("revealSectionsOnScroll")
    if val is not True:
        return False, f"Expected revealSectionsOnScroll=true, got {val}."

    return True, "Reveal sections on scroll is enabled."
