import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Check custom sig "Take 2 tablets by mouth once daily" has been deleted
    custom_sigs = state.get("customSigs", [])
    target_text = "Take 2 tablets by mouth once daily"

    for sig in custom_sigs:
        if sig.get("text") == target_text:
            return False, f"Custom sig '{target_text}' still present in customSigs"

    if len(custom_sigs) != 23:
        return False, f"Expected 23 custom sigs after deletion, found {len(custom_sigs)}"

    return True, "Custom sig 'Take 2 tablets by mouth once daily' deleted successfully; 23 sigs remain"
