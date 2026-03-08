# Task: Remove all delegates, disable delegate notifications, unlink all linked services.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()
    errors = []

    # Delegates array should be empty
    delegates = state.get("delegates", [])
    if len(delegates) > 0:
        emails = [d.get("email", "unknown") for d in delegates]
        errors.append(f"Delegates still exist: {', '.join(emails)}")

    # delegateActivity should be false
    settings = state.get("accountSettings", {})
    notifications = settings.get("notificationSettings", {})
    if notifications.get("delegateActivity") is not False:
        errors.append(
            f"delegateActivity={notifications.get('delegateActivity')}, expected False"
        )

    # All linked services should be unlinked
    linked_services = state.get("linkedServices", [])
    services_to_check = {
        "svc_1": "Google Search",
        "svc_2": "YouTube",
        "svc_4": "Google Play",
        "svc_5": "Chrome",
        "svc_7": "Google Maps",
    }
    svc_map = {s.get("id"): s for s in linked_services}
    for svc_id, name in services_to_check.items():
        svc = svc_map.get(svc_id)
        if svc and svc.get("isLinked"):
            errors.append(f"{name} is still linked")

    if errors:
        return False, "; ".join(errors)
    return True, "All delegates removed, delegate notifications disabled, all linked services unlinked."
