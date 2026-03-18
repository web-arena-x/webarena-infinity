import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    contact_groups = state.get("contactGroups", [])

    for group in contact_groups:
        if group.get("name") == "Mentors":
            return True, (
                "Contact label 'Mentors' has been successfully created."
            )

    group_names = [g.get("name", "") for g in contact_groups]
    return False, (
        f"No contact label named 'Mentors' found in contactGroups. "
        f"Existing labels: {group_names}."
    )
