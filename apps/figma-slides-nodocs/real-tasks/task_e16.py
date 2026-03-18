import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Expected HTTP 200, got {resp.status_code}"
    state = resp.json()
    presentations = state.get("presentations", [])
    pres = next((p for p in presentations if p.get("id") == "pres_010"), None)
    if pres is None:
        return False, "Presentation pres_010 (Marketing Campaign: Design Without Limits) not found"
    starred = pres.get("starred")
    if starred is False:
        return True, "pres_010 is unstarred as expected"
    return False, f"Expected pres_010 starred==false, got starred=={starred}"
