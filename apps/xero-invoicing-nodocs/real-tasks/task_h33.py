"""Verify: Update billing region for both Hamilton contacts to 'Waikato Region'."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    state = requests.get(f"{server_url}/api/state", timeout=5).json()
    contacts = state.get("contacts", [])

    # Hamilton contacts: con_2 (Hamilton Plumbing) and con_25 (Velocity Sports)
    target_ids = {"con_2": "Hamilton Plumbing Services", "con_25": "Velocity Sports Equipment"}
    errors = []

    for cid, name in target_ids.items():
        con = next((c for c in contacts if c["id"] == cid), None)
        if not con:
            errors.append(f"Contact {cid} ({name}) not found")
            continue
        region = con.get("billingAddress", {}).get("region", "")
        if region != "Waikato Region":
            errors.append(f"{name} region is '{region}', expected 'Waikato Region'")

    if errors:
        return False, "; ".join(errors)
    return True, "Both Hamilton contacts updated to 'Waikato Region'"
