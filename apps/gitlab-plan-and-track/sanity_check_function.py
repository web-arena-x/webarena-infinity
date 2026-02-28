#!/usr/bin/env python3
"""
Sanity check for GitLab Plan & Track function-test tasks.

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
    users: JSON.parse(JSON.stringify(USERS)),
    issues: JSON.parse(JSON.stringify(ISSUES)),
    labels: JSON.parse(JSON.stringify(LABELS)),
    milestones: JSON.parse(JSON.stringify(MILESTONES)),
    iterations: JSON.parse(JSON.stringify(ITERATIONS)),
    iterationCadences: JSON.parse(JSON.stringify(ITERATION_CADENCES)),
    epics: JSON.parse(JSON.stringify(EPICS)),
    boards: JSON.parse(JSON.stringify(BOARDS)),
    todos: JSON.parse(JSON.stringify(TODOS)),
    timelogs: JSON.parse(JSON.stringify(TIMELOGS)),
    currentUser: JSON.parse(JSON.stringify(CURRENT_USER)),
    _seedVersion: SEED_DATA_VERSION,
    _nextIssueIid: Math.max(...ISSUES.map(i => i.iid)) + 1,
    _nextEpicIid: Math.max(...EPICS.map(e => e.iid)) + 1,
    _nextLabelId: 50,
    _nextMilestoneId: 20,
    _nextIterationId: 20,
    _nextCadenceId: 10,
    _nextBoardId: 10,
    _nextTodoId: 20,
    _nextTimelogId: 30,
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


def find_issue_by_title(state, title):
    """Find an issue by exact title."""
    for i in state["issues"]:
        if i["title"] == title:
            return i
    raise ValueError(f"Issue not found: {title!r}")


def find_label_by_title(state, title):
    """Find a label by exact title."""
    for l in state["labels"]:
        if l["title"] == title:
            return l
    raise ValueError(f"Label not found: {title!r}")


def find_milestone_by_title(state, title):
    """Find a milestone by exact title."""
    for m in state["milestones"]:
        if m["title"] == title:
            return m
    raise ValueError(f"Milestone not found: {title!r}")


def find_epic_by_title(state, title):
    """Find an epic by exact title."""
    for e in state["epics"]:
        if e["title"] == title:
            return e
    raise ValueError(f"Epic not found: {title!r}")


def find_cadence_by_title(state, title):
    """Find a cadence by exact title."""
    for c in state["iterationCadences"]:
        if c["title"] == title:
            return c
    raise ValueError(f"Cadence not found: {title!r}")


def find_iteration_by_title(state, title):
    """Find an iteration by exact title."""
    for i in state["iterations"]:
        if i["title"] == title:
            return i
    raise ValueError(f"Iteration not found: {title!r}")


def find_todo_by_target_and_action(state, target_id, action):
    """Find a todo by target ID and action."""
    for t in state["todos"]:
        if t["targetId"] == target_id and t["action"] == action:
            return t
    raise ValueError(f"Todo not found: targetId={target_id!r}, action={action!r}")


def next_issue_id(state):
    """Get the next issue IID and increment counter."""
    iid = state.get("_nextIssueIid", 100)
    state["_nextIssueIid"] = iid + 1
    return iid


def next_epic_iid(state):
    """Get the next epic IID and increment counter."""
    iid = state.get("_nextEpicIid", 20)
    state["_nextEpicIid"] = iid + 1
    return iid


def next_label_id(state):
    """Get the next label ID and increment counter."""
    lid = state.get("_nextLabelId", 50)
    state["_nextLabelId"] = lid + 1
    return lid


def next_milestone_id(state):
    """Get the next milestone ID and increment counter."""
    mid = state.get("_nextMilestoneId", 20)
    state["_nextMilestoneId"] = mid + 1
    return mid


def next_iteration_id(state):
    """Get the next iteration ID and increment counter."""
    iid = state.get("_nextIterationId", 20)
    state["_nextIterationId"] = iid + 1
    return iid


def next_cadence_id(state):
    """Get the next cadence ID and increment counter."""
    cid = state.get("_nextCadenceId", 10)
    state["_nextCadenceId"] = cid + 1
    return cid


def next_timelog_id(state):
    """Get the next timelog ID and increment counter."""
    tid = state.get("_nextTimelogId", 30)
    state["_nextTimelogId"] = tid + 1
    return tid


# ── solve functions ──────────────────────────────────────────────────

def solve_task_1(state):
    """Create issue 'Implement user profile badges' with weight 5."""
    iid = next_issue_id(state)
    now = "2026-02-28T12:00:00Z"
    state["issues"].append({
        "id": f"issue_{iid}", "iid": iid,
        "title": "Implement user profile badges",
        "description": "", "status": "open",
        "assignees": [], "labels": [],
        "milestoneId": None, "iterationId": None, "epicId": None,
        "weight": 5, "dueDate": None, "startDate": None,
        "healthStatus": None, "timeEstimate": 0, "timeSpent": 0,
        "confidential": False, "authorId": state["currentUser"]["id"],
        "createdAt": now, "updatedAt": now, "closedAt": None,
        "taskIds": [], "linkedIssueIds": []
    })


def solve_task_2(state):
    """Create issue 'Add mobile dark mode toggle' with full details."""
    iid = next_issue_id(state)
    now = "2026-02-28T12:00:00Z"
    ms = find_milestone_by_title(state, "v4.3 - Mobile Optimization")
    state["issues"].append({
        "id": f"issue_{iid}", "iid": iid,
        "title": "Add mobile dark mode toggle",
        "description": "Allow users to toggle dark mode on mobile devices",
        "status": "open",
        "assignees": ["usr_2", "usr_3"],
        "labels": ["lbl_10"],
        "milestoneId": ms["id"], "iterationId": None, "epicId": None,
        "weight": None, "dueDate": None, "startDate": None,
        "healthStatus": None, "timeEstimate": 0, "timeSpent": 0,
        "confidential": False, "authorId": state["currentUser"]["id"],
        "createdAt": now, "updatedAt": now, "closedAt": None,
        "taskIds": [], "linkedIssueIds": []
    })


def solve_task_3(state):
    """Create confidential issue 'Security audit: XSS in comment parser'."""
    iid = next_issue_id(state)
    now = "2026-02-28T12:00:00Z"
    state["issues"].append({
        "id": f"issue_{iid}", "iid": iid,
        "title": "Security audit: XSS in comment parser",
        "description": "", "status": "open",
        "assignees": [],
        "labels": ["lbl_21", "lbl_1"],
        "milestoneId": None, "iterationId": None, "epicId": None,
        "weight": None, "dueDate": None, "startDate": None,
        "healthStatus": None, "timeEstimate": 0, "timeSpent": 0,
        "confidential": True, "authorId": state["currentUser"]["id"],
        "createdAt": now, "updatedAt": now, "closedAt": None,
        "taskIds": [], "linkedIssueIds": []
    })


def solve_task_4(state):
    """Rename issue 'Migrate user settings page to React' -> add 'and TypeScript'."""
    issue = find_issue_by_title(state, "Migrate user settings page to React")
    issue["title"] = "Migrate user settings page to React and TypeScript"


def solve_task_5(state):
    """Close issue 'Dashboard widget layout breaks at 1440px viewport'."""
    issue = find_issue_by_title(state, "Dashboard widget layout breaks at 1440px viewport")
    issue["status"] = "closed"
    issue["closedAt"] = "2026-02-28T12:00:00Z"


def solve_task_6(state):
    """Reopen issue 'Fix SQL injection vulnerability in search endpoint'."""
    issue = find_issue_by_title(state, "Fix SQL injection vulnerability in search endpoint")
    issue["status"] = "open"
    issue["closedAt"] = None


def solve_task_7(state):
    """Delete issue 'Markdown preview renders incorrectly with nested code blocks'."""
    issue = find_issue_by_title(state, "Markdown preview renders incorrectly with nested code blocks")
    issue_id = issue["id"]
    state["issues"] = [i for i in state["issues"] if i["id"] != issue_id]
    state["todos"] = [t for t in state["todos"] if not (t["targetType"] == "issue" and t["targetId"] == issue_id)]
    state["timelogs"] = [t for t in state["timelogs"] if t["issueId"] != issue_id]


def solve_task_8(state):
    """Add David Kim (usr_8) to assignees of 'Login page shows blank screen on Safari 17.2'."""
    issue = find_issue_by_title(state, "Login page shows blank screen on Safari 17.2")
    if "usr_8" not in issue["assignees"]:
        issue["assignees"].append("usr_8")


def solve_task_9(state):
    """Remove Alex Thompson (usr_11) from assignees of 'Migrate user settings page to React'."""
    issue = find_issue_by_title(state, "Migrate user settings page to React")
    issue["assignees"] = [a for a in issue["assignees"] if a != "usr_11"]


def solve_task_10(state):
    """Add Chen Wei (usr_10) to assignees of 'Implement CSRF token rotation'."""
    issue = find_issue_by_title(state, "Implement CSRF token rotation")
    if "usr_10" not in issue["assignees"]:
        issue["assignees"].append("usr_10")


def solve_task_11(state):
    """Add 'security' (lbl_21) label to 'File upload fails silently for files > 50MB'."""
    issue = find_issue_by_title(state, "File upload fails silently for files > 50MB")
    if "lbl_21" not in issue["labels"]:
        issue["labels"].append("lbl_21")


def solve_task_12(state):
    """Remove 'UX' (lbl_23) label from 'Add dark mode support for the entire application'."""
    issue = find_issue_by_title(state, "Add dark mode support for the entire application")
    issue["labels"] = [l for l in issue["labels"] if l != "lbl_23"]


def solve_task_13(state):
    """Change priority from high to critical on 'Upgrade vulnerable dependencies'."""
    issue = find_issue_by_title(state, "Upgrade vulnerable dependencies identified in audit")
    issue["labels"] = [l for l in issue["labels"] if l != "lbl_2"]
    if "lbl_1" not in issue["labels"]:
        issue["labels"].append("lbl_1")


def solve_task_14(state):
    """Set milestone 'v4.2 - Security Hardening' on 'File upload fails silently'."""
    issue = find_issue_by_title(state, "File upload fails silently for files > 50MB")
    ms = find_milestone_by_title(state, "v4.2 - Security Hardening")
    issue["milestoneId"] = ms["id"]


def solve_task_15(state):
    """Remove milestone from 'Update project README with new setup instructions'."""
    issue = find_issue_by_title(state, "Update project README with new setup instructions")
    issue["milestoneId"] = None


def solve_task_16(state):
    """Set iteration 'Sprint 27' on 'Dashboard widget layout breaks at 1440px viewport'."""
    issue = find_issue_by_title(state, "Dashboard widget layout breaks at 1440px viewport")
    iteration = find_iteration_by_title(state, "Sprint 27")
    issue["iterationId"] = iteration["id"]


def solve_task_17(state):
    """Remove iteration from 'Analyze and optimize slow queries from APM logs'."""
    issue = find_issue_by_title(state, "Analyze and optimize slow queries from APM logs")
    issue["iterationId"] = None


def solve_task_18(state):
    """Set epic 'Performance Initiative' on 'Implement lazy loading for images and avatars'."""
    issue = find_issue_by_title(state, "Implement lazy loading for images and avatars")
    epic = find_epic_by_title(state, "Performance Initiative")
    issue["epicId"] = epic["id"]


def solve_task_19(state):
    """Remove epic from 'Build component library documentation site'."""
    issue = find_issue_by_title(state, "Build component library documentation site")
    issue["epicId"] = None


def solve_task_20(state):
    """Set health status to 'at_risk' on 'Implement GraphQL gateway for v3 API'."""
    issue = find_issue_by_title(state, "Implement GraphQL gateway for v3 API")
    issue["healthStatus"] = "at_risk"


def solve_task_21(state):
    """Clear health status from 'Upgrade vulnerable dependencies identified in audit'."""
    issue = find_issue_by_title(state, "Upgrade vulnerable dependencies identified in audit")
    issue["healthStatus"] = None


def solve_task_22(state):
    """Set due date '2026-05-01' on 'File upload fails silently for files > 50MB'."""
    issue = find_issue_by_title(state, "File upload fails silently for files > 50MB")
    issue["dueDate"] = "2026-05-01"


def solve_task_23(state):
    """Clear due date from 'Email notifications sent with wrong timezone offset'."""
    issue = find_issue_by_title(state, "Email notifications sent with wrong timezone offset")
    issue["dueDate"] = None


def solve_task_24(state):
    """Set weight to 13 on 'Add webhook support for issue state changes'."""
    issue = find_issue_by_title(state, "Add webhook support for issue state changes")
    issue["weight"] = 13


def solve_task_25(state):
    """Clear weight from 'Dashboard widget layout breaks at 1440px viewport'."""
    issue = find_issue_by_title(state, "Dashboard widget layout breaks at 1440px viewport")
    issue["weight"] = None


def solve_task_26(state):
    """Set time estimate to 4h (14400) on 'Fix dropdown menu position clipping'."""
    issue = find_issue_by_title(state, "Fix dropdown menu position clipping at viewport edges")
    issue["timeEstimate"] = 14400


def solve_task_27(state):
    """Remove time estimate from 'Implement lazy loading for images and avatars'."""
    issue = find_issue_by_title(state, "Implement lazy loading for images and avatars")
    issue["timeEstimate"] = 0


def solve_task_28(state):
    """Add timelog of 2h30m (9000s) to 'Implement retry mechanism for failed API calls'."""
    issue = find_issue_by_title(state, "Implement retry mechanism for failed API calls")
    tid = next_timelog_id(state)
    state["timelogs"].append({
        "id": f"tl_{tid}",
        "issueId": issue["id"],
        "userId": state["currentUser"]["id"],
        "timeSpent": 9000,
        "summary": "Initial investigation and research",
        "spentAt": "2026-02-28T12:00:00Z"
    })
    issue["timeSpent"] = (issue.get("timeSpent") or 0) + 9000


def solve_task_29(state):
    """Delete timelog 'Safari debugging and investigation' from issue #17."""
    issue = find_issue_by_title(state, "Login page shows blank screen on Safari 17.2")
    tl = next(
        t for t in state["timelogs"]
        if t["issueId"] == issue["id"] and "Safari debugging" in t["summary"]
    )
    issue["timeSpent"] = max(0, (issue.get("timeSpent") or 0) - tl["timeSpent"])
    state["timelogs"] = [t for t in state["timelogs"] if t["id"] != tl["id"]]


