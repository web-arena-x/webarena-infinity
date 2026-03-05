import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Update Dr. Chen's telehealth instructions and change video chat mode."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Check Dr. Chen's telehealth instructions
    providers = state.get("providers", [])
    prov_1 = next((p for p in providers if p.get("id") == "prov_1"), None)
    if prov_1 is None:
        return False, "Provider prov_1 (Dr. Chen) not found."

    expected_url = "https://zoom.us/j/newlink123"
    instructions = prov_1.get("virtualVisitInstructions", "")
    if expected_url not in instructions:
        return False, (
            f"Dr. Chen's telehealth instructions do not contain "
            f"'{expected_url}'. Current: '{instructions[:100]}...'"
        )

    # Check video chat mode
    video_settings = state.get("practiceSettings", {}).get("videoSettings", {})
    chat_mode = video_settings.get("chatMode")
    if chat_mode != "everyone_in_waiting_room":
        return False, (
            f"Video chat mode is '{chat_mode}', expected "
            f"'everyone_in_waiting_room'."
        )

    return True, (
        "Dr. Chen's telehealth instructions updated and chat mode "
        "changed to 'Everyone in Waiting Room'."
    )
