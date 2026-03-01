import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    errors = []

    # All originally-done todos should now be pending
    # todo_9 (issue_1), todo_10 (issue_36), todo_13 (epic_1), todo_15 (issue_10)
    restored_count = 0
    for todo in state.get("todos", []):
        if todo.get("id") in ("todo_9", "todo_10", "todo_15"):
            if todo.get("status") != "pending":
                errors.append(
                    f"Todo '{todo.get('id')}' should be pending (restored), "
                    f"got '{todo.get('status')}'."
                )
            else:
                restored_count += 1

    # Epic-referencing todos should be snoozed until March 15
    # todo_4 (epic_7) was already pending, todo_13 (epic_1) just restored
    epic_snoozed = 0
    for todo in state.get("todos", []):
        if todo.get("targetType") == "epic":
            if todo.get("status") != "snoozed":
                errors.append(
                    f"Epic todo '{todo.get('id')}' should be snoozed, "
                    f"got '{todo.get('status')}'."
                )
            elif todo.get("snoozedUntil") is None or "2026-03-15" not in todo.get("snoozedUntil", ""):
                errors.append(
                    f"Epic todo '{todo.get('id')}' snoozedUntil is "
                    f"'{todo.get('snoozedUntil')}', expected '2026-03-15'."
                )
            else:
                epic_snoozed += 1

    if epic_snoozed < 2:
        errors.append(
            f"Expected at least 2 epic todos snoozed, found {epic_snoozed}."
        )

    if errors:
        return False, " ".join(errors)

    return True, f"Done todos restored ({restored_count}); epic todos snoozed ({epic_snoozed}) until March 15."
