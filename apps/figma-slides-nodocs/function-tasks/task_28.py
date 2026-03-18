import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Find pres_001 by title
    pres = None
    for p in state.get("presentations", []):
        if p.get("title") == "Q1 2026 Product Roadmap":
            pres = p
            break
    if not pres:
        return False, "Could not find presentation 'Q1 2026 Product Roadmap'."

    pres_id = pres["id"]

    # Find slide with order 0
    target_slide = None
    for s in state.get("slides", []):
        if s.get("presentationId") == pres_id and s.get("order") == 0:
            target_slide = s
            break
    if not target_slide:
        return False, "Could not find slide with order 0 in pres_001."

    # Get second element (index 1) - the subtitle
    elements = target_slide.get("elements", [])
    if len(elements) < 2:
        return False, f"Expected at least 2 elements on slide order 0, but found {len(elements)}."

    subtitle = elements[1]
    italic = subtitle.get("style", {}).get("italic")
    if italic is True:
        return True, "Italic toggled to true on subtitle of first slide successfully."
    return False, f"Expected italic to be True for subtitle on slide order 0, but found {italic}."
