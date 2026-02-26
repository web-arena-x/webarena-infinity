import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    filters = state.get("filters", [])
    if not filters:
        return False, "No filters found in state."

    target_filter = None
    for f in filters:
        criteria = f.get("criteria", {})
        from_val = (criteria.get("from") or "").lower()
        subject_val = (criteria.get("subject") or "").lower()
        if "coursera" in from_val and "certificate" in subject_val:
            target_filter = f
            break

    if not target_filter:
        return False, "No filter found with criteria.from containing 'coursera' and criteria.subject containing 'certificate'."

    actions = target_filter.get("actions", {})

    if actions.get("label") != "label_8":
        return False, f"Filter actions.label is '{actions.get('label')}', expected 'label_8'."

    if actions.get("markRead") is not True:
        return False, f"Filter actions.markRead is {actions.get('markRead')}, expected True."

    if actions.get("archive") is not True:
        return False, f"Filter actions.archive is {actions.get('archive')}, expected True."

    return True, "Task completed successfully."
