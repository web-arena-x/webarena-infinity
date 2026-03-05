import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    apps = state.get("apps", [])
    recs = state.get("recommendations", [])
    tags = state.get("tagManagerTags", [])
    errors = []

    # Yotpo and Bold should be removed
    for name in ["Yotpo Loyalty & Rewards", "Bold Product Options"]:
        found = next((a for a in apps if a.get("name") == name), None)
        if found is not None:
            errors.append(f"App '{name}' should have been removed but still exists.")

    # All medium-priority recommendations should be resolved
    medium_recs = [
        "Reduce JavaScript execution on product pages",
        "Set explicit dimensions for product images",
        "Evaluate Privy pop-up timing",
        "Reduce homepage sections",
    ]
    for title in medium_recs:
        rec = next((r for r in recs if r.get("title") == title), None)
        if rec is None:
            errors.append(f"Recommendation '{title}' not found.")
        elif rec.get("status") != "resolved":
            errors.append(f"Recommendation '{title}' status is '{rec.get('status')}', expected 'resolved'.")

    # Microsoft Clarity should be deactivated
    clarity = next((t for t in tags if t.get("name") == "Microsoft Clarity"), None)
    if clarity is None:
        errors.append("Microsoft Clarity tag not found.")
    elif clarity.get("status") != "inactive":
        errors.append(f"Microsoft Clarity status is '{clarity.get('status')}', expected 'inactive'.")

    if errors:
        return False, " ".join(errors)
    return True, "Yotpo and Bold removed, all medium-priority recommendations resolved, Clarity deactivated."