def solve_task_30(state):
    """Create label 'deployment' with color #ff5733, type project."""
    lid = next_label_id(state)
    state["labels"].append({
        "id": f"lbl_{lid}",
        "title": "deployment",
        "description": "",
        "color": "#ff5733",
        "textColor": "#fff",
        "type": "project",
        "scoped": False
    })


def solve_task_31(state):
    """Create scoped label 'environment::production' with color #cc0000, type group."""
    lid = next_label_id(state)
    state["labels"].append({
        "id": f"lbl_{lid}",
        "title": "environment::production",
        "description": "",
        "color": "#cc0000",
        "textColor": "#fff",
        "type": "group",
        "scoped": True
    })


def solve_task_32(state):
    """Rename label 'good-first-issue' to 'beginner-friendly'."""
    label = find_label_by_title(state, "good-first-issue")
    label["title"] = "beginner-friendly"
    label["scoped"] = False


def solve_task_33(state):
    """Change color of 'needs-discussion' to #0075ca."""
    label = find_label_by_title(state, "needs-discussion")
    label["color"] = "#0075ca"


def solve_task_34(state):
    """Delete label 'testing' (lbl_30)."""
    label = find_label_by_title(state, "testing")
    label_id = label["id"]
    state["labels"] = [l for l in state["labels"] if l["id"] != label_id]
    for issue in state["issues"]:
        issue["labels"] = [l for l in issue["labels"] if l != label_id]
    for epic in state["epics"]:
        epic["labels"] = [l for l in epic["labels"] if l != label_id]


