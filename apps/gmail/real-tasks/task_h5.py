"""
Task H5: Trash all promotional emails from Amazon, Nike, and REI.
Verify: Emails 44, 52, 55 all have isTrashed=True.
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    emails = state.get("emails", [])

    target_ids = {
        44: "Amazon (Your recommendations: Tech deals of the week)",
        52: "Nike (Members Week: 25% off everything)",
        55: "REI (Garage Sale: Up to 50% off)",
    }

    not_found = []
    not_trashed = []

    for eid, desc in target_ids.items():
        email = next((e for e in emails if e.get("id") == eid), None)
        if email is None:
            not_found.append(f"id={eid} ({desc})")
            continue
        if not email.get("isTrashed"):
            not_trashed.append(f"id={eid} ({desc})")

    errors = []
    if not_found:
        errors.append(f"Emails not found: {', '.join(not_found)}")
    if not_trashed:
        errors.append(f"Emails not trashed: {', '.join(not_trashed)}")

    if errors:
        return False, "; ".join(errors)

    return True, "All promotional emails from Amazon, Nike, and REI are trashed."
