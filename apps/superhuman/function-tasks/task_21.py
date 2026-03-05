import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    emails = state.get("emails", [])

    # Get Me To Zero preserving starred:
    # - Starred emails should remain in inbox
    # - Non-starred emails should be moved to done
    inbox_emails = [
        e for e in emails
        if e.get("folder") == "inbox"
        and not e.get("isDraft", False)
        and not e.get("isScheduled", False)
    ]

    # All remaining inbox emails must be starred
    non_starred_in_inbox = [e for e in inbox_emails if not e.get("isStarred", False)]
    if len(non_starred_in_inbox) > 0:
        subjects = [e.get("subject", "unknown") for e in non_starred_in_inbox[:5]]
        return False, (
            f"Found {len(non_starred_in_inbox)} non-starred emails still in inbox. "
            f"Examples: {subjects}. Expected only starred emails to remain."
        )

    # There should be at least some starred emails remaining in inbox
    starred_in_inbox = [e for e in inbox_emails if e.get("isStarred", False)]
    if len(starred_in_inbox) == 0:
        return False, "No starred emails remain in inbox. Expected starred emails to be preserved."

    return True, (
        f"Get Me To Zero (preserving starred) completed. "
        f"{len(starred_in_inbox)} starred emails remain in inbox, non-starred archived."
    )
