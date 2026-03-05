"""Task H10: Create a label 'Investor Relations' and apply to all Fundraising-labeled inbox emails."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    # Find the Investor Relations label
    labels = state.get("labels", [])
    ir_label = None
    for label in labels:
        if label.get("name") == "Investor Relations":
            ir_label = label
            break

    if ir_label is None:
        return False, "Label 'Investor Relations' not found in state labels."

    ir_id = ir_label["id"]

    # Check target emails have the new label
    target_ids = ["email_002", "email_023", "email_026", "email_119", "email_120"]
    emails_by_id = {e["id"]: e for e in state.get("emails", [])}

    failures = []
    for eid in target_ids:
        email = emails_by_id.get(eid)
        if email is None:
            failures.append(f"{eid}: not found in state")
            continue
        email_labels = email.get("labels", [])
        if ir_id not in email_labels:
            failures.append(f"{eid}: missing Investor Relations label (id={ir_id}), has labels {email_labels}")

    if failures:
        return False, "Not all Fundraising emails have Investor Relations label: " + "; ".join(failures)

    return True, f"Label 'Investor Relations' (id={ir_id}) created and applied to all 5 Fundraising inbox emails."
