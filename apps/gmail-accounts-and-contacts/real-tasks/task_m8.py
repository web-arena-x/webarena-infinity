# Task: Create label 'Project Alpha' and assign to Sarah Chen.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()
    errors = []

    contact_labels = state.get("contactLabels", [])
    label = next((l for l in contact_labels if l.get("name") == "Project Alpha"), None)

    if label is None:
        errors.append("No label named 'Project Alpha' found in contactLabels")
    else:
        label_id = label.get("id")

        contacts = state.get("contacts", [])
        sarah = next(
            (c for c in contacts if c.get("firstName") == "Sarah" and c.get("lastName") == "Chen"),
            None,
        )
        if sarah is None:
            errors.append("Contact Sarah Chen not found")
        else:
            if label_id not in sarah.get("labels", []):
                errors.append(
                    f"Sarah Chen's labels {sarah.get('labels', [])} do not contain "
                    f"the 'Project Alpha' label id '{label_id}'"
                )

    if errors:
        return False, "; ".join(errors)
    return True, "Label 'Project Alpha' created and assigned to Sarah Chen."
