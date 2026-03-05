import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    apps = state.get("apps", [])
    tags = state.get("tagManagerTags", [])
    errors = []

    # Moderate-impact apps with >= 2 scripts should be disabled
    expected_disabled = ["Klaviyo", "Google Analytics", "Meta Pixel", "Yotpo", "Bold Product", "TikTok"]
    for substring in expected_disabled:
        app = next((a for a in apps if substring in a.get("name", "")), None)
        if app is None:
            errors.append(f"App containing '{substring}' not found.")
            continue
        if app.get("status") != "disabled":
            errors.append(f"App '{app.get('name')}' status is '{app.get('status')}', expected 'disabled'.")
        if app.get("loadsOnStorefront") is not False:
            errors.append(f"App '{app.get('name')}' loadsOnStorefront is {app.get('loadsOnStorefront')}, expected False.")

    # Product-pages only tag (Affirm Messaging) should be removed
    affirm = next((t for t in tags if t.get("name") == "Affirm Messaging"), None)
    if affirm is not None:
        errors.append("Affirm Messaging tag should have been removed but still exists.")

    if errors:
        return False, " ".join(errors)
    return True, "All moderate-impact apps with 2+ scripts disabled and product-pages tag removed."
