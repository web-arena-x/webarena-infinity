#!/usr/bin/env python3
"""
Sanity check for Handshake Career Exploration real tasks.

For each task, directly applies the expected end-state (bypassing the agent),
then runs the verifier and asserts it passes.

Usage:
    python3 sanity_check.py                     # All tasks, sequential
    python3 sanity_check.py --workers N          # N parallel environments
    python3 sanity_check.py --task-id task_e1    # Single task
    python3 sanity_check.py --port 9500          # Custom base port
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
TASKS_FILE = APP_DIR / "real-tasks.json"

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


def find_job(state, job_id):
    return find_entity(state["jobs"], id=job_id)


# -- solve functions ----------------------------------------------------------

# === EASY ===

def solve_task_e1(state):
    """Follow Spotify (emp_13)."""
    user = state["currentUser"]
    if "emp_13" not in user["followedEmployerIds"]:
        user["followedEmployerIds"].append("emp_13")
    emp = find_employer(state, "emp_13")
    emp["followCount"] = emp["followCount"] + 1


def solve_task_e2(state):
    """Unfollow Stripe (emp_10)."""
    user = state["currentUser"]
    user["followedEmployerIds"] = [
        eid for eid in user["followedEmployerIds"] if eid != "emp_10"
    ]
    emp = find_employer(state, "emp_10")
    emp["followCount"] = emp["followCount"] - 1


def solve_task_e3(state):
    """Save Microsoft SWE Intern (job_04)."""
    user = state["currentUser"]
    if "job_04" not in user["savedJobIds"]:
        user["savedJobIds"].append("job_04")


def solve_task_e4(state):
    """Unsave Meta ML Engineer Intern (job_07)."""
    user = state["currentUser"]
    user["savedJobIds"] = [jid for jid in user["savedJobIds"] if jid != "job_07"]


def solve_task_e5(state):
    """RSVP to JPMorgan Markets & Trading Panel (evt_08)."""
    evt = find_event(state, "evt_08")
    evt["rsvped"] = True
    evt["rsvpCount"] = evt["rsvpCount"] + 1


def solve_task_e6(state):
    """Bookmark Amazon AWS post (post_07)."""
    post = find_post(state, "post_07")
    post["bookmarked"] = True
    user = state["currentUser"]
    if "post_07" not in user["savedPostIds"]:
        user["savedPostIds"].append("post_07")


def solve_task_e7(state):
    """Like Jordan Taylor's startup post (post_12)."""
    post = find_post(state, "post_12")
    post["likes"] = post["likes"] + 1


def solve_task_e8(state):
    """Read Apple Pathways message (msg_08)."""
    msg = find_message(state, "msg_08")
    msg["isRead"] = True


def solve_task_e9(state):
    """Follow Goldman Sachs (emp_06)."""
    user = state["currentUser"]
    if "emp_06" not in user["followedEmployerIds"]:
        user["followedEmployerIds"].append("emp_06")
    emp = find_employer(state, "emp_06")
    emp["followCount"] = emp["followCount"] + 1


def solve_task_e10(state):
    """Save Palantir FDE Intern (job_19)."""
    user = state["currentUser"]
    if "job_19" not in user["savedJobIds"]:
        user["savedJobIds"].append("job_19")


def solve_task_e11(state):
    """RSVP to Google Tech Talk (evt_04)."""
    evt = find_event(state, "evt_04")
    evt["rsvped"] = True
    evt["rsvpCount"] = evt["rsvpCount"] + 1


def solve_task_e12(state):
    """Read Meta ML Intern message (msg_03)."""
    msg = find_message(state, "msg_03")
    msg["isRead"] = True


def solve_task_e13(state):
    """Like Anthropic AI safety post (post_05)."""
    post = find_post(state, "post_05")
    post["likes"] = post["likes"] + 1


def solve_task_e14(state):
    """Follow Palantir (emp_17)."""
    user = state["currentUser"]
    if "emp_17" not in user["followedEmployerIds"]:
        user["followedEmployerIds"].append("emp_17")
    emp = find_employer(state, "emp_17")
    emp["followCount"] = emp["followCount"] + 1


def solve_task_e15(state):
    """Bookmark Kevin O'Brien's FAANG post (post_08)."""
    post = find_post(state, "post_08")
    post["bookmarked"] = True
    user = state["currentUser"]
    if "post_08" not in user["savedPostIds"]:
        user["savedPostIds"].append("post_08")


def solve_task_e16(state):
    """RSVP to Salesforce Futureforce (evt_10)."""
    evt = find_event(state, "evt_10")
    evt["rsvped"] = True
    evt["rsvpCount"] = evt["rsvpCount"] + 1


def solve_task_e17(state):
    """Unsave Amazon PM Intern (job_24)."""
    user = state["currentUser"]
    user["savedJobIds"] = [jid for jid in user["savedJobIds"] if jid != "job_24"]


def solve_task_e18(state):
    """Mark Nathan Brooks's answer (ans_14) on qa_12 as helpful."""
    q = find_question(state, "qa_12")
    ans = find_entity(q["answers"], id="ans_14")
    ans["helpful"] = ans["helpful"] + 1


def solve_task_e19(state):
    """Like Microsoft Imagine Cup post (post_19)."""
    post = find_post(state, "post_19")
    post["likes"] = post["likes"] + 1


def solve_task_e20(state):
    """Follow Teach For America (emp_18)."""
    user = state["currentUser"]
    if "emp_18" not in user["followedEmployerIds"]:
        user["followedEmployerIds"].append("emp_18")
    emp = find_employer(state, "emp_18")
    emp["followCount"] = emp["followCount"] + 1


# === MEDIUM ===

def solve_task_m1(state):
    """Update bio to mention AI safety."""
    state["currentUser"]["bio"] = "Exploring opportunities in AI safety and alignment research. CS student at Stanford."


def solve_task_m2(state):
    """Add Machine Learning Engineer to preferred roles."""
    ci = state["currentUser"]["careerInterests"]
    if "Machine Learning Engineer" not in ci["roles"]:
        ci["roles"].append("Machine Learning Engineer")


def solve_task_m3(state):
    """Post Q&A question about PM interview prep."""
    q_id = "qa_" + str(state["_nextQuestionId"]).zfill(2)
    state["_nextQuestionId"] += 1
    state["qaQuestions"].insert(0, {
        "id": q_id,
        "authorName": "Maya Chen",
        "authorSchool": state["currentUser"]["school"],
        "authorMajor": state["currentUser"]["major"],
        "authorGradYear": state["currentUser"]["graduationYear"],
        "authorAvatarColor": state["currentUser"]["avatarColor"],
        "question": "What are the best ways to prepare for product management interviews at top tech companies?",
        "status": "pending",
        "createdAt": "2026-03-07T12:00:00Z",
        "views": 0,
        "answers": [],
    })


def solve_task_m4(state):
    """Comment on Jessica Park's post (post_02)."""
    post = find_post(state, "post_02")
    comment_id = "cmt_" + str(state["_nextCommentId"])
    state["_nextCommentId"] += 1
    post["comments"].append({
        "id": comment_id,
        "authorName": state["currentUser"]["fullName"],
        "authorSchool": state["currentUser"]["school"],
        "authorAvatarColor": state["currentUser"]["avatarColor"],
        "text": "Congrats! Would love to hear more about your experience.",
        "createdAt": "2026-03-07T12:00:00Z",
        "isAnonymous": False,
    })


def solve_task_m5(state):
    """Schedule resume review for March 12 at 11 AM, in person."""
    appt_id = "appt_" + str(state["_nextAppointmentId"]).zfill(2)
    state["_nextAppointmentId"] += 1
    state["appointments"].append({
        "id": appt_id,
        "category": "Resume & Cover Letter",
        "type": "Resume Review",
        "staffId": None,
        "staffName": None,
        "date": "2026-03-12",
        "time": "11:00 AM",
        "duration": 30,
        "medium": "In Person",
        "location": "Career Center",
        "status": "requested",
        "details": "",
        "comments": [],
        "createdAt": "2026-03-07T12:00:00Z",
    })


def solve_task_m6(state):
    """Change career community to Science & Research."""
    state["currentUser"]["careerInterests"]["careerCommunity"] = "Science & Research"


def solve_task_m7(state):
    """Add Boston, MA and Denver, CO to preferred locations."""
    ci = state["currentUser"]["careerInterests"]
    for loc in ["Boston, MA", "Denver, CO"]:
        if loc not in ci["locations"]:
            ci["locations"].append(loc)


def solve_task_m8(state):
    """Remove Finance, add Consulting to industries."""
    ci = state["currentUser"]["careerInterests"]
    ci["industries"] = [ind for ind in ci["industries"] if ind != "Finance"]
    if "Consulting" not in ci["industries"]:
        ci["industries"].append("Consulting")


def solve_task_m9(state):
    """Update LinkedIn URL."""
    state["currentUser"]["linkedinUrl"] = "linkedin.com/in/maya-chen-cs"


def solve_task_m10(state):
    """Create feed post about system design resources."""
    post_id = "post_" + str(state["_nextPostId"])
    state["_nextPostId"] += 1
    state["feedPosts"].insert(0, {
        "id": post_id,
        "authorType": "student",
        "authorId": state["currentUser"]["id"],
        "authorName": state["currentUser"]["fullName"],
        "authorSchool": state["currentUser"]["school"],
        "authorAvatarColor": state["currentUser"]["avatarColor"],
        "content": "Here are my favorite system design resources for interview prep: System Design Primer, Grokking the System Design Interview, and Designing Data-Intensive Applications.",
        "audience": "everyone",
        "likes": 0,
        "comments": [],
        "hasImage": False,
        "hasVideo": False,
        "createdAt": "2026-03-07T12:00:00Z",
        "bookmarked": False,
    })


def solve_task_m11(state):
    """Answer qa_04 about virtual career fair attire."""
    q = find_question(state, "qa_04")
    ans_id = "ans_" + str(state["_nextAnswerId"]).zfill(2)
    state["_nextAnswerId"] += 1
    q["answers"].append({
        "id": ans_id,
        "authorName": "Maya Chen",
        "authorSchool": state["currentUser"]["school"],
        "authorMajor": state["currentUser"]["major"],
        "authorGradYear": state["currentUser"]["graduationYear"],
        "authorAvatarColor": state["currentUser"]["avatarColor"],
        "text": "I'd recommend business casual attire - a nice top or blouse works well. Also make sure to test your camera and microphone beforehand!",
        "visibility": "full",
        "status": "pending",
        "createdAt": "2026-03-07T12:00:00Z",
        "helpful": 0,
    })


def solve_task_m12(state):
    """Add comment to appt_01 about LinkedIn headline."""
    appt = find_appointment(state, "appt_01")
    appt["comments"].append({
        "author": state["currentUser"]["fullName"],
        "text": "Can you also help with my LinkedIn headline during our session?",
        "createdAt": "2026-03-07T12:00:00Z",
    })


def solve_task_m13(state):
    """Remove Data Analytics, add Research to job functions."""
    ci = state["currentUser"]["careerInterests"]
    ci["jobFunctions"] = [jf for jf in ci["jobFunctions"] if jf != "Data Analytics"]
    if "Research" not in ci["jobFunctions"]:
        ci["jobFunctions"].append("Research")


def solve_task_m14(state):
    """Change expected graduation date to August 2027."""
    state["currentUser"]["careerInterests"]["expectedGraduationDate"] = "August 2027"


