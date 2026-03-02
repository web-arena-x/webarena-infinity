import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    payment_methods = state.get("paymentMethods", [])
    templates = state.get("templates", [])
    products = state.get("products", [])
    themes = state.get("themes", [])

    dawn = next((t for t in themes if t.get("name") == "Dawn"), None)
    if dawn is None:
        return False, "Theme 'Dawn' not found."

    # Check all accelerated methods except PayPal are inactive
    for m in payment_methods:
        if m.get("type") != "accelerated":
            continue
        if m.get("name") == "PayPal":
            if m.get("isActive") is not True:
                return False, f"Expected PayPal to remain active, got isActive={m.get('isActive')}."
        else:
            if m.get("isActive") is not False:
                return False, (
                    f"Expected '{m['name']}' deactivated (not PayPal), "
                    f"got isActive={m.get('isActive')}."
                )

    # Check new template exists
    paypal_tmpl = next(
        (t for t in templates if t.get("name") == "Product - PayPal Only" and t.get("themeId") == dawn["id"]),
        None
    )
    if paypal_tmpl is None:
        return False, "Template 'Product - PayPal Only' not found on Dawn."

    if paypal_tmpl.get("showAcceleratedCheckout") is not True:
        return False, (
            f"Expected checkout enabled on 'Product - PayPal Only', "
            f"got {paypal_tmpl.get('showAcceleratedCheckout')}."
        )

    # Check Digital Gift Card is assigned
    gift_card = next((p for p in products if p.get("title") == "Digital Gift Card"), None)
    if gift_card is None:
        return False, "Digital Gift Card product not found."
    if gift_card.get("templateId") != paypal_tmpl["id"]:
        return False, (
            f"Expected Digital Gift Card on 'Product - PayPal Only' template, "
            f"but it's on template '{gift_card.get('templateId')}'."
        )

    return True, (
        "All accelerated methods except PayPal deactivated. "
        "Template 'Product - PayPal Only' created with checkout enabled. "
        "Digital Gift Card assigned to it."
    )
