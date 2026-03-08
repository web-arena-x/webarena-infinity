# Task: Remove Stripe other contact.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    other_contacts = state.get("otherContacts", [])
    for contact in other_contacts:
        if contact.get("email") == "no-reply@stripe.com":
            return False, "Stripe Notifications other contact (no-reply@stripe.com) still exists."

    return True, "Stripe Notifications other contact has been removed."
