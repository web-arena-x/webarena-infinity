import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Discontinue Dr. Reyes's rx, renew Dr. Okafor's rx with 11 refills."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # rx_007 Gabapentin (prov_003 Dr. Reyes) -> discontinued
    rx_007 = next((r for r in state["prescriptions"] if r["id"] == "rx_007"), None)
    if not rx_007:
        errors.append("Prescription rx_007 (Gabapentin) not found.")
    else:
        if rx_007.get("status") != "discontinued":
            errors.append(f"Expected rx_007 (Gabapentin, Dr. Reyes) status 'discontinued', got '{rx_007.get('status')}'.")

    # rx_004 Levothyroxine (prov_002 Dr. Okafor) -> renewed with 11 refills
    rx_004 = next((r for r in state["prescriptions"] if r["id"] == "rx_004"), None)
    if not rx_004:
        errors.append("Prescription rx_004 (Levothyroxine) not found.")
    else:
        if rx_004.get("refillsRemaining") != 11:
            errors.append(f"Expected rx_004 (Levothyroxine, Dr. Okafor) refillsRemaining 11, got {rx_004.get('refillsRemaining')}.")

    if errors:
        return False, " ".join(errors)
    return True, "Gabapentin (Dr. Reyes) discontinued and Levothyroxine (Dr. Okafor) renewed with 11 refills."
