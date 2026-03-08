# Task: Create label 'Investors' with #FF5722 and add to Emily Rodriguez.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()
    errors = []

    contact_labels = state.get("contactLabels", [])
    label = next((l for l in contact_labels if l.get("name") == "Investors"), None)

    if label is None:
        errors.append("No label named 'Investors' found in contactLabels")
    else:
        if label.get("color") != "#FF5722":
            errors.append(f"Expected 'Investors' label color to be '#FF5722', got '{label.get('color')}'")

        label_id = label.get("id")
        contacts = state.get("contacts", [])
        emily = next(
            (c for c in contacts if c.get("firstName") == "Emily" and c.get("lastName") == "Rodriguez"),
            None,
        )
        if emily is None:
            errors.append("Contact Emily Rodriguez not found")
        else:
            if label_id not in emily.get("labels", []):
                errors.append(
                    f"Emily Rodriguez's labels {emily.get('labels', [])} do not contain "
                    f"the 'Investors' label id '{label_id}'"
                )

    if errors:
        return False, "; ".join(errors)
    return True, "Label 'Investors' created with color #FF5722 and assigned to Emily Rodriguez."
