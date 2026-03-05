"""Task H31: Star every Fundraising-labeled email in the inbox and enable auto-archive for receipts."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    failures = []

    # Inbox emails with label_3 (Fundraising): email_002, 023, 026, 119, 120
    target_ids = ["email_002", "email_023", "email_026", "email_119", "email_120"]
    emails_by_id = {e["id"]: e for e in state.get("emails", [])}

    for eid in target_ids:
        email = emails_by_id.get(eid)
        if email is None:
            failures.append(f"{eid}: not found in state")
            continue
        if email.get("isStarred") is not True:
            failures.append(f"{eid}: isStarred is {email.get('isStarred')}, expected True")

    # Check auto-archive enabled with receipts
    auto_archive = state.get("settings", {}).get("autoArchive", {})
    if auto_archive.get("enabled") is not True:
        failures.append(f"autoArchive.enabled is {auto_archive.get('enabled')}, expected True")
    if "autolabel_receipts" not in auto_archive.get("autoLabels", []):
        failures.append(f"autolabel_receipts not in autoArchive.autoLabels: {auto_archive.get('autoLabels')}")

    if failures:
        return False, "Fundraising star / auto-archive checks failed: " + "; ".join(failures)

    return True, "All 5 Fundraising inbox emails starred and auto-archive enabled for receipts."
