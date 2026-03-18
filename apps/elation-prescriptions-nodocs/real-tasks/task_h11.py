import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    prescriptions = state.get("prescriptions", [])
    errors = []

    # Active prescriptions for pat_001 with originally < 3 refills remaining:
    # rx_001 (Atorvastatin): 2 remaining
    # rx_005 (Pantoprazole): 1 remaining
    # rx_006 (Albuterol): 2 remaining
    # rx_008 (Flonase): 2 remaining
    target_ids = ["rx_001", "rx_005", "rx_006", "rx_008"]

    for rx_id in target_ids:
        rx = None
        for r in prescriptions:
            if r.get("id") == rx_id:
                rx = r
                break
        if rx is None:
            errors.append(f"Prescription {rx_id} not found.")
        elif rx.get("refillsRemaining") != 5:
            errors.append(f"Expected {rx_id} ({rx.get('drugName', '?')}) refillsRemaining 5, got {rx.get('refillsRemaining')}.")

    if errors:
        return False, " ".join(errors)

    return True, "All prescriptions with fewer than 3 refills renewed with 5 refills."
