import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Find Dr. Reyes's prescription and increase dosage to 400mg."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # rx_007 is the only active rx for Margaret prescribed by Dr. Linda Reyes (prov_003)
    rx_007 = next((rx for rx in state["prescriptions"] if rx["id"] == "rx_007"), None)
    if not rx_007:
        return False, "Prescription rx_007 (Gabapentin) not found."

    if "400" not in str(rx_007.get("dosage", "")):
        return False, f"Expected rx_007 dosage to contain '400', got '{rx_007.get('dosage')}'."

    return True, "Gabapentin (Dr. Reyes's prescription) dosage increased to 400mg."
