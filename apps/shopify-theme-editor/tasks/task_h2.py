import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify new Multicolumn section exists with a Column block."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    # Seed already has one multicolumn section (section_13)
    mc_sections = [s for s in state["sections"]
                   if s["type"] == "multicolumn" and s["templateId"] == "home" and s["group"] == "template"]

    if len(mc_sections) < 2:
        return False, f"Expected at least 2 multicolumn sections, found {len(mc_sections)}."

    # Find the new one (not section_13) and check it has a column block
    new_mc = [s for s in mc_sections if s["id"] != "section_13"]
    if not new_mc:
        return False, "No new multicolumn section found (only the original section_13)."

    column_blocks = [b for b in new_mc[0]["blocks"] if b["type"] == "column"]
    if len(column_blocks) < 1:
        return False, f"New multicolumn section has no column blocks."

    return True, "New Multicolumn section with Column block found."
