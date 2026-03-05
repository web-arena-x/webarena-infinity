import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that auto-archive is enabled with Newsletters and Receipts auto-labels."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()

    try:
        auto_archive = state["settings"]["autoArchive"]
    except (KeyError, TypeError) as e:
        return False, f"Could not find settings.autoArchive: {e}"

    enabled = auto_archive.get("enabled")
    if enabled is not True:
        return False, f"Expected settings.autoArchive.enabled to be True, got {enabled!r}."

    auto_labels = auto_archive.get("autoLabels", [])
    required_ids = {"autolabel_newsletters", "autolabel_receipts"}
    present_ids = set(auto_labels) if isinstance(auto_labels, list) else set()

    missing = required_ids - present_ids
    if missing:
        return False, f"Auto-archive autoLabels missing required IDs: {missing}. Found: {auto_labels!r}."

    return True, "Auto-archive is enabled with Newsletters and Receipts auto-labels."
