"""
Task: Your earliest completed appointment was a specific type. Schedule a
follow-up appointment of the same category and type with the same staff
member, for March 28, 2026 at 9:00 AM, in person.

Discovery: Completed appointments by date:
  appt_07 (Sep 20, 2025) — earliest, Career Counseling / Major Exploration,
  Maria Rodriguez (staff_03).
  March 28 available: 9:00 AM, 11:00 AM, 1:00 PM. staff_03 available.

Verify:
(1) New appointment: category 'Career Counseling', type 'Major Exploration',
    staffId 'staff_03', date '2026-03-28', time '9:00 AM', medium 'In Person'
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    errors = []
    appointments = state.get("appointments", [])

    seed_ids = {
        "appt_01", "appt_02", "appt_03", "appt_04",
        "appt_05", "appt_06", "appt_07", "appt_08",
    }
    new_appts = [a for a in appointments if a.get("id") not in seed_ids]

    match = None
    for a in new_appts:
        if (
            a.get("category") == "Career Counseling"
            and a.get("type") == "Major Exploration"
        ):
            match = a
            break

    if match is None:
        errors.append(
            "No new appointment with category 'Career Counseling' "
            "and type 'Major Exploration' found."
        )
    else:
        if match.get("staffId") != "staff_03":
            errors.append(
                f"Staff is '{match.get('staffName')}', "
                "expected Maria Rodriguez (staff_03)."
            )
        if match.get("date") != "2026-03-28":
            errors.append(
                f"Date is '{match.get('date')}', expected '2026-03-28'."
            )
        if match.get("time") != "9:00 AM":
            errors.append(
                f"Time is '{match.get('time')}', expected '9:00 AM'."
            )
        if match.get("medium") != "In Person":
            errors.append(
                f"Medium is '{match.get('medium')}', expected 'In Person'."
            )

    if errors:
        return False, " | ".join(errors)
    return True, (
        "Earliest completed appointment identified (appt_07). "
        "Follow-up scheduled with Maria Rodriguez on March 28 at 9 AM."
    )
