import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    sigs = state.get("customSigs", [])

    old_text = "Dissolve 1 tablet under the tongue as needed"
    new_text = "Dissolve 1 tablet under the tongue every 5 minutes as needed, max 3 doses"

    old_match = [s for s in sigs if s.get("text") == old_text]
    if old_match:
        return False, f"Old sig text '{old_text}' still exists. Expected it to be replaced."

    new_match = [
        s for s in sigs
        if s.get("text") == new_text and s.get("category") == "sublingual"
    ]

    if not new_match:
        text_match = [s for s in sigs if s.get("text") == new_text]
        if text_match:
            actual_cat = text_match[0].get("category")
            return False, f"New sig text found but category is '{actual_cat}', expected 'sublingual'."
        return False, f"No custom sig found with text='{new_text}'."

    return True, f"Sublingual sig updated to '{new_text}' with category='sublingual'."
