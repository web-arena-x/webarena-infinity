import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: Spelling language Japanese, big nudge 50, default alignment right."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    prefs = state.get("preferences", {})
    errors = []

    if prefs.get("spellingLanguage") != "Japanese":
        errors.append(f"spellingLanguage: expected 'Japanese', got '{prefs.get('spellingLanguage')}'.")
    if prefs.get("bigNudgeAmount") != 50:
        errors.append(f"bigNudgeAmount: expected 50, got {prefs.get('bigNudgeAmount')}.")
    if prefs.get("defaultHorizontalAlign") != "right":
        errors.append(f"defaultHorizontalAlign: expected 'right', got '{prefs.get('defaultHorizontalAlign')}'.")

    if errors:
        return False, "; ".join(errors)
    return True, "Settings updated: Japanese spelling, big nudge 50, default align right."
