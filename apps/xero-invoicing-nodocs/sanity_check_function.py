#!/usr/bin/env python3
"""
Sanity check for Xero Invoicing function-test tasks.

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

const state = {
    contacts: JSON.parse(JSON.stringify(CONTACTS)),
    invoices: JSON.parse(JSON.stringify(INVOICES)),
    payments: JSON.parse(JSON.stringify(PAYMENTS)),
    taxRates: JSON.parse(JSON.stringify(TAX_RATES)),
    accountCodes: JSON.parse(JSON.stringify(ACCOUNT_CODES)),
    bankAccounts: JSON.parse(JSON.stringify(BANK_ACCOUNTS)),
    currencies: JSON.parse(JSON.stringify(CURRENCIES)),
    brandingThemes: JSON.parse(JSON.stringify(BRANDING_THEMES)),
    settings: JSON.parse(JSON.stringify(DEFAULT_SETTINGS)),
    _nextInvoiceId: 114,
    _nextContactId: 26,
    _nextPaymentId: PAYMENTS.length + 1,
    _nextLineItemId: 10000,
    _seedVersion: SEED_DATA_VERSION,
};
process.stdout.write(JSON.stringify(state));
"""


# ── helpers ──────────────────────────────────────────────────────────

def find_contact_by_name(state, name):
    for c in state["contacts"]:
        if c["name"] == name:
            return c
    raise ValueError(f"Contact not found: {name!r}")


def find_invoice_by_number(state, num):
    for inv in state["invoices"]:
        if inv["invoiceNumber"] == num:
            return inv
    raise ValueError(f"Invoice not found: {num!r}")


def next_invoice_id(state):
    iid = state.get("_nextInvoiceId", 114)
    state["_nextInvoiceId"] = iid + 1
    return iid


def next_contact_id(state):
    cid = state.get("_nextContactId", 26)
    state["_nextContactId"] = cid + 1
    return cid


def next_payment_id(state):
    pid = state.get("_nextPaymentId", 100)
    state["_nextPaymentId"] = pid + 1
    return pid


def next_line_item_id(state):
    lid = state.get("_nextLineItemId", 10000)
    state["_nextLineItemId"] = lid + 1
    return lid


NOW = "2026-03-18T12:00:00Z"
TODAY = "2026-03-18"


def make_invoice(state, contact_id, line_items_raw, **kwargs):
    """Create a new invoice and append to state. Returns the invoice."""
    inv_id = next_invoice_id(state)
    prefix = state["settings"]["invoiceNumberPrefix"]
    next_num = state["settings"]["invoiceNumberNextNumber"]
    padding = state["settings"]["invoiceNumberPadding"]
    inv_num = prefix + str(next_num).zfill(padding)
    state["settings"]["invoiceNumberNextNumber"] = next_num + 1

    subtotal = 0
    tax_total = 0
    line_items = []
    for li_raw in line_items_raw:
        lid = next_line_item_id(state)
        lt = round(li_raw["quantity"] * li_raw["unitPrice"], 2)
        subtotal += lt
        tax_rate_id = li_raw.get("taxRateId", "tax_1")
        rate_obj = next((t for t in state["taxRates"] if t["id"] == tax_rate_id), None)
        rate_pct = rate_obj["rate"] if rate_obj else 0
        tax_total += lt * (rate_pct / 100)
        line_items.append({
            "id": f"li_{lid}",
            "description": li_raw["description"],
            "quantity": li_raw["quantity"],
            "unitPrice": li_raw["unitPrice"],
            "taxRateId": tax_rate_id,
            "accountCode": li_raw.get("accountCode", "200"),
            "lineTotal": lt,
        })
    subtotal = round(subtotal, 2)
    tax_total = round(tax_total, 2)
    total = round(subtotal + tax_total, 2)
    status = kwargs.get("status", "draft")

    activity = [{"type": "created", "date": NOW, "user": "System", "detail": "Invoice created"}]
    if status == "awaiting_payment":
        activity.append({"type": "approved", "date": NOW, "user": "System", "detail": "Invoice approved"})

    inv = {
        "id": f"inv_{inv_id}",
        "invoiceNumber": kwargs.get("invoiceNumber", inv_num),
        "reference": kwargs.get("reference", ""),
        "contactId": contact_id,
        "status": status,
        "issueDate": kwargs.get("issueDate", TODAY),
        "dueDate": kwargs.get("dueDate", ""),
        "currency": kwargs.get("currency", "NZD"),
        "lineItems": line_items,
        "subtotal": subtotal,
        "taxTotal": tax_total,
        "total": total,
        "amountPaid": 0,
        "amountDue": total,
        "notes": kwargs.get("notes", ""),
        "brandingThemeId": kwargs.get("brandingThemeId", state["settings"]["defaultBrandingThemeId"]),
        "createdAt": NOW,
        "updatedAt": NOW,
        "sentAt": None,
        "paidAt": None,
        "voidedAt": None,
        "activity": activity,
    }
    state["invoices"].append(inv)
    return inv


