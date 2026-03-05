"""Task H8: Add the Urgent label to every unread email in the inbox that has an attachment."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    # email_001 and email_027 need label_7 added; email_125 already had it and should still have it
    check_ids = ["email_001", "email_027", "email_125"]
    emails_by_id = {e["id"]: e for e in state.get("emails", [])}

    failures = []
    for eid in check_ids:
        email = emails_by_id.get(eid)
        if email is None:
            failures.append(f"{eid}: not found in state")
            continue
        email_labels = email.get("labels", [])
        if "label_7" not in email_labels:
            failures.append(f"{eid}: missing Urgent label (label_7), has labels {email_labels}")

    if failures:
        return False, "Not all target emails have Urgent label: " + "; ".join(failures)

    return True, "Urgent label (label_7) present on email_001, email_027, and email_125."
