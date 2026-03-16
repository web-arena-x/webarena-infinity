"""
Task: Delete the Heading/Display text style.
Verify: No style named "Heading/Display" exists in textStyles.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    text_styles = state.get("textStyles", [])
    for style in text_styles:
        if style.get("name") == "Heading/Display":
            return False, "Text style 'Heading/Display' still exists in textStyles."

    return True, "Text style 'Heading/Display' has been successfully deleted."
