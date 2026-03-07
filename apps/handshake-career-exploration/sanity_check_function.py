#!/usr/bin/env python3
"""
Sanity check for Handshake Career Exploration function-test tasks.

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
    employers: JSON.parse(JSON.stringify(EMPLOYERS)),
    jobs: JSON.parse(JSON.stringify(JOBS)),
    feedPosts: JSON.parse(JSON.stringify(FEED_POSTS)),
    events: JSON.parse(JSON.stringify(EVENTS)),
    appointments: JSON.parse(JSON.stringify(APPOINTMENTS)),
    appointmentCategories: JSON.parse(JSON.stringify(APPOINTMENT_CATEGORIES)),
    appointmentStaff: JSON.parse(JSON.stringify(APPOINTMENT_STAFF)),
    availableSlots: JSON.parse(JSON.stringify(AVAILABLE_APPOINTMENT_SLOTS)),
    qaQuestions: JSON.parse(JSON.stringify(QA_QUESTIONS)),
    messages: JSON.parse(JSON.stringify(MESSAGES)),
    schoolLabels: [...SCHOOL_LABELS],
    _nextPostId: 100,
    _nextCommentId: 100,
    _nextAppointmentId: 100,
    _nextQuestionId: 100,
    _nextAnswerId: 100,
};
process.stdout.write(JSON.stringify(state));
"""


# -- helpers ------------------------------------------------------------------

def find_entity(entities, **kwargs):
    """Find an entity by attribute match. Raises if not found."""
    for e in entities:
        if all(e.get(k) == v for k, v in kwargs.items()):
            return e
    raise ValueError(f"Entity not found: {kwargs}")


def find_post(state, post_id):
    return find_entity(state["feedPosts"], id=post_id)


def find_event(state, event_id):
    return find_entity(state["events"], id=event_id)


def find_message(state, message_id):
    return find_entity(state["messages"], id=message_id)


def find_appointment(state, appt_id):
    return find_entity(state["appointments"], id=appt_id)


def find_question(state, question_id):
    return find_entity(state["qaQuestions"], id=question_id)


def find_employer(state, employer_id):
    return find_entity(state["employers"], id=employer_id)


# -- solve functions ----------------------------------------------------------

def solve_task_1(state):
    """Create a post with PM interview prep content."""
    post_id = "post_" + str(state["_nextPostId"])
    state["_nextPostId"] += 1
    state["feedPosts"].insert(0, {
        "id": post_id,
        "authorType": "student",
        "authorId": state["currentUser"]["id"],
        "authorName": state["currentUser"]["fullName"],
        "authorSchool": state["currentUser"]["school"],
        "authorAvatarColor": state["currentUser"]["avatarColor"],
        "content": "Looking for advice on product management interview prep! Any tips appreciated.",
        "audience": "everyone",
        "likes": 0,
        "comments": [],
        "hasImage": False,
        "hasVideo": False,
        "createdAt": "2026-03-07T12:00:00Z",
        "bookmarked": False,
    })


def solve_task_2(state):
    """Like Kevin O'Brien's FAANG prep post (post_08, likes=534)."""
    post = find_post(state, "post_08")
    post["likes"] = 535


def solve_task_3(state):
    """Bookmark Aisha Mohammed's NSBE post (post_06)."""
    post = find_post(state, "post_06")
    post["bookmarked"] = True
    if "post_06" not in state["currentUser"]["savedPostIds"]:
        state["currentUser"]["savedPostIds"].append("post_06")


def solve_task_4(state):
    """Remove bookmark from Jessica Park's Meta post (post_02)."""
    post = find_post(state, "post_02")
    post["bookmarked"] = False
    state["currentUser"]["savedPostIds"] = [
        pid for pid in state["currentUser"]["savedPostIds"] if pid != "post_02"
    ]


