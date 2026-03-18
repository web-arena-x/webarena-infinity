import requests


def verify(server_url: str) -> tuple[bool, str]:
    """David's Metoprolol to twice daily, William's Valsartan quantity to 60."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # rx_016 Metoprolol ER frequency -> Twice daily
    rx_016 = next((r for r in state["prescriptions"] if r["id"] == "rx_016"), None)
    if not rx_016:
        errors.append("Prescription rx_016 (Metoprolol) not found.")
    else:
        if rx_016.get("frequency") != "Twice daily":
            errors.append(f"Expected rx_016 (Metoprolol) frequency 'Twice daily', got '{rx_016.get('frequency')}'.")

    # rx_022 Valsartan quantity -> 60
    rx_022 = next((r for r in state["prescriptions"] if r["id"] == "rx_022"), None)
    if not rx_022:
        errors.append("Prescription rx_022 (Valsartan) not found.")
    else:
        if rx_022.get("quantity") != 60:
            errors.append(f"Expected rx_022 (Valsartan) quantity 60, got {rx_022.get('quantity')}.")

    if errors:
        return False, " ".join(errors)
    return True, "David's Metoprolol changed to twice daily and William's Valsartan quantity updated to 60."
