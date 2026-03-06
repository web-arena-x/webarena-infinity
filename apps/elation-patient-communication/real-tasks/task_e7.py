import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that virtual visits are deactivated for Dr. Michael Torres."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    providers = state.get("providers", [])
    provider = None
    for prov in providers:
        if prov.get("firstName") == "Michael" and prov.get("lastName") == "Torres":
            provider = prov
            break

    if provider is None:
        return False, "Provider Dr. Michael Torres not found"

    virtual_visit = provider.get("virtualVisitActivated")
    if virtual_visit is not False:
        return False, f"Dr. Michael Torres virtualVisitActivated is {virtual_visit}, expected False"

    return True, "Virtual visits are deactivated for Dr. Michael Torres"
