import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    sigs = state.get("customSigs", [])

    target_text = "Apply 1 patch to skin every 72 hours"
    match = [
        s for s in sigs
        if s.get("text") == target_text and s.get("category") == "topical"
    ]

    if not match:
        text_match = [s for s in sigs if s.get("text") == target_text]
        if text_match:
            actual_cat = text_match[0].get("category")
            return False, f"Custom sig '{target_text}' exists but category is '{actual_cat}', expected 'topical'."
        return False, f"No custom sig found with text='{target_text}'."

    return True, f"Custom sig '{target_text}' exists with category='topical'."
