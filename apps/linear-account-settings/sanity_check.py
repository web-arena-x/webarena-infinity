#!/usr/bin/env python3
"""
Verifier sanity check — for each task, directly apply the expected state
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

import requests

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TASKS_DIR = os.path.join(SCRIPT_DIR, "tasks")

# ── Name-based lookup helpers ──────────────────────────────────

def find_session(state, device_name):
    return next(s for s in state["sessions"] if s["deviceName"] == device_name)

def find_api_key(state, label):
    return next(k for k in state["apiKeys"] if k["label"] == label)

def find_passkey(state, name):
    return next(p for p in state["passkeys"] if p["name"] == name)

def find_auth_app(state, name):
    return next(a for a in state["authorizedApps"] if a["name"] == name)

def find_connected_account(state, provider):
    return next(a for a in state["connectedAccounts"] if a["provider"] == provider)

def find_subscription(state, issue_id):
    return next(s for s in state["issueSubscriptions"] if s["issueId"] == issue_id)

def find_notification_group(state, group_id):
    return next(g for g in state["notificationGroups"] if g["id"] == group_id)

def sync_current_user_to_members(state):
    """Keep workspaceMembers entry in sync with currentUser."""
    cu = state["currentUser"]
    for i, m in enumerate(state["workspaceMembers"]):
        if m["id"] == cu["id"]:
            state["workspaceMembers"][i] = copy.deepcopy(cu)
            break

# ── Seed state construction via Node ───────────────────────────

def get_seed_state():
    """Evaluate js/data.js through Node and return the seed state dict."""
    data_js_path = os.path.join(SCRIPT_DIR, "js", "data.js")
    with open(data_js_path) as f:
        js_code = f.read()

    js_code += """
