import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    booking_pages = state.get("bookingPages", [])

    for page in booking_pages:
        if page.get("title") == "Chat with Alex":
            if page.get("isActive") is False:
                return True, "Booking page 'Chat with Alex' is now inactive."
            return False, f"Booking page 'Chat with Alex' is still active (isActive={page.get('isActive')})."

    return False, "No booking page titled 'Chat with Alex' found."
