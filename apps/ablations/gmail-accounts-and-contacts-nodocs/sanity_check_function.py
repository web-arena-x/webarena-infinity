#!/usr/bin/env python3
"""
Sanity check for Gmail Accounts & Contacts function-test tasks.

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

def find_contact(state, **kwargs):
    """Find a contact by attribute match. Raises if not found."""
    for c in state["contacts"]:
        if all(c.get(k) == v for k, v in kwargs.items()):
            return c
    raise ValueError(f"Contact not found: {kwargs}")


def find_contact_by_name(state, first, last):
    """Find a contact by first and last name."""
    for c in state["contacts"]:
        if c["firstName"] == first and c["lastName"] == last:
            return c
    raise ValueError(f"Contact not found: {first} {last}")


def find_group_by_name(state, name):
    """Find a contact group by name."""
    for g in state["contactGroups"]:
        if g["name"] == name:
            return g
    raise ValueError(f"Group not found: {name!r}")


def find_alias_by_email(state, email):
    """Find an alias by email."""
    for a in state["aliases"]:
        if a["email"] == email:
            return a
    raise ValueError(f"Alias not found: {email!r}")


def find_delegate_by_email(state, email):
    """Find a delegate by email."""
    for d in state["delegates"]:
        if d["email"] == email:
            return d
    raise ValueError(f"Delegate not found: {email!r}")


def find_import_by_email(state, email):
    """Find an import account by email."""
    for i in state["importAccounts"]:
        if i["email"] == email:
            return i
    raise ValueError(f"Import account not found: {email!r}")


def find_other_by_email(state, email):
    """Find an other contact by email."""
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

def solve_task_1(state):
    """Create contact Maria Lopez with email."""
    cid = next_contact_id(state)
    state["contacts"].append({
        "id": f"ct_{cid}", "firstName": "Maria", "lastName": "Lopez",
        "email": "maria.lopez@example.com", "phone": "", "company": "",
        "jobTitle": "", "address": "", "birthday": "", "notes": "",
        "starred": False, "groups": [], "createdAt": NOW, "updatedAt": NOW
    })


def solve_task_2(state):
    """Create contact John Doe with all fields."""
    cid = next_contact_id(state)
    state["contacts"].append({
        "id": f"ct_{cid}", "firstName": "John", "lastName": "Doe",
        "email": "john.doe@example.com", "phone": "+1 (555) 999-0001",
        "company": "Acme Corp", "jobTitle": "CEO",
        "address": "123 Main St, Springfield, IL 62701",
        "birthday": "1990-01-15", "notes": "Test contact with all fields",
        "starred": False, "groups": [], "createdAt": NOW, "updatedAt": NOW
    })


def solve_task_3(state):
    """Create contact with only email."""
    cid = next_contact_id(state)
    state["contacts"].append({
        "id": f"ct_{cid}", "firstName": "", "lastName": "",
        "email": "minimal@example.com", "phone": "", "company": "",
        "jobTitle": "", "address": "", "birthday": "", "notes": "",
        "starred": False, "groups": [], "createdAt": NOW, "updatedAt": NOW
    })


def solve_task_4(state):
    """Create contact Alex Demo assigned to Work (grp_2)."""
    cid = next_contact_id(state)
    state["contacts"].append({
        "id": f"ct_{cid}", "firstName": "Alex", "lastName": "Demo",
        "email": "alex.demo@techcorp.io", "phone": "", "company": "",
        "jobTitle": "", "address": "", "birthday": "", "notes": "",
        "starred": False, "groups": ["grp_2"], "createdAt": NOW, "updatedAt": NOW
    })


def solve_task_5(state):
    """Create contact Jane Test assigned to Family (grp_1) and Friends (grp_3)."""
    cid = next_contact_id(state)
    state["contacts"].append({
        "id": f"ct_{cid}", "firstName": "Jane", "lastName": "Test",
        "email": "jane.test@gmail.com", "phone": "", "company": "",
        "jobTitle": "", "address": "", "birthday": "", "notes": "",
        "starred": False, "groups": ["grp_1", "grp_3"], "createdAt": NOW, "updatedAt": NOW
    })


def solve_task_6(state):
    """Edit David Chen's email."""
    c = find_contact_by_name(state, "David", "Chen")
    c["email"] = "david.chen.updated@gmail.com"
    c["updatedAt"] = NOW


