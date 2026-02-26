#!/usr/bin/env python3
"""
Sanity check for Gmail function-test tasks.

For each task, directly applies the expected end-state (bypassing the agent),
then runs the verifier and asserts it passes.

Usage:
    python3 sanity_check_function.py                     # All tasks, sequential
    python3 sanity_check_function.py --workers N          # N parallel environments
    python3 sanity_check_function.py --task-id task_5     # Single task
    python3 sanity_check_function.py --port 9000          # Custom base port
"""
import argparse
import importlib.util
import json
import os
import signal
import socket
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from copy import deepcopy
from pathlib import Path

import requests

APP_DIR = Path(__file__).resolve().parent
TASKS_FILE = APP_DIR / "function-tasks.json"

# JS snippet to evaluate data.js and emit the seed state as JSON
_SEED_STATE_JS = """
const fs = require('fs');
const vm = require('vm');
const code = fs.readFileSync(process.argv[1], 'utf8');
vm.runInThisContext(code);

// Replicate what AppState._loadSeedData() does
const state = {
    _seedVersion: SEED_DATA_VERSION,
    emails: JSON.parse(JSON.stringify(EMAILS)),
    labels: JSON.parse(JSON.stringify(LABELS)),
    filters: JSON.parse(JSON.stringify(FILTERS)),
    settings: JSON.parse(JSON.stringify(SETTINGS)),
    contacts: JSON.parse(JSON.stringify(CONTACTS)),
    blockedSenders: JSON.parse(JSON.stringify(BLOCKED_SENDERS)),
    currentUser: JSON.parse(JSON.stringify(CURRENT_USER)),
    _nextEmailId: EMAILS.length > 0 ? Math.max(...EMAILS.map(e => e.id)) + 1 : 200,
    _nextLabelId: 30,
    _nextFilterId: 20,
};
process.stdout.write(JSON.stringify(state));
"""


# ── helpers ──────────────────────────────────────────────────────────

def find_entity(entities, **kwargs):
    """Find an entity by attribute match. Raises if not found."""
    for e in entities:
        if all(e.get(k) == v for k, v in kwargs.items()):
            return e
    raise ValueError(f"Entity not found: {kwargs}")


def find_email_by_subject(state, subject, **extra):
    """Find an email by subject (and optional extra filters)."""
    for e in state["emails"]:
        if e["subject"] == subject:
            if all(e.get(k) == v for k, v in extra.items()):
                return e
    raise ValueError(f"Email not found: subject={subject!r}, {extra}")


def find_email_by_subject_and_sender(state, subject, sender_email):
    """Find an email by subject and sender email."""
    for e in state["emails"]:
        if e["subject"] == subject and e["from"]["email"] == sender_email:
            return e
    raise ValueError(f"Email not found: subject={subject!r}, from={sender_email!r}")


def find_label_by_name(state, name):
    """Find a label by name."""
    for l in state["labels"]:
        if l["name"] == name:
            return l
    raise ValueError(f"Label not found: {name!r}")


def find_filter_by_from(state, from_addr):
    """Find a filter by criteria.from."""
    for f in state["filters"]:
        if f["criteria"]["from"] == from_addr:
            return f
    raise ValueError(f"Filter not found with from: {from_addr!r}")


# ── solve functions ──────────────────────────────────────────────────

def solve_task_1(state):
    """Mark email 'Q1 Product Roadmap Review' as read."""
    email = find_email_by_subject(state, "Q1 Product Roadmap Review")
    email["isRead"] = True


def solve_task_2(state):
    """Mark email 'Monthly Financial Report - January 2026' as unread."""
    email = find_email_by_subject(state, "Monthly Financial Report - January 2026")
    email["isRead"] = False


def solve_task_3(state):
    """Star email 'Re: Platform Performance Issues'."""
    email = find_email_by_subject(state, "Re: Platform Performance Issues")
    email["isStarred"] = True
    email["starType"] = "yellow-star"


