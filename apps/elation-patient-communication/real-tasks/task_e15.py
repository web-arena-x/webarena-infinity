import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    providers = state.get("providers", [])
    for provider in providers:
        if provider.get("id") == "prov_4":
            if provider.get("virtualVisitActivated") is False:
                return True, "Telehealth has been deactivated for Dr. Kim."
            else:
                return False, (
                    f"Provider prov_4 found but virtualVisitActivated is "
                    f"{provider.get('virtualVisitActivated')}, expected False."
                )

    return False, "Provider with id 'prov_4' not found in providers."
