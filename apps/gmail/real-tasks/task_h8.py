"""
Task H8: Switch to dark theme with compact density, disable hover actions
and dynamic email, change undo send delay to 20s.
Verify settings:
  - theme='dark'
  - density='compact'
  - hoverActions=False
  - dynamicEmail=False
  - undoSendDelay=20
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    settings = state.get("settings", {})

    errors = []

    if settings.get("theme") != "dark":
        errors.append(f"theme={settings.get('theme')!r}, expected 'dark'")

    if settings.get("density") != "compact":
        errors.append(f"density={settings.get('density')!r}, expected 'compact'")

    if settings.get("hoverActions") is not False:
        errors.append(
            f"hoverActions={settings.get('hoverActions')!r}, expected False"
        )

    if settings.get("dynamicEmail") is not False:
        errors.append(
            f"dynamicEmail={settings.get('dynamicEmail')!r}, expected False"
        )

    undo_delay = settings.get("undoSendDelay")
    if undo_delay != 20:
        errors.append(f"undoSendDelay={undo_delay!r}, expected 20")

    if errors:
        return False, "Settings check failed: " + "; ".join(errors)

    return True, (
        "Settings updated: dark theme, compact density, hover actions disabled, "
        "dynamic email disabled, undo send delay 20s."
    )
