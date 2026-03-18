import requests


def verify(server_url: str) -> tuple[bool, str]:
    """4-patient SSRI management: renew David's, increase Aisha's, discontinue Margaret's, increase Jessica's."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # rx_018 David's Escitalopram -> renewed with 5 refills
    rx_018 = next((r for r in state["prescriptions"] if r["id"] == "rx_018"), None)
    if not rx_018:
        errors.append("Prescription rx_018 (Escitalopram, David) not found.")
    elif rx_018.get("refillsRemaining") != 5:
        errors.append(f"Expected rx_018 refillsRemaining 5, got {rx_018.get('refillsRemaining')}.")

    # rx_021 Aisha's Escitalopram -> dosage 10mg
    rx_021 = next((r for r in state["prescriptions"] if r["id"] == "rx_021"), None)
    if not rx_021:
        errors.append("Prescription rx_021 (Escitalopram, Aisha) not found.")
    elif rx_021.get("dosage") != "10mg":
        errors.append(f"Expected rx_021 dosage '10mg', got '{rx_021.get('dosage')}'.")

    # rx_013 Margaret's Sertraline -> discontinued
    rx_013 = next((r for r in state["prescriptions"] if r["id"] == "rx_013"), None)
    if not rx_013:
        errors.append("Prescription rx_013 (Sertraline, Margaret) not found.")
    elif rx_013.get("status") != "discontinued":
        errors.append(f"Expected rx_013 status 'discontinued', got '{rx_013.get('status')}'.")

    # rx_026 Jessica's Fluoxetine -> dosage 40mg
    rx_026 = next((r for r in state["prescriptions"] if r["id"] == "rx_026"), None)
    if not rx_026:
        errors.append("Prescription rx_026 (Fluoxetine, Jessica) not found.")
    elif rx_026.get("dosage") != "40mg":
        errors.append(f"Expected rx_026 dosage '40mg', got '{rx_026.get('dosage')}'.")

    if errors:
        return False, " ".join(errors)
    return True, "All four SSRI prescriptions managed correctly."