def solve_task_4(state):
    """Unstar email 'API Integration Issue' from Priya Sharma."""
    email = find_email_by_subject_and_sender(
        state, "API Integration Issue", "priya.sharma@cloudnine.dev"
    )
    email["isStarred"] = False
    email["starType"] = None


def solve_task_5(state):
    """Mark email 'Office Renovation Plans' as important."""
    email = find_email_by_subject(state, "Office Renovation Plans")
    email["isImportant"] = True
    if "IMPORTANT" not in email["labels"]:
        email["labels"].append("IMPORTANT")


def solve_task_6(state):
    """Remove important from email 'Q1 Product Roadmap Review'."""
    email = find_email_by_subject_and_sender(
        state, "Q1 Product Roadmap Review", "sarah.chen@techcorp.io"
    )
    email["isImportant"] = False
    email["labels"] = [l for l in email["labels"] if l != "IMPORTANT"]


def solve_task_7(state):
    """Archive email 'Volunteer Event: Spring Health Fair'."""
    email = find_email_by_subject(state, "Volunteer Event: Spring Health Fair")
    email["isArchived"] = True
    email["labels"] = [l for l in email["labels"] if l != "INBOX"]


def solve_task_8(state):
    """Trash email 'Design System Update v4.2'."""
    email = find_email_by_subject(state, "Design System Update v4.2")
    email["isTrashed"] = True
    email["labels"] = [l for l in email["labels"] if l != "INBOX"]


def solve_task_9(state):
    """Mark email 'Your recommendations: Tech deals of the week' as spam."""
    email = find_email_by_subject(state, "Your recommendations: Tech deals of the week")
    email["isSpam"] = True
    email["labels"] = [l for l in email["labels"] if l != "INBOX"]


def solve_task_10(state):
    """Snooze email 'CI/CD Pipeline Migration Plan' until March 1, 2026."""
    email = find_email_by_subject(state, "CI/CD Pipeline Migration Plan")
    email["isSnoozed"] = True
    email["snoozeUntil"] = "2026-03-01T08:00:00.000Z"
    email["labels"] = [l for l in email["labels"] if l != "INBOX"]


def solve_task_11(state):
    """Mute conversation 'Quarterly Team Dinner'."""
    email = find_email_by_subject_and_sender(
        state, "Quarterly Team Dinner", "sarah.chen@techcorp.io"
    )
    email["isMuted"] = True
    email["isArchived"] = True
    email["labels"] = [l for l in email["labels"] if l != "INBOX"]


def solve_task_12(state):
    """Apply 'Finance' label to email 'SaaS Platform Q1 Pricing Update'."""
    email = find_email_by_subject(state, "SaaS Platform Q1 Pricing Update")
    finance_label = find_label_by_name(state, "Finance")
    if finance_label["id"] not in email["labels"]:
        email["labels"].append(finance_label["id"])


def solve_task_13(state):
    """Remove 'Work' label from email 'Office Renovation Plans'."""
    email = find_email_by_subject(state, "Office Renovation Plans")
    work_label = find_label_by_name(state, "Work")
    email["labels"] = [l for l in email["labels"] if l != work_label["id"]]


def solve_task_14(state):
    """Create label 'Urgent'."""
    next_id = state.get("_nextLabelId", 30)
    new_label = {
        "id": f"label_{next_id}",
        "name": "Urgent",
        "type": "user",
        "color": None,
        "visible": True,
        "parentId": None,
        "messageCount": 0,
        "unreadCount": 0,
    }
    state["labels"].append(new_label)
    state["_nextLabelId"] = next_id + 1


def solve_task_15(state):
    """Create label 'Deadlines' nested under 'Work'."""
    work_label = find_label_by_name(state, "Work")
    next_id = state.get("_nextLabelId", 30)
    new_label = {
        "id": f"label_{next_id}",
        "name": "Deadlines",
        "type": "user",
        "color": None,
        "visible": True,
        "parentId": work_label["id"],
        "messageCount": 0,
        "unreadCount": 0,
    }
    state["labels"].append(new_label)
    state["_nextLabelId"] = next_id + 1


