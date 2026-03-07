import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    pages = state.get("bookingPages", [])

    for page in pages:
        if page.get("title") == "Product Demo":
            return False, "Booking page 'Product Demo' still exists."

    return True, "Booking page 'Product Demo' has been successfully deleted."
