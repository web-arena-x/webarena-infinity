import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    labels = state.get("labels", [])
    taxes_label = None
    for label in labels:
        if label.get("name", "").lower() == "taxes":
            taxes_label = label
            break

    if not taxes_label:
        return False, "Could not find label with name 'Taxes'."

    errors = []
    parent_id = taxes_label.get("parentId")
    if parent_id != "label_3":
        errors.append(f"parentId is '{parent_id}', expected 'label_3' (Finance)")

    label_type = taxes_label.get("type", "")
    if label_type != "user":
        errors.append(f"type is '{label_type}', expected 'user'")

    if errors:
        return False, f"Label 'Taxes': {'; '.join(errors)}."

    return True, "Task completed successfully."
