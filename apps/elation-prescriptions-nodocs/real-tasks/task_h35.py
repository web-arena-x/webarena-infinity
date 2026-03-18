import requests


def verify(server_url: str) -> tuple[bool, str]:
    """History discovery: increase CCB (Amlodipine) dose to 10mg."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # rx_002: Margaret's Amlodipine (the CCB that replaced the discontinued Lisinopril)
    rx_002 = next((rx for rx in state["prescriptions"] if rx["id"] == "rx_002"), None)
    if not rx_002:
        return False, "Prescription rx_002 (Amlodipine) not found."

    if "10" not in str(rx_002.get("dosage", "")):
        return False, f"Expected rx_002 dosage to contain '10', got '{rx_002.get('dosage')}'."

    return True, "Amlodipine (calcium channel blocker) dose increased to 10mg."
