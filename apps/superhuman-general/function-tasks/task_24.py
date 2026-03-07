import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    pages = state.get("bookingPages", [])

    for page in pages:
        if (
            page.get("title") == "Strategy Session"
            and page.get("duration") == 60
            and page.get("location") == "Google Meet"
        ):
            return True, "Booking page 'Strategy Session' with 60-minute duration and Google Meet location found."

    return False, "Booking page 'Strategy Session' with duration 60 and location 'Google Meet' not found."