def add_payment(state, invoice_id, amount, bank_account_id="bank_1", reference="", exchange_rate=1):
    """Record a payment on an invoice."""
    inv = next(i for i in state["invoices"] if i["id"] == invoice_id)
    pid = next_payment_id(state)
    payment = {
        "id": f"pay_{pid}",
        "invoiceId": invoice_id,
        "date": TODAY,
        "amount": amount,
        "bankAccountId": bank_account_id,
        "reference": reference,
        "note": "",
        "exchangeRate": exchange_rate,
    }
    state["payments"].append(payment)
    inv["amountPaid"] = round(inv["amountPaid"] + amount, 2)
    inv["amountDue"] = round(inv["total"] - inv["amountPaid"], 2)
    if inv["amountDue"] <= 0.005:
        inv["status"] = "paid"
        inv["paidAt"] = NOW
        inv["amountDue"] = 0
    inv["updatedAt"] = NOW
    inv["activity"].append({
        "type": "payment",
        "date": NOW,
        "user": "System",
        "detail": f"Payment of ${amount:.2f} received",
    })
    return payment


# ── solve functions ──────────────────────────────────────────────────

def solve_task_1(state):
    """Create draft invoice for Ridgeway University."""
    con = find_contact_by_name(state, "Ridgeway University")
    make_invoice(state, con["id"], [
        {"description": "Strategic consulting session", "quantity": 3, "unitPrice": 450,
         "taxRateId": "tax_1", "accountCode": "200"},
    ])


def solve_task_2(state):
    """Create draft invoice for DataFlow Analytics Inc in USD."""
    con = find_contact_by_name(state, "DataFlow Analytics Inc")
    make_invoice(state, con["id"], [
        {"description": "Cloud migration assessment", "quantity": 1, "unitPrice": 2500,
         "taxRateId": "tax_1", "accountCode": "200"},
    ], currency="USD")


def solve_task_3(state):
    """Create draft invoice for Coastal Cafe Group with ref and notes."""
    con = find_contact_by_name(state, "Coastal Cafe Group")
    make_invoice(state, con["id"], [
        {"description": "Catering services - corporate event", "quantity": 1, "unitPrice": 1200,
         "taxRateId": "tax_1", "accountCode": "200"},
    ], reference="PO-CAFE-2026", notes="Payment due within 14 days.")


def solve_task_4(state):
    """Create draft invoice for Green Valley Organics with 2 mixed-tax line items."""
    con = find_contact_by_name(state, "Green Valley Organics")
    make_invoice(state, con["id"], [
        {"description": "Environmental impact assessment", "quantity": 1, "unitPrice": 1500,
         "taxRateId": "tax_3", "accountCode": "200"},
        {"description": "Sustainability report preparation", "quantity": 2, "unitPrice": 800,
         "taxRateId": "tax_1", "accountCode": "200"},
    ])


def solve_task_5(state):
    """Create draft invoice for Heritage Craft Brewery in AUD."""
    con = find_contact_by_name(state, "Heritage Craft Brewery")
    make_invoice(state, con["id"], [
        {"description": "Event planning and coordination", "quantity": 5, "unitPrice": 300,
         "taxRateId": "tax_1", "accountCode": "270"},
    ], currency="AUD")


def solve_task_6(state):
    """Create and approve invoice for Bright Spark Electrical."""
    con = find_contact_by_name(state, "Bright Spark Electrical")
    make_invoice(state, con["id"], [
        {"description": "Electrical inspection", "quantity": 1, "unitPrice": 350,
         "taxRateId": "tax_1", "accountCode": "200"},
    ], status="awaiting_payment")


