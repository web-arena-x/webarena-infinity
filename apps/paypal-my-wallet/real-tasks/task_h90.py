import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    offers = state.get("offers", [])
    offer_map = {o.get("merchantName"): o for o in offers}

    # After: save available offers with maxCashback >= $15, then unsave saved fixed-type offers.
    # Expected final states:
    expected = {
        "Starbucks": "saved",      # was saved, percent -> stays saved
        "Uber": "available",        # was saved, fixed -> unsaved
        "DoorDash": "saved",        # was available, maxCB=15 >= 15 -> saved
        "Nike": "saved",            # was available, maxCB=50 >= 15 -> saved
        "Target": "saved",          # was available, maxCB=25 >= 15 -> saved
        "Spotify": "available",     # was saved, fixed -> unsaved
        "Walmart": "saved",         # was available, maxCB=20 >= 15 -> saved
        "Lyft": "saved",            # was available, maxCB=15 >= 15 -> saved
        "Amazon": "saved",          # was available, maxCB=40 >= 15 -> saved
        "Chipotle": "available",    # was available, maxCB=2 < 15 -> stays available
    }

    for merchant, expected_status in expected.items():
        offer = offer_map.get(merchant)
        if offer is None:
            errors.append(f"Offer for '{merchant}' not found.")
        elif offer.get("status") != expected_status:
            errors.append(
                f"Offer '{merchant}' has status '{offer.get('status')}', "
                f"expected '{expected_status}'."
            )

    if errors:
        return False, " ".join(errors)
    return True, "Saved high-cashback available offers and unsaved fixed-type saved offers."
