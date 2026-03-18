import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Expected HTTP 200, got {resp.status_code}"
    state = resp.json()
    presentations = state.get("presentations", [])
    pres = next((p for p in presentations if p.get("id") == "pres_004"), None)
    if pres is None:
        return False, "Presentation pres_004 (User Research Findings — Mobile App) not found"
    starred = pres.get("starred")
    if starred is True:
        return True, "pres_004 is starred as expected"
    return False, f"Expected pres_004 starred==true, got starred=={starred}"
