#!/usr/bin/env python3
"""
Verifier sanity check -- for each task, directly apply the expected state
changes via the API, run the verifier, and assert it passes.

Usage:
    python3 sanity_check.py                      # Run all 30 tasks sequentially
    python3 sanity_check.py --workers 4           # Run with 4 parallel server workers
    python3 sanity_check.py --task-id task_e1     # Run a single task
    python3 sanity_check.py --port 9000           # Custom base port
"""

import argparse
import copy
import importlib.util
import json
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone

import requests

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TASKS_DIR = os.path.join(SCRIPT_DIR, "tasks")

# -- Helper: find email by id ------------------------------------------------

def find_email(state, email_id):
    return next(e for e in state["emails"] if e["id"] == email_id)

# -- Seed state construction via Node ----------------------------------------

def get_seed_state():
    """Evaluate js/data.js through Node and return the seed state dict."""
    data_js_path = os.path.join(SCRIPT_DIR, "js", "data.js")
    with open(data_js_path) as f:
        js_code = f.read()

    js_code += """
console.log(JSON.stringify({
    _seedVersion: SEED_DATA_VERSION,
    emails: EMAILS,
    labels: LABELS,
    filters: FILTERS,
    settings: SETTINGS,
    contacts: CONTACTS,
    blockedSenders: BLOCKED_SENDERS,
    currentUser: CURRENT_USER,
    _nextEmailId: Math.max(...EMAILS.map(e => e.id)) + 1,
    _nextLabelId: 30,
    _nextFilterId: 20
}));
"""
    result = subprocess.run(
        ["node", "-"],
        input=js_code,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"Failed to evaluate seed data: {result.stderr}", file=sys.stderr)
        sys.exit(1)
    return json.loads(result.stdout.strip())

# -- Per-task solve functions ------------------------------------------------
# Each function mutates the state dict to match what the verifier expects.

def solve_task_e1(state):
    """Star the email 'Q1 Product Roadmap Review' (id=1)."""
    email = find_email(state, 1)
    email["isStarred"] = True
    email["starType"] = "yellow-star"

def solve_task_e2(state):
    """Mark email 'Design System Update v4.2' (id=6) as read."""
    email = find_email(state, 6)
    email["isRead"] = True

def solve_task_e3(state):
    """Archive email 'Shipping Update: Order #LP-2026-8834' (id=19)."""
    email = find_email(state, 19)
    if "INBOX" in email["labels"]:
        email["labels"].remove("INBOX")
    email["isArchived"] = True

def solve_task_e4(state):
    """Delete email 'Property Listing: 45 Oak Avenue' (id=15)."""
    email = find_email(state, 15)
    email["isTrashed"] = True
    if "INBOX" in email["labels"]:
        email["labels"].remove("INBOX")

def solve_task_e5(state):
    """Mark email 'CI/CD Pipeline Migration Plan' (id=9) as important."""
    email = find_email(state, 9)
    email["isImportant"] = True
    if "IMPORTANT" not in email["labels"]:
        email["labels"].append("IMPORTANT")

def solve_task_e6(state):
    """Remove star from 'Partnership Opportunity - Series B Company' (id=7)."""
    email = find_email(state, 7)
    email["isStarred"] = False
    email["starType"] = None

def solve_task_e7(state):
    """Move spam email (id=93) out of spam and back to inbox."""
    email = find_email(state, 93)
    email["isSpam"] = False
    if "INBOX" not in email["labels"]:
        email["labels"].append("INBOX")

def solve_task_e8(state):
    """Report Amazon email (id=44) as spam."""
    email = find_email(state, 44)
    email["isSpam"] = True
    if "INBOX" in email["labels"]:
        email["labels"].remove("INBOX")

def solve_task_e9(state):
    """Unblock 'annoying@daily-deals.biz' from blocked senders."""
    state["blockedSenders"] = [
        b for b in state["blockedSenders"]
        if b["email"] != "annoying@daily-deals.biz"
    ]

def solve_task_e10(state):
    """Turn off conversation view."""
    state["settings"]["conversationView"] = False

