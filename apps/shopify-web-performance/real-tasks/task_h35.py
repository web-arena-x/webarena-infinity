import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    themes = state.get("themes", [])
    errors = []

    # Prestige is the only non-optimized theme (isOptimized: false)
    prestige = next((t for t in themes if t.get("name") == "Prestige"), None)
    if prestige is None:
        return False, "Could not find Prestige theme."

    sections = prestige.get("sectionsPerPage", {})
    # Original: home=18, product=12, collection=9, cart=5, blog=7
    # After -3: home=15, product=9, collection=6, cart=2, blog=4
    expected = {"home": 15, "product": 9, "collection": 6, "cart": 2, "blog": 4}
    for page_type, expected_val in expected.items():
        actual = sections.get(page_type)
        if actual != expected_val:
            errors.append(f"Prestige {page_type} sections is {actual}, expected {expected_val}.")

    if errors:
        return False, " ".join(errors)
    return True, "Prestige (non-optimized) theme: all page type sections reduced by 3."
