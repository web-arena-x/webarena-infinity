"""Task M15: Enable auto-archive for newsletters."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    settings = state.get("settings", {})
    auto_archive = settings.get("autoArchive", {})

    enabled = auto_archive.get("enabled")
    if enabled is not True:
        return False, f"Auto-archive is not enabled: enabled={enabled}"

    auto_labels = auto_archive.get("autoLabels", [])
    if "autolabel_newsletters" in auto_labels:
        return True, "Auto-archive is enabled and 'autolabel_newsletters' is in autoLabels"

    return False, f"'autolabel_newsletters' not found in autoArchive.autoLabels: {auto_labels}"
