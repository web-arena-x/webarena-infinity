import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that virtual visits are activated for Jessica Okafor with the correct instructions."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    providers = state.get("providers", [])
    provider = None
    for prov in providers:
        if prov.get("firstName") == "Jessica" and prov.get("lastName") == "Okafor":
            provider = prov
            break

    if provider is None:
        return False, "Provider Jessica Okafor not found"

    virtual_visit = provider.get("virtualVisitActivated")
    if virtual_visit is not True:
        return False, f"Jessica Okafor virtualVisitActivated is {virtual_visit}, expected True"

    instructions = provider.get("virtualVisitInstructions", "")
    if "https://zoom.us/j/1234567890" not in instructions:
        return False, (
            f"Jessica Okafor virtualVisitInstructions does not contain 'https://zoom.us/j/1234567890'. "
            f"Current instructions: '{instructions}'"
        )

    return True, "Virtual visits activated for Jessica Okafor with correct Zoom link"
