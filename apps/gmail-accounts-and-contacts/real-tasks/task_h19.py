# Task: All sync off, uncheck Google Sync ack, all notifications off, tracking off.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()
    errors = []

    settings = state.get("accountSettings", {})
    sync = settings.get("syncSettings", {})
    notifications = settings.get("notificationSettings", {})
    privacy = settings.get("privacySettings", {})

    # Sync settings checks
    sync_checks = {
        "contactsSync": False,
        "calendarSync": False,
        "emailSync": False,
        "googleSyncDeprecationAcknowledged": False,
    }
    for key, expected in sync_checks.items():
        actual = sync.get(key)
        if actual != expected:
            errors.append(f"syncSettings.{key}={actual}, expected {expected}")

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

    # Activity tracking
    if privacy.get("activityTracking") is not False:
        errors.append(
            f"privacySettings.activityTracking={privacy.get('activityTracking')}, expected False"
        )

    if errors:
        return False, "; ".join(errors)
    return True, "All sync off, Google Sync ack unchecked, all notifications off, tracking off."
