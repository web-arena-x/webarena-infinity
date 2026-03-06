import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that screen sharing for patients during video visits is turned off."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    practice_settings = state.get("practiceSettings", {})
    video_settings = practice_settings.get("videoSettings", {})
    screen_sharing = video_settings.get("screenSharingPatients")

    if screen_sharing is not False:
        return False, f"practiceSettings.videoSettings.screenSharingPatients is {screen_sharing}, expected False"

    return True, "Screen sharing for patients during video visits is disabled"