def solve_task_7(state):
    """Approve draft invoice INV-0005."""
    inv = find_invoice_by_number(state, "INV-0005")
    inv["status"] = "awaiting_payment"
    inv["updatedAt"] = NOW
    inv["activity"].append({"type": "approved", "date": NOW, "user": "System", "detail": "Invoice approved"})


def solve_task_8(state):
    """Approve invoice INV-0008 (awaiting_approval)."""
    inv = find_invoice_by_number(state, "INV-0008")
    inv["status"] = "awaiting_payment"
    inv["updatedAt"] = NOW
    inv["activity"].append({"type": "approved", "date": NOW, "user": "System", "detail": "Invoice approved"})


def solve_task_9(state):
    """Approve and send draft invoice INV-0042."""
    inv = find_invoice_by_number(state, "INV-0042")
    inv["status"] = "awaiting_payment"
    inv["sentAt"] = NOW
    inv["updatedAt"] = NOW
    inv["activity"].append({"type": "approved", "date": NOW, "user": "System", "detail": "Invoice approved"})
    con = next(c for c in state["contacts"] if c["id"] == inv["contactId"])
    inv["activity"].append({"type": "sent", "date": NOW, "user": "System", "detail": f"Email sent to {con['email']}"})


def solve_task_10(state):
    """Mark invoice INV-0004 as sent."""
    inv = find_invoice_by_number(state, "INV-0004")
    inv["sentAt"] = inv.get("sentAt") or NOW
    inv["updatedAt"] = NOW
    inv["activity"].append({"type": "marked_sent", "date": NOW, "user": "System", "detail": "Invoice marked as sent"})


def solve_task_11(state):
    """Void overdue invoice INV-0015."""
    inv = find_invoice_by_number(state, "INV-0015")
    inv["status"] = "voided"
    inv["voidedAt"] = NOW
    inv["updatedAt"] = NOW
    inv["activity"].append({"type": "voided", "date": NOW, "user": "System", "detail": "Invoice voided"})


def solve_task_12(state):
    """Void invoice INV-0002."""
    inv = find_invoice_by_number(state, "INV-0002")
    inv["status"] = "voided"
    inv["voidedAt"] = NOW
    inv["updatedAt"] = NOW
    inv["activity"].append({"type": "voided", "date": NOW, "user": "System", "detail": "Invoice voided"})


def solve_task_13(state):
    """Copy paid invoice INV-0001 to new draft."""
    orig = find_invoice_by_number(state, "INV-0001")
    li_raw = [{"description": li["description"], "quantity": li["quantity"],
               "unitPrice": li["unitPrice"], "taxRateId": li["taxRateId"],
               "accountCode": li["accountCode"]} for li in orig["lineItems"]]
    ref = (orig["reference"] + " (copy)") if orig["reference"] else ""
    make_invoice(state, orig["contactId"], li_raw,
                 reference=ref, notes=orig["notes"], currency=orig["currency"],
                 brandingThemeId=orig["brandingThemeId"])


def solve_task_14(state):
    """Approve and send invoice INV-0017 (awaiting_approval)."""
    inv = find_invoice_by_number(state, "INV-0017")
    inv["status"] = "awaiting_payment"
    inv["sentAt"] = NOW
    inv["updatedAt"] = NOW
    inv["activity"].append({"type": "approved", "date": NOW, "user": "System", "detail": "Invoice approved"})
    con = next(c for c in state["contacts"] if c["id"] == inv["contactId"])
    inv["activity"].append({"type": "sent", "date": NOW, "user": "System", "detail": f"Email sent to {con['email']}"})


def solve_task_15(state):
    """Edit draft INV-0005 reference."""
    inv = find_invoice_by_number(state, "INV-0005")
    inv["reference"] = "UPDATED-REF-001"
    inv["updatedAt"] = NOW


def solve_task_16(state):
    """Edit draft INV-0054 contact to Green Valley Organics."""
    inv = find_invoice_by_number(state, "INV-0054")
    con = find_contact_by_name(state, "Green Valley Organics")
    inv["contactId"] = con["id"]
    inv["updatedAt"] = NOW


def solve_task_17(state):
    """Edit draft INV-0020 due date."""
    inv = find_invoice_by_number(state, "INV-0020")
    inv["dueDate"] = "2026-04-30"
    inv["updatedAt"] = NOW


