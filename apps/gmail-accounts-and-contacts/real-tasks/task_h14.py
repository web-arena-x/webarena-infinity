# Task: Delete non-US contacts.
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()
    errors = []

    contacts = state.get("contacts", [])

    # Non-US contacts that should be deleted
    deleted_contacts = [
        ("Sophie", "Laurent"),
        ("Yuki", "Tanaka"),
        ("Raj", "Kapoor"),
        ("Elena", "Volkov"),
    ]

    for first, last in deleted_contacts:
        for c in contacts:
            if c.get("firstName") == first and c.get("lastName") == last:
                errors.append(
                    f"Non-US contact '{first} {last}' still exists"
                )
                break

    if errors:
        return False, "; ".join(errors)
    return True, "All non-US contacts successfully deleted."