def solve_task_m1(state):
    """Apply label 'Action Required' (label_17) to email id=20."""
    email = find_email(state, 20)
    if "label_17" not in email["labels"]:
        email["labels"].append("label_17")

def solve_task_m2(state):
    """Create a new label 'Urgent' with red color."""
    state["labels"].append({
        "id": "label_30",
        "name": "Urgent",
        "type": "user",
        "color": {"background": "#cc3333", "text": "#fff"},
        "visible": True,
        "parentId": None,
        "messageCount": 0,
        "unreadCount": 0,
    })
    state["_nextLabelId"] = state.get("_nextLabelId", 30) + 1

def solve_task_m3(state):
    """Change inbox type to 'unread_first'."""
    state["settings"]["inboxType"] = "unread_first"

def solve_task_m4(state):
    """Delete filter matching sarah.chen@techcorp.io (filter_5)."""
    state["filters"] = [
        f for f in state["filters"] if f["id"] != "filter_5"
    ]

def solve_task_m5(state):
    """Rename label 'Waiting For Reply' (label_18) to 'Pending Response'."""
    for label in state["labels"]:
        if label["id"] == "label_18":
            label["name"] = "Pending Response"
            break

def solve_task_m6(state):
    """Change theme to dark."""
    state["settings"]["theme"] = "dark"

def solve_task_m7(state):
    """Disable social category."""
    state["settings"]["categoriesEnabled"]["social"] = False

def solve_task_m8(state):
    """Move email id=14 to 'Travel' label and remove from inbox."""
    email = find_email(state, 14)
    if "label_4" not in email["labels"]:
        email["labels"].append("label_4")
    if "INBOX" in email["labels"]:
        email["labels"].remove("INBOX")

def solve_task_m9(state):
    """Change undo send delay to 30 seconds."""
    state["settings"]["undoSendDelay"] = 30

def solve_task_m10(state):
    """Set email density to compact."""
    state["settings"]["density"] = "compact"

def solve_task_h1(state):
    """Create filter for notifications@vercel.com with label Work + mark read."""
    state["filters"].append({
        "id": "filter_13",
        "criteria": {
            "from": "notifications@vercel.com",
            "to": "",
            "subject": "",
            "hasWords": "",
            "doesntHave": "",
            "hasAttachment": False,
            "size": None,
            "sizeUnit": "MB",
            "sizeComparison": "greater",
        },
        "actions": {
            "label": "label_1",
            "archive": False,
            "markRead": True,
            "star": False,
            "forward": None,
            "delete": False,
            "neverSpam": False,
            "alwaysImportant": False,
            "neverImportant": False,
            "category": None,
        },
        "enabled": True,
        "createdAt": datetime.now(timezone.utc).isoformat(),
    })
    state["_nextFilterId"] = state.get("_nextFilterId", 20) + 1

def solve_task_h2(state):
    """Create sub-label 'DevOps' under 'Work', apply to email id=9."""
    state["labels"].append({
        "id": "label_30",
        "name": "DevOps",
        "type": "user",
        "color": {"background": "#13828b", "text": "#fff"},
        "visible": True,
        "parentId": "label_1",
        "messageCount": 0,
        "unreadCount": 0,
    })
    email = find_email(state, 9)
    if "label_30" not in email["labels"]:
        email["labels"].append("label_30")
    state["_nextLabelId"] = state.get("_nextLabelId", 30) + 1

def solve_task_h3(state):
    """Archive all unread promotions emails that are in inbox."""
    for email in state["emails"]:
        if (email.get("category") == "promotions"
                and not email.get("isRead", True)
                and "INBOX" in email.get("labels", [])):
            email["labels"].remove("INBOX")
            email["isArchived"] = True

def solve_task_h4(state):
    """Email id=28: ensure Finance label, star with yellow-star, mark important."""
    email = find_email(state, 28)
    if "label_3" not in email["labels"]:
        email["labels"].append("label_3")
    email["isStarred"] = True
    email["starType"] = "yellow-star"
    email["isImportant"] = True
    if "IMPORTANT" not in email["labels"]:
        email["labels"].append("IMPORTANT")

