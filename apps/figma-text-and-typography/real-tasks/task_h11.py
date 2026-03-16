"""
Task: Enable vertical trim on both the Page Title and Section Header.
Verify: Layers named "Page Title" and "Section Header" both have verticalTrim=True.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    text_layers = state.get("textLayers", [])

    target_names = ["Page Title", "Section Header"]
    errors = []

    for name in target_names:
        layer = next((l for l in text_layers if l.get("name") == name), None)
        if layer is None:
            errors.append(f"Layer '{name}' not found")
            continue
        if layer.get("verticalTrim") is not True:
            errors.append(
                f"Layer '{name}' has verticalTrim={layer.get('verticalTrim')}, expected True"
            )

    if errors:
        return False, "; ".join(errors)

    return True, "Both Page Title and Section Header have verticalTrim enabled."
