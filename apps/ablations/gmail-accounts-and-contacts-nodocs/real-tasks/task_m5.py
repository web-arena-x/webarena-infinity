import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    delegates = state.get("delegates", [])

    # Find delegate with target email
    target_email = "david.park@techcorp.io"
    delegate = None
    for d in delegates:
        if d.get("email") == target_email:
            delegate = d
            break

    if not delegate:
        return False, f"Delegate with email '{target_email}' not found."

    # Verify name
    if delegate.get("name") != "David Park":
        return False, f"Expected delegate name 'David Park', got '{delegate.get('name')}'."

    # Verify status is pending
    if delegate.get("status") != "pending":
        return False, f"Expected delegate status 'pending', got '{delegate.get('status')}'."

    return True, "Delegate 'David Park' (david.park@techcorp.io) added with pending status."
