import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    post = next((p for p in state["feedPosts"] if p["id"] == "post_09"), None)
    if not post:
        return False, "Post 'post_09' not found."
    for comment in post.get("comments", []):
        if "How selective is the application process" in comment.get("text", "") and comment.get("isAnonymous"):
            return True, "Anonymous comment added successfully."
    return False, "Anonymous comment not found on post."
