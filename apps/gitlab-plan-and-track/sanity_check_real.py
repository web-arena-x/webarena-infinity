#!/usr/bin/env python3
"""
Sanity check for GitLab Plan & Track real-task verifiers.

For each task, directly applies the expected end-state (bypassing the agent),
then runs the verifier and asserts it passes.

Usage:
    python3 sanity_check_real.py                     # All tasks, sequential
    python3 sanity_check_real.py --workers N          # N parallel environments
    python3 sanity_check_real.py --task-id task_e1    # Single task
    python3 sanity_check_real.py --port 9500          # Custom base port
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
TASKS_FILE = APP_DIR / "tasks.json"

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


def find_user_by_name(state, name):
    """Find a user by name."""
    for u in state["users"]:
        if u["name"] == name:
            return u
    raise ValueError(f"User not found: {name!r}")


def find_board_by_name(state, name):
    """Find a board by name."""
    for b in state["boards"]:
        if b["name"] == name:
            return b
    raise ValueError(f"Board not found: {name!r}")


def find_todo_for_issue(state, issue_id, action):
    """Find a todo by target issue and action."""
    for t in state["todos"]:
        if t["targetId"] == issue_id and t["action"] == action:
            return t
    raise ValueError(f"Todo not found: targetId={issue_id!r}, action={action!r}")


def next_issue_id(state):
    iid = state.get("_nextIssueIid", 100)
    state["_nextIssueIid"] = iid + 1
    return iid


def next_epic_iid(state):
    iid = state.get("_nextEpicIid", 20)
    state["_nextEpicIid"] = iid + 1
    return iid


def next_label_id(state):
    lid = state.get("_nextLabelId", 50)
    state["_nextLabelId"] = lid + 1
    return lid


def next_milestone_id(state):
    mid = state.get("_nextMilestoneId", 20)
    state["_nextMilestoneId"] = mid + 1
    return mid


def next_iteration_id(state):
    iid = state.get("_nextIterationId", 20)
    state["_nextIterationId"] = iid + 1
    return iid


def next_cadence_id(state):
    cid = state.get("_nextCadenceId", 10)
    state["_nextCadenceId"] = cid + 1
    return cid


def next_board_id(state):
    bid = state.get("_nextBoardId", 10)
    state["_nextBoardId"] = bid + 1
    return bid


NOW = "2026-02-28T12:00:00Z"


# ── Easy solve functions ─────────────────────────────────────────────

def solve_task_e1(state):
    """Close the Safari login page blank screen bug."""
    issue = find_issue_by_title(state, "Login page shows blank screen on Safari 17.2")
    issue["status"] = "closed"
    issue["closedAt"] = NOW
    issue["updatedAt"] = NOW


def solve_task_e2(state):
    """Reopen the Analytics Dashboard epic."""
    epic = find_epic_by_title(state, "Analytics Dashboard")
    epic["status"] = "open"
    epic["updatedAt"] = NOW


def solve_task_e3(state):
    """Mark the todo about upgrading vulnerable dependencies as done."""
    issue = find_issue_by_title(state, "Upgrade vulnerable dependencies identified in audit")
    todo = find_todo_for_issue(state, issue["id"], "assigned")
    todo["status"] = "done"


def solve_task_e4(state):
    """Delete the markdown preview rendering bug."""
    issue = find_issue_by_title(state, "Markdown preview renders incorrectly with nested code blocks")
    issue_id = issue["id"]
    state["issues"] = [i for i in state["issues"] if i["id"] != issue_id]
    state["todos"] = [t for t in state["todos"] if not (t["targetType"] == "issue" and t["targetId"] == issue_id)]
    state["timelogs"] = [t for t in state["timelogs"] if t["issueId"] != issue_id]


def solve_task_e5(state):
    """Set the weight of the 404 error page typo fix to 3."""
    issue = find_issue_by_title(state, "Fix typo in 404 error page message")
    issue["weight"] = 3
    issue["updatedAt"] = NOW


def solve_task_e6(state):
    """Make the API rate limiting issue confidential."""
    issue = find_issue_by_title(state, "Add rate limiting to v3 endpoints")
    issue["confidential"] = True
    issue["updatedAt"] = NOW


def solve_task_e7(state):
    """Remove the 'needs-discussion' label from the real-time collaborative editing issue."""
    issue = find_issue_by_title(state, "Build real-time collaborative editing for issue descriptions")
    label = find_label_by_title(state, "needs-discussion")
    issue["labels"] = [l for l in issue["labels"] if l != label["id"]]
    issue["updatedAt"] = NOW


def solve_task_e8(state):
    """Close the v4.3 - Mobile Optimization milestone."""
    ms = find_milestone_by_title(state, "v4.3 - Mobile Optimization")
    ms["status"] = "closed"


def solve_task_e9(state):
    """Assign Luca Rossi to the retry mechanism for failed API calls issue."""
    issue = find_issue_by_title(state, "Implement retry mechanism for failed API calls")
    user = find_user_by_name(state, "Luca Rossi")
    if user["id"] not in issue["assignees"]:
        issue["assignees"].append(user["id"])
    issue["updatedAt"] = NOW


def solve_task_e10(state):
    """Set a due date of April 30, 2026 for the webhook support issue."""
    issue = find_issue_by_title(state, "Add webhook support for issue state changes")
    issue["dueDate"] = "2026-04-30"
    issue["updatedAt"] = NOW


def solve_task_e11(state):
    """Change the health status of the JavaScript bundle size reduction issue to at risk."""
    issue = find_issue_by_title(state, "Reduce JavaScript bundle size by 40%")
    issue["healthStatus"] = "at_risk"
    issue["updatedAt"] = NOW


def solve_task_e12(state):
    """Mark the todo about the lazy loading for images issue as done."""
    issue = find_issue_by_title(state, "Implement lazy loading for images and avatars")
    todo = find_todo_for_issue(state, issue["id"], "mentioned")
    todo["status"] = "done"


def solve_task_e13(state):
    """Remove Nina Kowalski from the dark mode support issue."""
    issue = find_issue_by_title(state, "Add dark mode support for the entire application")
    user = find_user_by_name(state, "Nina Kowalski")
    issue["assignees"] = [a for a in issue["assignees"] if a != user["id"]]
    issue["updatedAt"] = NOW


def solve_task_e14(state):
    """Rename the 'good-first-issue' label to 'starter-issue'."""
    label = find_label_by_title(state, "good-first-issue")
    label["title"] = "starter-issue"


def solve_task_e15(state):
    """Close the Frontend Modernization epic."""
    epic = find_epic_by_title(state, "Frontend Modernization")
    epic["status"] = "closed"
    epic["updatedAt"] = NOW


def solve_task_e16(state):
    """Delete the Backlog milestone."""
    ms = find_milestone_by_title(state, "Backlog")
    ms_id = ms["id"]
    state["milestones"] = [m for m in state["milestones"] if m["id"] != ms_id]
    for issue in state["issues"]:
        if issue["milestoneId"] == ms_id:
            issue["milestoneId"] = None


def solve_task_e17(state):
    """Unassign Oliver Schmidt from the vulnerable dependencies upgrade issue."""
    issue = find_issue_by_title(state, "Upgrade vulnerable dependencies identified in audit")
    user = find_user_by_name(state, "Oliver Schmidt")
    issue["assignees"] = [a for a in issue["assignees"] if a != user["id"]]
    issue["updatedAt"] = NOW


def solve_task_e18(state):
    """Set the weight of the sidebar tooltip issue to 3."""
    issue = find_issue_by_title(state, "Add tooltip to truncated sidebar labels")
    issue["weight"] = 3
    issue["updatedAt"] = NOW


def solve_task_e19(state):
    """Move the project README update issue to the Q1 2026 Planning milestone."""
    issue = find_issue_by_title(state, "Update project README with new setup instructions")
    ms = find_milestone_by_title(state, "Q1 2026 Planning")
    issue["milestoneId"] = ms["id"]
    issue["updatedAt"] = NOW


def solve_task_e20(state):
    """Restore the snoozed todo about the GraphQL gateway review."""
    issue = find_issue_by_title(state, "Implement GraphQL gateway for v3 API")
    todo = find_todo_for_issue(state, issue["id"], "review_requested")
    todo["status"] = "pending"
    todo["snoozedUntil"] = None


# ── Medium solve functions ───────────────────────────────────────────

def solve_task_m1(state):
    """Create a new milestone called 'v4.4 - Integrations' starting August 1, 2026 and ending September 30, 2026."""
    mid = next_milestone_id(state)
    state["milestones"].append({
        "id": f"ms_{mid}",
        "title": "v4.4 - Integrations",
        "description": "",
        "startDate": "2026-08-01",
        "dueDate": "2026-09-30",
        "status": "active",
        "createdAt": NOW,
    })


def solve_task_m2(state):
    """Add the keyboard shortcuts issue to the Platform Redesign epic and set its iteration to Sprint 27."""
    issue = find_issue_by_title(state, "Implement keyboard shortcuts for common actions")
    epic = find_epic_by_title(state, "Platform Redesign")
    iteration = find_iteration_by_title(state, "Sprint 27")
    issue["epicId"] = epic["id"]
    issue["iterationId"] = iteration["id"]
    issue["updatedAt"] = NOW


def solve_task_m3(state):
    """Create a new issue titled 'Set up monitoring dashboard' assigned to Luca Rossi with the priority::high label."""
    user = find_user_by_name(state, "Luca Rossi")
    label = find_label_by_title(state, "priority::high")
    iid = next_issue_id(state)
    state["issues"].append({
        "id": f"issue_{iid}",
        "iid": iid,
        "title": "Set up monitoring dashboard",
        "description": "",
        "status": "open",
        "assignees": [user["id"]],
        "labels": [label["id"]],
        "milestoneId": None,
        "iterationId": None,
        "epicId": None,
        "weight": None,
        "dueDate": None,
        "startDate": None,
        "healthStatus": None,
        "timeEstimate": 0,
        "timeSpent": 0,
        "confidential": False,
        "authorId": state["currentUser"]["id"],
        "createdAt": NOW,
        "updatedAt": NOW,
        "closedAt": None,
        "taskIds": [],
        "linkedIssueIds": [],
    })


def solve_task_m4(state):
    """Remove all assignees from the dark mode support issue and set its health status to needs attention."""
    issue = find_issue_by_title(state, "Add dark mode support for the entire application")
    issue["assignees"] = []
    issue["healthStatus"] = "needs_attention"
    issue["updatedAt"] = NOW


def solve_task_m5(state):
    """Move the loading skeletons issue to the v4.0 - Platform Redesign milestone and add it to the Frontend Modernization epic."""
    issue = find_issue_by_title(state, "Add loading skeletons to replace spinners")
    ms = find_milestone_by_title(state, "v4.0 - Platform Redesign")
    epic = find_epic_by_title(state, "Frontend Modernization")
    issue["milestoneId"] = ms["id"]
    issue["epicId"] = epic["id"]
    issue["updatedAt"] = NOW


def solve_task_m6(state):
    """Add the 'breaking-change' and 'performance' labels to the container registry garbage collection issue."""
    issue = find_issue_by_title(state, "Implement container registry garbage collection")
    lbl_bc = find_label_by_title(state, "breaking-change")
    lbl_perf = find_label_by_title(state, "performance")
    for lid in [lbl_bc["id"], lbl_perf["id"]]:
        if lid not in issue["labels"]:
            issue["labels"].append(lid)
    issue["updatedAt"] = NOW


def solve_task_m7(state):
    """Disable automatic scheduling and roll-over on the Sprint Cadence."""
    cad = find_cadence_by_title(state, "Sprint Cadence")
    cad["automatic"] = False
    cad["rollOver"] = False


def solve_task_m8(state):
    """Close all open issues assigned to Fatima Al-Rashid."""
    user = find_user_by_name(state, "Fatima Al-Rashid")
    for issue in state["issues"]:
        if user["id"] in issue["assignees"] and issue["status"] == "open":
            issue["status"] = "closed"
            issue["closedAt"] = NOW
            issue["updatedAt"] = NOW


def solve_task_m9(state):
    """Create a new epic called 'CI/CD Pipeline Improvements' and add the Playwright end-to-end testing issue to it."""
    iid = next_epic_iid(state)
    epic_id = f"epic_{iid}"
    state["epics"].append({
        "id": epic_id,
        "iid": iid,
        "title": "CI/CD Pipeline Improvements",
        "description": "",
        "status": "open",
        "startDate": None,
        "dueDate": None,
        "labels": [],
        "healthStatus": None,
        "authorId": state["currentUser"]["id"],
        "confidential": False,
        "parentEpicId": None,
        "createdAt": NOW,
        "updatedAt": NOW,
    })
    issue = find_issue_by_title(state, "Set up end-to-end testing with Playwright")
    issue["epicId"] = epic_id
    issue["updatedAt"] = NOW


def solve_task_m10(state):
    """Set a time estimate of 4 hours on the dropdown menu position bug and assign it to the Backlog milestone."""
    issue = find_issue_by_title(state, "Fix dropdown menu position clipping at viewport edges")
    ms = find_milestone_by_title(state, "Backlog")
    issue["timeEstimate"] = 14400  # 4 hours in seconds
    issue["milestoneId"] = ms["id"]
    issue["updatedAt"] = NOW


def solve_task_m11(state):
    """Move the CSP headers issue to the v4.1 milestone and change its iteration to Sprint 27."""
    issue = find_issue_by_title(state, "Implement Content Security Policy headers")
    ms = find_milestone_by_title(state, "v4.1 - Performance")
    iteration = find_iteration_by_title(state, "Sprint 27")
    issue["milestoneId"] = ms["id"]
    issue["iterationId"] = iteration["id"]
    issue["updatedAt"] = NOW


def solve_task_m12(state):
    """Move all issues in Sprint 26 assigned to David Kim to Sprint 27."""
    user = find_user_by_name(state, "David Kim")
    sprint26 = find_iteration_by_title(state, "Sprint 26")
    sprint27 = find_iteration_by_title(state, "Sprint 27")
    for issue in state["issues"]:
        if issue["iterationId"] == sprint26["id"] and user["id"] in issue["assignees"]:
            issue["iterationId"] = sprint27["id"]
            issue["updatedAt"] = NOW


def solve_task_m13(state):
    """Set a start date of March 15 and due date of April 15, 2026 for the retry mechanism issue."""
    issue = find_issue_by_title(state, "Implement retry mechanism for failed API calls")
    issue["startDate"] = "2026-03-15"
    issue["dueDate"] = "2026-04-15"
    issue["updatedAt"] = NOW


def solve_task_m14(state):
    """Create a new iteration called 'Sprint 29' in the Sprint Cadence starting March 31 and ending April 13, 2026."""
    cad = find_cadence_by_title(state, "Sprint Cadence")
    iid = next_iteration_id(state)
    state["iterations"].append({
        "id": f"iter_{iid}",
        "title": "Sprint 29",
        "cadenceId": cad["id"],
        "startDate": "2026-03-31",
        "dueDate": "2026-04-13",
        "status": "upcoming",
        "createdAt": NOW,
    })


def solve_task_m15(state):
    """Replace the 'UX' label on the Platform Redesign epic with 'needs-discussion'."""
    epic = find_epic_by_title(state, "Platform Redesign")
    lbl_ux = find_label_by_title(state, "UX")
    lbl_nd = find_label_by_title(state, "needs-discussion")
    epic["labels"] = [l for l in epic["labels"] if l != lbl_ux["id"]]
    if lbl_nd["id"] not in epic["labels"]:
        epic["labels"].append(lbl_nd["id"])
    epic["updatedAt"] = NOW


def solve_task_m16(state):
    """Assign Priya Patel and Marcus Johnson to the component library documentation issue."""
    issue = find_issue_by_title(state, "Build component library documentation site")
    priya = find_user_by_name(state, "Priya Patel")
    marcus = find_user_by_name(state, "Marcus Johnson")
    for uid in [priya["id"], marcus["id"]]:
        if uid not in issue["assignees"]:
            issue["assignees"].append(uid)
    issue["updatedAt"] = NOW


def solve_task_m17(state):
    """Create a new board called 'Priority Board' with a list for the priority::critical label."""
    label = find_label_by_title(state, "priority::critical")
    bid = next_board_id(state)
    state["boards"].append({
        "id": f"board_{bid}",
        "name": "Priority Board",
        "lists": [
            {
                "id": f"list_{bid}_1",
                "type": "label",
                "labelId": label["id"],
                "position": 0,
            }
        ],
    })


def solve_task_m18(state):
    """Add the 'performance' label to the JWT authentication migration issue and set its health status to needs attention."""
    issue = find_issue_by_title(state, "Migrate user authentication from sessions to JWT")
    label = find_label_by_title(state, "performance")
    if label["id"] not in issue["labels"]:
        issue["labels"].append(label["id"])
    issue["healthStatus"] = "needs_attention"
    issue["updatedAt"] = NOW


def solve_task_m19(state):
    """Remove Aisha Mohammed from the component library documentation issue and assign Nina Kowalski instead."""
    issue = find_issue_by_title(state, "Build component library documentation site")
    aisha = find_user_by_name(state, "Aisha Mohammed")
    nina = find_user_by_name(state, "Nina Kowalski")
    issue["assignees"] = [a for a in issue["assignees"] if a != aisha["id"]]
    if nina["id"] not in issue["assignees"]:
        issue["assignees"].append(nina["id"])
    issue["updatedAt"] = NOW


def solve_task_m20(state):
    """Rename the 'technical-debt' label to 'tech-debt' and set its description to 'Legacy code requiring refactoring'."""
    label = find_label_by_title(state, "technical-debt")
    label["title"] = "tech-debt"
    label["description"] = "Legacy code requiring refactoring"


# ── Hard solve functions ─────────────────────────────────────────────

def solve_task_h1(state):
    """Create a new epic 'Accessibility Initiative' with the accessibility label, then add all issues with that label to it."""
    lbl = find_label_by_title(state, "accessibility")
    iid = next_epic_iid(state)
    epic_id = f"epic_{iid}"
    state["epics"].append({
        "id": epic_id,
        "iid": iid,
        "title": "Accessibility Initiative",
        "description": "",
        "status": "open",
        "startDate": None,
        "dueDate": None,
        "labels": [lbl["id"]],
        "healthStatus": None,
        "authorId": state["currentUser"]["id"],
        "confidential": False,
        "parentEpicId": None,
        "createdAt": NOW,
        "updatedAt": NOW,
    })
    for issue in state["issues"]:
        if lbl["id"] in issue["labels"]:
            issue["epicId"] = epic_id
            issue["updatedAt"] = NOW


def solve_task_h2(state):
    """Close all open bugs that have priority::low."""
    lbl_bug = find_label_by_title(state, "type::bug")
    lbl_low = find_label_by_title(state, "priority::low")
    for issue in state["issues"]:
        if (issue["status"] == "open"
                and lbl_bug["id"] in issue["labels"]
                and lbl_low["id"] in issue["labels"]):
            issue["status"] = "closed"
            issue["closedAt"] = NOW
            issue["updatedAt"] = NOW


def solve_task_h3(state):
    """Move all issues in Security Hardening that don't have the security label to v4.1."""
    ms_sec = find_milestone_by_title(state, "v4.2 - Security Hardening")
    ms_perf = find_milestone_by_title(state, "v4.1 - Performance")
    lbl_sec = find_label_by_title(state, "security")
    for issue in state["issues"]:
        if issue["milestoneId"] == ms_sec["id"] and lbl_sec["id"] not in issue["labels"]:
            issue["milestoneId"] = ms_perf["id"]
            issue["updatedAt"] = NOW


