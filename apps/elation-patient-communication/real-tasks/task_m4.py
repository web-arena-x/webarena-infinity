import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that Nurses (ug_3) are added to Robert Kim's Prescription Refill routing."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    message_routing = state.get("messageRouting", {})
    prov4_routing = message_routing.get("prov_4")
    if prov4_routing is None:
        return False, "No message routing found for prov_4 (Robert Kim)"

    rx_refill_routing = prov4_routing.get("Prescription Refill")
    if rx_refill_routing is None:
        return False, "No 'Prescription Refill' routing found for Robert Kim (prov_4)"

    if "ug_3" not in rx_refill_routing:
        return False, (
            f"'ug_3' (Nurses) not found in Robert Kim's Prescription Refill routing. "
            f"Current routing: {rx_refill_routing}"
        )

    return True, "Nurses (ug_3) are in Robert Kim's Prescription Refill message routing"
