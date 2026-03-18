import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    con = next((c for c in state["contacts"] if c["name"] == "Pacific Cloud Solutions"), None)
    if not con:
        return False, "Contact 'Pacific Cloud Solutions' not found."
    if con["email"] != "info@pacificcloud.com":
        return False, f"Wrong email: {con['email']}"
    if con["phone"] != "+1 503 555 6789":
        return False, f"Wrong phone: {con['phone']}"
    addr = con.get("billingAddress", {})
    if addr.get("street") != "900 SW Fifth Avenue":
        return False, f"Wrong street: {addr.get('street')}"
    if addr.get("city") != "Portland":
        return False, f"Wrong city: {addr.get('city')}"
    if addr.get("region") != "OR":
        return False, f"Wrong region: {addr.get('region')}"
    if addr.get("postalCode") != "97204":
        return False, f"Wrong postal code: {addr.get('postalCode')}"
    if addr.get("country") != "United States":
        return False, f"Wrong country: {addr.get('country')}"
    if con.get("taxId") != "US-93-7654321":
        return False, f"Wrong tax ID: {con.get('taxId')}"
    return True, "Contact 'Pacific Cloud Solutions' created with full address and tax ID."
