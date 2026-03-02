import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    providers = state.get("providers", [])
    provider = None
    for prov in providers:
        if prov.get("id") == "prov_3":
            provider = prov
            break

    if provider is None:
        return False, "Provider prov_3 (Jessica Okafor) not found."

    if provider.get("virtualVisitActivated") is not True:
        return False, "Telehealth is not activated for Jessica Okafor."

    instructions = str(provider.get("virtualVisitInstructions", ""))
    if "zoom.us/j/1234567890" not in instructions:
        return False, f"Zoom link 'zoom.us/j/1234567890' not found in virtual visit instructions. Current instructions: '{instructions}'."

    return True, "Telehealth activated for Jessica Okafor with Zoom link."
