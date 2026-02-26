import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    # Check that no filter matches emails from notifications@linkedin.com
    matching_filter = next(
        (f for f in state["filters"]
         if f["criteria"]["from"] == "notifications@linkedin.com"),
        None,
    )
    if matching_filter:
        return False, "Filter matching 'notifications@linkedin.com' still exists."

    return True, "Filter for 'notifications@linkedin.com' has been deleted."
