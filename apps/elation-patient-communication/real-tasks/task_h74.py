import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify Clinical Team added and Front Desk removed from all of Dr. Torres's routing."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    routing = state.get("messageRouting", {}).get("prov_2", {})
    if not routing:
        return False, "No message routing found for prov_2 (Dr. Torres)"

    categories = [
        "General Question", "Prescription Refill", "Appointment Request",
        "Test Results", "Billing Question", "Referral Request",
        "Medical Records Request", "Other",
    ]

    errors = []
    for cat in categories:
        cat_routing = routing.get(cat, [])

        # Clinical Team (ug_2) must be present
        if "ug_2" not in cat_routing:
            errors.append(f"'{cat}': Clinical Team (ug_2) not found. Current: {cat_routing}")

        # Front Desk (ug_1) must NOT be present
        if "ug_1" in cat_routing:
            errors.append(f"'{cat}': Front Desk (ug_1) still present. Current: {cat_routing}")

    if errors:
        return False, "; ".join(errors)
    return True, "Clinical Team added and Front Desk removed from all Dr. Torres routing categories"
