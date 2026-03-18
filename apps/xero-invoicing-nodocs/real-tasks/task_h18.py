import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Enable late penalties at 3% weekly, default due date terms to 14, branding Bold Corporate."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    settings = state.get("settings", {})
    errors = []

    # Check latePenaltyEnabled
    enabled = settings.get("latePenaltyEnabled")
    if enabled is not True:
        errors.append(f"settings.latePenaltyEnabled is {enabled}, expected True")

    # Check latePenaltyRate == 3
    rate = settings.get("latePenaltyRate")
    if rate is None or abs(float(rate) - 3.0) > 0.01:
        errors.append(f"settings.latePenaltyRate is {rate}, expected 3")

    # Check latePenaltyFrequency == 'weekly'
    freq = settings.get("latePenaltyFrequency")
    if freq != "weekly":
        errors.append(f"settings.latePenaltyFrequency is '{freq}', expected 'weekly'")

    # Check defaultDueDateTerms == '14'
    terms = settings.get("defaultDueDateTerms")
    if str(terms) != "14":
        errors.append(f"settings.defaultDueDateTerms is '{terms}', expected '14'")

    # Check defaultBrandingThemeId == 'theme_4'
    theme = settings.get("defaultBrandingThemeId")
    if theme != "theme_4":
        errors.append(f"settings.defaultBrandingThemeId is '{theme}', expected 'theme_4' (Bold Corporate)")

    if errors:
        return False, "; ".join(errors)

    return True, "Settings updated: late penalties 3% weekly, due date terms 14, branding Bold Corporate"