def solve_task_18(state):
    """Edit draft INV-0083 add line item."""
    inv = find_invoice_by_number(state, "INV-0083")
    lid = next_line_item_id(state)
    new_li = {
        "id": f"li_{lid}",
        "description": "Technical documentation",
        "quantity": 4,
        "unitPrice": 125,
        "taxRateId": "tax_1",
        "accountCode": "200",
        "lineTotal": 500.0,
    }
    inv["lineItems"].append(new_li)
    # Recalculate totals
    subtotal = sum(li["lineTotal"] for li in inv["lineItems"])
    tax_total = 0
    for li in inv["lineItems"]:
        rate_obj = next((t for t in state["taxRates"] if t["id"] == li["taxRateId"]), None)
        if rate_obj:
            tax_total += li["lineTotal"] * (rate_obj["rate"] / 100)
    inv["subtotal"] = round(subtotal, 2)
    inv["taxTotal"] = round(tax_total, 2)
    inv["total"] = round(subtotal + tax_total, 2)
    inv["amountDue"] = round(inv["total"] - inv["amountPaid"], 2)
    inv["updatedAt"] = NOW


def solve_task_19(state):
    """Edit draft INV-0093 branding theme to Bold Corporate."""
    inv = find_invoice_by_number(state, "INV-0093")
    inv["brandingThemeId"] = "theme_4"
    inv["updatedAt"] = NOW


def solve_task_20(state):
    """Edit draft INV-0042 notes."""
    inv = find_invoice_by_number(state, "INV-0042")
    inv["notes"] = "Please reference invoice number on all payments."
    inv["updatedAt"] = NOW


def solve_task_21(state):
    """Delete draft invoice INV-0084."""
    inv = find_invoice_by_number(state, "INV-0084")
    state["invoices"] = [i for i in state["invoices"] if i["id"] != inv["id"]]
    state["payments"] = [p for p in state["payments"] if p["invoiceId"] != inv["id"]]


def solve_task_22(state):
    """Delete draft invoice INV-0108."""
    inv = find_invoice_by_number(state, "INV-0108")
    state["invoices"] = [i for i in state["invoices"] if i["id"] != inv["id"]]
    state["payments"] = [p for p in state["payments"] if p["invoiceId"] != inv["id"]]


def solve_task_23(state):
    """Record full payment $207 on INV-0002."""
    inv = find_invoice_by_number(state, "INV-0002")
    add_payment(state, inv["id"], 207.0, "bank_1", "PAY-0002")


def solve_task_24(state):
    """Record partial payment $1000 on INV-0004."""
    inv = find_invoice_by_number(state, "INV-0004")
    add_payment(state, inv["id"], 1000.0, "bank_1", "PARTIAL-004")


def solve_task_25(state):
    """Record payment $4875.84 on INV-0006 (remaining)."""
    inv = find_invoice_by_number(state, "INV-0006")
    add_payment(state, inv["id"], 4875.84, "bank_2", "FINAL-006")


def solve_task_26(state):
    """Record full payment $5330.25 on INV-0007."""
    inv = find_invoice_by_number(state, "INV-0007")
    add_payment(state, inv["id"], 5330.25, "bank_1", "PAY-0007")


def solve_task_27(state):
    """Record payment $2388.96 on INV-0034 (remaining)."""
    inv = find_invoice_by_number(state, "INV-0034")
    add_payment(state, inv["id"], 2388.96, "bank_1", "FINAL-034")


def solve_task_28(state):
    """Remove partial payment from INV-0006."""
    inv = find_invoice_by_number(state, "INV-0006")
    # Find the partial payment for this invoice
    pay = next(p for p in state["payments"] if p["invoiceId"] == inv["id"])
    state["payments"] = [p for p in state["payments"] if p["id"] != pay["id"]]
    inv["amountPaid"] = round(inv["amountPaid"] - pay["amount"], 2)
    if inv["amountPaid"] < 0:
        inv["amountPaid"] = 0
    inv["amountDue"] = round(inv["total"] - inv["amountPaid"], 2)
    if inv["status"] == "paid":
        inv["status"] = "awaiting_payment"
        inv["paidAt"] = None
    inv["updatedAt"] = NOW


def solve_task_29(state):
    """Record $10000 on overdue INV-0015."""
    inv = find_invoice_by_number(state, "INV-0015")
    add_payment(state, inv["id"], 10000.0, "bank_1", "PARTIAL-015")
    # Override status back to overdue since it's still not fully paid
    # (add_payment only changes to 'paid' if fully paid)


