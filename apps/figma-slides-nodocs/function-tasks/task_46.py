import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Find the first slide of pres_001 (order 0)
    slides = state.get("slides", [])
    first_slide = None
    for s in slides:
        if s.get("presentationId") == "pres_001" and s.get("order") == 0:
            first_slide = s
            break

    if not first_slide:
        return False, "First slide (order 0) of pres_001 not found."

    first_slide_id = first_slide.get("id")

    comments = state.get("comments", [])
    target_content = "Great progress on the roadmap!"

    for c in comments:
        if c.get("presentationId") == "pres_001" and c.get("slideId") == first_slide_id:
            if target_content in c.get("content", ""):
                return True, f"Comment '{target_content}' found on the first slide of 'Q1 2026 Product Roadmap'."

    # Also check if the comment exists on pres_001 but on the wrong slide
    for c in comments:
        if c.get("presentationId") == "pres_001" and target_content in c.get("content", ""):
            return False, f"Comment '{target_content}' found on pres_001 but on slide '{c.get('slideId')}', not the first slide '{first_slide_id}'."

    return False, f"No comment containing '{target_content}' found on pres_001."
