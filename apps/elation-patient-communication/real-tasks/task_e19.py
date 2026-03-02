import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    providers = state.get("providers", [])
    for provider in providers:
        if provider.get("id") == "prov_1":
            sharing_default = provider.get("sharingDefault")
            if sharing_default == 4:
                return True, "Default Passport sharing level set to Level 4."
            else:
                return False, (
                    f"Provider prov_1 found but sharingDefault is "
                    f"{sharing_default}, expected 4."
                )

    return False, "Provider with id 'prov_1' not found in providers."
