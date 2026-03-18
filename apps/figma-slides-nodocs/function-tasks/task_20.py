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

    expected_notes = "Highlight the three major product launches and their specific impact metrics."
    notes = target_slide.get("speakerNotes", "")
    if notes == expected_notes:
        return True, "Speaker notes updated successfully."
    return False, f"Expected speakerNotes to be '{expected_notes}', but found '{notes}'."
