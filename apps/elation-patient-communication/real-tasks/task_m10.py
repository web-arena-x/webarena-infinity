import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    message_routing = state.get("messageRouting", {})
    prov_2_routing = message_routing.get("prov_2", {})
    prescription_refill = prov_2_routing.get("Prescription Refill", [])

    if "ug_2" not in prescription_refill:
        return False, f"'ug_2' (Clinical Team) not found in Dr. Torres's Prescription Refill routing. Current routing: {prescription_refill}."

    return True, "Clinical Team added to Dr. Torres's Prescription Refill routing."
