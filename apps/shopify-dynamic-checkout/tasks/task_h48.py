import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    themes = state.get("themes", [])
    templates = state.get("templates", [])
    payment_methods = state.get("paymentMethods", [])

    ride = next((t for t in themes if t.get("name") == "Ride"), None)
    if ride is None:
        return False, "Theme 'Ride' not found."

    # Check Ride is published
    if ride.get("role") != "main":
        return False, f"Expected Ride to be published (main), but got role='{ride.get('role')}'."

    # Check Amazon Pay active
    amazon = next((m for m in payment_methods if m.get("name") == "Amazon Pay"), None)
    if amazon is None:
        return False, "Amazon Pay not found."
    if amazon.get("isActive") is not True:
        return False, f"Expected Amazon Pay active, got isActive={amazon.get('isActive')}."

    # Check Venmo active
    venmo = next((m for m in payment_methods if m.get("name") == "Venmo"), None)
    if venmo is None:
        return False, "Venmo not found."
    if venmo.get("isActive") is not True:
        return False, f"Expected Venmo active, got isActive={venmo.get('isActive')}."

    # Check Ride default template has checkout enabled
    ride_default = next(
        (t for t in templates if t.get("themeId") == ride["id"] and t.get("isDefault") is True),
        None
    )
    if ride_default is None:
        return False, "Ride's default template not found."
    if ride_default.get("showAcceleratedCheckout") is not True:
        return False, (
            f"Expected Ride default template checkout enabled, "
            f"got {ride_default.get('showAcceleratedCheckout')}."
        )

    # Check Ride button font
    ride_typo = ride.get("settings", {}).get("typography", {})
    if ride_typo.get("buttonFont") != "Oswald":
        return False, (
            f"Expected Ride button font 'Oswald', got '{ride_typo.get('buttonFont')}'."
        )

    return True, (
        "Amazon Pay and Venmo activated. Ride theme published with "
        "checkout enabled on default template and button font set to Oswald."
    )
