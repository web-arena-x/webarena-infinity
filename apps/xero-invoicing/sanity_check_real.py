#!/usr/bin/env python3
"""
Sanity check for xero-invoicing real tasks.

For each task: reset → apply solve (state mutation) → verify → assert pass.
Validates that verifiers correctly recognize solved tasks.
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

import requests

APP_DIR = os.path.dirname(os.path.abspath(__file__))
TASKS_FILE = os.path.join(APP_DIR, "real-tasks.json")
DATA_JS = os.path.join(APP_DIR, "js", "data.js")
SERVER_PY = os.path.join(APP_DIR, "server.py")

# ---------------------------------------------------------------------------
# Seed state generation
# ---------------------------------------------------------------------------

_SEED_STATE_JS = r"""
const fs = require('fs');
const vm = require('vm');
const code = fs.readFileSync(process.argv[1], 'utf8');
vm.runInThisContext(code);

const state = {
    _seedVersion: SEED_DATA_VERSION,
    contacts: JSON.parse(JSON.stringify(CONTACTS)),
    invoices: JSON.parse(JSON.stringify(INVOICES)),
    quotes: JSON.parse(JSON.stringify(QUOTES)),
    creditNotes: JSON.parse(JSON.stringify(CREDIT_NOTES)),
    repeatingInvoices: JSON.parse(JSON.stringify(REPEATING_INVOICES)),
    items: JSON.parse(JSON.stringify(ITEMS)),
    taxRates: JSON.parse(JSON.stringify(TAX_RATES)),
    accounts: JSON.parse(JSON.stringify(ACCOUNTS)),
    trackingCategories: JSON.parse(JSON.stringify(TRACKING_CATEGORIES)),
    currencies: JSON.parse(JSON.stringify(CURRENCIES)),
    brandingThemes: JSON.parse(JSON.stringify(BRANDING_THEMES)),
    invoiceSettings: JSON.parse(JSON.stringify(INVOICE_SETTINGS)),
    invoiceReminders: JSON.parse(JSON.stringify(INVOICE_REMINDERS)),
    currentUser: JSON.parse(JSON.stringify(CURRENT_USER)),
    _nextInvoiceNum: INVOICE_SETTINGS.invoiceNextNumber,
    _nextQuoteNum: INVOICE_SETTINGS.quoteNextNumber,
    _nextCreditNoteNum: INVOICE_SETTINGS.creditNoteNextNumber,
    _nextContactId: 26,
    _nextItemId: 16,
    _nextReminderId: 5,
    _nextRepeatId: 6,
    _nextLineItemId: 1000,
    _nextPaymentId: 100,
    _nextThemeId: 5,
};
process.stdout.write(JSON.stringify(state));
"""


def generate_seed_state() -> dict:
    result = subprocess.run(
        ["node", "-e", _SEED_STATE_JS, DATA_JS],
        capture_output=True, text=True, timeout=10,
    )
    if result.returncode != 0:
        raise RuntimeError(f"Seed state generation failed:\n{result.stderr}")
    return json.loads(result.stdout)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def find_entity(entities, **kwargs):
    for e in entities:
        if all(e.get(k) == v for k, v in kwargs.items()):
            return e
    raise ValueError(f"Entity not found: {kwargs}")


def find_invoice(state, number):
    return find_entity(state["invoices"], number=number)


def find_quote(state, number):
    return find_entity(state["quotes"], number=number)


def find_credit_note(state, number):
    return find_entity(state["creditNotes"], number=number)


def find_contact(state, name):
    return find_entity(state["contacts"], name=name)


def find_reminder(state, timing, days):
    return find_entity(state["invoiceReminders"], timing=timing, days=days)


def find_theme(state, id):
    return find_entity(state["brandingThemes"], id=id)


def find_repeating(state, id):
    return find_entity(state["repeatingInvoices"], id=id)


# ---------------------------------------------------------------------------
# Solve functions — one per task, derived from verifiers
# ---------------------------------------------------------------------------

# ===== EASY =====

def solve_task_e1(state):
    """Approve the draft invoice for Murray River Winery."""
    inv = find_invoice(state, "INV-0058")
    inv["status"] = "awaiting_payment"


def solve_task_e2(state):
    """Delete the Bright Spark Electrical draft invoice."""
    inv = find_invoice(state, "INV-0059")
    inv["status"] = "deleted"


def solve_task_e3(state):
    """Void the invoice for Sapphire Bay Resort."""
    inv = find_invoice(state, "INV-0054")
    inv["status"] = "voided"
    inv["amountDue"] = 0


def solve_task_e4(state):
    """Accept Redback Mining's quote."""
    quo = find_quote(state, "QU-0023")
    quo["status"] = "accepted"


def solve_task_e5(state):
    """Decline Metro Fabrication Works' quote."""
    quo = find_quote(state, "QU-0028")
    quo["status"] = "declined"


def solve_task_e6(state):
    """Delete the declined Horizon Media quote."""
    quo = find_quote(state, "QU-0026")
    quo["status"] = "deleted"


def solve_task_e7(state):
    """Approve the Pacific Freight Lines credit note."""
    cn = find_credit_note(state, "CN-0011")
    cn["status"] = "awaiting_payment"


def solve_task_e8(state):
    """Turn on the 30-day overdue reminder."""
    rem = find_reminder(state, "after", 30)
    rem["enabled"] = True


def solve_task_e9(state):
    """Disable the upcoming-due-date invoice reminder."""
    rem = find_reminder(state, "before", 7)
    rem["enabled"] = False


def solve_task_e10(state):
    """Make Professional Services the default branding theme."""
    for t in state["brandingThemes"]:
        t["isDefault"] = (t["id"] == "theme_professional")


def solve_task_e11(state):
    """Remove the Simple Clean branding theme."""
    state["brandingThemes"] = [t for t in state["brandingThemes"] if t["id"] != "theme_simple"]


def solve_task_e12(state):
    """Hide the tax column on invoices."""
    state["invoiceSettings"]["showTaxColumn"] = False


def solve_task_e13(state):
    """Switch to tax-inclusive pricing by default."""
    state["invoiceSettings"]["defaultTaxMode"] = "inclusive"


def solve_task_e14(state):
    """Turn off the discount column."""
    state["invoiceSettings"]["showDiscountColumn"] = False


def solve_task_e15(state):
    """Stop displaying item codes on invoices."""
    state["invoiceSettings"]["showItemCode"] = False


def solve_task_e16(state):
    """Cancel the Summit Health Group repeating invoice."""
    state["repeatingInvoices"] = [r for r in state["repeatingInvoices"] if r["id"] != "rep_005"]


def solve_task_e17(state):
    """Submit the Redback Mining Supplies invoice for approval."""
    inv = find_invoice(state, "INV-0060")
    inv["status"] = "awaiting_approval"


def solve_task_e18(state):
    """Mark the Stellar Education Services invoice as sent."""
    inv = find_invoice(state, "INV-0057")
    inv["status"] = "awaiting_payment"
    inv["sentAt"] = "2026-03-02T12:00:00Z"


def solve_task_e19(state):
    """Delete the two-week overdue reminder."""
    state["invoiceReminders"] = [
        r for r in state["invoiceReminders"]
        if not (r["timing"] == "after" and r["days"] == 14)
    ]


def solve_task_e20(state):
    """Hide the ABN on the Standard template."""
    theme = find_theme(state, "theme_standard")
    theme["showTaxNumber"] = False


# ===== MEDIUM =====

def solve_task_m1(state):
    """Pay off the Vanguard Security Systems invoice in full."""
    inv = find_invoice(state, "INV-0053")
    pay_id = f"pay_{state['_nextPaymentId']}"
    state["_nextPaymentId"] += 1
    inv["payments"].append({
        "id": pay_id,
        "date": "2026-03-02",
        "amount": 823.90,
        "reference": "",
        "accountId": "acc_090",
    })
    inv["amountPaid"] = 823.90
    inv["amountDue"] = 0
    inv["status"] = "paid"


