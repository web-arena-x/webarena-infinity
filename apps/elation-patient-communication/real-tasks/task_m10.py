import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that Front Desk (ug_1) has been removed from Dr. Torres's General Question routing."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    message_routing = state.get("messageRouting", {})
    prov2_routing = message_routing.get("prov_2")
    if prov2_routing is None:
        return False, "No message routing found for prov_2 (Dr. Torres)"

    general_question_routing = prov2_routing.get("General Question")
    if general_question_routing is None:
        return False, "No 'General Question' routing found for Dr. Torres (prov_2)"

    if "ug_1" in general_question_routing:
        return False, (
            f"'ug_1' (Front Desk) is still in Dr. Torres's General Question routing. "
            f"Current routing: {general_question_routing}"
        )

    return True, "Front Desk (ug_1) has been removed from Dr. Torres's General Question message routing"
