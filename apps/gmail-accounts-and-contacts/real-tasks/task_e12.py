# Task: Remove AWS Billing other contact.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    other_contacts = state.get("otherContacts", [])
    for contact in other_contacts:
        if contact.get("email") == "billing@aws.amazon.com":
            return False, "AWS Billing other contact (billing@aws.amazon.com) still exists."

    return True, "AWS Billing other contact has been removed."
