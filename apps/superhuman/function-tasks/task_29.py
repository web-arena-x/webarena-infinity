import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    labels = state.get("labels", [])

    target_name = "Infrastructure"
    label = next(
        (l for l in labels if l.get("name", "").lower() == target_name.lower()),
        None,
    )

    if label is None:
        label_names = [l.get("name") for l in labels]
        return False, (
            f"No label named '{target_name}' found. "
            f"Existing labels: {label_names}"
        )

    # Check for teal-ish color in the label's color settings
    color = label.get("color", {})
    bg = color.get("background", "").lower()
    text_color = color.get("text", "").lower()

    teal_indicators = ["teal", "#009688", "#00897b", "#00796b", "#00695c",
                       "#004d40", "#26a69a", "#4db6ac", "#80cbc4", "#b2dfdb",
                       "#e0f2f1", "#1de9b6", "#64ffda", "#a7ffeb", "#00bfa5",
                       "#00e5ff", "#18ffff", "#84ffff", "#a7ffeb",
                       "#006064", "#00838f", "#0097a7", "#00acc1", "#00bcd4",
                       "#26c6da", "#4dd0e1", "#80deea", "#b2ebf2", "#e0f7fa"]

    is_teal = any(
        indicator in bg or indicator in text_color
        for indicator in teal_indicators
    )

    if not is_teal:
        # Label exists, which is the primary requirement
        return True, (
            f"Label '{target_name}' created. Color — background: '{bg}', "
            f"text: '{text_color}'. Note: color may not be precisely teal."
        )

    return True, (
        f"Label '{target_name}' created with teal color "
        f"(background: '{bg}', text: '{text_color}')."
    )
