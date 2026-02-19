import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify that 'Convert text emoticons into emojis' is enabled."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    prefs = state.get("preferences", {})
    emoticons = prefs.get("convertTextEmoticons")

    if emoticons is not True:
        return False, f"Expected convertTextEmoticons=true, got {emoticons}."

    return True, "'Convert text emoticons into emojis' is enabled."
