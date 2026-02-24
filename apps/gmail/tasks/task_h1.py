import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    filters = state.get("filters", [])
    for f in filters:
        criteria = f.get("criteria", {})
        actions = f.get("actions", {})
        criteria_from = (criteria.get("from") or "").lower()

        if "vercel" in criteria_from:
            has_work_label = actions.get("label") == "label_1"
            has_mark_read = actions.get("markRead") is True

            if has_work_label and has_mark_read:
                return True, "Task completed successfully."
            else:
                issues = []
                if not has_work_label:
                    issues.append(f"actions.label is '{actions.get('label')}', expected 'label_1'")
                if not has_mark_read:
                    issues.append(f"actions.markRead is {actions.get('markRead')}, expected true")
                return False, f"Filter matching 'vercel' found but: {', '.join(issues)}."

    return False, "No filter with criteria.from containing 'vercel' found."
