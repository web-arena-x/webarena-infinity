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

    # Find slide with order 2
    target_slide = None
    for s in state.get("slides", []):
        if s.get("presentationId") == pres_id and s.get("order") == 2:
            target_slide = s
            break
    if not target_slide:
        return False, "Could not find slide with order 2 in pres_001."

    # Find first text element
    elements = target_slide.get("elements", [])
    first_text = None
    for elem in elements:
        if elem.get("type") == "text":
            first_text = elem
            break
    if not first_text:
        return False, "Could not find a text element on slide order 2."

    content = first_text.get("content", "")
    if content == "Q1 Major Launches":
        return True, "Title text on third slide changed to 'Q1 Major Launches' successfully."
    return False, f"Expected first text element content 'Q1 Major Launches', but found '{content}'."
