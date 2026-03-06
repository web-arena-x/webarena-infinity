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

    # Check deleted templates are NOT present
    deleted_templates = [
        "Lisinopril 20mg tablet",
        "Metformin 1000mg tablet",
        "Atorvastatin 40mg tablet",
    ]
    for name in deleted_templates:
        if name in template_names:
            return False, f"Template '{name}' still found in rxTemplates, expected it to be deleted"

    # Check Azithromycin template is NOT present
    azithromycin_found = any("azithromycin" in name.lower() for name in template_names)
    if azithromycin_found:
        return False, "Azithromycin template still found in rxTemplates, expected it to be deleted"

    # Check count is 8 (was 12, deleted 4)
    if len(rx_templates) != 8:
        return False, f"rxTemplates count is {len(rx_templates)}, expected 8 (was 12, deleted 4)"

    return True, "4 Rx templates deleted successfully: Lisinopril 20mg, Metformin 1000mg, Atorvastatin 40mg, Azithromycin Z-Pack"
