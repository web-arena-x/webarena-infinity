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
    slide = next((s for s in slides if s['order'] == 4), None)
    if not slide:
        return False, "Slide with order 4 not found in pres_001."

    elements = slide.get('elements', [])
    circle_elem = next(
        (e for e in elements if e.get('type') == 'shape' and e.get('shapeType') == 'circle'),
        None
    )
    if not circle_elem:
        return False, "No shape element with shapeType 'circle' found on slide order 4. The rectangle should have been changed to a circle."

    return True, "Shape type on slide order 4 of pres_001 is correctly changed to 'circle'."
