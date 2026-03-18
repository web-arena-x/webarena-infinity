import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify the food delivery Petrova was deleted, the other Petrova remains."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])

    # Diana Petrova works at Wolt (food delivery) — should be deleted
    # Elena Petrova works at Yandex — should remain
    diana_found = False
    elena_found = False

    for c in contacts:
        if c.get("lastName") == "Petrova":
            if c.get("firstName") == "Diana":
                diana_found = True
            elif c.get("firstName") == "Elena":
                elena_found = True

    if diana_found:
        return False, (
            "Diana Petrova (Wolt, food delivery) should have been deleted."
        )

    if not elena_found:
        return False, (
            "Elena Petrova (Yandex) should still exist — "
            "only the food delivery contact should have been deleted."
        )

    return True, (
        "Diana Petrova (Wolt/food delivery) deleted. "
        "Elena Petrova (Yandex) correctly preserved."
    )
