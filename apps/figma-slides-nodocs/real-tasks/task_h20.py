import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to get state: {resp.status_code}"

    state = resp.json()
    comments = state.get("comments", [])
    presentations = state.get("presentations", [])

    errors = []

    # Seed comments on pres_004: cmt_011, cmt_012, cmt_013, cmt_037 — all should be gone
    pres_004_comment_ids = {"cmt_011", "cmt_012", "cmt_013", "cmt_037"}
    remaining_by_id = [
        c.get("id") for c in comments if c.get("id") in pres_004_comment_ids
    ]
    if remaining_by_id:
        errors.append(f"Original pres_004 comments still present: {remaining_by_id}")

    # Also check by presentationId field — no comments for pres_004 should exist
    remaining_by_pres = [
        c.get("id", "?") for c in comments
        if c.get("presentationId") == "pres_004" or c.get("presId") == "pres_004"
    ]
    if remaining_by_pres:
        errors.append(f"Comments still linked to pres_004: {remaining_by_pres}")

    # pres_004 should have allowComments==false
    pres_map = {p["id"]: p for p in presentations}
    if "pres_004" not in pres_map:
        errors.append("pres_004 (User Research Findings) not found in state")
    else:
        p = pres_map["pres_004"]
        allow_comments = p.get("shareSettings", {}).get("allowComments")
        if allow_comments is not False and allow_comments != 0:
            errors.append(
                f"pres_004 allowComments is {allow_comments!r}, expected false"
            )

    if errors:
        return False, f"pres_004 issues: {'; '.join(errors)}"

    return True, "All comments on User Research Findings deleted and allowComments disabled."
