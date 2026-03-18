#!/usr/bin/env python3
"""
Sanity check for Gmail Accounts & Contacts real tasks.

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
TASKS_FILE = APP_DIR / "real-tasks.json"

# JS snippet to evaluate data.js and emit the seed state as JSON
_SEED_STATE_JS = r"""
const fs = require('fs');
const vm = require('vm');
const code = fs.readFileSync(process.argv[1], 'utf8');
vm.runInThisContext(code);

const state = {
    currentUser: JSON.parse(JSON.stringify(CURRENT_USER)),
    aliases: JSON.parse(JSON.stringify(ALIASES)),
    delegates: JSON.parse(JSON.stringify(DELEGATES)),
    importAccounts: JSON.parse(JSON.stringify(IMPORT_ACCOUNTS)),
    contacts: JSON.parse(JSON.stringify(CONTACTS)),
    contactGroups: JSON.parse(JSON.stringify(CONTACT_GROUPS)),
    otherContacts: JSON.parse(JSON.stringify(OTHER_CONTACTS)),
    directory: JSON.parse(JSON.stringify(DIRECTORY)),
    appPasswords: JSON.parse(JSON.stringify(APP_PASSWORDS)),
    replyFromSetting: REPLY_FROM_SETTING,
    _seedVersion: SEED_DATA_VERSION,
    _nextContactId: 121,
    _nextGroupId: 11,
    _nextAliasId: 5,
    _nextDelegateId: 4,
    _nextImportId: 3,
    _nextAppPasswordId: 4,
    _nextOtherContactId: 26,
};
process.stdout.write(JSON.stringify(state));
"""


# ── helpers ──────────────────────────────────────────────────────────

def find_contact_by_name(state, first, last):
    for c in state["contacts"]:
        if c["firstName"] == first and c["lastName"] == last:
            return c
    raise ValueError(f"Contact not found: {first} {last}")


def find_group_by_name(state, name):
    for g in state["contactGroups"]:
        if g["name"] == name:
            return g
    raise ValueError(f"Group not found: {name!r}")


def find_alias_by_email(state, email):
    for a in state["aliases"]:
        if a["email"] == email:
            return a
    raise ValueError(f"Alias not found: {email!r}")


def find_delegate_by_email(state, email):
    for d in state["delegates"]:
        if d["email"] == email:
            return d
    raise ValueError(f"Delegate not found: {email!r}")


def find_import_by_email(state, email):
    for i in state["importAccounts"]:
        if i["email"] == email:
            return i
    raise ValueError(f"Import account not found: {email!r}")


def find_other_by_email(state, email):
    for oc in state["otherContacts"]:
        if oc["email"] == email:
            return oc
    raise ValueError(f"Other contact not found: {email!r}")


def next_contact_id(state):
    cid = state.get("_nextContactId", 121)
    state["_nextContactId"] = cid + 1
    return cid


def next_group_id(state):
    gid = state.get("_nextGroupId", 11)
    state["_nextGroupId"] = gid + 1
    return gid


def next_alias_id(state):
    aid = state.get("_nextAliasId", 5)
    state["_nextAliasId"] = aid + 1
    return aid


def next_delegate_id(state):
    did = state.get("_nextDelegateId", 4)
    state["_nextDelegateId"] = did + 1
    return did


def next_import_id(state):
    iid = state.get("_nextImportId", 3)
    state["_nextImportId"] = iid + 1
    return iid


def next_app_password_id(state):
    apid = state.get("_nextAppPasswordId", 4)
    state["_nextAppPasswordId"] = apid + 1
    return apid


NOW = "2026-03-18T12:00:00Z"


# ── solve functions ──────────────────────────────────────────────────

# ── Easy tasks ──

def solve_task_e1(state):
    """Star Mei Zhang."""
    c = find_contact_by_name(state, "Mei", "Zhang")
    c["starred"] = True
    c["updatedAt"] = NOW


def solve_task_e2(state):
    """Unstar Jake Morrison."""
    c = find_contact_by_name(state, "Jake", "Morrison")
    c["starred"] = False
    c["updatedAt"] = NOW


def solve_task_e3(state):
    """Delete Penny Crawford."""
    state["contacts"] = [c for c in state["contacts"]
                         if not (c["firstName"] == "Penny" and c["lastName"] == "Crawford")]


def solve_task_e4(state):
    """Rename Book Club to Reading Group."""
    g = find_group_by_name(state, "Book Club")
    g["name"] = "Reading Group"
    g["updatedAt"] = NOW


def solve_task_e5(state):
    """Turn off 2-Step Verification."""
    state["currentUser"]["twoStepVerification"] = False


def solve_task_e6(state):
    """Revoke app password Mail on iPhone."""
    state["appPasswords"] = [a for a in state["appPasswords"]
                             if a["name"] != "Mail on iPhone"]


def solve_task_e7(state):
    """Remove delegate Alex Martinez."""
    state["delegates"] = [d for d in state["delegates"]
                          if d["email"] != "alex.martinez@techcorp.io"]


def solve_task_e8(state):
    """Delete Stanford alumni alias."""
    state["aliases"] = [a for a in state["aliases"]
                        if a["email"] != "schen@alumni.stanford.edu"]


def solve_task_e9(state):
    """Set reply-from to same."""
    state["replyFromSetting"] = "same"


def solve_task_e10(state):
    """Remove old startup import account."""
    state["importAccounts"] = [i for i in state["importAccounts"]
                               if i["email"] != "sarah@old-startup.com"]


def solve_task_e11(state):
    """Delete GitHub notifications from Other Contacts."""
    state["otherContacts"] = [o for o in state["otherContacts"]
                              if o["email"] != "noreply@github.com"]


def solve_task_e12(state):
    """Update recovery phone."""
    state["currentUser"]["recoveryPhone"] = "+1 (650) 555-0300"


def solve_task_e13(state):
    """Create Mentors label."""
    gid = next_group_id(state)
    state["contactGroups"].append({
        "id": f"grp_{gid}", "name": "Mentors",
        "system": False, "createdAt": NOW, "updatedAt": NOW
    })


def solve_task_e14(state):
    """Make support@techcorp.io the default alias."""
    for a in state["aliases"]:
        a["isDefault"] = (a["email"] == "support@techcorp.io")


def solve_task_e15(state):
    """Delete Investors label."""
    grp = find_group_by_name(state, "Investors")
    grp_id = grp["id"]
    state["contactGroups"] = [g for g in state["contactGroups"] if g["id"] != grp_id]
    for c in state["contacts"]:
        c["groups"] = [g for g in c["groups"] if g != grp_id]


def solve_task_e16(state):
    """Remove Tom O'Brien from Engineering Team."""
    c = find_contact_by_name(state, "Tom", "O'Brien")
    c["groups"] = [g for g in c["groups"] if g != "grp_4"]
    c["updatedAt"] = NOW


