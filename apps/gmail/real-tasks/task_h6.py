"""
Task H6: Change the star on United Airlines deal to green star, move from
Promotions to Primary, apply Action Required label.
Verify email id=49:
  - isStarred=True and starType='green-star'
  - category='primary' and 'CATEGORY_PRIMARY' in labels,
    'CATEGORY_PROMOTIONS' not in labels
  - 'label_17' (Action Required) in labels
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    emails = state.get("emails", [])

    email = next((e for e in emails if e.get("id") == 49), None)
    if email is None:
        return False, "Email with id=49 (United Airlines deal) not found."

    errors = []
    email_labels = email.get("labels", [])

    # Check star
    if not email.get("isStarred"):
        errors.append(f"isStarred={email.get('isStarred')!r}, expected True")
    if email.get("starType") != "green-star":
        errors.append(
            f"starType={email.get('starType')!r}, expected 'green-star'"
        )

    # Check category move
    category = email.get("category", "")
    if category != "primary":
        errors.append(f"category={category!r}, expected 'primary'")
    if "CATEGORY_PRIMARY" not in email_labels:
        errors.append("'CATEGORY_PRIMARY' not in labels")
    if "CATEGORY_PROMOTIONS" in email_labels:
        errors.append("'CATEGORY_PROMOTIONS' still in labels (should be removed)")

    # Check Action Required label
    if "label_17" not in email_labels:
        errors.append("'label_17' (Action Required) not in labels")

    if errors:
        return False, (
            f"Email id=49 checks failed: " + "; ".join(errors)
            + f". Current labels: {email_labels}"
        )

    return True, (
        "Email id=49 has green star, moved to Primary, and has Action Required label."
    )
