import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Expected HTTP 200, got {resp.status_code}"
    state = resp.json()
    presentations = state.get("presentations", [])
    pres = next((p for p in presentations if p.get("id") == "pres_006"), None)
    if pres is None:
        return False, "Presentation pres_006 (Annual Company All-Hands 2026) not found"
    starred = pres.get("starred")
    if starred is False:
        return True, "pres_006 is unstarred as expected"
    return False, f"Expected pres_006 starred==false, got starred=={starred}"