def solve_task_7(state):
    """Edit Alex Martinez's company and job title."""
    c = find_contact_by_name(state, "Alex", "Martinez")
    c["company"] = "TechCorp Inc"
    c["jobTitle"] = "Senior Frontend Engineer"
    c["updatedAt"] = NOW


def solve_task_8(state):
    """Edit Amy Chen-Wu's phone."""
    c = find_contact_by_name(state, "Amy", "Chen-Wu")
    c["phone"] = "+1 (510) 555-9999"
    c["updatedAt"] = NOW


def solve_task_9(state):
    """Edit Tom O'Brien's address."""
    c = find_contact_by_name(state, "Tom", "O'Brien")
    c["address"] = "123 New Street, San Francisco, CA 94100"
    c["updatedAt"] = NOW


def solve_task_10(state):
    """Edit Mei Zhang's birthday."""
    c = find_contact_by_name(state, "Mei", "Zhang")
    c["birthday"] = "1992-07-15"
    c["updatedAt"] = NOW


def solve_task_11(state):
    """Edit Lisa Kim's notes."""
    c = find_contact_by_name(state, "Lisa", "Kim")
    c["notes"] = "Design system owner - working on v2 redesign"
    c["updatedAt"] = NOW


def solve_task_12(state):
    """Add Nina Patel to VIP (grp_10)."""
    c = find_contact_by_name(state, "Nina", "Patel")
    if "grp_10" not in c["groups"]:
        c["groups"].append("grp_10")
    c["updatedAt"] = NOW


def solve_task_13(state):
    """Remove Marcus Johnson from Engineering Team (grp_4)."""
    c = find_contact_by_name(state, "Marcus", "Johnson")
    c["groups"] = [g for g in c["groups"] if g != "grp_4"]
    c["updatedAt"] = NOW


def solve_task_14(state):
    """Delete contact Emma Thompson."""
    state["contacts"] = [c for c in state["contacts"]
                         if not (c["firstName"] == "Emma" and c["lastName"] == "Thompson")]


def solve_task_15(state):
    """Delete contact Timothy Buchanan."""
    state["contacts"] = [c for c in state["contacts"]
                         if not (c["firstName"] == "Timothy" and c["lastName"] == "Buchanan")]


def solve_task_16(state):
    """Star Alex Martinez."""
    c = find_contact_by_name(state, "Alex", "Martinez")
    c["starred"] = True
    c["updatedAt"] = NOW


def solve_task_17(state):
    """Unstar David Chen."""
    c = find_contact_by_name(state, "David", "Chen")
    c["starred"] = False
    c["updatedAt"] = NOW


def solve_task_18(state):
    """Star Hannah Cohen."""
    c = find_contact_by_name(state, "Hannah", "Cohen")
    c["starred"] = True
    c["updatedAt"] = NOW


def solve_task_19(state):
    """Create label 'Project Alpha'."""
    gid = next_group_id(state)
    state["contactGroups"].append({
        "id": f"grp_{gid}", "name": "Project Alpha",
        "system": False, "createdAt": NOW, "updatedAt": NOW
    })


def solve_task_20(state):
    """Create label 'Emergency Contacts'."""
    gid = next_group_id(state)
    state["contactGroups"].append({
        "id": f"grp_{gid}", "name": "Emergency Contacts",
        "system": False, "createdAt": NOW, "updatedAt": NOW
    })


def solve_task_21(state):
    """Rename 'Book Club' to 'Reading Circle'."""
    g = find_group_by_name(state, "Book Club")
    g["name"] = "Reading Circle"
    g["updatedAt"] = NOW


def solve_task_22(state):
    """Delete 'College Alumni' label."""
    grp = find_group_by_name(state, "College Alumni")
    grp_id = grp["id"]
    state["contactGroups"] = [g for g in state["contactGroups"] if g["id"] != grp_id]
    for c in state["contacts"]:
        c["groups"] = [g for g in c["groups"] if g != grp_id]


