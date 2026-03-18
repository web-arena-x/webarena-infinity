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
    slide = next((s for s in slides if s['order'] == 3), None)
    if not slide:
        return False, "Slide with order 3 not found in pres_001."

    elements = slide.get('elements', [])
    rect_elem = next(
        (e for e in elements if e.get('type') == 'shape' and e.get('shapeType') == 'rectangle'),
        None
    )
    if not rect_elem:
        return False, "No rectangle shape element found on slide order 3."

    fill = rect_elem.get('fill', '')
    if fill.lower() != '#0d99ff':
        return False, f"Expected fill '#0D99FF', got '{fill}'."

    return True, "Fill color of first rectangle shape on slide order 3 of pres_001 is correctly set to #0D99FF."
