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

    title_elem = elements[0]
    letter_spacing = title_elem.get('style', {}).get('letterSpacing')
    if letter_spacing != 2:
        return False, f"Expected letterSpacing to be 2, got {letter_spacing}."

    return True, "Letter spacing of title on slide order 2 of pres_001 is correctly set to 2."
