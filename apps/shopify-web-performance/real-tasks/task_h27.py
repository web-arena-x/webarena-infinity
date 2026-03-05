import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    apps = state.get("apps", [])
    settings = state.get("settings", {})
    errors = []

    # All non-Shopify storefront-loading apps should be disabled
    non_shopify_storefront = [
        "Klaviyo", "Judge.me", "Google Analytics", "Meta Pixel",
        "Recharge", "Privy", "Yotpo", "Hotjar", "Bold Product",
        "TikTok", "Back in Stock"
    ]
    for substring in non_shopify_storefront:
        app = next((a for a in apps if substring in a.get("name", "")), None)
        if app is None:
            errors.append(f"App containing '{substring}' not found.")
            continue
        if app.get("status") != "disabled":
            errors.append(f"App '{app.get('name')}' status is '{app.get('status')}', expected 'disabled'.")
        if app.get("loadsOnStorefront") is not False:
            errors.append(f"App '{app.get('name')}' loadsOnStorefront is {app.get('loadsOnStorefront')}, expected False.")

    # Shopify Inbox should remain active
    inbox = next((a for a in apps if "Shopify Inbox" in a.get("name", "")), None)
    if inbox is None:
        errors.append("Could not find Shopify Inbox app.")
    elif inbox.get("status") != "active":
        errors.append(f"Shopify Inbox status is '{inbox.get('status')}', expected 'active' (Shopify app should be exempt).")

    # Comparison should be off
    if settings.get("comparisonEnabled") is not False:
        errors.append(f"comparisonEnabled is {settings.get('comparisonEnabled')}, expected False.")

    if errors:
        return False, " ".join(errors)
    return True, "All non-Shopify storefront apps disabled, Shopify Inbox kept, comparison off."
