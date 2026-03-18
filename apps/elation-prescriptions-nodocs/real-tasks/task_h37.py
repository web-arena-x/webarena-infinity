import requests


def verify(server_url: str) -> tuple[bool, str]:
    """All prior-auth prescriptions across all patients renewed with 5."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # All active prescriptions with prior auth:
    # rx_014 (Margaret, Apixaban), rx_023 (William, Insulin Glargine),
    # rx_027 (Robert, Empagliflozin), rx_030 (Margaret, Semaglutide)
    pa_rxs = {
        "rx_014": "Apixaban",
        "rx_023": "Insulin Glargine",
        "rx_027": "Empagliflozin",
        "rx_030": "Semaglutide",
    }

    for rx_id, name in pa_rxs.items():
        rx = next((r for r in state["prescriptions"] if r["id"] == rx_id), None)
        if not rx:
            errors.append(f"Prescription {rx_id} ({name}) not found.")
        elif rx.get("refillsRemaining", 0) < 5:
            errors.append(f"Expected {rx_id} ({name}) refillsRemaining >= 5, got {rx.get('refillsRemaining')}.")

    if errors:
        return False, " ".join(errors)
    return True, "All prior-authorization prescriptions renewed with 5 refills."