def solve_task_35(state):
    """Create milestone 'v4.4 - Internationalization'."""
    mid = next_milestone_id(state)
    state["milestones"].append({
        "id": f"ms_{mid}",
        "title": "v4.4 - Internationalization",
        "description": "",
        "startDate": "2026-07-16",
        "dueDate": "2026-09-30",
        "status": "active",
        "createdAt": "2026-02-28T12:00:00Z"
    })


def solve_task_36(state):
    """Edit milestone 'Backlog' description."""
    ms = find_milestone_by_title(state, "Backlog")
    ms["description"] = "Unscheduled items awaiting prioritization and scheduling."


def solve_task_37(state):
    """Close milestone 'Q1 2026 Planning'."""
    ms = find_milestone_by_title(state, "Q1 2026 Planning")
    ms["status"] = "closed"


def solve_task_38(state):
    """Reopen milestone 'v3.9 - Maintenance'."""
    ms = find_milestone_by_title(state, "v3.9 - Maintenance")
    ms["status"] = "active"


def solve_task_39(state):
    """Create epic 'CI/CD Pipeline Modernization'."""
    iid = next_epic_iid(state)
    now = "2026-02-28T12:00:00Z"
    state["epics"].append({
        "id": f"epic_{iid}", "iid": iid,
        "title": "CI/CD Pipeline Modernization",
        "description": "Modernize the CI/CD pipeline with container-native builds and GitOps deployment",
        "status": "open",
        "startDate": None, "dueDate": None,
        "labels": ["lbl_18"],
        "healthStatus": None,
        "authorId": state["currentUser"]["id"],
        "confidential": False,
        "parentEpicId": None,
        "createdAt": now, "updatedAt": now
    })


