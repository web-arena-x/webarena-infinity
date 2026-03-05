"""Task M19: Remove the Newsletters split from the inbox."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    splits = state.get("splits", [])
    for split in splits:
        if split.get("id") == "split_newsletters":
            return False, f"Newsletters split (split_newsletters) still exists in splits: {split}"

    return True, "Newsletters split (split_newsletters) has been removed from splits"
