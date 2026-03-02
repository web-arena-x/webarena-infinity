import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    video_settings = state.get("practiceSettings", {}).get("videoSettings", {})

    chat_mode = video_settings.get("chatMode")
    if chat_mode != "host_only":
        return False, f"Chat mode is '{chat_mode}', expected 'host_only'."

    screen_sharing = video_settings.get("screenSharingPatients")
    if screen_sharing is not False:
        return False, f"Screen sharing for patients is {screen_sharing}, expected False."

    return True, "Video settings updated: chat mode set to host only, screen sharing disabled."
