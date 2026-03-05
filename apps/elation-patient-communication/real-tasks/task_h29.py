import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Apply Dr. Chen's routing to all other providers."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    routing = state.get("messageRouting", {})
    chen_routing = routing.get("prov_1", {})

    if not chen_routing:
        return False, "Dr. Chen's routing (prov_1) is empty or missing."

    categories = [
        "General Question", "Prescription Refill", "Appointment Request",
        "Test Results", "Billing Question", "Referral Request",
        "Medical Records Request", "Other",
    ]

    other_providers = ["prov_2", "prov_3", "prov_4", "prov_5"]
    for prov_id in other_providers:
        prov_routing = routing.get(prov_id, {})
        for cat in categories:
            expected = sorted(chen_routing.get(cat, []))
            actual = sorted(prov_routing.get(cat, []))
            if actual != expected:
                return False, (
                    f"Provider {prov_id} routing for '{cat}' is {actual}, "
                    f"expected {expected} (matching Dr. Chen's routing)."
                )

    return True, "Dr. Chen's routing configuration applied to all providers."