def solve_task_m15(state):
    """Comment on McKinsey post (post_09) about projects."""
    post = find_post(state, "post_09")
    comment_id = "cmt_" + str(state["_nextCommentId"])
    state["_nextCommentId"] += 1
    post["comments"].append({
        "id": comment_id,
        "authorName": state["currentUser"]["fullName"],
        "authorSchool": state["currentUser"]["school"],
        "authorAvatarColor": state["currentUser"]["avatarColor"],
        "text": "What types of projects can attendees expect to hear about?",
        "createdAt": "2026-03-07T12:00:00Z",
        "isAnonymous": False,
    })


def solve_task_m16(state):
    """Save both Anthropic jobs (job_12 already saved, add job_29)."""
    user = state["currentUser"]
    for jid in ["job_12", "job_29"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)


def solve_task_m17(state):
    """Add On-campus to job type preferences."""
    ci = state["currentUser"]["careerInterests"]
    if "On-campus" not in ci["jobTypes"]:
        ci["jobTypes"].append("On-campus")


def solve_task_m18(state):
    """Cancel case interview prep appointment (appt_08)."""
    appt = find_appointment(state, "appt_08")
    appt["status"] = "cancelled"


def solve_task_m19(state):
    """Schedule networking strategy appointment for March 17 at 1 PM, virtual."""
    appt_id = "appt_" + str(state["_nextAppointmentId"]).zfill(2)
    state["_nextAppointmentId"] += 1
    state["appointments"].append({
        "id": appt_id,
        "category": "Networking & Professional Development",
        "type": "Networking Strategy",
        "staffId": None,
        "staffName": None,
        "date": "2026-03-17",
        "time": "1:00 PM",
        "duration": 30,
        "medium": "Virtual on Handshake",
        "location": None,
        "status": "requested",
        "details": "",
        "comments": [],
        "createdAt": "2026-03-07T12:00:00Z",
    })


def solve_task_m20(state):
    """Post semi-anonymous answer to qa_06 about mock interviews."""
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
        "text": "I also highly recommend practicing with mock system design interviews. Seeing how others approach problems really helps build intuition.",
        "visibility": "semi-anonymous",
        "status": "pending",
        "createdAt": "2026-03-07T12:00:00Z",
        "helpful": 0,
    })


# === HARD ===

def solve_task_h1(state):
    """Follow all consulting firms: McKinsey (emp_04), Deloitte (emp_08), Bain (emp_11)."""
    user = state["currentUser"]
    for emp_id in ["emp_04", "emp_08", "emp_11"]:
        if emp_id not in user["followedEmployerIds"]:
            user["followedEmployerIds"].append(emp_id)
        emp = find_employer(state, emp_id)
        emp["followCount"] = emp["followCount"] + 1


def solve_task_h2(state):
    """Pivot career interests toward consulting."""
    ci = state["currentUser"]["careerInterests"]
    ci["careerCommunity"] = "Business & Finance"
    for role in ["Consultant", "Business Analyst"]:
        if role not in ci["roles"]:
            ci["roles"].append(role)
    if "Consulting" not in ci["industries"]:
        ci["industries"].append("Consulting")
    if "Sales" not in ci["jobFunctions"]:
        ci["jobFunctions"].append("Sales")


def solve_task_h3(state):
    """Save all active Google jobs: job_01, job_02, job_22."""
    user = state["currentUser"]
    for jid in ["job_01", "job_02", "job_22"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)


def solve_task_h4(state):
    """Unsave closed jobs. job_03 is the only closed job in savedJobIds."""
    user = state["currentUser"]
    closed_ids = set()
    for jid in user["savedJobIds"]:
        try:
            job = find_job(state, jid)
            if job.get("status") == "closed":
                closed_ids.add(jid)
        except ValueError:
            pass
    user["savedJobIds"] = [jid for jid in user["savedJobIds"] if jid not in closed_ids]


def solve_task_h5(state):
    """RSVP to all upcoming virtual events: evt_02, evt_06, evt_07, evt_10."""
    for evt_id in ["evt_02", "evt_06", "evt_07", "evt_10"]:
        evt = find_event(state, evt_id)
        evt["rsvped"] = True
        evt["rsvpCount"] = evt["rsvpCount"] + 1


def solve_task_h6(state):
    """Follow all finance employers: JPMorgan (emp_02), Goldman (emp_06)."""
    user = state["currentUser"]
    for emp_id in ["emp_02", "emp_06"]:
        if emp_id not in user["followedEmployerIds"]:
            user["followedEmployerIds"].append(emp_id)
        emp = find_employer(state, emp_id)
        emp["followCount"] = emp["followCount"] + 1


def solve_task_h7(state):
    """Save all Google and Microsoft internships: job_01, job_02, job_22, job_04, job_23."""
    user = state["currentUser"]
    for jid in ["job_01", "job_02", "job_22", "job_04", "job_23"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)


def solve_task_h8(state):
    """Schedule grad school advising with Maria Rodriguez and ensure Grad school in postGraduation."""
    appt_id = "appt_" + str(state["_nextAppointmentId"]).zfill(2)
    state["_nextAppointmentId"] += 1
    state["appointments"].append({
        "id": appt_id,
        "category": "Graduate School",
        "type": "Grad School Advising",
        "staffId": "staff_03",
        "staffName": "Maria Rodriguez",
        "date": "2026-03-18",
        "time": "10:00 AM",
        "duration": 30,
        "medium": "Virtual on Handshake",
        "location": None,
        "status": "requested",
        "details": "",
        "comments": [],
        "createdAt": "2026-03-07T12:00:00Z",
    })
    ci = state["currentUser"]["careerInterests"]
    if "Grad school" not in ci["postGraduation"]:
        ci["postGraduation"].append("Grad school")


def solve_task_h9(state):
    """Bookmark all employer posts from followed companies."""
    seed_followed = ["emp_01", "emp_03", "emp_05", "emp_07", "emp_10", "emp_12", "emp_15"]
    user = state["currentUser"]
    for post in state["feedPosts"]:
        if post.get("authorType") == "employer" and post.get("authorId") in seed_followed:
            post["bookmarked"] = True
            pid = post["id"]
            if pid not in user["savedPostIds"]:
                user["savedPostIds"].append(pid)


def solve_task_h10(state):
    """Read all unread messages and RSVP to Interview Prep workshop (evt_09)."""
    for msg_id in ["msg_01", "msg_03", "msg_06", "msg_08"]:
        msg = find_message(state, msg_id)
        msg["isRead"] = True
    evt = find_event(state, "evt_09")
    evt["rsvped"] = True
    evt["rsvpCount"] = evt["rsvpCount"] + 1


def solve_task_h11(state):
    """PM recruiting prep: ensure PM in roles, add Full-time, ensure job_18 and job_24 saved."""
    ci = state["currentUser"]["careerInterests"]
    if "Product Manager" not in ci["roles"]:
        ci["roles"].append("Product Manager")
    if "Full-time" not in ci["jobTypes"]:
        ci["jobTypes"].append("Full-time")
    user = state["currentUser"]
    for jid in ["job_18", "job_24"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)


def solve_task_h12(state):
    """Replace all locations with Boston, Chicago, Washington DC."""
    state["currentUser"]["careerInterests"]["locations"] = [
        "Boston, MA", "Chicago, IL", "Washington, DC"
    ]


def solve_task_h13(state):
    """Create school-audience post about case interviews and RSVP to McKinsey presentation."""
    post_id = "post_" + str(state["_nextPostId"])
    state["_nextPostId"] += 1
    state["feedPosts"].insert(0, {
        "id": post_id,
        "authorType": "student",
        "authorId": state["currentUser"]["id"],
        "authorName": state["currentUser"]["fullName"],
        "authorSchool": state["currentUser"]["school"],
        "authorAvatarColor": state["currentUser"]["avatarColor"],
        "content": "Anyone interested in forming a study group for case interview prep? Let's connect!",
        "audience": "school",
        "likes": 0,
        "comments": [],
        "hasImage": False,
        "hasVideo": False,
        "createdAt": "2026-03-07T12:00:00Z",
        "bookmarked": False,
    })
    evt = find_event(state, "evt_01")
    evt["rsvped"] = True
    evt["rsvpCount"] = evt["rsvpCount"] + 1


def solve_task_h14(state):
    """Answer qa_10 about networking, mark ans_07 on qa_05 as helpful."""
    q10 = find_question(state, "qa_10")
    ans_id = "ans_" + str(state["_nextAnswerId"]).zfill(2)
    state["_nextAnswerId"] += 1
    q10["answers"].append({
        "id": ans_id,
        "authorName": "Maya Chen",
        "authorSchool": state["currentUser"]["school"],
        "authorMajor": state["currentUser"]["major"],
        "authorGradYear": state["currentUser"]["graduationYear"],
        "authorAvatarColor": state["currentUser"]["avatarColor"],
        "text": "Start networking with alumni and recruiters early, ideally in August-September of the previous year.",
        "visibility": "full",
        "status": "pending",
        "createdAt": "2026-03-07T12:00:00Z",
        "helpful": 0,
    })
    q05 = find_question(state, "qa_05")
    ans07 = find_entity(q05["answers"], id="ans_07")
    ans07["helpful"] = ans07["helpful"] + 1


def solve_task_h15(state):
    """Cancel all requested appointments: appt_02 and appt_08."""
    for appt_id in ["appt_02", "appt_08"]:
        appt = find_appointment(state, appt_id)
        appt["status"] = "cancelled"


def solve_task_h16(state):
    """Set AI/ML-focused career interests."""
    ci = state["currentUser"]["careerInterests"]
    ci["careerCommunity"] = "Technology"
    ci["roles"] = ["Software Engineer", "Machine Learning Engineer", "Data Scientist", "Research Scientist"]
    ci["industries"] = ["Technology", "Artificial Intelligence"]


def solve_task_h17(state):
    """Follow all employers with AI/ML labeled jobs."""
    user = state["currentUser"]
    aiml_employer_ids = set()
    for job in state["jobs"]:
        if "AI/ML" in job.get("labels", []):
            aiml_employer_ids.add(job["employerId"])
    for emp_id in aiml_employer_ids:
        if emp_id not in user["followedEmployerIds"]:
            user["followedEmployerIds"].append(emp_id)
            emp = find_employer(state, emp_id)
            emp["followCount"] = emp["followCount"] + 1


def solve_task_h18(state):
    """Save all active internships in San Francisco: job_02, job_09, job_12, job_29, job_30."""
    user = state["currentUser"]
    for jid in ["job_02", "job_09", "job_12", "job_29", "job_30"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)


def solve_task_h19(state):
    """Schedule salary negotiation appointment and update phone."""
    appt_id = "appt_" + str(state["_nextAppointmentId"]).zfill(2)
    state["_nextAppointmentId"] += 1
    state["appointments"].append({
        "id": appt_id,
        "category": "Networking & Professional Development",
        "type": "Salary Negotiation",
        "staffId": None,
        "staffName": None,
        "date": "2026-03-13",
        "time": "3:00 PM",
        "duration": 30,
        "medium": "Phone",
        "location": None,
        "status": "requested",
        "details": "",
        "comments": [],
        "createdAt": "2026-03-07T12:00:00Z",
    })
    state["currentUser"]["phone"] = "(650) 555-0200"


def solve_task_h20(state):
    """Mark answers about diversity/salary as helpful, bookmark posts by Q&A answerers."""
    # Mark helpful
    q11 = find_question(state, "qa_11")
    ans13 = find_entity(q11["answers"], id="ans_13")
    ans13["helpful"] = ans13["helpful"] + 1

    q05 = find_question(state, "qa_05")
    ans07 = find_entity(q05["answers"], id="ans_07")
    ans07["helpful"] = ans07["helpful"] + 1
    ans08 = find_entity(q05["answers"], id="ans_08")
    ans08["helpful"] = ans08["helpful"] + 1

    # Bookmark posts by Q&A answerers
    user = state["currentUser"]
    for post_id in ["post_12", "post_06", "post_10"]:
        post = find_post(state, post_id)
        post["bookmarked"] = True
        if post_id not in user["savedPostIds"]:
            user["savedPostIds"].append(post_id)


