"""Create a filter for emails with attachments larger than 5 MB that applies the Reference label and skips the inbox."""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    response = requests.get(f"{server_url}/api/state")
    if response.status_code != 200:
        return False, f"Failed to fetch state: HTTP {response.status_code}"

    state = response.json()
    filters = state.get("filters", [])

    matching_filter = None
    for f in filters:
        criteria = f.get("criteria", {})
        actions = f.get("actions", {})

        has_attachment = criteria.get("hasAttachment") is True
        size_match = criteria.get("size") == 5
        label_match = actions.get("label") == "label_19"
        archive_match = actions.get("archive") is True

        if has_attachment and size_match and label_match and archive_match:
            matching_filter = f
            break

    if matching_filter is None:
        # Provide diagnostic info
        diag = []
        for f in filters:
            criteria = f.get("criteria", {})
            actions = f.get("actions", {})
            diag.append(
                f"filter {f.get('id', '?')}: "
                f"hasAttachment={criteria.get('hasAttachment')}, "
                f"size={criteria.get('size')}, "
                f"label={actions.get('label')}, "
                f"archive={actions.get('archive')}"
            )
        return False, (
            "No filter found with criteria.hasAttachment=True, "
            "criteria.size=5, actions.label='label_19' (Reference), and "
            f"actions.archive=True. Existing filters: {'; '.join(diag)}"
        )

    return True, (
        f"Filter '{matching_filter.get('id', '?')}' matches: attachments > 5MB, "
        "applies Reference label, skips inbox."
    )
