"""Mark Marcus Williams' Design System Update as read, star it with a blue star, and apply the Projects label."""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    response = requests.get(f"{server_url}/api/state")
    if response.status_code != 200:
        return False, f"Failed to fetch state: HTTP {response.status_code}"

    state = response.json()
    emails = state.get("emails", [])

    email = next((e for e in emails if e["id"] == 6), None)
    if email is None:
        return False, "Email 6 ('Design System Update v4.2') not found in state"

    errors = []

    if not email.get("isRead", False):
        errors.append("Email is not marked as read")

    if not email.get("isStarred", False):
        errors.append("Email is not starred")

    star_type = email.get("starType", "")
    if star_type != "blue-star":
        errors.append(f"Star type is '{star_type}', expected 'blue-star'")

    labels = email.get("labels", [])
    if "label_9" not in labels:
        errors.append(
            f"Email does not have 'label_9' (Projects) in labels: {labels}"
        )

    if errors:
        return False, "; ".join(errors)

    return True, "Email 6 is read, has blue star, and Projects label applied."