def solve_task_h4(state):
    """Create Hotfix Cadence with 1-week duration, then create Hotfix 1 iteration."""
    cid = next_cadence_id(state)
    cadence_id = f"cad_{cid}"
    state["iterationCadences"].append({
        "id": cadence_id,
        "title": "Hotfix Cadence",
        "description": "",
        "automatic": False,
        "startDate": "2026-03-03",
        "durationWeeks": 1,
        "upcomingIterations": 1,
        "rollOver": False,
        "active": True,
    })
    iid = next_iteration_id(state)
    state["iterations"].append({
        "id": f"iter_{iid}",
        "title": "Hotfix 1",
        "cadenceId": cadence_id,
        "startDate": "2026-03-03",
        "dueDate": "2026-03-09",
        "status": "upcoming",
        "createdAt": NOW,
    })


def solve_task_h5(state):
    """Reassign all of James O'Brien's open issues to Yuki Tanaka."""
    james = find_user_by_name(state, "James O'Brien")
    yuki = find_user_by_name(state, "Yuki Tanaka")
    for issue in state["issues"]:
        if issue["status"] == "open" and james["id"] in issue["assignees"]:
            issue["assignees"] = [a for a in issue["assignees"] if a != james["id"]]
            if yuki["id"] not in issue["assignees"]:
                issue["assignees"].append(yuki["id"])
            issue["updatedAt"] = NOW


def solve_task_h6(state):
    """Close the v4.0 milestone and move all its open issues to v4.1."""
    ms_v40 = find_milestone_by_title(state, "v4.0 - Platform Redesign")
    ms_v41 = find_milestone_by_title(state, "v4.1 - Performance")
    ms_v40["status"] = "closed"
    for issue in state["issues"]:
        if issue["milestoneId"] == ms_v40["id"] and issue["status"] == "open":
            issue["milestoneId"] = ms_v41["id"]
            issue["updatedAt"] = NOW


def solve_task_h7(state):
    """Remove all labels from the error boundary issue and replace with type::bug and priority::medium."""
    issue = find_issue_by_title(state, "Improve error boundary fallback UI")
    lbl_bug = find_label_by_title(state, "type::bug")
    lbl_med = find_label_by_title(state, "priority::medium")
    issue["labels"] = [lbl_bug["id"], lbl_med["id"]]
    issue["updatedAt"] = NOW


def solve_task_h8(state):
    """Create confidential issue 'Emergency security patch' with priority::critical, security, assigned to James O'Brien and Oliver Schmidt, weight 2, in Security Hardening milestone."""
    lbl_crit = find_label_by_title(state, "priority::critical")
    lbl_sec = find_label_by_title(state, "security")
    james = find_user_by_name(state, "James O'Brien")
    oliver = find_user_by_name(state, "Oliver Schmidt")
    ms = find_milestone_by_title(state, "v4.2 - Security Hardening")
    iid = next_issue_id(state)
    state["issues"].append({
        "id": f"issue_{iid}",
        "iid": iid,
        "title": "Emergency security patch",
        "description": "",
        "status": "open",
        "assignees": [james["id"], oliver["id"]],
        "labels": [lbl_crit["id"], lbl_sec["id"]],
        "milestoneId": ms["id"],
        "iterationId": None,
        "epicId": None,
        "weight": 2,
        "dueDate": None,
        "startDate": None,
        "healthStatus": None,
        "timeEstimate": 0,
        "timeSpent": 0,
        "confidential": True,
        "authorId": state["currentUser"]["id"],
        "createdAt": NOW,
        "updatedAt": NOW,
        "closedAt": None,
        "taskIds": [],
        "linkedIssueIds": [],
    })


def solve_task_h9(state):
    """Move all unassigned open issues to the Backlog milestone and add 'needs-discussion' label."""
    ms = find_milestone_by_title(state, "Backlog")
    lbl = find_label_by_title(state, "needs-discussion")
    for issue in state["issues"]:
        if issue["status"] == "open" and len(issue["assignees"]) == 0:
            issue["milestoneId"] = ms["id"]
            if lbl["id"] not in issue["labels"]:
                issue["labels"].append(lbl["id"])
            issue["updatedAt"] = NOW


