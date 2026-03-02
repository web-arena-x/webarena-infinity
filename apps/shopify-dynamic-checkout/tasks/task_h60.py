import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    themes = state.get("themes", [])
    payment_methods = state.get("paymentMethods", [])
    apps = state.get("installedApps", [])
    cart_attrs = state.get("cartAttributes", [])
    shop_promise = state.get("shopPromise", {})

    # Check conflicting cart attributes are disabled
    for attr in cart_attrs:
        if attr.get("conflictsWithCheckout") is True:
            if attr.get("isActive") is not False:
                return False, (
                    f"Expected '{attr['name']}' (conflicts) disabled, "
                    f"got isActive={attr.get('isActive')}."
                )

    # Check conflicting apps are deactivated
    for app in apps:
        if app.get("conflictsWithCheckout") is True:
            if app.get("isActive") is not False:
                return False, (
                    f"Expected '{app['name']}' (conflicts) deactivated, "
                    f"got isActive={app.get('isActive')}."
                )

    # Check Amazon Pay active
    amazon = next((m for m in payment_methods if m.get("name") == "Amazon Pay"), None)
    if amazon and amazon.get("isActive") is not True:
        return False, f"Expected Amazon Pay active, got isActive={amazon.get('isActive')}."

    # Check Venmo active
    venmo = next((m for m in payment_methods if m.get("name") == "Venmo"), None)
    if venmo and venmo.get("isActive") is not True:
        return False, f"Expected Venmo active, got isActive={venmo.get('isActive')}."

    # Check Shop Promise
    if shop_promise.get("isActive") is not True:
        return False, f"Expected Shop Promise enabled, got isActive={shop_promise.get('isActive')}."

    delivery = shop_promise.get("estimatedDeliveryDays", {})
    if delivery.get("min") != 1:
        return False, f"Expected min delivery days 1, got {delivery.get('min')}."
    if delivery.get("max") != 3:
        return False, f"Expected max delivery days 3, got {delivery.get('max')}."

    threshold = shop_promise.get("freeShippingThreshold")
    if threshold != 50 and threshold != 50.0:
        return False, f"Expected free shipping threshold $50, got ${threshold}."

    # Check Craft is published
    craft = next((t for t in themes if t.get("name") == "Craft"), None)
    if craft is None:
        return False, "Theme 'Craft' not found."
    if craft.get("role") != "main":
        return False, f"Expected Craft published, got role='{craft.get('role')}'."

    dawn = next((t for t in themes if t.get("name") == "Dawn"), None)
    if dawn and dawn.get("role") == "main":
        return False, "Dawn should no longer be published."

    return True, (
        "Conflicting cart attributes and apps disabled. "
        "Amazon Pay and Venmo activated. "
        "Shop Promise enabled (1-3 days, $50). Craft theme published."
    )
