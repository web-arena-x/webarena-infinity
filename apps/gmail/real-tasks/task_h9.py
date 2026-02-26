"""
Task H9: Configure multiple inbox: section 1 = 'is:important' named 'Priority',
section 2 = 'label:Action Required' named 'Action Items'.
Verify:
  - settings.multipleInboxSections[0].query='is:important' and .name='Priority'
  - settings.multipleInboxSections[1].query='label:Action Required' and
    .name='Action Items'
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    settings = state.get("settings", {})
    sections = settings.get("multipleInboxSections", [])

    if len(sections) < 2:
        return False, (
            f"multipleInboxSections has {len(sections)} entries, expected at least 2."
        )

    errors = []

    # Section 1 (index 0)
    s1 = sections[0]
    if s1.get("query") != "is:important":
        errors.append(
            f"Section 1 query={s1.get('query')!r}, expected 'is:important'"
        )
    if s1.get("name") != "Priority":
        errors.append(
            f"Section 1 name={s1.get('name')!r}, expected 'Priority'"
        )

    # Section 2 (index 1)
    s2 = sections[1]
    if s2.get("query") != "label:Action Required":
        errors.append(
            f"Section 2 query={s2.get('query')!r}, expected 'label:Action Required'"
        )
    if s2.get("name") != "Action Items":
        errors.append(
            f"Section 2 name={s2.get('name')!r}, expected 'Action Items'"
        )

    if errors:
        return False, "Multiple inbox config incorrect: " + "; ".join(errors)

    return True, (
        "Multiple inbox configured: section 1 = 'is:important' / 'Priority', "
        "section 2 = 'label:Action Required' / 'Action Items'."
    )
