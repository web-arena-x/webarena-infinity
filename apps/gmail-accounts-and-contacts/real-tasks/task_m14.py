# Task: Delete Dr. Patricia Nguyen and Mike Chen.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()
    errors = []

    contacts = state.get("contacts", [])

    patricia = next(
        (c for c in contacts if c.get("firstName") == "Dr. Patricia" and c.get("lastName") == "Nguyen"),
        None,
    )
    if patricia is not None:
        errors.append("Contact 'Dr. Patricia Nguyen' still exists (should have been deleted)")

    mike = next(
        (c for c in contacts if c.get("firstName") == "Mike" and c.get("lastName") == "Chen"),
        None,
    )
    if mike is not None:
        errors.append("Contact 'Mike Chen' still exists (should have been deleted)")

    if errors:
        return False, "; ".join(errors)
    return True, "Dr. Patricia Nguyen and Mike Chen deleted successfully."
