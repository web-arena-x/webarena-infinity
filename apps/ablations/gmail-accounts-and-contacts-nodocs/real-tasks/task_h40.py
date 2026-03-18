import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify Vendors label filtered to cloud infra only, remaining starred."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    contacts = state.get("contacts", [])
    contact_groups = state.get("contactGroups", [])

    # Find Vendors label
    vendors = None
    for g in contact_groups:
        if g.get("name") == "Vendors":
            vendors = g
            break

    if vendors is None:
        return False, "Vendors label not found."

    vendors_id = vendors["id"]

    # Cloud infrastructure companies to keep
    keep_companies = {
        "Amazon Web Services",
        "Cloudflare",
        "Snowflake",
        "Datadog",
        "MongoDB",
        "HashiCorp",
        "Elastic",
    }

    # Expected to remain in Vendors
    expected_keep = [
        ("Gregory", "Foster", "Datadog"),
        ("Michelle", "Torres", "Cloudflare"),
        ("Andrew", "Blackstone", "Snowflake"),
        ("Jessica", "Singh", "Amazon Web Services"),
        ("Jonathan", "Price", "MongoDB"),
        ("Aaron", "Blake", "HashiCorp"),
        ("Raymond", "Torres", "Elastic"),
    ]

    # Verify expected contacts are still in Vendors and starred
    missing = []
    not_starred = []
    for first, last, company in expected_keep:
        for c in contacts:
            if c.get("firstName") == first and c.get("lastName") == last:
                name = f"{first} {last} ({company})"
                if vendors_id not in c.get("groups", []):
                    missing.append(name)
                elif not c.get("starred"):
                    not_starred.append(name)
                break

    if missing:
        return False, (
            f"Cloud infra contacts should remain in Vendors: "
            f"{', '.join(missing)}."
        )

    if not_starred:
        return False, (
            f"Remaining vendor contacts should be starred: "
            f"{', '.join(not_starred)}."
        )

    # Verify non-cloud-infra contacts are NOT in Vendors
    should_be_removed = []
    for c in contacts:
        if vendors_id in c.get("groups", []):
            company = c.get("company", "")
            if company not in keep_companies:
                name = f"{c.get('firstName', '')} {c.get('lastName', '')} ({company})"
                should_be_removed.append(name)

    if should_be_removed:
        return False, (
            f"Non-cloud-infra contacts should be removed from Vendors: "
            f"{', '.join(should_be_removed)}."
        )

    # Verify removed contacts still exist (just not in Vendors)
    removed_names = [
        ("Samuel", "Lee"),
        ("Charlotte", "Müller"),
        ("Raj", "Kapoor"),
        ("Brandon", "Cooper"),
    ]
    for first, last in removed_names:
        found = False
        for c in contacts:
            if c.get("firstName") == first and c.get("lastName") == last:
                found = True
                break
        if not found:
            return False, (
                f"{first} {last} should still exist as a contact "
                f"(removed from Vendors, not deleted)."
            )

    return True, (
        "Vendors label filtered to 7 cloud infrastructure contacts. "
        "All remaining vendor contacts are starred."
    )