def solve_task_5(state):
    """Add comment to Google post (post_01)."""
    post = find_post(state, "post_01")
    comment_id = "cmt_" + str(state["_nextCommentId"])
    state["_nextCommentId"] += 1
    post["comments"].append({
        "id": comment_id,
        "authorName": state["currentUser"]["fullName"],
        "authorSchool": state["currentUser"]["school"],
        "authorAvatarColor": state["currentUser"]["avatarColor"],
        "text": "Great tips, thanks for sharing!",
        "createdAt": "2026-03-07T12:00:00Z",
        "isAnonymous": False,
    })


def solve_task_6(state):
    """Add anonymous comment to McKinsey post (post_09)."""
    post = find_post(state, "post_09")
    comment_id = "cmt_" + str(state["_nextCommentId"])
    state["_nextCommentId"] += 1
    post["comments"].append({
        "id": comment_id,
        "authorName": "Anonymous Student",
        "authorSchool": state["currentUser"]["school"],
        "authorAvatarColor": "#95A5A6",
        "text": "How selective is the application process?",
        "createdAt": "2026-03-07T12:00:00Z",
        "isAnonymous": True,
    })


def solve_task_7(state):
    """Create post with school audience about system design study group."""
    post_id = "post_" + str(state["_nextPostId"])
    state["_nextPostId"] += 1
    state["feedPosts"].insert(0, {
        "id": post_id,
        "authorType": "student",
        "authorId": state["currentUser"]["id"],
        "authorName": state["currentUser"]["fullName"],
        "authorSchool": state["currentUser"]["school"],
        "authorAvatarColor": state["currentUser"]["avatarColor"],
        "content": "Anyone interested in forming a study group for system design?",
        "audience": "school",
        "likes": 0,
        "comments": [],
        "hasImage": False,
        "hasVideo": False,
        "createdAt": "2026-03-07T12:00:00Z",
        "bookmarked": False,
    })


def solve_task_8(state):
    """Follow Amazon (emp_09)."""
    user = state["currentUser"]
    if "emp_09" not in user["followedEmployerIds"]:
        user["followedEmployerIds"].append("emp_09")
    emp = find_employer(state, "emp_09")
    emp["followCount"] = emp["followCount"] + 1


def solve_task_9(state):
    """Unfollow Google (emp_01)."""
    user = state["currentUser"]
    user["followedEmployerIds"] = [
        eid for eid in user["followedEmployerIds"] if eid != "emp_01"
    ]
    emp = find_employer(state, "emp_01")
    emp["followCount"] = emp["followCount"] - 1


def solve_task_10(state):
    """Follow JPMorgan Chase (emp_02)."""
    user = state["currentUser"]
    if "emp_02" not in user["followedEmployerIds"]:
        user["followedEmployerIds"].append("emp_02")
    emp = find_employer(state, "emp_02")
    emp["followCount"] = emp["followCount"] + 1


def solve_task_11(state):
    """Follow Deloitte (emp_08)."""
    user = state["currentUser"]
    if "emp_08" not in user["followedEmployerIds"]:
        user["followedEmployerIds"].append("emp_08")
    emp = find_employer(state, "emp_08")
    emp["followCount"] = emp["followCount"] + 1


def solve_task_12(state):
    """Save Google SWE Intern job (job_01)."""
    user = state["currentUser"]
    if "job_01" not in user["savedJobIds"]:
        user["savedJobIds"].append("job_01")


def solve_task_13(state):
    """Unsave JPMorgan IB Summer Analyst (job_03)."""
    user = state["currentUser"]
    user["savedJobIds"] = [jid for jid in user["savedJobIds"] if jid != "job_03"]


def solve_task_14(state):
    """Save Startup Grind Labs Full-Stack Engineer (job_21)."""
    user = state["currentUser"]
    if "job_21" not in user["savedJobIds"]:
        user["savedJobIds"].append("job_21")


def solve_task_15(state):
    """Save Epic Systems Technical Solutions Engineer (job_16)."""
    user = state["currentUser"]
    if "job_16" not in user["savedJobIds"]:
        user["savedJobIds"].append("job_16")


