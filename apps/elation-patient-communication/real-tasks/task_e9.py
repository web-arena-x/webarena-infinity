import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    practice_settings = state.get("practiceSettings", {})
    video_settings = practice_settings.get("videoSettings", {})
    audio_notification = video_settings.get("waitingRoomAudioNotification")

    if audio_notification is False:
        return True, "Waiting room audio notification has been disabled."
    else:
        return False, f"waitingRoomAudioNotification is {audio_notification}, expected False."