def solve_task_16(state):
    """Rename 'Receipts' label to 'Purchase Receipts'."""
    label = find_entity(state["labels"], id="label_5")
    label["name"] = "Purchase Receipts"


def solve_task_17(state):
    """Delete 'Education' label (label_8) and remove from all emails."""
    label_id = "label_8"
    # Remove label from all emails
    for email in state["emails"]:
        email["labels"] = [l for l in email["labels"] if l != label_id]
    # Remove the label itself
    state["labels"] = [l for l in state["labels"] if l["id"] != label_id]


def solve_task_18(state):
    """Send email to sarah.chen@techcorp.io with subject 'Meeting Follow-up'."""
    next_id = state.get("_nextEmailId", 200)
    new_email = {
        "id": next_id,
        "threadId": f"thread_{next_id}",
        "from": {
            "name": state["currentUser"]["name"],
            "email": state["currentUser"]["email"],
        },
        "to": [{"name": "Sarah Chen", "email": "sarah.chen@techcorp.io"}],
        "cc": [],
        "bcc": [],
        "subject": "Meeting Follow-up",
        "snippet": "Thanks for the update on the project.",
        "body": "Thanks for the update on the project.",
        "date": "2026-02-26T12:00:00.000Z",
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
    }
    state["emails"].insert(0, new_email)
    state["_nextEmailId"] = next_id + 1


def solve_task_19(state):
    """Save draft email to david.kim@financeplus.com with subject 'Budget Discussion'."""
    next_id = state.get("_nextEmailId", 200)
    new_draft = {
        "id": next_id,
        "threadId": f"thread_{next_id}",
        "from": {
            "name": state["currentUser"]["name"],
            "email": state["currentUser"]["email"],
        },
        "to": [{"name": "david.kim@financeplus.com", "email": "david.kim@financeplus.com"}],
        "cc": [],
        "bcc": [],
        "subject": "Budget Discussion",
        "snippet": "Let us discuss the Q2 budget next week.",
        "body": "Let us discuss the Q2 budget next week.",
        "date": "2026-02-26T12:00:00.000Z",
        "isRead": True,
        "isStarred": False,
        "starType": None,
        "isImportant": False,
        "labels": ["DRAFT"],
        "category": "primary",
        "hasAttachments": False,
        "attachments": [],
        "isSnoozed": False,
        "snoozeUntil": None,
        "isTrashed": False,
        "isSpam": False,
        "isArchived": False,
        "isDraft": True,
        "isSent": False,
        "isMuted": False,
    }
    state["emails"].insert(0, new_draft)
    state["_nextEmailId"] = next_id + 1


def solve_task_20(state):
    """Create filter: from 'noreply@medium.com', apply Newsletters label, archive."""
    newsletters_label = find_label_by_name(state, "Newsletters")
    next_id = state.get("_nextFilterId", 20)
    new_filter = {
        "id": f"filter_{next_id}",
        "criteria": {
            "from": "noreply@medium.com",
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
            "label": newsletters_label["id"],
            "archive": True,
            "markRead": False,
            "star": False,
            "forward": None,
            "delete": False,
            "neverSpam": False,
            "alwaysImportant": False,
            "neverImportant": False,
            "category": None,
        },
        "enabled": True,
        "createdAt": "2026-02-26T12:00:00.000Z",
    }
    state["filters"].append(new_filter)
    state["_nextFilterId"] = next_id + 1


def solve_task_21(state):
    """Delete filter matching from 'notifications@linkedin.com'."""
    state["filters"] = [
        f for f in state["filters"]
        if f["criteria"]["from"] != "notifications@linkedin.com"
    ]


def solve_task_22(state):
    """Change theme to dark."""
    state["settings"]["theme"] = "dark"


def solve_task_23(state):
    """Change density to compact."""
    state["settings"]["density"] = "compact"


def solve_task_24(state):
    """Disable conversation view."""
    state["settings"]["conversationView"] = False


def solve_task_25(state):
    """Change undo send delay to 30."""
    state["settings"]["undoSendDelay"] = 30


