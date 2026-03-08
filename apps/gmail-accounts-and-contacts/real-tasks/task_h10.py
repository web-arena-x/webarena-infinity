# Task: Create 'Tech' label, add to companies with 'Tech' in name.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()
    errors = []

    contact_labels = state.get("contactLabels", [])
    contacts = state.get("contacts", [])

    # Find the Tech label
    tech_label = None
    for lbl in contact_labels:
        if lbl.get("name") == "Tech":
            tech_label = lbl
            break

    if not tech_label:
        errors.append("'Tech' label not found in contactLabels")
        return False, "; ".join(errors)

    tech_id = tech_label.get("id")

    # Contacts that should have the Tech label
    # TechCorp: Sarah Chen, Maya Patel, Patricia Wong-Anderson
    # EdTech Academy: Aisha Mohammed
    target_contacts = {
        "Sarah Chen": None,
        "Maya Patel": None,
        "Patricia Wong-Anderson": None,
        "Aisha Mohammed": None,
    }

    for c in contacts:
        full_name = f"{c.get('firstName', '')} {c.get('lastName', '')}".strip()
        if full_name in target_contacts:
            target_contacts[full_name] = c

    for name, contact in target_contacts.items():
        if contact is None:
            errors.append(f"Contact '{name}' not found")
            continue
        if tech_id not in contact.get("labels", []):
            errors.append(f"'{name}' does not have 'Tech' label ({tech_id})")

    if errors:
        return False, "; ".join(errors)
    return True, "Tech label created and added to all contacts with 'Tech' in company name."
