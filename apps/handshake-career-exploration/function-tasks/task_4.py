import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    post = next((p for p in state["feedPosts"] if p["id"] == "post_02"), None)
    if not post:
        return False, "Post 'post_02' not found."
    if post.get("bookmarked"):
        return False, "Post is still bookmarked."
    if "post_02" in state["currentUser"]["savedPostIds"]:
        return False, "Post ID still in user's savedPostIds."
    return True, "Bookmark removed successfully."
