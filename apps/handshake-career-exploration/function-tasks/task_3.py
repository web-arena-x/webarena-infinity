import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    post = next((p for p in state["feedPosts"] if p["id"] == "post_06"), None)
    if not post:
        return False, "Post 'post_06' not found."
    if not post.get("bookmarked"):
        return False, "Post is not bookmarked."
    if "post_06" not in state["currentUser"]["savedPostIds"]:
        return False, "Post ID not in user's savedPostIds."
    return True, "Post bookmarked and saved successfully."
