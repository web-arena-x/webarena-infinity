import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    apps = state.get("apps", [])
    tags = state.get("tagManagerTags", [])
    recs = state.get("recommendations", [])
    settings = state.get("settings", {})
    errors = []

    # High-impact apps disabled
    for substring in ["Recharge", "Privy", "Hotjar"]:
        app = next((a for a in apps if substring in a.get("name", "")), None)
        if app is None:
            errors.append(f"App containing '{substring}' not found.")
            continue
        if app.get("status") != "disabled":
            errors.append(f"App '{app.get('name')}' status is '{app.get('status')}', expected 'disabled'.")
        if app.get("loadsOnStorefront") is not False:
            errors.append(f"App '{app.get('name')}' loadsOnStorefront is {app.get('loadsOnStorefront')}, expected False.")

    # Inactive tags removed
    for tag_name in ["Pinterest Tag", "Snapchat Pixel", "Lucky Orange"]:
        found = next((t for t in tags if t.get("name") == tag_name), None)
        if found is not None:
            errors.append(f"Inactive tag '{tag_name}' should have been removed.")

    # High-priority open recs resolved
    for title in [
        "Reduce the impact of third-party scripts",
        "Optimize large hero images on homepage",
        "Reserve space for Privy pop-up banner",
    ]:
        rec = next((r for r in recs if r.get("title") == title), None)
        if rec is None:
            errors.append(f"Recommendation '{title}' not found.")
        elif rec.get("status") != "resolved":
            errors.append(f"Recommendation '{title}' status is '{rec.get('status')}', expected 'resolved'.")

    # Dashboard settings
    if settings.get("dateRange") != "last_30_days":
        errors.append(f"dateRange is '{settings.get('dateRange')}', expected 'last_30_days'.")
    if settings.get("deviceFilter") != "mobile":
        errors.append(f"deviceFilter is '{settings.get('deviceFilter')}', expected 'mobile'.")
    if settings.get("reportPercentile") != "p95":
        errors.append(f"reportPercentile is '{settings.get('reportPercentile')}', expected 'p95'.")
    if settings.get("comparisonEnabled") is not False:
        errors.append(f"comparisonEnabled is {settings.get('comparisonEnabled')}, expected False.")

    if errors:
        return False, " ".join(errors)
    return True, "Audit prep complete: high-impact apps disabled, inactive tags removed, high-priority recs resolved, dashboard configured."