def solve_task_m2(state):
    """Close out the remaining balance on Pinnacle Construction's January invoice."""
    inv = find_invoice(state, "INV-0045")
    pay_id = f"pay_{state['_nextPaymentId']}"
    state["_nextPaymentId"] += 1
    remaining = inv["total"] - inv["amountPaid"]
    inv["payments"].append({
        "id": pay_id,
        "date": "2026-03-02",
        "amount": remaining,
        "reference": "",
        "accountId": "acc_090",
    })
    inv["amountPaid"] = inv["total"]
    inv["amountDue"] = 0
    inv["status"] = "paid"


def solve_task_m3(state):
    """Make a copy of the Baxter & Associates Legal invoice."""
    src = find_invoice(state, "INV-0046")
    copy = deepcopy(src)
    num = state["_nextInvoiceNum"]
    copy["id"] = f"inv_{num:03d}"
    copy["number"] = state["invoiceSettings"]["invoicePrefix"] + f"{num:04d}"
    state["_nextInvoiceNum"] = num + 1
    copy["status"] = "draft"
    copy["payments"] = []
    copy["amountPaid"] = 0
    copy["amountDue"] = copy["total"]
    copy["sentAt"] = None
    copy["notes"] = [{"date": "2026-03-02T12:00:00Z", "text": f"Copied from {src['number']}", "user": "Sarah Mitchell"}]
    lid = state["_nextLineItemId"]
    for li in copy["lineItems"]:
        li["id"] = f"li_{lid}"
        lid += 1
    state["_nextLineItemId"] = lid
    state["invoices"].append(copy)


def solve_task_m4(state):
    """Convert the accepted Pinnacle Construction quote into a draft invoice."""
    quo = find_quote(state, "QU-0022")
    num = state["_nextInvoiceNum"]
    lid = state["_nextLineItemId"]
    line_items = deepcopy(quo["lineItems"])
    for li in line_items:
        li["id"] = f"li_{lid}"
        lid += 1
    inv = {
        "id": f"inv_{num:03d}",
        "number": state["invoiceSettings"]["invoicePrefix"] + f"{num:04d}",
        "contactId": quo["contactId"],
        "status": "draft",
        "date": "2026-03-02",
        "dueDate": "2026-04-01",
        "reference": quo["reference"],
        "currency": quo["currency"],
        "brandingThemeId": quo["brandingThemeId"],
        "taxMode": quo["taxMode"],
        "lineItems": line_items,
        "subtotal": quo["subtotal"],
        "taxTotal": quo["taxTotal"],
        "total": quo["total"],
        "amountDue": quo["total"],
        "amountPaid": 0,
        "payments": [],
        "notes": [{"date": "2026-03-02T12:00:00Z", "text": "Invoice created", "user": "Sarah Mitchell"}],
        "sentAt": None,
        "title": quo["title"],
        "summary": quo["summary"],
    }
    state["invoices"].append(inv)
    state["_nextInvoiceNum"] = num + 1
    state["_nextLineItemId"] = lid
    quo["isInvoiced"] = True


def solve_task_m5(state):
    """Apply Coastal Living Interiors' credit note against their open invoice."""
    cn = find_credit_note(state, "CN-0009")
    inv = find_invoice(state, "INV-0049")
    amount = 249.75
    cn["allocations"].append({
        "invoiceId": inv["id"],
        "invoiceNumber": inv["number"],
        "amount": amount,
        "date": "2026-03-02",
    })
    cn["remainingCredit"] -= amount
    if cn["remainingCredit"] <= 0.005:
        cn["status"] = "paid"
        cn["remainingCredit"] = 0
    inv["amountPaid"] += amount
    inv["amountDue"] -= amount
    if inv["amountDue"] <= 0.005:
        inv["status"] = "paid"
        inv["amountDue"] = 0


def solve_task_m6(state):
    """Change CloudNine Analytics repeating invoice from monthly to quarterly."""
    ri = find_repeating(state, "rep_002")
    ri["frequency"] = "quarterly"


def solve_task_m7(state):
    """Set the Greenfield Organics repeating invoice to end on June 30, 2027."""
    ri = find_repeating(state, "rep_001")
    ri["endDate"] = "2027-06-30"


def solve_task_m8(state):
    """Update the invoice number prefix to TAX-."""
    state["invoiceSettings"]["invoicePrefix"] = "TAX-"


def solve_task_m9(state):
    """Switch the credit note prefix to CR-."""
    state["invoiceSettings"]["creditNotePrefix"] = "CR-"


def solve_task_m10(state):
    """Create a new branding theme called 'Modern Minimalist'."""
    tid = state["_nextThemeId"]
    state["_nextThemeId"] = tid + 1
    theme = {
        "id": f"theme_{tid}",
        "name": "Modern Minimalist",
        "isDefault": False,
        "logoUrl": "",
        "paymentTerms": "Net 14 days",
        "termsAndConditions": "",
        "showTaxNumber": True,
        "showPaymentAdvice": True,
    }
    state["brandingThemes"].append(theme)


def solve_task_m11(state):
    """Add reference 'MRW-WEB-MARCH' to Murray River Winery draft invoice."""
    inv = find_invoice(state, "INV-0058")
    inv["reference"] = "MRW-WEB-MARCH"


def solve_task_m12(state):
    """Add reference 'Cascade monthly license' to Cascade Software repeating invoice."""
    ri = find_repeating(state, "rep_003")
    ri["reference"] = "Cascade monthly license"


def solve_task_m13(state):
    """Set the title of the Fresh Start Catering quote to 'Online Catering Portal'."""
    quo = find_quote(state, "QU-0025")
    quo["title"] = "Online Catering Portal"


def solve_task_m14(state):
    """Change the default payment terms to end of the following month."""
    state["invoiceSettings"]["defaultDueDate"] = {"type": "endOfFollowingMonth", "days": 0}


def solve_task_m15(state):
    """Send the Fresh Start Catering draft quote."""
    quo = find_quote(state, "QU-0025")
    quo["status"] = "sent"
    quo["sentAt"] = "2026-03-02T12:00:00Z"


def solve_task_m16(state):
    """Rename the Retail branding theme to 'Retail Premium'."""
    theme = find_theme(state, "theme_retail")
    theme["name"] = "Retail Premium"


def solve_task_m17(state):
    """Update the Professional Services template's terms and conditions."""
    theme = find_theme(state, "theme_professional")
    theme["termsAndConditions"] = "All work is subject to our Master Services Agreement. Payment terms are strictly net 30 days."


def solve_task_m18(state):
    """Change the 1-day overdue reminder subject."""
    rem = find_reminder(state, "after", 1)
    rem["subject"] = "Payment Required - {InvoiceNumber}"


def solve_task_m19(state):
    """Reverse the partial payment on the Pinnacle Construction invoice."""
    inv = find_invoice(state, "INV-0045")
    inv["payments"] = []
    inv["amountPaid"] = 0
    inv["amountDue"] = inv["total"]
    if inv["status"] == "paid":
        inv["status"] = "awaiting_payment"


def solve_task_m20(state):
    """Duplicate the Atlas Engineering quote."""
    src = find_quote(state, "QU-0024")
    copy = deepcopy(src)
    num = state["_nextQuoteNum"]
    copy["id"] = f"quo_{num:03d}"
    copy["number"] = state["invoiceSettings"]["quotePrefix"] + f"{num:04d}"
    state["_nextQuoteNum"] = num + 1
    copy["status"] = "draft"
    copy["sentAt"] = None
    copy["isInvoiced"] = False
    copy["notes"] = [{"date": "2026-03-02T12:00:00Z", "text": f"Copied from {src['number']}", "user": "Sarah Mitchell"}]
    lid = state["_nextLineItemId"]
    for li in copy["lineItems"]:
        li["id"] = f"li_{lid}"
        lid += 1
    state["_nextLineItemId"] = lid
    state["quotes"].append(copy)


# ===== HARD =====

