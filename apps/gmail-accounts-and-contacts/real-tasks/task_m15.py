# Task: Star Ben Walker and Tony Russo.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()
    errors = []

    contacts = state.get("contacts", [])

    ben = next(
        (c for c in contacts if c.get("firstName") == "Ben" and c.get("lastName") == "Walker"),
        None,
    )
    if ben is None:
        errors.append("Contact 'Ben Walker' not found")
    elif ben.get("isStarred") is not True:
        errors.append(f"Expected Ben Walker isStarred to be true, got {ben.get('isStarred')}")

    tony = next(
        (c for c in contacts if c.get("firstName") == "Tony" and c.get("lastName") == "Russo"),
        None,
    )
    if tony is None:
        errors.append("Contact 'Tony Russo' not found")
    elif tony.get("isStarred") is not True:
        errors.append(f"Expected Tony Russo isStarred to be true, got {tony.get('isStarred')}")

    if errors:
        return False, "; ".join(errors)
    return True, "Ben Walker and Tony Russo starred successfully."
