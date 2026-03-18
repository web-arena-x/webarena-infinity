import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Expected HTTP 200, got {resp.status_code}"
    state = resp.json()
    presentations = state.get("presentations", [])
    pres = next((p for p in presentations if p.get("id") == "pres_015"), None)
    if pres is None:
        return False, "Presentation pres_015 (Product Demo — Enterprise Features) not found"
    starred = pres.get("starred")
    if starred is True:
        return True, "pres_015 is starred as expected"
    return False, f"Expected pres_015 starred==true, got starred=={starred}"
