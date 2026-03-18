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
    slide = next((s for s in slides if s['order'] == 2), None)
    if not slide:
        return False, "Slide with order 2 not found in pres_001."

    elements = slide.get('elements', [])
    if len(elements) < 2:
        return False, f"Expected at least 2 elements on slide order 2, got {len(elements)}."

    content_elem = elements[1]
    list_type = content_elem.get('style', {}).get('listType')
    if list_type != 'numbered':
        return False, f"Expected listType to be 'numbered', got '{list_type}'."

    return True, "List type of content text on slide order 2 of pres_001 is correctly set to 'numbered'."
