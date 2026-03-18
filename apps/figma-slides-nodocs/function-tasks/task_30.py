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
    if len(elements) < 2:
        return False, f"Expected at least 2 elements on slide order 0, got {len(elements)}."

    subtitle_elem = elements[1]
    text_align = subtitle_elem.get('style', {}).get('textAlign')
    if text_align != 'left':
        return False, f"Expected textAlign to be 'left', got '{text_align}'."

    return True, "Subtitle text alignment on slide order 0 of pres_001 is correctly set to 'left'."
