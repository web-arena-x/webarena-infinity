import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    apps = state.get("apps", [])
    tags = state.get("tagManagerTags", [])
    errors = []

    # All analytics apps should be disabled
    analytics_apps = ["Google Analytics (GA4)", "Meta Pixel & Conversions API", "Hotjar Heatmaps & Recordings"]
    for name in analytics_apps:
        app = next((a for a in apps if a.get("name") == name), None)
        if app is None:
            errors.append(f"App '{name}' not found.")
            continue
        if app.get("status") != "disabled":
            errors.append(f"App '{name}' status is '{app.get('status')}', expected 'disabled'.")
        if app.get("loadsOnStorefront") is not False:
            errors.append(f"App '{name}' loadsOnStorefront is {app.get('loadsOnStorefront')}, expected False.")

    # Corresponding tags should be removed
    removed_tags = ["Google Analytics 4", "Meta Pixel", "Hotjar Tracking"]
    for tag_name in removed_tags:
        found = next((t for t in tags if t.get("name") == tag_name), None)
        if found is not None:
            errors.append(f"Tag '{tag_name}' should have been removed but still exists.")

    if errors:
        return False, " ".join(errors)
    return True, "All analytics apps disabled and their corresponding tracking tags removed."
