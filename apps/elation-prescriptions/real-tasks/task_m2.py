import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Check permanentOtcMeds for Glucosamine
    otc_meds = state.get("permanentOtcMeds", [])
    glucosamine_med = None
    for med in otc_meds:
        name = med.get("medicationName", "").lower()
        if "glucosamine" in name:
            glucosamine_med = med
            break

    if glucosamine_med is None:
        return False, "No medication containing 'Glucosamine' found in permanentOtcMeds"

    # Check classification is permanent_otc
    classification = glucosamine_med.get("classification", "")
    if classification != "permanent_otc":
        return False, f"Glucosamine classification is '{classification}', expected 'permanent_otc'"

    # Check sig contains "once daily"
    sig = glucosamine_med.get("sig", "")
    if "once daily" not in sig.lower():
        return False, f"Glucosamine sig is '{sig}', expected it to contain 'once daily'"

    return True, "Glucosamine 1500mg documented as permanent OTC with once daily sig"
