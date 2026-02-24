import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify Facebook and YouTube social media links."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    social = state.get("themeSettings", {}).get("socialMedia", {})

    fb = social.get("facebook")
    if fb != "https://facebook.com/mystore":
        return False, f"Expected facebook='https://facebook.com/mystore', got '{fb}'."

    yt = social.get("youtube")
    if yt != "https://youtube.com/@mystore":
        return False, f"Expected youtube='https://youtube.com/@mystore', got '{yt}'."

    return True, "Facebook and YouTube links set correctly."