def solve_task_h1(state):
    """Invoice TechVault Solutions for 10 hours of development work."""
    contact = find_contact(state, "TechVault Solutions Pty Ltd")
    num = state["_nextInvoiceNum"]
    lid = state["_nextLineItemId"]
    subtotal = 10 * 185.00
    tax = subtotal * 0.10
    total = subtotal + tax
    inv = {
        "id": f"inv_{num:03d}",
        "number": state["invoiceSettings"]["invoicePrefix"] + f"{num:04d}",
        "contactId": contact["id"],
        "status": "draft",
        "date": "2026-03-02",
        "dueDate": "2026-04-01",
        "reference": "",
        "currency": "AUD",
        "brandingThemeId": "theme_standard",
        "taxMode": "exclusive",
        "lineItems": [{
            "id": f"li_{lid}",
            "itemId": "item_001",
            "description": "Software Development - Hourly Rate",
            "quantity": 10,
            "unitPrice": 185.00,
            "discountPercent": 0,
            "accountId": "acc_200",
            "taxRateId": "tax_gst",
            "trackingRegion": "",
            "trackingDept": "",
        }],
        "subtotal": subtotal,
        "taxTotal": tax,
        "total": total,
        "amountDue": total,
        "amountPaid": 0,
        "payments": [],
        "notes": [{"date": "2026-03-02T12:00:00Z", "text": "Invoice created", "user": "Sarah Mitchell"}],
        "sentAt": None,
        "title": "",
        "summary": "",
    }
    state["invoices"].append(inv)
    state["_nextInvoiceNum"] = num + 1
    state["_nextLineItemId"] = lid + 1


def solve_task_h2(state):
    """Bill Wellington & Partners in US dollars for 12 hours of consulting."""
    contact = find_contact(state, "Wellington & Partners Accounting")
    num = state["_nextInvoiceNum"]
    lid = state["_nextLineItemId"]
    subtotal = 12 * 250.00
    tax = 0
    total = subtotal + tax
    inv = {
        "id": f"inv_{num:03d}",
        "number": state["invoiceSettings"]["invoicePrefix"] + f"{num:04d}",
        "contactId": contact["id"],
        "status": "draft",
        "date": "2026-03-02",
        "dueDate": "2026-04-01",
        "reference": "",
        "currency": "USD",
        "brandingThemeId": "theme_standard",
        "taxMode": "exclusive",
        "lineItems": [{
            "id": f"li_{lid}",
            "itemId": "item_002",
            "description": "Consulting Services - Per Hour",
            "quantity": 12,
            "unitPrice": 250.00,
            "discountPercent": 0,
            "accountId": "acc_260",
            "taxRateId": "tax_gst_free",
            "trackingRegion": "",
            "trackingDept": "",
        }],
        "subtotal": subtotal,
        "taxTotal": tax,
        "total": total,
        "amountDue": total,
        "amountPaid": 0,
        "payments": [],
        "notes": [{"date": "2026-03-02T12:00:00Z", "text": "Invoice created", "user": "Sarah Mitchell"}],
        "sentAt": None,
        "title": "",
        "summary": "",
    }
    state["invoices"].append(inv)
    state["_nextInvoiceNum"] = num + 1
    state["_nextLineItemId"] = lid + 1


def solve_task_h3(state):
    """Issue a $100 hosting credit to Greenfield Organics."""
    contact = find_contact(state, "Greenfield Organics")
    num = state["_nextCreditNoteNum"]
    lid = state["_nextLineItemId"]
    subtotal = 100.00
    tax = 10.00
    total = subtotal + tax
    cn = {
        "id": f"cn_{num:03d}",
        "number": state["invoiceSettings"]["creditNotePrefix"] + f"{num:04d}",
        "contactId": contact["id"],
        "status": "draft",
        "date": "2026-03-02",
        "reference": "",
        "currency": "AUD",
        "brandingThemeId": "theme_standard",
        "taxMode": "exclusive",
        "lineItems": [{
            "id": f"li_{lid}",
            "itemId": None,
            "description": "Hosting credit adjustment",
            "quantity": 1,
            "unitPrice": 100.00,
            "discountPercent": 0,
            "accountId": "acc_200",
            "taxRateId": "tax_gst",
            "trackingRegion": "",
            "trackingDept": "",
        }],
        "subtotal": subtotal,
        "taxTotal": tax,
        "total": total,
        "remainingCredit": total,
        "allocations": [],
        "refunds": [],
        "notes": [{"date": "2026-03-02T12:00:00Z", "text": "Credit note created", "user": "Sarah Mitchell"}],
    }
    state["creditNotes"].append(cn)
    state["_nextCreditNoteNum"] = num + 1
    state["_nextLineItemId"] = lid + 1


def solve_task_h4(state):
    """Create and approve a credit note for TechVault for a rate adjustment."""
    contact = find_contact(state, "TechVault Solutions Pty Ltd")
    num = state["_nextCreditNoteNum"]
    lid = state["_nextLineItemId"]
    subtotal = 4 * 25.00
    tax = subtotal * 0.10
    total = subtotal + tax
    cn = {
        "id": f"cn_{num:03d}",
        "number": state["invoiceSettings"]["creditNotePrefix"] + f"{num:04d}",
        "contactId": contact["id"],
        "status": "awaiting_payment",
        "date": "2026-03-02",
        "reference": "",
        "currency": "AUD",
        "brandingThemeId": "theme_standard",
        "taxMode": "exclusive",
        "lineItems": [{
            "id": f"li_{lid}",
            "itemId": None,
            "description": "Rate adjustment",
            "quantity": 4,
            "unitPrice": 25.00,
            "discountPercent": 0,
            "accountId": "acc_260",
            "taxRateId": "tax_gst",
            "trackingRegion": "",
            "trackingDept": "",
        }],
        "subtotal": subtotal,
        "taxTotal": tax,
        "total": total,
        "remainingCredit": total,
        "allocations": [],
        "refunds": [],
        "notes": [{"date": "2026-03-02T12:00:00Z", "text": "Credit note created", "user": "Sarah Mitchell"}],
    }
    state["creditNotes"].append(cn)
    state["_nextCreditNoteNum"] = num + 1
    state["_nextLineItemId"] = lid + 1


def solve_task_h5(state):
    """Set up monthly billing for Bright Spark Electrical for cloud hosting."""
    contact = find_contact(state, "Bright Spark Electrical")
    rid = state["_nextRepeatId"]
    state["_nextRepeatId"] = rid + 1
    ri = {
        "id": f"rep_{rid:03d}",
        "contactId": contact["id"],
        "status": "draft",
        "frequency": "monthly",
        "startDate": "2026-04-01",
        "nextDate": "2026-04-01",
        "endDate": "",
        "currency": "AUD",
        "brandingThemeId": "theme_standard",
        "taxMode": "exclusive",
        "saveAs": "draft",
        "lineItems": [{
            "id": f"rli_{rid * 10}",
            "itemId": "item_004",
            "description": "Cloud Hosting - Monthly",
            "quantity": 1,
            "unitPrice": 299.00,
            "accountId": "acc_200",
            "taxRateId": "tax_gst",
        }],
        "dueDate": {"type": "daysAfterInvoice", "days": 30},
        "reference": "",
        "emailSubject": "",
        "emailBody": "",
    }
    state["repeatingInvoices"].append(ri)


def solve_task_h6(state):
    """Set up quarterly auto-approved recurring invoices for Southern Cross Veterinary."""
    contact = find_contact(state, "Southern Cross Veterinary")
    rid = state["_nextRepeatId"]
    state["_nextRepeatId"] = rid + 1
    ri = {
        "id": f"rep_{rid:03d}",
        "contactId": contact["id"],
        "status": "draft",
        "frequency": "quarterly",
        "startDate": "2026-04-01",
        "nextDate": "2026-04-01",
        "endDate": "",
        "currency": "AUD",
        "brandingThemeId": "theme_standard",
        "taxMode": "exclusive",
        "saveAs": "approved",
        "lineItems": [{
            "id": f"rli_{rid * 10}",
            "itemId": "item_005",
            "description": "Technical Support - Monthly Plan",
            "quantity": 1,
            "unitPrice": 450.00,
            "accountId": "acc_200",
            "taxRateId": "tax_gst_free",
        }],
        "dueDate": {"type": "daysAfterInvoice", "days": 30},
        "reference": "",
        "emailSubject": "",
        "emailBody": "",
    }
    state["repeatingInvoices"].append(ri)


