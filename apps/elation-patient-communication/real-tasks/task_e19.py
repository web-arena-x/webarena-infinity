import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that the waiting room audio notification for telehealth is disabled."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    practice_settings = state.get("practiceSettings", {})
    video_settings = practice_settings.get("videoSettings", {})
    audio_notification = video_settings.get("waitingRoomAudioNotification")

    if audio_notification is not False:
        return False, f"practiceSettings.videoSettings.waitingRoomAudioNotification is {audio_notification}, expected False"

    return True, "Waiting room audio notification for telehealth is disabled"
