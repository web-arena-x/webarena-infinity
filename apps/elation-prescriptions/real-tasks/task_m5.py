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
    target_text = "Take 2 capsules by mouth once daily with food"
    matching_sig = None
    for sig in custom_sigs:
        if sig.get("text") == target_text:
            matching_sig = sig
            break

    if matching_sig is None:
        return False, f"Custom sig with text '{target_text}' not found in customSigs"

    # Check category is oral
    category = matching_sig.get("category", "")
    if category != "oral":
        return False, f"Custom sig category is '{category}', expected 'oral'"

    return True, "Custom sig 'Take 2 capsules by mouth once daily with food' added in oral category"