def solve_task_e17(state):
    """Delete Slack notifications from Other Contacts."""
    state["otherContacts"] = [o for o in state["otherContacts"]
                              if o["email"] != "notifications@slack.com"]


def solve_task_e18(state):
    """Change account last name to Chen-Williams."""
    state["currentUser"]["lastName"] = "Chen-Williams"


def solve_task_e19(state):
    """Remove family email alias."""
    state["aliases"] = [a for a in state["aliases"]
                        if a["email"] != "sarah@chen-family.org"]


def solve_task_e20(state):
    """Star Olivia Grant."""
    c = find_contact_by_name(state, "Olivia", "Grant")
    c["starred"] = True
    c["updatedAt"] = NOW


# ── Medium tasks ──

def solve_task_m1(state):
    """Add new contact Taylor Morgan in Work."""
    cid = next_contact_id(state)
    work_grp = find_group_by_name(state, "Work")
    state["contacts"].append({
        "id": f"ct_{cid}", "firstName": "Taylor", "lastName": "Morgan",
        "email": "taylor.morgan@techcorp.io", "phone": "+1 (415) 555-3500",
        "company": "TechCorp", "jobTitle": "Marketing Manager",
        "address": "", "birthday": "", "notes": "",
        "starred": False, "groups": [work_grp["id"]], "createdAt": NOW, "updatedAt": NOW
    })


def solve_task_m2(state):
    """Update Priya Sharma's title and add to VIP."""
    c = find_contact_by_name(state, "Priya", "Sharma")
    c["jobTitle"] = "VP of Engineering"
    vip = find_group_by_name(state, "VIP")
    if vip["id"] not in c["groups"]:
        c["groups"].append(vip["id"])
    c["updatedAt"] = NOW


def solve_task_m3(state):
    """Promote LinkedIn recruiter to main contacts."""
    oc = find_other_by_email(state, "jason.recruiter@linkedin.com")
    cid = next_contact_id(state)
    state["contacts"].append({
        "id": f"ct_{cid}",
        "firstName": oc.get("firstName", "") or "",
        "lastName": oc.get("lastName", "") or "",
        "email": oc["email"],
        "phone": "", "company": "", "jobTitle": "", "address": "",
        "birthday": "", "notes": "", "starred": False, "groups": [],
        "createdAt": NOW, "updatedAt": NOW
    })
    state["otherContacts"] = [o for o in state["otherContacts"]
                              if o["email"] != oc["email"]]


def solve_task_m4(state):
    """Add alias sarah.personal@protonmail.com."""
    aid = next_alias_id(state)
    state["aliases"].append({
        "id": f"alias_{aid}",
        "name": "Sarah Chen (Personal)",
        "email": "sarah.personal@protonmail.com",
        "isPrimary": False, "isDefault": False,
        "replyFrom": "default",
        "smtpServer": "smtp.protonmail.com",
        "smtpPort": "587",
        "smtpUsername": "sarah.personal@protonmail.com",
        "useSSL": True,
        "createdAt": NOW
    })


