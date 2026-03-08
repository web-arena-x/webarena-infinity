# Task: Move all real people from other contacts to main contacts.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()
    errors = []

    contacts = state.get("contacts", [])
    other_contacts = state.get("otherContacts", [])

    # Real people emails that should be in main contacts
    real_people_emails = [
        "jason.blake@salesforce.com",
        "tina.marshall@designhub.com",
        "alex.rivera@notion.so",
        "mike.santos@cloudflare.com",
        "wendy.chung@techcorp.io",
        "chloe.b@sequoiacap.com",
        "peter.grant@mongodb.com",
        "nina.k@figma.com",
    ]

    # Collect all emails from contacts and otherContacts
    contact_emails = set()
    for c in contacts:
        if c.get("email"):
            contact_emails.add(c["email"])
        if c.get("secondaryEmail"):
            contact_emails.add(c["secondaryEmail"])

    other_emails = set()
    for oc in other_contacts:
        if oc.get("email"):
            other_emails.add(oc["email"])

    # Check each real person email is in contacts and NOT in otherContacts
    for email in real_people_emails:
        if email not in contact_emails:
            errors.append(f"'{email}' not found in main contacts")
        if email in other_emails:
            errors.append(f"'{email}' still in otherContacts")

    # Check service accounts are still in otherContacts
    service_emails = [
        "support@vercel.com",
        "billing@aws.amazon.com",
        "hr@techcorp.io",
        "no-reply@stripe.com",
        "noreply@github.com",
        "receipts@uber.com",
        "team@linear.app",
        "do-not-reply@zoom.us",
        "alerts@datadog.com",
        "notifications@jira.atlassian.com",
        "newsletter@hackernews.com",
        "no-reply@docusign.net",
    ]
    for email in service_emails:
        if email not in other_emails:
            errors.append(f"Service account '{email}' missing from otherContacts")

    if errors:
        return False, "; ".join(errors)
    return True, "All real people moved to main contacts; service accounts remain in other contacts."
