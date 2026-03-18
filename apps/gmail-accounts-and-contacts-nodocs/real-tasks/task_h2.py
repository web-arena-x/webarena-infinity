import requests
import re


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Find the Leadership Team group by name
    contact_groups = state.get("contactGroups", [])
    leadership_group = None
    for g in contact_groups:
        if g.get("name") == "Leadership Team":
            leadership_group = g
            break

    if leadership_group is None:
        return False, "Leadership Team group not found. It should have been created."

    leadership_id = leadership_group["id"]

    # Find all TechCorp contacts
    contacts = state.get("contacts", [])
    techcorp_contacts = [
        c for c in contacts
        if (c.get("company") or "").lower() == "techcorp"
    ]

    if len(techcorp_contacts) == 0:
        return False, "No TechCorp contacts found in the contacts list."

    # Determine which TechCorp contacts should have the Leadership Team label
    title_pattern = re.compile(r"\b(VP|Head|CFO)\b", re.IGNORECASE)

    expected_members = []
    non_members = []
    for c in techcorp_contacts:
        job_title = c.get("jobTitle", "")
        name = f"{c.get('firstName', '')} {c.get('lastName', '')}".strip()
        if title_pattern.search(job_title):
            expected_members.append((name, job_title, c))
        else:
            non_members.append((name, job_title, c))

    # Verify all matching TechCorp contacts have the Leadership Team group
    missing = []
    for name, title, c in expected_members:
        if leadership_id not in c.get("groups", []):
            missing.append(f"{name} ({title})")

    if missing:
        return False, (
            f"The following TechCorp contacts with VP/Head/CFO titles are not in "
            f"Leadership Team: {', '.join(missing)}."
        )

    # Verify non-matching TechCorp contacts do NOT have the Leadership Team group
    incorrectly_added = []
    for name, title, c in non_members:
        if leadership_id in c.get("groups", []):
            incorrectly_added.append(f"{name} ({title})")

    if incorrectly_added:
        return False, (
            f"The following TechCorp contacts should NOT be in Leadership Team "
            f"(title does not contain VP/Head/CFO): {', '.join(incorrectly_added)}."
        )

    if len(expected_members) < 4:
        return False, (
            f"Expected at least 4 TechCorp contacts with VP/Head/CFO titles, "
            f"found {len(expected_members)}."
        )

    member_names = [name for name, _, _ in expected_members]
    return True, (
        f"Leadership Team group exists and contains all {len(expected_members)} "
        f"qualifying TechCorp contacts: {', '.join(member_names)}."
    )
