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

    # Original slide had 3 elements: [text, text, shape(line)].
    # After deletion of the line shape, should have 2 elements and no line shape elements.
    line_shapes = [e for e in elements if e.get('type') == 'shape' and e.get('shapeType') == 'line']
    if line_shapes:
        return False, "Line shape still exists on the first slide. Expected it to be deleted."

    if len(elements) >= 3:
        return False, f"Expected fewer than 3 elements after deletion, but found {len(elements)}."

    if len(elements) < 2:
        return False, f"Expected at least 2 remaining text elements, but found {len(elements)}."

    return True, "Line shape has been successfully deleted from the first slide. Slide now has 2 elements."
