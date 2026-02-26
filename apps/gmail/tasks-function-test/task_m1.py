import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    labels = state.get("labels", [])
    work_label = None
    for label in labels:
        if label.get("name", "").lower() == "work":
            work_label = label
            break

    if not work_label:
        return False, "Could not find label with name 'Work'."

    color = work_label.get("color", {})
    bg = color.get("background", "")
    if not bg:
        return False, f"Label 'Work' has no background color set. Current color: {color}"

    accepted_greens = [
        '#2a8547', '#4caf50', '#388e3c', '#2e7d32', '#1b5e20',
        '#43a047', '#66bb6a', '#81c784', '#a5d6a7', '#00c853',
        '#00e676', '#69f0ae', '#b9f6ca', '#008b45', '#00a550',
    ]

    bg_lower = bg.strip().lower()

    if bg_lower in [g.lower() for g in accepted_greens]:
        return True, "Task completed successfully."

    # Try parsing hex to check channel values
    hex_str = bg_lower.lstrip('#')
    if len(hex_str) == 6:
        try:
            r = int(hex_str[0:2], 16)
            g = int(hex_str[2:4], 16)
            b = int(hex_str[4:6], 16)
            if g > 100 and g > r * 1.3 and g > b * 1.3:
                return True, "Task completed successfully."
        except ValueError:
            pass

    return False, f"Label 'Work' background color is '{bg}', which is not a recognized green color."
