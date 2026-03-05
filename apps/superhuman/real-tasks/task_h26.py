"""Task H26: Find the snippet with the most sends and add '(Top Performer)' to the end of its name."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    # snip_008 (Bug Report Acknowledgment) has 52 sends — the highest
    snippets = state.get("snippets", [])
    for snippet in snippets:
        if snippet.get("id") == "snip_008":
            name = snippet.get("name", "")
            if name == "Bug Report Acknowledgment (Top Performer)":
                return True, f"snip_008 renamed to '{name}'."
            return False, f"snip_008 name is '{name}', expected 'Bug Report Acknowledgment (Top Performer)'."

    return False, "snip_008 not found in state."
