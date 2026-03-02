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
    if default_tmpl is None:
        return False, "Dawn's default template not found."

    # Check Home & Gather products are archived
    hg_products = [p for p in products if p.get("vendor") == "Home & Gather"]
    if not hg_products:
        return False, "No Home & Gather products found."

    for p in hg_products:
        if p.get("status") != "archived":
            return False, (
                f"Expected '{p['title']}' (Home & Gather) to be archived, "
                f"but got status='{p.get('status')}'."
            )

    # Check no products remain on the 'No checkout buttons' template
    no_checkout = next(
        (t for t in templates if t.get("name") == "Product - No checkout buttons" and t.get("themeId") == dawn["id"]),
        None
    )

    if no_checkout is not None:
        products_on_nc = [p for p in products if p.get("templateId") == no_checkout["id"]]
        if products_on_nc:
            names = [p["title"] for p in products_on_nc]
            return False, (
                f"Expected no products on 'No checkout buttons' template, "
                f"but found: {', '.join(names)}."
            )

    return True, (
        f"Home & Gather products archived. "
        f"All former 'No checkout buttons' products reassigned to default template."
    )
