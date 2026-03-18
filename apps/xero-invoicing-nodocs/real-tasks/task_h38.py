"""Verify: Find max amountDue awaiting-payment invoice (inv_22), update contact phone."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    state = requests.get(f"{server_url}/api/state", timeout=5).json()
    contacts = state.get("contacts", [])

    # inv_22 ($250,000 amountDue) belongs to Meridian Health Clinic (con_22)
    con = next((c for c in contacts if c["id"] == "con_22"), None)
    if not con:
        return False, "Contact con_22 (Meridian Health Clinic) not found"

    phone = (con.get("phone") or "").replace(" ", "")
    expected = "+6499990000"

    if phone != expected:
        return False, f"Meridian Health Clinic phone is '{con.get('phone')}', expected '+64 9 999 0000'"

    return True, "Meridian Health Clinic phone updated to '+64 9 999 0000'"
