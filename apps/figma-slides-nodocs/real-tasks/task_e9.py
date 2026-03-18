import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Expected HTTP 200, got {resp.status_code}"
    state = resp.json()
    presentations = state.get("presentations", [])
    pres = next((p for p in presentations if p.get("id") == "pres_018"), None)
    if pres is None:
        return False, "Presentation pres_018 (Design Workshop Materials) not found"
    share_settings = pres.get("shareSettings", {})
    allow_comments = share_settings.get("allowComments")
    if allow_comments is False:
        return True, "pres_018 shareSettings.allowComments is false as expected"
    return False, f"Expected pres_018 shareSettings.allowComments==false, got allowComments=={allow_comments}"