def solve_task_h10(state):
    """Delete the Sprint Board and create a new Release Board with lists for v4.0, v4.1, and v4.2 milestones."""
    state["boards"] = [b for b in state["boards"] if b["name"] != "Sprint Board"]
    ms_v40 = find_milestone_by_title(state, "v4.0 - Platform Redesign")
    ms_v41 = find_milestone_by_title(state, "v4.1 - Performance")
    ms_v42 = find_milestone_by_title(state, "v4.2 - Security Hardening")
    bid = next_board_id(state)
    state["boards"].append({
        "id": f"board_{bid}",
        "name": "Release Board",
        "lists": [
            {"id": f"list_{bid}_1", "type": "milestone", "milestoneId": ms_v40["id"], "position": 0},
            {"id": f"list_{bid}_2", "type": "milestone", "milestoneId": ms_v41["id"], "position": 1},
            {"id": f"list_{bid}_3", "type": "milestone", "milestoneId": ms_v42["id"], "position": 2},
        ],
    })


def solve_task_h11(state):
    """Reassign all of Luca Rossi's issues under the Performance Initiative epic tree to Chen Wei."""
    luca = find_user_by_name(state, "Luca Rossi")
    chen = find_user_by_name(state, "Chen Wei")
    perf_epic = find_epic_by_title(state, "Performance Initiative")
    # Collect all epic IDs in the tree (parent + children)
    epic_ids = {perf_epic["id"]}
    for epic in state["epics"]:
        if epic["parentEpicId"] == perf_epic["id"]:
            epic_ids.add(epic["id"])
    for issue in state["issues"]:
        if issue["epicId"] in epic_ids and luca["id"] in issue["assignees"]:
            issue["assignees"] = [a for a in issue["assignees"] if a != luca["id"]]
            if chen["id"] not in issue["assignees"]:
                issue["assignees"].append(chen["id"])
            issue["updatedAt"] = NOW


def solve_task_h12(state):
    """Set weight to 8 and add priority::high to all issues in the Database Optimization epic."""
    epic = find_epic_by_title(state, "Database Optimization")
    lbl_high = find_label_by_title(state, "priority::high")
    for issue in state["issues"]:
        if issue["epicId"] == epic["id"]:
            issue["weight"] = 8
            # Remove existing priority:: labels (scoped)
            issue["labels"] = [l for l in issue["labels"]
                               if not any(lab["title"].startswith("priority::") and lab["id"] == l
                                          for lab in state["labels"])]
            if lbl_high["id"] not in issue["labels"]:
                issue["labels"].append(lbl_high["id"])
            issue["updatedAt"] = NOW


def solve_task_h13(state):
    """Create label 'sprint-goal' with green color, then apply to all open issues in Sprint 26."""
    lid = next_label_id(state)
    label_id = f"lbl_{lid}"
    state["labels"].append({
        "id": label_id,
        "title": "sprint-goal",
        "description": "",
        "color": "#1aaa55",
        "textColor": "#fff",
        "type": "project",
        "scoped": False,
    })
    sprint26 = find_iteration_by_title(state, "Sprint 26")
    for issue in state["issues"]:
        if issue["status"] == "open" and issue["iterationId"] == sprint26["id"]:
            if label_id not in issue["labels"]:
                issue["labels"].append(label_id)
            issue["updatedAt"] = NOW


def solve_task_h14(state):
    """Mark all pending todos as done, then create a new issue 'Review Q1 objectives' assigned to self with priority::medium."""
    for todo in state["todos"]:
        if todo["status"] == "pending":
            todo["status"] = "done"
    lbl = find_label_by_title(state, "priority::medium")
    iid = next_issue_id(state)
    state["issues"].append({
        "id": f"issue_{iid}",
        "iid": iid,
        "title": "Review Q1 objectives",
        "description": "",
        "status": "open",
        "assignees": [state["currentUser"]["id"]],
        "labels": [lbl["id"]],
        "milestoneId": None,
        "iterationId": None,
        "epicId": None,
        "weight": None,
        "dueDate": None,
        "startDate": None,
        "healthStatus": None,
        "timeEstimate": 0,
        "timeSpent": 0,
        "confidential": False,
        "authorId": state["currentUser"]["id"],
        "createdAt": NOW,
        "updatedAt": NOW,
        "closedAt": None,
        "taskIds": [],
        "linkedIssueIds": [],
    })


def solve_task_h15(state):
    """Delete all labels in the 'component' scope."""
    component_ids = {l["id"] for l in state["labels"] if l["title"].startswith("component::")}
    state["labels"] = [l for l in state["labels"] if l["id"] not in component_ids]
    for issue in state["issues"]:
        orig_len = len(issue["labels"])
        issue["labels"] = [l for l in issue["labels"] if l not in component_ids]
        if len(issue["labels"]) != orig_len:
            issue["updatedAt"] = NOW
    for epic in state["epics"]:
        epic["labels"] = [l for l in epic["labels"] if l not in component_ids]


def solve_task_h16(state):
    """Make sure Nina Kowalski is assigned to every issue in the Frontend Modernization epic."""
    nina = find_user_by_name(state, "Nina Kowalski")
    epic = find_epic_by_title(state, "Frontend Modernization")
    for issue in state["issues"]:
        if issue["epicId"] == epic["id"]:
            if nina["id"] not in issue["assignees"]:
                issue["assignees"].append(nina["id"])
                issue["updatedAt"] = NOW


def solve_task_h17(state):
    """Remove 'technical-debt' label from all issues and add 'type::improvement' instead."""
    lbl_td = find_label_by_title(state, "technical-debt")
    lbl_imp = find_label_by_title(state, "type::improvement")
    for issue in state["issues"]:
        if lbl_td["id"] in issue["labels"]:
            issue["labels"] = [l for l in issue["labels"] if l != lbl_td["id"]]
            # type::improvement is scoped, remove existing type:: labels
            issue["labels"] = [l for l in issue["labels"]
                               if not any(lab["title"].startswith("type::") and lab["id"] == l
                                          for lab in state["labels"])]
            if lbl_imp["id"] not in issue["labels"]:
                issue["labels"].append(lbl_imp["id"])
            issue["updatedAt"] = NOW


def solve_task_h18(state):
    """Create milestone 'Bug Bash Week' then move open type::bug issues without a milestone into it."""
    mid = next_milestone_id(state)
    ms_id = f"ms_{mid}"
    state["milestones"].append({
        "id": ms_id,
        "title": "Bug Bash Week",
        "description": "",
        "startDate": "2026-03-10",
        "dueDate": "2026-03-14",
        "status": "active",
        "createdAt": NOW,
    })
    lbl_bug = find_label_by_title(state, "type::bug")
    for issue in state["issues"]:
        if (issue["status"] == "open"
                and lbl_bug["id"] in issue["labels"]
                and issue["milestoneId"] is None):
            issue["milestoneId"] = ms_id
            issue["updatedAt"] = NOW


def solve_task_h19(state):
    """Close the Caching Layer Implementation epic and reassign its issues to Database Optimization."""
    epic_cache = find_epic_by_title(state, "Caching Layer Implementation")
    epic_db = find_epic_by_title(state, "Database Optimization")
    epic_cache["status"] = "closed"
    epic_cache["updatedAt"] = NOW
    for issue in state["issues"]:
        if issue["epicId"] == epic_cache["id"]:
            issue["epicId"] = epic_db["id"]
            issue["updatedAt"] = NOW


def solve_task_h20(state):
    """Delete 'blocked' label, create 'status::blocked' with #b91c1c, apply to user settings migration issue."""
    # Delete old blocked label
    old_lbl = find_label_by_title(state, "blocked")
    old_id = old_lbl["id"]
    state["labels"] = [l for l in state["labels"] if l["id"] != old_id]
    # Remove from all issues and epics
    for issue in state["issues"]:
        issue["labels"] = [l for l in issue["labels"] if l != old_id]
    for epic in state["epics"]:
        epic["labels"] = [l for l in epic["labels"] if l != old_id]

    # Create new scoped label
    lid = next_label_id(state)
    new_label_id = f"lbl_{lid}"
    state["labels"].append({
        "id": new_label_id,
        "title": "status::blocked",
        "description": "",
        "color": "#b91c1c",
        "textColor": "#fff",
        "type": "project",
        "scoped": True,
    })
    # Apply to user settings migration issue
    issue = find_issue_by_title(state, "Migrate user settings page to React")
    if new_label_id not in issue["labels"]:
        issue["labels"].append(new_label_id)
    issue["updatedAt"] = NOW


# ── Hardening round 1 solve functions ─────────────────────────────────

def solve_task_h21(state):
    """Log 3h with summary 'Schema validation review' on GraphQL gateway issue; set health to needs_attention."""
    issue = find_issue_by_title(state, "Implement GraphQL gateway for v3 API")
    issue["healthStatus"] = "needs_attention"
    issue["updatedAt"] = NOW
    tl_id = state.get("_nextTimelogId", 30)
    state["_nextTimelogId"] = tl_id + 1
    state["timelogs"].append({
        "id": f"tl_{tl_id}",
        "issueId": issue["id"],
        "userId": state["currentUser"]["id"],
        "timeSpent": 10800,
        "summary": "Schema validation review",
        "spentAt": NOW,
    })
    issue["timeSpent"] = issue.get("timeSpent", 0) + 10800


def solve_task_h22(state):
    """Assign Chen Wei to the unassigned open issue in Security Hardening epic; set iteration to Sprint 27."""
    issue = find_issue_by_title(state, "Implement CSRF token rotation")
    chen = find_user_by_name(state, "Chen Wei")
    sprint27 = find_iteration_by_title(state, "Sprint 27")
    issue["assignees"] = [chen["id"]]
    issue["iterationId"] = sprint27["id"]
    issue["updatedAt"] = NOW


def solve_task_h23(state):
    """Create 'Security Overview' board with lists for priority::critical, priority::high, and security."""
    lbl_crit = find_label_by_title(state, "priority::critical")
    lbl_high = find_label_by_title(state, "priority::high")
    lbl_sec = find_label_by_title(state, "security")
    bid = next_board_id(state)
    state["boards"].append({
        "id": f"board_{bid}",
        "name": "Security Overview",
        "lists": [
            {"id": f"list_{bid}_1", "type": "label", "labelId": lbl_crit["id"], "position": 0},
            {"id": f"list_{bid}_2", "type": "label", "labelId": lbl_high["id"], "position": 1},
            {"id": f"list_{bid}_3", "type": "label", "labelId": lbl_sec["id"], "position": 2},
        ],
    })


def solve_task_h24(state):
    """Delete all timelogs from user settings migration issue; set time estimate to 20h."""
    issue = find_issue_by_title(state, "Migrate user settings page to React")
    issue_id = issue["id"]
    state["timelogs"] = [t for t in state["timelogs"] if t["issueId"] != issue_id]
    issue["timeEstimate"] = 72000
    issue["timeSpent"] = 0
    issue["updatedAt"] = NOW


def solve_task_h25(state):
    """Set health status of Performance Initiative and both child epics to needs_attention."""
    perf_epic = find_epic_by_title(state, "Performance Initiative")
    perf_epic["healthStatus"] = "needs_attention"
    perf_epic["updatedAt"] = NOW
    for epic in state["epics"]:
        if epic["parentEpicId"] == perf_epic["id"]:
            epic["healthStatus"] = "needs_attention"
            epic["updatedAt"] = NOW


def solve_task_h26(state):
    """Create 'Technical Debt Cleanup' epic under Platform Redesign; move technical-debt issues into it."""
    platform_epic = find_epic_by_title(state, "Platform Redesign")
    td_label = find_label_by_title(state, "technical-debt")
    iid = next_epic_iid(state)
    epic_id = f"epic_{iid}"
    state["epics"].append({
        "id": epic_id,
        "iid": iid,
        "title": "Technical Debt Cleanup",
        "description": "",
        "status": "open",
        "startDate": None,
        "dueDate": None,
        "labels": [],
        "healthStatus": None,
        "authorId": state["currentUser"]["id"],
        "confidential": False,
        "parentEpicId": platform_epic["id"],
        "createdAt": NOW,
        "updatedAt": NOW,
    })
    for issue in state["issues"]:
        if td_label["id"] in issue["labels"]:
            issue["epicId"] = epic_id
            issue["updatedAt"] = NOW


