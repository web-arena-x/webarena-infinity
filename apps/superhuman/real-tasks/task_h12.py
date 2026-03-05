"""Task H12: Enable auto-archive for newsletters and receipts, archive all newsletter inbox emails."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    settings = state.get("settings", {})
    auto_archive = settings.get("autoArchive", {})

    failures = []

    # Check auto-archive enabled
    if auto_archive.get("enabled") is not True:
        failures.append(f"autoArchive.enabled is {auto_archive.get('enabled')}, expected True")

    # Check autoLabels list contains newsletters and receipts
    aa_labels = auto_archive.get("autoLabels", [])
    if "autolabel_newsletters" not in aa_labels:
        failures.append(f"autoArchive.autoLabels missing 'autolabel_newsletters', has {aa_labels}")
    if "autolabel_receipts" not in aa_labels:
        failures.append(f"autoArchive.autoLabels missing 'autolabel_receipts', has {aa_labels}")

    # Check newsletter inbox emails are archived
    target_ids = ["email_029", "email_030", "email_122"]
    emails_by_id = {e["id"]: e for e in state.get("emails", [])}

    for eid in target_ids:
        email = emails_by_id.get(eid)
        if email is None:
            failures.append(f"{eid}: not found in state")
            continue
        if email.get("folder") != "done":
            failures.append(f"{eid}: folder is '{email.get('folder')}', expected 'done'")

    if failures:
        return False, "Auto-archive / newsletter archive checks failed: " + "; ".join(failures)

    return True, "Auto-archive enabled for newsletters and receipts; all newsletter inbox emails archived."
