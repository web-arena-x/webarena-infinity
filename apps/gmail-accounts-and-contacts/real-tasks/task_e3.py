# Task: Remove the expired delegate.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    delegates = state.get("delegates", [])
    expired = [d for d in delegates if d.get("status") == "expired"]

    if len(expired) == 0:
        return True, "No expired delegates remain."
    else:
        names = [d.get("name", d.get("email", "unknown")) for d in expired]
        return False, f"Found {len(expired)} expired delegate(s): {', '.join(names)}."
