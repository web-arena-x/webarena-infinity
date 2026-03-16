import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Delete every text style not currently used by any layer."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_styles = state.get("textStyles", [])
    text_layers = state.get("textLayers", [])
    errors = []

    # In seed data, used styles (referenced by at least one layer):
    # ts_001 (Heading/H1), ts_002 (Body/Regular), ts_003 (Heading/H2),
    # ts_005 (Button/Primary), ts_006 (Caption/Small), ts_007 (Code/Inline),
    # ts_008 (Label/SmallCaps)
    used_style_names = {
        "Heading/H1", "Body/Regular", "Heading/H2",
        "Button/Primary", "Caption/Small", "Code/Inline", "Label/SmallCaps"
    }

    # Unused styles that should be deleted:
    # ts_004 (Heading/H3), ts_009 (Body/Large), ts_010 (Heading/Display),
    # ts_011 (Body/Small), ts_012 (Label/Overline)
    should_be_deleted = {"Heading/H3", "Body/Large", "Heading/Display", "Body/Small", "Label/Overline"}

    remaining_names = {s.get("name") for s in text_styles}

    # Check used styles still exist
    for name in used_style_names:
        if name not in remaining_names:
            errors.append(f"Used style '{name}' was deleted but should have been kept.")

    # Check unused styles are gone
    for name in should_be_deleted:
        if name in remaining_names:
            errors.append(f"Unused style '{name}' still exists but should have been deleted.")

    if errors:
        return False, "; ".join(errors)
    return True, "All 5 unused text styles deleted; 7 used styles preserved."
