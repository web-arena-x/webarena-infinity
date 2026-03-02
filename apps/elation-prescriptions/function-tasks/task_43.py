import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify Ondansetron 4mg tablet prescribed as temporary with pharmacy instructions."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    temporary_meds = state.get("temporaryMeds", [])

    # Find new Ondansetron 4mg in temporaryMeds
    ondansetron_meds = [
        m for m in temporary_meds
        if "Ondansetron" in m.get("medicationName", "")
        and "4mg" in m.get("medicationName", "")
    ]

    if not ondansetron_meds:
        med_names = [m.get("medicationName", "") for m in temporary_meds]
        return False, (
            f"No medication containing 'Ondansetron' and '4mg' found in temporaryMeds. "
            f"Current temporaryMeds: {med_names}"
        )

    med = ondansetron_meds[0]
    errors = []

    # Check qty
    actual_qty = med.get("qty")
    if actual_qty != 12:
        errors.append(f"qty: expected 12, got {actual_qty}")

    # Check refills
    actual_refills = med.get("refills")
    if actual_refills != 0:
        errors.append(f"refills: expected 0, got {actual_refills}")

    # Check classification
    actual_class = med.get("classification")
    if actual_class != "temporary":
        errors.append(f"classification: expected 'temporary', got '{actual_class}'")

    # Check instructionsToPharmacy contains 'post-surgical' or 'urgent'
    instructions = med.get("instructionsToPharmacy", "") or ""
    instructions_lower = instructions.lower()
    if "post-surgical" not in instructions_lower and "urgent" not in instructions_lower:
        errors.append(
            f"instructionsToPharmacy should contain 'post-surgical' or 'urgent', "
            f"got '{instructions}'"
        )

    if errors:
        return False, (
            f"Ondansetron 4mg found in temporaryMeds but has issues: {'; '.join(errors)}"
        )

    return True, (
        f"Ondansetron 4mg tablet correctly prescribed as temporary. "
        f"qty={actual_qty}, refills={actual_refills}, classification='{actual_class}', "
        f"instructionsToPharmacy='{instructions}'"
    )
