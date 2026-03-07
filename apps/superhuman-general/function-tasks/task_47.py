import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})
    signature = settings.get("signature", "")

    if not signature:
        return False, "Signature is empty or not set."

    missing = []
    if "Regards" not in signature:
        missing.append("Regards")
    if "Alex Morgan" not in signature:
        missing.append("Alex Morgan")
    if "VP of Product" not in signature:
        missing.append("VP of Product")

    if missing:
        return False, f"Signature is missing: {', '.join(missing)}. Current signature: {signature!r}"

    return True, "Email signature updated correctly."