def solve_task_m5(state):
    """Add delegate david.park@techcorp.io."""
    did = next_delegate_id(state)
    state["delegates"].append({
        "id": f"del_{did}",
        "email": "david.park@techcorp.io",
        "name": "David Park",
        "status": "pending",
        "addedAt": NOW
    })


def solve_task_m6(state):
    """Update support@techcorp.io alias display name."""
    a = find_alias_by_email(state, "support@techcorp.io")
    a["name"] = "TechCorp Support Team"


def solve_task_m7(state):
    """Generate app password Spark Email Client."""
    apid = next_app_password_id(state)
    state["appPasswords"].append({
        "id": f"ap_{apid}", "name": "Spark Email Client",
        "createdAt": NOW, "lastUsed": None
    })


def solve_task_m8(state):
    """Move Natalie Dubois into Work and Friends."""
    c = find_contact_by_name(state, "Natalie", "Dubois")
    work = find_group_by_name(state, "Work")
    friends = find_group_by_name(state, "Friends")
    if work["id"] not in c["groups"]:
        c["groups"].append(work["id"])
    if friends["id"] not in c["groups"]:
        c["groups"].append(friends["id"])
    c["updatedAt"] = NOW


def solve_task_m9(state):
    """Add POP3 import for sarah@side-project.io."""
    iid = next_import_id(state)
    state["importAccounts"].append({
        "id": f"imp_{iid}",
        "email": "sarah@side-project.io",
        "server": "pop.side-project.io",
        "port": "995",
        "username": "sarah",
        "useSSL": True,
        "leaveOnServer": True,
        "labelIncoming": "side-project",
        "status": "active",
        "lastChecked": NOW,
        "addedAt": NOW
    })


def solve_task_m10(state):
    """Update Alex Martinez's phone and birthday."""
    c = find_contact_by_name(state, "Alex", "Martinez")
    c["phone"] = "+1 (415) 555-1100"
    c["birthday"] = "1994-01-20"
    c["updatedAt"] = NOW


def solve_task_m11(state):
    """Update recovery email and phone."""
    state["currentUser"]["recoveryEmail"] = "sarah.backup@protonmail.com"
    state["currentUser"]["recoveryPhone"] = "+1 (510) 555-0199"


def solve_task_m12(state):
    """Create Open Source label, add Philip Okonkwo and Damian Kowalczyk."""
    gid = next_group_id(state)
    grp_id = f"grp_{gid}"
    state["contactGroups"].append({
        "id": grp_id, "name": "Open Source",
        "system": False, "createdAt": NOW, "updatedAt": NOW
    })
    c1 = find_contact_by_name(state, "Philip", "Okonkwo")
    c2 = find_contact_by_name(state, "Damian", "Kowalczyk")
    if grp_id not in c1["groups"]:
        c1["groups"].append(grp_id)
    if grp_id not in c2["groups"]:
        c2["groups"].append(grp_id)
    c1["updatedAt"] = NOW
    c2["updatedAt"] = NOW


def solve_task_m13(state):
    """Update Kevin Chen's company and job title."""
    c = find_contact_by_name(state, "Kevin", "Chen")
    c["company"] = "Google"
    c["jobTitle"] = "Senior Product Manager"
    c["updatedAt"] = NOW


def solve_task_m14(state):
    """Remove Thunderbird and Outlook app passwords."""
    state["appPasswords"] = [a for a in state["appPasswords"]
                             if a["name"] not in ("Thunderbird on MacBook", "Outlook Desktop")]


def solve_task_m15(state):
    """Promote HubSpot sales contact to main contacts."""
    oc = find_other_by_email(state, "mike.sales@hubspot.com")
    cid = next_contact_id(state)
    state["contacts"].append({
        "id": f"ct_{cid}",
        "firstName": oc.get("firstName", "") or "",
        "lastName": oc.get("lastName", "") or "",
        "email": oc["email"],
        "phone": "", "company": "", "jobTitle": "", "address": "",
        "birthday": "", "notes": "", "starred": False, "groups": [],
        "createdAt": NOW, "updatedAt": NOW
    })
    state["otherContacts"] = [o for o in state["otherContacts"]
                              if o["email"] != oc["email"]]


def solve_task_m16(state):
    """Add Elena Vasquez to Conference Contacts."""
    cid = next_contact_id(state)
    conf = find_group_by_name(state, "Conference Contacts")
    state["contacts"].append({
        "id": f"ct_{cid}", "firstName": "Elena", "lastName": "Vasquez",
        "email": "elena.vasquez@greentech.io", "phone": "",
        "company": "GreenTech Solutions", "jobTitle": "Sustainability Director",
        "address": "", "birthday": "", "notes": "",
        "starred": False, "groups": [conf["id"]], "createdAt": NOW, "updatedAt": NOW
    })


def solve_task_m17(state):
    """Rename Vendors to Technology Partners, Conference Contacts to Industry Network."""
    g1 = find_group_by_name(state, "Vendors")
    g1["name"] = "Technology Partners"
    g1["updatedAt"] = NOW
    g2 = find_group_by_name(state, "Conference Contacts")
    g2["name"] = "Industry Network"
    g2["updatedAt"] = NOW


