import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    shop_promise = state.get("shopPromise", {})
    payment_methods = state.get("paymentMethods", [])
    templates = state.get("templates", [])
    sections = state.get("themeSections", [])
    themes = state.get("themes", [])

    dawn = next((t for t in themes if t.get("name") == "Dawn"), None)
    if dawn is None:
        return False, "Theme 'Dawn' not found."

    # Check threshold is $100
    threshold = shop_promise.get("freeShippingThreshold")
    if threshold != 100 and threshold != 100.0:
        return False, f"Expected free shipping threshold $100, got ${threshold}."

    # Check Shop Promise is NOT enabled
    if shop_promise.get("isActive") is not False:
        return False, (
            f"Expected Shop Promise to remain disabled, "
            f"got isActive={shop_promise.get('isActive')}."
        )

    # Check Apple Pay inactive
    apple = next((m for m in payment_methods if m.get("name") == "Apple Pay"), None)
    if apple and apple.get("isActive") is not False:
        return False, f"Expected Apple Pay deactivated, got isActive={apple.get('isActive')}."

    # Check Google Pay inactive
    google = next((m for m in payment_methods if m.get("name") == "Google Pay"), None)
    if google and google.get("isActive") is not False:
        return False, f"Expected Google Pay deactivated, got isActive={google.get('isActive')}."

    # Check Dawn default template checkout disabled
    default_tmpl = next(
        (t for t in templates if t.get("themeId") == dawn["id"] and t.get("isDefault") is True),
        None
    )
    if default_tmpl is None:
        return False, "Dawn default template not found."
    if default_tmpl.get("showAcceleratedCheckout") is not False:
        return False, (
            f"Expected Dawn default template checkout disabled, "
            f"got {default_tmpl.get('showAcceleratedCheckout')}."
        )

    # Check home page featured section checkout disabled
    featured_sec = next(
        (s for s in sections if s.get("type") == "featured_product" and s.get("pageId") == "page_home"),
        None
    )
    if featured_sec is None:
        return False, "Featured product section not found."
    if featured_sec.get("showAcceleratedCheckout") is not False:
        return False, (
            f"Expected featured section checkout disabled, "
            f"got {featured_sec.get('showAcceleratedCheckout')}."
        )

    return True, (
        "Shop Promise threshold $100 (not enabled). Apple Pay and Google Pay deactivated. "
        "Checkout disabled on Dawn default template and home featured section."
    )
