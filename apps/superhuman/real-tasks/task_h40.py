"""Task H40: Move the SREcon talk acceptance email from Done back to inbox and apply Engineering label."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    # email_076 = SREcon 2026 talk acceptance in Done folder
    emails_by_id = {e["id"]: e for e in state.get("emails", [])}
    email = emails_by_id.get("email_076")

    if email is None:
        return False, "email_076 not found in state."

    failures = []

    if email.get("folder") != "inbox":
        failures.append(f"folder is '{email.get('folder')}', expected 'inbox'")

    email_labels = email.get("labels", [])
    if "label_10" not in email_labels:
        failures.append(f"missing Engineering label (label_10), has labels {email_labels}")

    if failures:
        return False, "email_076 checks failed: " + "; ".join(failures)

    return True, "email_076 (SREcon talk acceptance) moved to inbox with Engineering label."