def solve_task_16(state):
    """RSVP to Stanford Spring Career Fair (evt_03)."""
    evt = find_event(state, "evt_03")
    evt["rsvped"] = True
    evt["rsvpCount"] = evt["rsvpCount"] + 1


def solve_task_17(state):
    """RSVP to AI/ML Careers at Meta (evt_02)."""
    evt = find_event(state, "evt_02")
    evt["rsvped"] = True
    evt["rsvpCount"] = evt["rsvpCount"] + 1


def solve_task_18(state):
    """RSVP to Resume Workshop (evt_05)."""
    evt = find_event(state, "evt_05")
    evt["rsvped"] = True
    evt["rsvpCount"] = evt["rsvpCount"] + 1


def solve_task_19(state):
    """RSVP to Anthropic Research Talk (evt_06)."""
    evt = find_event(state, "evt_06")
    evt["rsvped"] = True
    evt["rsvpCount"] = evt["rsvpCount"] + 1


def solve_task_20(state):
    """Mark Google message (msg_01) as read."""
    msg = find_message(state, "msg_01")
    msg["isRead"] = True


def solve_task_21(state):
    """Mark all messages as read."""
    for msg in state["messages"]:
        msg["isRead"] = True


def solve_task_22(state):
    """Mark Stripe message (msg_06) as read."""
    msg = find_message(state, "msg_06")
    msg["isRead"] = True


def solve_task_23(state):
    """Schedule Career Counseling / General Career Advising appointment."""
    appt_id = "appt_" + str(state["_nextAppointmentId"]).zfill(2)
    state["_nextAppointmentId"] += 1
    state["appointments"].append({
        "id": appt_id,
        "category": "Career Counseling",
        "type": "General Career Advising",
        "staffId": None,
        "staffName": None,
        "date": "2026-03-10",
        "time": "9:00 AM",
        "duration": 30,
        "medium": "In Person",
        "location": "Career Center",
        "status": "requested",
        "details": "Need guidance on choosing between tech and consulting career paths.",
        "comments": [],
        "createdAt": "2026-03-07T12:00:00Z",
    })


def solve_task_24(state):
    """Cancel Mock Interview - Technical appointment (appt_02)."""
    appt = find_appointment(state, "appt_02")
    appt["status"] = "cancelled"


def solve_task_25(state):
    """Cancel Case Interview Prep appointment (appt_08)."""
    appt = find_appointment(state, "appt_08")
    appt["status"] = "cancelled"


def solve_task_26(state):
    """Add comment about cover letter to Resume Review appointment (appt_01)."""
    appt = find_appointment(state, "appt_01")
    appt["comments"].append({
        "author": state["currentUser"]["fullName"],
        "text": "Could we also review my cover letter during our session?",
        "createdAt": "2026-03-07T12:00:00Z",
    })


def solve_task_27(state):
    """Schedule Interview Preparation / Mock Interview - Behavioral with David Kim."""
    appt_id = "appt_" + str(state["_nextAppointmentId"]).zfill(2)
    state["_nextAppointmentId"] += 1
    state["appointments"].append({
        "id": appt_id,
        "category": "Interview Preparation",
        "type": "Mock Interview - Behavioral",
        "staffId": "staff_04",
        "staffName": "David Kim",
        "date": "2026-03-11",
        "time": "10:00 AM",
        "duration": 30,
        "medium": "Virtual on Handshake",
        "location": None,
        "status": "requested",
        "details": "Preparing for Amazon behavioral interviews.",
        "comments": [],
        "createdAt": "2026-03-07T12:00:00Z",
    })


def solve_task_28(state):
    """Submit question about best tech companies for new grads."""
    q_id = "qa_" + str(state["_nextQuestionId"]).zfill(2)
    state["_nextQuestionId"] += 1
    state["qaQuestions"].insert(0, {
        "id": q_id,
        "authorName": "Maya Chen",
        "authorSchool": state["currentUser"]["school"],
        "authorMajor": state["currentUser"]["major"],
        "authorGradYear": state["currentUser"]["graduationYear"],
        "authorAvatarColor": state["currentUser"]["avatarColor"],
        "question": "What are the best tech companies for new grad software engineers in 2026?",
        "status": "pending",
        "createdAt": "2026-03-07T12:00:00Z",
        "views": 0,
        "answers": [],
    })