def solve_task_h7(state):
    """Add a 21-day overdue reminder."""
    rid = state["_nextReminderId"]
    state["_nextReminderId"] = rid + 1
    rem = {
        "id": f"rem_{rid:03d}",
        "enabled": True,
        "timing": "after",
        "days": 21,
        "subject": "Third reminder: Invoice overdue - {InvoiceNumber}",
        "body": "Dear {ContactName}, Invoice {InvoiceNumber} is now 21 days past due. Please arrange immediate payment.",
        "includeInvoicePdf": True,
        "includeSummary": True,
    }
    state["invoiceReminders"].append(rem)


def solve_task_h8(state):
    """Quote Southern Cross Veterinary for 8 hours of consulting."""
    contact = find_contact(state, "Southern Cross Veterinary")
    num = state["_nextQuoteNum"]
    lid = state["_nextLineItemId"]
    subtotal = 8 * 250.00
    tax = 0
    total = subtotal + tax
    quo = {
        "id": f"quo_{num:03d}",
        "number": state["invoiceSettings"]["quotePrefix"] + f"{num:04d}",
        "contactId": contact["id"],
        "status": "draft",
        "date": "2026-03-02",
        "expiryDate": "2026-04-01",
        "reference": "",
        "currency": "AUD",
        "brandingThemeId": "theme_standard",
        "taxMode": "exclusive",
        "lineItems": [{
            "id": f"li_{lid}",
            "itemId": "item_002",
            "description": "Consulting Services - Per Hour",
            "quantity": 8,
            "unitPrice": 250.00,
            "discountPercent": 0,
            "accountId": "acc_260",
            "taxRateId": "tax_gst_free",
            "trackingRegion": "",
            "trackingDept": "",
        }],
        "subtotal": subtotal,
        "taxTotal": tax,
        "total": total,
        "title": "",
        "summary": "",
        "terms": "",
        "notes": [{"date": "2026-03-02T12:00:00Z", "text": "Quote created", "user": "Sarah Mitchell"}],
        "sentAt": None,
        "isInvoiced": False,
    }
    state["quotes"].append(quo)
    state["_nextQuoteNum"] = num + 1
    state["_nextLineItemId"] = lid + 1


def solve_task_h9(state):
    """Convert the accepted Alpha Logistics quote into a draft invoice."""
    quo = find_quote(state, "QU-0029")
    num = state["_nextInvoiceNum"]
    lid = state["_nextLineItemId"]
    line_items = deepcopy(quo["lineItems"])
    for li in line_items:
        li["id"] = f"li_{lid}"
        lid += 1
    inv = {
        "id": f"inv_{num:03d}",
        "number": state["invoiceSettings"]["invoicePrefix"] + f"{num:04d}",
        "contactId": quo["contactId"],
        "status": "draft",
        "date": "2026-03-02",
        "dueDate": "2026-04-01",
        "reference": quo["reference"],
        "currency": quo["currency"],
        "brandingThemeId": quo["brandingThemeId"],
        "taxMode": quo["taxMode"],
        "lineItems": line_items,
        "subtotal": quo["subtotal"],
        "taxTotal": quo["taxTotal"],
        "total": quo["total"],
        "amountDue": quo["total"],
        "amountPaid": 0,
        "payments": [],
        "notes": [
            {"date": "2026-03-02T12:00:00Z", "text": "Invoice created", "user": "Sarah Mitchell"},
            {"date": "2026-03-02T12:00:01Z", "text": f"Created from quote {quo['number']}", "user": "Sarah Mitchell"},
        ],
        "sentAt": None,
        "title": quo["title"],
        "summary": quo["summary"],
    }
    state["invoices"].append(inv)
    state["_nextInvoiceNum"] = num + 1
    state["_nextLineItemId"] = lid
    quo["isInvoiced"] = True


def solve_task_h10(state):
    """Apply CloudNine Analytics' credit note against their largest outstanding invoice."""
    cn = find_credit_note(state, "CN-0012")
    inv = find_invoice(state, "INV-0047")
    amount = 2035.00
    cn["allocations"].append({
        "invoiceId": inv["id"],
        "invoiceNumber": inv["number"],
        "amount": amount,
        "date": "2026-03-02",
    })
    cn["remainingCredit"] -= amount
    if cn["remainingCredit"] <= 0.005:
        cn["status"] = "paid"
        cn["remainingCredit"] = 0
    inv["amountPaid"] += amount
    inv["amountDue"] -= amount
    if inv["amountDue"] <= 0.005:
        inv["status"] = "paid"
        inv["amountDue"] = 0


def solve_task_h11(state):
    """Record a $5,000 partial payment on the Cascade Software Solutions invoice."""
    inv = find_invoice(state, "INV-0052")
    pay_id = f"pay_{state['_nextPaymentId']}"
    state["_nextPaymentId"] += 1
    inv["payments"].append({
        "id": pay_id,
        "date": "2026-03-02",
        "amount": 5000.00,
        "reference": "",
        "accountId": "acc_090",
    })
    inv["amountPaid"] += 5000.00
    inv["amountDue"] = inv["total"] - inv["amountPaid"]


def solve_task_h12(state):
    """Update invoice numbering to start at TAX-0100."""
    state["invoiceSettings"]["invoicePrefix"] = "TAX-"
    state["invoiceSettings"]["invoiceNextNumber"] = 100


def solve_task_h13(state):
    """Approve the Horizon Media invoice and send it out."""
    inv = find_invoice(state, "INV-0056")
    inv["status"] = "awaiting_payment"
    inv["sentAt"] = "2026-03-02T12:00:00Z"


def solve_task_h14(state):
    """Set up monthly auto-sent hosting invoices for Harbour City Plumbing."""
    contact = find_contact(state, "Harbour City Plumbing")
    rid = state["_nextRepeatId"]
    state["_nextRepeatId"] = rid + 1
    ri = {
        "id": f"rep_{rid:03d}",
        "contactId": contact["id"],
        "status": "draft",
        "frequency": "monthly",
        "startDate": "2026-04-01",
        "nextDate": "2026-04-01",
        "endDate": "",
        "currency": "AUD",
        "brandingThemeId": "theme_standard",
        "taxMode": "exclusive",
        "saveAs": "approved_for_sending",
        "lineItems": [{
            "id": f"rli_{rid * 10}",
            "itemId": "item_004",
            "description": "Cloud Hosting - Monthly",
            "quantity": 1,
            "unitPrice": 299.00,
            "accountId": "acc_200",
            "taxRateId": "tax_gst",
        }],
        "dueDate": {"type": "daysAfterInvoice", "days": 30},
        "reference": "",
        "emailSubject": "",
        "emailBody": "",
    }
    state["repeatingInvoices"].append(ri)


def solve_task_h15(state):
    """Create a new 'Corporate' branding theme."""
    tid = state["_nextThemeId"]
    state["_nextThemeId"] = tid + 1
    theme = {
        "id": f"theme_{tid}",
        "name": "Corporate",
        "isDefault": False,
        "logoUrl": "",
        "paymentTerms": "Payment due within 7 business days",
        "termsAndConditions": "",
        "showTaxNumber": True,
        "showPaymentAdvice": False,
    }
    state["brandingThemes"].append(theme)


def solve_task_h16(state):
    """Bill Sapphire Bay Resort for 3 days of on-site training."""
    contact = find_contact(state, "Sapphire Bay Resort")
    num = state["_nextInvoiceNum"]
    lid = state["_nextLineItemId"]
    subtotal = 3 * 2200.00
    tax = subtotal * 0.10
    total = subtotal + tax
    inv = {
        "id": f"inv_{num:03d}",
        "number": state["invoiceSettings"]["invoicePrefix"] + f"{num:04d}",
        "contactId": contact["id"],
        "status": "draft",
        "date": "2026-03-02",
        "dueDate": "2026-04-01",
        "reference": "",
        "currency": "AUD",
        "brandingThemeId": "theme_standard",
        "taxMode": "exclusive",
        "lineItems": [{
            "id": f"li_{lid}",
            "itemId": "item_006",
            "description": "On-site Training - Per Day",
            "quantity": 3,
            "unitPrice": 2200.00,
            "discountPercent": 0,
            "accountId": "acc_200",
            "taxRateId": "tax_gst",
            "trackingRegion": "",
            "trackingDept": "",
        }],
        "subtotal": subtotal,
        "taxTotal": tax,
        "total": total,
        "amountDue": total,
        "amountPaid": 0,
        "payments": [],
        "notes": [{"date": "2026-03-02T12:00:00Z", "text": "Invoice created", "user": "Sarah Mitchell"}],
        "sentAt": None,
        "title": "",
        "summary": "",
    }
    state["invoices"].append(inv)
    state["_nextInvoiceNum"] = num + 1
    state["_nextLineItemId"] = lid + 1


