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

    albuterol = None
    for med in permanent_rx_meds:
        name = med.get("medicationName", "").lower()
        if "albuterol" in name:
            albuterol = med
            break

    if albuterol is None:
        return False, "No Albuterol medication found in permanentRxMeds"

    qty = albuterol.get("qty")
    if qty != 1:
        return False, f"Albuterol qty is {qty}, expected 1"

    refills = albuterol.get("refills", albuterol.get("refillsRemaining"))
    if refills != 1:
        return False, f"Albuterol refills/refillsRemaining is {refills}, expected 1"

    pharmacy_id = albuterol.get("pharmacyId", "")
    pharmacy_name = albuterol.get("pharmacyName", "")
    if pharmacy_id != "pharm_012" and "ucsf" not in pharmacy_name.lower():
        return False, f"Albuterol pharmacy is '{pharmacy_name}' ({pharmacy_id}), expected UCSF Medical Center Pharmacy (pharm_012)"

    classification = albuterol.get("classification", "")
    if classification != "permanent_rx":
        return False, f"Albuterol classification is '{classification}', expected 'permanent_rx'"

    return True, "Albuterol 90mcg inhaler prescribed correctly: qty 1, 1 refill, permanent, UCSF pharmacy"
