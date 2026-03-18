import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Expected HTTP 200, got {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])

    pres = next(
        (p for p in presentations if p.get("id") == "pres_016"),
        None,
    )
    if pres is None:
        pres = next(
            (p for p in presentations if "Website Redesign Proposal" in p.get("title", "")),
            None,
        )
    if pres is None:
        return False, "Website Redesign Proposal — TechStartup.io (pres_016) not found"

    pres_id = pres.get("id")
    comments = state.get("comments", [])
    remaining = [c for c in comments if c.get("presentationId") == pres_id]

    if remaining:
        ids = [c.get("id") for c in remaining]
        return (
            False,
            f"Expected 0 comments on Website Redesign Proposal (id={pres_id}), found {len(remaining)}: {ids}",
        )

    return True, f"All comments deleted from Website Redesign Proposal — TechStartup.io (id={pres_id})"
