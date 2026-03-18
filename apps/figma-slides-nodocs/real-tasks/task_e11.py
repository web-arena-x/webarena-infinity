import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Expected HTTP 200, got {resp.status_code}"
    state = resp.json()
    presentations = state.get("presentations", [])
    pres = next((p for p in presentations if p.get("id") == "pres_016"), None)
    if pres is None:
        return False, "Presentation pres_016 (Website Redesign Proposal — TechStartup.io) not found"
    status = pres.get("status")
    if status == "published":
        return True, "pres_016 status is 'published' as expected"
    return False, f"Expected pres_016 status=='published', got status=='{status}'"
