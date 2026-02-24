import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify 'Featured collection' is above 'Image banner' in template order."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    template_sections = [s for s in state["sections"]
                         if s["templateId"] == "home" and s["group"] == "template"]
    template_sections.sort(key=lambda s: s["order"])

    fc = next((s for s in template_sections if s["name"] == "Featured collection"), None)
    ib = next((s for s in template_sections if s["name"] == "Image banner"), None)

    if not fc:
        return False, "Featured collection section not found."
    if not ib:
        return False, "Image banner section not found."

    if fc["order"] >= ib["order"]:
        return False, f"Featured collection (order={fc['order']}) is not above Image banner (order={ib['order']})."

    return True, "Featured collection is above Image banner."
