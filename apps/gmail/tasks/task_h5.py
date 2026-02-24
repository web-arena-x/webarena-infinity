import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = state.get("settings", {})
    inbox_type = settings.get("inboxType")
    sections = settings.get("multipleInboxSections", [])

    issues = []

    if inbox_type != "multiple_inboxes":
        issues.append(f"inboxType is '{inbox_type}', expected 'multiple_inboxes'")

    if len(sections) == 0:
        issues.append("multipleInboxSections is empty")
    else:
        first_section = sections[0]
        query = first_section.get("query", "")
        name = first_section.get("name", "")

        if query != "label:Action Required":
            issues.append(f"first section query is '{query}', expected 'label:Action Required'")
        if name != "Action Items":
            issues.append(f"first section name is '{name}', expected 'Action Items'")

    if not issues:
        return True, "Task completed successfully."
    else:
        return False, f"Settings issues: {'; '.join(issues)}."
