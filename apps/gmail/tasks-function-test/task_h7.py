import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = state.get("settings", {})

    sections = settings.get("multipleInboxSections", [])
    if len(sections) < 2:
        return False, f"multipleInboxSections has {len(sections)} entries, need at least 2."

    section = sections[1]

    query = section.get("query")
    if query != "is:important":
        return False, f"multipleInboxSections[1].query is '{query}', expected 'is:important'."

    name = section.get("name")
    if name != "Priority Items":
        return False, f"multipleInboxSections[1].name is '{name}', expected 'Priority Items'."

    position = settings.get("multipleInboxPosition")
    if position != "above":
        return False, f"settings.multipleInboxPosition is '{position}', expected 'above'."

    return True, "Task completed successfully."