def solve_task_23(state):
    """Remove Ben Watkins from Friends (grp_3)."""
    c = find_contact_by_name(state, "Ben", "Watkins")
    c["groups"] = [g for g in c["groups"] if g != "grp_3"]
    c["updatedAt"] = NOW


def solve_task_24(state):
    """Rename 'Vendors' to 'Technology Partners'."""
    g = find_group_by_name(state, "Vendors")
    g["name"] = "Technology Partners"
    g["updatedAt"] = NOW


def solve_task_25(state):
    """Delete 'Conference Contacts' label."""
    grp = find_group_by_name(state, "Conference Contacts")
    grp_id = grp["id"]
    state["contactGroups"] = [g for g in state["contactGroups"] if g["id"] != grp_id]
    for c in state["contacts"]:
        c["groups"] = [g for g in c["groups"] if g != grp_id]


def solve_task_26(state):
    """Promote other contact jason.recruiter@linkedin.com to main contacts."""
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
    state["otherContacts"] = [o for o in state["otherContacts"] if o["email"] != oc["email"]]


def solve_task_27(state):
    """Delete other contact noreply@github.com."""
    state["otherContacts"] = [o for o in state["otherContacts"] if o["email"] != "noreply@github.com"]


def solve_task_28(state):
    """Promote other contact mike.sales@hubspot.com to main contacts."""
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
    state["otherContacts"] = [o for o in state["otherContacts"] if o["email"] != oc["email"]]


def solve_task_29(state):
    """Delete other contact alex@doordash-driver.com."""
    state["otherContacts"] = [o for o in state["otherContacts"]
                              if o["email"] != "alex@doordash-driver.com"]


def solve_task_30(state):
    """Change account name to Sarah Chen-Williams."""
    state["currentUser"]["firstName"] = "Sarah"
    state["currentUser"]["lastName"] = "Chen-Williams"


def solve_task_31(state):
    """Change first name to Sara, keep last name Chen."""
    state["currentUser"]["firstName"] = "Sara"


def solve_task_32(state):
    """Change recovery email."""
    state["currentUser"]["recoveryEmail"] = "sarah.backup@protonmail.com"


def solve_task_33(state):
    """Change recovery phone."""
    state["currentUser"]["recoveryPhone"] = "+1 (650) 555-0000"


def solve_task_34(state):
    """Disable 2-Step Verification."""
    state["currentUser"]["twoStepVerification"] = False


def solve_task_35(state):
    """Generate app password 'Calendar Sync App'."""
    apid = next_app_password_id(state)
    state["appPasswords"].append({
        "id": f"ap_{apid}", "name": "Calendar Sync App",
        "createdAt": NOW, "lastUsed": None
    })


def solve_task_36(state):
    """Revoke app password 'Outlook Desktop'."""
    state["appPasswords"] = [a for a in state["appPasswords"] if a["name"] != "Outlook Desktop"]


def solve_task_37(state):
    """Revoke app password 'Thunderbird on MacBook'."""
    state["appPasswords"] = [a for a in state["appPasswords"]
                             if a["name"] != "Thunderbird on MacBook"]


def solve_task_38(state):
    """Add alias sarah.personal@gmail.com."""
    aid = next_alias_id(state)
    state["aliases"].append({
        "id": f"alias_{aid}",
        "name": "Sarah Chen (Personal)",
        "email": "sarah.personal@gmail.com",
        "isPrimary": False, "isDefault": False,
        "replyFrom": "default",
        "smtpServer": "smtp.gmail.com",
        "smtpPort": "587",
        "smtpUsername": "sarah.personal@gmail.com",
        "useSSL": True,
        "createdAt": NOW
    })


def solve_task_39(state):
    """Edit alias support@techcorp.io display name."""
    a = find_alias_by_email(state, "support@techcorp.io")
    a["name"] = "TechCorp Support"


def solve_task_40(state):
    """Delete alias schen@alumni.stanford.edu."""
    state["aliases"] = [a for a in state["aliases"]
                        if a["email"] != "schen@alumni.stanford.edu"]


