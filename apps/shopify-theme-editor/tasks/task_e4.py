import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify 'Rich text' section is hidden."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    rich_text = [s for s in state["sections"] if s["name"] == "Rich text" and s["templateId"] == "home"]
    if not rich_text:
        return False, "Rich text section not found."

    if rich_text[0]["visible"] is not False:
        return False, f"Expected Rich text section visible=false, got {rich_text[0]['visible']}."

    return True, "Rich text section is hidden."
