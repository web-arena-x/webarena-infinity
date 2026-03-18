#!/usr/bin/env python3
"""
Sanity check for Xero Invoicing real tasks.

For each task, directly applies the expected end-state (bypassing the agent),
then runs the verifier and asserts it passes.

Usage:
    python3 sanity_check_real.py                     # All tasks, sequential
    python3 sanity_check_real.py --workers N          # N parallel environments
    python3 sanity_check_real.py --task-id task_e1    # Single task
    python3 sanity_check_real.py --port 9000          # Custom base port
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

NOW = "2026-03-18T12:00:00Z"
TODAY = "2026-03-18"


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


def find_invoice_by_id(state, inv_id):
    for inv in state["invoices"]:
        if inv["id"] == inv_id:
            return inv
    raise ValueError(f"Invoice not found: {inv_id!r}")


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

    sent_at = kwargs.get("sentAt", None)
    if sent_at:
        con = next((c for c in state["contacts"] if c["id"] == contact_id), None)
        email = con["email"] if con else "contact"
        activity.append({"type": "sent", "date": sent_at, "user": "System", "detail": f"Email sent to {email}"})

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
        "sentAt": sent_at,
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


def void_invoice(state, inv):
    """Void an invoice."""
    inv["status"] = "voided"
    inv["voidedAt"] = NOW
    inv["updatedAt"] = NOW
    inv["activity"].append({"type": "voided", "date": NOW, "user": "System", "detail": "Invoice voided"})


def approve_invoice(state, inv):
    """Approve an invoice."""
    inv["status"] = "awaiting_payment"
    inv["updatedAt"] = NOW
    inv["activity"].append({"type": "approved", "date": NOW, "user": "System", "detail": "Invoice approved"})


def send_invoice(state, inv):
    """Approve (if needed) and send an invoice."""
    if inv["status"] in ("draft", "awaiting_approval"):
        inv["status"] = "awaiting_payment"
        inv["activity"].append({"type": "approved", "date": NOW, "user": "System", "detail": "Invoice approved"})
    inv["sentAt"] = NOW
    inv["updatedAt"] = NOW
    con = next((c for c in state["contacts"] if c["id"] == inv["contactId"]), None)
    email = con["email"] if con else "contact"
    inv["activity"].append({"type": "sent", "date": NOW, "user": "System", "detail": f"Email sent to {email}"})


def create_contact(state, name, email, phone="", street="", city="", region="", postal_code="", country="New Zealand", tax_id=""):
    """Create a new contact."""
    cid = next_contact_id(state)
    contact = {
        "id": f"con_{cid}",
        "name": name,
        "email": email,
        "phone": phone,
        "billingAddress": {
            "street": street,
            "city": city,
            "region": region,
            "postalCode": postal_code,
            "country": country,
        },
        "taxId": tax_id,
        "contactType": "customer",
        "createdAt": NOW,
    }
    state["contacts"].append(contact)
    return contact


# ── solve functions ──────────────────────────────────────────────────

# ---------- EASY ----------

def solve_task_e1(state):
    """Approve invoice INV-0008."""
    inv = find_invoice_by_number(state, "INV-0008")
    approve_invoice(state, inv)


def solve_task_e2(state):
    """Void overdue invoice INV-0015 for Bloom & Branch Florists."""
    inv = find_invoice_by_number(state, "INV-0015")
    void_invoice(state, inv)


def solve_task_e3(state):
    """Delete draft invoice INV-0054."""
    inv = find_invoice_by_number(state, "INV-0054")
    state["invoices"] = [i for i in state["invoices"] if i["id"] != inv["id"]]
    state["payments"] = [p for p in state["payments"] if p["invoiceId"] != inv["id"]]


def solve_task_e4(state):
    """Change company name to Kiwi Consulting Group."""
    state["settings"]["companyName"] = "Kiwi Consulting Group"


def solve_task_e5(state):
    """Update invoice number prefix to KCL-."""
    state["settings"]["invoiceNumberPrefix"] = "KCL-"


def solve_task_e6(state):
    """Approve the Bright Spark Electrical draft invoice (INV-0005)."""
    inv = find_invoice_by_number(state, "INV-0005")
    approve_invoice(state, inv)


def solve_task_e7(state):
    """Change email for Ridgeway University."""
    con = find_contact_by_name(state, "Ridgeway University")
    con["email"] = "billing@ridgewayuni.ac.nz"


def solve_task_e8(state):
    """Enable late payment penalties."""
    state["settings"]["latePenaltyEnabled"] = True


def solve_task_e9(state):
    """Change default tax rate to No GST (0%)."""
    state["settings"]["defaultTaxRateId"] = "tax_3"


def solve_task_e10(state):
    """Update phone for Coastal Cafe Group."""
    con = find_contact_by_name(state, "Coastal Cafe Group")
    con["phone"] = "+64 3 441 9999"


def solve_task_e11(state):
    """Send invoice INV-0017."""
    inv = find_invoice_by_number(state, "INV-0017")
    send_invoice(state, inv)


def solve_task_e12(state):
    """Change default branding theme to Professional Blue."""
    state["settings"]["defaultBrandingThemeId"] = "theme_2"


def solve_task_e13(state):
    """Update company tax ID."""
    state["settings"]["companyTaxId"] = "NZ-98-765-432"


def solve_task_e14(state):
    """Set late penalty rate to 2.5%."""
    state["settings"]["latePenaltyRate"] = 2.5


def solve_task_e15(state):
    """Change billing city for Oceanview Resort & Spa."""
    con = find_contact_by_name(state, "Oceanview Resort & Spa")
    con["billingAddress"]["city"] = "Takapuna"


def solve_task_e16(state):
    """Set next invoice number to 200."""
    state["settings"]["invoiceNumberNextNumber"] = 200


def solve_task_e17(state):
    """Change default due date terms to 30."""
    state["settings"]["defaultDueDateTerms"] = "30"


def solve_task_e18(state):
    """Void invoice INV-0068."""
    inv = find_invoice_by_number(state, "INV-0068")
    void_invoice(state, inv)


def solve_task_e19(state):
    """Update company email."""
    state["settings"]["companyEmail"] = "finance@kiwiconsulting.co.nz"


def solve_task_e20(state):
    """Change late penalty frequency to weekly."""
    state["settings"]["latePenaltyFrequency"] = "weekly"


# ---------- MEDIUM ----------

def solve_task_m1(state):
    """Record full payment for INV-0007."""
    inv = find_invoice_by_number(state, "INV-0007")
    add_payment(state, inv["id"], inv["amountDue"], "bank_1")


def solve_task_m2(state):
    """Create contact Southern Cross Logistics."""
    create_contact(state, "Southern Cross Logistics", "logistics@southerncross.co.nz",
                   phone="+64 9 300 1234", street="10 Customs Street",
                   city="Auckland", region="Auckland", postal_code="1010", country="New Zealand")


def solve_task_m3(state):
    """Copy invoice INV-0009 as draft."""
    orig = find_invoice_by_number(state, "INV-0009")
    li_raw = [{"description": li["description"], "quantity": li["quantity"],
               "unitPrice": li["unitPrice"], "taxRateId": li["taxRateId"],
               "accountCode": li["accountCode"]} for li in orig["lineItems"]]
    ref = (orig["reference"] + " (copy)") if orig["reference"] else ""
    make_invoice(state, orig["contactId"], li_raw,
                 reference=ref, notes=orig["notes"], currency=orig["currency"],
                 brandingThemeId=orig["brandingThemeId"])


def solve_task_m4(state):
    """Record $2,000 partial payment on INV-0039."""
    inv = find_invoice_by_number(state, "INV-0039")
    add_payment(state, inv["id"], 2000, "bank_1")


def solve_task_m5(state):
    """Update reference on INV-0042."""
    inv = find_invoice_by_number(state, "INV-0042")
    inv["reference"] = "WO-55555"
    inv["updatedAt"] = NOW


def solve_task_m6(state):
    """Update Harmony Music Academy billing address."""
    con = find_contact_by_name(state, "Harmony Music Academy")
    con["billingAddress"] = {
        "street": "100 Willis Street",
        "city": "Wellington",
        "region": "Wellington",
        "postalCode": "6011",
        "country": "New Zealand",
    }


def solve_task_m7(state):
    """Update email template subject."""
    state["settings"]["defaultEmailSubject"] = "Invoice {InvoiceNumber} - Kiwi Consulting Group"


def solve_task_m8(state):
    """Approve and send INV-0038."""
    inv = find_invoice_by_number(state, "INV-0038")
    send_invoice(state, inv)


def solve_task_m9(state):
    """Add line item to INV-0083."""
    inv = find_invoice_by_number(state, "INV-0083")
    lid = next_line_item_id(state)
    new_li = {
        "id": f"li_{lid}",
        "description": "Express delivery surcharge",
        "quantity": 1,
        "unitPrice": 150,
        "taxRateId": "tax_1",
        "accountCode": "200",
        "lineTotal": 150.0,
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


def solve_task_m10(state):
    """Create new draft invoice for Ridgeway University."""
    con = find_contact_by_name(state, "Ridgeway University")
    make_invoice(state, con["id"], [
        {"description": "Annual subscription renewal", "quantity": 1, "unitPrice": 4500,
         "taxRateId": "tax_1", "accountCode": "200"},
    ], issueDate="2026-03-18", dueDate="2026-04-17")


def solve_task_m11(state):
    """Record full payment for INV-0087."""
    inv = find_invoice_by_number(state, "INV-0087")
    add_payment(state, inv["id"], inv["amountDue"], "bank_1")


def solve_task_m12(state):
    """Update currency on INV-0020 to NZD."""
    inv = find_invoice_by_number(state, "INV-0020")
    inv["currency"] = "NZD"
    inv["updatedAt"] = NOW


def solve_task_m13(state):
    """Change branding theme on INV-0084 to Bold Corporate."""
    inv = find_invoice_by_number(state, "INV-0084")
    inv["brandingThemeId"] = "theme_4"
    inv["updatedAt"] = NOW


def solve_task_m14(state):
    """Update DataFlow Analytics Inc tax ID."""
    con = find_contact_by_name(state, "DataFlow Analytics Inc")
    con["taxId"] = "US-95-7654321"


def solve_task_m15(state):
    """Record remaining balance on INV-0034."""
    inv = find_invoice_by_number(state, "INV-0034")
    add_payment(state, inv["id"], inv["amountDue"], "bank_1")


def solve_task_m16(state):
    """Change invoice number padding to 5 and prefix to KINV-."""
    state["settings"]["invoiceNumberPadding"] = 5
    state["settings"]["invoiceNumberPrefix"] = "KINV-"


def solve_task_m17(state):
    """Approve all awaiting_approval invoices for Hamilton Plumbing Services."""
    con = find_contact_by_name(state, "Hamilton Plumbing Services")
    for inv in state["invoices"]:
        if inv["contactId"] == con["id"] and inv["status"] == "awaiting_approval":
            approve_invoice(state, inv)


def solve_task_m18(state):
    """Update notes on INV-0093."""
    inv = find_invoice_by_number(state, "INV-0093")
    inv["notes"] = "Payment due strictly within 14 days"
    inv["updatedAt"] = NOW


def solve_task_m19(state):
    """Create contact Horizon Architecture Studio."""
    create_contact(state, "Horizon Architecture Studio", "hello@horizonarch.co.nz",
                   street="200 Parnell Road", city="Auckland", region="Auckland",
                   postal_code="1052", country="New Zealand")


def solve_task_m20(state):
    """Change default email body."""
    state["settings"]["defaultEmailBody"] = (
        "Dear {ContactName},\n\n"
        "Attached is invoice {InvoiceNumber} for {Total}, due {DueDate}.\n\n"
        "Thank you,\nKiwi Consulting Group"
    )


# ---------- HARD ----------

def solve_task_h1(state):
    """Void all overdue invoices for Bloom & Branch Florists."""
    con = find_contact_by_name(state, "Bloom & Branch Florists")
    for inv in state["invoices"]:
        if inv["contactId"] == con["id"] and inv["status"] == "overdue":
            void_invoice(state, inv)


def solve_task_h2(state):
    """Create approved invoice for Nexus Technologies Ltd with 3 line items."""
    con = find_contact_by_name(state, "Nexus Technologies Ltd")
    make_invoice(state, con["id"], [
        {"description": "Cloud migration services", "quantity": 40, "unitPrice": 200,
         "taxRateId": "tax_1", "accountCode": "200"},
        {"description": "Database optimization", "quantity": 16, "unitPrice": 250,
         "taxRateId": "tax_1", "accountCode": "200"},
        {"description": "Security audit", "quantity": 8, "unitPrice": 300,
         "taxRateId": "tax_1", "accountCode": "200"},
    ], issueDate="2026-03-18", dueDate="2026-04-07", reference="PROJ-NEXUS-01",
       status="awaiting_payment")


def solve_task_h3(state):
    """Record full payments for all overdue Nexus Technologies invoices."""
    con = find_contact_by_name(state, "Nexus Technologies Ltd")
    for inv in state["invoices"]:
        if inv["contactId"] == con["id"] and inv["status"] == "overdue":
            add_payment(state, inv["id"], inv["amountDue"], "bank_1")


def solve_task_h4(state):
    """Delete all AUD draft invoices."""
    to_delete = [inv["id"] for inv in state["invoices"]
                 if inv["status"] == "draft" and inv["currency"] == "AUD"]
    for inv_id in to_delete:
        state["invoices"] = [i for i in state["invoices"] if i["id"] != inv_id]
        state["payments"] = [p for p in state["payments"] if p["invoiceId"] != inv_id]


def solve_task_h5(state):
    """Update company details in settings."""
    state["settings"]["companyName"] = "Kiwi Consulting Group"
    state["settings"]["companyEmail"] = "hello@kiwiconsulting.co.nz"
    state["settings"]["companyPhone"] = "+64 9 555 0200"
    state["settings"]["companyAddress"] = "100 Queen Street, Level 10, Auckland 1010, New Zealand"


def solve_task_h6(state):
    """Create contact Tasman Engineering Ltd and a draft invoice."""
    contact = create_contact(state, "Tasman Engineering Ltd", "accounts@tasmaneng.co.nz",
                             phone="+64 3 545 1234", street="25 Trafalgar Street",
                             city="Nelson", region="Nelson", postal_code="7010",
                             country="New Zealand", tax_id="NZ-45-678-901")
    make_invoice(state, contact["id"], [
        {"description": "Structural engineering consultation", "quantity": 24, "unitPrice": 180,
         "taxRateId": "tax_1", "accountCode": "200"},
        {"description": "Site inspection report", "quantity": 1, "unitPrice": 750,
         "taxRateId": "tax_1", "accountCode": "200"},
    ], issueDate="2026-03-18", dueDate="2026-04-17")


def solve_task_h7(state):
    """Approve and send all NZD awaiting_approval invoices."""
    for inv in state["invoices"]:
        if inv["status"] == "awaiting_approval" and inv["currency"] == "NZD":
            send_invoice(state, inv)


def solve_task_h8(state):
    """Record full payments for INV-0059 and INV-0089."""
    for num in ["INV-0059", "INV-0089"]:
        inv = find_invoice_by_number(state, num)
        add_payment(state, inv["id"], inv["amountDue"], "bank_1")


def solve_task_h9(state):
    """Copy INV-0001, change contact to Meridian Health Clinic."""
    orig = find_invoice_by_number(state, "INV-0001")
    con = find_contact_by_name(state, "Meridian Health Clinic")
    li_raw = [{"description": li["description"], "quantity": li["quantity"],
               "unitPrice": li["unitPrice"], "taxRateId": li["taxRateId"],
               "accountCode": li["accountCode"]} for li in orig["lineItems"]]
    ref = (orig["reference"] + " (copy)") if orig["reference"] else ""
    make_invoice(state, con["id"], li_raw,
                 reference=ref, notes=orig["notes"], currency=orig["currency"],
                 brandingThemeId=orig["brandingThemeId"])


def solve_task_h10(state):
    """Change multiple settings: prefix, next number, padding, branding, tax."""
    state["settings"]["invoiceNumberPrefix"] = "RC-"
    state["settings"]["invoiceNumberNextNumber"] = 500
    state["settings"]["invoiceNumberPadding"] = 5
    state["settings"]["defaultBrandingThemeId"] = "theme_3"
    state["settings"]["defaultTaxRateId"] = "tax_5"


def solve_task_h11(state):
    """Record remaining balance on all partially-paid invoices."""
    for inv in state["invoices"]:
        if inv["status"] == "awaiting_payment" and inv["amountPaid"] > 0 and inv["amountDue"] > 0.01:
            add_payment(state, inv["id"], inv["amountDue"], "bank_1")


def solve_task_h12(state):
    """Create, approve, and send invoice for Ironclad Security Systems."""
    con = find_contact_by_name(state, "Ironclad Security Systems")
    inv = make_invoice(state, con["id"], [
        {"description": "CCTV installation - 8 cameras", "quantity": 8, "unitPrice": 450,
         "taxRateId": "tax_1", "accountCode": "200"},
        {"description": "Annual monitoring subscription", "quantity": 1, "unitPrice": 2400,
         "taxRateId": "tax_1", "accountCode": "200"},
    ], issueDate="2026-03-18", dueDate="2026-04-17", reference="SEC-2026-001",
       brandingThemeId="theme_4", status="awaiting_payment", sentAt=NOW)


def solve_task_h13(state):
    """Void all overdue invoices with reference starting with PROJ-."""
    for inv in state["invoices"]:
        if inv["status"] == "overdue" and inv.get("reference", "").startswith("PROJ-"):
            void_invoice(state, inv)


def solve_task_h14(state):
    """Update Wellington contacts postal code to 6012."""
    for con in state["contacts"]:
        addr = con.get("billingAddress", {})
        if addr.get("city") == "Wellington" and addr.get("postalCode") == "6011":
            addr["postalCode"] = "6012"


def solve_task_h15(state):
    """Delete all draft invoices for Metro Print Solutions and Apex Legal Partners."""
    con_metro = find_contact_by_name(state, "Metro Print Solutions")
    con_apex = find_contact_by_name(state, "Apex Legal Partners")
    target_ids = {con_metro["id"], con_apex["id"]}
    to_delete = [inv["id"] for inv in state["invoices"]
                 if inv["status"] == "draft" and inv["contactId"] in target_ids]
    for inv_id in to_delete:
        state["invoices"] = [i for i in state["invoices"] if i["id"] != inv_id]
        state["payments"] = [p for p in state["payments"] if p["invoiceId"] != inv_id]


def solve_task_h16(state):
    """Create AUD draft invoice for CloudBridge Software."""
    con = find_contact_by_name(state, "CloudBridge Software")
    make_invoice(state, con["id"], [
        {"description": "API integration development", "quantity": 60, "unitPrice": 175,
         "taxRateId": "tax_1", "accountCode": "200"},
        {"description": "Technical documentation", "quantity": 20, "unitPrice": 120,
         "taxRateId": "tax_1", "accountCode": "200"},
    ], currency="AUD", issueDate="2026-03-18", dueDate="2026-04-17", reference="CB-INT-001")


def solve_task_h17(state):
    """Approve INV-0066 and record $30,000 payment."""
    inv = find_invoice_by_number(state, "INV-0066")
    approve_invoice(state, inv)
    add_payment(state, inv["id"], 30000, "bank_1")


def solve_task_h18(state):
    """Enable late penalties at 3% weekly, due terms 14, branding Bold Corporate."""
    state["settings"]["latePenaltyEnabled"] = True
    state["settings"]["latePenaltyRate"] = 3
    state["settings"]["latePenaltyFrequency"] = "weekly"
    state["settings"]["defaultDueDateTerms"] = "14"
    state["settings"]["defaultBrandingThemeId"] = "theme_4"


def solve_task_h19(state):
    """Record full payments for overdue invoices with REF or QUO in reference."""
    for inv in state["invoices"]:
        if inv["status"] == "overdue":
            ref = inv.get("reference", "")
            if "REF" in ref or "QUO" in ref:
                add_payment(state, inv["id"], inv["amountDue"], "bank_1")


def solve_task_h20(state):
    """Create contact Pacific Digital Solutions and a draft invoice."""
    contact = create_contact(state, "Pacific Digital Solutions", "billing@pacificdigital.co.nz",
                             phone="+64 9 888 7777", street="55 Victoria Street West",
                             city="Auckland", region="Auckland", postal_code="1010",
                             country="New Zealand")
    make_invoice(state, contact["id"], [
        {"description": "Website redesign", "quantity": 1, "unitPrice": 8000,
         "taxRateId": "tax_1", "accountCode": "200"},
        {"description": "SEO package - 6 months", "quantity": 6, "unitPrice": 500,
         "taxRateId": "tax_1", "accountCode": "200"},
        {"description": "Content writing", "quantity": 10, "unitPrice": 150,
         "taxRateId": "tax_1", "accountCode": "200"},
    ], issueDate="2026-03-18", dueDate="2026-04-17")


# ---------- HARD (hardening round 1) ----------

def solve_task_h21(state):
    """Delete every draft invoice for contacts with billing city Auckland."""
    auckland_ids = {c["id"] for c in state["contacts"]
                    if c.get("billingAddress", {}).get("city") == "Auckland"}
    to_delete = [inv["id"] for inv in state["invoices"]
                 if inv["status"] == "draft" and inv["contactId"] in auckland_ids]
    for inv_id in to_delete:
        state["invoices"] = [i for i in state["invoices"] if i["id"] != inv_id]
        state["payments"] = [p for p in state["payments"] if p["invoiceId"] != inv_id]


def solve_task_h22(state):
    """Record half-payment on the overdue invoice with the largest total (inv_40)."""
    overdue = [i for i in state["invoices"] if i["status"] == "overdue"]
    overdue.sort(key=lambda i: i["total"], reverse=True)
    inv = overdue[0]  # inv_40, total=121725
    half = round(inv["total"] / 2, 2)
    add_payment(state, inv["id"], half, "bank_1")


def solve_task_h23(state):
    """Approve all awaiting-approval invoices with PO- reference."""
    for inv in state["invoices"]:
        if inv["status"] == "awaiting_approval" and inv.get("reference", "").startswith("PO-"):
            approve_invoice(state, inv)


def solve_task_h24(state):
    """Create Alpine Adventure Tours contact and approved invoice."""
    contact = create_contact(state, "Alpine Adventure Tours", "bookings@alpineadventure.co.nz",
                             phone="+64 3 442 5678", street="30 Camp Street",
                             city="Queenstown", region="Otago", postal_code="9300",
                             country="New Zealand", tax_id="NZ-55-123-456")
    make_invoice(state, contact["id"], [
        {"description": "Guided tour package", "quantity": 10, "unitPrice": 350,
         "taxRateId": "tax_1", "accountCode": "200"},
        {"description": "Equipment hire - 3 days", "quantity": 3, "unitPrice": 200,
         "taxRateId": "tax_1", "accountCode": "200"},
    ], issueDate="2026-03-18", dueDate="2026-04-17", reference="TOUR-2026-01",
       status="awaiting_payment")


def solve_task_h25(state):
    """Pay the oldest overdue invoice (earliest issue date) via Business Savings."""
    overdue = [i for i in state["invoices"] if i["status"] == "overdue"]
    overdue.sort(key=lambda i: i["issueDate"])
    inv = overdue[0]  # inv_87, issueDate=2025-10-13
    add_payment(state, inv["id"], inv["amountDue"], "bank_2")


def solve_task_h26(state):
    """Void all overdue AUD invoices."""
    for inv in state["invoices"]:
        if inv["status"] == "overdue" and inv.get("currency") == "AUD":
            void_invoice(state, inv)


def solve_task_h27(state):
    """Pay all overdue invoices for the Ponsonby Road contact (Bloom & Branch)."""
    ponsonby = next(c for c in state["contacts"]
                    if "Ponsonby" in c.get("billingAddress", {}).get("street", ""))
    for inv in state["invoices"]:
        if inv["contactId"] == ponsonby["id"] and inv["status"] == "overdue":
            add_payment(state, inv["id"], inv["amountDue"], "bank_1")


def solve_task_h28(state):
    """Copy the highest-total paid invoice as a draft."""
    paid = [i for i in state["invoices"] if i["status"] == "paid"]
    paid.sort(key=lambda i: i["total"], reverse=True)
    orig = paid[0]  # inv_48, total=88550
    li_raw = [{"description": li["description"], "quantity": li["quantity"],
               "unitPrice": li["unitPrice"], "taxRateId": li["taxRateId"],
               "accountCode": li["accountCode"]} for li in orig["lineItems"]]
    ref = (orig["reference"] + " (copy)") if orig["reference"] else ""
    make_invoice(state, orig["contactId"], li_raw,
                 reference=ref, notes=orig["notes"], currency=orig["currency"],
                 brandingThemeId=orig["brandingThemeId"])


def solve_task_h29(state):
    """Change default tax to AU GST and create AUD draft for CloudBridge."""
    state["settings"]["defaultTaxRateId"] = "tax_7"
    con = find_contact_by_name(state, "CloudBridge Software")
    make_invoice(state, con["id"], [
        {"description": "Quarterly SaaS license", "quantity": 1, "unitPrice": 9600,
         "taxRateId": "tax_7", "accountCode": "200"},
    ], currency="AUD", issueDate="2026-03-18", dueDate="2026-06-18")


def solve_task_h30(state):
    """Approve awaiting-approval invoices for contacts that have overdue invoices."""
    contacts_with_overdue = {inv["contactId"] for inv in state["invoices"]
                             if inv["status"] == "overdue"}
    for inv in state["invoices"]:
        if inv["status"] == "awaiting_approval" and inv["contactId"] in contacts_with_overdue:
            approve_invoice(state, inv)


def solve_task_h31(state):
    """Green Valley Organics: void overdue, approve awaiting, delete drafts."""
    con = find_contact_by_name(state, "Green Valley Organics")
    for inv in state["invoices"]:
        if inv["contactId"] == con["id"]:
            if inv["status"] == "overdue":
                void_invoice(state, inv)
            elif inv["status"] == "awaiting_approval":
                approve_invoice(state, inv)
    # Delete drafts (after iteration to avoid modifying list during loop)
    to_delete = [inv["id"] for inv in state["invoices"]
                 if inv["contactId"] == con["id"] and inv["status"] == "draft"]
    for inv_id in to_delete:
        state["invoices"] = [i for i in state["invoices"] if i["id"] != inv_id]
        state["payments"] = [p for p in state["payments"] if p["invoiceId"] != inv_id]


def solve_task_h32(state):
    """Update billing street for the US contact (DataFlow Analytics)."""
    con = next(c for c in state["contacts"]
               if c.get("billingAddress", {}).get("country") == "United States")
    con["billingAddress"]["street"] = "600 Market Street, Suite 500"


def solve_task_h33(state):
    """Update billing region for both Hamilton contacts."""
    for con in state["contacts"]:
        if con.get("billingAddress", {}).get("city") == "Hamilton":
            con["billingAddress"]["region"] = "Waikato Region"


def solve_task_h34(state):
    """Pay all overdue invoices for Auckland-region contacts."""
    auckland_ids = {c["id"] for c in state["contacts"]
                    if c.get("billingAddress", {}).get("region") == "Auckland"}
    for inv in state["invoices"]:
        if inv["status"] == "overdue" and inv["contactId"] in auckland_ids:
            add_payment(state, inv["id"], inv["amountDue"], "bank_1")


def solve_task_h35(state):
    """PROJ-ALPHA awaiting-approval: add line item, approve, send."""
    inv = next(i for i in state["invoices"]
               if i.get("reference") == "PROJ-ALPHA" and i["status"] == "awaiting_approval")
    lid = next_line_item_id(state)
    new_li = {
        "id": f"li_{lid}",
        "description": "Project closeout documentation",
        "quantity": 5,
        "unitPrice": 120,
        "taxRateId": "tax_1",
        "accountCode": "200",
        "lineTotal": 600.0,
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
    send_invoice(state, inv)


def solve_task_h36(state):
    """Create AUD invoice for Australia contact (CloudBridge), approve."""
    con = next(c for c in state["contacts"]
               if c.get("billingAddress", {}).get("country") == "Australia")
    make_invoice(state, con["id"], [
        {"description": "Architecture review", "quantity": 8, "unitPrice": 300,
         "taxRateId": "tax_1", "accountCode": "200"},
        {"description": "Performance testing", "quantity": 16, "unitPrice": 200,
         "taxRateId": "tax_1", "accountCode": "200"},
    ], currency="AUD", issueDate="2026-03-18", dueDate="2026-05-18",
       reference="AU-REVIEW-001", status="awaiting_payment")


def solve_task_h37(state):
    """Delete all draft invoices with empty reference."""
    to_delete = [inv["id"] for inv in state["invoices"]
                 if inv["status"] == "draft" and not inv.get("reference")]
    for inv_id in to_delete:
        state["invoices"] = [i for i in state["invoices"] if i["id"] != inv_id]
        state["payments"] = [p for p in state["payments"] if p["invoiceId"] != inv_id]


def solve_task_h38(state):
    """Update phone for contact of max-amountDue awaiting-payment invoice."""
    awaiting = [i for i in state["invoices"] if i["status"] == "awaiting_payment"]
    awaiting.sort(key=lambda i: i["amountDue"], reverse=True)
    top_inv = awaiting[0]  # inv_22, Meridian Health Clinic
    con = next(c for c in state["contacts"] if c["id"] == top_inv["contactId"])
    con["phone"] = "+64 9 999 0000"


def solve_task_h39(state):
    """Update notes on draft/awaiting-approval invoices with QUO in reference."""
    for inv in state["invoices"]:
        if inv["status"] in ("draft", "awaiting_approval") and "QUO" in inv.get("reference", ""):
            inv["notes"] = "Quote-linked invoice - review before sending"
            inv["updatedAt"] = NOW


def solve_task_h40(state):
    """Create Summit Events Ltd contact and invoice, approve and send."""
    contact = create_contact(state, "Summit Events Ltd", "events@summitevents.co.nz",
                             phone="+64 9 555 3456", street="45 Queen Street",
                             city="Auckland", region="Auckland", postal_code="1010",
                             country="New Zealand")
    inv = make_invoice(state, contact["id"], [
        {"description": "Venue hire - full day", "quantity": 1, "unitPrice": 2500,
         "taxRateId": "tax_1", "accountCode": "200"},
        {"description": "Catering package - 50 guests", "quantity": 50, "unitPrice": 85,
         "taxRateId": "tax_1", "accountCode": "200"},
        {"description": "AV equipment rental", "quantity": 1, "unitPrice": 1200,
         "taxRateId": "tax_1", "accountCode": "200"},
    ], issueDate="2026-03-18", dueDate="2026-04-17", reference="EVT-2026-001",
       status="awaiting_payment", sentAt=NOW)


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
    """Reset -> solve -> verify for a single task. Returns (task_id, passed, msg)."""
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

def _sort_key(task_id):
    """Sort key: e < m < h, then by number."""
    parts = task_id.split("_", 1)
    if len(parts) == 2:
        prefix = parts[1][0]  # e, m, or h
        order = {"e": 0, "m": 1, "h": 2}.get(prefix, 3)
        num = int(parts[1][1:]) if parts[1][1:].isdigit() else 0
        return (order, num)
    return (9, 0)


def main():
    parser = argparse.ArgumentParser(description="Sanity check for real tasks")
    parser.add_argument("--task-id", help="Run a single task by ID")
    parser.add_argument("--workers", type=int, default=1, help="Parallel workers")
    parser.add_argument("--port", type=int, default=9200, help="Base port")
    args = parser.parse_args()

    tasks = load_tasks()
    if args.task_id:
        tasks = [t for t in tasks if t["id"] == args.task_id]
        if not tasks:
            print(f"Task {args.task_id} not found")
            sys.exit(1)

    print("Generating seed state...")
    seed_state = generate_seed_state()
    print(f"Running {len(tasks)} task(s) with {args.workers} worker(s)...\n")

    if args.workers <= 1:
        port = find_free_port(args.port)
        results = run_tasks_sequential(tasks, port, seed_state)
    else:
        results = run_tasks_parallel(tasks, args.workers, args.port, seed_state)

    # Sort by task ID
    results.sort(key=lambda r: _sort_key(r[0]))

    passed = 0
    failed = []
    for task_id, ok, msg in results:
        status = "\033[32m  PASS\033[0m" if ok else "\033[31m  FAIL\033[0m"
        print(f"{status}  {task_id:12s}  {msg}")
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
