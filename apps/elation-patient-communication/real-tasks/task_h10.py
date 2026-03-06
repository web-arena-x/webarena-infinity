import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that Clinical Team (ug_2) is in all of Dr. Chen's message routing categories."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    message_routing = state.get("messageRouting", {})
    prov1_routing = message_routing.get("prov_1")

    if prov1_routing is None:
        return False, "No message routing found for prov_1 (Dr. Chen)"

    categories = [
        "General Question",
        "Prescription Refill",
        "Appointment Request",
        "Test Results",
        "Billing Question",
        "Referral Request",
        "Medical Records Request",
        "Other"
    ]

    missing = []
    for cat in categories:
        routing = prov1_routing.get(cat)
        if routing is None:
            missing.append(f"'{cat}' - category not found")
        elif "ug_2" not in routing:
            missing.append(f"'{cat}' - current routing: {routing}")

    if missing:
        return False, (
            f"Clinical Team (ug_2) is missing from Dr. Chen's routing for: "
            f"{'; '.join(missing)}"
        )

    return True, "Clinical Team (ug_2) is included in all 8 of Dr. Chen's message routing categories"
