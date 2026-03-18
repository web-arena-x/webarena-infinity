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
        if s.get("presentationId") == "pres_001" and s.get("order") == 8:
            target_slide = s
            break

    if not target_slide:
        return False, "Slide with order 8 (ninth slide) not found in pres_001."

    elements = target_slide.get("elements", [])
    if not elements:
        return False, "Slide order 8 has no elements."

    title_elem = elements[0]
    animation = title_elem.get("animation", {})

    errors = []
    anim_type = animation.get("type", "none")
    if anim_type != "bounce-in":
        errors.append(f"animation type is '{anim_type}', expected 'bounce-in'")

    anim_duration = animation.get("duration")
    if anim_duration != 500:
        errors.append(f"animation duration is {anim_duration}, expected 500")

    anim_delay = animation.get("delay")
    if anim_delay != 200:
        errors.append(f"animation delay is {anim_delay}, expected 200")

    if errors:
        return False, "Title animation on slide order 8: " + "; ".join(errors) + "."

    return True, "Title element on slide order 8 of 'Q1 2026 Product Roadmap' has animation bounce-in, duration 500ms, delay 200ms."
