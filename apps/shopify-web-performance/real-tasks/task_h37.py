import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    themes = state.get("themes", [])
    errors = []

    dawn = next((t for t in themes if t.get("name") == "Dawn (backup)"), None)
    prestige = next((t for t in themes if t.get("name") == "Prestige"), None)

    if dawn is None:
        return False, "Could not find Dawn (backup) theme."
    if prestige is None:
        return False, "Could not find Prestige theme."

    dawn_sections = dawn.get("sectionsPerPage", {})
    prestige_sections = prestige.get("sectionsPerPage", {})

    # Dawn: home=10, cart=5
    if dawn_sections.get("home") != 10:
        errors.append(f"Dawn home sections is {dawn_sections.get('home')}, expected 10.")
    if dawn_sections.get("cart") != 5:
        errors.append(f"Dawn cart sections is {dawn_sections.get('cart')}, expected 5.")

    # Prestige: home=15, cart=8
    if prestige_sections.get("home") != 15:
        errors.append(f"Prestige home sections is {prestige_sections.get('home')}, expected 15.")
    if prestige_sections.get("cart") != 8:
        errors.append(f"Prestige cart sections is {prestige_sections.get('cart')}, expected 8.")

    if errors:
        return False, " ".join(errors)
    return True, "Dawn home=10/cart=5 and Prestige home=15/cart=8 set correctly."