def solve_task_29(state):
    """Submit fully visible answer to qa_10 (finance internship timeline)."""
    q = find_question(state, "qa_10")
    ans_id = "ans_" + str(state["_nextAnswerId"]).zfill(2)
    state["_nextAnswerId"] += 1
    q["answers"].append({
        "id": ans_id,
        "authorName": "Maya Chen",
        "authorSchool": state["currentUser"]["school"],
        "authorMajor": state["currentUser"]["major"],
        "authorGradYear": state["currentUser"]["graduationYear"],
        "authorAvatarColor": state["currentUser"]["avatarColor"],
        "text": "Most bulge bracket banks start recruiting in August-September of the previous year. Start networking early!",
        "visibility": "full",
        "status": "pending",
        "createdAt": "2026-03-07T12:00:00Z",
        "helpful": 0,
    })


def solve_task_30(state):
    """Submit semi-anonymous answer to qa_06 (system design resources)."""
    q = find_question(state, "qa_06")
    ans_id = "ans_" + str(state["_nextAnswerId"]).zfill(2)
    state["_nextAnswerId"] += 1
    q["answers"].append({
        "id": ans_id,
        "authorName": "Anonymous",
        "authorSchool": state["currentUser"]["school"],
        "authorMajor": state["currentUser"]["major"],
        "authorGradYear": state["currentUser"]["graduationYear"],
        "authorAvatarColor": "#95A5A6",
        "text": "I also recommend watching mock system design interviews on YouTube. Seeing others think through problems helps a lot.",
        "visibility": "semi-anonymous",
        "status": "pending",
        "createdAt": "2026-03-07T12:00:00Z",
        "helpful": 0,
    })


def solve_task_31(state):
    """Mark Jordan Taylor's salary negotiation answer (ans_07) as helpful."""
    q = find_question(state, "qa_05")
    ans = find_entity(q["answers"], id="ans_07")
    ans["helpful"] = ans["helpful"] + 1


def solve_task_32(state):
    """Mark Tyler Wong's Google interview answer (ans_01) as helpful."""
    q = find_question(state, "qa_01")
    ans = find_entity(q["answers"], id="ans_01")
    ans["helpful"] = ans["helpful"] + 1


def solve_task_33(state):
    """Submit question about balancing coursework with internship applications."""
    q_id = "qa_" + str(state["_nextQuestionId"]).zfill(2)
    state["_nextQuestionId"] += 1
    state["qaQuestions"].insert(0, {
        "id": q_id,
        "authorName": "Maya Chen",
        "authorSchool": state["currentUser"]["school"],
        "authorMajor": state["currentUser"]["major"],
        "authorGradYear": state["currentUser"]["graduationYear"],
        "authorAvatarColor": state["currentUser"]["avatarColor"],
        "question": "How do you balance coursework with internship applications during junior year?",
        "status": "pending",
        "createdAt": "2026-03-07T12:00:00Z",
        "views": 0,
        "answers": [],
    })


def solve_task_34(state):
    """Update bio."""
    state["currentUser"]["bio"] = "Aspiring product manager and engineer. Passionate about building AI products that make a difference."


def solve_task_35(state):
    """Update phone number."""
    state["currentUser"]["phone"] = "(650) 555-9999"


def solve_task_36(state):
    """Change profile visibility to Employers."""
    state["currentUser"]["profileVisibility"] = "Employers"


def solve_task_37(state):
    """Change profile visibility to Private."""
    state["currentUser"]["profileVisibility"] = "Private"


def solve_task_38(state):
    """Update LinkedIn URL."""
    state["currentUser"]["linkedinUrl"] = "linkedin.com/in/maya-chen-stanford"


def solve_task_39(state):
    """Update website URL."""
    state["currentUser"]["websiteUrl"] = "mayachen.io"


