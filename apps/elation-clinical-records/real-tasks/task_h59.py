import requests
from datetime import datetime


def verify(server_url: str) -> tuple[bool, str]:
    """Find template with billing code 99395, create note for youngest adult (18+) with that template + Annual Exam category."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    today = datetime(2026, 3, 8)

    # Find template with billing code 99395
    target_tmpl = None
    for t in state.get("visitNoteTemplates", []):
        for b in t.get("billingItems", []):
            if b.get("cptCode") == "99395":
                target_tmpl = t
                break
        if target_tmpl:
            break
    if not target_tmpl:
        return False, "No template with billing code 99395 found."

    # Find youngest adult patient (18+)
    adults = []
    for p in state.get("patients", []):
        dob_str = p.get("dateOfBirth", "")
        if not dob_str:
            continue
        try:
            dob = datetime.strptime(dob_str, "%Y-%m-%d")
            age = (today - dob).days // 365
        except ValueError:
            continue
        if age >= 18:
            adults.append((p, dob, age))

    if not adults:
        return False, "No adult patients found."

    # Youngest = most recent DOB
    adults.sort(key=lambda x: x[1], reverse=True)
    youngest = adults[0][0]
    youngest_age = adults[0][2]
    last_name = youngest.get("lastName", "?")
    pid = youngest.get("id")

    # Find Annual Exam category
    annual_cat_id = None
    for c in state.get("visitNoteCategories", []):
        if c.get("name", "").lower() == "annual exam":
            annual_cat_id = c.get("id")
            break
    if not annual_cat_id:
        return False, "Annual Exam category not found."

    # Find new note
    existing_note_ids = set()
    for n in state.get("visitNotes", []):
        if n.get("patientId") == pid:
            existing_note_ids.add(n.get("id"))
    # Remove any seed data note IDs
    seed_notes = {"note_009"}  # Rodriguez-Martinez's existing note
    existing_note_ids = existing_note_ids & seed_notes

    new_notes = [
        n for n in state.get("visitNotes", [])
        if n.get("patientId") == pid and n.get("id") not in seed_notes
    ]

    matching = None
    for n in new_notes:
        cat = n.get("category") or n.get("categoryId", "")
        tmpl = n.get("templateUsed", "")
        if cat == annual_cat_id and tmpl == target_tmpl.get("id"):
            matching = n
            break

    if not matching:
        return False, (
            f"{last_name} (youngest adult, age {youngest_age}) does not have a new note "
            f"with Annual Exam category and template '{target_tmpl.get('name')}'."
        )

    return True, (
        f"{last_name} (youngest adult, age {youngest_age}) has new note (id={matching['id']}) "
        f"with Annual Exam category and template '{target_tmpl.get('name')}'."
    )
