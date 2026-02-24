import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: Announcement bar hidden, Newsletter last in template, page width 1000."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # 1. Announcement bar should be hidden
    announcement = next((s for s in state["sections"]
                         if s["name"] == "Announcement bar" and s["templateId"] == "home"), None)
    if not announcement:
        return False, "Announcement bar section not found."
    if announcement["visible"] is not False:
        return False, f"Expected Announcement bar visible=false, got {announcement['visible']}."

    # 2. Newsletter should be last in template group
    template_sections = [s for s in state["sections"]
                         if s["templateId"] == "home" and s["group"] == "template"]
    template_sections.sort(key=lambda s: s["order"])

    newsletter = next((s for s in template_sections if s["name"] == "Newsletter"), None)
    if not newsletter:
        return False, "Newsletter section not found in template."

    last_section = template_sections[-1]
    if last_section["id"] != newsletter["id"]:
        return False, f"Newsletter is not the last template section. Last is '{last_section['name']}'."

    # 3. Page width should be 1000
    pw = state.get("themeSettings", {}).get("layout", {}).get("pageWidth")
    if pw != 1000:
        return False, f"Expected pageWidth=1000, got {pw}."

    return True, "Announcement bar hidden, Newsletter last, page width 1000."
