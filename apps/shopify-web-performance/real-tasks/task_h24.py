import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    apps = state.get("apps", [])
    errors = []

    # Apps with LCP >= 250 AND INP >= 40 should be disabled
    expected_disabled = {
        "Recharge": (450, 80),
        "Privy": (380, 95),
        "Hotjar": (350, 110),
        "Klaviyo": (320, 45),
        "TikTok": (260, 40),
    }

    for substring, (lcp, inp) in expected_disabled.items():
        app = next((a for a in apps if substring in a.get("name", "")), None)
        if app is None:
            errors.append(f"App containing '{substring}' not found.")
            continue
        if app.get("status") != "disabled":
            errors.append(f"App '{app.get('name')}' (LCP {lcp}, INP {inp}) status is '{app.get('status')}', expected 'disabled'.")
        if app.get("loadsOnStorefront") is not False:
            errors.append(f"App '{app.get('name')}' loadsOnStorefront is {app.get('loadsOnStorefront')}, expected False.")

    # Apps that DON'T meet both thresholds should remain active (or their original status)
    should_remain_active = ["Yotpo", "Bold Product", "Google Analytics", "Meta Pixel"]
    for substring in should_remain_active:
        app = next((a for a in apps if substring in a.get("name", "")), None)
        if app and app.get("status") != "active":
            errors.append(f"App '{app.get('name')}' should remain active but is '{app.get('status')}'.")

    if errors:
        return False, " ".join(errors)
    return True, "All apps with LCP >= 250ms and INP >= 40ms disabled; others remain active."