# === HARDENING ROUND 1 ===

def solve_task_h21(state):
    """Save all active Google jobs and RSVP to Google's tech talk.
    Discovery: unread top-match recruiting + tech talk → Google.
    """
    user = state["currentUser"]
    for jid in ["job_01", "job_02", "job_22"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)
    evt = find_event(state, "evt_04")
    evt["rsvped"] = True
    evt["rsvpCount"] = evt["rsvpCount"] + 1


def solve_task_h22(state):
    """Like Nathan Brooks' post (qa_12 liberal arts answerer → post_16)."""
    post = find_post(state, "post_16")
    post["likes"] = post["likes"] + 1


def solve_task_h23(state):
    """Create school post about salary negotiation (most-viewed Q&A: qa_05, 1567 views)."""
    post_id = "post_" + str(state["_nextPostId"])
    state["_nextPostId"] += 1
    state["feedPosts"].insert(0, {
        "id": post_id,
        "authorType": "student",
        "authorId": state["currentUser"]["id"],
        "authorName": state["currentUser"]["fullName"],
        "authorSchool": state["currentUser"]["school"],
        "authorAvatarColor": state["currentUser"]["avatarColor"],
        "content": "The most-viewed question in Q&A is about salary negotiation for new grad offers. I highly recommend checking it out - great advice on leveraging competing offers and negotiating total comp!",
        "audience": "school",
        "likes": 0,
        "comments": [],
        "hasImage": False,
        "hasVideo": False,
        "createdAt": "2026-03-07T12:00:00Z",
        "bookmarked": False,
    })


def solve_task_h24(state):
    """RSVP to upcoming events from followed employers: evt_02, evt_04, evt_06."""
    for evt_id in ["evt_02", "evt_04", "evt_06"]:
        evt = find_event(state, evt_id)
        evt["rsvped"] = True
        evt["rsvpCount"] = evt["rsvpCount"] + 1


def solve_task_h25(state):
    """Mark Aisha Mohammed's Q&A answer helpful (NSBE post author → ans_13 on qa_11)."""
    q = find_question(state, "qa_11")
    ans = find_entity(q["answers"], id="ans_13")
    ans["helpful"] = ans["helpful"] + 1


def solve_task_h26(state):
    """Save active internships from private companies + follow unfollowed private companies."""
    user = state["currentUser"]
    # Save active internships from private employers
    for jid in ["job_05", "job_09", "job_11", "job_12", "job_29"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)
    # Follow private companies not yet followed
    for emp_id in ["emp_04", "emp_08", "emp_11", "emp_14", "emp_20"]:
        if emp_id not in user["followedEmployerIds"]:
            user["followedEmployerIds"].append(emp_id)
            emp = find_employer(state, emp_id)
            emp["followCount"] = emp["followCount"] + 1


def solve_task_h27(state):
    """Schedule application review + post Q&A question about follow-up."""
    appt_id = "appt_" + str(state["_nextAppointmentId"]).zfill(2)
    state["_nextAppointmentId"] += 1
    state["appointments"].append({
        "id": appt_id,
        "category": "Job & Internship Search",
        "type": "Application Review",
        "staffId": None,
        "staffName": None,
        "date": "2026-03-13",
        "time": "10:00 AM",
        "duration": 30,
        "medium": "Phone",
        "location": None,
        "status": "requested",
        "details": "",
        "comments": [],
        "createdAt": "2026-03-07T12:00:00Z",
    })
    q_id = "qa_" + str(state["_nextQuestionId"]).zfill(2)
    state["_nextQuestionId"] += 1
    state["qaQuestions"].insert(0, {
        "id": q_id,
        "authorName": "Maya Chen",
        "authorSchool": state["currentUser"]["school"],
        "authorMajor": state["currentUser"]["major"],
        "authorGradYear": state["currentUser"]["graduationYear"],
        "authorAvatarColor": state["currentUser"]["avatarColor"],
        "question": "What is the best way to follow up after submitting job applications? How long should I wait before reaching out?",
        "status": "pending",
        "createdAt": "2026-03-07T12:00:00Z",
        "views": 0,
        "answers": [],
    })


def solve_task_h28(state):
    """Mark non-anonymous answer on Google interview Q&A as helpful + bookmark Google post."""
    q = find_question(state, "qa_01")
    ans = find_entity(q["answers"], id="ans_01")
    ans["helpful"] = ans["helpful"] + 1
    post = find_post(state, "post_01")
    post["bookmarked"] = True
    user = state["currentUser"]
    if "post_01" not in user["savedPostIds"]:
        user["savedPostIds"].append("post_01")


def solve_task_h29(state):
    """Save active STEM jobs from non-followed employers."""
    user = state["currentUser"]
    for jid in ["job_08", "job_15", "job_16", "job_19", "job_28"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)


def solve_task_h30(state):
    """Refocus career on finance."""
    ci = state["currentUser"]["careerInterests"]
    ci["careerCommunity"] = "Business & Finance"
    ci["roles"] = ["Financial Analyst", "Business Analyst", "Consultant"]
    ci["industries"] = ["Finance", "Consulting"]
    ci["jobFunctions"] = [jf for jf in ci["jobFunctions"] if jf != "Engineering"]
    if "Finance & Accounting" not in ci["jobFunctions"]:
        ci["jobFunctions"].append("Finance & Accounting")


def solve_task_h31(state):
    """Comment on Marcus Johnson's Stripe post (post_04) + save Stripe job (job_09)."""
    post = find_post(state, "post_04")
    comment_id = "cmt_" + str(state["_nextCommentId"])
    state["_nextCommentId"] += 1
    post["comments"].append({
        "id": comment_id,
        "authorName": state["currentUser"]["fullName"],
        "authorSchool": state["currentUser"]["school"],
        "authorAvatarColor": state["currentUser"]["avatarColor"],
        "text": "That sounds amazing! How was the onboarding process at Stripe?",
        "createdAt": "2026-03-07T12:00:00Z",
        "isAnonymous": False,
    })
    user = state["currentUser"]
    if "job_09" not in user["savedJobIds"]:
        user["savedJobIds"].append("job_09")


def solve_task_h32(state):
    """Save Microsoft jobs (job_04, job_23) + comment on Imagine Cup post (post_19)."""
    user = state["currentUser"]
    for jid in ["job_04", "job_23"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)
    post = find_post(state, "post_19")
    comment_id = "cmt_" + str(state["_nextCommentId"])
    state["_nextCommentId"] += 1
    post["comments"].append({
        "id": comment_id,
        "authorName": state["currentUser"]["fullName"],
        "authorSchool": state["currentUser"]["school"],
        "authorAvatarColor": state["currentUser"]["avatarColor"],
        "text": "This sounds great! I'm interested in participating in Imagine Cup this year.",
        "createdAt": "2026-03-07T12:00:00Z",
        "isAnonymous": False,
    })


def solve_task_h33(state):
    """Comment on David Lee's PM study group post (post_14) found via Saved tab."""
    post = find_post(state, "post_14")
    comment_id = "cmt_" + str(state["_nextCommentId"])
    state["_nextCommentId"] += 1
    post["comments"].append({
        "id": comment_id,
        "authorName": state["currentUser"]["fullName"],
        "authorSchool": state["currentUser"]["school"],
        "authorAvatarColor": state["currentUser"]["avatarColor"],
        "text": "Thanks for organizing this study group! I'd love to join.",
        "createdAt": "2026-03-07T12:00:00Z",
        "isAnonymous": False,
    })


def solve_task_h34(state):
    """Unsave jobs from non-Tech/AI employers: job_03 (Finance), job_18 (Retail)."""
    user = state["currentUser"]
    user["savedJobIds"] = [
        jid for jid in user["savedJobIds"] if jid not in ("job_03", "job_18")
    ]


def solve_task_h35(state):
    """Follow all NY employers + save their active internships."""
    user = state["currentUser"]
    for emp_id in ["emp_02", "emp_04", "emp_06", "emp_08", "emp_13", "emp_18"]:
        if emp_id not in user["followedEmployerIds"]:
            user["followedEmployerIds"].append(emp_id)
            emp = find_employer(state, emp_id)
            emp["followCount"] = emp["followCount"] + 1
    for jid in ["job_05", "job_11", "job_15"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)


def solve_task_h36(state):
    """Schedule cover letter review with Sarah Thompson + update website URL."""
    appt_id = "appt_" + str(state["_nextAppointmentId"]).zfill(2)
    state["_nextAppointmentId"] += 1
    state["appointments"].append({
        "id": appt_id,
        "category": "Resume & Cover Letter",
        "type": "Cover Letter Review",
        "staffId": "staff_05",
        "staffName": "Sarah Thompson",
        "date": "2026-03-11",
        "time": "1:00 PM",
        "duration": 30,
        "medium": "Virtual on Handshake",
        "location": None,
        "status": "requested",
        "details": "",
        "comments": [],
        "createdAt": "2026-03-07T12:00:00Z",
    })
    state["currentUser"]["websiteUrl"] = "mayachen.design"


def solve_task_h37(state):
    """Set profile visibility to Employers, swap Part-time for Full-time, add LA."""
    state["currentUser"]["profileVisibility"] = "Employers"
    ci = state["currentUser"]["careerInterests"]
    ci["jobTypes"] = [jt for jt in ci["jobTypes"] if jt != "Part-time"]
    if "Full-time" not in ci["jobTypes"]:
        ci["jobTypes"].append("Full-time")
    if "Los Angeles, CA" not in ci["locations"]:
        ci["locations"].append("Los Angeles, CA")


def solve_task_h38(state):
    """Mark Nathan Brooks' Q&A answer helpful (ans_14 on qa_12) + comment on post_16."""
    q = find_question(state, "qa_12")
    ans = find_entity(q["answers"], id="ans_14")
    ans["helpful"] = ans["helpful"] + 1
    post = find_post(state, "post_16")
    comment_id = "cmt_" + str(state["_nextCommentId"])
    state["_nextCommentId"] += 1
    post["comments"].append({
        "id": comment_id,
        "authorName": state["currentUser"]["fullName"],
        "authorSchool": state["currentUser"]["school"],
        "authorAvatarColor": state["currentUser"]["avatarColor"],
        "text": "Thanks for sharing these career fair tips! Really helpful advice.",
        "createdAt": "2026-03-07T12:00:00Z",
        "isAnonymous": False,
    })


def solve_task_h39(state):
    """Like consulting/finance employer posts, follow them, save their active jobs."""
    # Like posts
    post_09 = find_post(state, "post_09")
    post_09["likes"] = post_09["likes"] + 1
    post_15 = find_post(state, "post_15")
    post_15["likes"] = post_15["likes"] + 1
    # Follow employers
    user = state["currentUser"]
    for emp_id in ["emp_02", "emp_04"]:
        if emp_id not in user["followedEmployerIds"]:
            user["followedEmployerIds"].append(emp_id)
            emp = find_employer(state, emp_id)
            emp["followCount"] = emp["followCount"] + 1
    # Save active jobs
    for jid in ["job_05", "job_27"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)


def solve_task_h40(state):
    """Read unread messages from Tech employers + bookmark their posts."""
    # Read messages
    for msg_id in ["msg_01", "msg_03", "msg_06", "msg_08"]:
        msg = find_message(state, msg_id)
        msg["isRead"] = True
    # Bookmark posts
    user = state["currentUser"]
    for post_id in ["post_01", "post_03", "post_11", "post_13"]:
        post = find_post(state, post_id)
        post["bookmarked"] = True
        if post_id not in user["savedPostIds"]:
            user["savedPostIds"].append(post_id)


