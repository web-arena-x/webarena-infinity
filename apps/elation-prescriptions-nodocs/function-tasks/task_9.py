import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    prescriptions = state.get("prescriptions", [])

    rx = next((p for p in prescriptions if p.get("id") == "rx_005"), None)

    if rx is None:
        return False, "Prescription rx_005 not found in state."

    if rx.get("status") != "discontinued":
        return False, f"rx_005 status should be 'discontinued', got '{rx.get('status')}'."

    reason = rx.get("discontinuedReason", "")
    if "no longer clinically indicated" not in reason.lower():
        return False, f"rx_005 discontinuedReason should contain 'No longer clinically indicated', got '{reason}'."

    return True, "Prescription rx_005 (Pantoprazole) is discontinued with correct reason."
