"""Task H2: Create a label called 'Series B' and apply it to every Fundraising-labeled email in the inbox."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    # Find the Series B label
    labels = state.get("labels", [])
    series_b_label = None
    for label in labels:
        if label.get("name") == "Series B":
            series_b_label = label
            break

    if series_b_label is None:
        return False, "Label 'Series B' not found in state labels."

    series_b_id = series_b_label["id"]

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
        if series_b_id not in email_labels:
            failures.append(f"{eid}: missing Series B label (id={series_b_id}), has labels {email_labels}")

    if failures:
        return False, "Not all Fundraising emails have Series B label: " + "; ".join(failures)

    return True, f"Label 'Series B' (id={series_b_id}) created and applied to all 5 Fundraising inbox emails."
