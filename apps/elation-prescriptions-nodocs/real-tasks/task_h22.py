import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Find DAW prescription and increase dose to 88mcg."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    rx_004 = next((rx for rx in state["prescriptions"] if rx["id"] == "rx_004"), None)
    if not rx_004:
        return False, "Prescription rx_004 (Levothyroxine) not found."

    if "88" not in str(rx_004.get("dosage", "")):
        return False, f"Expected rx_004 dosage to contain '88', got '{rx_004.get('dosage')}'."

    return True, "Levothyroxine (DAW prescription) dose increased to 88mcg."
