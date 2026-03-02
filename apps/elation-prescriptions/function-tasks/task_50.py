import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify bulk refill of Lisinopril 10mg and Metformin 500mg."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    permanent_rx_meds = state.get("permanentRxMeds", [])
    errors = []

    # Check total count is at least 13 (was 11 seed + 2 new refills)
    actual_count = len(permanent_rx_meds)
    if actual_count < 13:
        errors.append(
            f"permanentRxMeds count: expected at least 13 (11 seed + 2 refills), "
            f"got {actual_count}"
        )

    # Check at least 2 meds with 'Lisinopril' in name
    lisinopril_meds = [
        m for m in permanent_rx_meds
        if "Lisinopril" in m.get("medicationName", "")
    ]
    if len(lisinopril_meds) < 2:
        errors.append(
            f"Expected at least 2 medications containing 'Lisinopril' in permanentRxMeds "
            f"(original + refill), found {len(lisinopril_meds)}"
        )

    # Check at least 2 meds with 'Metformin' in name
    metformin_meds = [
        m for m in permanent_rx_meds
        if "Metformin" in m.get("medicationName", "")
    ]
    if len(metformin_meds) < 2:
        errors.append(
            f"Expected at least 2 medications containing 'Metformin' in permanentRxMeds "
            f"(original + refill), found {len(metformin_meds)}"
        )

    if errors:
        med_names = [m.get("medicationName", "") for m in permanent_rx_meds]
        return False, (
            f"Bulk refill verification issues: {'; '.join(errors)}. "
            f"Current permanentRxMeds ({actual_count}): {med_names}"
        )

    return True, (
        f"Bulk refill completed successfully. permanentRxMeds count={actual_count}. "
        f"Found {len(lisinopril_meds)} Lisinopril entries and "
        f"{len(metformin_meds)} Metformin entries."
    )
