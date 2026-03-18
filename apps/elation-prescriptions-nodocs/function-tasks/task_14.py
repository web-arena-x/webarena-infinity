import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    prescriptions = state.get("prescriptions", [])

    rx = next((p for p in prescriptions if p.get("id") == "rx_007"), None)

    if rx is None:
        return False, "Prescription rx_007 not found in state."

    errors = []

    if rx.get("status") != "active":
        errors.append(f"status should be 'active', got '{rx.get('status')}'")

    if rx.get("refillsRemaining") != 3:
        errors.append(f"refillsRemaining should be 3, got {rx.get('refillsRemaining')}")

    if rx.get("refillsTotal") != 3:
        errors.append(f"refillsTotal should be 3, got {rx.get('refillsTotal')}")

    if errors:
        return False, "rx_007 (Gabapentin) renewal has issues: " + "; ".join(errors)

    return True, "Prescription rx_007 (Gabapentin) renewed with 3 refills."
