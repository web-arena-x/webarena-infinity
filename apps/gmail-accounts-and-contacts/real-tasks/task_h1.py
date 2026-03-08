# Task: Remove all non-active delegates and add delegate backup@admin.com 'Backup Admin'.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()
    errors = []

    delegates = state.get("delegates", [])

    # Check no original non-active delegate remains (the new backup delegate will be pending)
    for d in delegates:
        if d.get("status") in ("pending", "expired") and d.get("email") != "backup@admin.com":
            errors.append(
                f"Delegate '{d.get('email')}' still has non-active status '{d.get('status')}'"
            )

    # Check backup@admin.com exists
    backup_found = False
    for d in delegates:
        if d.get("email") == "backup@admin.com":
            backup_found = True
            if d.get("name") != "Backup Admin":
                errors.append(
                    f"Backup delegate has name '{d.get('name')}' instead of 'Backup Admin'"
                )
            break

    if not backup_found:
        errors.append("Delegate with email 'backup@admin.com' not found")

    if errors:
        return False, "; ".join(errors)
    return True, "All non-active delegates removed and backup@admin.com added successfully."
