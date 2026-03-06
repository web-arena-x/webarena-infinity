import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that Clinical Team (ug_2) has been added to Dr. Chen's Test Results routing."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    message_routing = state.get("messageRouting", {})
    prov1_routing = message_routing.get("prov_1")
    if prov1_routing is None:
        return False, "No message routing found for prov_1 (Dr. Chen)"

    test_results_routing = prov1_routing.get("Test Results")
    if test_results_routing is None:
        return False, "No 'Test Results' routing found for Dr. Chen (prov_1)"

    if "ug_2" not in test_results_routing:
        return False, (
            f"'ug_2' (Clinical Team) not found in Dr. Chen's Test Results routing. "
            f"Current routing: {test_results_routing}"
        )

    return True, "Clinical Team (ug_2) has been added to Dr. Chen's Test Results message routing"
