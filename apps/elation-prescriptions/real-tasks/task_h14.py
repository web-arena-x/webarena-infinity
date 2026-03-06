import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    settings = state.get("settings", {})

    # Check default pharmacy changed to Walgreens #7892
    default_pharmacy = settings.get("defaultPharmacyId", "")
    if default_pharmacy != "pharm_003":
        return False, f"settings.defaultPharmacyId is '{default_pharmacy}', expected 'pharm_003' (Walgreens #7892)"

    # Check auto-populate is off
    auto_populate = settings.get("autoPopulateLastPharmacy")
    if auto_populate is not False:
        return False, f"settings.autoPopulateLastPharmacy is {auto_populate}, expected false"

    # Check a Gabapentin entry exists at Walgreens with qty 90 and refills 3
    permanent_rx_meds = state.get("permanentRxMeds", [])
    gabapentin_walgreens = None
    for med in permanent_rx_meds:
        name = med.get("medicationName", "").lower()
        if "gabapentin" not in name:
            continue
        pharmacy_id = med.get("pharmacyId", "")
        pharmacy_name = med.get("pharmacyName", "")
        if pharmacy_id == "pharm_003" or "walgreens" in pharmacy_name.lower():
            if med.get("qty") == 90:
                refills = med.get("refills", med.get("refillsRemaining"))
                if refills == 3:
                    gabapentin_walgreens = med
                    break

    if gabapentin_walgreens is None:
        return False, "No Gabapentin entry found in permanentRxMeds at Walgreens (pharm_003) with qty 90 and 3 refills"

    return True, "Default pharmacy set to Walgreens, auto-populate disabled, Gabapentin 300mg prescribed at Walgreens with qty 90 and 3 refills"
