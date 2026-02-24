import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = state.get("settings", {})
    preview_pane = settings.get("previewPane")
    max_page_size = settings.get("maxPageSize")

    issues = []

    if preview_pane != "right":
        issues.append(f"previewPane is '{preview_pane}', expected 'right'")
    if max_page_size != 25:
        issues.append(f"maxPageSize is {max_page_size}, expected 25")

    if not issues:
        return True, "Task completed successfully."
    else:
        return False, f"Settings issues: {'; '.join(issues)}."
