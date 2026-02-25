import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    RED_BACKGROUNDS = [
        "#cc3333", "#dc3545", "#ff0000", "#e53935", "#d32f2f",
        "#c62828", "#b71c1c", "#f44336", "#e57373", "#ef5350",
        "#ef9a9a", "#ffcdd2", "#ffebee", "#ff1744", "#ff5252",
        "#ff8a80", "#e53e3e", "#fc5c65", "#eb3b5a", "#ee5a24",
        "#ac725e", "#d06b64", "#f83a22", "#fa573c", "#ff7537",
        "#cc3a21",
    ]

    labels = state.get("labels", [])
    for label in labels:
        if label.get("name") == "Urgent":
            color = label.get("color")
            if color is None:
                return False, "Label 'Urgent' found but has no color set."
            bg = (color.get("background") or "").lower()
            if bg in [c.lower() for c in RED_BACKGROUNDS]:
                return True, "Task completed successfully."
            # Also accept any hex color that is predominantly red
            if bg.startswith("#") and len(bg) == 7:
                try:
                    r = int(bg[1:3], 16)
                    g = int(bg[3:5], 16)
                    b = int(bg[5:7], 16)
                    if r > 150 and r > g * 1.5 and r > b * 1.5:
                        return True, "Task completed successfully."
                except ValueError:
                    pass
            return False, f"Label 'Urgent' found but color background is '{bg}', expected a red color."

    return False, "Label with name 'Urgent' not found."