def solve_task_m18(state):
    """Remove James Wu delegate, add Jennifer Walsh."""
    state["delegates"] = [d for d in state["delegates"]
                          if d["email"] != "james.wu@techcorp.io"]
    did = next_delegate_id(state)
    state["delegates"].append({
        "id": f"del_{did}",
        "email": "jennifer.walsh@techcorp.io",
        "name": "Jennifer Walsh",
        "status": "pending",
        "addedAt": NOW
    })


def solve_task_m19(state):
    """Update Hannah Cohen's email and remove from Work."""
    c = find_contact_by_name(state, "Hannah", "Cohen")
    c["email"] = "hannah.cohen@gmail.com"
    work = find_group_by_name(state, "Work")
    c["groups"] = [g for g in c["groups"] if g != work["id"]]
    c["updatedAt"] = NOW


def solve_task_m20(state):
    """Delete Zoom and Calendly from Other Contacts."""
    state["otherContacts"] = [o for o in state["otherContacts"]
                              if o["email"] not in ("no-reply@zoom.us", "meetingbot@calendly.com")]


# ── Hard tasks ──

def solve_task_h1(state):
    """Star all contacts in Investors."""
    grp = find_group_by_name(state, "Investors")
    for c in state["contacts"]:
        if grp["id"] in c.get("groups", []):
            c["starred"] = True
            c["updatedAt"] = NOW


def solve_task_h2(state):
    """Create Leadership Team label, add TechCorp VP/Head/CFO contacts."""
    gid = next_group_id(state)
    grp_id = f"grp_{gid}"
    state["contactGroups"].append({
        "id": grp_id, "name": "Leadership Team",
        "system": False, "createdAt": NOW, "updatedAt": NOW
    })
    import re
    pattern = re.compile(r'\b(VP|Head|CFO)\b', re.IGNORECASE)
    for c in state["contacts"]:
        if c.get("company") == "TechCorp" and c.get("jobTitle") and pattern.search(c["jobTitle"]):
            if grp_id not in c["groups"]:
                c["groups"].append(grp_id)
            c["updatedAt"] = NOW


def solve_task_h3(state):
    """Remove TechCorp contacts from Conference Contacts."""
    grp = find_group_by_name(state, "Conference Contacts")
    for c in state["contacts"]:
        if c.get("company") == "TechCorp" and grp["id"] in c.get("groups", []):
            c["groups"] = [g for g in c["groups"] if g != grp["id"]]
            c["updatedAt"] = NOW


def solve_task_h4(state):
    """Promote Kira Volkov: update title, add to VIP, star."""
    c = find_contact_by_name(state, "Kira", "Volkov")
    c["jobTitle"] = "Junior Backend Engineer"
    c["starred"] = True
    vip = find_group_by_name(state, "VIP")
    if vip["id"] not in c["groups"]:
        c["groups"].append(vip["id"])
    c["updatedAt"] = NOW


def solve_task_h5(state):
    """Delete automated-service other contacts (noreply/no-reply in email)."""
    state["otherContacts"] = [
        o for o in state["otherContacts"]
        if "noreply" not in o["email"].lower() and "no-reply" not in o["email"].lower()
    ]


def solve_task_h6(state):
    """Add Book Club members to Friends."""
    book = find_group_by_name(state, "Book Club")
    friends = find_group_by_name(state, "Friends")
    for c in state["contacts"]:
        if book["id"] in c.get("groups", []):
            if friends["id"] not in c["groups"]:
                c["groups"].append(friends["id"])
                c["updatedAt"] = NOW


def solve_task_h7(state):
    """Security audit: disable 2FA, revoke all app passwords, remove family alias."""
    state["currentUser"]["twoStepVerification"] = False
    state["appPasswords"] = []
    state["aliases"] = [a for a in state["aliases"]
                        if a["email"] != "sarah@chen-family.org"]


def solve_task_h8(state):
    """Create Patricia Nguyen, Work + VIP, starred."""
    cid = next_contact_id(state)
    work = find_group_by_name(state, "Work")
    vip = find_group_by_name(state, "VIP")
    state["contacts"].append({
        "id": f"ct_{cid}", "firstName": "Patricia", "lastName": "Nguyen",
        "email": "patricia.nguyen@techcorp.io", "phone": "+1 (415) 555-4000",
        "company": "TechCorp", "jobTitle": "Chief of Staff",
        "address": "", "birthday": "", "notes": "",
        "starred": True, "groups": [work["id"], vip["id"]],
        "createdAt": NOW, "updatedAt": NOW
    })


def solve_task_h9(state):
    """Add all Engineering Team members to Work."""
    eng = find_group_by_name(state, "Engineering Team")
    work = find_group_by_name(state, "Work")
    for c in state["contacts"]:
        if eng["id"] in c.get("groups", []):
            if work["id"] not in c["groups"]:
                c["groups"].append(work["id"])
                c["updatedAt"] = NOW


