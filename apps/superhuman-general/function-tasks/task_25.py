import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    pages = state.get("bookingPages", [])

    for page in pages:
        if page.get("title") == "Quick Sync":
            if page.get("isActive") is True:
                return True, "Booking page 'Quick Sync' is now active."
            else:
                return False, f"Booking page 'Quick Sync' isActive is {page.get('isActive')}, expected True."

    return False, "Booking page 'Quick Sync' not found."