def solve_task_26(state):
    """Disable Social category."""
    state["settings"]["categoriesEnabled"]["social"] = False


def solve_task_27(state):
    """Block sender 'omar.ar@consulting.group'."""
    state["blockedSenders"].append({
        "email": "omar.ar@consulting.group",
        "blockedAt": "2026-02-26T12:00:00.000Z",
    })


def solve_task_28(state):
    """Unblock sender 'spam@marketing-blast.com'."""
    state["blockedSenders"] = [
        b for b in state["blockedSenders"]
        if b["email"] != "spam@marketing-blast.com"
    ]


def solve_task_29(state):
    """Move email 'Congratulations! You won $10,000!' from Trash to Inbox."""
    email = next(
        e for e in state["emails"]
        if "Congratulations" in e["subject"] and "won" in e["subject"]
    )
    email["isTrashed"] = False
    email["isSpam"] = False
    if "INBOX" not in email["labels"]:
        email["labels"].append("INBOX")


def solve_task_30(state):
    """Move email 'Interview Request: Tech Innovation Panel' to Updates category."""
    email = find_email_by_subject(state, "Interview Request: Tech Innovation Panel")
    email["category"] = "updates"
    email["labels"] = [l for l in email["labels"] if not l.startswith("CATEGORY_")]
    email["labels"].append("CATEGORY_UPDATES")


SOLVERS = {
    "task_1": solve_task_1,
    "task_2": solve_task_2,
    "task_3": solve_task_3,
    "task_4": solve_task_4,
    "task_5": solve_task_5,
    "task_6": solve_task_6,
    "task_7": solve_task_7,
    "task_8": solve_task_8,
    "task_9": solve_task_9,
    "task_10": solve_task_10,
    "task_11": solve_task_11,
    "task_12": solve_task_12,
    "task_13": solve_task_13,
    "task_14": solve_task_14,
    "task_15": solve_task_15,
    "task_16": solve_task_16,
    "task_17": solve_task_17,
    "task_18": solve_task_18,
    "task_19": solve_task_19,
    "task_20": solve_task_20,
    "task_21": solve_task_21,
    "task_22": solve_task_22,
    "task_23": solve_task_23,
    "task_24": solve_task_24,
    "task_25": solve_task_25,
    "task_26": solve_task_26,
    "task_27": solve_task_27,
    "task_28": solve_task_28,
    "task_29": solve_task_29,
    "task_30": solve_task_30,
}


# ── server management ────────────────────────────────────────────────

def generate_seed_state():
    """Use Node.js to evaluate data.js and produce the seed state JSON."""
    data_js = str(APP_DIR / "js" / "data.js")
    result = subprocess.run(
        ["node", "-e", _SEED_STATE_JS, data_js],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"Failed to generate seed state:\n{result.stderr}")
    return json.loads(result.stdout)


def seed_server(server_url, seed_state):
    """PUT the seed state to the server to establish the baseline."""
    resp = requests.put(
        f"{server_url}/api/state",
        json=seed_state,
        headers={"Content-Type": "application/json"},
    )
    if resp.status_code != 200:
        raise RuntimeError(f"Failed to seed server: HTTP {resp.status_code}")


def find_free_port(start=9000):
    """Find a free port starting from `start`."""
    port = start
    while port < start + 100:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("", port))
                return port
            except OSError:
                port += 1
    raise RuntimeError(f"No free port found in range {start}-{start+100}")


