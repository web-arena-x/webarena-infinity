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

    # All active analytics tags should be deactivated
    analytics_tags = ["Google Analytics 4", "Hotjar Tracking", "Microsoft Clarity"]
    for tag_name in analytics_tags:
        tag = next((t for t in tags if t.get("name") == tag_name), None)
        if tag is None:
            errors.append(f"Tag '{tag_name}' not found.")
        elif tag.get("status") != "inactive":
            errors.append(f"Tag '{tag_name}' status is '{tag.get('status')}', expected 'inactive'.")

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

    # Report percentile should be P90
    if settings.get("reportPercentile") != "p90":
        errors.append(f"reportPercentile is '{settings.get('reportPercentile')}', expected 'p90'.")

    # Date grouping should be weekly
    if settings.get("dateGrouping") != "weekly":
        errors.append(f"dateGrouping is '{settings.get('dateGrouping')}', expected 'weekly'.")

    if errors:
        return False, " ".join(errors)
    return True, "Analytics tags deactivated, analytics apps disabled, P90 and weekly reporting set."
