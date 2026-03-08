import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    users = state.get("firmUsers", [])
    matters = state.get("matters", [])

    # Identify paralegals
    paralegals = [u for u in users if u.get("role") == "Paralegal"]
    if not paralegals:
        return False, "No paralegals found in firm users."

    # Count open matters per paralegal as responsible staff
    staff_counts = {}
    for u in paralegals:
        uid = u.get("id")
        count = sum(
            1 for m in matters
            if m.get("responsibleStaffId") == uid and m.get("status") == "Open"
        )
        staff_counts[uid] = count

    # Find the paralegal with the most open matters
    best_id = max(staff_counts, key=staff_counts.get)

    # Find Singh matter
    singh = None
    for m in matters:
        if "Singh" in (m.get("description") or ""):
            singh = m
            break

    if not singh:
        return False, "Singh estate matter not found."

    actual = singh.get("responsibleStaffId")
    if actual != best_id:
        best_name = next(
            (u["fullName"] for u in users if u["id"] == best_id), best_id
        )
        actual_name = next(
            (u["fullName"] for u in users if u["id"] == actual), actual
        )
        return False, (
            f"Singh responsible staff is '{actual_name}', "
            f"expected '{best_name}' (paralegal with most open matters: {staff_counts[best_id]})."
        )

    return True, "Singh estate case assigned to the paralegal with the most open matters."
