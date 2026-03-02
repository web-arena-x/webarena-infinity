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

    # In seed data, the vendor with a draft product is Atelier Goods (Cashmere Beanie is draft)
    # Find the draft product's vendor
    draft_products = [p for p in products if p.get("status") == "draft"]
    # In the solved state, the draft product should now be active,
    # so we look for Atelier Goods vendor directly

    # The Cashmere Beanie should now be active
    beanie = next((p for p in products if p.get("title") == "Cashmere Beanie"), None)
    if beanie is None:
        return False, "Cashmere Beanie not found."
    if beanie.get("status") != "active":
        return False, (
            f"Expected Cashmere Beanie (formerly draft) to be active, "
            f"got status='{beanie.get('status')}'."
        )

    vendor = beanie.get("vendor")  # Atelier Goods

    # Check 'Product - Curated' template exists
    curated = next(
        (t for t in templates if t.get("name") == "Product - Curated" and t.get("themeId") == dawn["id"]),
        None
    )
    if curated is None:
        return False, "Template 'Product - Curated' not found on Dawn."

    if curated.get("showAcceleratedCheckout") is not True:
        return False, (
            f"Expected checkout enabled on 'Product - Curated', "
            f"got {curated.get('showAcceleratedCheckout')}."
        )

    if curated.get("buyButtonText") != "Add to collection":
        return False, (
            f"Expected buy button text 'Add to collection', "
            f"got '{curated.get('buyButtonText')}'."
        )

    # Check all products from the vendor are on the curated template
    vendor_products = [p for p in products if p.get("vendor") == vendor]
    for p in vendor_products:
        if p.get("templateId") != curated["id"]:
            return False, (
                f"Expected '{p['title']}' ({vendor}) on 'Product - Curated' template, "
                f"but it's on template '{p.get('templateId')}'."
            )

    return True, (
        f"Cashmere Beanie activated. Template 'Product - Curated' created "
        f"(checkout enabled, 'Add to collection' button). "
        f"All {len(vendor_products)} {vendor} products assigned."
    )
