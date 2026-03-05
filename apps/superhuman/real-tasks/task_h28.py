"""Task H28: Update email signature to say 'CTO' instead of 'VP of Engineering' and set undo send delay to 30s."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    failures = []

    # Check signature
    signature = state.get("settings", {}).get("signatures", {}).get("default", "")
    if "CTO" not in signature:
        failures.append(f"Signature does not contain 'CTO'")
    if "VP of Engineering" in signature:
        failures.append(f"Signature still contains 'VP of Engineering'")

    # Check undo send delay
    undo_delay = state.get("settings", {}).get("general", {}).get("undoSendDelay")
    if undo_delay != 30:
        failures.append(f"undoSendDelay is {undo_delay}, expected 30")

    if failures:
        return False, "Signature/settings checks failed: " + "; ".join(failures)

    return True, "Signature updated to CTO and undo send delay set to 30 seconds."
