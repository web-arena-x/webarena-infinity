import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})
    split_inbox = settings.get("splitInbox", {})
    split_ids = split_inbox.get("splits", [])
    splits_array = state.get("splits", [])

    errors = []

    # Check that split_newsletters is not in settings.splitInbox.splits
    if "split_newsletters" in split_ids:
        errors.append(
            "'split_newsletters' still present in settings.splitInbox.splits."
        )

    # Check that no split with id 'split_newsletters' exists in splits array
    newsletters_split = next(
        (s for s in splits_array if s.get("id") == "split_newsletters"),
        None,
    )
    if newsletters_split is not None:
        errors.append(
            f"Split with id 'split_newsletters' still exists in splits array "
            f"(name: '{newsletters_split.get('name')}')."
        )

    if errors:
        return False, " ".join(errors)

    return True, "News split (split_newsletters) successfully removed."
