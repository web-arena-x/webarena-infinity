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

    # Original first slide has no rectangle shapes (only a line shape).
    # Verify a rectangle shape now exists.
    rect_elements = [
        e for e in elements
        if e.get('type') == 'shape' and e.get('shapeType') == 'rectangle'
    ]
    if not rect_elements:
        return False, "No element with type='shape' and shapeType='rectangle' found on slide order 0."

    return True, "Rectangle shape element correctly added to slide order 0 of pres_001."
