import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Margaret: SSRI frequency twice daily, blood thinner qty 90, deny Sertraline refill."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # rx_013 Sertraline (SSRI) frequency -> Twice daily
    rx_013 = next((r for r in state["prescriptions"] if r["id"] == "rx_013"), None)
    if not rx_013:
        errors.append("Prescription rx_013 (Sertraline) not found.")
    else:
        if rx_013.get("frequency") != "Twice daily":
            errors.append(f"Expected rx_013 (Sertraline) frequency 'Twice daily', got '{rx_013.get('frequency')}'.")

    # rx_014 Apixaban (blood thinner) quantity -> 90
    rx_014 = next((r for r in state["prescriptions"] if r["id"] == "rx_014"), None)
    if not rx_014:
        errors.append("Prescription rx_014 (Apixaban) not found.")
    else:
        if rx_014.get("quantity") != 90:
            errors.append(f"Expected rx_014 (Apixaban) quantity 90, got {rx_014.get('quantity')}.")

    # rr_011 Sertraline refill -> denied with reason containing "changed"
    rr_011 = next((r for r in state["refillRequests"] if r["id"] == "rr_011"), None)
    if not rr_011:
        errors.append("Refill request rr_011 not found.")
    else:
        if rr_011.get("status") != "denied":
            errors.append(f"Expected rr_011 status 'denied', got '{rr_011.get('status')}'.")
        elif "changed" not in rr_011.get("denyReason", "").lower():
            errors.append(f"Expected rr_011 denyReason to mention 'changed', got '{rr_011.get('denyReason')}'.")

    if errors:
        return False, " ".join(errors)
    return True, "Sertraline frequency updated, Apixaban qty 90, Sertraline refill denied."
