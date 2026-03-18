import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Change the billing city for Oceanview Resort & Spa to Takapuna."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    contacts = state.get("contacts", [])
    target = None
    for contact in contacts:
        if contact.get("name") == "Oceanview Resort & Spa":
            target = contact
            break

    if target is None:
        return False, "Contact 'Oceanview Resort & Spa' not found in state"

    billing = target.get("billingAddress", {})
    city = billing.get("city")

    if city == "Takapuna":
        return True, "Billing city for 'Oceanview Resort & Spa' is 'Takapuna'"
    else:
        return False, f"Billing city for 'Oceanview Resort & Spa' is '{city}', expected 'Takapuna'"
