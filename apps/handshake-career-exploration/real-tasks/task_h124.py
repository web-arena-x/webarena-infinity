"""
Task: Cancel your requested appointment with the interview coach. Schedule
a new mock behavioral interview for March 19, 2026 at 3:00 PM, virtually.
Add a comment to your approved appointment asking about portfolio tips.

Discovery:
  Interview coach: David Kim (staff_04) → appt_02 (requested).
  Approved appointment: appt_01 (Resume Review with Michael Okafor).

Verify:
(1) appt_02 status == 'cancelled'
(2) New appointment: type contains 'Behavioral', date '2026-03-19',
    time '3:00 PM', medium 'Virtual on Handshake'
(3) appt_01 has comment from Maya mentioning 'portfolio'
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    errors = []
    appointments = state.get("appointments", [])

    # Check 1: appt_02 cancelled
    appt_02 = next((a for a in appointments if a.get("id") == "appt_02"), None)
    if appt_02 is None:
        errors.append("appt_02 not found.")
    elif appt_02.get("status") != "cancelled":
        errors.append(f"appt_02 not cancelled. status='{appt_02.get('status')}'")

    # Check 2: new mock behavioral appointment
    new_appt = None
    for a in appointments:
        if (
            a.get("id") not in (
                "appt_01", "appt_02", "appt_03", "appt_04",
                "appt_05", "appt_06", "appt_07", "appt_08",
            )
            and "behavioral" in a.get("type", "").lower()
        ):
            new_appt = a
            break

    if new_appt is None:
        errors.append("No new mock behavioral appointment found.")
    else:
        if new_appt.get("date") != "2026-03-19":
            errors.append(
                f"New appointment date is '{new_appt.get('date')}', "
                "expected '2026-03-19'."
            )
        if new_appt.get("time") != "3:00 PM":
            errors.append(
                f"New appointment time is '{new_appt.get('time')}', "
                "expected '3:00 PM'."
            )
        if new_appt.get("medium") != "Virtual on Handshake":
            errors.append(
                f"New appointment medium is '{new_appt.get('medium')}', "
                "expected 'Virtual on Handshake'."
            )

    # Check 3: appt_01 comment about portfolio
    appt_01 = next((a for a in appointments if a.get("id") == "appt_01"), None)
    if appt_01 is None:
        errors.append("appt_01 not found.")
    else:
        found = any(
            "maya" in c.get("author", "").lower()
            and "portfolio" in c.get("text", "").lower()
            for c in appt_01.get("comments", [])
        )
        if not found:
            errors.append(
                "No comment from Maya mentioning 'portfolio' on appt_01."
            )

    if errors:
        return False, " | ".join(errors)
    return True, (
        "appt_02 cancelled. New mock behavioral interview scheduled "
        "for March 19 at 3 PM virtually. Portfolio comment added to appt_01."
    )
