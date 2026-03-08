# Task: Delete Book Club and Gym Buddies labels, add Friends to affected contacts who don't have it.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()
    errors = []

    contact_labels = state.get("contactLabels", [])
    contacts = state.get("contacts", [])

    # Check labels are deleted
    for lbl in contact_labels:
        if lbl.get("id") == "clabel_8" or lbl.get("name") == "Book Club":
            errors.append("Book Club label (clabel_8) still exists")
        if lbl.get("id") == "clabel_5" or lbl.get("name") == "Gym Buddies":
            errors.append("Gym Buddies label (clabel_5) still exists")

    # Contacts who previously lacked Friends (clabel_2) should now have it:
    # Book Club: Tony Russo (had no Friends)
    # Gym Buddies: Hannah Brooks, Diana Castillo (had no Friends)
    need_friends = {
        "Tony Russo": None,
        "Hannah Brooks": None,
        "Diana Castillo": None,
    }

    for c in contacts:
        full_name = f"{c.get('firstName', '')} {c.get('lastName', '')}".strip()
        if full_name in need_friends:
            need_friends[full_name] = c

    for name, contact in need_friends.items():
        if contact is None:
            errors.append(f"Contact '{name}' not found")
            continue
        if "clabel_2" not in contact.get("labels", []):
            errors.append(f"'{name}' does not have Friends label (clabel_2)")

    if errors:
        return False, "; ".join(errors)
    return True, "Book Club and Gym Buddies labels deleted; Friends added to affected contacts."