def solve_task_h41(state):
    """Mark Kevin O'Brien's Q&A answer helpful (most-liked student post → ans_09)."""
    q = find_question(state, "qa_06")
    ans = find_entity(q["answers"], id="ans_09")
    ans["helpful"] = ans["helpful"] + 1


def solve_task_h42(state):
    """Read unread top-match messages + save all active jobs from those employers."""
    for msg_id in ["msg_01", "msg_03", "msg_08"]:
        msg = find_message(state, msg_id)
        msg["isRead"] = True
    user = state["currentUser"]
    for jid in ["job_01", "job_02", "job_22", "job_06", "job_25", "job_26"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)


def solve_task_h43(state):
    """RSVP Google event + bookmark Google post (most active job listings)."""
    evt = find_event(state, "evt_04")
    evt["rsvped"] = True
    evt["rsvpCount"] = evt["rsvpCount"] + 1
    post = find_post(state, "post_01")
    post["bookmarked"] = True
    user = state["currentUser"]
    if "post_01" not in user["savedPostIds"]:
        user["savedPostIds"].append("post_01")


def solve_task_h44(state):
    """Save all active FT jobs, unsave all seed internships."""
    user = state["currentUser"]
    user["savedJobIds"] = [
        jid for jid in user["savedJobIds"]
        if jid not in ("job_03", "job_07", "job_12", "job_18", "job_24")
    ]
    for jid in ["job_16", "job_17", "job_20", "job_21", "job_27", "job_28"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)


def solve_task_h45(state):
    """Like + bookmark Jordan Taylor's post (salary Q&A most helpful → post_12)."""
    post = find_post(state, "post_12")
    post["likes"] = post["likes"] + 1
    post["bookmarked"] = True
    user = state["currentUser"]
    if "post_12" not in user["savedPostIds"]:
        user["savedPostIds"].append("post_12")


def solve_task_h46(state):
    """Mark David Lee's Q&A answer helpful (ans_10) + like his post (post_14)."""
    q = find_question(state, "qa_07")
    ans = find_entity(q["answers"], id="ans_10")
    ans["helpful"] = ans["helpful"] + 1
    post = find_post(state, "post_14")
    post["likes"] = post["likes"] + 1


def solve_task_h47(state):
    """Add Fellowship/Gap year to postGraduation, Exploring to helpWith, grad Dec 2026."""
    ci = state["currentUser"]["careerInterests"]
    if "Fellowship" not in ci["postGraduation"]:
        ci["postGraduation"].append("Fellowship")
    if "Gap year" not in ci["postGraduation"]:
        ci["postGraduation"].append("Gap year")
    if "Exploring" not in ci["helpWith"]:
        ci["helpWith"].append("Exploring")
    ci["expectedGraduationDate"] = "December 2026"


def solve_task_h48(state):
    """RSVP Anthropic event + save job_29 (phone screen message → Anthropic)."""
    evt = find_event(state, "evt_06")
    evt["rsvped"] = True
    evt["rsvpCount"] = evt["rsvpCount"] + 1
    user = state["currentUser"]
    if "job_29" not in user["savedJobIds"]:
        user["savedJobIds"].append("job_29")


def solve_task_h49(state):
    """Save active jobs from on-campus event host employers."""
    user = state["currentUser"]
    for jid in ["job_01", "job_02", "job_05", "job_22", "job_27"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)


def solve_task_h50(state):
    """Comment on FAANG study plan (post_08) + bookmark PM book post (post_18)."""
    post_08 = find_post(state, "post_08")
    comment_id = "cmt_" + str(state["_nextCommentId"])
    state["_nextCommentId"] += 1
    post_08["comments"].append({
        "id": comment_id,
        "authorName": state["currentUser"]["fullName"],
        "authorSchool": state["currentUser"]["school"],
        "authorAvatarColor": state["currentUser"]["avatarColor"],
        "text": "Great study plan! How long did your preparation timeline look like?",
        "createdAt": "2026-03-07T12:00:00Z",
        "isAnonymous": False,
    })
    post_18 = find_post(state, "post_18")
    post_18["bookmarked"] = True
    user = state["currentUser"]
    if "post_18" not in user["savedPostIds"]:
        user["savedPostIds"].append("post_18")


def solve_task_h51(state):
    """Save Meta's unsaved job + RSVP Meta event + like Meta post."""
    user = state["currentUser"]
    if "job_26" not in user["savedJobIds"]:
        user["savedJobIds"].append("job_26")
    evt = find_event(state, "evt_02")
    evt["rsvped"] = True
    evt["rsvpCount"] = evt["rsvpCount"] + 1
    post = find_post(state, "post_03")
    post["likes"] = post["likes"] + 1


def solve_task_h52(state):
    """Remove closed job_03, follow employers of remaining saved jobs."""
    user = state["currentUser"]
    user["savedJobIds"] = [jid for jid in user["savedJobIds"] if jid != "job_03"]
    for emp_id in ["emp_16", "emp_09"]:
        if emp_id not in user["followedEmployerIds"]:
            user["followedEmployerIds"].append(emp_id)
            emp = find_employer(state, emp_id)
            emp["followCount"] = emp["followCount"] + 1


def solve_task_h53(state):
    """Follow TFA (nonprofit) + save job_20 + like post_17."""
    user = state["currentUser"]
    if "emp_18" not in user["followedEmployerIds"]:
        user["followedEmployerIds"].append("emp_18")
        emp = find_employer(state, "emp_18")
        emp["followCount"] = emp["followCount"] + 1
    if "job_20" not in user["savedJobIds"]:
        user["savedJobIds"].append("job_20")
    post = find_post(state, "post_17")
    post["likes"] = post["likes"] + 1


def solve_task_h54(state):
    """Like employer posts for AI/ML labeled jobs: post_03, post_05, post_11."""
    for post_id in ["post_03", "post_05", "post_11"]:
        post = find_post(state, post_id)
        post["likes"] = post["likes"] + 1


def solve_task_h55(state):
    """Like Emma Rodriguez's post (post_10) + mark her Q&A answer helpful (ans_06)."""
    post = find_post(state, "post_10")
    post["likes"] = post["likes"] + 1
    q = find_question(state, "qa_04")
    ans = find_entity(q["answers"], id="ans_06")
    ans["helpful"] = ans["helpful"] + 1


def solve_task_h56(state):
    """Save all active jobs in Seattle or New York."""
    user = state["currentUser"]
    for jid in ["job_08", "job_15", "job_24", "job_27", "job_28"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)


def solve_task_h57(state):
    """Submit answer to qa_05 (salary negotiation) — discovered via Jordan Taylor."""
    q = find_question(state, "qa_05")
    ans_id = "ans_" + str(state["_nextAnswerId"]).zfill(2)
    state["_nextAnswerId"] += 1
    q["answers"].append({
        "id": ans_id,
        "authorName": "Maya Chen",
        "authorSchool": state["currentUser"]["school"],
        "authorMajor": state["currentUser"]["major"],
        "authorGradYear": state["currentUser"]["graduationYear"],
        "authorAvatarColor": state["currentUser"]["avatarColor"],
        "text": "From my experience, always negotiate. Research market rates and have data to support your ask.",
        "visibility": "full",
        "status": "pending",
        "createdAt": "2026-03-07T12:00:00Z",
        "helpful": 0,
    })


def solve_task_h58(state):
    """Set visibility Private, add Military to postGraduation, remove Remote from locations."""
    state["currentUser"]["profileVisibility"] = "Private"
    ci = state["currentUser"]["careerInterests"]
    if "Military" not in ci["postGraduation"]:
        ci["postGraduation"].append("Military")
    ci["locations"] = [loc for loc in ci["locations"] if loc != "Remote"]


def solve_task_h59(state):
    """Like all student posts with > 300 likes: post_08, post_12, post_16."""
    for post_id in ["post_08", "post_12", "post_16"]:
        post = find_post(state, post_id)
        post["likes"] = post["likes"] + 1


def solve_task_h60(state):
    """Follow unfollowed Tech employers + save their active internships."""
    user = state["currentUser"]
    for emp_id in ["emp_09", "emp_17", "emp_19", "emp_20"]:
        if emp_id not in user["followedEmployerIds"]:
            user["followedEmployerIds"].append(emp_id)
            emp = find_employer(state, emp_id)
            emp["followCount"] = emp["followCount"] + 1
    for jid in ["job_08", "job_19", "job_24", "job_30"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)


# === HARDENING ROUND 2 ===

def solve_task_h61(state):
    """RSVP McKinsey event (evt_01) + schedule case interview prep with David Kim."""
    evt = find_event(state, "evt_01")
    evt["rsvped"] = True
    evt["rsvpCount"] = evt["rsvpCount"] + 1
    appt_id = "appt_" + str(state["_nextAppointmentId"]).zfill(2)
    state["_nextAppointmentId"] += 1
    state["appointments"].append({
        "id": appt_id,
        "category": "Interview Preparation",
        "type": "Case Interview Prep",
        "staffId": "staff_04",
        "staffName": "David Kim",
        "date": "2026-03-17",
        "time": "3:00 PM",
        "duration": 60,
        "medium": "Virtual on Handshake",
        "location": None,
        "status": "requested",
        "details": "",
        "comments": [],
        "createdAt": "2026-03-07T12:00:00Z",
    })


def solve_task_h62(state):
    """Save active jobs from non-followed message senders."""
    user = state["currentUser"]
    for jid in ["job_05", "job_08", "job_17", "job_24", "job_27", "job_30"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)


def solve_task_h63(state):
    """Follow Startup Grind Labs (emp_20, fewest followers) + save job_21."""
    user = state["currentUser"]
    if "emp_20" not in user["followedEmployerIds"]:
        user["followedEmployerIds"].append("emp_20")
        emp = find_employer(state, "emp_20")
        emp["followCount"] = emp["followCount"] + 1
    if "job_21" not in user["savedJobIds"]:
        user["savedJobIds"].append("job_21")


def solve_task_h64(state):
    """Unsave jobs from non-CA employers: job_03 (NY), job_18 (OR), job_24 (WA)."""
    user = state["currentUser"]
    user["savedJobIds"] = [
        jid for jid in user["savedJobIds"]
        if jid not in ("job_03", "job_18", "job_24")
    ]


def solve_task_h65(state):
    """Like Marcus Johnson's post (post_04) + save Stripe job (job_09)."""
    post = find_post(state, "post_04")
    post["likes"] = post["likes"] + 1
    user = state["currentUser"]
    if "job_09" not in user["savedJobIds"]:
        user["savedJobIds"].append("job_09")


def solve_task_h66(state):
    """Healthcare career pivot."""
    ci = state["currentUser"]["careerInterests"]
    ci["careerCommunity"] = "Healthcare"
    ci["roles"] = ["Solutions Architect", "Research Scientist"]
    ci["industries"] = ["Healthcare Technology", "Biotechnology"]
    if "Supply Chain" not in ci["jobFunctions"]:
        ci["jobFunctions"].append("Supply Chain")


def solve_task_h67(state):
    """Comment on Emma Rodriguez's post (post_10) - fewest helpful Q&A answer."""
    post = find_post(state, "post_10")
    comment_id = "cmt_" + str(state["_nextCommentId"])
    state["_nextCommentId"] += 1
    post["comments"].append({
        "id": comment_id,
        "authorName": state["currentUser"]["fullName"],
        "authorSchool": state["currentUser"]["school"],
        "authorAvatarColor": state["currentUser"]["avatarColor"],
        "text": "Great Q&A advice, Emma! Your tips about virtual career fairs were really helpful.",
        "createdAt": "2026-03-07T12:00:00Z",
        "isAnonymous": False,
    })


