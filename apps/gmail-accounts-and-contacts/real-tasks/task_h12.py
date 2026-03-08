# Task: Merge CloudNine, dismiss EuroDesign, remove pending delegate.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()
    errors = []

    contacts = state.get("contacts", [])
    merge_suggestions = state.get("mergeSuggestions", [])
    delegates = state.get("delegates", [])

    # Check merge_1 (CloudNine) is dismissed
    merge_1 = None
    for ms in merge_suggestions:
        if ms.get("id") == "merge_1":
            merge_1 = ms
            break
    if merge_1 is None:
        errors.append("merge_1 not found in mergeSuggestions")
    elif not merge_1.get("dismissed"):
        errors.append("merge_1 (CloudNine) not dismissed")

    # After merging CloudNine: contact_36 (Raj Kapoor) should be gone,
    # contact_05 (Priya Sharma) should still exist
    contact_ids = {c.get("id") for c in contacts}

    if "contact_36" in contact_ids:
        errors.append("contact_36 (Raj Kapoor) still exists after merge")

    if "contact_05" not in contact_ids:
        errors.append("contact_05 (Priya Sharma) should still exist after merge")

    # Check merge_2 (EuroDesign) is dismissed
    merge_2 = None
    for ms in merge_suggestions:
        if ms.get("id") == "merge_2":
            merge_2 = ms
            break
    if merge_2 is None:
        errors.append("merge_2 not found in mergeSuggestions")
    elif not merge_2.get("dismissed"):
        errors.append("merge_2 (EuroDesign) not dismissed")

    # No delegate with status='pending'
    for d in delegates:
        if d.get("status") == "pending":
            errors.append(
                f"Delegate '{d.get('email')}' still has pending status"
            )

    if errors:
        return False, "; ".join(errors)
    return True, "CloudNine merged, EuroDesign dismissed, pending delegate removed."
