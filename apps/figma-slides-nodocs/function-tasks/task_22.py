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

    # Find slide with order 5
    target_slide = None
    for s in state.get("slides", []):
        if s.get("presentationId") == pres_id and s.get("order") == 5:
            target_slide = s
            break
    if not target_slide:
        return False, "Could not find slide with order 5 in pres_001."

    transition = target_slide.get("transition", {})
    trans_type = transition.get("type")
    trans_duration = transition.get("duration")

    if trans_type == "push" and trans_duration == 800:
        return True, "Transition of sixth slide set to push/800ms successfully."
    return False, (
        f"Expected transition type 'push' with duration 800 for slide order 5, "
        f"but found type='{trans_type}', duration={trans_duration}."
    )