def solve_task_30(state):
    """Create contact Wellington Design Studio."""
    cid = next_contact_id(state)
    state["contacts"].append({
        "id": f"con_{cid}",
        "name": "Wellington Design Studio",
        "email": "hello@wellingtondesign.co.nz",
        "phone": "+64 4 555 1234",
        "billingAddress": {"street": "", "city": "", "region": "", "postalCode": "", "country": "New Zealand"},
        "taxId": "",
        "contactType": "customer",
        "createdAt": NOW,
    })


def solve_task_31(state):
    """Create contact Pacific Cloud Solutions with full address."""
    cid = next_contact_id(state)
    state["contacts"].append({
        "id": f"con_{cid}",
        "name": "Pacific Cloud Solutions",
        "email": "info@pacificcloud.com",
        "phone": "+1 503 555 6789",
        "billingAddress": {
            "street": "900 SW Fifth Avenue",
            "city": "Portland",
            "region": "OR",
            "postalCode": "97204",
            "country": "United States",
        },
        "taxId": "US-93-7654321",
        "contactType": "customer",
        "createdAt": NOW,
    })


def solve_task_32(state):
    """Update Ridgeway University phone."""
    con = find_contact_by_name(state, "Ridgeway University")
    con["phone"] = "+64 9 445 8000"


def solve_task_33(state):
    """Update Coastal Cafe Group email."""
    con = find_contact_by_name(state, "Coastal Cafe Group")
    con["email"] = "accounts@coastalcafe.co.nz"


def solve_task_34(state):
    """Update Nexus Technologies Ltd address."""
    con = find_contact_by_name(state, "Nexus Technologies Ltd")
    con["billingAddress"]["street"] = "200 Lambton Quay, Level 15"
    con["billingAddress"]["postalCode"] = "6012"


def solve_task_35(state):
    """Update Summit Financial Advisors tax ID."""
    con = find_contact_by_name(state, "Summit Financial Advisors")
    con["taxId"] = "NZ-55-777-888"


def solve_task_36(state):
    """Create contact Queenstown Adventure Tours."""
    cid = next_contact_id(state)
    state["contacts"].append({
        "id": f"con_{cid}",
        "name": "Queenstown Adventure Tours",
        "email": "bookings@qtadventure.co.nz",
        "phone": "+64 3 442 5500",
        "billingAddress": {
            "street": "28 Shotover Street",
            "city": "Queenstown",
            "region": "Otago",
            "postalCode": "9300",
            "country": "New Zealand",
        },
        "taxId": "",
        "contactType": "customer",
        "createdAt": NOW,
    })


def solve_task_37(state):
    """Change due date terms to 30."""
    state["settings"]["defaultDueDateTerms"] = "30"


def solve_task_38(state):
    """Change default tax rate to No GST."""
    state["settings"]["defaultTaxRateId"] = "tax_3"


def solve_task_39(state):
    """Change invoice prefix to KCL-."""
    state["settings"]["invoiceNumberPrefix"] = "KCL-"


def solve_task_40(state):
    """Change next number to 500, padding to 6."""
    state["settings"]["invoiceNumberNextNumber"] = 500
    state["settings"]["invoiceNumberPadding"] = 6


def solve_task_41(state):
    """Change branding theme to Professional Blue."""
    state["settings"]["defaultBrandingThemeId"] = "theme_2"


def solve_task_42(state):
    """Update company name."""
    state["settings"]["companyName"] = "Kiwi Consulting Group Ltd"


def solve_task_43(state):
    """Update company email and phone."""
    state["settings"]["companyEmail"] = "billing@kiwiconsulting.co.nz"
    state["settings"]["companyPhone"] = "+64 21 555 0200"


def solve_task_44(state):
    """Enable late penalty, rate 2.5%, daily."""
    state["settings"]["latePenaltyEnabled"] = True
    state["settings"]["latePenaltyRate"] = 2.5
    state["settings"]["latePenaltyFrequency"] = "daily"


def solve_task_45(state):
    """Change email subject."""
    state["settings"]["defaultEmailSubject"] = "Invoice {InvoiceNumber} - Kiwi Consulting Group"


def solve_task_46(state):
    """Update company address and tax ID."""
    state["settings"]["companyAddress"] = "100 Victoria Street, Level 10, Auckland 1010, New Zealand"
    state["settings"]["companyTaxId"] = "NZ-98-765-432"


