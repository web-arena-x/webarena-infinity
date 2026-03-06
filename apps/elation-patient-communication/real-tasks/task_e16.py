import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that the video chat mode is changed to Host Only."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    practice_settings = state.get("practiceSettings", {})
    video_settings = practice_settings.get("videoSettings", {})
    chat_mode = video_settings.get("chatMode")

    if chat_mode != "host_only":
        return False, f"practiceSettings.videoSettings.chatMode is '{chat_mode}', expected 'host_only'"

    return True, "Video chat mode is set to Host Only"
