import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    apps = state.get("apps", [])
    tags = state.get("tagManagerTags", [])
    settings = state.get("settings", {})
    errors = []

    # Non-analytics apps with >= 2 scripts should be disabled
    expected_disabled = ["Klaviyo", "Recharge", "Privy", "Yotpo", "Bold Product", "TikTok"]
    for substring in expected_disabled:
        app = next((a for a in apps if substring in a.get("name", "")), None)
        if app is None:
            errors.append(f"App containing '{substring}' not found.")
            continue
        if app.get("status") != "disabled":
            errors.append(f"App '{app.get('name')}' status is '{app.get('status')}', expected 'disabled'.")
        if app.get("loadsOnStorefront") is not False:
            errors.append(f"App '{app.get('name')}' loadsOnStorefront is {app.get('loadsOnStorefront')}, expected False.")

    # Analytics apps with >= 2 scripts should remain active
    analytics_apps = ["Google Analytics (GA4)", "Meta Pixel & Conversions API", "Hotjar Heatmaps & Recordings"]
    for name in analytics_apps:
        app = next((a for a in apps if a.get("name") == name), None)
        if app and app.get("status") != "active":
            errors.append(f"Analytics app '{name}' should remain active but is '{app.get('status')}'.")

    # Affirm Messaging (payments tag) should be removed
    affirm = next((t for t in tags if t.get("name") == "Affirm Messaging"), None)
    if affirm is not None:
        errors.append("Affirm Messaging tag should have been removed.")

    # INP threshold should be 100
    alerts = settings.get("performanceAlerts", {})
    if alerts.get("inpThreshold") != 100:
        errors.append(f"inpThreshold is {alerts.get('inpThreshold')}, expected 100.")

    if errors:
        return False, " ".join(errors)
    return True, "Non-analytics apps with 2+ scripts disabled, analytics kept, Affirm removed, INP threshold set to 100."
