import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    apps = state.get("apps", [])
    recs = state.get("recommendations", [])
    errors = []

    # Hotjar has the worst INP impact (110ms) — it should be disabled
    hotjar = next((a for a in apps if "Hotjar" in a.get("name", "")), None)
    if hotjar is None:
        errors.append("Could not find Hotjar app.")
    else:
        if hotjar.get("status") != "disabled":
            errors.append(f"Hotjar status is '{hotjar.get('status')}', expected 'disabled'.")
        if hotjar.get("loadsOnStorefront") is not False:
            errors.append(f"Hotjar loadsOnStorefront is {hotjar.get('loadsOnStorefront')}, expected False.")

    # Recommendation about JavaScript execution should be resolved
    rec = next((r for r in recs if r.get("title") == "Reduce JavaScript execution on product pages"), None)
    if rec is None:
        errors.append("Could not find recommendation 'Reduce JavaScript execution on product pages'.")
    elif rec.get("status") != "resolved":
        errors.append(f"Recommendation status is '{rec.get('status')}', expected 'resolved'.")

    if errors:
        return False, " ".join(errors)
    return True, "Worst INP app (Hotjar, 110ms) disabled and JavaScript execution recommendation resolved."
