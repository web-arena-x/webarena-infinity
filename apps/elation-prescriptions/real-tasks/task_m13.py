import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Check temporaryMeds for Ondansetron 4mg
    temporary_meds = state.get("temporaryMeds", [])
    ondansetron_med = None
    for med in temporary_meds:
        name = med.get("medicationName", "").lower()
        if "ondansetron" in name and "4mg" in name:
            ondansetron_med = med
            break

    if ondansetron_med is None:
        return False, "No medication containing 'Ondansetron' and '4mg' found in temporaryMeds"

    # Check qty == 12
    qty = ondansetron_med.get("qty")
    if qty != 12:
        return False, f"Ondansetron qty is {qty}, expected 12"

    # Check classification is temporary
    classification = ondansetron_med.get("classification", "")
    if classification != "temporary":
        return False, f"Ondansetron classification is '{classification}', expected 'temporary'"

    return True, "Ondansetron 4mg prescribed as temporary medication with qty 12"
