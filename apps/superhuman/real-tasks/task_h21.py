"""Task H21: Archive the email from the customer who's been stuck on a data export issue for two weeks."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    emails_by_id = {e["id"]: e for e in state.get("emails", [])}
    email = emails_by_id.get("email_009")

    if email is None:
        return False, "email_009 not found in state."

    if email.get("folder") != "done":
        return False, f"email_009 folder is '{email.get('folder')}', expected 'done'."

    return True, "email_009 (Monica Estrada's data export complaint) archived to Done."
