import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    pres = next((p for p in state['presentations'] if p['id'] == 'pres_001'), None)
    if not pres:
        return False, "Presentation pres_001 not found."

    slides = sorted(
        [s for s in state['slides'] if s['presentationId'] == pres['id']],
        key=lambda s: s['order']
    )
    slide = next((s for s in slides if s['order'] == 0), None)
    if not slide:
        return False, "Slide with order 0 not found in pres_001."

    elements = slide.get('elements', [])
    if len(elements) <= 3:
        return False, f"Expected more than 3 elements after adding a text element (was 3), got {len(elements)}."

    text_elements = [e for e in elements if e.get('type') == 'text']
    if len(text_elements) <= 2:
        return False, f"Expected more than 2 text elements (was 2), got {len(text_elements)}."

    return True, "New text element correctly added to slide order 0 of pres_001."
