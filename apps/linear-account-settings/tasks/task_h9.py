import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify API key 'Personal Automation' renamed to 'Production Monitoring'."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    keys = state.get("apiKeys", [])

    # The old label should not exist
    old_key = [k for k in keys if k.get("label") == "Personal Automation"]
    if old_key:
        return False, "API key still has label 'Personal Automation'."

    # The new label should exist
    new_key = [k for k in keys if k.get("label") == "Production Monitoring"]
    if not new_key:
        return False, "API key 'Production Monitoring' not found."

    # Verify it has the same prefix (id key-a4b5c6)
    key = new_key[0]
    if "a4b5" not in key.get("prefix", ""):
        return False, f"Expected renamed key to retain original prefix, got '{key.get('prefix')}'."

    return True, "API key successfully renamed to 'Production Monitoring'."
