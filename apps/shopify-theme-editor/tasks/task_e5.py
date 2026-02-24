import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify Slideshow section has exactly 2 slide blocks (third removed)."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    slideshow = [s for s in state["sections"] if s["name"] == "Slideshow" and s["templateId"] == "home"]
    if not slideshow:
        return False, "Slideshow section not found."

    slides = [b for b in slideshow[0]["blocks"] if b["type"] == "slide"]
    if len(slides) != 2:
        return False, f"Expected 2 slide blocks, got {len(slides)}."

    return True, "Slideshow has 2 slide blocks (third removed)."
