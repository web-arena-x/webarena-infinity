import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify Front Desk removed from Appointment Request and All Providers added to Other for all providers."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    routing = state.get("messageRouting", {})
    providers = ["prov_1", "prov_2", "prov_3", "prov_4", "prov_5"]
    errors = []

    for pid in providers:
        prov_routing = routing.get(pid, {})

        # Check Front Desk (ug_1) NOT in Appointment Request
        appt_routing = prov_routing.get("Appointment Request", [])
        if "ug_1" in appt_routing:
            errors.append(f"{pid}: Front Desk (ug_1) still in Appointment Request routing")

        # Check All Providers (ug_4) IN Other
        other_routing = prov_routing.get("Other", [])
        if "ug_4" not in other_routing:
            errors.append(f"{pid}: All Providers (ug_4) not in Other routing. Current: {other_routing}")

    if errors:
        return False, "; ".join(errors)
    return True, "Front Desk removed from Appointment Request and All Providers added to Other for all providers"