def solve_task_h5(state):
    """Set inbox type to multiple_inboxes, configure first section."""
    state["settings"]["inboxType"] = "multiple_inboxes"
    state["settings"]["multipleInboxSections"][0]["query"] = "label:Action Required"
    state["settings"]["multipleInboxSections"][0]["name"] = "Action Items"

def solve_task_h6(state):
    """Set preview pane to right and max page size to 25."""
    state["settings"]["previewPane"] = "right"
    state["settings"]["maxPageSize"] = 25

def solve_task_h7(state):
    """Delete label 'Newsletters' (label_6) and remove from all emails."""
    state["labels"] = [l for l in state["labels"] if l["id"] != "label_6"]
    for email in state["emails"]:
        if "label_6" in email.get("labels", []):
            email["labels"].remove("label_6")

def solve_task_h8(state):
    """Compose and send a new email to sarah.chen@techcorp.io."""
    next_id = state.get("_nextEmailId", 200)
    state["emails"].append({
        "id": next_id,
        "threadId": "thread_" + str(next_id),
        "from": {
            "name": "Alex Johnson",
            "email": "alex.johnson@gmail.com",
        },
        "to": [{"name": "Sarah Chen", "email": "sarah.chen@techcorp.io"}],
        "cc": [],
        "bcc": [],
        "subject": "Project Update Meeting",
        "snippet": "Hi Sarah, can we schedule...",
        "body": "Hi Sarah, can we schedule a project update meeting for next week? Thanks, Alex",
        "date": datetime.now(timezone.utc).isoformat(),
        "isRead": True,
        "isStarred": False,
        "starType": None,
        "isImportant": False,
        "labels": ["SENT"],
        "category": "primary",
        "hasAttachments": False,
        "attachments": [],
        "isSnoozed": False,
        "snoozeUntil": None,
        "isTrashed": False,
        "isSpam": False,
        "isArchived": False,
        "isDraft": False,
        "isSent": True,
        "isMuted": False,
    })
    state["_nextEmailId"] = next_id + 1

def solve_task_h9(state):
    """Remove 'Action Required' label from email id=129, mark as read."""
    email = find_email(state, 129)
    if "label_17" in email["labels"]:
        email["labels"].remove("label_17")
    email["isRead"] = True

def solve_task_h10(state):
    """Disable keyboard shortcuts, importance markers; set reply behavior to reply_all."""
    state["settings"]["keyboardShortcutsEnabled"] = False
    state["settings"]["importanceMarkers"] = False
    state["settings"]["defaultReplyBehavior"] = "reply_all"


SOLVERS = {
    "task_e1": solve_task_e1, "task_e2": solve_task_e2,
    "task_e3": solve_task_e3, "task_e4": solve_task_e4,
    "task_e5": solve_task_e5, "task_e6": solve_task_e6,
    "task_e7": solve_task_e7, "task_e8": solve_task_e8,
    "task_e9": solve_task_e9, "task_e10": solve_task_e10,
    "task_m1": solve_task_m1, "task_m2": solve_task_m2,
    "task_m3": solve_task_m3, "task_m4": solve_task_m4,
    "task_m5": solve_task_m5, "task_m6": solve_task_m6,
    "task_m7": solve_task_m7, "task_m8": solve_task_m8,
    "task_m9": solve_task_m9, "task_m10": solve_task_m10,
    "task_h1": solve_task_h1, "task_h2": solve_task_h2,
    "task_h3": solve_task_h3, "task_h4": solve_task_h4,
    "task_h5": solve_task_h5, "task_h6": solve_task_h6,
    "task_h7": solve_task_h7, "task_h8": solve_task_h8,
    "task_h9": solve_task_h9, "task_h10": solve_task_h10,
}

# -- Server lifecycle --------------------------------------------------------

