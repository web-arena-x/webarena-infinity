import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    templates = state.get("templates", [])
    products = state.get("products", [])
    sections = state.get("themeSections", [])
    themes = state.get("themes", [])

    dawn = next((t for t in themes if t.get("name") == "Dawn"), None)
    if dawn is None:
        return False, "Theme 'Dawn' not found."

    # In seed data, Dawn has 3 templates:
    # tmpl_1 (Default, ~16 products), tmpl_2 (No checkout, 3 products), tmpl_3 (Gift cards, 1 product)
    # The one with fewest products is Gift cards (1 product) → should be deleted.

    # Verify Gift cards template was deleted
    gift_cards = next(
        (t for t in templates if t.get("name") == "Product - Gift cards" and t.get("themeId") == dawn["id"]),
        None
    )
    if gift_cards is not None:
        # Count products on it to verify it's the right one
        count = sum(1 for p in products if p.get("templateId") == gift_cards["id"])
        return False, (
            f"Expected 'Product - Gift cards' template (fewest products) to be deleted, "
            f"but it still exists with {count} product(s)."
        )

    # Check all remaining Dawn templates have checkout disabled
    dawn_templates = [t for t in templates if t.get("themeId") == dawn["id"]]
    for t in dawn_templates:
        if t.get("showAcceleratedCheckout") is not False:
            return False, (
                f"Expected checkout disabled on '{t['name']}', "
                f"but got showAcceleratedCheckout={t.get('showAcceleratedCheckout')}."
            )

    # Check home page featured product section has checkout disabled
    featured_sec = next(
        (s for s in sections if s.get("type") == "featured_product" and s.get("pageId") == "page_home"),
        None
    )
    if featured_sec is None:
        return False, "Featured product section not found."
    if featured_sec.get("showAcceleratedCheckout") is not False:
        return False, (
            f"Expected checkout disabled on home page featured section, "
            f"but got {featured_sec.get('showAcceleratedCheckout')}."
        )

    return True, (
        "Gift cards template (fewest products) deleted. "
        "Checkout disabled on all remaining Dawn templates and home page section."
    )