def solve_task_h10(state):
    """Remove all delegates, add Jennifer Walsh and David Park."""
    state["delegates"] = []
    did1 = next_delegate_id(state)
    state["delegates"].append({
        "id": f"del_{did1}",
        "email": "jennifer.walsh@techcorp.io",
        "name": "Jennifer Walsh",
        "status": "pending",
        "addedAt": NOW
    })
    did2 = next_delegate_id(state)
    state["delegates"].append({
        "id": f"del_{did2}",
        "email": "david.park@techcorp.io",
        "name": "David Park",
        "status": "pending",
        "addedAt": NOW
    })


def solve_task_h11(state):
    """Delete all contacts with no label."""
    state["contacts"] = [c for c in state["contacts"] if c.get("groups")]


def solve_task_h12(state):
    """Add notifications@techcorp.io alias, make default, set reply-from to same."""
    aid = next_alias_id(state)
    state["aliases"].append({
        "id": f"alias_{aid}",
        "name": "TechCorp Notifications",
        "email": "notifications@techcorp.io",
        "isPrimary": False, "isDefault": False,
        "replyFrom": "default",
        "smtpServer": "smtp.techcorp.io",
        "smtpPort": "587",
        "smtpUsername": "notifications@techcorp.io",
        "useSSL": True,
        "createdAt": NOW
    })
    # Make it default
    for a in state["aliases"]:
        a["isDefault"] = (a["email"] == "notifications@techcorp.io")
    state["replyFromSetting"] = "same"


def solve_task_h13(state):
    """Delete College Alumni label, unstar members not in VIP/Investors."""
    grp = find_group_by_name(state, "College Alumni")
    grp_id = grp["id"]
    vip = find_group_by_name(state, "VIP")
    investors = find_group_by_name(state, "Investors")
    protected_groups = {vip["id"], investors["id"]}

    for c in state["contacts"]:
        if grp_id in c.get("groups", []):
            # Check if contact is in VIP or Investors
            other_special = set(c["groups"]) & protected_groups
            if not other_special:
                c["starred"] = False
            c["groups"] = [g for g in c["groups"] if g != grp_id]
            c["updatedAt"] = NOW

    state["contactGroups"] = [g for g in state["contactGroups"] if g["id"] != grp_id]


def solve_task_h14(state):
    """Promote other contacts with >50 interactions to main contacts."""
    to_promote = [oc for oc in state["otherContacts"] if oc.get("interactionCount", 0) > 50]
    for oc in to_promote:
        cid = next_contact_id(state)
        state["contacts"].append({
            "id": f"ct_{cid}",
            "firstName": oc.get("firstName", "") or "",
            "lastName": oc.get("lastName", "") or "",
            "email": oc["email"],
            "phone": "", "company": "", "jobTitle": "", "address": "",
            "birthday": "", "notes": "", "starred": False, "groups": [],
            "createdAt": NOW, "updatedAt": NOW
        })
    promoted_emails = {oc["email"] for oc in to_promote}
    state["otherContacts"] = [o for o in state["otherContacts"]
                              if o["email"] not in promoted_emails]


def solve_task_h15(state):
    """Create Advisors and Board labels, move Investors to Advisors, Derek+Victoria to Board."""
    gid1 = next_group_id(state)
    advisors_id = f"grp_{gid1}"
    state["contactGroups"].append({
        "id": advisors_id, "name": "Advisors",
        "system": False, "createdAt": NOW, "updatedAt": NOW
    })
    gid2 = next_group_id(state)
    board_id = f"grp_{gid2}"
    state["contactGroups"].append({
        "id": board_id, "name": "Board",
        "system": False, "createdAt": NOW, "updatedAt": NOW
    })
    investors = find_group_by_name(state, "Investors")
    for c in state["contacts"]:
        if investors["id"] in c.get("groups", []):
            if advisors_id not in c["groups"]:
                c["groups"].append(advisors_id)
            c["updatedAt"] = NOW
    # Also add Derek Hoffman and Victoria Blackwell to Board
    derek = find_contact_by_name(state, "Derek", "Hoffman")
    victoria = find_contact_by_name(state, "Victoria", "Blackwell")
    if board_id not in derek["groups"]:
        derek["groups"].append(board_id)
    if board_id not in victoria["groups"]:
        victoria["groups"].append(board_id)


def solve_task_h16(state):
    """Update account name, recovery email, support alias name."""
    state["currentUser"]["firstName"] = "S."
    state["currentUser"]["lastName"] = "Chen"
    state["currentUser"]["recoveryEmail"] = "s.chen.recovery@gmail.com"
    a = find_alias_by_email(state, "support@techcorp.io")
    a["name"] = "S. Chen (Support)"


def solve_task_h17(state):
    """Remove all non-primary non-default aliases, set reply-from to default."""
    state["aliases"] = [a for a in state["aliases"]
                        if a.get("isPrimary") or a.get("isDefault")]
    state["replyFromSetting"] = "default"


