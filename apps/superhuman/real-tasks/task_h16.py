"""Task H16: Rename 'Bug Report Acknowledgment' snippet to 'Issue Response' and make private."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    snippets = state.get("snippets", [])
    snippet = None
    for s in snippets:
        if s.get("id") == "snip_008":
            snippet = s
            break

    if snippet is None:
        return False, "Snippet snip_008 not found in state."

    failures = []

    name = snippet.get("name")
    if name != "Issue Response":
        failures.append(f"name is '{name}', expected 'Issue Response'")

    is_shared = snippet.get("isShared")
    if is_shared is not False:
        failures.append(f"isShared is {is_shared}, expected False")

    if failures:
        return False, "snip_008 checks failed: " + "; ".join(failures)

    return True, "Snippet snip_008 renamed to 'Issue Response' and set to private (isShared=False)."
