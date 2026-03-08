import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify notification timeframes set based on virtual visit activation status."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    expected = {
        "prov_1": ("Dr. Chen", "72_hours"),
        "prov_2": ("Dr. Torres", "72_hours"),
        "prov_3": ("Jessica Okafor", "1_week"),
        "prov_4": ("Dr. Kim", "72_hours"),
        "prov_5": ("Amanda Wright", "1_week"),
    }

    errors = []
    for prov in state.get("providers", []):
        pid = prov.get("id")
        if pid in expected:
            name, exp_tf = expected[pid]
            actual_tf = prov.get("notificationTimeframe")
            if actual_tf != exp_tf:
                errors.append(
                    f"{name} ({pid}) timeframe is '{actual_tf}', expected '{exp_tf}'"
                )

    if errors:
        return False, "; ".join(errors)
    return True, "All provider notification timeframes set correctly based on virtual visit status"
