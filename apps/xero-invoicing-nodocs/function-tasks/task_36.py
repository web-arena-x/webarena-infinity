import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    con = next((c for c in state["contacts"] if c["name"] == "Queenstown Adventure Tours"), None)
    if not con:
        return False, "Contact 'Queenstown Adventure Tours' not found."
    if con["email"] != "bookings@qtadventure.co.nz":
        return False, f"Wrong email: {con['email']}"
    if con["phone"] != "+64 3 442 5500":
        return False, f"Wrong phone: {con['phone']}"
    addr = con.get("billingAddress", {})
    if addr.get("street") != "28 Shotover Street":
        return False, f"Wrong street: {addr.get('street')}"
    if addr.get("city") != "Queenstown":
        return False, f"Wrong city: {addr.get('city')}"
    return True, "Contact 'Queenstown Adventure Tours' created with address."
