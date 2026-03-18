import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Expected HTTP 200, got {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])

    pres = next(
        (p for p in presentations if p.get("id") == "pres_001"),
        None,
    )
    if pres is None:
        pres = next(
            (p for p in presentations if "Q1 2026 Product Roadmap" in p.get("title", "")),
            None,
        )
    if pres is None:
        return False, "Q1 2026 Product Roadmap (pres_001) not found"

    pres_id = pres.get("id")
    comments = state.get("comments", [])
    roadmap_comments = [c for c in comments if c.get("presentationId") == pres_id]

    if not roadmap_comments:
        return False, f"No comments found for presentation id '{pres_id}'"

    unresolved = [c for c in roadmap_comments if not c.get("resolved", False)]
    if unresolved:
        unresolved_ids = [c.get("id") for c in unresolved]
        return (
            False,
            f"Found {len(unresolved)} unresolved comment(s) on Q1 Product Roadmap: {unresolved_ids}",
        )

    return (
        True,
        f"All {len(roadmap_comments)} comment(s) on Q1 2026 Product Roadmap are resolved",
    )
