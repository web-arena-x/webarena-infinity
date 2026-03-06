import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that Dr. Chen's clinical profile sharing default is changed to Level 3."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    providers = state.get("providers", [])
    provider = None
    for prov in providers:
        if prov.get("firstName") == "Sarah" and prov.get("lastName") == "Chen":
            provider = prov
            break

    if provider is None:
        return False, "Provider Dr. Sarah Chen not found"

    sharing_default = provider.get("sharingDefault")
    if sharing_default != 3:
        return False, f"Dr. Chen's sharingDefault is {sharing_default}, expected 3"

    return True, "Dr. Chen's clinical profile sharing default is set to Level 3"
