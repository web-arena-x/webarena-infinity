import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that the default signature contains 'CTO'."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()

    try:
        signature = state["settings"]["signatures"]["default"]
    except (KeyError, TypeError) as e:
        return False, f"Could not find settings.signatures.default: {e}"

    if "CTO" in signature:
        return True, "Signature contains 'CTO'."
    return False, f"Expected 'CTO' in signature, got: {signature!r}."
