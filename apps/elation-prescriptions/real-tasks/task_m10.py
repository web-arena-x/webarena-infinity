import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Find the Metformin 1000mg template (tpl_004)
    rx_templates = state.get("rxTemplates", [])
    metformin_template = None
    for tpl in rx_templates:
        if tpl.get("medicationName") == "Metformin 1000mg tablet":
            metformin_template = tpl
            break

    if metformin_template is None:
        return False, "Metformin 1000mg tablet template not found in rxTemplates"

    # Check qty == 90
    qty = metformin_template.get("qty")
    if qty != 90:
        return False, f"Metformin 1000mg template qty is {qty}, expected 90"

    # Check daysSupply == 45
    days_supply = metformin_template.get("daysSupply")
    if days_supply != 45:
        return False, f"Metformin 1000mg template daysSupply is {days_supply}, expected 45"

    return True, "Metformin 1000mg Rx template updated to qty 90 and daysSupply 45"