def solve_task_41(state):
    """Set support@techcorp.io as default."""
    for a in state["aliases"]:
        a["isDefault"] = (a["email"] == "support@techcorp.io")


def solve_task_42(state):
    """Change reply-from setting to 'same'."""
    state["replyFromSetting"] = "same"


def solve_task_43(state):
    """Add alias test@example.com with SSL disabled."""
    aid = next_alias_id(state)
    state["aliases"].append({
        "id": f"alias_{aid}",
        "name": "Test Alias",
        "email": "test@example.com",
        "isPrimary": False, "isDefault": False,
        "replyFrom": "default",
        "smtpServer": "smtp.example.com",
        "smtpPort": "25",
        "smtpUsername": "test",
        "useSSL": False,
        "createdAt": NOW
    })


def solve_task_44(state):
    """Delete alias sarah@chen-family.org."""
    state["aliases"] = [a for a in state["aliases"]
                        if a["email"] != "sarah@chen-family.org"]


def solve_task_45(state):
    """Add delegate david.park@techcorp.io."""
    did = next_delegate_id(state)
    state["delegates"].append({
        "id": f"del_{did}",
        "email": "david.park@techcorp.io",
        "name": "David Park",
        "status": "pending",
        "addedAt": NOW
    })


def solve_task_46(state):
    """Remove delegate Alex Martinez."""
    state["delegates"] = [d for d in state["delegates"]
                          if d["email"] != "alex.martinez@techcorp.io"]


def solve_task_47(state):
    """Remove delegate James Wu."""
    state["delegates"] = [d for d in state["delegates"]
                          if d["email"] != "james.wu@techcorp.io"]


def solve_task_48(state):
    """Add delegate jennifer.walsh@techcorp.io."""
    did = next_delegate_id(state)
    state["delegates"].append({
        "id": f"del_{did}",
        "email": "jennifer.walsh@techcorp.io",
        "name": "Jennifer Walsh",
        "status": "pending",
        "addedAt": NOW
    })


def solve_task_49(state):
    """Add POP3 import sarah@personal-blog.com."""
    iid = next_import_id(state)
    state["importAccounts"].append({
        "id": f"imp_{iid}",
        "email": "sarah@personal-blog.com",
        "server": "pop.personal-blog.com",
        "port": "995",
        "username": "sarah",
        "useSSL": True,
        "leaveOnServer": True,
        "labelIncoming": "blog",
        "status": "active",
        "lastChecked": NOW,
        "addedAt": NOW
    })


def solve_task_50(state):
    """Remove import account sarah@old-startup.com."""
    state["importAccounts"] = [i for i in state["importAccounts"]
                               if i["email"] != "sarah@old-startup.com"]


def solve_task_51(state):
    """Remove import account sarahchen.personal@gmail.com."""
    state["importAccounts"] = [i for i in state["importAccounts"]
                               if i["email"] != "sarahchen.personal@gmail.com"]


def solve_task_52(state):
    """Add POP3 import archive@company.com with SSL off, leave on server off."""
    iid = next_import_id(state)
    state["importAccounts"].append({
        "id": f"imp_{iid}",
        "email": "archive@company.com",
        "server": "pop.company.com",
        "port": "110",
        "username": "archive",
        "useSSL": False,
        "leaveOnServer": False,
        "labelIncoming": "company-archive",
        "status": "active",
        "lastChecked": NOW,
        "addedAt": NOW
    })


def solve_task_53(state):
    """Delete contact Jessica Singh."""
    state["contacts"] = [c for c in state["contacts"]
                         if not (c["firstName"] == "Jessica" and c["lastName"] == "Singh")]


def solve_task_54(state):
    """Delete Investors label (grp_5) and clean up contacts."""
    grp = find_group_by_name(state, "Investors")
    grp_id = grp["id"]
    state["contactGroups"] = [g for g in state["contactGroups"] if g["id"] != grp_id]
    for c in state["contacts"]:
        c["groups"] = [g for g in c["groups"] if g != grp_id]


def solve_task_55(state):
    """Add Natalie Dubois to Work (grp_2) and VIP (grp_10)."""
    c = find_contact_by_name(state, "Natalie", "Dubois")
    if "grp_2" not in c["groups"]:
        c["groups"].append("grp_2")
    if "grp_10" not in c["groups"]:
        c["groups"].append("grp_10")
    c["updatedAt"] = NOW


