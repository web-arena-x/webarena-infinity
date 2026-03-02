import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    meds = state.get("permanentRxMeds", [])

    match = [
        m for m in meds
        if "Albuterol" in m.get("medicationName", "")
    ]

    if not match:
        return False, "No med found in permanentRxMeds with medicationName containing 'Albuterol'."

    med = match[0]
    errors = []

    sig = med.get("sig", "")
    if "puffs" not in sig.lower():
        errors.append(f"sig: expected to contain 'puffs', got '{sig}'")
    if "as needed" not in sig.lower():
        errors.append(f"sig: expected to contain 'as needed', got '{sig}'")

    if med.get("qty") != 1:
        errors.append(f"qty: expected 1, got {med.get('qty')}")

    if med.get("unit") != "inhalers":
        errors.append(f"unit: expected 'inhalers', got '{med.get('unit')}'")

    if med.get("refills") != 2:
        errors.append(f"refills: expected 2, got {med.get('refills')}")

    diagnosis = med.get("diagnosis", [])
    codes = [d.get("code") for d in diagnosis if isinstance(d, dict)]
    if "J45.20" not in codes:
        errors.append(f"diagnosis: expected code 'J45.20' in diagnosis array, got codes {codes}")

    if errors:
        return False, f"Albuterol found in permanentRxMeds but has incorrect fields: {'; '.join(errors)}"

    return True, "Albuterol inhaler correctly prescribed with sig containing 'puffs' and 'as needed', qty=1, unit='inhalers', refills=2, diagnosis includes J45.20."
