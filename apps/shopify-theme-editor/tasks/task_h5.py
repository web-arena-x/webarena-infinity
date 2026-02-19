import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify TikTok set, LinkedIn set, and Pinterest cleared in social links."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = next((ts for ts in state["themeSettings"] if ts.get("themeId") == 1), None)
    if not settings:
        return False, "Theme settings for Dawn not found."

    social = settings.get("socialLinks", {})

    tiktok = social.get("tiktok")
    if tiktok != "https://tiktok.com/@northwindtraders":
        return False, f"TikTok URL is '{tiktok}', expected 'https://tiktok.com/@northwindtraders'."

    linkedin = social.get("linkedin")
    if linkedin != "https://linkedin.com/company/northwindtraders":
        return False, f"LinkedIn URL is '{linkedin}', expected 'https://linkedin.com/company/northwindtraders'."

    pinterest = social.get("pinterest")
    if pinterest != "":
        return False, f"Pinterest URL is '{pinterest}', expected empty string."

    return True, "TikTok and LinkedIn URLs set, Pinterest cleared."