console.log(JSON.stringify({
    _seedVersion: SEED_DATA_VERSION,
    currentUser: CURRENT_USER,
    workspaceMembers: WORKSPACE_MEMBERS,
    workspace: WORKSPACE,
    preferences: PREFERENCES,
    notificationChannels: NOTIFICATION_CHANNELS,
    notificationGroups: NOTIFICATION_GROUPS,
    emailDigestSettings: EMAIL_DIGEST_SETTINGS,
    communicationPreferences: COMMUNICATION_PREFERENCES,
    sessions: SESSIONS,
    passkeys: PASSKEYS,
    apiKeys: API_KEYS,
    authorizedApps: AUTHORIZED_APPS,
    connectedAccounts: CONNECTED_ACCOUNTS,
    issueSubscriptions: ISSUE_SUBSCRIPTIONS,
    _nextSessionId: 8,
    _nextPasskeyId: 3,
    _nextApiKeyId: 4,
    _nextSubscriptionId: 9,
    _nextConnectedAccountId: 6
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

# ── Per-task solve functions ───────────────────────────────────

def solve_task_e1(state):
    """Change name to 'Jordan R. Rivera'."""
    state["currentUser"]["name"] = "Jordan R. Rivera"
    sync_current_user_to_members(state)

def solve_task_e2(state):
    """Change username to 'j.rivera'."""
    state["currentUser"]["username"] = "j.rivera"
    sync_current_user_to_members(state)

def solve_task_e3(state):
    """Update pronouns to 'he/him'."""
    state["currentUser"]["pronouns"] = "he/him"
    sync_current_user_to_members(state)

def solve_task_e4(state):
    """Turn off displayFullNames."""
    state["preferences"]["displayFullNames"] = False

def solve_task_e5(state):
    """Enable convertTextEmoticons (already true in seed, but ensure it)."""
    state["preferences"]["convertTextEmoticons"] = True

def solve_task_e6(state):
    """Disable mobile notification channel."""
    state["notificationChannels"]["mobile"]["enabled"] = False

def solve_task_e7(state):
    """Revoke 'Firefox on Ubuntu' session."""
    state["sessions"] = [s for s in state["sessions"] if s["deviceName"] != "Firefox on Ubuntu"]

def solve_task_e8(state):
    """Revoke 'Monitoring Dashboard' API key."""
    state["apiKeys"] = [k for k in state["apiKeys"] if k["label"] != "Monitoring Dashboard"]

def solve_task_e9(state):
    """Disable notification badge."""
    state["preferences"]["notificationBadge"] = False

def solve_task_e10(state):
    """Unsubscribe from NEX-987."""
    state["issueSubscriptions"] = [s for s in state["issueSubscriptions"] if s["issueId"] != "NEX-987"]

def solve_task_m1(state):
    """Change default home view to 'my_issues'."""
    state["preferences"]["defaultHomeView"] = "my_issues"

def solve_task_m2(state):
    """Change first day of week to 'sunday'."""
    state["preferences"]["firstDayOfWeek"] = "sunday"

def solve_task_m3(state):
    """Change email to 'jordan@nextera-labs.com'."""
    state["currentUser"]["email"] = "jordan@nextera-labs.com"
    sync_current_user_to_members(state)

def solve_task_m4(state):
    """Remove '1Password' passkey."""
    state["passkeys"] = [p for p in state["passkeys"] if p["name"] != "1Password"]

def solve_task_m5(state):
    """Disconnect GitLab connected account."""
    state["connectedAccounts"] = [a for a in state["connectedAccounts"] if a["provider"] != "GitLab"]

def solve_task_m6(state):
    """Revoke Zendesk authorized app."""
    state["authorizedApps"] = [a for a in state["authorizedApps"] if a["name"] != "Zendesk"]

def solve_task_m7(state):
    """Enable both auto-assign settings."""
    state["preferences"]["autoAssignOnCreate"] = True
    state["preferences"]["autoAssignOnStarted"] = True

def solve_task_m8(state):
    """Set theme='dark', fontSize='large'."""
    state["preferences"]["theme"] = "dark"
    state["preferences"]["fontSize"] = "large"

def solve_task_m9(state):
    """Enable SLA breach immediate, disable delay low priority."""
    state["emailDigestSettings"]["sendImmediatelyOnSLABreach"] = True
    state["emailDigestSettings"]["delayLowPriorityToWorkHours"] = False

def solve_task_m10(state):
    """Create new API key 'Staging Environment'."""
    key_id = "key-" + "sanity"
    state["apiKeys"].append({
        "id": key_id,
        "label": "Staging Environment",
        "prefix": "lin_api_test...xx",
        "createdAt": "2026-01-01T00:00:00Z",
        "lastUsedAt": None
    })

def solve_task_h1(state):
    """Change timezone to 'Europe/London' and theme to 'light'."""
    state["currentUser"]["timezone"] = "Europe/London"
    sync_current_user_to_members(state)
    state["preferences"]["theme"] = "light"

def solve_task_h2(state):
    """Revoke all non-current sessions and disable desktop channel."""
    state["sessions"] = [s for s in state["sessions"] if s.get("isCurrent")]
    state["notificationChannels"]["desktop"]["enabled"] = False

def solve_task_h3(state):
    """Register passkey 'YubiKey 5C' with cross-platform type."""
    pk_id = "pk-" + str(state.get("_nextPasskeyId", 3)).zfill(4)
    state["passkeys"].append({
        "id": pk_id,
        "name": "YubiKey 5C",
        "createdAt": "2026-01-01T00:00:00Z",
        "lastUsedAt": None,
        "deviceType": "cross-platform"
    })

def solve_task_h4(state):
    """Disconnect Figma connected account and revoke Figma auth app."""
    state["connectedAccounts"] = [a for a in state["connectedAccounts"] if a["provider"] != "Figma"]
    state["authorizedApps"] = [a for a in state["authorizedApps"] if a["name"] != "Figma"]

def solve_task_h5(state):
    """Change git attachment format and enable git branch auto-assign."""
    state["preferences"]["gitAttachmentFormat"] = "title_and_repo"
    state["preferences"]["gitBranchAutoAssign"] = True

def solve_task_h6(state):
    """Disable changelog and tips, enable product updates."""
    state["communicationPreferences"]["changelog"] = False
    state["communicationPreferences"]["tips"] = False
    state["communicationPreferences"]["productUpdates"] = True

def solve_task_h7(state):
    """Disable issue_status for slack, keep others unchanged."""
    group = find_notification_group(state, "issue_status")
    group["channels"]["slack"] = False

def solve_task_h8(state):
    """Change name, username, and default home view."""
    state["currentUser"]["name"] = "Jordan Rivera-Chen"
    state["currentUser"]["username"] = "jordan.rc"
    sync_current_user_to_members(state)
    state["preferences"]["defaultHomeView"] = "inbox"

def solve_task_h9(state):
    """Rename API key 'Personal Automation' to 'Production Monitoring'."""
    key = find_api_key(state, "Personal Automation")
    key["label"] = "Production Monitoring"

def solve_task_h10(state):
    """Enable email channel and enable project_updates for email."""
    state["notificationChannels"]["email"]["enabled"] = True
    group = find_notification_group(state, "project_updates")
    group["channels"]["email"] = True


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

# ── Server lifecycle ───────────────────────────────────────────

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

# ── Verifier loading ──────────────────────────────────────────

def load_verifier(task_id):
    path = os.path.join(TASKS_DIR, f"{task_id}.py")
    spec = importlib.util.spec_from_file_location(task_id, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.verify

# ── Worker: run a batch of tasks on one server ────────────────

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

# ── Main ───────────────────────────────────────────────────────

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
    print(f"Seed loaded: {len(seed_state['sessions'])} sessions, "
          f"{len(seed_state['apiKeys'])} API keys, "
          f"{len(seed_state['passkeys'])} passkeys")

    num_workers = min(args.workers, len(task_ids))
    all_results = []

    if num_workers <= 1:
        all_results = run_tasks(task_ids, args.port, seed_state)
    else:
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
