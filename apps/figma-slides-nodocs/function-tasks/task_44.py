import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    presentations = state.get("presentations", [])
    target_pres = None
    for p in presentations:
        if p.get("id") == "pres_001":
            target_pres = p
            break

    if not target_pres:
        return False, "Presentation 'pres_001' (Q1 2026 Product Roadmap) not found."

    slides = state.get("slides", [])
    target_slide = None
    for s in slides:
        if s.get("presentationId") == "pres_001" and s.get("order") == 2:
            target_slide = s
            break

    if not target_slide:
        return False, "Slide with order 2 (third slide) not found in pres_001."

    elements = target_slide.get("elements", [])
    if not elements:
        return False, "Slide order 2 has no elements."

    title_elem = elements[0]
    animation = title_elem.get("animation", {})
    anim_type = animation.get("type", "none")

    if anim_type != "fade-in":
        return False, f"Title element animation type is '{anim_type}', expected 'fade-in'."

    return True, "Title element ('Major Launches') on slide order 2 of 'Q1 2026 Product Roadmap' has animation type 'fade-in'."
