import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Update billing addresses for all Wellington-based contacts to use postal code 6012 instead of 6011."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    contacts = state.get("contacts", [])

    # Wellington contacts that originally had postalCode '6011'
    target_contacts = {
        "con_4": "Nexus Technologies Ltd",
        "con_13": "Harmony Music Academy",
        "con_18": "Apex Legal Partners",
    }

    errors = []

    for con_id, name in target_contacts.items():
        contact = None
        for c in contacts:
            if c.get("id") == con_id:
                contact = c
                break

        if contact is None:
            errors.append(f"Contact {name} ({con_id}) not found in state")
            continue

        billing_address = contact.get("billingAddress", {})
        postal_code = billing_address.get("postalCode")

        if str(postal_code) != "6012":
            errors.append(
                f"{name} ({con_id}) has billingAddress.postalCode='{postal_code}', expected '6012'"
            )

    if errors:
        return False, "; ".join(errors)

    return True, "All 3 Wellington contacts (con_4, con_13, con_18) updated to postal code 6012"
