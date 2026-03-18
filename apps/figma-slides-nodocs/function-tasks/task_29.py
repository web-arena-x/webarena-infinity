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
    if not elements:
        return False, "No elements found on slide with order 2."

    first_elem = elements[0]
    underline = first_elem.get('style', {}).get('underline')
    if underline is not True:
        return False, f"Expected underline to be True, got {underline}."

    return True, "Underline on title of 3rd slide (order 2) is correctly toggled to True."