def solve_task_40(state):
    """Create epic 'Search Performance' as child of 'Performance Initiative'."""
    parent = find_epic_by_title(state, "Performance Initiative")
    iid = next_epic_iid(state)
    now = "2026-02-28T12:00:00Z"
    state["epics"].append({
        "id": f"epic_{iid}", "iid": iid,
        "title": "Search Performance",
        "description": "",
        "status": "open",
        "startDate": None, "dueDate": None,
        "labels": [],
        "healthStatus": None,
        "authorId": state["currentUser"]["id"],
        "confidential": False,
        "parentEpicId": parent["id"],
        "createdAt": now, "updatedAt": now
    })


def solve_task_41(state):
    """Rename epic 'Documentation Overhaul' to 'Documentation Overhaul v2'."""
    epic = find_epic_by_title(state, "Documentation Overhaul")
    epic["title"] = "Documentation Overhaul v2"


def solve_task_42(state):
    """Close epic 'Mobile App v2'."""
    epic = find_epic_by_title(state, "Mobile App v2")
    epic["status"] = "closed"


def solve_task_43(state):
    """Reopen epic 'Analytics Dashboard'."""
    epic = find_epic_by_title(state, "Analytics Dashboard")
    epic["status"] = "open"


def solve_task_44(state):
    """Add 'security' (lbl_21) label to epic 'Caching Layer Implementation'."""
    epic = find_epic_by_title(state, "Caching Layer Implementation")
    if "lbl_21" not in epic["labels"]:
        epic["labels"].append("lbl_21")


