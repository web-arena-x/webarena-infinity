import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    todos = state.get("todos", [])

    # Check that no todos have status 'done'
    done_todos = [t for t in todos if t.get("status") == "done"]
    if done_todos:
        return False, f"Found {len(done_todos)} todo(s) still in 'done' status, expected all restored to pending."

    # Check that no todos have status 'snoozed'
    snoozed_todos = [t for t in todos if t.get("status") == "snoozed"]
    if snoozed_todos:
        return False, f"Found {len(snoozed_todos)} todo(s) still in 'snoozed' status, expected snooze removed."

    # All todos should be 'pending'
    non_pending = [t for t in todos if t.get("status") != "pending"]
    if non_pending:
        return False, f"Found {len(non_pending)} todo(s) that are not 'pending'."

    # Verify snoozedUntil is cleared for all
    still_snoozed = [t for t in todos if t.get("snoozedUntil") is not None]
    if still_snoozed:
        return False, f"Found {len(still_snoozed)} todo(s) that still have a snoozedUntil value."

    return True, f"All {len(todos)} todos are in pending status with no snooze dates."
