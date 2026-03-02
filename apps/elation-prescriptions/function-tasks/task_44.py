import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify Amlodipine 10mg tablet prescribed to preferred pharmacy with diagnosis I10."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    permanent_rx_meds = state.get("permanentRxMeds", [])

    # Find Amlodipine 10mg (NOT the existing 5mg)
    amlodipine_10mg_meds = [
        m for m in permanent_rx_meds
        if "Amlodipine" in m.get("medicationName", "")
        and "10mg" in m.get("medicationName", "")
    ]

    if not amlodipine_10mg_meds:
        amlodipine_all = [
            m.get("medicationName", "") for m in permanent_rx_meds
            if "Amlodipine" in m.get("medicationName", "")
        ]
        return False, (
            f"No medication containing 'Amlodipine' and '10mg' found in permanentRxMeds. "
            f"Amlodipine meds found: {amlodipine_all}"
        )

    med = amlodipine_10mg_meds[0]
    errors = []

    # Check sig
    expected_sig = "Take 1 tablet by mouth once daily"
    actual_sig = med.get("sig")
    if actual_sig != expected_sig:
        errors.append(f"sig: expected '{expected_sig}', got '{actual_sig}'")

    # Check qty
    actual_qty = med.get("qty")
    if actual_qty != 30:
        errors.append(f"qty: expected 30, got {actual_qty}")

    # Check refills
    actual_refills = med.get("refills")
    if actual_refills != 3:
        errors.append(f"refills: expected 3, got {actual_refills}")

    # Check pharmacyId matches preferredPharmacyId
    current_patient = state.get("currentPatient", {})
    preferred_pharmacy_id = current_patient.get("preferredPharmacyId")
    actual_pharmacy_id = med.get("pharmacyId")

    if not preferred_pharmacy_id:
        errors.append("currentPatient.preferredPharmacyId is not set")
    elif actual_pharmacy_id != preferred_pharmacy_id:
        errors.append(
            f"pharmacyId: expected '{preferred_pharmacy_id}' (preferred pharmacy), "
            f"got '{actual_pharmacy_id}'"
        )

    # Check diagnosis contains I10
    diagnosis_list = med.get("diagnosis", [])
    has_i10 = any(
        d.get("code") == "I10" for d in diagnosis_list
    )
    if not has_i10:
        diag_codes = [d.get("code") for d in diagnosis_list]
        errors.append(f"diagnosis should contain code 'I10', got codes: {diag_codes}")

    if errors:
        return False, (
            f"Amlodipine 10mg found in permanentRxMeds but has issues: {'; '.join(errors)}"
        )

    return True, (
        f"Amlodipine 10mg tablet correctly prescribed to preferred pharmacy "
        f"(pharmacyId='{actual_pharmacy_id}'). sig='{actual_sig}', qty={actual_qty}, "
        f"refills={actual_refills}, diagnosis includes I10."
    )