def solve_task_h68(state):
    """Like all posts from publicly-traded employers."""
    for post_id in ["post_01", "post_03", "post_07", "post_11", "post_15", "post_19"]:
        post = find_post(state, post_id)
        post["likes"] = post["likes"] + 1


def solve_task_h69(state):
    """Comment on all saved posts (post_02, post_08, post_14)."""
    for post_id in ["post_02", "post_08", "post_14"]:
        post = find_post(state, post_id)
        comment_id = "cmt_" + str(state["_nextCommentId"])
        state["_nextCommentId"] += 1
        post["comments"].append({
            "id": comment_id,
            "authorName": state["currentUser"]["fullName"],
            "authorSchool": state["currentUser"]["school"],
            "authorAvatarColor": state["currentUser"]["avatarColor"],
            "text": "Thanks for sharing your insight! Really appreciate it.",
            "createdAt": "2026-03-07T12:00:00Z",
            "isAnonymous": False,
        })


def solve_task_h70(state):
    """Save Stripe internship (job_09) + bookmark Stripe post (post_13)."""
    user = state["currentUser"]
    if "job_09" not in user["savedJobIds"]:
        user["savedJobIds"].append("job_09")
    post = find_post(state, "post_13")
    post["bookmarked"] = True
    if "post_13" not in user["savedPostIds"]:
        user["savedPostIds"].append("post_13")


def solve_task_h71(state):
    """RSVP all employer events + save their active unsaved jobs."""
    for evt_id in ["evt_01", "evt_02", "evt_04", "evt_06", "evt_08", "evt_10"]:
        evt = find_event(state, evt_id)
        evt["rsvped"] = True
        evt["rsvpCount"] = evt["rsvpCount"] + 1
    user = state["currentUser"]
    for jid in ["job_01", "job_02", "job_05", "job_17", "job_22", "job_26",
                "job_27", "job_29", "job_30"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)


def solve_task_h72(state):
    """Schedule personal statement review with Maria Rodriguez + post Q&A question."""
    appt_id = "appt_" + str(state["_nextAppointmentId"]).zfill(2)
    state["_nextAppointmentId"] += 1
    state["appointments"].append({
        "id": appt_id,
        "category": "Graduate School",
        "type": "Personal Statement Review",
        "staffId": "staff_03",
        "staffName": "Maria Rodriguez",
        "date": "2026-03-28",
        "time": "11:00 AM",
        "duration": 30,
        "medium": "In Person",
        "location": "Career Center",
        "status": "requested",
        "details": "",
        "comments": [],
        "createdAt": "2026-03-07T12:00:00Z",
    })
    q_id = "qa_" + str(state["_nextQuestionId"]).zfill(2)
    state["_nextQuestionId"] += 1
    state["qaQuestions"].insert(0, {
        "id": q_id,
        "authorName": "Maya Chen",
        "authorSchool": state["currentUser"]["school"],
        "authorMajor": state["currentUser"]["major"],
        "authorGradYear": state["currentUser"]["graduationYear"],
        "authorAvatarColor": state["currentUser"]["avatarColor"],
        "question": "What is the typical timeline for grad school applications in computer science? When should I start preparing?",
        "status": "pending",
        "createdAt": "2026-03-07T12:00:00Z",
        "views": 0,
        "answers": [],
    })


def solve_task_h73(state):
    """Read Stripe message (msg_06) + like Marcus Johnson's post (post_04)."""
    msg = find_message(state, "msg_06")
    msg["isRead"] = True
    post = find_post(state, "post_04")
    post["likes"] = post["likes"] + 1


def solve_task_h74(state):
    """Like Jordan Taylor's post (post_12) + save job_21 (fewest applicant startup)."""
    post = find_post(state, "post_12")
    post["likes"] = post["likes"] + 1
    user = state["currentUser"]
    if "job_21" not in user["savedJobIds"]:
        user["savedJobIds"].append("job_21")


def solve_task_h75(state):
    """Cancel appt_02 + reschedule Mock Interview - Technical with David Kim."""
    appt = find_appointment(state, "appt_02")
    appt["status"] = "cancelled"
    appt_id = "appt_" + str(state["_nextAppointmentId"]).zfill(2)
    state["_nextAppointmentId"] += 1
    state["appointments"].append({
        "id": appt_id,
        "category": "Interview Preparation",
        "type": "Mock Interview - Technical",
        "staffId": "staff_04",
        "staffName": "David Kim",
        "date": "2026-03-25",
        "time": "11:00 AM",
        "duration": 60,
        "medium": "Virtual on Handshake",
        "location": None,
        "status": "requested",
        "details": "",
        "comments": [],
        "createdAt": "2026-03-07T12:00:00Z",
    })


def solve_task_h76(state):
    """Bookmark tech talk host posts: post_01 (Google) + post_05 (Anthropic)."""
    user = state["currentUser"]
    for post_id in ["post_01", "post_05"]:
        post = find_post(state, post_id)
        post["bookmarked"] = True
        if post_id not in user["savedPostIds"]:
            user["savedPostIds"].append(post_id)


def solve_task_h77(state):
    """Set visibility Limited, phone, add Volunteering, create school post."""
    state["currentUser"]["profileVisibility"] = "Limited"
    state["currentUser"]["phone"] = "(650) 555-0300"
    ci = state["currentUser"]["careerInterests"]
    if "Volunteering" not in ci["postGraduation"]:
        ci["postGraduation"].append("Volunteering")
    post_id = "post_" + str(state["_nextPostId"])
    state["_nextPostId"] += 1
    state["feedPosts"].insert(0, {
        "id": post_id,
        "authorType": "student",
        "authorId": state["currentUser"]["id"],
        "authorName": state["currentUser"]["fullName"],
        "authorSchool": state["currentUser"]["school"],
        "authorAvatarColor": state["currentUser"]["avatarColor"],
        "content": "Looking for volunteer opportunities over the summer! If anyone knows of programs or orgs accepting volunteers, please share.",
        "audience": "school",
        "likes": 0,
        "comments": [],
        "hasImage": False,
        "hasVideo": False,
        "createdAt": "2026-03-07T12:00:00Z",
        "bookmarked": False,
    })


def solve_task_h78(state):
    """Save Apple's unsaved jobs (job_06, job_25) + like Apple's post (post_11)."""
    user = state["currentUser"]
    for jid in ["job_06", "job_25"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)
    post = find_post(state, "post_11")
    post["likes"] = post["likes"] + 1


def solve_task_h79(state):
    """Like all non-Stanford student posts."""
    for post_id in ["post_04", "post_06", "post_08", "post_12",
                    "post_14", "post_16", "post_18", "post_20"]:
        post = find_post(state, post_id)
        post["likes"] = post["likes"] + 1


def solve_task_h80(state):
    """Follow 10K+ employers not followed + save their active internships."""
    user = state["currentUser"]
    for emp_id in ["emp_02", "emp_06", "emp_08", "emp_09", "emp_16", "emp_19"]:
        if emp_id not in user["followedEmployerIds"]:
            user["followedEmployerIds"].append(emp_id)
            emp = find_employer(state, emp_id)
            emp["followCount"] = emp["followCount"] + 1
    for jid in ["job_08", "job_11", "job_30"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)


# === HARDENING ROUND 3 ===

def solve_task_h81(state):
    """Read Google top-match msg, save Google jobs, RSVP tech talk, bookmark post."""
    msg = find_message(state, "msg_01")
    msg["isRead"] = True
    user = state["currentUser"]
    for jid in ["job_01", "job_02", "job_22"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)
    evt = find_event(state, "evt_04")
    evt["rsvped"] = True
    evt["rsvpCount"] = evt["rsvpCount"] + 1
    post = find_post(state, "post_01")
    post["bookmarked"] = True
    if "post_01" not in user["savedPostIds"]:
        user["savedPostIds"].append("post_01")


def solve_task_h82(state):
    """Comment on appt_01 + schedule LinkedIn Profile Review with Michael Okafor."""
    appt = find_appointment(state, "appt_01")
    appt["comments"].append({
        "author": state["currentUser"]["fullName"],
        "text": "Could you also help with my LinkedIn headline during our session?",
        "createdAt": "2026-03-07T12:00:00Z",
    })
    appt_id = "appt_" + str(state["_nextAppointmentId"]).zfill(2)
    state["_nextAppointmentId"] += 1
    state["appointments"].append({
        "id": appt_id,
        "category": "Resume & Cover Letter",
        "type": "LinkedIn Profile Review",
        "staffId": "staff_06",
        "staffName": "Michael Okafor",
        "date": "2026-03-14",
        "time": "9:00 AM",
        "duration": 30,
        "medium": "In Person",
        "location": "Career Center",
        "status": "requested",
        "details": "",
        "comments": [],
        "createdAt": "2026-03-07T12:00:00Z",
    })


def solve_task_h83(state):
    """Add Full-time to job types, save active FT jobs from Technology employers."""
    ci = state["currentUser"]["careerInterests"]
    if "Full-time" not in ci["jobTypes"]:
        ci["jobTypes"].append("Full-time")
    user = state["currentUser"]
    for jid in ["job_17", "job_21"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)


def solve_task_h84(state):
    """Follow employers who messaged but have no upcoming events: Amazon, Bain."""
    user = state["currentUser"]
    for emp_id in ["emp_09", "emp_11"]:
        if emp_id not in user["followedEmployerIds"]:
            user["followedEmployerIds"].append(emp_id)
            emp = find_employer(state, emp_id)
            emp["followCount"] = emp["followCount"] + 1


def solve_task_h85(state):
    """Submit answer to qa_06 (Kevin O'Brien's system design Q) + like post_08."""
    q = find_question(state, "qa_06")
    ans_id = "ans_" + str(state["_nextAnswerId"]).zfill(2)
    state["_nextAnswerId"] += 1
    q["answers"].append({
        "id": ans_id,
        "authorName": "Maya Chen",
        "authorSchool": state["currentUser"]["school"],
        "authorMajor": state["currentUser"]["major"],
        "authorGradYear": state["currentUser"]["graduationYear"],
        "authorAvatarColor": state["currentUser"]["avatarColor"],
        "text": "I recommend the System Design Primer on GitHub and Designing Data-Intensive Applications. Practice with mock interviews too!",
        "visibility": "full",
        "status": "pending",
        "createdAt": "2026-03-07T12:00:00Z",
        "helpful": 0,
    })
    post = find_post(state, "post_08")
    post["likes"] = post["likes"] + 1


def solve_task_h86(state):
    """RSVP in-person employer events + save one job from each host."""
    for evt_id in ["evt_01", "evt_04", "evt_08"]:
        evt = find_event(state, evt_id)
        evt["rsvped"] = True
        evt["rsvpCount"] = evt["rsvpCount"] + 1
    user = state["currentUser"]
    for jid in ["job_05", "job_01", "job_27"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)


def solve_task_h87(state):
    """East Coast focus: locations = NY only, unfollow CA employers."""
    state["currentUser"]["careerInterests"]["locations"] = ["New York, NY"]
    user = state["currentUser"]
    for emp_id in ["emp_01", "emp_05", "emp_07", "emp_10", "emp_15"]:
        if emp_id in user["followedEmployerIds"]:
            user["followedEmployerIds"].remove(emp_id)
            emp = find_employer(state, emp_id)
            emp["followCount"] = emp["followCount"] - 1


def solve_task_h88(state):
    """Apple (most followers): like + bookmark post_11, save job_06 + job_25."""
    post = find_post(state, "post_11")
    post["likes"] = post["likes"] + 1
    post["bookmarked"] = True
    user = state["currentUser"]
    if "post_11" not in user["savedPostIds"]:
        user["savedPostIds"].append("post_11")
    for jid in ["job_06", "job_25"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)


