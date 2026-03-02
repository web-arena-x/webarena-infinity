import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    sigs = state.get("customSigs", [])

    target_text = "Take 2 capsules by mouth once daily with breakfast"
    match = [
        s for s in sigs
        if s.get("text") == target_text and s.get("category") == "oral"
    ]

    if not match:
        # Check if sig exists but with wrong category
        text_match = [s for s in sigs if s.get("text") == target_text]
        if text_match:
            actual_cat = text_match[0].get("category")
            return False, f"Custom sig '{target_text}' exists but category is '{actual_cat}', expected 'oral'."
        return False, f"No custom sig found with text='{target_text}'."

    return True, f"Custom sig '{target_text}' exists with category='oral'."
