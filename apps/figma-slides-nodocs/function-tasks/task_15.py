import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Find pres_008 by title
    pres = None
    for p in state.get("presentations", []):
        if "Design Sprint Week 12 Recap" in p.get("title", ""):
            pres = p
            break
    if not pres:
        return False, "Could not find presentation 'Design Sprint Week 12 Recap'."

    pres_id = pres["id"]

    # Count slides for this presentation
    slide_count = sum(
        1 for s in state.get("slides", []) if s.get("presentationId") == pres_id
    )

    if slide_count > 8:
        return True, f"New blank slide added successfully. Slide count is now {slide_count}."
    return False, f"Expected more than 8 slides for pres_008, but found {slide_count}."