def solve_task_h89(state):
    """Read unread top-match msgs, RSVP Google+Meta events, save their unsaved jobs."""
    for msg_id in ["msg_01", "msg_03", "msg_08"]:
        msg = find_message(state, msg_id)
        msg["isRead"] = True
    evt_02 = find_event(state, "evt_02")
    evt_02["rsvped"] = True
    evt_02["rsvpCount"] = evt_02["rsvpCount"] + 1
    evt_04 = find_event(state, "evt_04")
    evt_04["rsvped"] = True
    evt_04["rsvpCount"] = evt_04["rsvpCount"] + 1
    user = state["currentUser"]
    for jid in ["job_01", "job_02", "job_22", "job_26"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)


def solve_task_h90(state):
    """Submit answer to qa_11 (diversity programs) + bookmark post_06 (NSBE)."""
    q = find_question(state, "qa_11")
    ans_id = "ans_" + str(state["_nextAnswerId"]).zfill(2)
    state["_nextAnswerId"] += 1
    q["answers"].append({
        "id": ans_id,
        "authorName": "Maya Chen",
        "authorSchool": state["currentUser"]["school"],
        "authorMajor": state["currentUser"]["major"],
        "authorGradYear": state["currentUser"]["graduationYear"],
        "authorAvatarColor": state["currentUser"]["avatarColor"],
        "text": "I've also found Handshake's diversity filters helpful. Programs like Google STEP and Microsoft Explore are great for underrepresented students.",
        "visibility": "full",
        "status": "pending",
        "createdAt": "2026-03-07T12:00:00Z",
        "helpful": 0,
    })
    post = find_post(state, "post_06")
    post["bookmarked"] = True
    user = state["currentUser"]
    if "post_06" not in user["savedPostIds"]:
        user["savedPostIds"].append("post_06")


def solve_task_h91(state):
    """Schedule advising with Dr. Williams + comment on completed Jan appointment."""
    appt_id = "appt_" + str(state["_nextAppointmentId"]).zfill(2)
    state["_nextAppointmentId"] += 1
    state["appointments"].append({
        "id": appt_id,
        "category": "Career Counseling",
        "type": "General Career Advising",
        "staffId": "staff_01",
        "staffName": "Dr. Patricia Williams",
        "date": "2026-03-19",
        "time": "1:00 PM",
        "duration": 45,
        "medium": "Virtual on Handshake",
        "location": None,
        "status": "requested",
        "details": "",
        "comments": [],
        "createdAt": "2026-03-07T12:00:00Z",
    })
    appt = find_appointment(state, "appt_04")
    appt["comments"].append({
        "author": state["currentUser"]["fullName"],
        "text": "I followed your advice about applying broadly and submitted applications to over 20 companies!",
        "createdAt": "2026-03-07T12:00:00Z",
    })


def solve_task_h92(state):
    """Save Microsoft jobs + comment on Imagine Cup + add Cloud Engineer role."""
    user = state["currentUser"]
    for jid in ["job_04", "job_23"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)
    post = find_post(state, "post_19")
    comment_id = "cmt_" + str(state["_nextCommentId"])
    state["_nextCommentId"] += 1
    post["comments"].append({
        "id": comment_id,
        "authorName": state["currentUser"]["fullName"],
        "authorSchool": state["currentUser"]["school"],
        "authorAvatarColor": state["currentUser"]["avatarColor"],
        "text": "I'm very interested in participating in Imagine Cup! Looking for teammates.",
        "createdAt": "2026-03-07T12:00:00Z",
        "isAnonymous": False,
    })
    ci = state["currentUser"]["careerInterests"]
    if "Cloud Engineer" not in ci["roles"]:
        ci["roles"].append("Cloud Engineer")


def solve_task_h93(state):
    """CA-only locations + save all active CA internships."""
    state["currentUser"]["careerInterests"]["locations"] = [
        "San Francisco, CA", "San Jose, CA", "Los Angeles, CA"
    ]
    user = state["currentUser"]
    for jid in ["job_01", "job_02", "job_06", "job_07", "job_09", "job_12",
                "job_22", "job_25", "job_26", "job_29", "job_30"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)


def solve_task_h94(state):
    """Like all student posts from Q&A answerers."""
    for post_id in ["post_08", "post_04", "post_12", "post_10",
                    "post_06", "post_16", "post_14"]:
        post = find_post(state, post_id)
        post["likes"] = post["likes"] + 1


def solve_task_h95(state):
    """Remove closed job_03, save active JPMorgan job_27."""
    user = state["currentUser"]
    user["savedJobIds"] = [jid for jid in user["savedJobIds"] if jid != "job_03"]
    if "job_27" not in user["savedJobIds"]:
        user["savedJobIds"].append("job_27")


def solve_task_h96(state):
    """Save Microsoft jobs + like Imagine Cup post + add IT & Infrastructure."""
    user = state["currentUser"]
    for jid in ["job_04", "job_23"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)
    post = find_post(state, "post_19")
    post["likes"] = post["likes"] + 1
    ci = state["currentUser"]["careerInterests"]
    if "IT & Infrastructure" not in ci["jobFunctions"]:
        ci["jobFunctions"].append("IT & Infrastructure")


def solve_task_h97(state):
    """Mark ans_07 helpful + submit own answer to qa_05 (most viewed)."""
    q05 = find_question(state, "qa_05")
    ans07 = find_entity(q05["answers"], id="ans_07")
    ans07["helpful"] = ans07["helpful"] + 1
    ans_id = "ans_" + str(state["_nextAnswerId"]).zfill(2)
    state["_nextAnswerId"] += 1
    q05["answers"].append({
        "id": ans_id,
        "authorName": "Maya Chen",
        "authorSchool": state["currentUser"]["school"],
        "authorMajor": state["currentUser"]["major"],
        "authorGradYear": state["currentUser"]["graduationYear"],
        "authorAvatarColor": state["currentUser"]["avatarColor"],
        "text": "Always negotiate! Research the market rate on Levels.fyi and have competing offers ready if possible.",
        "visibility": "full",
        "status": "pending",
        "createdAt": "2026-03-07T12:00:00Z",
        "helpful": 0,
    })


def solve_task_h98(state):
    """Unfollow non-Tech/AI employers (Tesla) + save all remaining followed internships."""
    user = state["currentUser"]
    if "emp_12" in user["followedEmployerIds"]:
        user["followedEmployerIds"].remove("emp_12")
        emp = find_employer(state, "emp_12")
        emp["followCount"] = emp["followCount"] - 1
    for jid in ["job_01", "job_02", "job_04", "job_06", "job_09",
                "job_22", "job_23", "job_25", "job_26", "job_29"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)


def solve_task_h99(state):
    """Read Stripe msg + save Stripe job + comment on Stripe post + add Backend Developer."""
    msg = find_message(state, "msg_06")
    msg["isRead"] = True
    user = state["currentUser"]
    if "job_09" not in user["savedJobIds"]:
        user["savedJobIds"].append("job_09")
    post = find_post(state, "post_13")
    comment_id = "cmt_" + str(state["_nextCommentId"])
    state["_nextCommentId"] += 1
    post["comments"].append({
        "id": comment_id,
        "authorName": state["currentUser"]["fullName"],
        "authorSchool": state["currentUser"]["school"],
        "authorAvatarColor": state["currentUser"]["avatarColor"],
        "text": "Fascinating post about distributed systems architecture! I'd love to learn more about working at Stripe.",
        "createdAt": "2026-03-07T12:00:00Z",
        "isAnonymous": False,
    })
    ci = state["currentUser"]["careerInterests"]
    if "Backend Developer" not in ci["roles"]:
        ci["roles"].append("Backend Developer")


def solve_task_h100(state):
    """Cancel both requested appts + schedule behavioral mock + update phone + school post."""
    for appt_id in ["appt_02", "appt_08"]:
        appt = find_appointment(state, appt_id)
        appt["status"] = "cancelled"
    appt_id = "appt_" + str(state["_nextAppointmentId"]).zfill(2)
    state["_nextAppointmentId"] += 1
    state["appointments"].append({
        "id": appt_id,
        "category": "Interview Preparation",
        "type": "Mock Interview - Behavioral",
        "staffId": "staff_04",
        "staffName": "David Kim",
        "date": "2026-03-21",
        "time": "3:00 PM",
        "duration": 60,
        "medium": "In Person",
        "location": "Career Center",
        "status": "requested",
        "details": "",
        "comments": [],
        "createdAt": "2026-03-07T12:00:00Z",
    })
    state["currentUser"]["phone"] = "(650) 555-0250"
    post_id = "post_" + str(state["_nextPostId"])
    state["_nextPostId"] += 1
    state["feedPosts"].insert(0, {
        "id": post_id,
        "authorType": "student",
        "authorId": state["currentUser"]["id"],
        "authorName": state["currentUser"]["fullName"],
        "authorSchool": state["currentUser"]["school"],
        "authorAvatarColor": state["currentUser"]["avatarColor"],
        "content": "Rescheduled my career center appointments and preparing for upcoming interviews! Time to practice behavioral questions.",
        "audience": "school",
        "likes": 0,
        "comments": [],
        "hasImage": False,
        "hasVideo": False,
        "createdAt": "2026-03-07T12:00:00Z",
        "bookmarked": False,
    })


# === HARDENING ROUND 4 ===

def solve_task_h101(state):
    """Save Amazon jobs + like Amazon post. Discovery: Twitch → Amazon."""
    user = state["currentUser"]
    for jid in ["job_08", "job_24"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)
    post = find_post(state, "post_07")
    post["likes"] = post["likes"] + 1


def solve_task_h102(state):
    """Bookmark student posts < 200 likes, like student posts >= 200 likes."""
    user = state["currentUser"]
    # Bookmark < 200
    for post_id in ["post_02", "post_04", "post_10", "post_20"]:
        post = find_post(state, post_id)
        post["bookmarked"] = True
        if post_id not in user["savedPostIds"]:
            user["savedPostIds"].append(post_id)
    # Like >= 200
    for post_id in ["post_06", "post_08", "post_12", "post_14", "post_16", "post_18"]:
        post = find_post(state, post_id)
        post["likes"] = post["likes"] + 1


def solve_task_h103(state):
    """Schedule Professional Branding with Michael Okafor (discovered from appt_01)."""
    appt_id = "appt_" + str(state["_nextAppointmentId"]).zfill(2)
    state["_nextAppointmentId"] += 1
    state["appointments"].append({
        "id": appt_id,
        "category": "Networking & Professional Development",
        "type": "Professional Branding",
        "staffId": "staff_06",
        "staffName": "Michael Okafor",
        "date": "2026-03-18",
        "time": "2:00 PM",
        "duration": 30,
        "medium": "Virtual on Handshake",
        "location": None,
        "status": "requested",
        "details": "",
        "comments": [],
        "createdAt": "2026-03-07T12:00:00Z",
    })


def solve_task_h104(state):
    """RSVP Salesforce event + follow Salesforce. Discovery: Tableau → Salesforce."""
    evt = find_event(state, "evt_10")
    evt["rsvped"] = True
    evt["rsvpCount"] = evt["rsvpCount"] + 1
    user = state["currentUser"]
    if "emp_19" not in user["followedEmployerIds"]:
        user["followedEmployerIds"].append("emp_19")
        emp = find_employer(state, "emp_19")
        emp["followCount"] = emp["followCount"] + 1


def solve_task_h105(state):
    """Mark ans_02 helpful on qa_01 (2nd most viewed, fewer helpful votes)."""
    q = find_question(state, "qa_01")
    ans = find_entity(q["answers"], id="ans_02")
    ans["helpful"] = ans["helpful"] + 1


def solve_task_h106(state):
    """Save active internships >= $50/hr from unfollowed employers."""
    user = state["currentUser"]
    for jid in ["job_08", "job_19", "job_24"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)


