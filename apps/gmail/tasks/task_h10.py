import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = state.get("settings", {})
    keyboard_shortcuts = settings.get("keyboardShortcutsEnabled")
    importance_markers = settings.get("importanceMarkers")
    default_reply = settings.get("defaultReplyBehavior")

    issues = []

    if keyboard_shortcuts is not False:
        issues.append(f"keyboardShortcutsEnabled is {keyboard_shortcuts}, expected false")
    if importance_markers is not False:
        issues.append(f"importanceMarkers is {importance_markers}, expected false")
    if default_reply != "reply_all":
        issues.append(f"defaultReplyBehavior is '{default_reply}', expected 'reply_all'")

    if not issues:
        return True, "Task completed successfully."
    else:
        return False, f"Settings issues: {'; '.join(issues)}."
