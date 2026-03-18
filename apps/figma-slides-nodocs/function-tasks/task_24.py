import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    pres = next((p for p in state.get("presentations", []) if p.get("title") == "Q1 2026 Product Roadmap"), None)
    if not pres:
        return False, "Presentation 'Q1 2026 Product Roadmap' not found."

    slides = sorted(
        [s for s in state.get("slides", []) if s.get("presentationId") == pres["id"]],
        key=lambda s: s.get("order", 0)
    )
    if not slides:
        return False, "No slides found for 'Q1 2026 Product Roadmap'."

    slide = slides[0]
    elements = slide.get("elements", [])
    if not elements:
        return False, "No elements found on first slide of 'Q1 2026 Product Roadmap'."

    first_elem = elements[0]
    font_family = first_elem.get("style", {}).get("fontFamily", "")
    if font_family != "Poppins":
        return False, f"Expected fontFamily 'Poppins' on title element, got '{font_family}'."

    return True, "Font family of title element on first slide of 'Q1 2026 Product Roadmap' is correctly changed to 'Poppins'."