def solve_task_56(state):
    """Create contact with only first name 'TestContact'."""
    cid = next_contact_id(state)
    state["contacts"].append({
        "id": f"ct_{cid}", "firstName": "TestContact", "lastName": "",
        "email": "", "phone": "", "company": "",
        "jobTitle": "", "address": "", "birthday": "", "notes": "",
        "starred": False, "groups": [], "createdAt": NOW, "updatedAt": NOW
    })


def solve_task_57(state):
    """Edit Rachel Park: email and notes."""
    c = find_contact_by_name(state, "Rachel", "Park")
    c["email"] = "rachel.park.personal@gmail.com"
    c["notes"] = "CS professor at Stanford - ML collaboration"
    c["updatedAt"] = NOW


def solve_task_58(state):
    """Clear Tom O'Brien's birthday."""
    c = find_contact_by_name(state, "Tom", "O'Brien")
    c["birthday"] = ""
    c["updatedAt"] = NOW


def solve_task_59(state):
    """Star Olivia Grant and add to VIP (grp_10)."""
    c = find_contact_by_name(state, "Olivia", "Grant")
    c["starred"] = True
    if "grp_10" not in c["groups"]:
        c["groups"].append("grp_10")
    c["updatedAt"] = NOW


def solve_task_60(state):
    """Delete contact Derek Hoffman."""
    state["contacts"] = [c for c in state["contacts"]
                         if not (c["firstName"] == "Derek" and c["lastName"] == "Hoffman")]


def solve_task_61(state):
    """Create label 'Priority Contacts'."""
    gid = next_group_id(state)
    state["contactGroups"].append({
        "id": f"grp_{gid}", "name": "Priority Contacts",
        "system": False, "createdAt": NOW, "updatedAt": NOW
    })


def solve_task_62(state):
    """Delete 'Friends' label and remove grp_3 from all contacts."""
    grp = find_group_by_name(state, "Friends")
    grp_id = grp["id"]
    state["contactGroups"] = [g for g in state["contactGroups"] if g["id"] != grp_id]
    for c in state["contacts"]:
        c["groups"] = [g for g in c["groups"] if g != grp_id]


def solve_task_63(state):
    """Edit support@techcorp.io alias SMTP port and username."""
    a = find_alias_by_email(state, "support@techcorp.io")
    a["smtpPort"] = "465"
    a["smtpUsername"] = "support-admin@techcorp.io"


def solve_task_64(state):
    """Remove all delegates."""
    state["delegates"] = []


def solve_task_65(state):
    """Generate two app passwords."""
    apid1 = next_app_password_id(state)
    state["appPasswords"].append({
        "id": f"ap_{apid1}", "name": "Spark Mac Client",
        "createdAt": NOW, "lastUsed": None
    })
    apid2 = next_app_password_id(state)
    state["appPasswords"].append({
        "id": f"ap_{apid2}", "name": "K-9 Mail Android",
        "createdAt": NOW, "lastUsed": None
    })


def solve_task_66(state):
    """Revoke all existing app passwords."""
    state["appPasswords"] = [a for a in state["appPasswords"]
                             if a["name"] not in {"Thunderbird on MacBook", "Mail on iPhone", "Outlook Desktop"}]


def solve_task_67(state):
    """Change recovery email and phone."""
    state["currentUser"]["recoveryEmail"] = "sarah.chen.recovery@outlook.com"
    state["currentUser"]["recoveryPhone"] = "+1 (510) 555-0100"


def solve_task_68(state):
    """Change first name to 'S.' keep last name 'Chen'."""
    state["currentUser"]["firstName"] = "S."


def solve_task_69(state):
    """Delete other contact meetingbot@calendly.com."""
    state["otherContacts"] = [o for o in state["otherContacts"]
                              if o["email"] != "meetingbot@calendly.com"]


def solve_task_70(state):
    """Delete other contact receipts@uber.com."""
    state["otherContacts"] = [o for o in state["otherContacts"]
                              if o["email"] != "receipts@uber.com"]


