import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    con = next((c for c in state["contacts"] if c["name"] == "Nexus Technologies Ltd"), None)
    if not con:
        return False, "Contact 'Nexus Technologies Ltd' not found."
    addr = con.get("billingAddress", {})
    if addr.get("street") != "200 Lambton Quay, Level 15":
        return False, f"Expected street '200 Lambton Quay, Level 15', got '{addr.get('street')}'"
    if addr.get("postalCode") != "6012":
        return False, f"Expected postal code '6012', got '{addr.get('postalCode')}'"
    return True, "Nexus Technologies Ltd billing address updated correctly."
