import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify page width is 1200 and section spacing is 36."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    layout = state.get("themeSettings", {}).get("layout", {})

    pw = layout.get("pageWidth")
    if pw != 1200:
        return False, f"Expected pageWidth=1200, got {pw}."

    ss = layout.get("sectionSpacing")
    if ss != 36:
        return False, f"Expected sectionSpacing=36, got {ss}."

    return True, "Page width is 1200px and section spacing is 36px."