def solve_task_71(state):
    """Promote other contact billing@aws.amazon.com to main contacts."""
    oc = find_other_by_email(state, "billing@aws.amazon.com")
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
    state["otherContacts"] = [o for o in state["otherContacts"] if o["email"] != oc["email"]]


def solve_task_72(state):
    """Edit Kevin Chen: company and job title."""
    c = find_contact_by_name(state, "Kevin", "Chen")
    c["company"] = "Google"
    c["jobTitle"] = "Senior Product Manager"
    c["updatedAt"] = NOW


def solve_task_73(state):
    """Create contact Multi Label with Work, Engineering Team, and VIP labels."""
    cid = next_contact_id(state)
    state["contacts"].append({
        "id": f"ct_{cid}", "firstName": "Multi", "lastName": "Label",
        "email": "multi.label@test.com", "phone": "", "company": "",
        "jobTitle": "", "address": "", "birthday": "", "notes": "",
        "starred": False, "groups": ["grp_2", "grp_4", "grp_10"],
        "createdAt": NOW, "updatedAt": NOW
    })


def solve_task_74(state):
    """Edit alias sarah@chen-family.org display name."""
    a = find_alias_by_email(state, "sarah@chen-family.org")
    a["name"] = "Sarah (Family)"


def solve_task_75(state):
    """Delete contact Henry Wright."""
    state["contacts"] = [c for c in state["contacts"]
                         if not (c["firstName"] == "Henry" and c["lastName"] == "Wright")]


def solve_task_76(state):
    """Edit Ben Watkins: company and job title."""
    c = find_contact_by_name(state, "Ben", "Watkins")
    c["company"] = "Watkins Photography"
    c["jobTitle"] = "Professional Photographer"
    c["updatedAt"] = NOW


def solve_task_77(state):
    """Add Marcus Johnson to Investors (grp_5)."""
    c = find_contact_by_name(state, "Marcus", "Johnson")
    if "grp_5" not in c["groups"]:
        c["groups"].append("grp_5")
    c["updatedAt"] = NOW


def solve_task_78(state):
    """Edit Natalie Dubois: phone and company."""
    c = find_contact_by_name(state, "Natalie", "Dubois")
    c["phone"] = "+33 7 99 88 77 66"
    c["company"] = "DesignStudio Paris"
    c["updatedAt"] = NOW


def solve_task_79(state):
    """Add POP3 import sarah@consulting.dev with SSL off, leave off."""
    iid = next_import_id(state)
    state["importAccounts"].append({
        "id": f"imp_{iid}",
        "email": "sarah@consulting.dev",
        "server": "pop.consulting.dev",
        "port": "110",
        "username": "sarah.consulting",
        "useSSL": False,
        "leaveOnServer": False,
        "labelIncoming": "consulting-work",
        "status": "active",
        "lastChecked": NOW,
        "addedAt": NOW
    })


def solve_task_80(state):
    """Add Sophia Andersson to Engineering Team (grp_4) and Conference Contacts (grp_8)."""
    c = find_contact_by_name(state, "Sophia", "Andersson")
    if "grp_4" not in c["groups"]:
        c["groups"].append("grp_4")
    if "grp_8" not in c["groups"]:
        c["groups"].append("grp_8")
    c["updatedAt"] = NOW


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
    "task_61": solve_task_61,
    "task_62": solve_task_62,
    "task_63": solve_task_63,
    "task_64": solve_task_64,
    "task_65": solve_task_65,
    "task_66": solve_task_66,
    "task_67": solve_task_67,
    "task_68": solve_task_68,
    "task_69": solve_task_69,
    "task_70": solve_task_70,
    "task_71": solve_task_71,
    "task_72": solve_task_72,
    "task_73": solve_task_73,
    "task_74": solve_task_74,
    "task_75": solve_task_75,
    "task_76": solve_task_76,
    "task_77": solve_task_77,
    "task_78": solve_task_78,
    "task_79": solve_task_79,
    "task_80": solve_task_80,
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
    parser = argparse.ArgumentParser(description="Gmail Accounts & Contacts function-task sanity check")
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
