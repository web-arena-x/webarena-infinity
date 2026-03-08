import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    errors = []

    # Highest amount gift card: Target gc_003 = $100 to Marcus Williams (marcus.williams@email.com)
    # Should have a new $50 Target gift card for Marcus Williams

    gift_cards = state.get("giftCards", [])
    seed_gc_ids = {"gc_001", "gc_002", "gc_003", "gc_004", "gc_005"}
    new_target_gcs = [
        gc for gc in gift_cards
        if gc.get("id") not in seed_gc_ids
        and gc.get("merchantName") == "Target"
        and gc.get("amount") == 50
    ]

    if not new_target_gcs:
        errors.append("No new $50 Target gift card found.")
    else:
        gc = new_target_gcs[0]
        if gc.get("recipientEmail") != "marcus.williams@email.com":
            errors.append(
                f"Gift card recipient email is '{gc.get('recipientEmail')}', "
                f"expected 'marcus.williams@email.com'."
            )
        if gc.get("recipientName") != "Marcus Williams":
            errors.append(
                f"Gift card recipient name is '{gc.get('recipientName')}', "
                f"expected 'Marcus Williams'."
            )
        if gc.get("message") != "Another one for you!":
            errors.append(
                f"Gift card message is '{gc.get('message')}', "
                f"expected 'Another one for you!'."
            )

    if errors:
        return False, " ".join(errors)
    return True, "Sent $50 Target gift card to Marcus Williams (matching highest-amount gift card)."
