import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    sigs = state.get("customSigs", [])

    target_text = "Instill 1 drop in affected eye(s) twice daily"
    match = [s for s in sigs if s.get("text") == target_text]

    if match:
        return False, f"Custom sig with text='{target_text}' still exists. Expected it to be deleted."

    return True, f"Custom sig '{target_text}' was successfully deleted."
