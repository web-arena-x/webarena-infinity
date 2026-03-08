# Task: Create 'Collaborators' label and add to CloudNine/DesignHub contacts.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()
    errors = []

    contact_labels = state.get("contactLabels", [])
    contacts = state.get("contacts", [])

    # Find the Collaborators label
    collab_label = None
    for lbl in contact_labels:
        if lbl.get("name") == "Collaborators":
            collab_label = lbl
            break

    if not collab_label:
        errors.append("'Collaborators' label not found in contactLabels")
        return False, "; ".join(errors)

    collab_id = collab_label.get("id")

    # Check CloudNine contacts: Priya Sharma, Raj Kapoor
    # Check DesignHub contacts: Marcus Williams
    target_contacts = {
        "Priya Sharma": None,
        "Raj Kapoor": None,
        "Marcus Williams": None,
    }

    for c in contacts:
        full_name = f"{c.get('firstName', '')} {c.get('lastName', '')}".strip()
        if full_name in target_contacts:
            target_contacts[full_name] = c

    for name, contact in target_contacts.items():
        if contact is None:
            errors.append(f"Contact '{name}' not found")
            continue
        if collab_id not in contact.get("labels", []):
            errors.append(f"'{name}' does not have 'Collaborators' label ({collab_id})")

    if errors:
        return False, "; ".join(errors)
    return True, "Collaborators label created and added to all CloudNine/DesignHub contacts."