def solve_task_h27(state):
    """Rename Monthly Planning to 'Bi-Weekly Planning' with 2-week duration."""
    cad = find_cadence_by_title(state, "Monthly Planning")
    cad["title"] = "Bi-Weekly Planning"
    cad["durationWeeks"] = 2


def solve_task_h28(state):
    """Add 2h timelog 'Security review' to CSP headers issue; move from Sprint 26 to Sprint 28."""
    issue = find_issue_by_title(state, "Implement Content Security Policy headers")
    sprint28 = find_iteration_by_title(state, "Sprint 28")
    issue["iterationId"] = sprint28["id"]
    issue["updatedAt"] = NOW
    tl_id = state.get("_nextTimelogId", 30)
    state["_nextTimelogId"] = tl_id + 1
    state["timelogs"].append({
        "id": f"tl_{tl_id}",
        "issueId": issue["id"],
        "userId": state["currentUser"]["id"],
        "timeSpent": 7200,
        "summary": "Security review",
        "spentAt": NOW,
    })
    issue["timeSpent"] = issue.get("timeSpent", 0) + 7200


def solve_task_h29(state):
    """Close all open type::bug issues in v4.1 - Performance milestone."""
    ms = find_milestone_by_title(state, "v4.1 - Performance")
    lbl_bug = find_label_by_title(state, "type::bug")
    for issue in state["issues"]:
        if (issue["milestoneId"] == ms["id"]
                and lbl_bug["id"] in issue["labels"]
                and issue["status"] == "open"):
            issue["status"] = "closed"
            issue["closedAt"] = NOW
            issue["updatedAt"] = NOW


def solve_task_h30(state):
    """Create 'Security Sprint' in Release Cycle; assign all open Security Hardening epic issues to it."""
    release_cad = find_cadence_by_title(state, "Release Cycle")
    iid = next_iteration_id(state)
    iter_id = f"iter_{iid}"
    state["iterations"].append({
        "id": iter_id,
        "title": "Security Sprint",
        "cadenceId": release_cad["id"],
        "startDate": "2026-03-03",
        "dueDate": "2026-03-16",
        "status": "upcoming",
        "createdAt": NOW,
    })
    sec_epic = find_epic_by_title(state, "Security Hardening")
    for issue in state["issues"]:
        if issue["epicId"] == sec_epic["id"] and issue["status"] == "open":
            issue["iterationId"] = iter_id
            issue["updatedAt"] = NOW


def solve_task_h31(state):
    """Make Enterprise SSO Integration a child of Security Hardening; set health to on_track."""
    sso_epic = find_epic_by_title(state, "Enterprise SSO Integration")
    sec_epic = find_epic_by_title(state, "Security Hardening")
    sso_epic["parentEpicId"] = sec_epic["id"]
    sso_epic["healthStatus"] = "on_track"
    sso_epic["updatedAt"] = NOW


def solve_task_h32(state):
    """Assign Sarah Chen + Marcus Johnson to CSRF issue; set priority::high; move to Sprint 28."""
    issue = find_issue_by_title(state, "Implement CSRF token rotation")
    sarah = find_user_by_name(state, "Sarah Chen")
    marcus = find_user_by_name(state, "Marcus Johnson")
    sprint28 = find_iteration_by_title(state, "Sprint 28")
    lbl_high = find_label_by_title(state, "priority::high")
    # Add assignees
    for uid in [sarah["id"], marcus["id"]]:
        if uid not in issue["assignees"]:
            issue["assignees"].append(uid)
    # Replace scoped priority label
    issue["labels"] = [l for l in issue["labels"]
                       if not any(lab["title"].startswith("priority::") and lab["id"] == l
                                  for lab in state["labels"])]
    if lbl_high["id"] not in issue["labels"]:
        issue["labels"].append(lbl_high["id"])
    issue["iterationId"] = sprint28["id"]
    issue["updatedAt"] = NOW


def solve_task_h33(state):
    """Delete Bug Triage board; create Team Workload with workflow::ready, in-progress, review lists."""
    state["boards"] = [b for b in state["boards"] if b["name"] != "Bug Triage"]
    lbl_ready = find_label_by_title(state, "workflow::ready")
    lbl_ip = find_label_by_title(state, "workflow::in-progress")
    lbl_review = find_label_by_title(state, "workflow::review")
    bid = next_board_id(state)
    state["boards"].append({
        "id": f"board_{bid}",
        "name": "Team Workload",
        "lists": [
            {"id": f"list_{bid}_1", "type": "label", "labelId": lbl_ready["id"], "position": 0},
            {"id": f"list_{bid}_2", "type": "label", "labelId": lbl_ip["id"], "position": 1},
            {"id": f"list_{bid}_3", "type": "label", "labelId": lbl_review["id"], "position": 2},
        ],
    })


def solve_task_h34(state):
    """Close both issues in Documentation Overhaul epic, remove milestones, close epic."""
    epic = find_epic_by_title(state, "Documentation Overhaul")
    for issue in state["issues"]:
        if issue["epicId"] == epic["id"]:
            issue["status"] = "closed"
            issue["closedAt"] = NOW
            issue["milestoneId"] = None
            issue["updatedAt"] = NOW
    epic["status"] = "closed"
    epic["updatedAt"] = NOW


def solve_task_h35(state):
    """Rename 'performance' label to 'perf', color #0284c7, description 'Performance optimization work'."""
    label = find_label_by_title(state, "performance")
    label["title"] = "perf"
    label["color"] = "#0284c7"
    label["description"] = "Performance optimization work"


def solve_task_h36(state):
    """Reopen the two closed issues from Sprint 24 and move them to Sprint 28."""
    sprint28 = find_iteration_by_title(state, "Sprint 28")
    for title in [
        "Implement sidebar navigation with collapsible sections",
        "Create reusable modal dialog system",
    ]:
        issue = find_issue_by_title(state, title)
        issue["status"] = "open"
        issue["closedAt"] = None
        issue["iterationId"] = sprint28["id"]
        issue["updatedAt"] = NOW


def solve_task_h37(state):
    """Add accessibility label to every open issue in Frontend Modernization epic that lacks it."""
    epic = find_epic_by_title(state, "Frontend Modernization")
    acc_label = find_label_by_title(state, "accessibility")
    for issue in state["issues"]:
        if (issue["epicId"] == epic["id"]
                and issue["status"] == "open"
                and acc_label["id"] not in issue["labels"]):
            issue["labels"].append(acc_label["id"])
            issue["updatedAt"] = NOW


def solve_task_h38(state):
    """Set weight 5 and priority::medium on open issues with no assignees, no milestone, no epic."""
    lbl_med = find_label_by_title(state, "priority::medium")
    for issue in state["issues"]:
        if (issue["status"] == "open"
                and len(issue["assignees"]) == 0
                and issue["milestoneId"] is None
                and issue["epicId"] is None):
            issue["weight"] = 5
            # Replace scoped priority label
            issue["labels"] = [l for l in issue["labels"]
                               if not any(lab["title"].startswith("priority::") and lab["id"] == l
                                          for lab in state["labels"])]
            if lbl_med["id"] not in issue["labels"]:
                issue["labels"].append(lbl_med["id"])
            issue["updatedAt"] = NOW


def solve_task_h39(state):
    """Enable automatic scheduling on Release Cycle cadence: March 1, 4-week, 2 upcoming."""
    cad = find_cadence_by_title(state, "Release Cycle")
    cad["automatic"] = True
    cad["startDate"] = "2026-03-01"
    cad["durationWeeks"] = 4
    cad["upcomingIterations"] = 2


def solve_task_h40(state):
    """Create 'needs-review' label with color #fbca04; apply to all open issues assigned to Marcus Johnson."""
    marcus = find_user_by_name(state, "Marcus Johnson")
    lid = next_label_id(state)
    label_id = f"lbl_{lid}"
    state["labels"].append({
        "id": label_id,
        "title": "needs-review",
        "description": "",
        "color": "#fbca04",
        "textColor": "#333",
        "type": "project",
        "scoped": False,
    })
    for issue in state["issues"]:
        if marcus["id"] in issue["assignees"] and issue["status"] == "open":
            if label_id not in issue["labels"]:
                issue["labels"].append(label_id)
            issue["updatedAt"] = NOW


# ── Hardening round 2 solve functions ─────────────────────────────────

def solve_task_h41(state):
    """For open issues in v4.2: if confidential -> at_risk; if not -> make confidential + needs_attention."""
    ms = find_milestone_by_title(state, "v4.2 - Security Hardening")
    for issue in state["issues"]:
        if issue["milestoneId"] == ms["id"] and issue["status"] == "open":
            if issue["confidential"]:
                issue["healthStatus"] = "at_risk"
            else:
                issue["confidential"] = True
                issue["healthStatus"] = "needs_attention"
            issue["updatedAt"] = NOW


def solve_task_h42(state):
    """Find at_risk epic (Security Hardening), create milestone, move its open issues."""
    sec_epic = find_epic_by_title(state, "Security Hardening")
    mid = next_milestone_id(state)
    ms_id = f"ms_{mid}"
    state["milestones"].append({
        "id": ms_id,
        "title": "Risk Mitigation Sprint",
        "description": "",
        "startDate": "2026-03-03",
        "dueDate": "2026-03-14",
        "status": "active",
        "createdAt": NOW,
    })
    for issue in state["issues"]:
        if issue["epicId"] == sec_epic["id"] and issue["status"] == "open":
            issue["milestoneId"] = ms_id
            issue["updatedAt"] = NOW


def solve_task_h43(state):
    """Assign highest-weight open issue to Sprint 27 and add needs-discussion."""
    issue = find_issue_by_title(state, "Build real-time collaborative editing for issue descriptions")
    sprint27 = find_iteration_by_title(state, "Sprint 27")
    nd_label = find_label_by_title(state, "needs-discussion")
    issue["iterationId"] = sprint27["id"]
    if nd_label["id"] not in issue["labels"]:
        issue["labels"].append(nd_label["id"])
    issue["updatedAt"] = NOW


def solve_task_h44(state):
    """Create review::pending label; apply to all open issues with workflow::ready."""
    ready_label = find_label_by_title(state, "workflow::ready")
    lid = next_label_id(state)
    label_id = f"lbl_{lid}"
    state["labels"].append({
        "id": label_id,
        "title": "review::pending",
        "description": "",
        "color": "#7b68ee",
        "textColor": "#fff",
        "type": "project",
        "scoped": True,
    })
    for issue in state["issues"]:
        if issue["status"] == "open" and ready_label["id"] in issue["labels"]:
            if label_id not in issue["labels"]:
                issue["labels"].append(label_id)
            issue["updatedAt"] = NOW


def solve_task_h45(state):
    """Close the Platform Redesign child epic with fewer open issues (API v3 Migration)."""
    api_epic = find_epic_by_title(state, "API v3 Migration")
    api_epic["status"] = "closed"
    api_epic["updatedAt"] = NOW


def solve_task_h46(state):
    """Move open issues with no epic and no milestone to Backlog + Documentation Overhaul."""
    backlog = find_milestone_by_title(state, "Backlog")
    doc_epic = find_epic_by_title(state, "Documentation Overhaul")
    for issue in state["issues"]:
        if (issue["status"] == "open"
                and issue["epicId"] is None
                and issue["milestoneId"] is None):
            issue["milestoneId"] = backlog["id"]
            issue["epicId"] = doc_epic["id"]
            issue["updatedAt"] = NOW


