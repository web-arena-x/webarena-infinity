# Task: All visibility to Nobody, disable tracking, turn off all notifications.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()
    errors = []

    settings = state.get("accountSettings", {})
    privacy = settings.get("privacySettings", {})
    notifications = settings.get("notificationSettings", {})

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

    # Notification checks
    notification_checks = {
        "delegateActivity": False,
        "contactChanges": False,
        "securityAlerts": False,
        "linkedServiceUpdates": False,
    }
    for key, expected in notification_checks.items():
        actual = notifications.get(key)
        if actual != expected:
            errors.append(
                f"notificationSettings.{key}={actual}, expected {expected}"
            )

    if errors:
        return False, "; ".join(errors)
    return True, "All visibility set to nobody, tracking disabled, all notifications off."
