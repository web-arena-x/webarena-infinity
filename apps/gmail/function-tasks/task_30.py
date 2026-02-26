import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    email = next(
        (e for e in state["emails"]
         if e["subject"] == "Interview Request: Tech Innovation Panel"),
        None,
    )
    if not email:
        return False, "Email 'Interview Request: Tech Innovation Panel' not found."

    if email.get("category") != "updates":
        return False, f"Expected category 'updates', got '{email.get('category')}'."

    if "CATEGORY_UPDATES" not in email["labels"]:
        return False, "Email does not have CATEGORY_UPDATES label."

    if "CATEGORY_PRIMARY" in email["labels"]:
        return False, "Email still has CATEGORY_PRIMARY label."

    return True, "Email moved to Updates category."
