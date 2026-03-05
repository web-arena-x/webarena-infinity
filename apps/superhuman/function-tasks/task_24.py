import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    emails = state.get("emails", [])

    email = next((e for e in emails if e.get("id") == "email_103"), None)

    if email is None:
        return False, "Could not find email with id 'email_103'."

    errors = []

    if email.get("isDraft") is not True:
        errors.append(
            f"isDraft is {email.get('isDraft')}, expected True."
        )

    if email.get("isScheduled") is not False:
        errors.append(
            f"isScheduled is {email.get('isScheduled')}, expected False."
        )

    if email.get("folder") != "drafts":
        errors.append(
            f"folder is '{email.get('folder')}', expected 'drafts'."
        )

    if errors:
        return False, (
            f"Email 'email_103' not correctly cancelled. " + " ".join(errors)
        )

    return True, (
        "Scheduled email 'TechCorp + FusionLabs — KubeCon Europe proposal' "
        "has been cancelled and moved to drafts."
    )
