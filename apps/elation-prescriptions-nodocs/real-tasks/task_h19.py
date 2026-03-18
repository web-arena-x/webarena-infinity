import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Renew Margaret's rxs: 1 remaining -> 5 refills, 2 remaining -> 3 refills."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # Originally 1 refill remaining: rx_005 Pantoprazole -> now 5
    rx_005 = next((r for r in state["prescriptions"] if r["id"] == "rx_005"), None)
    if not rx_005:
        errors.append("Prescription rx_005 (Pantoprazole) not found.")
    elif rx_005.get("refillsRemaining") != 5:
        errors.append(f"Expected rx_005 (Pantoprazole, had 1 refill) refillsRemaining 5, got {rx_005.get('refillsRemaining')}.")

    # Originally 2 refills remaining: rx_001, rx_006, rx_008 -> now 3
    for rx_id, name in [("rx_001", "Atorvastatin"), ("rx_006", "Albuterol"), ("rx_008", "Flonase")]:
        rx = next((r for r in state["prescriptions"] if r["id"] == rx_id), None)
        if not rx:
            errors.append(f"Prescription {rx_id} ({name}) not found.")
        elif rx.get("refillsRemaining") != 3:
            errors.append(f"Expected {rx_id} ({name}, had 2 refills) refillsRemaining 3, got {rx.get('refillsRemaining')}.")

    if errors:
        return False, " ".join(errors)
    return True, "All qualifying prescriptions renewed based on refill thresholds."
