# Task: Invert all Google service link states.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()
    errors = []

    linked_services = state.get("linkedServices", [])

    # Expected states after inversion (opposite of seed)
    expected = {
        "svc_1": ("Google Search", False),
        "svc_2": ("YouTube", False),
        "svc_3": ("Google Ads", True),
        "svc_4": ("Google Play", False),
        "svc_5": ("Chrome", False),
        "svc_6": ("Google Shopping", True),
        "svc_7": ("Google Maps", False),
    }

    svc_map = {s.get("id"): s for s in linked_services}

    for svc_id, (name, expected_linked) in expected.items():
        svc = svc_map.get(svc_id)
        if not svc:
            errors.append(f"Service '{name}' ({svc_id}) not found")
            continue
        if svc.get("isLinked") != expected_linked:
            errors.append(
                f"{name} isLinked={svc.get('isLinked')}, expected {expected_linked}"
            )

    if errors:
        return False, "; ".join(errors)
    return True, "All Google service link states successfully inverted."
