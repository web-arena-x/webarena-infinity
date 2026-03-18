import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Find pres_014 by title
    pres = None
    for p in state.get("presentations", []):
        if "Team Retrospective" in p.get("title", "") and "Sprint 47" in p.get("title", ""):
            pres = p
            break
    if not pres:
        return False, "Could not find presentation 'Team Retrospective — Sprint 47'."

    pres_id = pres["id"]

    # Count slides for this presentation
    slide_count = sum(
        1 for s in state.get("slides", []) if s.get("presentationId") == pres_id
    )

    if slide_count == 5:
        return True, "Last slide deleted successfully. Slide count is now 5."
    return False, f"Expected 5 slides for pres_014 after deletion, but found {slide_count}."
