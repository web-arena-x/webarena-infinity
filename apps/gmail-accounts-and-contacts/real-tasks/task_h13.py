# Task: EuroDesign contacts: remove Work, add VIP Clients.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()
    errors = []

    contacts = state.get("contacts", [])

    # EuroDesign contacts: Sophie Laurent (contact_15), Elena Volkov (contact_37)
    target_contacts = {
        "Sophie Laurent": None,
        "Elena Volkov": None,
    }

    for c in contacts:
        full_name = f"{c.get('firstName', '')} {c.get('lastName', '')}".strip()
        if full_name in target_contacts:
            target_contacts[full_name] = c

    for name, contact in target_contacts.items():
        if contact is None:
            errors.append(f"Contact '{name}' not found")
            continue

        labels = contact.get("labels", [])

        # Should have clabel_4 (VIP Clients)
        if "clabel_4" not in labels:
            errors.append(f"'{name}' missing VIP Clients label (clabel_4)")

        # Should NOT have clabel_3 (Work)
        if "clabel_3" in labels:
            errors.append(f"'{name}' still has Work label (clabel_3)")

    if errors:
        return False, "; ".join(errors)
    return True, "EuroDesign contacts updated: Work removed, VIP Clients added."
