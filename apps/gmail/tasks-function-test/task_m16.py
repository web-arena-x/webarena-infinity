import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    filters = state.get("filters", [])
    if not filters:
        return False, "No filters found in state."

    for f in filters:
        criteria = f.get("criteria", {})
        from_field = criteria.get("from", "")
        if "morningbrew" in from_field.lower():
            actions = f.get("actions", {})
            errors = []

            if actions.get("markRead") is not True:
                errors.append(
                    f"actions.markRead is {actions.get('markRead')}, expected True"
                )

            label = actions.get("label", "")
            if label != "label_6":
                errors.append(
                    f"actions.label is '{label}', expected 'label_6' (Newsletters)"
                )

            if errors:
                return False, (
                    f"Filter with from containing 'morningbrew': {'; '.join(errors)}."
                )

            return True, "Task completed successfully."

    return False, "No filter found with criteria.from containing 'morningbrew'."
