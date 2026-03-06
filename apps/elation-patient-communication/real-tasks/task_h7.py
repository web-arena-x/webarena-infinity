import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify all virtual March 2026 appointments are cancelled and Dr. Kim's virtual visits are deactivated."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    appointments = state.get("appointments", [])

    # Virtual appointments in March 2026:
    # appt_2, appt_6, appt_9, appt_13, appt_14
    virtual_march_ids = {"appt_2", "appt_6", "appt_9", "appt_13", "appt_14"}

    not_cancelled = []
    for appt in appointments:
        if appt.get("id") in virtual_march_ids:
            if appt.get("status") != "cancelled":
                not_cancelled.append(
                    f"{appt.get('id')} (status='{appt.get('status')}')"
                )

    if not_cancelled:
        return False, (
            f"The following virtual March 2026 appointments are not cancelled: "
            f"{', '.join(not_cancelled)}"
        )

    # Check Dr. Kim (prov_4) virtual visits deactivated
    providers = state.get("providers", [])
    dr_kim = None
    for prov in providers:
        if prov.get("id") == "prov_4":
            dr_kim = prov
            break

    if dr_kim is None:
        return False, "Provider prov_4 (Dr. Kim) not found"

    if dr_kim.get("virtualVisitActivated") is not False:
        return False, (
            f"Dr. Kim's virtualVisitActivated is {dr_kim.get('virtualVisitActivated')}, "
            f"expected False"
        )

    return True, (
        "All virtual March 2026 appointments cancelled and Dr. Kim's virtual visits deactivated"
    )
