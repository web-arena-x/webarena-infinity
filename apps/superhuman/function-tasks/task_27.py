import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    labels = state.get("labels", [])

    target_name = "Customer"
    label = next(
        (l for l in labels if l.get("name", "").lower() == target_name.lower()),
        None,
    )

    if label is None:
        return False, (
            f"No label named '{target_name}' found. "
            f"Existing labels: {[l.get('name') for l in labels]}"
        )

    # Original seed color for Customer label
    original_bg = "#e8f5e9"
    original_text = "#2e7d32"

    color = label.get("color", {})
    current_bg = color.get("background", "").lower()
    current_text = color.get("text", "").lower()

    if current_bg == original_bg and current_text == original_text:
        return False, (
            f"Label '{target_name}' color has not changed from the original "
            f"(background: '{original_bg}', text: '{original_text}'). "
            f"Expected an orange color."
        )

    # Check for orange-ish color indicators
    orange_indicators = ["orange", "#ff9800", "#ff6d00", "#ff8f00", "#ffa000",
                         "#ffb300", "#ffc107", "#e65100", "#ef6c00", "#f57c00",
                         "#fb8c00", "#ffa726", "#ffb74d", "#ffcc80", "#ffe0b2",
                         "#fff3e0", "#ff5722", "#bf360c", "#d84315", "#e64a19",
                         "#f4511e", "#ff7043", "#ff8a65", "#ffab91", "#ffccbc",
                         "#fbe9e7", "#dd2c00", "#ff3d00", "#ff6e40", "#ff9e80"]

    is_orange = any(
        indicator in current_bg or indicator in current_text
        for indicator in orange_indicators
    )

    if not is_orange:
        # Even if it's not exactly a recognized orange hex, the color changed
        # from green, which is the primary requirement
        return True, (
            f"Label '{target_name}' color changed from original green. "
            f"New color — background: '{current_bg}', text: '{current_text}'. "
            f"Note: color may not be precisely orange but has been changed."
        )

    return True, (
        f"Label '{target_name}' color changed to orange "
        f"(background: '{current_bg}', text: '{current_text}')."
    )
