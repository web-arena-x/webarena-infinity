import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find prescription rx_014
    prescriptions = state.get("prescriptions", [])
    rx = next((p for p in prescriptions if p.get("id") == "rx_014"), None)
    if rx is None:
        return False, "Prescription 'rx_014' not found in state."

    # Check sig contains 'twice daily with food'
    sig = rx.get("sig", "")
    if "twice daily with food" not in sig:
        return False, f"Prescription rx_014 sig is '{sig}', expected it to contain 'twice daily with food'."

    return True, "Prescription rx_014 (Apixaban) sig updated to contain 'twice daily with food'."
