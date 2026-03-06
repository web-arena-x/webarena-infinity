import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Check customSigs for the exact text
    custom_sigs = state.get("customSigs", [])
    target_text = "Apply to affected area three times daily"
    matching_sig = None
    for sig in custom_sigs:
        if sig.get("text") == target_text:
            matching_sig = sig
            break

    if matching_sig is None:
        return False, f"Custom sig with text '{target_text}' not found in customSigs"

    # Check category is topical
    category = matching_sig.get("category", "")
    if category != "topical":
        return False, f"Custom sig category is '{category}', expected 'topical'"

    return True, "Custom sig 'Apply to affected area three times daily' added in topical category"
