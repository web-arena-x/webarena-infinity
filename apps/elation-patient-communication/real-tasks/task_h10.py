import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    providers = state.get("providers", [])
    provider_map = {p["id"]: p for p in providers}

    # Jessica Okafor (prov_3)
    prov_3 = provider_map.get("prov_3")
    if prov_3 is None:
        return False, "Provider prov_3 (Jessica Okafor) not found in state."

    if prov_3.get("virtualVisitActivated") is not True:
        return False, (
            "Jessica Okafor (prov_3) virtualVisitActivated is not True."
        )

    instructions_3 = prov_3.get("virtualVisitInstructions", "") or ""
    if "zoom.us/j/okafor123" not in instructions_3:
        return False, (
            "Jessica Okafor (prov_3) instructions do not contain "
            "'zoom.us/j/okafor123'."
        )

    # Amanda Wright (prov_5)
    prov_5 = provider_map.get("prov_5")
    if prov_5 is None:
        return False, "Provider prov_5 (Amanda Wright) not found in state."

    if prov_5.get("virtualVisitActivated") is not True:
        return False, (
            "Amanda Wright (prov_5) virtualVisitActivated is not True."
        )

    instructions_5 = prov_5.get("virtualVisitInstructions", "") or ""
    if "zoom.us/j/wright456" not in instructions_5:
        return False, (
            "Amanda Wright (prov_5) instructions do not contain "
            "'zoom.us/j/wright456'."
        )

    return True, "Telehealth activated for Jessica Okafor and Amanda Wright."
