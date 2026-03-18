import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Expected HTTP 200, got {resp.status_code}"
    state = resp.json()
    presentations = state.get("presentations", [])
    pres = next((p for p in presentations if p.get("id") == "pres_002"), None)
    if pres is None:
        return False, "Presentation pres_002 (Brand Identity Guidelines v2.0) not found"
    share_settings = pres.get("shareSettings", {})
    allow_editing = share_settings.get("allowEditing")
    if allow_editing is False:
        return True, "pres_002 shareSettings.allowEditing is false as expected"
    return False, f"Expected pres_002 shareSettings.allowEditing==false, got allowEditing=={allow_editing}"