def solve_task_47(state):
    """Bulk approve INV-0005 and INV-0054."""
    for num in ["INV-0005", "INV-0054"]:
        inv = find_invoice_by_number(state, num)
        inv["status"] = "awaiting_payment"
        inv["updatedAt"] = NOW
        inv["activity"].append({"type": "approved", "date": NOW, "user": "System", "detail": "Invoice approved (bulk)"})


def solve_task_48(state):
    """Bulk delete INV-0083 and INV-0108."""
    for num in ["INV-0083", "INV-0108"]:
        inv = find_invoice_by_number(state, num)
        state["invoices"] = [i for i in state["invoices"] if i["id"] != inv["id"]]
        state["payments"] = [p for p in state["payments"] if p["invoiceId"] != inv["id"]]


def solve_task_49(state):
    """Update phone of contact with INV-0033."""
    inv = find_invoice_by_number(state, "INV-0033")
    con = next(c for c in state["contacts"] if c["id"] == inv["contactId"])
    con["phone"] = "+64 9 307 3300"


def solve_task_50(state):
    """Create draft for contact of INV-0039."""
    inv39 = find_invoice_by_number(state, "INV-0039")
    make_invoice(state, inv39["contactId"], [
        {"description": "Follow-up audit", "quantity": 1, "unitPrice": 750,
         "taxRateId": "tax_1", "accountCode": "200"},
    ])


def solve_task_51(state):
    """Copy INV-0003 to new draft."""
    orig = find_invoice_by_number(state, "INV-0003")
    li_raw = [{"description": li["description"], "quantity": li["quantity"],
               "unitPrice": li["unitPrice"], "taxRateId": li["taxRateId"],
               "accountCode": li["accountCode"]} for li in orig["lineItems"]]
    ref = (orig["reference"] + " (copy)") if orig["reference"] else ""
    make_invoice(state, orig["contactId"], li_raw,
                 reference=ref, notes=orig["notes"], currency=orig["currency"],
                 brandingThemeId=orig["brandingThemeId"])


def solve_task_52(state):
    """Pay INV-0074 remaining to fully pay."""
    inv = find_invoice_by_number(state, "INV-0074")
    add_payment(state, inv["id"], inv["amountDue"], "bank_1")


def solve_task_53(state):
    """Pay INV-0055 $37.20 remaining."""
    inv = find_invoice_by_number(state, "INV-0055")
    add_payment(state, inv["id"], 37.20, "bank_1")


def solve_task_54(state):
    """Remove payment from paid INV-0001."""
    inv = find_invoice_by_number(state, "INV-0001")
    pay = next(p for p in state["payments"] if p["invoiceId"] == inv["id"])
    state["payments"] = [p for p in state["payments"] if p["id"] != pay["id"]]
    inv["amountPaid"] = round(inv["amountPaid"] - pay["amount"], 2)
    if inv["amountPaid"] < 0:
        inv["amountPaid"] = 0
    inv["amountDue"] = round(inv["total"] - inv["amountPaid"], 2)
    inv["status"] = "awaiting_payment"
    inv["paidAt"] = None
    inv["updatedAt"] = NOW


def solve_task_55(state):
    """Void overdue INV-0033."""
    inv = find_invoice_by_number(state, "INV-0033")
    inv["status"] = "voided"
    inv["voidedAt"] = NOW
    inv["updatedAt"] = NOW
    inv["activity"].append({"type": "voided", "date": NOW, "user": "System", "detail": "Invoice voided"})


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
    """Run Node.js to evaluate data.js and return the seed state as a dict."""
    data_js = str(APP_DIR / "js" / "data.js")
    result = subprocess.run(
        ["node", "-e", _SEED_STATE_JS, data_js],
        capture_output=True, text=True, timeout=10,
    )
    if result.returncode != 0:
        print(f"FATAL: seed state generation failed:\n{result.stderr}", file=sys.stderr)
        sys.exit(1)
    return json.loads(result.stdout)


def seed_server(server_url, seed_state):
    """PUT seed state to the server."""
    resp = requests.put(f"{server_url}/api/state",
                        json=seed_state, timeout=5)
    assert resp.status_code == 200, f"Seed PUT failed: {resp.status_code}"


def find_free_port(start=9000):
    """Find a free TCP port starting from `start`."""
    for port in range(start, start + 200):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(("127.0.0.1", port))
                return port
        except OSError:
            continue
    raise RuntimeError("No free port found")


