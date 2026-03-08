"""
Task: Add 'Fellowship' and 'Volunteering' to your post-graduation plans.
Find the only Nonprofit employer on Handshake, save their active job, and
schedule a career change guidance appointment for March 20, 2026 at
10:00 AM, virtually.

Discovery: Nonprofit → Teach For America (emp_18). Active job: job_20.
Career Change Guidance: category 'Career Counseling', type 'Career Change Guidance'.
March 20 available: 10:00 AM, 2:00 PM. Staff: staff_02, staff_03.

Verify:
(1) 'Fellowship' in postGraduation
(2) 'Volunteering' in postGraduation
(3) job_20 in savedJobIds
(4) New appointment: type 'Career Change Guidance', date '2026-03-20',
    time '10:00 AM', medium 'Virtual on Handshake'
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    errors = []
    user = state.get("currentUser", {})

    post_grad = user.get("careerInterests", {}).get("postGraduation", [])
    for plan in ["Fellowship", "Volunteering"]:
        if plan not in post_grad:
            errors.append(f"'{plan}' not in postGraduation. Current: {post_grad}")

    saved = user.get("savedJobIds", [])
    if "job_20" not in saved:
        errors.append("job_20 not in savedJobIds.")

    appointments = state.get("appointments", [])
    seed_ids = {
        "appt_01", "appt_02", "appt_03", "appt_04",
        "appt_05", "appt_06", "appt_07", "appt_08",
    }
    new_appts = [a for a in appointments if a.get("id") not in seed_ids]

    match = None
    for a in new_appts:
        if a.get("type") == "Career Change Guidance":
            match = a
            break

    if match is None:
        errors.append("No new Career Change Guidance appointment found.")
    else:
        if match.get("date") != "2026-03-20":
            errors.append(
                f"Appointment date is '{match.get('date')}', "
                "expected '2026-03-20'."
            )
        if match.get("time") != "10:00 AM":
            errors.append(
                f"Appointment time is '{match.get('time')}', "
                "expected '10:00 AM'."
            )
        if match.get("medium") != "Virtual on Handshake":
            errors.append(
                f"Appointment medium is '{match.get('medium')}', "
                "expected 'Virtual on Handshake'."
            )

    if errors:
        return False, " | ".join(errors)
    return True, (
        "Fellowship and Volunteering added to post-grad plans. "
        "TFA job saved. Career Change Guidance appointment scheduled."
    )
