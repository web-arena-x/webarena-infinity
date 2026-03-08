import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Resolve every problem system-wide that currently has 'Controlled' status."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []
    resolved_count = 0

    # These are the problems that should have been Controlled in seed data:
    # prob_002 (Henderson - Essential Hypertension), prob_006 (Henderson - Allergic Rhinitis),
    # prob_016 (Rodriguez-Martinez - Allergic Rhinitis), prob_024 (Zhao - Hypothyroidism),
    # prob_027 (Bergstrom - DM Well-Controlled), prob_028 (Bergstrom - MDD in Remission)
    seed_controlled_ids = {"prob_002", "prob_006", "prob_016", "prob_024", "prob_027", "prob_028"}

    for prob in state.get("problems", []):
        pid = prob.get("id", "")
        if pid in seed_controlled_ids:
            if prob.get("status") == "Controlled":
                errors.append(
                    f"Problem '{prob.get('title', '?')}' ({pid}) still has 'Controlled' status; "
                    f"expected 'Resolved'."
                )
            elif prob.get("status") == "Resolved":
                resolved_count += 1
            else:
                errors.append(
                    f"Problem '{prob.get('title', '?')}' ({pid}) has status "
                    f"'{prob.get('status')}'; expected 'Resolved'."
                )

    # Also check no other problems are still Controlled
    for prob in state.get("problems", []):
        if prob.get("status") == "Controlled" and prob.get("id") not in seed_controlled_ids:
            # This shouldn't happen in seed data, but check anyway
            pass

    remaining_controlled = [
        p for p in state.get("problems", []) if p.get("status") == "Controlled"
    ]
    if remaining_controlled:
        names = [f"'{p.get('title', '?')}'" for p in remaining_controlled]
        errors.append(f"Still have Controlled problems: {', '.join(names)}.")

    if errors:
        return False, " ".join(errors)
    return True, f"All {resolved_count} previously Controlled problems are now Resolved."