def solve_task_h107(state):
    """RSVP both Tech Talks + save all jobs from hosts (Google, Anthropic)."""
    for evt_id in ["evt_04", "evt_06"]:
        evt = find_event(state, evt_id)
        evt["rsvped"] = True
        evt["rsvpCount"] = evt["rsvpCount"] + 1
    user = state["currentUser"]
    for jid in ["job_01", "job_02", "job_22", "job_12", "job_29"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)


def solve_task_h108(state):
    """Follow McKinsey + RSVP evt_01 + bookmark post_09. Most applicants: job_05."""
    user = state["currentUser"]
    if "emp_04" not in user["followedEmployerIds"]:
        user["followedEmployerIds"].append("emp_04")
        emp = find_employer(state, "emp_04")
        emp["followCount"] = emp["followCount"] + 1
    evt = find_event(state, "evt_01")
    evt["rsvped"] = True
    evt["rsvpCount"] = evt["rsvpCount"] + 1
    post = find_post(state, "post_09")
    post["bookmarked"] = True
    if "post_09" not in user["savedPostIds"]:
        user["savedPostIds"].append("post_09")


def solve_task_h109(state):
    """Mark Marcus Johnson's Q&A answer (ans_12) helpful + read Stripe msg (msg_06)."""
    q = find_question(state, "qa_09")
    ans = find_entity(q["answers"], id="ans_12")
    ans["helpful"] = ans["helpful"] + 1
    msg = find_message(state, "msg_06")
    msg["isRead"] = True


def solve_task_h110(state):
    """Save FT Finance jobs (job_27, job_28) + follow Finance employers."""
    user = state["currentUser"]
    for jid in ["job_27", "job_28"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)
    for emp_id in ["emp_02", "emp_06"]:
        if emp_id not in user["followedEmployerIds"]:
            user["followedEmployerIds"].append(emp_id)
            emp = find_employer(state, emp_id)
            emp["followCount"] = emp["followCount"] + 1


def solve_task_h111(state):
    """Follow unfollowed private companies + save their active FT jobs."""
    user = state["currentUser"]
    for emp_id in ["emp_04", "emp_08", "emp_11", "emp_14", "emp_20"]:
        if emp_id not in user["followedEmployerIds"]:
            user["followedEmployerIds"].append(emp_id)
            emp = find_employer(state, emp_id)
            emp["followCount"] = emp["followCount"] + 1
    for jid in ["job_16", "job_21"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)


def solve_task_h112(state):
    """Like Kevin O'Brien's post_08 + answer qa_03. Discovery: qa_03 author = post_08 author."""
    post = find_post(state, "post_08")
    post["likes"] = post["likes"] + 1
    q = find_question(state, "qa_03")
    ans_id = "ans_" + str(state["_nextAnswerId"]).zfill(2)
    state["_nextAnswerId"] += 1
    q["answers"].append({
        "id": ans_id,
        "authorName": "Maya Chen",
        "authorSchool": state["currentUser"]["school"],
        "authorMajor": state["currentUser"]["major"],
        "authorGradYear": state["currentUser"]["graduationYear"],
        "authorAvatarColor": state["currentUser"]["avatarColor"],
        "text": "A consulting internship can be valuable for building analytical skills that transfer to tech, especially for PM roles.",
        "visibility": "full",
        "status": "pending",
        "createdAt": "2026-03-07T12:00:00Z",
        "helpful": 0,
    })


def solve_task_h113(state):
    """Like Amazon post_07 + save internships. 2nd highest followers: Amazon."""
    post = find_post(state, "post_07")
    post["likes"] = post["likes"] + 1
    user = state["currentUser"]
    for jid in ["job_08", "job_24"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)


def solve_task_h114(state):
    """Create post about informational interviews + schedule networking with James Chen."""
    post_id = "post_" + str(state["_nextPostId"])
    state["_nextPostId"] += 1
    state["feedPosts"].insert(0, {
        "id": post_id,
        "authorType": "student",
        "authorId": state["currentUser"]["id"],
        "authorName": state["currentUser"]["fullName"],
        "authorSchool": state["currentUser"]["school"],
        "authorAvatarColor": state["currentUser"]["avatarColor"],
        "content": "Informational interviews are one of the most underrated tools for career exploration. Reach out to alumni and professionals to learn about their roles and industries!",
        "audience": "everyone",
        "likes": 0,
        "comments": [],
        "hasImage": False,
        "hasVideo": False,
        "createdAt": "2026-03-07T12:00:00Z",
        "bookmarked": False,
    })
    appt_id = "appt_" + str(state["_nextAppointmentId"]).zfill(2)
    state["_nextAppointmentId"] += 1
    state["appointments"].append({
        "id": appt_id,
        "category": "Networking & Professional Development",
        "type": "Networking Strategy",
        "staffId": "staff_02",
        "staffName": "James Chen",
        "date": "2026-03-20",
        "time": "2:00 PM",
        "duration": 30,
        "medium": "Virtual on Handshake",
        "location": None,
        "status": "requested",
        "details": "",
        "comments": [],
        "createdAt": "2026-03-07T12:00:00Z",
    })


def solve_task_h115(state):
    """Mark helpful: ans_05 (38), ans_06 (29), ans_12 (35)."""
    q03 = find_question(state, "qa_03")
    ans05 = find_entity(q03["answers"], id="ans_05")
    ans05["helpful"] = ans05["helpful"] + 1

    q04 = find_question(state, "qa_04")
    ans06 = find_entity(q04["answers"], id="ans_06")
    ans06["helpful"] = ans06["helpful"] + 1

    q09 = find_question(state, "qa_09")
    ans12 = find_entity(q09["answers"], id="ans_12")
    ans12["helpful"] = ans12["helpful"] + 1


def solve_task_h116(state):
    """Answer qa_08 + schedule Career Change Guidance March 10 3 PM in person."""
    q = find_question(state, "qa_08")
    ans_id = "ans_" + str(state["_nextAnswerId"]).zfill(2)
    state["_nextAnswerId"] += 1
    q["answers"].append({
        "id": ans_id,
        "authorName": "Maya Chen",
        "authorSchool": state["currentUser"]["school"],
        "authorMajor": state["currentUser"]["major"],
        "authorGradYear": state["currentUser"]["graduationYear"],
        "authorAvatarColor": state["currentUser"]["avatarColor"],
        "text": "GPA is important for the resume screen but once you get interviews it's all about case performance and fit. Aim for 3.5+ and focus on networking.",
        "visibility": "full",
        "status": "pending",
        "createdAt": "2026-03-07T12:00:00Z",
        "helpful": 0,
    })
    appt_id = "appt_" + str(state["_nextAppointmentId"]).zfill(2)
    state["_nextAppointmentId"] += 1
    state["appointments"].append({
        "id": appt_id,
        "category": "Career Counseling",
        "type": "Career Change Guidance",
        "staffId": None,
        "staffName": None,
        "date": "2026-03-10",
        "time": "3:00 PM",
        "duration": 30,
        "medium": "In Person",
        "location": "Career Center",
        "status": "requested",
        "details": "",
        "comments": [],
        "createdAt": "2026-03-07T12:00:00Z",
    })


def solve_task_h117(state):
    """Follow Epic + save job_16 + add Biotechnology. Discovery: patient care testimonial."""
    user = state["currentUser"]
    if "emp_14" not in user["followedEmployerIds"]:
        user["followedEmployerIds"].append("emp_14")
        emp = find_employer(state, "emp_14")
        emp["followCount"] = emp["followCount"] + 1
    if "job_16" not in user["savedJobIds"]:
        user["savedJobIds"].append("job_16")
    ci = user["careerInterests"]
    if "Biotechnology" not in ci["industries"]:
        ci["industries"].append("Biotechnology")


def solve_task_h118(state):
    """Read all unread messages + comment on Google's post (most recent sender)."""
    for msg_id in ["msg_01", "msg_03", "msg_06", "msg_08"]:
        msg = find_message(state, msg_id)
        msg["isRead"] = True
    post = find_post(state, "post_01")
    comment_id = "cmt_" + str(state["_nextCommentId"])
    state["_nextCommentId"] += 1
    post["comments"].append({
        "id": comment_id,
        "authorName": state["currentUser"]["fullName"],
        "authorSchool": state["currentUser"]["school"],
        "authorAvatarColor": state["currentUser"]["avatarColor"],
        "text": "Excited about the expanded internship program! Just submitted my application.",
        "createdAt": "2026-03-07T12:00:00Z",
        "isAnonymous": False,
    })


def solve_task_h119(state):
    """Bookmark posts from employers with >= 2 active jobs."""
    user = state["currentUser"]
    for post_id in ["post_01", "post_03", "post_05", "post_07", "post_11", "post_19"]:
        post = find_post(state, post_id)
        post["bookmarked"] = True
        if post_id not in user["savedPostIds"]:
            user["savedPostIds"].append(post_id)


def solve_task_h120(state):
    """Cancel appt_08 (further future) + comment on appt_02 (earlier) about frameworks."""
    appt_08 = find_appointment(state, "appt_08")
    appt_08["status"] = "cancelled"
    appt_02 = find_appointment(state, "appt_02")
    appt_02["comments"].append({
        "author": state["currentUser"]["fullName"],
        "text": "Could we also discuss interview frameworks during our session?",
        "createdAt": "2026-03-07T12:00:00Z",
    })


# === HARDENING ROUND 2 ===

def solve_task_h121(state):
    """Change profile visibility to Employers + save Anthropic jobs (AI safety testimonial)."""
    state["currentUser"]["profileVisibility"] = "Employers"
    user = state["currentUser"]
    for jid in ["job_12", "job_29"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)


def solve_task_h122(state):
    """Employers with exactly 1 active job: save if followed, follow if not."""
    user = state["currentUser"]
    # Count active jobs per employer
    active_count = {}
    for job in state["jobs"]:
        if job.get("status") == "active":
            eid = job["employerId"]
            active_count[eid] = active_count.get(eid, 0) + 1

    # Find the single active job for employers with exactly 1
    single_job = {}
    for job in state["jobs"]:
        if job.get("status") == "active":
            eid = job["employerId"]
            if active_count.get(eid) == 1:
                single_job[eid] = job["id"]

    seed_followed = set(user["followedEmployerIds"])
    for eid, jid in single_job.items():
        if eid in seed_followed:
            if jid not in user["savedJobIds"]:
                user["savedJobIds"].append(jid)
        else:
            user["followedEmployerIds"].append(eid)
            emp = find_employer(state, eid)
            emp["followCount"] = emp["followCount"] + 1


def solve_task_h123(state):
    """Google identified via 'grew more' testimonial. Save job_02 + comment on post_01."""
    user = state["currentUser"]
    if "job_02" not in user["savedJobIds"]:
        user["savedJobIds"].append("job_02")
    post = find_post(state, "post_01")
    comment_id = "cmt_" + str(state["_nextCommentId"])
    state["_nextCommentId"] += 1
    post["comments"].append({
        "id": comment_id,
        "authorName": user["fullName"],
        "authorSchool": user["school"],
        "authorAvatarColor": user["avatarColor"],
        "text": "Excited about the expanded internship program! The alumni testimonials are really inspiring.",
        "createdAt": "2026-03-08T12:00:00Z",
        "isAnonymous": False,
    })