def solve_task_45(state):
    """Remove 'component::frontend' (lbl_14) from epic 'Platform Redesign'."""
    epic = find_epic_by_title(state, "Platform Redesign")
    epic["labels"] = [l for l in epic["labels"] if l != "lbl_14"]


def solve_task_46(state):
    """Create cadence 'Bug Fix Cadence'."""
    cid = next_cadence_id(state)
    state["iterationCadences"].append({
        "id": f"cad_{cid}",
        "title": "Bug Fix Cadence",
        "description": "",
        "automatic": True,
        "startDate": None,
        "durationWeeks": 1,
        "upcomingIterations": 4,
        "rollOver": False,
        "active": True
    })


def solve_task_47(state):
    """Edit cadence 'Sprint Cadence' description."""
    cad = find_cadence_by_title(state, "Sprint Cadence")
    cad["description"] = "Bi-weekly development sprints for the engineering team. Updated for Q2 2026."


def solve_task_48(state):
    """Create iteration 'Release 4.0 GA' in 'Release Cycle' cadence."""
    cad = find_cadence_by_title(state, "Release Cycle")
    iid = next_iteration_id(state)
    state["iterations"].append({
        "id": f"iter_{iid}",
        "title": "Release 4.0 GA",
        "cadenceId": cad["id"],
        "startDate": "2026-03-01",
        "dueDate": "2026-03-15",
        "status": "upcoming",
        "createdAt": "2026-02-28T12:00:00Z"
    })