def solve_task_h17(state):
    """Create an invoice for Outback Adventures covering security audit and data migration."""
    contact = find_contact(state, "Outback Adventures Tourism")
    num = state["_nextInvoiceNum"]
    lid = state["_nextLineItemId"]
    subtotal = 5500.00 + 3800.00
    tax = subtotal * 0.10
    total = subtotal + tax
    inv = {
        "id": f"inv_{num:03d}",
        "number": state["invoiceSettings"]["invoicePrefix"] + f"{num:04d}",
        "contactId": contact["id"],
        "status": "draft",
        "date": "2026-03-02",
        "dueDate": "2026-04-01",
        "reference": "",
        "currency": "AUD",
        "brandingThemeId": "theme_standard",
        "taxMode": "exclusive",
        "lineItems": [
            {
                "id": f"li_{lid}",
                "itemId": "item_009",
                "description": "Security Audit - Fixed Fee",
                "quantity": 1,
                "unitPrice": 5500.00,
                "discountPercent": 0,
                "accountId": "acc_260",
                "taxRateId": "tax_gst",
                "trackingRegion": "",
                "trackingDept": "",
            },
            {
                "id": f"li_{lid + 1}",
                "itemId": "item_010",
                "description": "Data Migration Service",
                "quantity": 1,
                "unitPrice": 3800.00,
                "discountPercent": 0,
                "accountId": "acc_200",
                "taxRateId": "tax_gst",
                "trackingRegion": "",
                "trackingDept": "",
            },
        ],
        "subtotal": subtotal,
        "taxTotal": tax,
        "total": total,
        "amountDue": total,
        "amountPaid": 0,
        "payments": [],
        "notes": [{"date": "2026-03-02T12:00:00Z", "text": "Invoice created", "user": "Sarah Mitchell"}],
        "sentAt": None,
        "title": "",
        "summary": "",
    }
    state["invoices"].append(inv)
    state["_nextInvoiceNum"] = num + 1
    state["_nextLineItemId"] = lid + 2


def solve_task_h18(state):
    """Extend the Fresh Start Catering quote to expire at end of April and send it."""
    quo = find_quote(state, "QU-0025")
    quo["expiryDate"] = "2026-04-30"
    quo["status"] = "sent"
    quo["sentAt"] = "2026-03-02T12:00:00Z"


def solve_task_h19(state):
    """Create invoice for Atlas Engineering using Professional Services template for 5 days PM."""
    contact = find_contact(state, "Atlas Engineering Consultants")
    num = state["_nextInvoiceNum"]
    lid = state["_nextLineItemId"]
    subtotal = 5 * 1400.00
    tax = subtotal * 0.10
    total = subtotal + tax
    inv = {
        "id": f"inv_{num:03d}",
        "number": state["invoiceSettings"]["invoicePrefix"] + f"{num:04d}",
        "contactId": contact["id"],
        "status": "draft",
        "date": "2026-03-02",
        "dueDate": "2026-04-01",
        "reference": "",
        "currency": "AUD",
        "brandingThemeId": "theme_professional",
        "taxMode": "exclusive",
        "lineItems": [{
            "id": f"li_{lid}",
            "itemId": "item_003",
            "description": "Project Management - Day Rate",
            "quantity": 5,
            "unitPrice": 1400.00,
            "discountPercent": 0,
            "accountId": "acc_200",
            "taxRateId": "tax_gst",
            "trackingRegion": "",
            "trackingDept": "",
        }],
        "subtotal": subtotal,
        "taxTotal": tax,
        "total": total,
        "amountDue": total,
        "amountPaid": 0,
        "payments": [],
        "notes": [{"date": "2026-03-02T12:00:00Z", "text": "Invoice created", "user": "Sarah Mitchell"}],
        "sentAt": None,
        "title": "",
        "summary": "",
    }
    state["invoices"].append(inv)
    state["_nextInvoiceNum"] = num + 1
    state["_nextLineItemId"] = lid + 1


def solve_task_h20(state):
    """Issue a credit note to Greenfield Organics for 5 Widget A units and approve it."""
    contact = find_contact(state, "Greenfield Organics")
    num = state["_nextCreditNoteNum"]
    lid = state["_nextLineItemId"]
    subtotal = 5 * 24.95
    tax = subtotal * 0.10
    total = subtotal + tax
    cn = {
        "id": f"cn_{num:03d}",
        "number": state["invoiceSettings"]["creditNotePrefix"] + f"{num:04d}",
        "contactId": contact["id"],
        "status": "awaiting_payment",
        "date": "2026-03-02",
        "reference": "",
        "currency": "AUD",
        "brandingThemeId": "theme_standard",
        "taxMode": "exclusive",
        "lineItems": [{
            "id": f"li_{lid}",
            "itemId": "item_011",
            "description": "Widget Type A",
            "quantity": 5,
            "unitPrice": 24.95,
            "discountPercent": 0,
            "accountId": "acc_200",
            "taxRateId": "tax_gst",
            "trackingRegion": "",
            "trackingDept": "",
        }],
        "subtotal": subtotal,
        "taxTotal": tax,
        "total": total,
        "remainingCredit": total,
        "allocations": [],
        "refunds": [],
        "notes": [{"date": "2026-03-02T12:00:00Z", "text": "Credit note created", "user": "Sarah Mitchell"}],
    }
    state["creditNotes"].append(cn)
    state["_nextCreditNoteNum"] = num + 1
    state["_nextLineItemId"] = lid + 1


# ===== HARD (Hardening Round 1) =====

def solve_task_h21(state):
    """Fully pay the overdue invoice with the earliest due date (INV-0046, Baxter, due 2026-02-01)."""
    inv = find_invoice(state, "INV-0046")
    pay_id = f"pay_{state['_nextPaymentId']}"
    state["_nextPaymentId"] += 1
    amount = inv["amountDue"]
    inv["payments"].append({
        "id": pay_id,
        "date": "2026-03-02",
        "amount": amount,
        "reference": "",
        "accountId": "acc_090",
    })
    inv["amountPaid"] = inv["total"]
    inv["amountDue"] = 0
    inv["status"] = "paid"


def solve_task_h22(state):
    """Accept the Redback Mining Supplies quote and convert it to an invoice."""
    quo = find_quote(state, "QU-0023")
    quo["status"] = "accepted"
    num = state["_nextInvoiceNum"]
    lid = state["_nextLineItemId"]
    line_items = deepcopy(quo["lineItems"])
    for li in line_items:
        li["id"] = f"li_{lid}"
        lid += 1
    inv = {
        "id": f"inv_{num:03d}",
        "number": state["invoiceSettings"]["invoicePrefix"] + f"{num:04d}",
        "contactId": quo["contactId"],
        "status": "draft",
        "date": "2026-03-02",
        "dueDate": "2026-04-01",
        "reference": quo["reference"],
        "currency": quo["currency"],
        "brandingThemeId": quo["brandingThemeId"],
        "taxMode": quo["taxMode"],
        "lineItems": line_items,
        "subtotal": quo["subtotal"],
        "taxTotal": quo["taxTotal"],
        "total": quo["total"],
        "amountDue": quo["total"],
        "amountPaid": 0,
        "payments": [],
        "notes": [{"date": "2026-03-02T12:00:00Z", "text": "Invoice created", "user": "Sarah Mitchell"}],
        "sentAt": None,
        "title": quo["title"],
        "summary": quo["summary"],
    }
    state["invoices"].append(inv)
    state["_nextInvoiceNum"] = num + 1
    state["_nextLineItemId"] = lid
    quo["isInvoiced"] = True


