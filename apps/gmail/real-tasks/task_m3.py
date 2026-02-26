"""
Task M3: Move Emily Rodriguez's VC meetup email to the Social category.
Find email id=30, check category='social' AND 'CATEGORY_SOCIAL' in labels AND 'CATEGORY_PRIMARY' not in labels.
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    response = requests.get(f"{server_url}/api/state")
    if response.status_code != 200:
        return False, f"Failed to fetch state: HTTP {response.status_code}"

    state = response.json()
    emails = state.get("emails", [])

    target_email = None
    for email in emails:
        if email.get("id") == 30:
            target_email = email
            break

    if target_email is None:
        return False, "Email id=30 (VC Meetup Next Thursday) not found."

    category = target_email.get("category", "")
    labels = target_email.get("labels", [])
    errors = []

    if category != "social":
        errors.append(f"category is '{category}', expected 'social'")
    if "CATEGORY_SOCIAL" not in labels:
        errors.append("'CATEGORY_SOCIAL' not in labels")
    if "CATEGORY_PRIMARY" in labels:
        errors.append("'CATEGORY_PRIMARY' still in labels")

    if errors:
        return False, f"Email 30 not correctly moved to Social: {'; '.join(errors)}. Current labels: {labels}"

    return True, "Email 30 has been moved to the Social category."
