import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    splits = state.get("splits", [])

    for split in splits:
        if split.get("name") == "Investor Updates":
            criteria = split.get("criteria", {})
            auto_label = criteria.get("autoLabel")
            if auto_label == "Investor":
                return True, "Split 'Investor Updates' created with criteria.autoLabel == 'Investor'."
            return False, f"Split 'Investor Updates' exists but criteria.autoLabel is '{auto_label}', expected 'Investor'."

    return False, "No split named 'Investor Updates' found."
