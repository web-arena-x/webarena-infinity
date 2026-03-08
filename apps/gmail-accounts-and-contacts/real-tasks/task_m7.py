# Task: Remove pending and expired delegates.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()
    errors = []

    delegates = state.get("delegates", [])

    pending = [d for d in delegates if d.get("status") == "pending"]
    if pending:
        names = [d.get("name", d.get("email", "unknown")) for d in pending]
        errors.append(f"Pending delegates still exist: {names}")

    expired = [d for d in delegates if d.get("status") == "expired"]
    if expired:
        names = [d.get("name", d.get("email", "unknown")) for d in expired]
        errors.append(f"Expired delegates still exist: {names}")

    active = [d for d in delegates if d.get("status") == "active"]
    if not active:
        errors.append("No active delegates remain; active delegates should not have been removed")

    if errors:
        return False, "; ".join(errors)
    return True, "Pending and expired delegates removed; active delegates preserved."