def solve_task_h47(state):
    """Create Patch Release iteration in Release Cycle; assign open security issues with no iteration."""
    release_cad = find_cadence_by_title(state, "Release Cycle")
    iid = next_iteration_id(state)
    iter_id = f"iter_{iid}"
    state["iterations"].append({
        "id": iter_id,
        "title": "Patch Release",
        "cadenceId": release_cad["id"],
        "startDate": "2026-03-17",
        "dueDate": "2026-03-28",
        "status": "upcoming",
        "createdAt": NOW,
    })
    sec_label = find_label_by_title(state, "security")
    for issue in state["issues"]:
        if (issue["status"] == "open"
                and sec_label["id"] in issue["labels"]
                and issue.get("iterationId") is None):
            issue["iterationId"] = iter_id
            issue["updatedAt"] = NOW


def solve_task_h48(state):
    """Add breaking-change and remove workflow labels from API v3 Migration epic issues."""
    api_epic = find_epic_by_title(state, "API v3 Migration")
    bc_label = find_label_by_title(state, "breaking-change")
    workflow_ids = {l["id"] for l in state["labels"] if l["title"].startswith("workflow::")}
    for issue in state["issues"]:
        if issue["epicId"] == api_epic["id"] and issue["status"] == "open":
            issue["labels"] = [l for l in issue["labels"] if l not in workflow_ids]
            if bc_label["id"] not in issue["labels"]:
                issue["labels"].append(bc_label["id"])
            issue["updatedAt"] = NOW


def solve_task_h49(state):
    """Create two issues in Mobile App v2 epic assigned to Priya Patel."""
    mobile_epic = find_epic_by_title(state, "Mobile App v2")
    priya = find_user_by_name(state, "Priya Patel")
    design_label = find_label_by_title(state, "design-needed")
    task_label = find_label_by_title(state, "type::task")

    iid1 = next_issue_id(state)
    state["issues"].append({
        "id": f"issue_{iid1}",
        "iid": iid1,
        "title": "Mobile app wireframes",
        "description": "",
        "status": "open",
        "assignees": [priya["id"]],
        "labels": [design_label["id"]],
        "milestoneId": None,
        "iterationId": None,
        "epicId": mobile_epic["id"],
        "weight": 5,
        "dueDate": None,
        "startDate": None,
        "healthStatus": None,
        "timeEstimate": 0,
        "timeSpent": 0,
        "confidential": False,
        "authorId": state["currentUser"]["id"],
        "createdAt": NOW,
        "updatedAt": NOW,
        "closedAt": None,
        "taskIds": [],
        "linkedIssueIds": [],
    })

    iid2 = next_issue_id(state)
    state["issues"].append({
        "id": f"issue_{iid2}",
        "iid": iid2,
        "title": "React Native project scaffolding",
        "description": "",
        "status": "open",
        "assignees": [priya["id"]],
        "labels": [task_label["id"]],
        "milestoneId": None,
        "iterationId": None,
        "epicId": mobile_epic["id"],
        "weight": 3,
        "dueDate": None,
        "startDate": None,
        "healthStatus": None,
        "timeEstimate": 0,
        "timeSpent": 0,
        "confidential": False,
        "authorId": state["currentUser"]["id"],
        "createdAt": NOW,
        "updatedAt": NOW,
        "closedAt": None,
        "taskIds": [],
        "linkedIssueIds": [],
    })


def solve_task_h50(state):
    """Log 1h 'Sprint planning review' on Oliver Schmidt's open issues; set health to on_track."""
    oliver = find_user_by_name(state, "Oliver Schmidt")
    for issue in state["issues"]:
        if issue["status"] == "open" and oliver["id"] in issue["assignees"]:
            issue["healthStatus"] = "on_track"
            issue["updatedAt"] = NOW
            tl_id = state.get("_nextTimelogId", 30)
            state["_nextTimelogId"] = tl_id + 1
            state["timelogs"].append({
                "id": f"tl_{tl_id}",
                "issueId": issue["id"],
                "userId": state["currentUser"]["id"],
                "timeSpent": 3600,
                "summary": "Sprint planning review",
                "spentAt": NOW,
            })
            issue["timeSpent"] = issue.get("timeSpent", 0) + 3600


def solve_task_h51(state):
    """Close open type::documentation issues and remove milestones."""
    doc_label = find_label_by_title(state, "type::documentation")
    for issue in state["issues"]:
        if issue["status"] == "open" and doc_label["id"] in issue["labels"]:
            issue["status"] = "closed"
            issue["closedAt"] = NOW
            issue["milestoneId"] = None
            issue["updatedAt"] = NOW


def solve_task_h52(state):
    """Create Performance Tracker board; add priority::high to performance issues in v4.1."""
    lbl_crit = find_label_by_title(state, "priority::critical")
    lbl_high = find_label_by_title(state, "priority::high")
    lbl_med = find_label_by_title(state, "priority::medium")
    bid = next_board_id(state)
    state["boards"].append({
        "id": f"board_{bid}",
        "name": "Performance Tracker",
        "lists": [
            {"id": f"list_{bid}_1", "type": "label", "labelId": lbl_crit["id"], "position": 0},
            {"id": f"list_{bid}_2", "type": "label", "labelId": lbl_high["id"], "position": 1},
            {"id": f"list_{bid}_3", "type": "label", "labelId": lbl_med["id"], "position": 2},
        ],
    })
    ms_v41 = find_milestone_by_title(state, "v4.1 - Performance")
    perf_label = find_label_by_title(state, "performance")
    for issue in state["issues"]:
        if (issue["milestoneId"] == ms_v41["id"]
                and issue["status"] == "open"
                and perf_label["id"] in issue["labels"]):
            # Replace existing priority:: scoped labels
            issue["labels"] = [l for l in issue["labels"]
                               if not any(lab["title"].startswith("priority::") and lab["id"] == l
                                          for lab in state["labels"])]
            if lbl_high["id"] not in issue["labels"]:
                issue["labels"].append(lbl_high["id"])
            issue["updatedAt"] = NOW


def solve_task_h53(state):
    """Set health and label on top-level epic with latest due date (Mobile App v2)."""
    mobile_epic = find_epic_by_title(state, "Mobile App v2")
    nd_label = find_label_by_title(state, "needs-discussion")
    mobile_epic["healthStatus"] = "needs_attention"
    if nd_label["id"] not in mobile_epic["labels"]:
        mobile_epic["labels"].append(nd_label["id"])
    mobile_epic["updatedAt"] = NOW


def solve_task_h54(state):
    """Replace labels on Performance Initiative; set child epics to at_risk."""
    perf_epic = find_epic_by_title(state, "Performance Initiative")
    lbl_high = find_label_by_title(state, "priority::high")
    lbl_nd = find_label_by_title(state, "needs-discussion")
    perf_epic["labels"] = [lbl_high["id"], lbl_nd["id"]]
    perf_epic["updatedAt"] = NOW
    for epic in state["epics"]:
        if epic["parentEpicId"] == perf_epic["id"]:
            epic["healthStatus"] = "at_risk"
            epic["updatedAt"] = NOW


def solve_task_h55(state):
    """Update security label color/description; set weight 13 on Security Hardening epic issues with it."""
    sec_label = find_label_by_title(state, "security")
    sec_label["color"] = "#000000"
    sec_label["description"] = "Critical security work"
    sec_epic = find_epic_by_title(state, "Security Hardening")
    for issue in state["issues"]:
        if (issue["epicId"] == sec_epic["id"]
                and issue["status"] == "open"
                and sec_label["id"] in issue["labels"]):
            issue["weight"] = 13
            issue["updatedAt"] = NOW


def solve_task_h56(state):
    """Reassign Aisha's v4.0 open issues to Nina; set iteration to Sprint 28."""
    aisha = find_user_by_name(state, "Aisha Mohammed")
    nina = find_user_by_name(state, "Nina Kowalski")
    ms_v40 = find_milestone_by_title(state, "v4.0 - Platform Redesign")
    sprint28 = find_iteration_by_title(state, "Sprint 28")
    for issue in state["issues"]:
        if (issue["status"] == "open"
                and issue["milestoneId"] == ms_v40["id"]
                and aisha["id"] in issue["assignees"]):
            issue["assignees"] = [a for a in issue["assignees"] if a != aisha["id"]]
            if nina["id"] not in issue["assignees"]:
                issue["assignees"].append(nina["id"])
            issue["iterationId"] = sprint28["id"]
            issue["updatedAt"] = NOW


def solve_task_h57(state):
    """Create sprint-carry-over label; apply to Sprint 26 at-risk/needs-attention issues; move to Sprint 27."""
    lid = next_label_id(state)
    label_id = f"lbl_{lid}"
    state["labels"].append({
        "id": label_id,
        "title": "sprint-carry-over",
        "description": "",
        "color": "#f97316",
        "textColor": "#fff",
        "type": "project",
        "scoped": False,
    })
    sprint26 = find_iteration_by_title(state, "Sprint 26")
    sprint27 = find_iteration_by_title(state, "Sprint 27")
    for issue in state["issues"]:
        if (issue["status"] == "open"
                and issue["iterationId"] == sprint26["id"]
                and issue.get("healthStatus") in ("needs_attention", "at_risk")):
            if label_id not in issue["labels"]:
                issue["labels"].append(label_id)
            issue["iterationId"] = sprint27["id"]
            issue["updatedAt"] = NOW


def solve_task_h58(state):
    """DB Optimization (more issues) -> weight 13; Caching Layer (fewer) -> close all."""
    db_epic = find_epic_by_title(state, "Database Optimization")
    cache_epic = find_epic_by_title(state, "Caching Layer Implementation")
    for issue in state["issues"]:
        if issue["epicId"] == db_epic["id"]:
            issue["weight"] = 13
            issue["updatedAt"] = NOW
    for issue in state["issues"]:
        if issue["epicId"] == cache_epic["id"] and issue["status"] == "open":
            issue["status"] = "closed"
            issue["closedAt"] = NOW
            issue["updatedAt"] = NOW


def solve_task_h59(state):
    """Sprint 26 issues with due date before March 2 -> at_risk + move to Sprint 27."""
    sprint27 = find_iteration_by_title(state, "Sprint 27")
    sprint26 = find_iteration_by_title(state, "Sprint 26")
    for issue in state["issues"]:
        if (issue["status"] == "open"
                and issue["iterationId"] == sprint26["id"]
                and issue.get("dueDate") is not None
                and issue["dueDate"] < "2026-03-02"):
            issue["healthStatus"] = "at_risk"
            issue["iterationId"] = sprint27["id"]
            issue["updatedAt"] = NOW


def solve_task_h60(state):
    """Delete Sprint Board and Bug Triage; create Unified Workflow board with 4 workflow lists."""
    state["boards"] = [b for b in state["boards"]
                       if b["name"] not in ("Sprint Board", "Bug Triage")]
    lbl_ready = find_label_by_title(state, "workflow::ready")
    lbl_ip = find_label_by_title(state, "workflow::in-progress")
    lbl_review = find_label_by_title(state, "workflow::review")
    lbl_done = find_label_by_title(state, "workflow::done")
    bid = next_board_id(state)
    state["boards"].append({
        "id": f"board_{bid}",
        "name": "Unified Workflow",
        "lists": [
            {"id": f"list_{bid}_1", "type": "label", "labelId": lbl_ready["id"], "position": 0},
            {"id": f"list_{bid}_2", "type": "label", "labelId": lbl_ip["id"], "position": 1},
            {"id": f"list_{bid}_3", "type": "label", "labelId": lbl_review["id"], "position": 2},
            {"id": f"list_{bid}_4", "type": "label", "labelId": lbl_done["id"], "position": 3},
        ],
    })


# ── Hardening round 3 solve functions ─────────────────────────────────

