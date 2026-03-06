import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Check Losartan is NOT in permanentRxMeds
    permanent_rx_meds = state.get("permanentRxMeds", [])
    for med in permanent_rx_meds:
        if med.get("medicationName") == "Losartan 50mg tablet":
            return False, "Losartan 50mg tablet is still in permanentRxMeds; expected it to be removed"

    # Check Losartan IS in discontinuedMeds with status "discontinued"
    discontinued_meds = state.get("discontinuedMeds", [])
    losartan_discontinued = None
    for med in discontinued_meds:
        if med.get("medicationName") == "Losartan 50mg tablet":
            losartan_discontinued = med
            break

    if losartan_discontinued is None:
        return False, "Losartan 50mg tablet not found in discontinuedMeds"

    if losartan_discontinued.get("status") != "discontinued":
        return False, f"Losartan in discontinuedMeds has status '{losartan_discontinued.get('status')}', expected 'discontinued'"

    # Check discontinueReason contains "another prescriber"
    reason = losartan_discontinued.get("discontinueReason", "")
    details = losartan_discontinued.get("discontinueDetails", "")
    combined = (reason + " " + details).lower()
    if "another prescriber" not in combined:
        return False, f"Losartan discontinue reason/details do not contain 'another prescriber'. Reason: '{reason}', Details: '{details}'"

    return True, "Losartan discontinued with reason 'discontinued by another prescriber'"
