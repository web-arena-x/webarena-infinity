import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    tags = state.get("tagManagerTags", [])
    errors = []

    # Active advertising tags that fire on all-pages should be deactivated
    for tag_name in ["Meta Pixel", "TikTok Pixel"]:
        tag = next((t for t in tags if t.get("name") == tag_name), None)
        if tag is None:
            errors.append(f"Tag '{tag_name}' not found.")
        elif tag.get("status") != "inactive":
            errors.append(f"Tag '{tag_name}' status is '{tag.get('status')}', expected 'inactive'.")

    # Checkout-only advertising tag should remain active
    google_ads = next((t for t in tags if t.get("name") == "Google Ads Conversion"), None)
    if google_ads is None:
        errors.append("Tag 'Google Ads Conversion' not found.")
    elif google_ads.get("status") != "active":
        errors.append(f"Google Ads Conversion status is '{google_ads.get('status')}', expected 'active'.")

    # All originally inactive tags should be removed
    for tag_name in ["Pinterest Tag", "Snapchat Pixel", "Lucky Orange"]:
        found = next((t for t in tags if t.get("name") == tag_name), None)
        if found is not None:
            errors.append(f"Inactive tag '{tag_name}' should have been removed.")

    if errors:
        return False, " ".join(errors)
    return True, "All-pages advertising tags deactivated, checkout-only kept active, inactive tags removed."
