import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    apps = state.get("apps", [])
    tags = state.get("tagManagerTags", [])
    recs = state.get("recommendations", [])
    errors = []

    # Marketing apps should be removed
    for substring in ["Klaviyo", "Privy", "Back in Stock"]:
        found = next((a for a in apps if substring in a.get("name", "")), None)
        if found is not None:
            errors.append(f"Marketing app containing '{substring}' should have been removed but still exists.")

    # TikTok Pixel and Meta Pixel tags should be removed
    for tag_name in ["TikTok Pixel", "Meta Pixel"]:
        found = next((t for t in tags if t.get("name") == tag_name), None)
        if found is not None:
            errors.append(f"Tag '{tag_name}' should have been removed.")

    # Privy recommendations should be dismissed
    privy_recs = ["Evaluate Privy pop-up timing", "Reserve space for Privy pop-up banner"]
    for title in privy_recs:
        rec = next((r for r in recs if r.get("title") == title), None)
        if rec is None:
            errors.append(f"Recommendation '{title}' not found.")
        elif rec.get("status") != "dismissed":
            errors.append(f"Recommendation '{title}' status is '{rec.get('status')}', expected 'dismissed'.")

    if errors:
        return False, " ".join(errors)
    return True, "Marketing apps uninstalled, TikTok/Meta tags removed, Privy recommendations dismissed."
