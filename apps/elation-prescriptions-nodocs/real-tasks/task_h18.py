import requests


def verify(server_url: str) -> tuple[bool, str]:
    """November 2025 prescriptions: discontinue PCP's, double cardiologist's qty."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # rx_005 Pantoprazole (prov_001 Mitchell, PCP) -> discontinued
    rx_005 = next((r for r in state["prescriptions"] if r["id"] == "rx_005"), None)
    if not rx_005:
        errors.append("Prescription rx_005 (Pantoprazole) not found.")
    elif rx_005.get("status") != "discontinued":
        errors.append(f"Expected rx_005 (Pantoprazole) status 'discontinued', got '{rx_005.get('status')}'.")

    # rx_014 Apixaban (prov_006 Tanaka, cardiologist) -> quantity doubled from 60 to 120
    rx_014 = next((r for r in state["prescriptions"] if r["id"] == "rx_014"), None)
    if not rx_014:
        errors.append("Prescription rx_014 (Apixaban) not found.")
    elif rx_014.get("quantity") != 120:
        errors.append(f"Expected rx_014 (Apixaban) quantity 120, got {rx_014.get('quantity')}.")

    if errors:
        return False, " ".join(errors)
    return True, "Pantoprazole discontinued and Apixaban quantity doubled."
