# Task: Max security: security key 2FA, no remember password, no auto sign-in, all visibility nobody, no activity tracking.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()
    errors = []

    settings = state.get("accountSettings", {})
    login = settings.get("loginSettings", {})
    privacy = settings.get("privacySettings", {})

    # Login/security checks
    login_checks = {
        "twoFactorEnabled": True,
        "twoFactorMethod": "security_key",
        "rememberPassword": False,
        "autoSignIn": False,
    }
    for key, expected in login_checks.items():
        actual = login.get(key)
        if actual != expected:
            errors.append(f"loginSettings.{key}={actual}, expected {expected}")

    # Privacy checks
    privacy_checks = {
        "showProfilePhoto": "nobody",
        "showEmail": "nobody",
        "showPhone": "nobody",
        "activityTracking": False,
    }
    for key, expected in privacy_checks.items():
        actual = privacy.get(key)
        if actual != expected:
            errors.append(f"privacySettings.{key}={actual}, expected {expected}")

    if errors:
        return False, "; ".join(errors)
    return True, "Maximum security settings applied: security key 2FA, no auto-login, all visibility nobody, tracking off."
