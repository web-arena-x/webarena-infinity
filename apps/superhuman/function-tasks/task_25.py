import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    labels = state.get("labels", [])

    target_name = "Design System"
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

    # Check for blue-ish color in the label's color settings
    color = label.get("color", {})
    bg = color.get("background", "").lower()
    text_color = color.get("text", "").lower()

    blue_indicators = ["blue", "#0000", "#1a73", "#1976", "#2196", "#42a5",
                       "#64b5", "#90ca", "#bbde", "#e3f2", "#1565", "#0d47",
                       "#1e88", "#039be5", "#0288d1", "#0277bd", "#01579b",
                       "#03a9f4", "#29b6f6", "#4fc3f7", "#81d4fa", "#b3e5fc",
                       "#e1f5fe", "#2962ff", "#2979ff", "#448aff", "#82b1ff",
                       "#3f51b5", "#1a237e", "#283593", "#303f9f", "#3949ab",
                       "#5c6bc0", "#7986cb", "#9fa8da", "#c5cae9", "#e8eaf6"]

    is_blue = any(
        indicator in bg or indicator in text_color
        for indicator in blue_indicators
    )

    if not is_blue:
        return False, (
            f"Label '{target_name}' exists but color does not appear to be blue. "
            f"Background: '{bg}', Text: '{text_color}'."
        )

    return True, (
        f"Label '{target_name}' exists with blue color "
        f"(background: '{bg}', text: '{text_color}')."
    )