def solve_task_h23(state):
    """Record a full payment on the CloudNine Analytics invoice due first (INV-0047)."""
    inv = find_invoice(state, "INV-0047")
    pay_id = f"pay_{state['_nextPaymentId']}"
    state["_nextPaymentId"] += 1
    amount = inv["amountDue"]
    inv["payments"].append({
        "id": pay_id,
        "date": "2026-03-02",
        "amount": amount,
        "reference": "",
        "accountId": "acc_090",
    })
    inv["amountPaid"] = inv["total"]
    inv["amountDue"] = 0
    inv["status"] = "paid"


def solve_task_h24(state):
    """Approve CN-0011 then allocate full amount to INV-0048 (Pacific Freight Lines)."""
    cn = find_credit_note(state, "CN-0011")
    cn["status"] = "awaiting_payment"
    inv = find_invoice(state, "INV-0048")
    amount = 968.00
    cn["allocations"].append({
        "invoiceId": inv["id"],
        "invoiceNumber": inv["number"],
        "amount": amount,
        "date": "2026-03-02",
    })
    cn["remainingCredit"] -= amount
    if cn["remainingCredit"] <= 0.005:
        cn["status"] = "paid"
        cn["remainingCredit"] = 0
    inv["amountPaid"] += amount
    inv["amountDue"] -= amount
    if inv["amountDue"] <= 0.005:
        inv["status"] = "paid"
        inv["amountDue"] = 0


def solve_task_h25(state):
    """Copy the most expensive paid invoice (INV-0064, $23,100) to create a new draft."""
    src = find_invoice(state, "INV-0064")
    copy = deepcopy(src)
    num = state["_nextInvoiceNum"]
    copy["id"] = f"inv_{num:03d}"
    copy["number"] = state["invoiceSettings"]["invoicePrefix"] + f"{num:04d}"
    state["_nextInvoiceNum"] = num + 1
    copy["status"] = "draft"
    copy["payments"] = []
    copy["amountPaid"] = 0
    copy["amountDue"] = copy["total"]
    copy["sentAt"] = None
    copy["notes"] = [{"date": "2026-03-02T12:00:00Z", "text": f"Copied from {src['number']}", "user": "Sarah Mitchell"}]
    lid = state["_nextLineItemId"]
    for li in copy["lineItems"]:
        li["id"] = f"li_{lid}"
        lid += 1
    state["_nextLineItemId"] = lid
    state["invoices"].append(copy)


def solve_task_h26(state):
    """Create a quote for Metro Fabrication Works for setup fee + 20 USB-C cables, then send it."""
    contact = find_contact(state, "Metro Fabrication Works")
    num = state["_nextQuoteNum"]
    lid = state["_nextLineItemId"]
    subtotal = 500.00 + 20 * 12.50
    tax = subtotal * 0.10
    total = subtotal + tax
    quo = {
        "id": f"quo_{num:03d}",
        "number": state["invoiceSettings"]["quotePrefix"] + f"{num:04d}",
        "contactId": contact["id"],
        "status": "sent",
        "date": "2026-03-02",
        "expiryDate": "2026-04-01",
        "reference": "",
        "currency": "AUD",
        "brandingThemeId": "theme_standard",
        "taxMode": "exclusive",
        "lineItems": [
            {
                "id": f"li_{lid}",
                "itemId": "item_014",
                "description": "Initial Setup Fee",
                "quantity": 1,
                "unitPrice": 500.00,
                "discountPercent": 0,
                "accountId": "acc_200",
                "taxRateId": "tax_gst",
                "trackingRegion": "",
                "trackingDept": "",
            },
            {
                "id": f"li_{lid + 1}",
                "itemId": "item_013",
                "description": "USB-C Cable 2m",
                "quantity": 20,
                "unitPrice": 12.50,
                "discountPercent": 0,
                "accountId": "acc_200",
                "taxRateId": "tax_gst",
                "trackingRegion": "",
                "trackingDept": "",
            },
        ],
        "subtotal": subtotal,
        "taxTotal": tax,
        "total": total,
        "title": "",
        "summary": "",
        "terms": "",
        "notes": [{"date": "2026-03-02T12:00:00Z", "text": "Quote created", "user": "Sarah Mitchell"}],
        "sentAt": "2026-03-02T12:00:00Z",
        "isInvoiced": False,
    }
    state["quotes"].append(quo)
    state["_nextQuoteNum"] = num + 1
    state["_nextLineItemId"] = lid + 2


def solve_task_h27(state):
    """Make sure every overdue (after) reminder includes the invoice PDF."""
    for rem in state["invoiceReminders"]:
        if rem["timing"] == "after":
            rem["includeInvoicePdf"] = True


def solve_task_h28(state):
    """Set up fortnightly repeating invoice for Outback Adventures Tourism."""
    contact = find_contact(state, "Outback Adventures Tourism")
    rid = state["_nextRepeatId"]
    state["_nextRepeatId"] = rid + 1
    ri = {
        "id": f"rep_{rid:03d}",
        "contactId": contact["id"],
        "status": "draft",
        "frequency": "fortnightly",
        "startDate": "2026-05-01",
        "nextDate": "2026-05-01",
        "endDate": "",
        "currency": "AUD",
        "brandingThemeId": "theme_standard",
        "taxMode": "exclusive",
        "saveAs": "approved",
        "lineItems": [{
            "id": f"rli_{rid * 10}",
            "itemId": "item_007",
            "description": "UI/UX Design - Hourly Rate",
            "quantity": 3,
            "unitPrice": 165.00,
            "accountId": "acc_200",
            "taxRateId": "tax_gst",
        }],
        "dueDate": {"type": "daysAfterInvoice", "days": 30},
        "reference": "",
        "emailSubject": "",
        "emailBody": "",
    }
    state["repeatingInvoices"].append(ri)


def solve_task_h29(state):
    """Edit INV-0055 (TechVault's highest total): change theme to Retail, add title."""
    inv = find_invoice(state, "INV-0055")
    inv["brandingThemeId"] = "theme_retail"
    inv["title"] = "Q1 2026 Major Project"


def solve_task_h30(state):
    """Create invoice for Harbour City Plumbing: security audit + 16 hrs dev, Professional Services, approved."""
    contact = find_contact(state, "Harbour City Plumbing")
    num = state["_nextInvoiceNum"]
    lid = state["_nextLineItemId"]
    subtotal = 5500.00 + 16 * 185.00
    tax = subtotal * 0.10
    total = subtotal + tax
    inv = {
        "id": f"inv_{num:03d}",
        "number": state["invoiceSettings"]["invoicePrefix"] + f"{num:04d}",
        "contactId": contact["id"],
        "status": "awaiting_payment",
        "date": "2026-03-02",
        "dueDate": "2026-04-01",
        "reference": "",
        "currency": "AUD",
        "brandingThemeId": "theme_professional",
        "taxMode": "exclusive",
        "lineItems": [
            {
                "id": f"li_{lid}",
                "itemId": "item_009",
                "description": "Security Audit - Fixed Fee",
                "quantity": 1,
                "unitPrice": 5500.00,
                "discountPercent": 0,
                "accountId": "acc_260",
                "taxRateId": "tax_gst",
                "trackingRegion": "",
                "trackingDept": "",
            },
            {
                "id": f"li_{lid + 1}",
                "itemId": "item_001",
                "description": "Software Development - Hourly Rate",
                "quantity": 16,
                "unitPrice": 185.00,
                "discountPercent": 0,
                "accountId": "acc_200",
                "taxRateId": "tax_gst",
                "trackingRegion": "",
                "trackingDept": "",
            },
        ],
        "subtotal": subtotal,
        "taxTotal": tax,
        "total": total,
        "amountDue": total,
        "amountPaid": 0,
        "payments": [],
        "notes": [{"date": "2026-03-02T12:00:00Z", "text": "Invoice created", "user": "Sarah Mitchell"}],
        "sentAt": None,
        "title": "",
        "summary": "",
    }
    state["invoices"].append(inv)
    state["_nextInvoiceNum"] = num + 1
    state["_nextLineItemId"] = lid + 2


