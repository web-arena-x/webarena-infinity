"""
Task: Delete both the Body/Small and Body/Large text styles.
Verify: No style named "Body/Small" and no style named "Body/Large" exist.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    text_styles = state.get("textStyles", [])

    errors = []

    body_small = next(
        (s for s in text_styles if s.get("name") == "Body/Small"), None
    )
    if body_small is not None:
        errors.append("Text style 'Body/Small' still exists")

    body_large = next(
        (s for s in text_styles if s.get("name") == "Body/Large"), None
    )
    if body_large is not None:
        errors.append("Text style 'Body/Large' still exists")

    if errors:
        return False, "; ".join(errors)

    return True, "Both Body/Small and Body/Large text styles have been deleted."