def start_server(port):
    return subprocess.Popen(
        [sys.executable, "server.py", "--port", str(port)],
        cwd=SCRIPT_DIR,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

def wait_for_server(port, timeout=10):
    url = f"http://localhost:{port}/"
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            r = requests.get(url, timeout=2)
            if r.status_code == 200:
                return True
        except requests.ConnectionError:
            pass
        time.sleep(0.3)
    return False

def stop_server(proc):
    if proc.poll() is not None:
        return
    proc.terminate()
    try:
        proc.wait(timeout=5)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.wait()

# -- Verifier loading --------------------------------------------------------

def load_verifier(task_id):
    path = os.path.join(TASKS_DIR, f"{task_id}.py")
    spec = importlib.util.spec_from_file_location(task_id, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.verify

# -- Worker: run a batch of tasks on one server ------------------------------

def run_tasks(task_ids, port, seed_state):
    """Start a server on *port*, run each task, return list of (task_id, passed, message)."""
    results = []
    proc = start_server(port)
    try:
        if not wait_for_server(port):
            for tid in task_ids:
                results.append((tid, False, "Server failed to start"))
            return results

        base = f"http://localhost:{port}"

        # First PUT sets _seed_state on the server
        r = requests.put(f"{base}/api/state", json=seed_state, timeout=5)
        if r.status_code != 200:
            for tid in task_ids:
                results.append((tid, False, "Failed to seed server state"))
            return results

        for tid in task_ids:
            try:
                # Reset to seed
                requests.post(f"{base}/api/reset", timeout=5)

                # Fetch clean seed state
                state = requests.get(f"{base}/api/state", timeout=5).json()

                # Apply expected changes
                SOLVERS[tid](state)

                # Push solved state
                requests.put(f"{base}/api/state", json=state, timeout=5)

                # Run the verifier
                verify = load_verifier(tid)
                passed, message = verify(base)
                results.append((tid, passed, message))
            except Exception as e:
                results.append((tid, False, f"Error: {e}"))
    finally:
        stop_server(proc)
    return results

# -- Main --------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Verifier sanity check")
    parser.add_argument("--workers", type=int, default=1,
                        help="Number of parallel server workers (default: 1)")
    parser.add_argument("--task-id", type=str,
                        help="Run a single task (e.g. task_e1)")
    parser.add_argument("--port", type=int, default=18000,
                        help="Base port for servers (default: 18000)")
    args = parser.parse_args()

    # Determine which tasks to run
    if args.task_id:
        task_ids = [args.task_id]
    else:
        with open(os.path.join(SCRIPT_DIR, "tasks.json")) as f:
            task_ids = [t["id"] for t in json.load(f)]

    for tid in task_ids:
        if tid not in SOLVERS:
            print(f"Unknown task: {tid}", file=sys.stderr)
            sys.exit(1)

    # Build seed state from js/data.js
    print("Loading seed state via Node...")
    seed_state = get_seed_state()
    print(f"Seed loaded: {len(seed_state['emails'])} emails, "
          f"{len(seed_state['labels'])} labels, "
          f"{len(seed_state['filters'])} filters")

    num_workers = min(args.workers, len(task_ids))
    all_results = []

    if num_workers <= 1:
        # Sequential -- single server
        all_results = run_tasks(task_ids, args.port, seed_state)
    else:
        # Parallel -- one server per worker, tasks round-robin partitioned
        chunks = [[] for _ in range(num_workers)]
        for i, tid in enumerate(task_ids):
            chunks[i % num_workers].append(tid)

        with ThreadPoolExecutor(max_workers=num_workers) as pool:
            futures = {
                pool.submit(run_tasks, chunk, args.port + i, seed_state): i
                for i, chunk in enumerate(chunks) if chunk
            }
            for f in as_completed(futures):
                all_results.extend(f.result())

    # Sort by original task order
    order = {tid: i for i, tid in enumerate(task_ids)}
    all_results.sort(key=lambda r: order.get(r[0], 999))

    # Print results
    print()
    passed_count = 0
    failed = []
    for tid, passed, message in all_results:
        status = "PASS" if passed else "FAIL"
        if passed:
            passed_count += 1
        else:
            failed.append(tid)
        print(f"  {status}  {tid:12s}  {message}")

    total = len(all_results)
    print(f"\n{passed_count}/{total} passed")
    if failed:
        print(f"Failed: {', '.join(failed)}")
        sys.exit(1)
    else:
        print("All verifiers passed!")

if __name__ == "__main__":
    main()
