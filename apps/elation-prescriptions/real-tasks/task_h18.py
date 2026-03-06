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
    template_names = [t.get("medicationName", "") for t in rx_templates]

    # Check both Lisinopril templates are deleted
    if "Lisinopril 10mg tablet" in template_names:
        return False, "Template 'Lisinopril 10mg tablet' still found in rxTemplates, expected it to be deleted"

    if "Lisinopril 20mg tablet" in template_names:
        return False, "Template 'Lisinopril 20mg tablet' still found in rxTemplates, expected it to be deleted"

    # Check Losartan 50mg template exists
    losartan_tpl = None
    for tpl in rx_templates:
        name = tpl.get("medicationName", "").lower()
        if "losartan" in name and "50mg" in name:
            losartan_tpl = tpl
            break

    if losartan_tpl is None:
        return False, "No Losartan 50mg template found in rxTemplates"

    if losartan_tpl.get("qty") != 30:
        return False, f"Losartan template qty is {losartan_tpl.get('qty')}, expected 30"

    if losartan_tpl.get("refills") != 3:
        return False, f"Losartan template refills is {losartan_tpl.get('refills')}, expected 3"

    if losartan_tpl.get("daysSupply") != 30:
        return False, f"Losartan template daysSupply is {losartan_tpl.get('daysSupply')}, expected 30"

    # Check total count is 11 (was 12, deleted 2, added 1)
    if len(rx_templates) != 11:
        return False, f"rxTemplates count is {len(rx_templates)}, expected 11 (was 12, deleted 2, added 1)"

    return True, "Both Lisinopril templates deleted and Losartan 50mg template created: qty 30, 3 refills, 30 days"
