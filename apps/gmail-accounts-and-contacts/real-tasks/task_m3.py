# Task: Add delegate ops@techcorp.io named 'TechCorp Ops'.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()
    errors = []

    delegates = state.get("delegates", [])
    match = [
        d for d in delegates
        if d.get("email") == "ops@techcorp.io"
        and d.get("name") == "TechCorp Ops"
    ]

    if not match:
        errors.append("No delegate found with email='ops@techcorp.io' and name='TechCorp Ops'")

    if errors:
        return False, "; ".join(errors)
    return True, "Delegate 'TechCorp Ops' (ops@techcorp.io) added successfully."
