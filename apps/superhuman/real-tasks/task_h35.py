"""Task H35: Create 'Pending Decision' label and apply to every inbox email with a reminder."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    # Find the Pending Decision label
    labels = state.get("labels", [])
    pd_label = None
    for label in labels:
        if label.get("name") == "Pending Decision":
            pd_label = label
            break

    if pd_label is None:
        return False, "Label 'Pending Decision' not found in state labels."

    pd_id = pd_label["id"]

    # Inbox emails with reminders in seed: email_002, 003, 005, 009, 119
    target_ids = ["email_002", "email_003", "email_005", "email_009", "email_119"]
    emails_by_id = {e["id"]: e for e in state.get("emails", [])}

    failures = []
    for eid in target_ids:
        email = emails_by_id.get(eid)
        if email is None:
            failures.append(f"{eid}: not found in state")
            continue
        email_labels = email.get("labels", [])
        if pd_id not in email_labels:
            failures.append(f"{eid}: missing Pending Decision label (id={pd_id}), has labels {email_labels}")

    if failures:
        return False, "Not all reminder emails have Pending Decision label: " + "; ".join(failures)

    return True, f"Label 'Pending Decision' (id={pd_id}) created and applied to all 5 inbox emails with reminders."
