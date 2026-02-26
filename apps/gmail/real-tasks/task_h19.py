"""Empty the trash, then report all spam emails as not spam."""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    response = requests.get(f"{server_url}/api/state")
    if response.status_code != 200:
        return False, f"Failed to fetch state: HTTP {response.status_code}"

    state = response.json()
    emails = state.get("emails", [])

    errors = []

    # Check 1: No emails should have isTrashed=True
    trashed = [e for e in emails if e.get("isTrashed", False)]
    if trashed:
        trashed_ids = [e["id"] for e in trashed]
        errors.append(
            f"Found {len(trashed)} trashed email(s) (trash should be empty): "
            f"IDs {trashed_ids}"
        )

    # Check 2: No emails should have isSpam=True
    spam = [e for e in emails if e.get("isSpam", False)]
    if spam:
        spam_ids = [e["id"] for e in spam]
        errors.append(
            f"Found {len(spam)} spam email(s) (all spam should be unmarked): "
            f"IDs {spam_ids}"
        )

    # Check 3: Former spam emails should still exist (not deleted)
    # Look for email with subject containing "Turn $100" (crypto spam)
    crypto_spam = next(
        (e for e in emails if "Turn $100" in e.get("subject", "")),
        None,
    )
    if crypto_spam is None:
        errors.append(
            "Could not find email with subject containing 'Turn $100' — "
            "former spam emails may have been deleted instead of unmarked"
        )

    if errors:
        return False, "; ".join(errors)

    return True, (
        "Trash is empty, no spam emails remain, and former spam emails "
        "still exist in mailbox."
    )
