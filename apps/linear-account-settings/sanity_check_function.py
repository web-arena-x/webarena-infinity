#!/usr/bin/env python3
"""
Sanity check for Linear Account Settings function-test tasks.

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

const state = {
    _seedVersion: SEED_DATA_VERSION,
    currentUser: JSON.parse(JSON.stringify(CURRENT_USER)),
    workspaces: JSON.parse(JSON.stringify(WORKSPACES)),
    connectedAccounts: JSON.parse(JSON.stringify(CONNECTED_ACCOUNTS)),
    preferences: JSON.parse(JSON.stringify(PREFERENCES)),
    notificationChannels: JSON.parse(JSON.stringify(NOTIFICATION_CHANNELS)),
    emailDigestPreferences: JSON.parse(JSON.stringify(EMAIL_DIGEST_PREFERENCES)),
    communicationPreferences: JSON.parse(JSON.stringify(COMMUNICATION_PREFERENCES)),
    sessions: JSON.parse(JSON.stringify(SESSIONS)),
    passkeys: JSON.parse(JSON.stringify(PASSKEYS)),
    apiKeys: JSON.parse(JSON.stringify(API_KEYS)),
    authorizedApps: JSON.parse(JSON.stringify(AUTHORIZED_APPS)),
    _nextApiKeyId: INITIAL_NEXT_IDS._nextApiKeyId,
    _nextPasskeyId: INITIAL_NEXT_IDS._nextPasskeyId,
    _nextSessionId: INITIAL_NEXT_IDS._nextSessionId,
    _nextConnectedAccountId: INITIAL_NEXT_IDS._nextConnectedAccountId,
    _nextOAuthAppId: INITIAL_NEXT_IDS._nextOAuthAppId,
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


def find_channel(state, channel_id):
    """Find a notification channel by ID."""
    for c in state["notificationChannels"]:
        if c["id"] == channel_id:
            return c
    raise ValueError(f"Channel not found: {channel_id}")


def find_setting(channel, setting_id):
    """Find a notification setting within a channel."""
    for s in channel["settings"]:
        if s["id"] == setting_id:
            return s
    raise ValueError(f"Setting not found: {setting_id}")


# ── solve functions ──────────────────────────────────────────────────

# --- Profile ---

def solve_task_1(state):
    """Change full name to 'Alex Chen'."""
    state["currentUser"]["fullName"] = "Alex Chen"


def solve_task_2(state):
    """Change username to 'achen'."""
    state["currentUser"]["username"] = "achen"


def solve_task_3(state):
    """Change email to 'alex.chen@acmetech.io'."""
    state["currentUser"]["email"] = "alex.chen@acmetech.io"


def solve_task_4(state):
    """Disconnect Google account."""
    state["connectedAccounts"] = [
        a for a in state["connectedAccounts"] if a["provider"] != "Google"
    ]


def solve_task_5(state):
    """Disconnect GitHub account."""
    state["connectedAccounts"] = [
        a for a in state["connectedAccounts"] if a["provider"] != "GitHub"
    ]


def solve_task_6(state):
    """Disconnect Slack account."""
    state["connectedAccounts"] = [
        a for a in state["connectedAccounts"] if a["provider"] != "Slack"
    ]


def solve_task_7(state):
    """Disconnect Figma account."""
    state["connectedAccounts"] = [
        a for a in state["connectedAccounts"] if a["provider"] != "Figma"
    ]


def solve_task_8(state):
    """Leave workspace 'Side Project Labs'."""
    state["workspaces"] = [
        w for w in state["workspaces"] if w["name"] != "Side Project Labs"
    ]


# --- Preferences: General ---

def solve_task_9(state):
    """Change default home view to 'All issues'."""
    state["preferences"]["general"]["defaultHomeView"] = "All issues"


def solve_task_10(state):
    """Change default home view to 'Inbox'."""
    state["preferences"]["general"]["defaultHomeView"] = "Inbox"


def solve_task_11(state):
    """Change default home view to 'My Issues'."""
    state["preferences"]["general"]["defaultHomeView"] = "My Issues"


def solve_task_12(state):
    """Change default home view to 'Favorited Views'."""
    state["preferences"]["general"]["defaultHomeView"] = "Favorited Views"


def solve_task_13(state):
    """Disable 'Display full names'."""
    state["preferences"]["general"]["displayFullNames"] = False


def solve_task_14(state):
    """Change first day of week to 'Sunday'."""
    state["preferences"]["general"]["firstDayOfWeek"] = "Sunday"


def solve_task_15(state):
    """Disable 'Convert text emoticons into emojis'."""
    state["preferences"]["general"]["convertEmoticonToEmoji"] = False


# --- Preferences: Interface and Theme ---

def solve_task_16(state):
    """Change theme to 'light'."""
    state["preferences"]["interfaceAndTheme"]["theme"] = "light"


def solve_task_17(state):
    """Change theme to 'dark'."""
    state["preferences"]["interfaceAndTheme"]["theme"] = "dark"


def solve_task_18(state):
    """Change font size to 'small'."""
    state["preferences"]["interfaceAndTheme"]["fontSize"] = "small"


def solve_task_19(state):
    """Change font size to 'large'."""
    state["preferences"]["interfaceAndTheme"]["fontSize"] = "large"


def solve_task_20(state):
    """Enable 'Use pointer cursor'."""
    state["preferences"]["interfaceAndTheme"]["usePointerCursor"] = True


# --- Preferences: Desktop App ---

def solve_task_21(state):
    """Disable 'Open Linear URLs in desktop app'."""
    state["preferences"]["desktopApp"]["openLinksInDesktopApp"] = False


def solve_task_22(state):
    """Disable 'Show notification badge'."""
    state["preferences"]["desktopApp"]["showNotificationBadge"] = False


def solve_task_23(state):
    """Disable 'Enable spell check'."""
    state["preferences"]["desktopApp"]["enableSpellCheck"] = False


# --- Preferences: Automations and Workflows ---

def solve_task_24(state):
    """Enable 'Auto-assign issues you create to yourself'."""
    state["preferences"]["automationsAndWorkflows"]["autoAssignOnCreate"] = True


def solve_task_25(state):
    """Enable 'Auto-assign issues on started status'."""
    state["preferences"]["automationsAndWorkflows"]["autoAssignOnStarted"] = True


def solve_task_26(state):
    """Change git attachment format to 'Title and repository'."""
    state["preferences"]["automationsAndWorkflows"]["gitAttachmentFormat"] = "Title and repository"


def solve_task_27(state):
    """Disable 'On git branch copy, move issue to started status'."""
    state["preferences"]["automationsAndWorkflows"]["onGitBranchCopyMoveToStarted"] = False


def solve_task_28(state):
    """Disable 'On git branch copy, auto-assign to yourself'."""
    state["preferences"]["automationsAndWorkflows"]["onGitBranchCopyAutoAssign"] = False


# --- Notifications: Channels ---

def solve_task_29(state):
    """Disable Desktop notification channel (all settings become disabled)."""
    channel = find_channel(state, "notif_desktop")
    channel["enabled"] = False
    for s in channel["settings"]:
        s["enabled"] = False


def solve_task_30(state):
    """Enable 'Project updates' for Desktop."""
    channel = find_channel(state, "notif_desktop")
    setting = find_setting(channel, "desktop_project_update")
    setting["enabled"] = True


def solve_task_31(state):
    """Enable 'Cycle updates' for Desktop."""
    channel = find_channel(state, "notif_desktop")
    setting = find_setting(channel, "desktop_cycle_update")
    setting["enabled"] = True


def solve_task_32(state):
    """Disable 'SLA breach warnings' for Desktop."""
    channel = find_channel(state, "notif_desktop")
    setting = find_setting(channel, "desktop_sla_breach")
    setting["enabled"] = False


def solve_task_33(state):
    """Enable 'Status changes on subscribed issues' for Mobile."""
    channel = find_channel(state, "notif_mobile")
    setting = find_setting(channel, "mobile_issue_status")
    setting["enabled"] = True


def solve_task_34(state):
    """Disable 'Issue assigned to you' for Mobile."""
    channel = find_channel(state, "notif_mobile")
    setting = find_setting(channel, "mobile_issue_assigned")
    setting["enabled"] = False


def solve_task_35(state):
    """Enable 'Cycle updates' for Email."""
    channel = find_channel(state, "notif_email")
    setting = find_setting(channel, "email_cycle_update")
    setting["enabled"] = True


def solve_task_36(state):
    """Disable 'Project updates' for Email."""
    channel = find_channel(state, "notif_email")
    setting = find_setting(channel, "email_project_update")
    setting["enabled"] = False


def solve_task_37(state):
    """Enable 'Issue assigned to you' for Slack (auto-enables channel)."""
    channel = find_channel(state, "notif_slack")
    channel["enabled"] = True
    setting = find_setting(channel, "slack_issue_assigned")
    setting["enabled"] = True


def solve_task_38(state):
    """Disable Email notification channel (all settings become disabled)."""
    channel = find_channel(state, "notif_email")
    channel["enabled"] = False
    for s in channel["settings"]:
        s["enabled"] = False


# --- Notifications: Email Digest ---

def solve_task_39(state):
    """Disable 'Send immediately for urgent issues'."""
    state["emailDigestPreferences"]["sendImmediatelyOnUrgent"] = False


def solve_task_40(state):
    """Disable 'Delay low priority outside work hours'."""
    state["emailDigestPreferences"]["delayLowPriorityOutsideWorkHours"] = False


# --- Notifications: Communication Preferences ---

def solve_task_41(state):
    """Disable 'Changelogs'."""
    state["communicationPreferences"]["changelog"] = False


def solve_task_42(state):
    """Disable 'DPA updates'."""
    state["communicationPreferences"]["dpaUpdates"] = False


def solve_task_43(state):
    """Disable 'Product announcements'."""
    state["communicationPreferences"]["productAnnouncements"] = False


def solve_task_44(state):
    """Enable 'Tips and tutorials'."""
    state["communicationPreferences"]["tipsAndTutorials"] = True


def solve_task_45(state):
    """Enable 'Community updates'."""
    state["communicationPreferences"]["communityUpdates"] = True


# --- Security: Sessions ---

def solve_task_46(state):
    """Revoke session 'iPhone 15 Pro'."""
    state["sessions"] = [
        s for s in state["sessions"] if s["deviceName"] != "iPhone 15 Pro"
    ]


def solve_task_47(state):
    """Revoke session 'Windows Desktop'."""
    state["sessions"] = [
        s for s in state["sessions"] if s["deviceName"] != "Windows Desktop"
    ]


def solve_task_48(state):
    """Revoke all sessions except current."""
    state["sessions"] = [s for s in state["sessions"] if s["isCurrent"]]


# --- Security: Passkeys ---

def solve_task_49(state):
    """Add passkey 'Windows Hello'."""
    next_id = state.get("_nextPasskeyId", 3)
    new_passkey = {
        "id": f"pk_{str(next_id).zfill(3)}",
        "name": "Windows Hello",
        "createdAt": "2026-03-02T12:00:00.000Z",
        "lastUsedAt": None,
        "deviceType": "cross-platform",
    }
    state["passkeys"].append(new_passkey)
    state["_nextPasskeyId"] = next_id + 1


def solve_task_50(state):
    """Rename passkey 'MacBook Pro Touch ID' to 'Work Laptop Touch ID'."""
    pk = find_entity(state["passkeys"], name="MacBook Pro Touch ID")
    pk["name"] = "Work Laptop Touch ID"


def solve_task_51(state):
    """Remove passkey 'YubiKey 5C NFC'."""
    state["passkeys"] = [
        p for p in state["passkeys"] if p["name"] != "YubiKey 5C NFC"
    ]


def solve_task_52(state):
    """Add passkey 'iPad Face ID'."""
    next_id = state.get("_nextPasskeyId", 3)
    new_passkey = {
        "id": f"pk_{str(next_id).zfill(3)}",
        "name": "iPad Face ID",
        "createdAt": "2026-03-02T12:00:00.000Z",
        "lastUsedAt": None,
        "deviceType": "cross-platform",
    }
    state["passkeys"].append(new_passkey)
    state["_nextPasskeyId"] = next_id + 1


# --- Security: API Keys ---

def solve_task_53(state):
    """Create API key 'Data Export Script'."""
    next_id = state.get("_nextApiKeyId", 6)
    new_key = {
        "id": f"apikey_{str(next_id).zfill(3)}",
        "label": "Data Export Script",
        "prefix": "lin_api_0000",
        "createdAt": "2026-03-02T12:00:00.000Z",
        "lastUsedAt": None,
        "expiresAt": None,
    }
    state["apiKeys"].append(new_key)
    state["_nextApiKeyId"] = next_id + 1


def solve_task_54(state):
    """Revoke API key 'Staging Environment'."""
    state["apiKeys"] = [
        k for k in state["apiKeys"] if k["label"] != "Staging Environment"
    ]


def solve_task_55(state):
    """Revoke API key 'Personal Scripts'."""
    state["apiKeys"] = [
        k for k in state["apiKeys"] if k["label"] != "Personal Scripts"
    ]


# --- Security: Authorized Apps ---

def solve_task_56(state):
    """Revoke access for 'Loom'."""
    state["authorizedApps"] = [
        a for a in state["authorizedApps"] if a["name"] != "Loom"
    ]


def solve_task_57(state):
    """Revoke access for 'Statuspage'."""
    state["authorizedApps"] = [
        a for a in state["authorizedApps"] if a["name"] != "Statuspage"
    ]


def solve_task_58(state):
    """Revoke access for 'Zapier'."""
    state["authorizedApps"] = [
        a for a in state["authorizedApps"] if a["name"] != "Zapier"
    ]


# --- Extra coverage ---

def solve_task_59(state):
    """Change first day of week to 'Saturday'."""
    state["preferences"]["general"]["firstDayOfWeek"] = "Saturday"


def solve_task_60(state):
    """Disconnect GitLab account."""
    state["connectedAccounts"] = [
        a for a in state["connectedAccounts"] if a["provider"] != "GitLab"
    ]


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
    "task_31": solve_task_31,
    "task_32": solve_task_32,
    "task_33": solve_task_33,
    "task_34": solve_task_34,
    "task_35": solve_task_35,
    "task_36": solve_task_36,
    "task_37": solve_task_37,
    "task_38": solve_task_38,
    "task_39": solve_task_39,
    "task_40": solve_task_40,
    "task_41": solve_task_41,
    "task_42": solve_task_42,
    "task_43": solve_task_43,
    "task_44": solve_task_44,
    "task_45": solve_task_45,
    "task_46": solve_task_46,
    "task_47": solve_task_47,
    "task_48": solve_task_48,
    "task_49": solve_task_49,
    "task_50": solve_task_50,
    "task_51": solve_task_51,
    "task_52": solve_task_52,
    "task_53": solve_task_53,
    "task_54": solve_task_54,
    "task_55": solve_task_55,
    "task_56": solve_task_56,
    "task_57": solve_task_57,
    "task_58": solve_task_58,
    "task_59": solve_task_59,
    "task_60": solve_task_60,
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
    """Start the app server on the given port."""
    proc = subprocess.Popen(
        [sys.executable, "server.py", "--port", str(port)],
        cwd=str(APP_DIR),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
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
    parser = argparse.ArgumentParser(description="Linear Account Settings function-task sanity check")
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
