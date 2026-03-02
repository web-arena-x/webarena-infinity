import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    matter = next(
        (m for m in state.get("matters", [])
         if "Vertex" in m.get("description", "") and "Series B" in m.get("description", "")),
        None
    )

    if matter is None:
        return False, "Could not find a matter with description containing 'Vertex' and 'Series B'."

    billing = matter.get("billing", {})

    currency = billing.get("currency", "")
    if currency != "GBP":
        return False, f"Vertex Series B matter billing.currency is '{currency}', expected 'GBP'."

    budget = billing.get("budget", 0)
    if abs(budget - 100000) > 1:
        return False, f"Vertex Series B matter billing.budget is {budget}, expected 100000."

    return True, "Vertex Technologies Series B matter has billing currency GBP and budget $100,000."
