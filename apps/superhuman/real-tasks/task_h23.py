"""Task H23: Mark all unread emails from TechCorp teammates as read, star ones with Engineering label."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    # Unread inbox emails from @techcorp.io in seed state:
    # All should now be read; those with label_10 (Engineering) should also be starred.
    must_be_read = ["email_001", "email_012", "email_014", "email_024",
                    "email_114", "email_115", "email_124", "email_125"]
    must_be_starred = ["email_012", "email_114", "email_115", "email_125"]

    emails_by_id = {e["id"]: e for e in state.get("emails", [])}
    failures = []

    for eid in must_be_read:
        email = emails_by_id.get(eid)
        if email is None:
            failures.append(f"{eid}: not found in state")
            continue
        if email.get("isRead") is not True:
            failures.append(f"{eid}: isRead is {email.get('isRead')}, expected True")

    for eid in must_be_starred:
        email = emails_by_id.get(eid)
        if email is None:
            continue  # already reported above
        if email.get("isStarred") is not True:
            failures.append(f"{eid}: isStarred is {email.get('isStarred')}, expected True (has Engineering label)")

    if failures:
        return False, "Teammate email checks failed: " + "; ".join(failures)

    return True, "All 8 unread teammate emails marked read; 4 with Engineering label starred."
