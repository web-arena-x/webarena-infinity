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

    # Count slides for this presentation
    slide_count = sum(
        1 for s in state.get("slides", []) if s.get("presentationId") == pres_id
    )

    if slide_count == 16:
        return True, "First slide duplicated successfully. Slide count is now 16."
    return False, f"Expected 16 slides for pres_001 after duplication, but found {slide_count}."
