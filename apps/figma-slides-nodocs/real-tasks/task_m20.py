import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Expected HTTP 200, got {resp.status_code}"

    state = resp.json()
    presentations = state.get("presentations", [])

    pres = next(
        (p for p in presentations if p.get("id") == "pres_010"),
        None,
    )
    if pres is None:
        pres = next(
            (p for p in presentations if "Marketing Campaign" in p.get("title", "")),
            None,
        )
    if pres is None:
        return False, "Marketing Campaign presentation (pres_010) not found"

    pres_id = pres.get("id")
    comments = state.get("comments", [])
    marketing_comments = [c for c in comments if c.get("presentationId") == pres_id]

    hero_comment = next(
        (c for c in marketing_comments if "hero visual" in c.get("content", "").lower()),
        None,
    )
    if hero_comment is None:
        all_texts = [c.get("content", "")[:60] for c in marketing_comments]
        return (
            False,
            f"No comment containing 'hero visual' found on Marketing Campaign. Comments: {all_texts}",
        )

    kpis_comment = next(
        (c for c in marketing_comments if "kpi" in c.get("content", "").lower()),
        None,
    )
    if kpis_comment is None:
        all_texts = [c.get("content", "")[:60] for c in marketing_comments]
        return (
            False,
            f"No comment containing 'KPI' found on Marketing Campaign. Comments: {all_texts}",
        )

    errors = []
    if not hero_comment.get("resolved", False):
        errors.append(
            f"Hero visual comment (id={hero_comment.get('id')}) is not resolved"
        )
    if not kpis_comment.get("resolved", False):
        errors.append(
            f"KPIs comment (id={kpis_comment.get('id')}) is not resolved"
        )

    if errors:
        return False, "; ".join(errors)

    return (
        True,
        f"Both hero visual comment (id={hero_comment.get('id')}) and KPIs comment (id={kpis_comment.get('id')}) are resolved",
    )
