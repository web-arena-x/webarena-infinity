import requests
import re


def _is_blue_hex(hex_color: str) -> bool:
    """Check if a hex color is blue: B > 150, B > R*1.3, B > G*1.3."""
    match = re.match(r'^#([0-9a-fA-F]{6})$', hex_color)
    if not match:
        return False
    r = int(match.group(1)[0:2], 16)
    g = int(match.group(1)[2:4], 16)
    b = int(match.group(1)[4:6], 16)
    return b > 150 and b > r * 1.3 and b > g * 1.3


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    labels = state.get("labels", [])
    emails = state.get("emails", [])

    # Find 'Cloud' label
    cloud_label = None
    for label in labels:
        if label.get("name") == "Cloud":
            cloud_label = label
            break

    if not cloud_label:
        return False, "No label with name 'Cloud' found."

    if cloud_label.get("parentId") != "label_1":
        return False, f"Cloud label parentId is '{cloud_label.get('parentId')}', expected 'label_1'."

    color = cloud_label.get("color", {})
    bg = (color.get("background") or "").lower()

    accepted_blues = [
        '#2962ff', '#1a73e8', '#2196f3', '#1565c0', '#0d47a1',
        '#42a5f5', '#64b5f6', '#1e88e5', '#1976d2', '#0277bd',
    ]

    if bg not in accepted_blues and not _is_blue_hex(bg):
        return False, f"Cloud label background color '{bg}' is not a recognized blue color."

    cloud_label_id = cloud_label.get("id")

    # Find email with subject 'Re: API Integration Issue' from someone with 'priya' in the from
    target_email = None
    for email in emails:
        subject = email.get("subject", "")
        from_field = email.get("from") or {}
        from_email = (from_field.get("email", "") if isinstance(from_field, dict) else str(from_field)).lower()
        if subject == "Re: API Integration Issue" and "priya" in from_email:
            target_email = email
            break

    if not target_email:
        return False, "No email found with subject 'Re: API Integration Issue' from someone with 'priya' in the from."

    email_labels = target_email.get("labels", [])
    if cloud_label_id not in email_labels:
        return False, f"Email 'Re: API Integration Issue' does not have the Cloud label ('{cloud_label_id}') in its labels: {email_labels}"

    return True, "Task completed successfully."