def solve_task_40(state):
    """Add Full-time to career interest job types."""
    ci = state["currentUser"]["careerInterests"]
    if "Full-time" not in ci["jobTypes"]:
        ci["jobTypes"].append("Full-time")


def solve_task_41(state):
    """Remove Part-time from career interest job types."""
    ci = state["currentUser"]["careerInterests"]
    ci["jobTypes"] = [jt for jt in ci["jobTypes"] if jt != "Part-time"]


def solve_task_42(state):
    """Add Job to career interest helpWith."""
    ci = state["currentUser"]["careerInterests"]
    if "Job" not in ci["helpWith"]:
        ci["helpWith"].append("Job")


def solve_task_43(state):
    """Remove Events from career interest helpWith."""
    ci = state["currentUser"]["careerInterests"]
    ci["helpWith"] = [h for h in ci["helpWith"] if h != "Events"]


def solve_task_44(state):
    """Add Gap year to career interest postGraduation."""
    ci = state["currentUser"]["careerInterests"]
    if "Gap year" not in ci["postGraduation"]:
        ci["postGraduation"].append("Gap year")


def solve_task_45(state):
    """Remove Grad school from career interest postGraduation."""
    ci = state["currentUser"]["careerInterests"]
    ci["postGraduation"] = [pg for pg in ci["postGraduation"] if pg != "Grad school"]


def solve_task_46(state):
    """Add Frontend Developer to career interest roles."""
    ci = state["currentUser"]["careerInterests"]
    if "Frontend Developer" not in ci["roles"]:
        ci["roles"].append("Frontend Developer")


def solve_task_47(state):
    """Remove UX Designer from career interest roles."""
    ci = state["currentUser"]["careerInterests"]
    ci["roles"] = [r for r in ci["roles"] if r != "UX Designer"]


def solve_task_48(state):
    """Add Chicago, IL to career interest locations."""
    ci = state["currentUser"]["careerInterests"]
    if "Chicago, IL" not in ci["locations"]:
        ci["locations"].append("Chicago, IL")


def solve_task_49(state):
    """Remove Austin, TX from career interest locations."""
    ci = state["currentUser"]["careerInterests"]
    ci["locations"] = [loc for loc in ci["locations"] if loc != "Austin, TX"]


def solve_task_50(state):
    """Change career community to Business & Finance."""
    state["currentUser"]["careerInterests"]["careerCommunity"] = "Business & Finance"


def solve_task_51(state):
    """Change expected graduation date to December 2026."""
    state["currentUser"]["careerInterests"]["expectedGraduationDate"] = "December 2026"


def solve_task_52(state):
    """Add Cybersecurity to career interest industries."""
    ci = state["currentUser"]["careerInterests"]
    if "Cybersecurity" not in ci["industries"]:
        ci["industries"].append("Cybersecurity")


def solve_task_53(state):
    """Remove Finance from career interest industries."""
    ci = state["currentUser"]["careerInterests"]
    ci["industries"] = [ind for ind in ci["industries"] if ind != "Finance"]


def solve_task_54(state):
    """Add Marketing to career interest job functions."""
    ci = state["currentUser"]["careerInterests"]
    if "Marketing" not in ci["jobFunctions"]:
        ci["jobFunctions"].append("Marketing")


def solve_task_55(state):
    """Remove Design from career interest job functions."""
    ci = state["currentUser"]["careerInterests"]
    ci["jobFunctions"] = [jf for jf in ci["jobFunctions"] if jf != "Design"]


# -- solver registry ----------------------------------------------------------

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


# -- server management --------------------------------------------------------

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
    while port < start + 100:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("", port))
                return port
            except OSError:
                port += 1
    raise RuntimeError(f"No free port found in range {start}-{start+100}")


def start_server(port):
    """Start the server on the given port."""
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


# -- task runner ---------------------------------------------------------------

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
    """Reset -> solve -> verify for a single task."""
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


# -- main ---------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Handshake Career Exploration function-task sanity check"
    )
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
