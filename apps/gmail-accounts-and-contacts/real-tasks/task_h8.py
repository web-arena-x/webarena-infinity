# Task: Delete Vendor contacts and delete Vendors label.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()
    errors = []

    contacts = state.get("contacts", [])
    contact_labels = state.get("contactLabels", [])

    # Check no contact has clabel_9 in labels
    for c in contacts:
        if "clabel_9" in c.get("labels", []):
            name = f"{c.get('firstName', '')} {c.get('lastName', '')}".strip()
            errors.append(f"Contact '{name}' still has Vendors label (clabel_9)")

    # Check no contactLabel with name 'Vendors' or id 'clabel_9'
    for lbl in contact_labels:
        if lbl.get("name") == "Vendors" or lbl.get("id") == "clabel_9":
            errors.append(f"Vendors label still exists in contactLabels (id={lbl.get('id')})")

    # Check specific vendor contacts are gone
    vendor_names = {
        "James O'Brien",
        "Tom Bradley",
        "Carlos Mendez",
        "Daniel Thompson",
        "Greg Hoffman",
    }
    for c in contacts:
        full_name = f"{c.get('firstName', '')} {c.get('lastName', '')}".strip()
        if full_name in vendor_names:
            errors.append(f"Vendor contact '{full_name}' still exists")

    if errors:
        return False, "; ".join(errors)
    return True, "All Vendor contacts deleted and Vendors label removed."