def solve_task_h61(state):
    """Snooze all pending todos referencing issues in v4.0 milestone until March 10."""
    ms_v40 = find_milestone_by_title(state, "v4.0 - Platform Redesign")
    v40_issue_ids = {i["id"] for i in state["issues"] if i["milestoneId"] == ms_v40["id"]}
    for todo in state["todos"]:
        if (todo["status"] == "pending"
                and todo["targetType"] == "issue"
                and todo["targetId"] in v40_issue_ids):
            todo["status"] = "snoozed"
            todo["snoozedUntil"] = "2026-03-10T08:00:00Z"


def solve_task_h62(state):
    """Log 2h 'Sprint risk review' on at-risk/needs-attention Sprint 26 issues; move to Sprint 27."""
    sprint26 = find_iteration_by_title(state, "Sprint 26")
    sprint27 = find_iteration_by_title(state, "Sprint 27")
    for issue in state["issues"]:
        if (issue["status"] == "open"
                and issue["iterationId"] == sprint26["id"]
                and issue.get("healthStatus") in ("at_risk", "needs_attention")):
            issue["iterationId"] = sprint27["id"]
            issue["updatedAt"] = NOW
            tl_id = state.get("_nextTimelogId", 30)
            state["_nextTimelogId"] = tl_id + 1
            state["timelogs"].append({
                "id": f"tl_{tl_id}",
                "issueId": issue["id"],
                "userId": state["currentUser"]["id"],
                "timeSpent": 7200,
                "summary": "Sprint risk review",
                "spentAt": NOW,
            })
            issue["timeSpent"] = issue.get("timeSpent", 0) + 7200


def solve_task_h63(state):
    """Move open issues from Security Hardening (mentions 'security audit') to Performance (mentions 'performance optimization')."""
    ms_sec = find_milestone_by_title(state, "v4.2 - Security Hardening")
    ms_perf = find_milestone_by_title(state, "v4.1 - Performance")
    for issue in state["issues"]:
        if issue["milestoneId"] == ms_sec["id"] and issue["status"] == "open":
            issue["milestoneId"] = ms_perf["id"]
            issue["updatedAt"] = NOW


def solve_task_h64(state):
    """James O'Brien's issues: with milestone -> on_track; without -> Backlog + needs-discussion."""
    james = find_user_by_name(state, "James O'Brien")
    backlog = find_milestone_by_title(state, "Backlog")
    nd_label = find_label_by_title(state, "needs-discussion")
    for issue in state["issues"]:
        if issue["status"] == "open" and james["id"] in issue["assignees"]:
            if issue["milestoneId"] is not None:
                issue["healthStatus"] = "on_track"
            else:
                issue["milestoneId"] = backlog["id"]
                if nd_label["id"] not in issue["labels"]:
                    issue["labels"].append(nd_label["id"])
            issue["updatedAt"] = NOW


def solve_task_h65(state):
    """Performance issues: +database -> critical, +frontend -> high, others -> medium."""
    perf_label = find_label_by_title(state, "performance")
    db_label = find_label_by_title(state, "component::database")
    fe_label = find_label_by_title(state, "component::frontend")
    lbl_crit = find_label_by_title(state, "priority::critical")
    lbl_high = find_label_by_title(state, "priority::high")
    lbl_med = find_label_by_title(state, "priority::medium")
    priority_ids = {l["id"] for l in state["labels"] if l["title"].startswith("priority::")}
    for issue in state["issues"]:
        if issue["status"] == "open" and perf_label["id"] in issue["labels"]:
            # Remove existing priority labels
            issue["labels"] = [l for l in issue["labels"] if l not in priority_ids]
            if db_label["id"] in issue["labels"]:
                issue["labels"].append(lbl_crit["id"])
            elif fe_label["id"] in issue["labels"]:
                issue["labels"].append(lbl_high["id"])
            else:
                issue["labels"].append(lbl_med["id"])
            issue["updatedAt"] = NOW


def solve_task_h66(state):
    """Create 'sprint-focus' label (#0891b2); apply to all open Sprint 26 issues (most issues)."""
    lid = next_label_id(state)
    label_id = f"lbl_{lid}"
    state["labels"].append({
        "id": label_id,
        "title": "sprint-focus",
        "description": "",
        "color": "#0891b2",
        "textColor": "#fff",
        "type": "project",
        "scoped": False,
    })
    sprint26 = find_iteration_by_title(state, "Sprint 26")
    for issue in state["issues"]:
        if issue["status"] == "open" and issue["iterationId"] == sprint26["id"]:
            if label_id not in issue["labels"]:
                issue["labels"].append(label_id)
            issue["updatedAt"] = NOW


def solve_task_h67(state):
    """Delete all timelogs from GraphQL gateway; add 16h entry; set estimate to 40h."""
    issue = find_issue_by_title(state, "Implement GraphQL gateway for v3 API")
    issue_id = issue["id"]
    state["timelogs"] = [t for t in state["timelogs"] if t["issueId"] != issue_id]
    tl_id = state.get("_nextTimelogId", 30)
    state["_nextTimelogId"] = tl_id + 1
    state["timelogs"].append({
        "id": f"tl_{tl_id}",
        "issueId": issue_id,
        "userId": state["currentUser"]["id"],
        "timeSpent": 57600,
        "summary": "Complete rewrite estimate",
        "spentAt": NOW,
    })
    issue["timeSpent"] = 57600
    issue["timeEstimate"] = 144000
    issue["updatedAt"] = NOW


def solve_task_h68(state):
    """Log 1h 'Architecture review' on every open issue with weight >= 13."""
    for issue in state["issues"]:
        if (issue["status"] == "open"
                and issue.get("weight") is not None
                and issue["weight"] >= 13):
            tl_id = state.get("_nextTimelogId", 30)
            state["_nextTimelogId"] = tl_id + 1
            state["timelogs"].append({
                "id": f"tl_{tl_id}",
                "issueId": issue["id"],
                "userId": state["currentUser"]["id"],
                "timeSpent": 3600,
                "summary": "Architecture review",
                "spentAt": NOW,
            })
            issue["timeSpent"] = issue.get("timeSpent", 0) + 3600
            issue["updatedAt"] = NOW


def solve_task_h69(state):
    """Restore done todos to pending; snooze epic-referencing todos until March 15."""
    for todo in state["todos"]:
        if todo["status"] == "done":
            todo["status"] = "pending"
            todo["snoozedUntil"] = None
    for todo in state["todos"]:
        if todo["targetType"] == "epic" and todo["status"] == "pending":
            todo["status"] = "snoozed"
            todo["snoozedUntil"] = "2026-03-15T08:00:00Z"


def solve_task_h70(state):
    """Delete milestone-based board; create Milestone Tracker with 3 earliest-start milestones."""
    state["boards"] = [b for b in state["boards"] if b["name"] != "Sprint Board"]
    ms_v40 = find_milestone_by_title(state, "v4.0 - Platform Redesign")
    ms_q1 = find_milestone_by_title(state, "Q1 2026 Planning")
    ms_v41 = find_milestone_by_title(state, "v4.1 - Performance")
    bid = next_board_id(state)
    state["boards"].append({
        "id": f"board_{bid}",
        "name": "Milestone Tracker",
        "lists": [
            {"id": f"list_{bid}_1", "type": "milestone", "milestoneId": ms_v40["id"], "position": 0},
            {"id": f"list_{bid}_2", "type": "milestone", "milestoneId": ms_q1["id"], "position": 1},
            {"id": f"list_{bid}_3", "type": "milestone", "milestoneId": ms_v41["id"], "position": 2},
        ],
    })


def solve_task_h71(state):
    """Unassigned open issues: with milestone -> add needs-discussion; without -> Backlog + needs-discussion."""
    backlog = find_milestone_by_title(state, "Backlog")
    nd_label = find_label_by_title(state, "needs-discussion")
    for issue in state["issues"]:
        if issue["status"] == "open" and len(issue["assignees"]) == 0:
            if nd_label["id"] not in issue["labels"]:
                issue["labels"].append(nd_label["id"])
            if issue["milestoneId"] is None:
                issue["milestoneId"] = backlog["id"]
            issue["updatedAt"] = NOW


def solve_task_h72(state):
    """Add 30min timelog 'Resolved during onboarding' to good-first-issue issues, then close."""
    gfi_label = find_label_by_title(state, "good-first-issue")
    for issue in state["issues"]:
        if issue["status"] == "open" and gfi_label["id"] in issue["labels"]:
            tl_id = state.get("_nextTimelogId", 30)
            state["_nextTimelogId"] = tl_id + 1
            state["timelogs"].append({
                "id": f"tl_{tl_id}",
                "issueId": issue["id"],
                "userId": state["currentUser"]["id"],
                "timeSpent": 1800,
                "summary": "Resolved during onboarding",
                "spentAt": NOW,
            })
            issue["timeSpent"] = issue.get("timeSpent", 0) + 1800
            issue["status"] = "closed"
            issue["closedAt"] = NOW
            issue["updatedAt"] = NOW


def solve_task_h73(state):
    """Create Bug Fix Sprint in Sprint Cadence; move open type::bug issues with no iteration."""
    sprint_cad = find_cadence_by_title(state, "Sprint Cadence")
    iid = next_iteration_id(state)
    iter_id = f"iter_{iid}"
    state["iterations"].append({
        "id": iter_id,
        "title": "Bug Fix Sprint",
        "cadenceId": sprint_cad["id"],
        "startDate": "2026-03-31",
        "dueDate": "2026-04-13",
        "status": "upcoming",
        "createdAt": NOW,
    })
    bug_label = find_label_by_title(state, "type::bug")
    for issue in state["issues"]:
        if (issue["status"] == "open"
                and bug_label["id"] in issue["labels"]
                and issue.get("iterationId") is None):
            issue["iterationId"] = iter_id
            issue["updatedAt"] = NOW


def solve_task_h74(state):
    """Reassign Chen Wei's non-v4.0 open issues to Alex Thompson."""
    chen = find_user_by_name(state, "Chen Wei")
    alex = find_user_by_name(state, "Alex Thompson")
    ms_v40 = find_milestone_by_title(state, "v4.0 - Platform Redesign")
    for issue in state["issues"]:
        if (issue["status"] == "open"
                and chen["id"] in issue["assignees"]
                and issue["milestoneId"] != ms_v40["id"]):
            issue["assignees"] = [a for a in issue["assignees"] if a != chen["id"]]
            if alex["id"] not in issue["assignees"]:
                issue["assignees"].append(alex["id"])
            issue["updatedAt"] = NOW


def solve_task_h75(state):
    """Create 'Initial planning for ...' issues in empty epics, assigned to Priya Patel."""
    priya = find_user_by_name(state, "Priya Patel")
    task_label = find_label_by_title(state, "type::task")
    # Find open epics with no issues
    epic_ids_with_issues = {i["epicId"] for i in state["issues"] if i.get("epicId")}
    empty_epics = [e for e in state["epics"]
                   if e["status"] == "open" and e["id"] not in epic_ids_with_issues]
    for epic in empty_epics:
        iid = next_issue_id(state)
        state["issues"].append({
            "id": f"issue_{iid}",
            "iid": iid,
            "title": f"Initial planning for {epic['title']}",
            "description": "",
            "status": "open",
            "assignees": [priya["id"]],
            "labels": [task_label["id"]],
            "milestoneId": None,
            "iterationId": None,
            "epicId": epic["id"],
            "weight": None,
            "dueDate": None,
            "startDate": None,
            "healthStatus": None,
            "timeEstimate": 0,
            "timeSpent": 0,
            "confidential": False,
            "authorId": state["currentUser"]["id"],
            "createdAt": NOW,
            "updatedAt": NOW,
            "closedAt": None,
            "taskIds": [],
            "linkedIssueIds": [],
        })


