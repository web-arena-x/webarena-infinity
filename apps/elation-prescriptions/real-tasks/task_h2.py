import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    permanent_rx_meds = state.get("permanentRxMeds", [])

    buspirone = None
    for med in permanent_rx_meds:
        name = med.get("medicationName", "").lower()
        if "buspirone" in name and "10mg" in name:
            buspirone = med
            break

    if buspirone is None:
        return False, "No Buspirone 10mg medication found in permanentRxMeds"

    qty = buspirone.get("qty")
    if qty != 30:
        return False, f"Buspirone qty is {qty}, expected 30"

    refills = buspirone.get("refills", buspirone.get("refillsRemaining"))
    if refills != 5:
        return False, f"Buspirone refills/refillsRemaining is {refills}, expected 5"

    pharmacy_id = buspirone.get("pharmacyId", "")
    pharmacy_name = buspirone.get("pharmacyName", "")
    if pharmacy_id != "pharm_003" and "walgreens" not in pharmacy_name.lower():
        return False, f"Buspirone pharmacy is '{pharmacy_name}' ({pharmacy_id}), expected Walgreens #7892 (pharm_003)"

    return True, "Buspirone 10mg prescribed correctly: qty 30, 5 refills, at Walgreens #7892"