def solve_task_h124(state):
    """Cancel appt_02 (interview coach), schedule new behavioral, comment on appt_01."""
    appt_02 = find_appointment(state, "appt_02")
    appt_02["status"] = "cancelled"

    appt_id = "appt_" + str(state["_nextAppointmentId"]).zfill(2)
    state["_nextAppointmentId"] += 1
    state["appointments"].append({
        "id": appt_id,
        "category": "Interview Preparation",
        "type": "Mock Interview - Behavioral",
        "staffId": None,
        "staffName": None,
        "date": "2026-03-19",
        "time": "3:00 PM",
        "duration": 30,
        "medium": "Virtual on Handshake",
        "location": None,
        "status": "requested",
        "details": "",
        "comments": [],
        "createdAt": "2026-03-08T12:00:00Z",
    })

    appt_01 = find_appointment(state, "appt_01")
    appt_01["comments"].append({
        "author": state["currentUser"]["fullName"],
        "text": "Could we also go over some portfolio tips during our session?",
        "createdAt": "2026-03-08T12:00:00Z",
    })


def solve_task_h125(state):
    """Salesforce identified via Futureforce message. RSVP evt_10, follow, save job_17."""
    evt = find_event(state, "evt_10")
    evt["rsvped"] = True
    evt["rsvpCount"] = evt["rsvpCount"] + 1

    user = state["currentUser"]
    if "emp_19" not in user["followedEmployerIds"]:
        user["followedEmployerIds"].append("emp_19")
        emp = find_employer(state, "emp_19")
        emp["followCount"] = emp["followCount"] + 1

    if "job_17" not in user["savedJobIds"]:
        user["savedJobIds"].append("job_17")


def solve_task_h126(state):
    """Read msg_01 (most recent unread). RSVP evt_04 (Google). Save Google active jobs."""
    msg = find_message(state, "msg_01")
    msg["isRead"] = True

    evt = find_event(state, "evt_04")
    evt["rsvped"] = True
    evt["rsvpCount"] = evt["rsvpCount"] + 1

    user = state["currentUser"]
    for jid in ["job_01", "job_02", "job_22"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)


def solve_task_h127(state):
    """McKinsey (consulting + upcoming event). RSVP evt_01, save job_05."""
    evt = find_event(state, "evt_01")
    evt["rsvped"] = True
    evt["rsvpCount"] = evt["rsvpCount"] + 1

    user = state["currentUser"]
    if "job_05" not in user["savedJobIds"]:
        user["savedJobIds"].append("job_05")


def solve_task_h128(state):
    """Kevin O'Brien: FAANG post + system design Q&A. Mark ans_09 helpful, like post_08."""
    q = find_question(state, "qa_06")
    ans = find_entity(q["answers"], id="ans_09")
    ans["helpful"] = ans["helpful"] + 1

    post = find_post(state, "post_08")
    post["likes"] = post["likes"] + 1


def solve_task_h129(state):
    """Startup Grind Labs (fewest followers). Follow, save job_21, add Full-time."""
    user = state["currentUser"]
    if "emp_20" not in user["followedEmployerIds"]:
        user["followedEmployerIds"].append("emp_20")
        emp = find_employer(state, "emp_20")
        emp["followCount"] = emp["followCount"] + 1

    if "job_21" not in user["savedJobIds"]:
        user["savedJobIds"].append("job_21")

    ci = user["careerInterests"]
    if "Full-time" not in ci["jobTypes"]:
        ci["jobTypes"].append("Full-time")


def solve_task_h130(state):
    """Create school post about resume + mark helpful salary negotiation answers."""
    post_id = "post_" + str(state["_nextPostId"])
    state["_nextPostId"] += 1
    state["feedPosts"].insert(0, {
        "id": post_id,
        "authorType": "student",
        "authorId": state["currentUser"]["id"],
        "authorName": state["currentUser"]["fullName"],
        "authorSchool": state["currentUser"]["school"],
        "authorAvatarColor": state["currentUser"]["avatarColor"],
        "content": "Quick resume formatting tips: keep it to one page, use consistent fonts, quantify your achievements, and tailor it to each position!",
        "audience": "school",
        "likes": 0,
        "comments": [],
        "hasImage": False,
        "hasVideo": False,
        "createdAt": "2026-03-08T12:00:00Z",
        "bookmarked": False,
    })

    q = find_question(state, "qa_05")
    for ans_id in ["ans_07", "ans_08"]:
        ans = find_entity(q["answers"], id=ans_id)
        ans["helpful"] = ans["helpful"] + 1


def solve_task_h131(state):
    """Answer qa_10 (unanswered, finance timelines) + follow both Finance employers."""
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
        "text": "Finance recruiting for summer 2027 typically kicks off in August-September 2026. Start networking early and attend info sessions!",
        "visibility": "full",
        "status": "pending",
        "createdAt": "2026-03-08T12:00:00Z",
        "helpful": 0,
    })

    user = state["currentUser"]
    for emp_id in ["emp_02", "emp_06"]:
        if emp_id not in user["followedEmployerIds"]:
            user["followedEmployerIds"].append(emp_id)
            emp = find_employer(state, emp_id)
            emp["followCount"] = emp["followCount"] + 1


def solve_task_h132(state):
    """Like student posts with >=3 comments (post_08, post_14). Bookmark most-liked employer post (post_01)."""
    for post_id in ["post_08", "post_14"]:
        post = find_post(state, post_id)
        post["likes"] = post["likes"] + 1

    post_01 = find_post(state, "post_01")
    post_01["bookmarked"] = True
    user = state["currentUser"]
    if "post_01" not in user["savedPostIds"]:
        user["savedPostIds"].append("post_01")


def solve_task_h133(state):
    """Save highest-paid (job_12, $60/hr) + lowest-paid (job_30, $38/hr) internships. Follow Salesforce."""
    user = state["currentUser"]
    for jid in ["job_12", "job_30"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)

    if "emp_19" not in user["followedEmployerIds"]:
        user["followedEmployerIds"].append("emp_19")
        emp = find_employer(state, "emp_19")
        emp["followCount"] = emp["followCount"] + 1


def solve_task_h134(state):
    """Read unread top-match messages. Save most recently posted internship from each sender."""
    for msg_id in ["msg_01", "msg_03", "msg_08"]:
        msg = find_message(state, msg_id)
        msg["isRead"] = True

    user = state["currentUser"]
    # Google → job_22 (Feb 23), Meta → job_26 (Feb 26), Apple → job_25 (Mar 1)
    for jid in ["job_22", "job_26", "job_25"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)


def solve_task_h135(state):
    """Spotify (Media & Entertainment). Save job_15, follow, RSVP evt_07."""
    user = state["currentUser"]
    if "job_15" not in user["savedJobIds"]:
        user["savedJobIds"].append("job_15")

    if "emp_13" not in user["followedEmployerIds"]:
        user["followedEmployerIds"].append("emp_13")
        emp = find_employer(state, "emp_13")
        emp["followCount"] = emp["followCount"] + 1

    evt = find_event(state, "evt_07")
    evt["rsvped"] = True
    evt["rsvpCount"] = evt["rsvpCount"] + 1


def solve_task_h136(state):
    """Follow-up of earliest completed appt (appt_07: Major Exploration, Maria Rodriguez)."""
    appt_id = "appt_" + str(state["_nextAppointmentId"]).zfill(2)
    state["_nextAppointmentId"] += 1
    state["appointments"].append({
        "id": appt_id,
        "category": "Career Counseling",
        "type": "Major Exploration",
        "staffId": "staff_03",
        "staffName": "Maria Rodriguez",
        "date": "2026-03-28",
        "time": "9:00 AM",
        "duration": 30,
        "medium": "In Person",
        "location": "Career Center",
        "status": "requested",
        "details": "",
        "comments": [],
        "createdAt": "2026-03-08T12:00:00Z",
    })


def solve_task_h137(state):
    """Morehouse Q&A → Apple Pathways → read msg_08. Bookmark Aisha's post (post_06)."""
    msg = find_message(state, "msg_08")
    msg["isRead"] = True

    post = find_post(state, "post_06")
    post["bookmarked"] = True
    user = state["currentUser"]
    if "post_06" not in user["savedPostIds"]:
        user["savedPostIds"].append("post_06")


def solve_task_h138(state):
    """JPMorgan (closed job with most applicants: job_03, 5210). Follow + bookmark post_15."""
    user = state["currentUser"]
    if "emp_02" not in user["followedEmployerIds"]:
        user["followedEmployerIds"].append("emp_02")
        emp = find_employer(state, "emp_02")
        emp["followCount"] = emp["followCount"] + 1

    post = find_post(state, "post_15")
    post["bookmarked"] = True
    if "post_15" not in user["savedPostIds"]:
        user["savedPostIds"].append("post_15")


def solve_task_h139(state):
    """Career interests: remove UX Designer, add DevOps/Cloud, community=Engineering. Save Anthropic jobs."""
    ci = state["currentUser"]["careerInterests"]
    ci["roles"] = [r for r in ci["roles"] if r != "UX Designer"]
    for role in ["DevOps Engineer", "Cloud Engineer"]:
        if role not in ci["roles"]:
            ci["roles"].append(role)
    ci["careerCommunity"] = "Engineering"

    user = state["currentUser"]
    for jid in ["job_12", "job_29"]:
        if jid not in user["savedJobIds"]:
            user["savedJobIds"].append(jid)


def solve_task_h140(state):
    """Add Fellowship/Volunteering to postGrad. Save TFA job_20. Schedule career change guidance."""
    ci = state["currentUser"]["careerInterests"]
    for plan in ["Fellowship", "Volunteering"]:
        if plan not in ci["postGraduation"]:
            ci["postGraduation"].append(plan)

    user = state["currentUser"]
    if "job_20" not in user["savedJobIds"]:
        user["savedJobIds"].append("job_20")

    appt_id = "appt_" + str(state["_nextAppointmentId"]).zfill(2)
    state["_nextAppointmentId"] += 1
    state["appointments"].append({
        "id": appt_id,
        "category": "Career Counseling",
        "type": "Career Change Guidance",
        "staffId": None,
        "staffName": None,
        "date": "2026-03-20",
        "time": "10:00 AM",
        "duration": 30,
        "medium": "Virtual on Handshake",
        "location": None,
        "status": "requested",
        "details": "",
        "comments": [],
        "createdAt": "2026-03-08T12:00:00Z",
    })


# -- solver registry ----------------------------------------------------------

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
    "task_h101": solve_task_h101,
    "task_h102": solve_task_h102,
    "task_h103": solve_task_h103,
    "task_h104": solve_task_h104,
    "task_h105": solve_task_h105,
    "task_h106": solve_task_h106,
    "task_h107": solve_task_h107,
    "task_h108": solve_task_h108,
    "task_h109": solve_task_h109,
    "task_h110": solve_task_h110,
    "task_h111": solve_task_h111,
    "task_h112": solve_task_h112,
    "task_h113": solve_task_h113,
    "task_h114": solve_task_h114,
    "task_h115": solve_task_h115,
    "task_h116": solve_task_h116,
    "task_h117": solve_task_h117,
    "task_h118": solve_task_h118,
    "task_h119": solve_task_h119,
    "task_h120": solve_task_h120,
    "task_h121": solve_task_h121,
    "task_h122": solve_task_h122,
    "task_h123": solve_task_h123,
    "task_h124": solve_task_h124,
    "task_h125": solve_task_h125,
    "task_h126": solve_task_h126,
    "task_h127": solve_task_h127,
    "task_h128": solve_task_h128,
    "task_h129": solve_task_h129,
    "task_h130": solve_task_h130,
    "task_h131": solve_task_h131,
    "task_h132": solve_task_h132,
    "task_h133": solve_task_h133,
    "task_h134": solve_task_h134,
    "task_h135": solve_task_h135,
    "task_h136": solve_task_h136,
    "task_h137": solve_task_h137,
    "task_h138": solve_task_h138,
    "task_h139": solve_task_h139,
    "task_h140": solve_task_h140,
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
    """Load task definitions from real-tasks.json."""
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
        description="Handshake Career Exploration real-task sanity check"
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