def solve_task_h31(state):
    """Invoice Summit Health Group: 20 hrs dev (15% discount) + 2 days PM."""
    contact = find_contact(state, "Summit Health Group")
    num = state["_nextInvoiceNum"]
    lid = state["_nextLineItemId"]
    dev_line = 20 * 185.00 * (1 - 0.15)
    pm_line = 2 * 1400.00
    subtotal = dev_line + pm_line
    tax = subtotal * 0.10
    total = subtotal + tax
    inv = {
        "id": f"inv_{num:03d}",
        "number": state["invoiceSettings"]["invoicePrefix"] + f"{num:04d}",
        "contactId": contact["id"],
        "status": "draft",
        "date": "2026-03-02",
        "dueDate": "2026-04-01",
        "reference": "",
        "currency": "AUD",
        "brandingThemeId": "theme_standard",
        "taxMode": "exclusive",
        "lineItems": [
            {
                "id": f"li_{lid}",
                "itemId": "item_001",
                "description": "Software Development - Hourly Rate",
                "quantity": 20,
                "unitPrice": 185.00,
                "discountPercent": 15,
                "accountId": "acc_200",
                "taxRateId": "tax_gst",
                "trackingRegion": "",
                "trackingDept": "",
            },
            {
                "id": f"li_{lid + 1}",
                "itemId": "item_003",
                "description": "Project Management - Day Rate",
                "quantity": 2,
                "unitPrice": 1400.00,
                "discountPercent": 0,
                "accountId": "acc_200",
                "taxRateId": "tax_gst",
                "trackingRegion": "",
                "trackingDept": "",
            },
        ],
        "subtotal": subtotal,
        "taxTotal": tax,
        "total": total,
        "amountDue": total,
        "amountPaid": 0,
        "payments": [],
        "notes": [{"date": "2026-03-02T12:00:00Z", "text": "Invoice created", "user": "Sarah Mitchell"}],
        "sentAt": None,
        "title": "",
        "summary": "",
    }
    state["invoices"].append(inv)
    state["_nextInvoiceNum"] = num + 1
    state["_nextLineItemId"] = lid + 2


def solve_task_h32(state):
    """Create 'Government' branding theme and set it as default."""
    tid = state["_nextThemeId"]
    state["_nextThemeId"] = tid + 1
    theme = {
        "id": f"theme_{tid}",
        "name": "Government",
        "isDefault": True,
        "logoUrl": "",
        "paymentTerms": "Net 45 days from invoice date",
        "termsAndConditions": "Subject to government procurement regulations.",
        "showTaxNumber": True,
        "showPaymentAdvice": False,
    }
    for t in state["brandingThemes"]:
        t["isDefault"] = False
    state["brandingThemes"].append(theme)


def solve_task_h33(state):
    """Send a quote for 10 hrs consulting to client with highest awaiting-payment invoice (TechVault)."""
    contact = find_contact(state, "TechVault Solutions Pty Ltd")
    num = state["_nextQuoteNum"]
    lid = state["_nextLineItemId"]
    subtotal = 10 * 250.00
    tax = subtotal * 0.10
    total = subtotal + tax
    quo = {
        "id": f"quo_{num:03d}",
        "number": state["invoiceSettings"]["quotePrefix"] + f"{num:04d}",
        "contactId": contact["id"],
        "status": "sent",
        "date": "2026-03-02",
        "expiryDate": "2026-04-01",
        "reference": "",
        "currency": "AUD",
        "brandingThemeId": "theme_standard",
        "taxMode": "exclusive",
        "lineItems": [{
            "id": f"li_{lid}",
            "itemId": "item_002",
            "description": "Consulting Services - Per Hour",
            "quantity": 10,
            "unitPrice": 250.00,
            "discountPercent": 0,
            "accountId": "acc_260",
            "taxRateId": "tax_gst",
            "trackingRegion": "",
            "trackingDept": "",
        }],
        "subtotal": subtotal,
        "taxTotal": tax,
        "total": total,
        "title": "",
        "summary": "",
        "terms": "",
        "notes": [{"date": "2026-03-02T12:00:00Z", "text": "Quote created", "user": "Sarah Mitchell"}],
        "sentAt": "2026-03-02T12:00:00Z",
        "isInvoiced": False,
    }
    state["quotes"].append(quo)
    state["_nextQuoteNum"] = num + 1
    state["_nextLineItemId"] = lid + 1


def solve_task_h34(state):
    """Change Cascade Software repeating invoice to fortnightly with Professional Services theme."""
    ri = find_repeating(state, "rep_003")
    ri["frequency"] = "fortnightly"
    ri["brandingThemeId"] = "theme_professional"


def solve_task_h35(state):
    """Create CN for CloudNine (5 hrs dev), approve, allocate to INV-0062 (smaller invoice)."""
    contact = find_contact(state, "CloudNine Analytics")
    num = state["_nextCreditNoteNum"]
    lid = state["_nextLineItemId"]
    subtotal = 5 * 185.00
    tax = subtotal * 0.10
    total = subtotal + tax
    cn = {
        "id": f"cn_{num:03d}",
        "number": state["invoiceSettings"]["creditNotePrefix"] + f"{num:04d}",
        "contactId": contact["id"],
        "status": "awaiting_payment",
        "date": "2026-03-02",
        "reference": "",
        "currency": "AUD",
        "brandingThemeId": "theme_standard",
        "taxMode": "exclusive",
        "lineItems": [{
            "id": f"li_{lid}",
            "itemId": "item_001",
            "description": "Software Development - Hourly Rate",
            "quantity": 5,
            "unitPrice": 185.00,
            "discountPercent": 0,
            "accountId": "acc_200",
            "taxRateId": "tax_gst",
            "trackingRegion": "",
            "trackingDept": "",
        }],
        "subtotal": subtotal,
        "taxTotal": tax,
        "total": total,
        "remainingCredit": 0,
        "allocations": [],
        "refunds": [],
        "notes": [{"date": "2026-03-02T12:00:00Z", "text": "Credit note created", "user": "Sarah Mitchell"}],
    }
    inv = find_invoice(state, "INV-0062")
    alloc_amount = min(total, inv["amountDue"])
    cn["allocations"].append({
        "invoiceId": inv["id"],
        "invoiceNumber": inv["number"],
        "amount": alloc_amount,
        "date": "2026-03-02",
    })
    cn["remainingCredit"] = total - alloc_amount
    if cn["remainingCredit"] <= 0.005:
        cn["status"] = "paid"
        cn["remainingCredit"] = 0
    inv["amountPaid"] += alloc_amount
    inv["amountDue"] -= alloc_amount
    if inv["amountDue"] <= 0.005:
        inv["status"] = "paid"
        inv["amountDue"] = 0
    state["creditNotes"].append(cn)
    state["_nextCreditNoteNum"] = num + 1
    state["_nextLineItemId"] = lid + 1


def solve_task_h36(state):
    """Submit all draft invoices for approval."""
    for inv in state["invoices"]:
        if inv["status"] == "draft":
            inv["status"] = "awaiting_approval"


def solve_task_h37(state):
    """Edit INV-0058: switch to tax-exclusive, change theme to Professional Services."""
    inv = find_invoice(state, "INV-0058")
    inv["taxMode"] = "exclusive"
    inv["brandingThemeId"] = "theme_professional"


def solve_task_h38(state):
    """Create invoice for NT Power Corp: data migration + setup, approve and send."""
    contact = find_contact(state, "Northern Territory Power Corp")
    num = state["_nextInvoiceNum"]
    lid = state["_nextLineItemId"]
    subtotal = 3800.00 + 500.00
    tax = subtotal * 0.10
    total = subtotal + tax
    inv = {
        "id": f"inv_{num:03d}",
        "number": state["invoiceSettings"]["invoicePrefix"] + f"{num:04d}",
        "contactId": contact["id"],
        "status": "awaiting_payment",
        "date": "2026-03-02",
        "dueDate": "2026-04-01",
        "reference": "",
        "currency": "AUD",
        "brandingThemeId": "theme_standard",
        "taxMode": "exclusive",
        "lineItems": [
            {
                "id": f"li_{lid}",
                "itemId": "item_010",
                "description": "Data Migration Service",
                "quantity": 1,
                "unitPrice": 3800.00,
                "discountPercent": 0,
                "accountId": "acc_200",
                "taxRateId": "tax_gst",
                "trackingRegion": "",
                "trackingDept": "",
            },
            {
                "id": f"li_{lid + 1}",
                "itemId": "item_014",
                "description": "Initial Setup Fee",
                "quantity": 1,
                "unitPrice": 500.00,
                "discountPercent": 0,
                "accountId": "acc_200",
                "taxRateId": "tax_gst",
                "trackingRegion": "",
                "trackingDept": "",
            },
        ],
        "subtotal": subtotal,
        "taxTotal": tax,
        "total": total,
        "amountDue": total,
        "amountPaid": 0,
        "payments": [],
        "notes": [{"date": "2026-03-02T12:00:00Z", "text": "Invoice created", "user": "Sarah Mitchell"}],
        "sentAt": "2026-03-02T12:00:00Z",
        "title": "",
        "summary": "",
    }
    state["invoices"].append(inv)
    state["_nextInvoiceNum"] = num + 1
    state["_nextLineItemId"] = lid + 2


