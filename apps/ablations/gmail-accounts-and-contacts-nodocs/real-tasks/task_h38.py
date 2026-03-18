import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify active delegates removed, pending kept, two new delegates added."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    delegates = state.get("delegates", [])

    delegate_emails = {d.get("email") for d in delegates}

    # Active delegates should be removed
    # James Wu (active) and Priya Sharma (active)
    removed_active = {"james.wu@techcorp.io", "priya.sharma@techcorp.io"}
    still_present = removed_active & delegate_emails

    if still_present:
        return False, (
            f"Active delegates should be removed: {', '.join(still_present)}."
        )

    # Alex Martinez (pending) should remain
    if "alex.martinez@techcorp.io" not in delegate_emails:
        return False, (
            "Alex Martinez (pending delegate) should still be present."
        )

    # New delegates should exist
    expected_new = {
        "elaine.cho@techcorp.io",
        "brian.foster@techcorp.io",
    }
    missing_new = expected_new - delegate_emails

    if missing_new:
        return False, (
            f"Missing new delegates: {', '.join(missing_new)}."
        )

    # Should have 3 delegates total
    if len(delegates) != 3:
        return False, (
            f"Expected 3 delegates (1 existing pending + 2 new), "
            f"found {len(delegates)}."
        )

    return True, (
        "Active delegates (James Wu, Priya Sharma) removed. "
        "Pending delegate (Alex Martinez) kept. "
        "New delegates added: Elaine Cho, Brian Foster."
    )
