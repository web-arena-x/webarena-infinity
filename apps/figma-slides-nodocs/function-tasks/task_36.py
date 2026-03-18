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
    slide = next((s for s in slides if s['order'] == 1), None)
    if not slide:
        return False, "Slide with order 1 not found in pres_001."

    elements = slide.get('elements', [])
    line_elem = next(
        (e for e in elements if e.get('type') == 'shape' and e.get('shapeType') == 'line'),
        None
    )
    if not line_elem:
        return False, "No line shape element found on slide order 1."

    stroke = line_elem.get('stroke', '')
    if stroke.lower() != '#14ae5c':
        return False, f"Expected stroke '#14AE5C', got '{stroke}'."

    return True, "Stroke color of line shape on slide order 1 of pres_001 is correctly set to #14AE5C."
