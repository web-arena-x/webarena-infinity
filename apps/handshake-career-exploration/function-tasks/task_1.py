import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    for post in state["feedPosts"]:
        if post["authorType"] == "student" and post["authorId"] == state["currentUser"]["id"]:
            if "Looking for advice on product management interview prep" in post["content"]:
                return True, "Post created successfully with correct content."
    return False, "No post found with the expected content."
