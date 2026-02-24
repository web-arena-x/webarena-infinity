import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify layout: pageWidth=1400, sectionSpacing=48, gridHorizontalSpace=24, gridVerticalSpace=20."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    layout = state.get("themeSettings", {}).get("layout", {})

    checks = [
        ("pageWidth", 1400),
        ("sectionSpacing", 48),
        ("gridHorizontalSpace", 24),
        ("gridVerticalSpace", 20),
    ]

    for key, expected in checks:
        val = layout.get(key)
        if val != expected:
            return False, f"Expected {key}={expected}, got {val}."

    return True, "Layout settings: pageWidth=1400, sectionSpacing=48, gridHorizontalSpace=24, gridVerticalSpace=20."
