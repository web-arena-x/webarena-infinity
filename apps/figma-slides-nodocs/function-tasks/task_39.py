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
    if not elements:
        return False, "No elements found on slide with order 0."

    title_elem = elements[0]
    rotation = title_elem.get('rotation')
    if rotation is None:
        return False, "rotation not found on the first element."
    if float(rotation) != 45:
        return False, f"Expected rotation 45, got {rotation}."

    return True, "Rotation of title on slide order 0 of pres_001 is correctly set to 45."
