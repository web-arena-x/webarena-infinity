import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Check rxTemplates for Doxycycline 100mg
    rx_templates = state.get("rxTemplates", [])
    doxy_template = None
    for tpl in rx_templates:
        name = tpl.get("medicationName", "").lower()
        if "doxycycline" in name and "100mg" in name:
            doxy_template = tpl
            break

    if doxy_template is None:
        return False, "No Rx template containing 'Doxycycline' and '100mg' found in rxTemplates"

    # Check qty == 14
    qty = doxy_template.get("qty")
    if qty != 14:
        return False, f"Doxycycline template qty is {qty}, expected 14"

    # Check refills == 0
    refills = doxy_template.get("refills")
    if refills != 0:
        return False, f"Doxycycline template refills is {refills}, expected 0"

    # Check daysSupply == 7
    days_supply = doxy_template.get("daysSupply")
    if days_supply != 7:
        return False, f"Doxycycline template daysSupply is {days_supply}, expected 7"

    # Check sig contains BID / twice daily / two times
    sig = doxy_template.get("sig", "").lower()
    if not ("twice daily" in sig or "bid" in sig or "two times" in sig):
        return False, f"Doxycycline template sig is '{doxy_template.get('sig')}', expected it to contain 'twice daily', 'BID', or 'two times'"

    return True, "Doxycycline 100mg Rx template created with correct sig, qty 14, 0 refills, 7 days supply"
