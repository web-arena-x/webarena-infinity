import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify 5 social media links all set to greenleaf URLs."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    social = state.get("themeSettings", {}).get("socialMedia", {})

    expected = {
        "facebook": "https://facebook.com/greenleaf",
        "instagram": "https://instagram.com/greenleaf",
        "twitter": "https://twitter.com/greenleaf",
        "pinterest": "https://pinterest.com/greenleaf",
        "youtube": "https://youtube.com/greenleaf",
    }

    for key, url in expected.items():
        val = social.get(key)
        if val != url:
            return False, f"Expected {key}='{url}', got '{val}'."

    return True, "All 5 social media links set to greenleaf URLs."
