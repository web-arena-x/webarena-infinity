import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Expected HTTP 200, got {resp.status_code}"
    state = resp.json()
    presentations = state.get("presentations", [])
    pres = next((p for p in presentations if p.get("id") == "pres_012"), None)
    if pres is None:
        return False, "Presentation pres_012 (Q4 2025 Revenue Analysis) not found"
    share_settings = pres.get("shareSettings", {})
    visibility = share_settings.get("visibility")
    if visibility == "public":
        return True, "pres_012 shareSettings.visibility is 'public' as expected"
    return False, f"Expected pres_012 shareSettings.visibility=='public', got visibility=='{visibility}'"