def solve_task_h18(state):
    """Create Swedish Contacts label, add all contacts with +46 phone."""
    gid = next_group_id(state)
    grp_id = f"grp_{gid}"
    state["contactGroups"].append({
        "id": grp_id, "name": "Swedish Contacts",
        "system": False, "createdAt": NOW, "updatedAt": NOW
    })
    for c in state["contacts"]:
        phone = c.get("phone", "") or ""
        if phone.startswith("+46"):
            if grp_id not in c["groups"]:
                c["groups"].append(grp_id)
            c["updatedAt"] = NOW


def solve_task_h19(state):
    """Add POP3 import for consulting-gig, remove errored import."""
    iid = next_import_id(state)
    state["importAccounts"].append({
        "id": f"imp_{iid}",
        "email": "sarah@consulting-gig.com",
        "server": "pop.consulting-gig.com",
        "port": "110",
        "username": "sarah",
        "useSSL": False,
        "leaveOnServer": False,
        "labelIncoming": "consulting",
        "status": "active",
        "lastChecked": NOW,
        "addedAt": NOW
    })
    state["importAccounts"] = [i for i in state["importAccounts"]
                               if i["email"] != "sarah@old-startup.com"]


def solve_task_h20(state):
    """Remove non-TechCorp from VIP, add Priya Sharma and James Wu."""
    vip = find_group_by_name(state, "VIP")
    vip_id = vip["id"]
    for c in state["contacts"]:
        if vip_id in c.get("groups", []):
            if c.get("company") != "TechCorp":
                c["groups"] = [g for g in c["groups"] if g != vip_id]
                c["updatedAt"] = NOW
    priya = find_contact_by_name(state, "Priya", "Sharma")
    james = find_contact_by_name(state, "James", "Wu")
    if vip_id not in priya["groups"]:
        priya["groups"].append(vip_id)
        priya["updatedAt"] = NOW
    if vip_id not in james["groups"]:
        james["groups"].append(vip_id)
        james["updatedAt"] = NOW


# ── Hardening round 1 tasks ──

def solve_task_h21(state):
    """Add Stockholm Backend Engineer from directory to contacts."""
    cid = next_contact_id(state)
    work = find_group_by_name(state, "Work")
    eng = find_group_by_name(state, "Engineering Team")
    state["contacts"].append({
        "id": f"ct_{cid}", "firstName": "Eric", "lastName": "Johansson",
        "email": "eric.johansson@techcorp.io", "phone": "+46 70 234 5678",
        "company": "TechCorp", "jobTitle": "Backend Engineer",
        "address": "", "birthday": "", "notes": "",
        "starred": False, "groups": [work["id"], eng["id"]],
        "createdAt": NOW, "updatedAt": NOW
    })


def solve_task_h22(state):
    """Sequoia Capital contact transitions to independent advisor."""
    victoria = find_contact_by_name(state, "Victoria", "Blackwell")
    victoria["company"] = "Independent Advisor"
    victoria["starred"] = False
    investors = find_group_by_name(state, "Investors")
    victoria["groups"] = [g for g in victoria["groups"] if g != investors["id"]]
    # Create Former Investors label
    gid = next_group_id(state)
    grp_id = f"grp_{gid}"
    state["contactGroups"].append({
        "id": grp_id, "name": "Former Investors",
        "system": False, "createdAt": NOW, "updatedAt": NOW
    })
    victoria["groups"].append(grp_id)
    victoria["updatedAt"] = NOW


def solve_task_h23(state):
    """Remove Japanese +81 contacts from Conference Contacts."""
    conf = find_group_by_name(state, "Conference Contacts")
    conf_id = conf["id"]
    for c in state["contacts"]:
        phone = c.get("phone", "") or ""
        if phone.startswith("+81") and conf_id in c.get("groups", []):
            c["groups"] = [g for g in c["groups"] if g != conf_id]
            c["updatedAt"] = NOW


def solve_task_h24(state):
    """Delete Diana Petrova (Wolt, food delivery)."""
    state["contacts"] = [
        c for c in state["contacts"]
        if not (c["firstName"] == "Diana" and c["lastName"] == "Petrova")
    ]


def solve_task_h25(state):
    """Promote IT helpdesk from Other Contacts to main contacts, add to Work."""
    oc = find_other_by_email(state, "it-helpdesk@techcorp.io")
    cid = next_contact_id(state)
    work = find_group_by_name(state, "Work")
    state["contacts"].append({
        "id": f"ct_{cid}",
        "firstName": oc.get("firstName", "") or "IT",
        "lastName": oc.get("lastName", "") or "Help",
        "email": oc["email"],
        "phone": "", "company": "", "jobTitle": "", "address": "",
        "birthday": "", "notes": "", "starred": False,
        "groups": [work["id"]],
        "createdAt": NOW, "updatedAt": NOW
    })
    state["otherContacts"] = [
        o for o in state["otherContacts"] if o["email"] != oc["email"]
    ]


