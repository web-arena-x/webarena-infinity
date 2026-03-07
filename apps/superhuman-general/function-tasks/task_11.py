import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    emails = state.get("emails", [])
    labels = state.get("labels", [])

    # Find the Engineering label by name
    engineering_label = next((l for l in labels if l["name"] == "Engineering"), None)
    if engineering_label is None:
        return False, "Could not find label 'Engineering' in state."

    email = next(
        (e for e in emails if e["subject"] == "Re: Sprint 23 Retrospective Notes"
         and e["from"]["name"] == "Nate Patel"),
        None,
    )
    if email is None:
        return False, "Could not find email 'Re: Sprint 23 Retrospective Notes' from Nate Patel."

    email_labels = email.get("labels", [])
    if engineering_label["id"] in email_labels:
        return False, f"Email 'Re: Sprint 23 Retrospective Notes' still has the 'Engineering' label. Labels: {email_labels}"

    return True, "Label 'Engineering' removed from email 'Re: Sprint 23 Retrospective Notes' from Nate Patel."
