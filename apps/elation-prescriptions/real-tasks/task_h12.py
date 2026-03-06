import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    rx_templates = state.get("rxTemplates", [])

    # Check Doxycycline 100mg template exists
    doxycycline_tpl = None
    for tpl in rx_templates:
        name = tpl.get("medicationName", "").lower()
        if "doxycycline" in name and "100mg" in name:
            doxycycline_tpl = tpl
            break

    if doxycycline_tpl is None:
        return False, "No Doxycycline 100mg template found in rxTemplates"

    if doxycycline_tpl.get("qty") != 20:
        return False, f"Doxycycline template qty is {doxycycline_tpl.get('qty')}, expected 20"

    if doxycycline_tpl.get("refills") != 0:
        return False, f"Doxycycline template refills is {doxycycline_tpl.get('refills')}, expected 0"

    # Check Cephalexin 500mg template exists
    cephalexin_tpl = None
    for tpl in rx_templates:
        name = tpl.get("medicationName", "").lower()
        if "cephalexin" in name and "500mg" in name:
            cephalexin_tpl = tpl
            break

    if cephalexin_tpl is None:
        return False, "No Cephalexin 500mg template found in rxTemplates"

    if cephalexin_tpl.get("qty") != 21:
        return False, f"Cephalexin template qty is {cephalexin_tpl.get('qty')}, expected 21"

    if cephalexin_tpl.get("refills") != 0:
        return False, f"Cephalexin template refills is {cephalexin_tpl.get('refills')}, expected 0"

    # Check total template count is 14 (was 12, added 2)
    if len(rx_templates) != 14:
        return False, f"rxTemplates count is {len(rx_templates)}, expected 14 (was 12, added 2)"

    return True, "2 new Rx templates created: Doxycycline 100mg (qty 20, 0 refills) and Cephalexin 500mg (qty 21, 0 refills)"
