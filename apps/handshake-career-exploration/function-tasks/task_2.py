import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    post = next((p for p in state["feedPosts"] if p["id"] == "post_08"), None)
    if not post:
        return False, "Post 'post_08' not found."
    if post["likes"] > 534:
        return True, f"Post liked successfully. Likes: {post['likes']}."
    return False, f"Post likes not increased. Expected > 534, got {post['likes']}."
