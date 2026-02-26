import requests
import re


def _is_purple_hex(hex_color: str) -> bool:
    """Check if a hex color is purple: R and B are both > 100, G < R and G < B."""
    match = re.match(r'^#([0-9a-fA-F]{6})$', hex_color)
    if not match:
        return False
    r = int(match.group(1)[0:2], 16)
    g = int(match.group(1)[2:4], 16)
    b = int(match.group(1)[4:6], 16)
    return r > 100 and b > 100 and g < r and g < b


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    labels = state.get("labels", [])
    emails = state.get("emails", [])

    # Find 'Review Needed' label
    review_label = None
    for label in labels:
        if label.get("name") == "Review Needed":
            review_label = label
            break

    if not review_label:
        return False, "No label with name 'Review Needed' found."

    color = review_label.get("color", {})
    bg = (color.get("background") or "").lower()

    accepted_purples = [
        '#7e57c2', '#9c27b0', '#7b1fa2', '#6a1b9a', '#4a148c',
        '#ab47bc', '#ba68c8', '#ce93d8', '#aa00ff', '#d500f9',
        '#e040fb', '#ea80fc',
    ]

    if bg not in accepted_purples and not _is_purple_hex(bg):
        return False, f"Review Needed label background color '{bg}' is not a recognized purple color."

    review_label_id = review_label.get("id")

    # Check the three target emails
    target_subjects = [
        "Code Review Request: auth-service PR #42",
        "Brand Refresh Concepts",
        "CI/CD Pipeline Migration Plan",
    ]

    for subject in target_subjects:
        target_email = None
        for email in emails:
            if email.get("subject") == subject:
                target_email = email
                break

        if not target_email:
            return False, f"No email found with subject '{subject}'."

        email_labels = target_email.get("labels", [])
        if review_label_id not in email_labels:
            return False, f"Email '{subject}' does not have Review Needed label ('{review_label_id}') in its labels: {email_labels}"

    return True, "Task completed successfully."
