"""Task H38: Delete 'Feature Request Response' snippet, rename 'Partnership Proposal' to 'Business Proposal' and make it shared."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    snippets = state.get("snippets", [])
    failures = []

    # snip_007 (Feature Request Response) should be deleted
    for snippet in snippets:
        if snippet.get("id") == "snip_007":
            failures.append(f"snip_007 (Feature Request Response) still exists")
            break

    # snip_009 should be renamed to 'Business Proposal' and shared
    snip_009 = None
    for snippet in snippets:
        if snippet.get("id") == "snip_009":
            snip_009 = snippet
            break

    if snip_009 is None:
        failures.append("snip_009 not found in state")
    else:
        if snip_009.get("name") != "Business Proposal":
            failures.append(f"snip_009 name is '{snip_009.get('name')}', expected 'Business Proposal'")
        if snip_009.get("isShared") is not True:
            failures.append(f"snip_009 isShared is {snip_009.get('isShared')}, expected True")

    if failures:
        return False, "Snippet checks failed: " + "; ".join(failures)

    return True, "snip_007 deleted; snip_009 renamed to 'Business Proposal' and made shared."
