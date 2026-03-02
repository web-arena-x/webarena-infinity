import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    templates = state.get("templates", [])
    products = state.get("products", [])
    themes = state.get("themes", [])

    dawn = next((t for t in themes if t.get("name") == "Dawn"), None)
    if dawn is None:
        return False, "Theme 'Dawn' not found."

    # Find the new template
    sale_tmpl = next(
        (t for t in templates if t.get("name") == "Product - Sale Items" and t.get("themeId") == dawn["id"]),
        None
    )
    if sale_tmpl is None:
        return False, "Template 'Product - Sale Items' not found on Dawn."

    if sale_tmpl.get("showAcceleratedCheckout") is not True:
        return False, (
            f"Expected accelerated checkout enabled on 'Product - Sale Items', "
            f"but got {sale_tmpl.get('showAcceleratedCheckout')}."
        )

    if sale_tmpl.get("buyButtonText") != "Buy on sale":
        return False, (
            f"Expected buy button text 'Buy on sale', "
            f"but got '{sale_tmpl.get('buyButtonText')}'."
        )

    # Find products with compare-at prices
    compare_at_products = []
    for p in products:
        has_compare = any(
            v.get("compareAtPrice") is not None
            for v in p.get("variants", [])
        )
        if has_compare:
            compare_at_products.append(p)

    if not compare_at_products:
        return False, "No products with compare-at prices found."

    # Check all are assigned to the sale template
    for p in compare_at_products:
        if p.get("templateId") != sale_tmpl["id"]:
            return False, (
                f"Expected '{p['title']}' (has compare-at price) to be on "
                f"'Product - Sale Items' template, but it's on template '{p.get('templateId')}'."
            )

    return True, (
        f"Template 'Product - Sale Items' created with checkout enabled and 'Buy on sale' text. "
        f"{len(compare_at_products)} product(s) with compare-at prices assigned."
    )
