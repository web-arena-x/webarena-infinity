import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    post = next((p for p in state["feedPosts"] if p["id"] == "post_01"), None)
    if not post:
        return False, "Post 'post_01' not found."
    for comment in post.get("comments", []):
        if "Great tips, thanks for sharing" in comment.get("text", ""):
            return True, "Comment added successfully."
    return False, "Comment 'Great tips, thanks for sharing!' not found on post."
