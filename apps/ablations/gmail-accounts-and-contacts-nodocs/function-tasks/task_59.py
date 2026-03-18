import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])

    for contact in contacts:
        if contact.get("firstName") == "Olivia" and contact.get("lastName") == "Grant":
            errors = []
            if not contact.get("starred"):
                errors.append("Contact is not starred")
            if "grp_10" not in contact.get("groups", []):
                errors.append("grp_10 (VIP) not found in groups")
            if "grp_7" not in contact.get("groups", []):
                errors.append("grp_7 (Book Club) should be preserved but is missing")
            if errors:
                return False, f"Olivia Grant issues: {'; '.join(errors)}. Groups: {contact.get('groups')}"
            return True, "Olivia Grant is starred and in VIP label (Book Club preserved)."

    return False, "No contact found with firstName 'Olivia' and lastName 'Grant'."