def solve_task_h26(state):
    """Personal email change: recovery, remove old import, add new import."""
    state["currentUser"]["recoveryEmail"] = "sarah.chen.new@protonmail.com"
    state["importAccounts"] = [
        i for i in state["importAccounts"]
        if i["email"] != "sarahchen.personal@gmail.com"
    ]
    iid = next_import_id(state)
    state["importAccounts"].append({
        "id": f"imp_{iid}",
        "email": "sarah.chen.new@protonmail.com",
        "server": "pop.protonmail.com",
        "port": "993",
        "username": "sarah.chen.new",
        "useSSL": True,
        "leaveOnServer": True,
        "labelIncoming": "personal",
        "status": "active",
        "lastChecked": NOW,
        "addedAt": NOW
    })


def solve_task_h27(state):
    """Unstar all Family members except the youngest (Kevin Chen, 1995)."""
    family = find_group_by_name(state, "Family")
    family_id = family["id"]
    for c in state["contacts"]:
        if family_id in c.get("groups", []):
            if c["firstName"] == "Kevin" and c["lastName"] == "Chen":
                continue  # youngest — keep starred
            if c.get("starred"):
                c["starred"] = False
                c["updatedAt"] = NOW


def solve_task_h28(state):
    """Add non-Eng/Design directory employees not in contacts to Work."""
    work = find_group_by_name(state, "Work")
    new_employees = [
        {"firstName": "David", "lastName": "Park",
         "email": "david.park@techcorp.io", "phone": "+1 (415) 555-1022",
         "jobTitle": "Senior Product Manager"},
        {"firstName": "Jennifer", "lastName": "Walsh",
         "email": "jennifer.walsh@techcorp.io", "phone": "+1 (415) 555-1023",
         "jobTitle": "General Counsel"},
        {"firstName": "Tony", "lastName": "Russo",
         "email": "tony.russo@techcorp.io", "phone": "+1 (212) 555-1024",
         "jobTitle": "Account Executive"},
        {"firstName": "Elaine", "lastName": "Cho",
         "email": "elaine.cho@techcorp.io", "phone": "+1 (415) 555-1025",
         "jobTitle": "Marketing Director"},
        {"firstName": "Maria", "lastName": "Santos",
         "email": "maria.santos@techcorp.io", "phone": "+1 (415) 555-1029",
         "jobTitle": "Support Team Lead"},
    ]
    for emp in new_employees:
        cid = next_contact_id(state)
        state["contacts"].append({
            "id": f"ct_{cid}",
            "firstName": emp["firstName"], "lastName": emp["lastName"],
            "email": emp["email"], "phone": emp["phone"],
            "company": "TechCorp", "jobTitle": emp["jobTitle"],
            "address": "", "birthday": "", "notes": "",
            "starred": False, "groups": [work["id"]],
            "createdAt": NOW, "updatedAt": NOW
        })


def solve_task_h29(state):
    """Revoke all app passwords, generate 3 new ones."""
    state["appPasswords"] = []
    for name in ["Work Laptop", "Home Desktop", "Tablet"]:
        apid = next_app_password_id(state)
        state["appPasswords"].append({
            "id": f"ap_{apid}", "name": name,
            "createdAt": NOW, "lastUsed": None
        })


def solve_task_h30(state):
    """ByteDance Zhaos: star Helen + VIP, remove Wei from Conference."""
    helen = find_contact_by_name(state, "Helen", "Zhao")
    wei = find_contact_by_name(state, "Wei", "Zhao")
    vip = find_group_by_name(state, "VIP")
    conf = find_group_by_name(state, "Conference Contacts")
    helen["starred"] = True
    if vip["id"] not in helen["groups"]:
        helen["groups"].append(vip["id"])
    helen["updatedAt"] = NOW
    wei["groups"] = [g for g in wei["groups"] if g != conf["id"]]
    wei["updatedAt"] = NOW


def solve_task_h31(state):
    """Create Key Contacts from starred contacts with 2+ labels."""
    gid = next_group_id(state)
    grp_id = f"grp_{gid}"
    state["contactGroups"].append({
        "id": grp_id, "name": "Key Contacts",
        "system": False, "createdAt": NOW, "updatedAt": NOW
    })
    for c in state["contacts"]:
        if c.get("starred") and len(c.get("groups", [])) >= 2:
            c["groups"].append(grp_id)
            c["updatedAt"] = NOW


def solve_task_h32(state):
    """CFO: add notes, star, add to Family."""
    diana = find_contact_by_name(state, "Diana", "Ross-Taylor")
    diana["notes"] = "Executive sponsor for Q2 initiative"
    diana["starred"] = True
    family = find_group_by_name(state, "Family")
    if family["id"] not in diana["groups"]:
        diana["groups"].append(family["id"])
    diana["updatedAt"] = NOW


def solve_task_h33(state):
    """Support default, reply-from same, HR partner as delegate."""
    for a in state["aliases"]:
        a["isDefault"] = (a["email"] == "support@techcorp.io")
    state["replyFromSetting"] = "same"
    did = next_delegate_id(state)
    state["delegates"].append({
        "id": f"del_{did}",
        "email": "megan.fosterkim@techcorp.io",
        "name": "Megan Foster-Kim",
        "status": "pending",
        "addedAt": NOW
    })


