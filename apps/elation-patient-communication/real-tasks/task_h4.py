import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that Billing Question messages are routed to Front Desk for all providers."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    message_routing = state.get("messageRouting", {})

    provider_ids = ["prov_1", "prov_2", "prov_3", "prov_4", "prov_5"]
    provider_names = {
        "prov_1": "Dr. Chen",
        "prov_2": "Dr. Torres",
        "prov_3": "Jessica Okafor",
        "prov_4": "Dr. Kim",
        "prov_5": "Amanda Wright"
    }

    missing = []
    for prov_id in provider_ids:
        prov_routing = message_routing.get(prov_id)
        if prov_routing is None:
            missing.append(f"{provider_names[prov_id]} ({prov_id}) - no routing found")
            continue

        billing_routing = prov_routing.get("Billing Question")
        if billing_routing is None:
            missing.append(f"{provider_names[prov_id]} ({prov_id}) - no 'Billing Question' category")
            continue

        if "ug_1" not in billing_routing:
            missing.append(
                f"{provider_names[prov_id]} ({prov_id}) - 'ug_1' (Front Desk) not in routing: {billing_routing}"
            )

    if missing:
        return False, (
            f"Billing Question not routed to Front Desk (ug_1) for: {'; '.join(missing)}"
        )

    return True, "Billing Question messages are routed to Front Desk (ug_1) for all 5 providers"