def solve_task_h76(state):
    """Make Documentation Overhaul child of Platform Redesign; add priority::high to its issues; set health at_risk."""
    platform_epic = find_epic_by_title(state, "Platform Redesign")
    doc_epic = find_epic_by_title(state, "Documentation Overhaul")
    doc_epic["parentEpicId"] = platform_epic["id"]
    doc_epic["healthStatus"] = "at_risk"
    doc_epic["updatedAt"] = NOW
    lbl_high = find_label_by_title(state, "priority::high")
    priority_ids = {l["id"] for l in state["labels"] if l["title"].startswith("priority::")}
    for issue in state["issues"]:
        if issue["epicId"] == doc_epic["id"]:
            issue["labels"] = [l for l in issue["labels"] if l not in priority_ids]
            if lbl_high["id"] not in issue["labels"]:
                issue["labels"].append(lbl_high["id"])
            issue["updatedAt"] = NOW


def solve_task_h77(state):
    """Rename 'UX' to 'user-experience', change type to 'group', apply to Frontend Modernization issues."""
    ux_label = find_label_by_title(state, "UX")
    ux_label["title"] = "user-experience"
    ux_label["type"] = "group"
    fe_epic = find_epic_by_title(state, "Frontend Modernization")
    for issue in state["issues"]:
        if issue["epicId"] == fe_epic["id"] and issue["status"] == "open":
            if ux_label["id"] not in issue["labels"]:
                issue["labels"].append(ux_label["id"])
                issue["updatedAt"] = NOW


def solve_task_h78(state):
    """Create 'Tech Debt Sprint' milestone; move open technical-debt issues; set health needs_attention."""
    mid = next_milestone_id(state)
    ms_id = f"ms_{mid}"
    state["milestones"].append({
        "id": ms_id,
        "title": "Tech Debt Sprint",
        "description": "",
        "startDate": "2026-03-17",
        "dueDate": "2026-03-28",
        "status": "active",
        "createdAt": NOW,
    })
    td_label = find_label_by_title(state, "technical-debt")
    for issue in state["issues"]:
        if issue["status"] == "open" and td_label["id"] in issue["labels"]:
            issue["milestoneId"] = ms_id
            issue["healthStatus"] = "needs_attention"
            issue["updatedAt"] = NOW


def solve_task_h79(state):
    """Set time estimate 24h on Frontend Modernization issues; set epic health to at_risk."""
    fe_epic = find_epic_by_title(state, "Frontend Modernization")
    fe_epic["healthStatus"] = "at_risk"
    fe_epic["updatedAt"] = NOW
    for issue in state["issues"]:
        if issue["epicId"] == fe_epic["id"] and issue["status"] == "open":
            issue["timeEstimate"] = 86400
            issue["updatedAt"] = NOW


def solve_task_h80(state):
    """Set health needs_attention and add needs-discussion to top 2 time-spent issues."""
    nd_label = find_label_by_title(state, "needs-discussion")
    # The two open issues with most time spent: Dark mode (57600) and GraphQL gateway (43200)
    for title in [
        "Add dark mode support for the entire application",
        "Implement GraphQL gateway for v3 API",
    ]:
        issue = find_issue_by_title(state, title)
        issue["healthStatus"] = "needs_attention"
        if nd_label["id"] not in issue["labels"]:
            issue["labels"].append(nd_label["id"])
        issue["updatedAt"] = NOW


def solve_task_h81(state):
    """Create 'status::blocked' label and issue 'Resolve CDN provider outage'."""
    lid = next_label_id(state)
    label_id = f"lbl_{lid}"
    state["labels"].append({
        "id": label_id,
        "title": "status::blocked",
        "description": "",
        "color": "#b60205",
        "textColor": "#fff",
        "type": "project",
        "scoped": True,
    })
    luca = find_user_by_name(state, "Luca Rossi")
    ms = find_milestone_by_title(state, "v4.1 - Performance")
    iid = next_issue_id(state)
    state["issues"].append({
        "id": f"issue_{iid}",
        "iid": iid,
        "title": "Resolve CDN provider outage",
        "description": "",
        "status": "open",
        "assignees": [luca["id"]],
        "labels": [label_id],
        "milestoneId": ms["id"],
        "iterationId": None,
        "epicId": None,
        "weight": 5,
        "dueDate": None,
        "startDate": None,
        "healthStatus": None,
        "timeEstimate": 0,
        "timeSpent": 0,
        "confidential": False,
        "authorId": state["currentUser"]["id"],
        "createdAt": NOW,
        "updatedAt": NOW,
        "closedAt": None,
        "taskIds": [],
        "linkedIssueIds": [],
    })


def solve_task_h82(state):
    """Assign Chen Wei to unassigned CSRF issue, add priority::high, move to Sprint 27."""
    issue = find_issue_by_title(state, "Implement CSRF token rotation")
    chen_wei = find_user_by_name(state, "Chen Wei")
    issue["assignees"].append(chen_wei["id"])
    high_label = find_label_by_title(state, "priority::high")
    # Remove existing priority:: labels (scoped replacement)
    priority_ids = {l["id"] for l in state["labels"] if l["title"].startswith("priority::")}
    issue["labels"] = [l for l in issue["labels"] if l not in priority_ids]
    issue["labels"].append(high_label["id"])
    sprint27 = find_iteration_by_title(state, "Sprint 27")
    issue["iterationId"] = sprint27["id"]
    issue["updatedAt"] = NOW


def solve_task_h83(state):
    """Move Database Optimization issues from Sprint 26 to Sprint 27."""
    db_epic = find_epic_by_title(state, "Database Optimization")
    sprint26 = find_iteration_by_title(state, "Sprint 26")
    sprint27 = find_iteration_by_title(state, "Sprint 27")
    for issue in state["issues"]:
        if (
            issue["epicId"] == db_epic["id"]
            and issue["status"] == "open"
            and issue["iterationId"] == sprint26["id"]
        ):
            issue["iterationId"] = sprint27["id"]
            issue["updatedAt"] = NOW


def solve_task_h84(state):
    """Log 3h on slow queries issue; set weight 8 on keyset pagination issue."""
    slow_issue = find_issue_by_title(state, "Analyze and optimize slow queries from APM logs")
    tl_id = state.get("_nextTimelogId", 30)
    state["_nextTimelogId"] = tl_id + 1
    state["timelogs"].append({
        "id": f"tl_{tl_id}",
        "issueId": slow_issue["id"],
        "userId": state["currentUser"]["id"],
        "timeSpent": 10800,
        "summary": "Index optimization review",
        "spentAt": NOW,
    })
    slow_issue["timeSpent"] = slow_issue.get("timeSpent", 0) + 10800
    slow_issue["updatedAt"] = NOW

    keyset_issue = find_issue_by_title(state, "Optimize issue list query to use keyset pagination")
    keyset_issue["weight"] = 8
    keyset_issue["updatedAt"] = NOW


def solve_task_h85(state):
    """Close Q1 2026 Planning milestone; move its issues to v4.1 Performance."""
    q1_ms = find_milestone_by_title(state, "Q1 2026 Planning")
    q1_ms["status"] = "closed"
    perf_ms = find_milestone_by_title(state, "v4.1 - Performance")
    for issue in state["issues"]:
        if issue["milestoneId"] == q1_ms["id"] and issue["status"] == "open":
            issue["milestoneId"] = perf_ms["id"]
            issue["updatedAt"] = NOW


def solve_task_h86(state):
    """Create 'Release 4.0 GA' iteration in Release Cycle; assign CSP + vulnerable deps."""
    rc_cadence = find_cadence_by_title(state, "Release Cycle")
    iid = next_iteration_id(state)
    iter_id = f"iter_{iid}"
    state["iterations"].append({
        "id": iter_id,
        "title": "Release 4.0 GA",
        "cadenceId": rc_cadence["id"],
        "startDate": "2026-03-01",
        "dueDate": "2026-03-15",
        "status": "upcoming",
        "createdAt": NOW,
    })
    for title in [
        "Implement Content Security Policy headers",
        "Upgrade vulnerable dependencies identified in audit",
    ]:
        issue = find_issue_by_title(state, title)
        issue["iterationId"] = iter_id
        issue["updatedAt"] = NOW


def solve_task_h87(state):
    """Add needs-discussion to all open issues with both type::bug and priority::high."""
    bug_label = find_label_by_title(state, "type::bug")
    high_label = find_label_by_title(state, "priority::high")
    nd_label = find_label_by_title(state, "needs-discussion")
    for issue in state["issues"]:
        if (
            issue["status"] == "open"
            and bug_label["id"] in issue["labels"]
            and high_label["id"] in issue["labels"]
        ):
            if nd_label["id"] not in issue["labels"]:
                issue["labels"].append(nd_label["id"])
                issue["updatedAt"] = NOW


def solve_task_h88(state):
    """Create 'Developer Tooling' epic; add keyboard shortcuts and bulk operations issues."""
    feat_label = find_label_by_title(state, "type::feature")
    iid = next_epic_iid(state)
    epic_id = f"epic_{iid}"
    state["epics"].append({
        "id": epic_id,
        "iid": iid,
        "title": "Developer Tooling",
        "description": "Tools and utilities to improve developer productivity",
        "status": "open",
        "startDate": None,
        "dueDate": None,
        "labels": [feat_label["id"]],
        "healthStatus": None,
        "authorId": state["currentUser"]["id"],
        "confidential": False,
        "parentEpicId": None,
        "createdAt": NOW,
        "updatedAt": NOW,
    })
    for title in [
        "Implement keyboard shortcuts for common actions",
        "Add bulk operations for issue management",
    ]:
        issue = find_issue_by_title(state, title)
        issue["epicId"] = epic_id
        issue["updatedAt"] = NOW


def solve_task_h89(state):
    """Restore snoozed GraphQL gateway todo; add 2h timelog."""
    gql_issue = find_issue_by_title(state, "Implement GraphQL gateway for v3 API")
    # Find the snoozed todo for this issue
    for todo in state["todos"]:
        if todo["targetId"] == gql_issue["id"] and todo["action"] == "review_requested":
            todo["status"] = "pending"
            todo["snoozedUntil"] = None
            break
    # Add timelog
    tl_id = state.get("_nextTimelogId", 30)
    state["_nextTimelogId"] = tl_id + 1
    state["timelogs"].append({
        "id": f"tl_{tl_id}",
        "issueId": gql_issue["id"],
        "userId": state["currentUser"]["id"],
        "timeSpent": 7200,
        "summary": "Schema optimization review",
        "spentAt": NOW,
    })
    gql_issue["timeSpent"] = gql_issue.get("timeSpent", 0) + 7200
    gql_issue["updatedAt"] = NOW


def solve_task_h90(state):
    """Rename 'blocked' to 'on-hold', change color, update description, apply to CSRF issue."""
    blocked_label = find_label_by_title(state, "blocked")
    blocked_label["title"] = "on-hold"
    blocked_label["color"] = "#e67e22"
    blocked_label["description"] = "Temporarily paused pending external input"
    csrf_issue = find_issue_by_title(state, "Implement CSRF token rotation")
    if blocked_label["id"] not in csrf_issue["labels"]:
        csrf_issue["labels"].append(blocked_label["id"])
        csrf_issue["updatedAt"] = NOW


def solve_task_h91(state):
    """Move Caching Layer epic under Platform Redesign; set issues health needs_attention."""
    caching_epic = find_epic_by_title(state, "Caching Layer Implementation")
    platform_epic = find_epic_by_title(state, "Platform Redesign")
    caching_epic["parentEpicId"] = platform_epic["id"]
    caching_epic["updatedAt"] = NOW
    for issue in state["issues"]:
        if issue["epicId"] == caching_epic["id"] and issue["status"] == "open":
            issue["healthStatus"] = "needs_attention"
            issue["updatedAt"] = NOW


def solve_task_h92(state):
    """Log 8h on user settings migration; set health at_risk, weight 13."""
    issue = find_issue_by_title(state, "Migrate user settings page to React")
    tl_id = state.get("_nextTimelogId", 30)
    state["_nextTimelogId"] = tl_id + 1
    state["timelogs"].append({
        "id": f"tl_{tl_id}",
        "issueId": issue["id"],
        "userId": state["currentUser"]["id"],
        "timeSpent": 28800,
        "summary": "Form validation and API integration testing",
        "spentAt": NOW,
    })
    issue["timeSpent"] = issue.get("timeSpent", 0) + 28800
    issue["healthStatus"] = "at_risk"
    issue["weight"] = 13
    issue["updatedAt"] = NOW


