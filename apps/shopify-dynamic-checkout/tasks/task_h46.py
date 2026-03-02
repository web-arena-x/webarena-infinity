import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    products = state.get("products", [])
    templates = state.get("templates", [])
    themes = state.get("themes", [])

    dawn = next((t for t in themes if t.get("name") == "Dawn"), None)
    if dawn is None:
        return False, "Theme 'Dawn' not found."

    default_tmpl = next(
        (t for t in templates if t.get("themeId") == dawn["id"] and t.get("isDefault") is True),
        None
    )
    no_checkout = next(
        (t for t in templates if t.get("name") == "Product - No checkout buttons" and t.get("themeId") == dawn["id"]),
        None
    )

    if default_tmpl is None:
        return False, "Dawn's default template not found."
    if no_checkout is None:
        return False, "Dawn's 'No checkout buttons' template not found."

    # Check Activewear products are on No checkout buttons
    activewear = [p for p in products if p.get("productType") == "Activewear"]
    for p in activewear:
        if p.get("templateId") != no_checkout["id"]:
            return False, (
                f"Expected Activewear product '{p['title']}' on 'No checkout buttons' template, "
                f"but it's on template '{p.get('templateId')}'."
            )

    # Check Accessories products are on default template
    accessories = [p for p in products if p.get("productType") == "Accessories"]
    for p in accessories:
        if p.get("templateId") != default_tmpl["id"]:
            return False, (
                f"Expected Accessories product '{p['title']}' on default template, "
                f"but it's on template '{p.get('templateId')}'."
            )

    return True, (
        f"{len(activewear)} Activewear products moved to 'No checkout buttons'. "
        f"{len(accessories)} Accessories products moved to default template."
    )
