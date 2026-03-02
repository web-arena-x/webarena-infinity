import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify Probiotics documented as OTC."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    permanent_otc_meds = state.get("permanentOtcMeds", [])

    # Find Probiotic (case-insensitive) in permanentOtcMeds
    probiotic_meds = [
        m for m in permanent_otc_meds
        if "probiotic" in m.get("medicationName", "").lower()
    ]

    if not probiotic_meds:
        med_names = [m.get("medicationName", "") for m in permanent_otc_meds]
        return False, (
            f"No medication containing 'Probiotic' (case-insensitive) found in permanentOtcMeds. "
            f"Current permanentOtcMeds: {med_names}"
        )

    med = probiotic_meds[0]
    errors = []

    # Check sig contains 'once daily'
    actual_sig = med.get("sig", "")
    if "once daily" not in actual_sig.lower():
        errors.append(f"sig should contain 'once daily', got '{actual_sig}'")

    # Check classification
    actual_class = med.get("classification")
    if actual_class != "permanent_otc":
        errors.append(f"classification: expected 'permanent_otc', got '{actual_class}'")

    if errors:
        return False, (
            f"Probiotic found in permanentOtcMeds but has issues: {'; '.join(errors)}"
        )

    return True, (
        f"Probiotics correctly documented as OTC. "
        f"medicationName='{med.get('medicationName')}', sig='{actual_sig}', "
        f"classification='{actual_class}'."
    )
