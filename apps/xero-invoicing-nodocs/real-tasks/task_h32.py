"""Verify: Update billing street for US-based contact (DataFlow Analytics)."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    state = requests.get(f"{server_url}/api/state", timeout=5).json()
    contacts = state.get("contacts", [])

    # DataFlow Analytics Inc (con_11) is the only US contact
    con = next((c for c in contacts if c["id"] == "con_11"), None)
    if not con:
        return False, "Contact con_11 (DataFlow Analytics Inc) not found"

    addr = con.get("billingAddress", {})
    street = addr.get("street", "")

    if street != "600 Market Street, Suite 500":
        return False, f"Billing street is '{street}', expected '600 Market Street, Suite 500'"

    return True, "DataFlow Analytics Inc billing street updated to '600 Market Street, Suite 500'"
