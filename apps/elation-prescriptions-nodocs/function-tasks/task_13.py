import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    prescriptions = state.get("prescriptions", [])

    rx = next((p for p in prescriptions if p.get("id") == "rx_001"), None)

    if rx is None:
        return False, "Prescription rx_001 not found in state."

    errors = []

    if rx.get("status") != "active":
        errors.append(f"status should be 'active', got '{rx.get('status')}'")

    if rx.get("refillsRemaining") != 5:
        errors.append(f"refillsRemaining should be 5, got {rx.get('refillsRemaining')}")

    if rx.get("refillsTotal") != 5:
        errors.append(f"refillsTotal should be 5, got {rx.get('refillsTotal')}")

    if errors:
        return False, "rx_001 (Atorvastatin) renewal has issues: " + "; ".join(errors)

    return True, "Prescription rx_001 (Atorvastatin) renewed with 5 refills."