def solve_task_h39(state):
    """Invoice Atlas Engineering: 3 hrs UI/UX design (Victoria/Sales tracking) + 10 USB-C cables."""
    contact = find_contact(state, "Atlas Engineering Consultants")
    num = state["_nextInvoiceNum"]
    lid = state["_nextLineItemId"]
    subtotal = 3 * 165.00 + 10 * 12.50
    tax = subtotal * 0.10
    total = subtotal + tax
    inv = {
        "id": f"inv_{num:03d}",
        "number": state["invoiceSettings"]["invoicePrefix"] + f"{num:04d}",
        "contactId": contact["id"],
        "status": "draft",
        "date": "2026-03-02",
        "dueDate": "2026-04-01",
        "reference": "",
        "currency": "AUD",
        "brandingThemeId": "theme_standard",
        "taxMode": "exclusive",
        "lineItems": [
            {
                "id": f"li_{lid}",
                "itemId": "item_007",
                "description": "UI/UX Design - Hourly Rate",
                "quantity": 3,
                "unitPrice": 165.00,
                "discountPercent": 0,
                "accountId": "acc_200",
                "taxRateId": "tax_gst",
                "trackingRegion": "Victoria",
                "trackingDept": "Sales",
            },
            {
                "id": f"li_{lid + 1}",
                "itemId": "item_013",
                "description": "USB-C Cable 2m",
                "quantity": 10,
                "unitPrice": 12.50,
                "discountPercent": 0,
                "accountId": "acc_200",
                "taxRateId": "tax_gst",
                "trackingRegion": "",
                "trackingDept": "",
            },
        ],
        "subtotal": subtotal,
        "taxTotal": tax,
        "total": total,
        "amountDue": total,
        "amountPaid": 0,
        "payments": [],
        "notes": [{"date": "2026-03-02T12:00:00Z", "text": "Invoice created", "user": "Sarah Mitchell"}],
        "sentAt": None,
        "title": "",
        "summary": "",
    }
    state["invoices"].append(inv)
    state["_nextInvoiceNum"] = num + 1
    state["_nextLineItemId"] = lid + 2


def solve_task_h40(state):
    """Add a 3-day before-due-date invoice reminder."""
    rid = state["_nextReminderId"]
    state["_nextReminderId"] = rid + 1
    rem = {
        "id": f"rem_{rid:03d}",
        "enabled": True,
        "timing": "before",
        "days": 3,
        "subject": "Friendly reminder: Invoice {InvoiceNumber} due in 3 days",
        "body": "",
        "includeInvoicePdf": True,
        "includeSummary": True,
    }
    state["invoiceReminders"].append(rem)


# ---------------------------------------------------------------------------
# Solver registry
# ---------------------------------------------------------------------------

SOLVERS = {}
for _prefix in ("e", "m", "h"):
    for _i in range(1, 41):
        _key = f"task_{_prefix}{_i}"
        _fn = globals().get(f"solve_{_key}")
        if _fn:
            SOLVERS[_key] = _fn

# ---------------------------------------------------------------------------
# Task loading and verification
# ---------------------------------------------------------------------------

TASKS_FILE_HARDENED = os.path.join(APP_DIR, "tasks.json")


def load_tasks():
    with open(TASKS_FILE) as f:
        tasks = json.load(f)
    if os.path.exists(TASKS_FILE_HARDENED):
        with open(TASKS_FILE_HARDENED) as f:
            hardened = json.load(f)
        if hardened:
            tasks.extend(hardened)
    return tasks


def load_verifier(verify_path):
    full_path = os.path.join(APP_DIR, verify_path)
    spec = importlib.util.spec_from_file_location("verifier", full_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.verify


# ---------------------------------------------------------------------------
# Server management
# ---------------------------------------------------------------------------


def find_free_port(start=9500):
    port = start
    while port < start + 200:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("", port))
                return port
            except OSError:
                port += 1
    raise RuntimeError(f"No free port found starting from {start}")


def start_server(port, seed_state):
    proc = subprocess.Popen(
        [sys.executable, SERVER_PY, "--port", str(port)],
        cwd=APP_DIR,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    server_url = f"http://localhost:{port}"
    for _ in range(30):
        try:
            requests.post(f"{server_url}/api/reset", timeout=1)
            break
        except Exception:
            time.sleep(0.2)
    requests.put(
        f"{server_url}/api/state",
        json=seed_state,
        headers={"Content-Type": "application/json"},
        timeout=5,
    )
    return proc


def stop_server(proc):
    if proc and proc.poll() is None:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()


# ---------------------------------------------------------------------------
# Task runner
# ---------------------------------------------------------------------------


def run_single_task(task, server_url):
    task_id = task["id"]
    solver = SOLVERS.get(task_id)
    if not solver:
        return task_id, False, f"No solver defined for {task_id}"

    try:
        resp = requests.post(f"{server_url}/api/reset")
        if resp.status_code != 200:
            return task_id, False, f"Reset failed: HTTP {resp.status_code}"

        time.sleep(0.3)

        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return task_id, False, f"Could not read state after reset: HTTP {resp.status_code}"
        state = resp.json()

        solver(state)

        resp = requests.put(
            f"{server_url}/api/state",
            json=state,
            headers={"Content-Type": "application/json"},
        )
        if resp.status_code != 200:
            return task_id, False, f"Could not write state: HTTP {resp.status_code}"

        verify_fn = load_verifier(task["verify"])
        passed, message = verify_fn(server_url)
        return task_id, passed, message

    except Exception as e:
        return task_id, False, f"Exception: {e}"


def run_tasks_sequential(tasks, port, seed_state):
    proc = start_server(port, seed_state)
    server_url = f"http://localhost:{port}"
    results = []
    try:
        for task in tasks:
            tid, passed, msg = run_single_task(task, server_url)
            status = "\033[32m  PASS\033[0m" if passed else "\033[31m  FAIL\033[0m"
            print(f"{status}  {tid:12s} {msg}")
            results.append((tid, passed, msg))
    finally:
        stop_server(proc)
    return results


def run_tasks_parallel(tasks, workers, base_port, seed_state):
    results = []

    def worker_fn(task_batch, port):
        proc = start_server(port, seed_state)
        server_url = f"http://localhost:{port}"
        batch_results = []
        try:
            for task in task_batch:
                batch_results.append(run_single_task(task, server_url))
        finally:
            stop_server(proc)
        return batch_results

    batches = [[] for _ in range(workers)]
    for i, task in enumerate(tasks):
        batches[i % workers].append(task)

    ports = [find_free_port(base_port + i * 10) for i in range(workers)]

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {}
        for i, batch in enumerate(batches):
            if batch:
                fut = executor.submit(worker_fn, batch, ports[i])
                futures[fut] = i

        for fut in as_completed(futures):
            try:
                batch_results = fut.result()
                for tid, passed, msg in batch_results:
                    status = "\033[32m  PASS\033[0m" if passed else "\033[31m  FAIL\033[0m"
                    print(f"{status}  {tid:12s} {msg}")
                    results.append((tid, passed, msg))
            except Exception as e:
                print(f"\033[31m  ERROR\033[0m Worker {futures[fut]}: {e}")

    return results


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(description="Xero Invoicing real-task sanity check")
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
