import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Expected HTTP 200, got {resp.status_code}"
    state = resp.json()
    presentations = state.get("presentations", [])
    pres = next((p for p in presentations if p.get("id") == "pres_009"), None)
    if pres is None:
        return False, "Presentation pres_009 (Onboarding Training Module) not found"
    status = pres.get("status")
    if status == "draft":
        return True, "pres_009 status is 'draft' as expected"
    return False, f"Expected pres_009 status=='draft', got status=='{status}'"
