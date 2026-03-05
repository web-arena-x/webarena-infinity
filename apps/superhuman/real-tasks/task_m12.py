"""Task M12: Delete the Out of Office snippet."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    snippets = state.get("snippets", [])
    for snippet in snippets:
        if snippet.get("id") == "snip_006" or snippet.get("name") == "Out of Office":
            return False, f"Out of Office snippet still exists: {snippet}"

    return True, "Out of Office snippet (snip_006) has been deleted"
