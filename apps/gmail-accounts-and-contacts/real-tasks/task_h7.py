# Task: Delete auto-saved contacts with no-reply/do-not-reply emails.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()
    errors = []

    other_contacts = state.get("otherContacts", [])

    noreply_emails = {
        "no-reply@stripe.com",
        "noreply@github.com",
        "do-not-reply@zoom.us",
        "no-reply@docusign.net",
    }

    for oc in other_contacts:
        email = oc.get("email", "")
        if email in noreply_emails:
            errors.append(
                f"Other contact with no-reply email '{email}' still exists"
            )

    if errors:
        return False, "; ".join(errors)
    return True, "All auto-saved contacts with no-reply/do-not-reply emails deleted."
