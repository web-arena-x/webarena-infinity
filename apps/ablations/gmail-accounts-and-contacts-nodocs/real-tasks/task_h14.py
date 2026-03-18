import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])
    other_contacts = state.get("otherContacts", [])

    # Other contacts with >50 interactions that should be promoted
    promoted_emails = [
        "noreply@github.com",        # 342
        "notifications@slack.com",    # 156
        "receipts@uber.com",          # 67
        "hello@morningbrew.com",      # 89
        "no-reply@zoom.us",           # 203
        "alerts@sentry.io",           # 112
        "updates@linear.app",         # 56
        "digest@medium.com",          # 124
    ]

    # Verify none of the promoted emails remain in otherContacts
    still_in_other = []
    for oc in other_contacts:
        if oc.get("email") in promoted_emails:
            still_in_other.append(oc.get("email"))

    if still_in_other:
        return False, (
            f"The following promoted contacts still exist in otherContacts: "
            f"{', '.join(still_in_other)}."
        )

    # Verify all promoted emails now exist in contacts
    contact_emails = {c.get("email") for c in contacts}
    missing_from_contacts = []
    for email in promoted_emails:
        if email not in contact_emails:
            missing_from_contacts.append(email)

    if missing_from_contacts:
        return False, (
            f"The following promoted contacts are missing from the main contacts list: "
            f"{', '.join(missing_from_contacts)}."
        )

    # Verify that other contacts with <=50 interactions still exist
    # Original other contacts with <=50: oc_2 (3), oc_3 (8), oc_4 (45), oc_5 (24),
    # oc_6 (5), oc_7 (12), oc_8 (2), oc_10 (18), oc_14 (31), oc_16 (4),
    # oc_17 (38), oc_18 (7), oc_19 (15), oc_20 (1), oc_21 (9), oc_23 (11),
    # oc_25 (29) — 17 contacts
    remaining_other_emails = {oc.get("email") for oc in other_contacts}
    expected_remaining = [
        "jason.recruiter@linkedin.com",
        "support@vercel.com",
        "meetingbot@calendly.com",
        "billing@aws.amazon.com",
        "mike.sales@hubspot.com",
        "events@eventbrite.com",
        "sarah@restaurant-reservation.com",
        "travel@corporatetravel.com",
        "it-helpdesk@techcorp.io",
        "appointments@sfmedical.com",
        "order-confirm@amazon.com",
        "lisa@drycleaners-sf.com",
        "team@figma.com",
        "alex@doordash-driver.com",
        "security@1password.com",
        "amy.realtor@compass.com",
        "noreply@stripe.com",
    ]

    missing_remaining = []
    for email in expected_remaining:
        if email not in remaining_other_emails:
            missing_remaining.append(email)

    if missing_remaining:
        return False, (
            f"The following low-interaction other contacts should still exist "
            f"but are missing: {', '.join(missing_remaining)}."
        )

    return True, (
        f"All 8 other contacts with >50 interactions have been promoted to "
        f"the main contacts list. {len(other_contacts)} low-interaction "
        f"other contacts remain."
    )