def solve_task_49(state):
    """Mark todo about 'Login page shows blank screen on Safari 17.2' as done."""
    issue = find_issue_by_title(state, "Login page shows blank screen on Safari 17.2")
    todo = find_todo_by_target_and_action(state, issue["id"], "assigned")
    todo["status"] = "done"


def solve_task_50(state):
    """Snooze todo about 'Email notifications sent with wrong timezone offset'."""
    issue = find_issue_by_title(state, "Email notifications sent with wrong timezone offset")
    todo = find_todo_by_target_and_action(state, issue["id"], "mentioned")
    todo["status"] = "snoozed"
    todo["snoozedUntil"] = "2026-03-01T08:00:00Z"


def solve_task_51(state):
    """Unsnooze todo about 'Implement GraphQL gateway for v3 API'."""
    issue = find_issue_by_title(state, "Implement GraphQL gateway for v3 API")
    todo = find_todo_by_target_and_action(state, issue["id"], "review_requested")
    todo["status"] = "pending"
    todo["snoozedUntil"] = None


def solve_task_52(state):
    """Restore done todo about 'Design new navigation header component'."""
    issue = find_issue_by_title(state, "Design new navigation header component")
    todo = find_todo_by_target_and_action(state, issue["id"], "assigned")
    todo["status"] = "pending"
    todo["snoozedUntil"] = None


def solve_task_53(state):
    """Mark all pending todos as done."""
    for todo in state["todos"]:
        if todo["status"] == "pending":
            todo["status"] = "done"


def solve_task_54(state):
    """Create issue 'Implement API versioning documentation' with dates."""
    iid = next_issue_id(state)
    now = "2026-02-28T12:00:00Z"
    state["issues"].append({
        "id": f"issue_{iid}", "iid": iid,
        "title": "Implement API versioning documentation",
        "description": "", "status": "open",
        "assignees": [], "labels": [],
        "milestoneId": None, "iterationId": None, "epicId": None,
        "weight": None, "dueDate": "2026-04-15", "startDate": "2026-03-15",
        "healthStatus": None, "timeEstimate": 0, "timeSpent": 0,
        "confidential": False, "authorId": state["currentUser"]["id"],
        "createdAt": now, "updatedAt": now, "closedAt": None,
        "taskIds": [], "linkedIssueIds": []
    })


def solve_task_55(state):
    """Set iteration 'March 2026' and add 'needs-discussion' on 'Implement keyboard shortcuts'."""
    issue = find_issue_by_title(state, "Implement keyboard shortcuts for common actions")
    iteration = find_iteration_by_title(state, "March 2026")
    issue["iterationId"] = iteration["id"]
    if "lbl_19" not in issue["labels"]:
        issue["labels"].append("lbl_19")


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
    parser = argparse.ArgumentParser(description="GitLab Plan & Track function-task sanity check")
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
