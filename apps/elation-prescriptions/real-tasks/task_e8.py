import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Check Prednisone template has been deleted
    rx_templates = state.get("rxTemplates", [])

    for template in rx_templates:
        med_name = template.get("medicationName", "")
        if "Prednisone" in med_name:
            return False, f"Prednisone template still present in rxTemplates: '{med_name}'"

    if len(rx_templates) != 11:
        return False, f"Expected 11 Rx templates after deletion, found {len(rx_templates)}"

    return True, "Prednisone taper Rx template deleted successfully; 11 templates remain"
