import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    copies = [l for l in state["textLayers"] if "Page Title" in l["name"] and l["id"] != "tl_001"]
    if not copies:
        return False, "No duplicate of 'Page Title' found."

    copy = copies[0]
    original = next(l for l in state["textLayers"] if l["id"] == "tl_001")
    if copy["content"] != original["content"]:
        return False, f"Duplicate content mismatch: expected '{original['content']}', got '{copy['content']}'."
    if copy["fontFamily"] != original["fontFamily"]:
        return False, f"Duplicate fontFamily mismatch: expected '{original['fontFamily']}', got '{copy['fontFamily']}'."

    return True, "Text layer 'Page Title' duplicated successfully."
