import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify Glucosamine 1500mg documented as OTC and permanentOtcMeds count is 7."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    permanent_otc_meds = state.get("permanentOtcMeds", [])

    # Find Glucosamine in permanentOtcMeds
    glucosamine_meds = [
        m for m in permanent_otc_meds
        if "Glucosamine" in m.get("medicationName", "")
    ]

    if not glucosamine_meds:
        med_names = [m.get("medicationName", "") for m in permanent_otc_meds]
        return False, (
            f"No medication containing 'Glucosamine' found in permanentOtcMeds. "
            f"Current permanentOtcMeds: {med_names}"
        )

    med = glucosamine_meds[0]
    errors = []

    # Check sig contains 'once daily'
    actual_sig = med.get("sig", "")
    if "once daily" not in actual_sig.lower():
        errors.append(f"sig should contain 'once daily', got '{actual_sig}'")

    # Check classification
    actual_class = med.get("classification")
    if actual_class != "permanent_otc":
        errors.append(f"classification: expected 'permanent_otc', got '{actual_class}'")

    # Check count of permanentOtcMeds is 7 (was 6 in seed data)
    actual_count = len(permanent_otc_meds)
    if actual_count != 7:
        errors.append(
            f"permanentOtcMeds count: expected 7 (6 seed + 1 new), got {actual_count}"
        )

    if errors:
        return False, (
            f"Glucosamine found in permanentOtcMeds but has issues: {'; '.join(errors)}"
        )

    return True, (
        f"Glucosamine correctly documented as OTC. "
        f"medicationName='{med.get('medicationName')}', sig='{actual_sig}', "
        f"classification='{actual_class}', permanentOtcMeds count={actual_count}."
    )
