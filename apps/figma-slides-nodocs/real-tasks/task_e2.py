import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Expected HTTP 200, got {resp.status_code}"
    state = resp.json()
    presentations = state.get("presentations", [])
    pres = next((p for p in presentations if p.get("id") == "pres_008"), None)
    if pres is None:
        return False, "Presentation pres_008 (Design Sprint Week 12 Recap) not found"
    status = pres.get("status")
    if status == "archived":
        return True, "pres_008 status is 'archived' as expected"
    return False, f"Expected pres_008 status=='archived', got status=='{status}'"
