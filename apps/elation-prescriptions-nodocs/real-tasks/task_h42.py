import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Margaret's two prior-auth prescriptions: hold specialty, renew other with 3."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # rx_030 Semaglutide (specialty pharmacy BioPlus) -> on-hold
    rx_030 = next((r for r in state["prescriptions"] if r["id"] == "rx_030"), None)
    if not rx_030:
        errors.append("Prescription rx_030 (Semaglutide) not found.")
    else:
        if rx_030.get("status") != "on-hold":
            errors.append(f"Expected rx_030 (Semaglutide) status 'on-hold', got '{rx_030.get('status')}'.")

    # rx_014 Apixaban (non-specialty) -> renewed with 3 refills
    rx_014 = next((r for r in state["prescriptions"] if r["id"] == "rx_014"), None)
    if not rx_014:
        errors.append("Prescription rx_014 (Apixaban) not found.")
    else:
        if rx_014.get("refillsRemaining") != 3:
            errors.append(f"Expected rx_014 (Apixaban) refillsRemaining 3, got {rx_014.get('refillsRemaining')}.")

    if errors:
        return False, " ".join(errors)
    return True, "Semaglutide (specialty) placed on hold and Apixaban renewed with 3 refills."