def solve_task_h34(state):
    """Create Finance Network: all Investors + contacts with CFO/Finance/Banking."""
    import re
    gid = next_group_id(state)
    grp_id = f"grp_{gid}"
    state["contactGroups"].append({
        "id": grp_id, "name": "Finance Network",
        "system": False, "createdAt": NOW, "updatedAt": NOW
    })
    investors = find_group_by_name(state, "Investors")
    pattern = re.compile(r'\b(CFO|Finance|Banking)\b', re.IGNORECASE)
    for c in state["contacts"]:
        in_investors = investors["id"] in c.get("groups", [])
        title_match = c.get("jobTitle") and pattern.search(c["jobTitle"])
        if in_investors or title_match:
            if grp_id not in c["groups"]:
                c["groups"].append(grp_id)
            c["updatedAt"] = NOW


def solve_task_h35(state):
    """Delete aliases with external SMTP, set reply-from to default."""
    state["aliases"] = [
        a for a in state["aliases"]
        if not a.get("smtpServer")
        or a["smtpServer"].endswith("techcorp.io")
    ]
    state["replyFromSetting"] = "default"


def solve_task_h36(state):
    """HR Partner: title to Head of People Operations, VIP, star."""
    megan = find_contact_by_name(state, "Megan", "Foster-Kim")
    megan["jobTitle"] = "Head of People Operations"
    megan["starred"] = True
    vip = find_group_by_name(state, "VIP")
    if vip["id"] not in megan["groups"]:
        megan["groups"].append(vip["id"])
    megan["updatedAt"] = NOW


def solve_task_h37(state):
    """Marketing alias + default + Marketing Director as delegate."""
    aid = next_alias_id(state)
    state["aliases"].append({
        "id": f"alias_{aid}",
        "name": "TechCorp Marketing",
        "email": "marketing@techcorp.io",
        "isPrimary": False, "isDefault": False,
        "replyFrom": "default",
        "smtpServer": "smtp.techcorp.io",
        "smtpPort": "587",
        "smtpUsername": "marketing@techcorp.io",
        "useSSL": True,
        "createdAt": NOW
    })
    for a in state["aliases"]:
        a["isDefault"] = (a["email"] == "marketing@techcorp.io")
    did = next_delegate_id(state)
    state["delegates"].append({
        "id": f"del_{did}",
        "email": "elaine.cho@techcorp.io",
        "name": "Elaine Cho",
        "status": "pending",
        "addedAt": NOW
    })


def solve_task_h38(state):
    """Remove active delegates, keep pending, add Elaine Cho and Brian Foster."""
    state["delegates"] = [
        d for d in state["delegates"] if d.get("status") == "pending"
    ]
    did1 = next_delegate_id(state)
    state["delegates"].append({
        "id": f"del_{did1}",
        "email": "elaine.cho@techcorp.io",
        "name": "Elaine Cho",
        "status": "pending",
        "addedAt": NOW
    })
    did2 = next_delegate_id(state)
    state["delegates"].append({
        "id": f"del_{did2}",
        "email": "brian.foster@techcorp.io",
        "name": "Brian Foster",
        "status": "pending",
        "addedAt": NOW
    })


def solve_task_h39(state):
    """CEO reports → VIP + starred."""
    vip = find_group_by_name(state, "VIP")
    vip_id = vip["id"]
    # CEO reports who are in contacts: Marcus Johnson, Diana Ross-Taylor,
    # Carlos Mendoza, Sophia Andersson
    ceo_reports = [
        ("Marcus", "Johnson"),
        ("Diana", "Ross-Taylor"),
        ("Carlos", "Mendoza"),
        ("Sophia", "Andersson"),
    ]
    for first, last in ceo_reports:
        c = find_contact_by_name(state, first, last)
        if vip_id not in c["groups"]:
            c["groups"].append(vip_id)
        if not c.get("starred"):
            c["starred"] = True
        c["updatedAt"] = NOW


def solve_task_h40(state):
    """Keep only cloud infra vendors, star remaining."""
    vendors = find_group_by_name(state, "Vendors")
    vendors_id = vendors["id"]
    keep_companies = {
        "Amazon Web Services", "Cloudflare", "Snowflake",
        "Datadog", "MongoDB", "HashiCorp", "Elastic",
    }
    for c in state["contacts"]:
        if vendors_id in c.get("groups", []):
            if c.get("company") in keep_companies:
                if not c.get("starred"):
                    c["starred"] = True
                    c["updatedAt"] = NOW
            else:
                c["groups"] = [g for g in c["groups"] if g != vendors_id]
                c["updatedAt"] = NOW


# ── solver registry ──────────────────────────────────────────────────

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
    parser = argparse.ArgumentParser(description="Gmail Accounts & Contacts real-task sanity check")
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