def start_server(port):
    """Start the Gmail server on the given port."""
    proc = subprocess.Popen(
        [sys.executable, "server.py", "--port", str(port)],
        cwd=str(APP_DIR),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    # Wait for server to be ready
    for _ in range(30):
        try:
            requests.get(f"http://localhost:{port}/", timeout=1)
            return proc
        except (requests.ConnectionError, requests.Timeout):
            time.sleep(0.2)
    proc.kill()
    raise RuntimeError(f"Server failed to start on port {port}")


def stop_server(proc):
    """Stop the server process."""
    if proc and proc.poll() is None:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()


# ── task runner ──────────────────────────────────────────────────────

def load_tasks():
    """Load task definitions from function-tasks.json."""
    with open(TASKS_FILE) as f:
        return json.load(f)


def load_verifier(verify_path):
    """Dynamically load a verifier module."""
    full_path = APP_DIR / verify_path
    spec = importlib.util.spec_from_file_location("verifier", str(full_path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.verify


def run_single_task(task, server_url):
    """Reset → solve → verify for a single task."""
    task_id = task["id"]
    solver = SOLVERS.get(task_id)
    if not solver:
        return task_id, False, f"No solver defined for {task_id}"

    try:
        # 1. Reset to seed state
        resp = requests.post(f"{server_url}/api/reset")
        if resp.status_code != 200:
            return task_id, False, f"Reset failed: HTTP {resp.status_code}"

        # Wait briefly for reset to settle
        time.sleep(0.3)

        # 2. Read seed state
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return task_id, False, f"Could not read state after reset: HTTP {resp.status_code}"
        state = resp.json()

        # 3. Apply the solve function
        solver(state)

        # 4. Write solved state back
        resp = requests.put(
            f"{server_url}/api/state",
            json=state,
            headers={"Content-Type": "application/json"},
        )
        if resp.status_code != 200:
            return task_id, False, f"Could not write state: HTTP {resp.status_code}"

        # 5. Run the verifier
        verify_fn = load_verifier(task["verify"])
        passed, message = verify_fn(server_url)
        return task_id, passed, message

    except Exception as e:
        return task_id, False, f"Exception: {e}"


def run_tasks_sequential(tasks, port, seed_state):
    """Run all tasks sequentially on a single server."""
    proc = start_server(port)
    server_url = f"http://localhost:{port}"
    results = []
    try:
        # Seed the server with initial state so GET /api/state works
        seed_server(server_url, seed_state)
        for task in tasks:
            result = run_single_task(task, server_url)
            results.append(result)
            status = "\033[32m  PASS\033[0m" if result[1] else "\033[31m  FAIL\033[0m"
            print(f"{status}  {result[0]:12s}  {result[2]}")
    finally:
        stop_server(proc)
    return results


def run_tasks_parallel(tasks, workers, base_port, seed_state):
    """Run tasks in parallel across multiple server instances."""
    results = []

    def worker_fn(task, port):
        proc = start_server(port)
        server_url = f"http://localhost:{port}"
        try:
            seed_server(server_url, seed_state)
            return run_single_task(task, server_url)
        finally:
            stop_server(proc)

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {}
        for i, task in enumerate(tasks):
            port = base_port + i
            future = executor.submit(worker_fn, task, port)
            futures[future] = task["id"]

        for future in as_completed(futures):
            result = future.result()
            results.append(result)
            status = "\033[32m  PASS\033[0m" if result[1] else "\033[31m  FAIL\033[0m"
            print(f"{status}  {result[0]:12s}  {result[2]}")

    return results


# ── main ─────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Gmail function-task sanity check")
    parser.add_argument("--task-id", type=str, help="Run a single task by ID")
    parser.add_argument("--workers", type=int, default=1, help="Number of parallel workers")
    parser.add_argument("--port", type=int, default=9500, help="Base port for servers")
    args = parser.parse_args()

    tasks = load_tasks()
    if args.task_id:
        tasks = [t for t in tasks if t["id"] == args.task_id]
        if not tasks:
            print(f"Task '{args.task_id}' not found.")
            sys.exit(1)

    print("Generating seed state from JS data...")
    seed_state = generate_seed_state()
    print(f"Running {len(tasks)} task(s)...\n")

    if args.workers <= 1:
        port = find_free_port(args.port)
        results = run_tasks_sequential(tasks, port, seed_state)
    else:
        results = run_tasks_parallel(tasks, args.workers, args.port, seed_state)

    # Summary
    passed = sum(1 for _, p, _ in results if p)
    total = len(results)
    failed = [tid for tid, p, _ in results if not p]

    print(f"\n{passed}/{total} passed")
    if failed:
        print(f"Failed: {', '.join(failed)}")
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