def solve_task_h93(state):
    """Delete Bug Triage board; create Severity Board with priority::critical and priority::high."""
    state["boards"] = [b for b in state["boards"] if b["name"] != "Bug Triage"]
    crit_label = find_label_by_title(state, "priority::critical")
    high_label = find_label_by_title(state, "priority::high")
    bid = next_board_id(state)
    state["boards"].append({
        "id": f"board_{bid}",
        "name": "Severity Board",
        "lists": [
            {"id": f"list_{bid}_1", "type": "label", "labelId": crit_label["id"], "position": 0},
            {"id": f"list_{bid}_2", "type": "label", "labelId": high_label["id"], "position": 1},
        ],
    })


def solve_task_h94(state):
    """Set health needs_attention and start date on Enterprise SSO epic."""
    epic = find_epic_by_title(state, "Enterprise SSO Integration")
    epic["healthStatus"] = "needs_attention"
    epic["startDate"] = "2026-03-15"
    epic["updatedAt"] = NOW


def solve_task_h95(state):
    """Add 'blocked' label to the two heaviest issues in Sprint 26 (weight 13)."""
    blocked_label = find_label_by_title(state, "blocked")
    for title in [
        "Implement GraphQL gateway for v3 API",
        "Add dark mode support for the entire application",
    ]:
        issue = find_issue_by_title(state, title)
        if blocked_label["id"] not in issue["labels"]:
            issue["labels"].append(blocked_label["id"])
        issue["updatedAt"] = NOW


def solve_task_h96(state):
    """Create Hotfix 4.0.1 milestone + Hotfix Sprint iteration; assign 2 issues to both."""
    mid = next_milestone_id(state)
    ms_id = f"ms_{mid}"
    state["milestones"].append({
        "id": ms_id,
        "title": "Hotfix 4.0.1",
        "description": "",
        "startDate": "2026-03-03",
        "dueDate": "2026-03-10",
        "status": "active",
        "createdAt": NOW,
    })
    sprint_cad = find_cadence_by_title(state, "Sprint Cadence")
    iid = next_iteration_id(state)
    iter_id = f"iter_{iid}"
    state["iterations"].append({
        "id": iter_id,
        "title": "Hotfix Sprint",
        "cadenceId": sprint_cad["id"],
        "startDate": "2026-03-03",
        "dueDate": "2026-03-10",
        "status": "upcoming",
        "createdAt": NOW,
    })
    for title in [
        "Login page shows blank screen on Safari 17.2",
        "Email notifications sent with wrong timezone offset",
    ]:
        issue = find_issue_by_title(state, title)
        issue["milestoneId"] = ms_id
        issue["iterationId"] = iter_id
        issue["updatedAt"] = NOW


def solve_task_h97(state):
    """Replace component::api with component::backend on API v3 Migration issues."""
    api_epic = find_epic_by_title(state, "API v3 Migration")
    api_label = find_label_by_title(state, "component::api")
    backend_label = find_label_by_title(state, "component::backend")
    component_ids = {l["id"] for l in state["labels"] if l["title"].startswith("component::")}
    for issue in state["issues"]:
        if issue["epicId"] == api_epic["id"] and issue["status"] == "open":
            if api_label["id"] in issue["labels"]:
                # Remove all component:: labels (scoped replacement)
                issue["labels"] = [l for l in issue["labels"] if l not in component_ids]
                issue["labels"].append(backend_label["id"])
                issue["updatedAt"] = NOW


def solve_task_h98(state):
    """Move 2FA and JWT issues to v4.2 Security Hardening; add priority::high."""
    sec_ms = find_milestone_by_title(state, "v4.2 - Security Hardening")
    high_label = find_label_by_title(state, "priority::high")
    priority_ids = {l["id"] for l in state["labels"] if l["title"].startswith("priority::")}
    for title in [
        "Implement two-factor authentication with TOTP",
        "Migrate user authentication from sessions to JWT",
    ]:
        issue = find_issue_by_title(state, title)
        issue["milestoneId"] = sec_ms["id"]
        issue["labels"] = [l for l in issue["labels"] if l not in priority_ids]
        if high_label["id"] not in issue["labels"]:
            issue["labels"].append(high_label["id"])
        issue["updatedAt"] = NOW


def solve_task_h99(state):
    """Update Release Cycle cadence to automatic; create Release 4.1 Alpha iteration."""
    rc_cad = find_cadence_by_title(state, "Release Cycle")
    rc_cad["automatic"] = True
    rc_cad["durationWeeks"] = 4
    rc_cad["upcomingIterations"] = 2
    iid = next_iteration_id(state)
    state["iterations"].append({
        "id": f"iter_{iid}",
        "title": "Release 4.1 Alpha",
        "cadenceId": rc_cad["id"],
        "startDate": "2026-03-15",
        "dueDate": "2026-04-11",
        "status": "upcoming",
        "createdAt": NOW,
    })


def solve_task_h100(state):
    """Create 'in-review' label, Review Board, and apply label to 2 issues."""
    lid = next_label_id(state)
    label_id = f"lbl_{lid}"
    state["labels"].append({
        "id": label_id,
        "title": "in-review",
        "description": "",
        "color": "#7b68ee",
        "textColor": "#fff",
        "type": "project",
        "scoped": False,
    })
    bid = next_board_id(state)
    state["boards"].append({
        "id": f"board_{bid}",
        "name": "Review Board",
        "lists": [
            {"id": f"list_{bid}_1", "type": "label", "labelId": label_id, "position": 0},
        ],
    })
    for title in [
        "Implement GraphQL gateway for v3 API",
        "Add dark mode support for the entire application",
    ]:
        issue = find_issue_by_title(state, title)
        if label_id not in issue["labels"]:
            issue["labels"].append(label_id)
        issue["updatedAt"] = NOW


# ── Solver registry ──────────────────────────────────────────────────

SOLVERS = {
    "task_e1": solve_task_e1,
    "task_e2": solve_task_e2,
    "task_e3": solve_task_e3,
    "task_e4": solve_task_e4,
    "task_e5": solve_task_e5,
    "task_e6": solve_task_e6,
    "task_e7": solve_task_e7,
    "task_e8": solve_task_e8,
    "task_e9": solve_task_e9,
    "task_e10": solve_task_e10,
    "task_e11": solve_task_e11,
    "task_e12": solve_task_e12,
    "task_e13": solve_task_e13,
    "task_e14": solve_task_e14,
    "task_e15": solve_task_e15,
    "task_e16": solve_task_e16,
    "task_e17": solve_task_e17,
    "task_e18": solve_task_e18,
    "task_e19": solve_task_e19,
    "task_e20": solve_task_e20,
    "task_m1": solve_task_m1,
    "task_m2": solve_task_m2,
    "task_m3": solve_task_m3,
    "task_m4": solve_task_m4,
    "task_m5": solve_task_m5,
    "task_m6": solve_task_m6,
    "task_m7": solve_task_m7,
    "task_m8": solve_task_m8,
    "task_m9": solve_task_m9,
    "task_m10": solve_task_m10,
    "task_m11": solve_task_m11,
    "task_m12": solve_task_m12,
    "task_m13": solve_task_m13,
    "task_m14": solve_task_m14,
    "task_m15": solve_task_m15,
    "task_m16": solve_task_m16,
    "task_m17": solve_task_m17,
    "task_m18": solve_task_m18,
    "task_m19": solve_task_m19,
    "task_m20": solve_task_m20,
    "task_h1": solve_task_h1,
    "task_h2": solve_task_h2,
    "task_h3": solve_task_h3,
    "task_h4": solve_task_h4,
    "task_h5": solve_task_h5,
    "task_h6": solve_task_h6,
    "task_h7": solve_task_h7,
    "task_h8": solve_task_h8,
    "task_h9": solve_task_h9,
    "task_h10": solve_task_h10,
    "task_h11": solve_task_h11,
    "task_h12": solve_task_h12,
    "task_h13": solve_task_h13,
    "task_h14": solve_task_h14,
    "task_h15": solve_task_h15,
    "task_h16": solve_task_h16,
    "task_h17": solve_task_h17,
    "task_h18": solve_task_h18,
    "task_h19": solve_task_h19,
    "task_h20": solve_task_h20,
    "task_h21": solve_task_h21,
    "task_h22": solve_task_h22,
    "task_h23": solve_task_h23,
    "task_h24": solve_task_h24,
    "task_h25": solve_task_h25,
    "task_h26": solve_task_h26,
    "task_h27": solve_task_h27,
    "task_h28": solve_task_h28,
    "task_h29": solve_task_h29,
    "task_h30": solve_task_h30,
    "task_h31": solve_task_h31,
    "task_h32": solve_task_h32,
    "task_h33": solve_task_h33,
    "task_h34": solve_task_h34,
    "task_h35": solve_task_h35,
    "task_h36": solve_task_h36,
    "task_h37": solve_task_h37,
    "task_h38": solve_task_h38,
    "task_h39": solve_task_h39,
    "task_h40": solve_task_h40,
    "task_h41": solve_task_h41,
    "task_h42": solve_task_h42,
    "task_h43": solve_task_h43,
    "task_h44": solve_task_h44,
    "task_h45": solve_task_h45,
    "task_h46": solve_task_h46,
    "task_h47": solve_task_h47,
    "task_h48": solve_task_h48,
    "task_h49": solve_task_h49,
    "task_h50": solve_task_h50,
    "task_h51": solve_task_h51,
    "task_h52": solve_task_h52,
    "task_h53": solve_task_h53,
    "task_h54": solve_task_h54,
    "task_h55": solve_task_h55,
    "task_h56": solve_task_h56,
    "task_h57": solve_task_h57,
    "task_h58": solve_task_h58,
    "task_h59": solve_task_h59,
    "task_h60": solve_task_h60,
    "task_h61": solve_task_h61,
    "task_h62": solve_task_h62,
    "task_h63": solve_task_h63,
    "task_h64": solve_task_h64,
    "task_h65": solve_task_h65,
    "task_h66": solve_task_h66,
    "task_h67": solve_task_h67,
    "task_h68": solve_task_h68,
    "task_h69": solve_task_h69,
    "task_h70": solve_task_h70,
    "task_h71": solve_task_h71,
    "task_h72": solve_task_h72,
    "task_h73": solve_task_h73,
    "task_h74": solve_task_h74,
    "task_h75": solve_task_h75,
    "task_h76": solve_task_h76,
    "task_h77": solve_task_h77,
    "task_h78": solve_task_h78,
    "task_h79": solve_task_h79,
    "task_h80": solve_task_h80,
    "task_h81": solve_task_h81,
    "task_h82": solve_task_h82,
    "task_h83": solve_task_h83,
    "task_h84": solve_task_h84,
    "task_h85": solve_task_h85,
    "task_h86": solve_task_h86,
    "task_h87": solve_task_h87,
    "task_h88": solve_task_h88,
    "task_h89": solve_task_h89,
    "task_h90": solve_task_h90,
    "task_h91": solve_task_h91,
    "task_h92": solve_task_h92,
    "task_h93": solve_task_h93,
    "task_h94": solve_task_h94,
    "task_h95": solve_task_h95,
    "task_h96": solve_task_h96,
    "task_h97": solve_task_h97,
    "task_h98": solve_task_h98,
    "task_h99": solve_task_h99,
    "task_h100": solve_task_h100,
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


def find_free_port(start=9500):
    """Find a free port starting from `start`."""
    port = start
    while port < start + 200:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("", port))
                return port
            except OSError:
                port += 1
    raise RuntimeError(f"No free port found in range {start}-{start+200}")


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
    """Load task definitions from tasks.json."""
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
    parser = argparse.ArgumentParser(description="GitLab Plan & Track real-task sanity check")
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
