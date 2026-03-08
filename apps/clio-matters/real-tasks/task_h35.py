import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # The matter at DuPage County with Pending status is Nguyen (mat_005)
    nguyen = None
    for m in state.get("matters", []):
        desc = m.get("description") or ""
        if "Nguyen" in desc or m.get("id") == "mat_005":
            nguyen = m
            break

    if not nguyen:
        return False, "Nguyen matter not found."

    # Rodriguez's responsible staff
    rodriguez = None
    for m in state.get("matters", []):
        desc = m.get("description") or ""
        if "Rodriguez" in desc and "Premier Auto" in desc:
            rodriguez = m
            break

    if not rodriguez:
        return False, "Rodriguez matter not found."

    rodriguez_staff = rodriguez.get("responsibleStaffId")

    errors = []

    if nguyen.get("location") != "Cook County Circuit Court":
        errors.append(
            f"Nguyen location is '{nguyen.get('location')}', "
            f"expected 'Cook County Circuit Court'"
        )

    if nguyen.get("responsibleStaffId") != rodriguez_staff:
        errors.append(
            f"Nguyen responsible staff is '{nguyen.get('responsibleStaffId')}', "
            f"expected '{rodriguez_staff}' (same as Rodriguez case)"
        )

    if errors:
        return False, "; ".join(errors)

    return True, "Nguyen location changed to Cook County and staff assigned to match Rodriguez case."
