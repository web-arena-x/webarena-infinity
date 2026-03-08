import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify PA virtual visits activated and added to Dr. Kim's routing."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    errors = []

    # Check prov_5 virtual visits
    prov_5 = None
    for prov in state.get("providers", []):
        if prov.get("id") == "prov_5":
            prov_5 = prov
            break

    if not prov_5:
        errors.append("Provider prov_5 (Amanda Wright) not found")
    else:
        if not prov_5.get("virtualVisitActivated"):
            errors.append("prov_5 virtual visits not activated")
        instructions = prov_5.get("virtualVisitInstructions", "")
        if "https://meet.bayareafamilymed.com/wright" not in instructions:
            errors.append(
                f"prov_5 virtual visit instructions don't contain expected URL. "
                f"Got: '{instructions}'"
            )

    # Check prov_5 in Dr. Kim's routing
    kim_routing = state.get("messageRouting", {}).get("prov_4", {})

    test_results = kim_routing.get("Test Results", [])
    if "prov_5" not in test_results:
        errors.append(f"prov_5 not in Dr. Kim's Test Results routing. Current: {test_results}")

    referral = kim_routing.get("Referral Request", [])
    if "prov_5" not in referral:
        errors.append(f"prov_5 not in Dr. Kim's Referral Request routing. Current: {referral}")

    if errors:
        return False, "; ".join(errors)
    return True, "PA virtual visits activated and added to Dr. Kim's Test Results and Referral Request routing"
