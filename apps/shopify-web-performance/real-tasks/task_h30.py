import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    tags = state.get("tagManagerTags", [])
    apps = state.get("apps", [])
    recs = state.get("recommendations", [])
    errors = []

    # GA4 tag should still exist and be active
    ga4 = next((t for t in tags if t.get("name") == "Google Analytics 4"), None)
    if ga4 is None:
        errors.append("Google Analytics 4 tag should still exist but was not found.")
    elif ga4.get("status") != "active":
        errors.append(f"Google Analytics 4 status is '{ga4.get('status')}', expected 'active'.")

    # All other all-pages tags should be removed
    removed_all_pages = ["Meta Pixel", "TikTok Pixel", "Hotjar Tracking",
                         "Pinterest Tag", "Snapchat Pixel", "Microsoft Clarity", "Lucky Orange"]
    for tag_name in removed_all_pages:
        found = next((t for t in tags if t.get("name") == tag_name), None)
        if found is not None:
            errors.append(f"All-pages tag '{tag_name}' should have been removed.")

    # Privy should be disabled
    privy = next((a for a in apps if "Privy" in a.get("name", "")), None)
    if privy is None:
        errors.append("Could not find Privy app.")
    else:
        if privy.get("status") != "disabled":
            errors.append(f"Privy status is '{privy.get('status')}', expected 'disabled'.")
        if privy.get("loadsOnStorefront") is not False:
            errors.append(f"Privy loadsOnStorefront is {privy.get('loadsOnStorefront')}, expected False.")

    # Privy banner rec should be resolved
    rec = next((r for r in recs if r.get("title") == "Reserve space for Privy pop-up banner"), None)
    if rec is None:
        errors.append("Could not find recommendation about Privy pop-up banner.")
    elif rec.get("status") != "resolved":
        errors.append(f"Privy banner recommendation status is '{rec.get('status')}', expected 'resolved'.")

    if errors:
        return False, " ".join(errors)
    return True, "All-pages tags removed (except GA4), Privy disabled, banner recommendation resolved."
