import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    groups = state.get("contactGroups", [])
    group_names = [g.get("name") for g in groups]

    has_book_club = "Book Club" in group_names
    has_reading_group = "Reading Group" in group_names

    if has_book_club and not has_reading_group:
        return False, "The 'Book Club' label still exists and 'Reading Group' was not found. The rename did not happen."

    if has_book_club and has_reading_group:
        return False, "Both 'Book Club' and 'Reading Group' exist. The label was not renamed; a new one may have been created instead."

    if not has_book_club and not has_reading_group:
        return False, "Neither 'Book Club' nor 'Reading Group' found. The label may have been deleted instead of renamed."

    # not has_book_club and has_reading_group
    return True, "The 'Book Club' label has been successfully renamed to 'Reading Group'."
