import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    for post in state["feedPosts"]:
        if post["authorType"] == "student" and post["authorId"] == state["currentUser"]["id"]:
            if "study group for system design" in post.get("content", "").lower():
                if post.get("audience") == "school":
                    return True, "Post created with correct content and school audience."
                return False, f"Post found but audience is '{post.get('audience')}', expected 'school'."
    return False, "No post found with the expected content."
