import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    matters = state.get("matters", [])
    washington = next(
        (m for m in matters
         if "Washington" in m.get("description", "") and
         "Pacific Steel" in m.get("description", "")),
        None
    )

    if washington is None:
        return False, "Could not find a matter with description containing 'Washington' and 'Pacific Steel'."

    pi = washington.get("personalInjury", {})
    deduction_order = pi.get("deductionOrder")

    if deduction_order is None:
        return False, "Washington v. Pacific Steel matter has no personalInjury.deductionOrder set."

    if deduction_order != "fees_first":
        return False, (
            f"Washington v. Pacific Steel personalInjury.deductionOrder is "
            f"'{deduction_order}', expected 'fees_first'."
        )

    return True, "Washington v. Pacific Steel deduction order has been changed to 'fees_first'."
