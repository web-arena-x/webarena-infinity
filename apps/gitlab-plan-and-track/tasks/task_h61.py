import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # The originally-pending todos referencing v4.0 milestone issues:
    # todo_1 -> issue_17 (Safari bug, ms_1)
    # todo_2 -> issue_18 (Email notifications, ms_1)
    # todo_3 -> issue_4 (User settings migration, ms_1)
    # todo_5 -> issue_22 (Dark mode, ms_1)
    expected_todo_ids = ["todo_1", "todo_2", "todo_3", "todo_5"]

    errors = []
    snoozed_count = 0
    for todo in state.get("todos", []):
        if todo.get("id") in expected_todo_ids:
            if todo.get("status") != "snoozed":
                errors.append(
                    f"Todo '{todo.get('id')}' has status '{todo.get('status')}', "
                    f"expected 'snoozed'."
                )
            elif todo.get("snoozedUntil") is None or "2026-03-10" not in todo.get("snoozedUntil", ""):
                errors.append(
                    f"Todo '{todo.get('id')}' snoozedUntil is '{todo.get('snoozedUntil')}', "
                    f"expected date containing '2026-03-10'."
                )
            else:
                snoozed_count += 1

    if snoozed_count < 4:
        errors.append(
            f"Expected 4 todos snoozed for v4.0 issues, found {snoozed_count}."
        )

    if errors:
        return False, " ".join(errors)

    return True, f"All {snoozed_count} pending todos referencing v4.0 issues snoozed until March 10."
