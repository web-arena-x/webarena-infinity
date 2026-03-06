import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that all unacknowledged reminders have been acknowledged."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    reminders = state.get("reminders", [])

    # In seed data, rem_3 is already acknowledged.
    # All others (rem_1, rem_2, rem_4, rem_5, rem_6, rem_7, rem_8, rem_9, rem_10)
    # should now be acknowledged.
    not_acknowledged = []
    for rem in reminders:
        if not rem.get("acknowledged"):
            not_acknowledged.append(
                f"{rem.get('id')} ({rem.get('description', 'no description')[:60]})"
            )

    if not_acknowledged:
        return False, (
            f"The following reminders are still not acknowledged: "
            f"{'; '.join(not_acknowledged)}"
        )

    return True, "All reminders in the system have been acknowledged"
