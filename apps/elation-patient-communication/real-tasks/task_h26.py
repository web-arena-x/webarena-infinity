import requests


def verify(server_url: str) -> tuple[bool, str]:
    """For Dr. Torres categories where he's the sole recipient, add Front Desk."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    routing = state.get("messageRouting", {}).get("prov_2", {})

    # Categories where prov_2 was the sole recipient in seed data:
    # Prescription Refill, Test Results, Referral Request, Other
    # Front Desk = ug_1
    need_front_desk = [
        "Prescription Refill",
        "Test Results",
        "Referral Request",
        "Other",
    ]

    for cat in need_front_desk:
        recipients = routing.get(cat, [])
        if "ug_1" not in recipients:
            return False, (
                f"Dr. Torres's '{cat}' routing does not include Front Desk "
                f"(ug_1). Current recipients: {recipients}"
            )
        if "prov_2" not in recipients:
            return False, (
                f"Dr. Torres's '{cat}' routing lost Dr. Torres himself "
                f"(prov_2). Current recipients: {recipients}"
            )

    # Categories that already had multiple recipients should still be intact
    gen_q = routing.get("General Question", [])
    if "prov_2" not in gen_q or "ug_1" not in gen_q:
        return False, (
            f"Dr. Torres's 'General Question' routing was unexpectedly "
            f"modified: {gen_q}"
        )

    return True, (
        "Front Desk added to all Dr. Torres categories where he was "
        "the sole recipient."
    )
