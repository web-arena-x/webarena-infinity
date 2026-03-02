import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    shop_promise = state.get("shopPromise", {})
    apps = state.get("installedApps", [])

    # Count apps that conflict with checkout
    conflicting_count = sum(1 for a in apps if a.get("conflictsWithCheckout") is True)

    # Check Shop Promise enabled
    if shop_promise.get("isActive") is not True:
        return False, f"Expected Shop Promise enabled, got isActive={shop_promise.get('isActive')}."

    delivery = shop_promise.get("estimatedDeliveryDays", {})
    expected_min = conflicting_count
    expected_max = conflicting_count * 2

    if delivery.get("min") != expected_min:
        return False, (
            f"Expected min delivery days {expected_min} (= {conflicting_count} conflicting apps), "
            f"got {delivery.get('min')}."
        )
    if delivery.get("max") != expected_max:
        return False, (
            f"Expected max delivery days {expected_max} (= 2 × {conflicting_count} conflicting apps), "
            f"got {delivery.get('max')}."
        )

    threshold = shop_promise.get("freeShippingThreshold")
    if threshold != 80 and threshold != 80.0:
        return False, f"Expected free shipping threshold $80, got ${threshold}."

    return True, (
        f"Shop Promise enabled with {expected_min}-{expected_max} day delivery "
        f"(based on {conflicting_count} conflicting apps) and $80 threshold."
    )
