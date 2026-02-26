import requests
import re


def _is_orange_hex(hex_color: str) -> bool:
    """Check if a hex color is orange: R > 150, G > 80, G < R, B < 80."""
    match = re.match(r'^#([0-9a-fA-F]{6})$', hex_color)
    if not match:
        return False
    r = int(match.group(1)[0:2], 16)
    g = int(match.group(1)[2:4], 16)
    b = int(match.group(1)[4:6], 16)
    return r > 150 and g > 80 and g < r and b < 80


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    labels = state.get("labels", [])
    emails = state.get("emails", [])

    # Find 'DevReports' label
    dev_label = None
    for label in labels:
        if label.get("name") == "DevReports":
            dev_label = label
            break

    if not dev_label:
        return False, "No label with name 'DevReports' found."

    color = dev_label.get("color", {})
    bg = (color.get("background") or "").lower()

    accepted_oranges = [
        '#e37400', '#ff9800', '#f57c00', '#ef6c00', '#e65100',
        '#fb8c00', '#ffa726', '#ffb74d', '#ff6d00', '#ff9100',
    ]

    if bg not in accepted_oranges and not _is_orange_hex(bg):
        return False, f"DevReports label background color '{bg}' is not a recognized orange color."

    dev_label_id = dev_label.get("id")

    # Find email with subject 'Deployment successful: production'
    email_deploy = None
    for email in emails:
        if email.get("subject") == "Deployment successful: production":
            email_deploy = email
            break

    if not email_deploy:
        return False, "No email found with subject 'Deployment successful: production'."

    if dev_label_id not in email_deploy.get("labels", []):
        return False, f"Email 'Deployment successful: production' does not have DevReports label ('{dev_label_id}') in its labels: {email_deploy.get('labels', [])}"

    # Find email with subject 'Alert: High CPU usage on prod-api-3'
    email_alert = None
    for email in emails:
        if email.get("subject") == "Alert: High CPU usage on prod-api-3":
            email_alert = email
            break

    if not email_alert:
        return False, "No email found with subject 'Alert: High CPU usage on prod-api-3'."

    if dev_label_id not in email_alert.get("labels", []):
        return False, f"Email 'Alert: High CPU usage on prod-api-3' does not have DevReports label ('{dev_label_id}') in its labels: {email_alert.get('labels', [])}"

    return True, "Task completed successfully."
