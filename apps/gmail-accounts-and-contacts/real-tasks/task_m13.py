# Task: Profile photo and email visibility to Nobody.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()
    errors = []

    privacy = state.get("accountSettings", {}).get("privacySettings", {})

    show_photo = privacy.get("showProfilePhoto")
    if show_photo != "nobody":
        errors.append(f"Expected showProfilePhoto to be 'nobody', got '{show_photo}'")

    show_email = privacy.get("showEmail")
    if show_email != "nobody":
        errors.append(f"Expected showEmail to be 'nobody', got '{show_email}'")

    if errors:
        return False, "; ".join(errors)
    return True, "Profile photo and email visibility set to 'nobody'."
