import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify there are 2 Slideshow sections on Home page (original + duplicate)."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    slideshows = [s for s in state["sections"]
                  if s["type"] == "slideshow" and s["templateId"] == "home"]

    if len(slideshows) < 2:
        return False, f"Expected at least 2 slideshow sections, found {len(slideshows)}."

    return True, "Slideshow section has been duplicated."
