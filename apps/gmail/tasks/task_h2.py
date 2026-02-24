import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    TEAL_BACKGROUNDS = [
        "#076570", "#0d7377", "#149e60", "#16a765", "#2da2bb",
        "#42d692", "#44b984", "#4986e7", "#00897b", "#009688",
        "#00796b", "#00695c", "#004d40", "#26a69a", "#4db6ac",
        "#80cbc4", "#b2dfdb", "#e0f2f1", "#1de9b6", "#64ffda",
        "#a7ffeb", "#00bcd4", "#0097a7", "#00838f", "#006064",
        "#26c6da", "#4dd0e1", "#80deea", "#b2ebf2", "#e0f7fa",
        "#18ffff", "#84ffff",
    ]

    labels = state.get("labels", [])
    devops_label = None
    for label in labels:
        if label.get("name") == "DevOps":
            devops_label = label
            break

    if devops_label is None:
        return False, "Label 'DevOps' not found."

    if devops_label.get("parentId") != "label_1":
        return False, f"Label 'DevOps' has parentId='{devops_label.get('parentId')}', expected 'label_1' (Work)."

    color = devops_label.get("color")
    if color is None:
        return False, "Label 'DevOps' has no color set."

    bg = (color.get("background") or "").lower()
    is_teal = bg in [c.lower() for c in TEAL_BACKGROUNDS]

    if not is_teal and bg.startswith("#") and len(bg) == 7:
        try:
            r = int(bg[1:3], 16)
            g = int(bg[3:5], 16)
            b = int(bg[5:7], 16)
            if (g > r and b > r) or (g > 100 and b > 100 and r < g):
                is_teal = True
        except ValueError:
            pass

    if not is_teal:
        return False, f"Label 'DevOps' color background is '{bg}', expected a teal color."

    devops_label_id = devops_label.get("id")

    for email in state.get("emails", []):
        if email.get("subject") == "CI/CD Pipeline Migration Plan":
            email_labels = email.get("labels", [])
            if devops_label_id in email_labels:
                return True, "Task completed successfully."
            else:
                return False, f"Email 'CI/CD Pipeline Migration Plan' does not have DevOps label ('{devops_label_id}') in its labels: {email_labels}."

    return False, "Email with subject 'CI/CD Pipeline Migration Plan' not found."
