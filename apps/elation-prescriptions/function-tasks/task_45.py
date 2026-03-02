import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify Escitalopram 10mg tablet prescribed to Alto Pharmacy as permanent Rx."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    permanent_rx_meds = state.get("permanentRxMeds", [])

    # Find Escitalopram 10mg in permanentRxMeds
    escitalopram_meds = [
        m for m in permanent_rx_meds
        if "Escitalopram" in m.get("medicationName", "")
        and "10mg" in m.get("medicationName", "")
    ]

    if not escitalopram_meds:
        med_names = [m.get("medicationName", "") for m in permanent_rx_meds]
        return False, (
            f"No medication containing 'Escitalopram' and '10mg' found in permanentRxMeds. "
            f"Current permanentRxMeds: {med_names}"
        )

    med = escitalopram_meds[0]
    errors = []

    # Check sig
    expected_sig = "Take 1 tablet by mouth once daily in the morning"
    actual_sig = med.get("sig")
    if actual_sig != expected_sig:
        errors.append(f"sig: expected '{expected_sig}', got '{actual_sig}'")

    # Check qty
    actual_qty = med.get("qty")
    if actual_qty != 30:
        errors.append(f"qty: expected 30, got {actual_qty}")

    # Check refills
    actual_refills = med.get("refills")
    if actual_refills != 5:
        errors.append(f"refills: expected 5, got {actual_refills}")

    # Check classification
    actual_class = med.get("classification")
    if actual_class != "permanent_rx":
        errors.append(f"classification: expected 'permanent_rx', got '{actual_class}'")

    # Look up Alto Pharmacy by name
    pharmacies = state.get("pharmacies", [])
    alto_pharmacies = [
        p for p in pharmacies
        if "Alto" in p.get("name", "")
    ]

    if not alto_pharmacies:
        errors.append("No pharmacy with name containing 'Alto' found in state.pharmacies")
    else:
        alto_pharmacy_id = alto_pharmacies[0].get("id")
        actual_pharmacy_id = med.get("pharmacyId")
        if actual_pharmacy_id != alto_pharmacy_id:
            errors.append(
                f"pharmacyId: expected '{alto_pharmacy_id}' (Alto Pharmacy), "
                f"got '{actual_pharmacy_id}'"
            )

    if errors:
        return False, (
            f"Escitalopram 10mg found in permanentRxMeds but has issues: {'; '.join(errors)}"
        )

    return True, (
        f"Escitalopram 10mg tablet correctly prescribed to Alto Pharmacy as permanent Rx. "
        f"sig='{actual_sig}', qty={actual_qty}, refills={actual_refills}, "
        f"classification='{actual_class}', pharmacyId='{med.get('pharmacyId')}'."
    )
