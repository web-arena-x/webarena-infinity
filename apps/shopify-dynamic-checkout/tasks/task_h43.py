import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    shop_promise = state.get("shopPromise", {})
    payment_methods = state.get("paymentMethods", [])
    cart_attributes = state.get("cartAttributes", [])

    # Check Shop Promise enabled with correct values
    if shop_promise.get("isActive") is not True:
        return False, f"Expected Shop Promise enabled, but got isActive={shop_promise.get('isActive')}."

    delivery = shop_promise.get("estimatedDeliveryDays", {})
    if delivery.get("min") != 2:
        return False, f"Expected min delivery days 2, got {delivery.get('min')}."
    if delivery.get("max") != 4:
        return False, f"Expected max delivery days 4, got {delivery.get('max')}."

    threshold = shop_promise.get("freeShippingThreshold")
    if threshold != 50 and threshold != 50.0:
        return False, f"Expected free shipping threshold $50, got ${threshold}."

    # Check payment methods that require setup are deactivated
    for m in payment_methods:
        if m.get("type") == "accelerated" and m.get("requiresSetup") is True:
            if m.get("isActive") is not False:
                return False, (
                    f"Expected '{m['name']}' (requires setup) to be deactivated, "
                    f"but got isActive={m.get('isActive')}."
                )

    # Check terms and conditions is active
    terms = next((a for a in cart_attributes if a.get("name") == "Terms and conditions"), None)
    if terms is None:
        return False, "Terms and conditions cart attribute not found."
    if terms.get("isActive") is not True:
        return False, f"Expected terms and conditions enabled, got isActive={terms.get('isActive')}."

    return True, (
        "Shop Promise enabled (2-4 days, $50 threshold), "
        "setup-required payment methods deactivated, "
        "terms and conditions enabled."
    )
