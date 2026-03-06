import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify Dr. Torres's notification is set to 'Do not notify me' and he's removed from Dr. Chen's General Question routing."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    # Check Dr. Torres (prov_2) notification timeframe
    providers = state.get("providers", [])
    dr_torres = None
    for prov in providers:
        if prov.get("id") == "prov_2":
            dr_torres = prov
            break

    if dr_torres is None:
        return False, "Provider prov_2 (Dr. Torres) not found"

    timeframe = dr_torres.get("notificationTimeframe")
    if timeframe != "none":
        return False, (
            f"Dr. Torres's notificationTimeframe is '{timeframe}', expected 'none' "
            f"(Do not notify me)"
        )

    # Check Dr. Chen's General Question routing does NOT contain prov_2
    message_routing = state.get("messageRouting", {})
    prov1_routing = message_routing.get("prov_1")

    if prov1_routing is None:
        return False, "No message routing found for prov_1 (Dr. Chen)"

    general_routing = prov1_routing.get("General Question")
    if general_routing is None:
        return False, "No 'General Question' routing found for Dr. Chen"

    if "prov_2" in general_routing:
        return False, (
            f"Dr. Torres (prov_2) is still in Dr. Chen's General Question routing: "
            f"{general_routing}"
        )

    return True, (
        "Dr. Torres's notifications set to 'Do not notify me' and "
        "removed from Dr. Chen's General Question routing"
    )