def start_server(port):
    """Launch server.py on the given port, wait until ready."""
    proc = subprocess.Popen(
        [sys.executable, str(APP_DIR / "server.py"), "--port", str(port)],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        cwd=str(APP_DIR),
    )
    for _ in range(40):
        try:
            requests.get(f"http://localhost:{port}/", timeout=0.5)
            return proc
        except Exception:
            time.sleep(0.25)
    proc.terminate()
    raise RuntimeError(f"Server on port {port} did not start in time")


def stop_server(proc):
    """Stop the server process."""
    proc.terminate()
    try:
        proc.wait(timeout=5)
    except subprocess.TimeoutExpired:
        proc.kill()


# ── task runner ──────────────────────────────────────────────────────

def load_tasks():
    with open(TASKS_FILE) as f:
        return json.load(f)


def load_verifier(verify_path):
    """Dynamically import a verifier module, return its verify function."""
    abs_path = APP_DIR / verify_path
    spec = importlib.util.spec_from_file_location("verifier", abs_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.verify


def run_single_task(task, server_url, seed_state):
    """Reset → solve → verify for a single task. Returns (task_id, passed, msg)."""
    task_id = task["id"]
    try:
        solver = SOLVERS.get(task_id)
        if not solver:
            return task_id, False, f"No solver for {task_id}"

        # 1. Reset: PUT seed state
        state = deepcopy(seed_state)
        seed_server(server_url, state)

        # 2. Solve: mutate state in Python
        solver(state)

        # 3. Write solved state
        resp = requests.put(f"{server_url}/api/state", json=state, timeout=5)
        assert resp.status_code == 200

        # 4. Verify
        verify = load_verifier(task["verify"])
        passed, msg = verify(server_url)
        return task_id, passed, msg

    except Exception as e:
        return task_id, False, f"Exception: {e}"


def run_tasks_sequential(tasks, port, seed_state):
    """Run all tasks on a single server, sequentially."""
    proc = start_server(port)
    server_url = f"http://localhost:{port}"
    results = []
    try:
        for task in tasks:
            results.append(run_single_task(task, server_url, seed_state))
    finally:
        stop_server(proc)
    return results


def run_tasks_parallel(tasks, workers, base_port, seed_state):
    """Run tasks in parallel, one server per worker."""
    results = []

    def worker_fn(task, port):
        proc = start_server(port)
        server_url = f"http://localhost:{port}"
        try:
            return run_single_task(task, server_url, seed_state)
        finally:
            stop_server(proc)

    ports = []
    p = base_port
    for _ in range(len(tasks)):
        p = find_free_port(p)
        ports.append(p)
        p += 1

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(worker_fn, task, port): task["id"]
            for task, port in zip(tasks, ports)
        }
        for future in as_completed(futures):
            results.append(future.result())
    return results


# ── main ─────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Sanity check for function tasks")
    parser.add_argument("--task-id", help="Run a single task by ID")
    parser.add_argument("--workers", type=int, default=1, help="Parallel workers")
    parser.add_argument("--port", type=int, default=9100, help="Base port")
    args = parser.parse_args()

    tasks = load_tasks()
    if args.task_id:
        tasks = [t for t in tasks if t["id"] == args.task_id]
        if not tasks:
            print(f"Task {args.task_id} not found")
            sys.exit(1)

    print(f"Generating seed state...")
    seed_state = generate_seed_state()
    print(f"Running {len(tasks)} task(s) with {args.workers} worker(s)...\n")

    if args.workers <= 1:
        port = find_free_port(args.port)
        results = run_tasks_sequential(tasks, port, seed_state)
    else:
        results = run_tasks_parallel(tasks, args.workers, args.port, seed_state)

    # Sort by task ID for consistent output
    results.sort(key=lambda r: int(r[0].split("_")[1]))

    passed = 0
    failed = []
    for task_id, ok, msg in results:
        status = "\033[32m  PASS\033[0m" if ok else "\033[31m  FAIL\033[0m"
        print(f"{status}  {task_id:10s}  {msg}")
        if ok:
            passed += 1
        else:
            failed.append(task_id)

    print(f"\n{passed}/{len(results)} passed")
    if failed:
        print(f"Failed: {', '.join(failed)}")
        sys.exit(1)
    else:
        print("All tasks passed!")


if __name__ == "__main__":
    main()
