#!/usr/bin/env python3
"""
Sanity check for paypal-my-wallet real tasks.

For each task: reset -> apply solve (state mutation) -> verify -> assert pass.
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
    currentUser: JSON.parse(JSON.stringify(CURRENT_USER)),
    cards: JSON.parse(JSON.stringify(CARDS)),
    bankAccounts: JSON.parse(JSON.stringify(BANK_ACCOUNTS)),
    balances: JSON.parse(JSON.stringify(BALANCES)),
    cryptoHoldings: JSON.parse(JSON.stringify(CRYPTO_HOLDINGS)),
    paypalDebitCard: JSON.parse(JSON.stringify(PAYPAL_DEBIT_CARD)),
    savingsAccount: JSON.parse(JSON.stringify(SAVINGS_ACCOUNT)),
    payLaterPlans: JSON.parse(JSON.stringify(PAY_LATER_PLANS)),
    rewards: JSON.parse(JSON.stringify(REWARDS)),
    offers: JSON.parse(JSON.stringify(OFFERS)),
    giftCards: JSON.parse(JSON.stringify(GIFT_CARDS)),
    transactions: JSON.parse(JSON.stringify(TRANSACTIONS)),
    paypalCredit: JSON.parse(JSON.stringify(PAYPAL_CREDIT)),
    walletPreferences: JSON.parse(JSON.stringify(WALLET_PREFERENCES)),
    giftCardMerchants: JSON.parse(JSON.stringify(GIFT_CARD_MERCHANTS)),
    _nextCardId: 100,
    _nextBankId: 100,
    _nextTransactionId: 200,
    _nextGiftCardId: 100,
    _nextOfferId: 100,
    _nextRewardId: 100,
    _nextCryptoTxId: 200,
    _nextSavingsTxId: 100,
    _nextPlanId: 100,
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


def find_card(state, lastFour):
    return find_entity(state["cards"], lastFour=lastFour)


def find_bank(state, lastFour):
    return find_entity(state["bankAccounts"], lastFour=lastFour)


def find_balance(state, currency):
    return find_entity(state["balances"], currency=currency)


def find_crypto(state, symbol):
    return find_entity(state["cryptoHoldings"], symbol=symbol)


def find_offer(state, merchantName):
    return find_entity(state["offers"], merchantName=merchantName)


def now_iso():
    return "2026-03-07T12:00:00Z"


# ---------------------------------------------------------------------------
# Crypto fee calculation (mirrors state.js logic)
# ---------------------------------------------------------------------------

CRYPTO_FEE_SCHEDULE = [
    {"minAmount": 1, "maxAmount": 4.99, "fee": 0.49},
    {"minAmount": 5, "maxAmount": 24.99, "fee": 0.99},
    {"minAmount": 25, "maxAmount": 74.99, "fee": 1.99},
    {"minAmount": 75, "maxAmount": 200, "fee": 2.49},
    {"minAmount": 200.01, "maxAmount": None, "feePercent": 1.50},
]

EXCHANGE_RATES = {
    "USD": 1.0, "EUR": 0.92, "GBP": 0.79, "CAD": 1.36, "AUD": 1.54,
    "JPY": 149.50, "CHF": 0.88, "SEK": 10.42, "NOK": 10.68, "DKK": 6.87,
    "PLN": 3.98, "BRL": 4.97, "MXN": 17.15, "SGD": 1.34, "HKD": 7.82,
    "NZD": 1.64, "CZK": 22.85, "ILS": 3.67, "HUF": 356.20, "PHP": 55.80,
    "TWD": 31.45, "THB": 35.20, "INR": 83.10, "RUB": 92.50,
}


def calculate_crypto_fee(amount):
    for tier in CRYPTO_FEE_SCHEDULE:
        if amount >= tier["minAmount"] and (tier["maxAmount"] is None or amount <= tier["maxAmount"]):
            if "feePercent" in tier:
                return round(amount * tier["feePercent"]) / 100
            return tier["fee"]
    return 0


def convert_currency(state, from_currency, to_currency, amount):
    """Apply currency conversion matching state.js logic."""
    from_bal = find_balance(state, from_currency)
    to_bal = find_balance(state, to_currency)
    from_rate = EXCHANGE_RATES[from_currency]
    to_rate = EXCHANGE_RATES[to_currency]
    usd_amount = amount / from_rate
    converted = usd_amount * to_rate
    fee = usd_amount * 0.03
    from_bal["amount"] = round((from_bal["amount"] - amount) * 100) / 100
    to_bal["amount"] = round((to_bal["amount"] + converted - (fee * to_rate)) * 100) / 100
    txn_id = f"txn_{state['_nextTransactionId']:03d}"
    state["_nextTransactionId"] += 1
    state["transactions"].insert(0, {
        "id": txn_id,
        "type": "currency_convert",
        "description": f"Converted {from_currency} to {to_currency}",
        "amount": -amount,
        "currency": from_currency,
        "date": now_iso(),
        "status": "completed",
        "paymentMethod": "balance",
        "category": "Currency"
    })


def buy_crypto(state, symbol, usd_amount):
    """Apply crypto buy matching state.js logic."""
    usd = find_balance(state, "USD")
    crypto = find_crypto(state, symbol)
    fee = calculate_crypto_fee(usd_amount)
    net_amount = usd_amount - fee
    quantity = net_amount / crypto["currentPrice"]
    usd["amount"] = round((usd["amount"] - usd_amount) * 100) / 100
    crypto["quantity"] = round((crypto["quantity"] + quantity) * 100000) / 100000
    crypto["totalCost"] = round((crypto["totalCost"] + net_amount) * 100) / 100
    crypto["currentValue"] = round(crypto["quantity"] * crypto["currentPrice"] * 100) / 100
    crypto["totalReturn"] = round((crypto["currentValue"] - crypto["totalCost"]) * 100) / 100
    crypto["totalReturnPercent"] = round((crypto["totalReturn"] / crypto["totalCost"]) * 10000) / 100 if crypto["totalCost"] > 0 else 0
    crypto["averagePurchasePrice"] = round((crypto["totalCost"] / crypto["quantity"]) * 100) / 100 if crypto["quantity"] > 0 else 0
    ctx_id = f"ctx_{state['_nextCryptoTxId']:03d}"
    state["_nextCryptoTxId"] += 1
    crypto["transactions"].append({
        "id": ctx_id, "type": "buy", "quantity": quantity,
        "pricePerUnit": crypto["currentPrice"], "total": net_amount,
        "fee": fee, "date": now_iso()
    })
    txn_id = f"txn_{state['_nextTransactionId']:03d}"
    state["_nextTransactionId"] += 1
    state["transactions"].insert(0, {
        "id": txn_id, "type": "crypto_buy",
        "description": f"Bought {crypto['name']}",
        "amount": -usd_amount, "currency": "USD", "date": now_iso(),
        "status": "completed", "paymentMethod": "balance", "category": "Crypto"
    })


def sell_crypto(state, symbol, usd_amount):
    """Apply crypto sell matching state.js logic."""
    usd = find_balance(state, "USD")
    crypto = find_crypto(state, symbol)
    quantity = usd_amount / crypto["currentPrice"]
    fee = calculate_crypto_fee(usd_amount)
    net_proceeds = usd_amount - fee
    cost_basis = quantity * crypto["averagePurchasePrice"]
    crypto["quantity"] = round((crypto["quantity"] - quantity) * 100000) / 100000
    crypto["totalCost"] = max(0, round((crypto["totalCost"] - cost_basis) * 100) / 100)
    crypto["currentValue"] = round(crypto["quantity"] * crypto["currentPrice"] * 100) / 100
    crypto["totalReturn"] = round((crypto["currentValue"] - crypto["totalCost"]) * 100) / 100
    crypto["totalReturnPercent"] = round((crypto["totalReturn"] / crypto["totalCost"]) * 10000) / 100 if crypto["totalCost"] > 0 else 0
    usd["amount"] = round((usd["amount"] + net_proceeds) * 100) / 100
    ctx_id = f"ctx_{state['_nextCryptoTxId']:03d}"
    state["_nextCryptoTxId"] += 1
    crypto["transactions"].append({
        "id": ctx_id, "type": "sell", "quantity": quantity,
        "pricePerUnit": crypto["currentPrice"], "total": net_proceeds,
        "fee": fee, "date": now_iso()
    })
    txn_id = f"txn_{state['_nextTransactionId']:03d}"
    state["_nextTransactionId"] += 1
    state["transactions"].insert(0, {
        "id": txn_id, "type": "crypto_sell",
        "description": f"Sold {crypto['name']}",
        "amount": net_proceeds, "currency": "USD", "date": now_iso(),
        "status": "completed", "paymentMethod": "balance", "category": "Crypto"
    })


def deposit_to_savings(state, amount):
    """Move funds from USD balance to savings."""
    usd = find_balance(state, "USD")
    usd["amount"] = round((usd["amount"] - amount) * 100) / 100
    state["savingsAccount"]["balance"] = round((state["savingsAccount"]["balance"] + amount) * 100) / 100
    stx_id = f"stx_{state['_nextSavingsTxId']:03d}"
    state["_nextSavingsTxId"] += 1
    state["savingsAccount"]["transferHistory"].append({
        "id": stx_id, "type": "deposit", "amount": amount,
        "date": now_iso(), "from": "PayPal Balance"
    })
    txn_id = f"txn_{state['_nextTransactionId']:03d}"
    state["_nextTransactionId"] += 1
    state["transactions"].insert(0, {
        "id": txn_id, "type": "savings_deposit",
        "description": "Transfer to Savings", "amount": -amount,
        "currency": "USD", "date": now_iso(), "status": "completed",
        "paymentMethod": "balance", "category": "Savings"
    })


def withdraw_from_savings(state, amount):
    """Move funds from savings to USD balance."""
    usd = find_balance(state, "USD")
    usd["amount"] = round((usd["amount"] + amount) * 100) / 100
    state["savingsAccount"]["balance"] = round((state["savingsAccount"]["balance"] - amount) * 100) / 100
    stx_id = f"stx_{state['_nextSavingsTxId']:03d}"
    state["_nextSavingsTxId"] += 1
    state["savingsAccount"]["transferHistory"].append({
        "id": stx_id, "type": "withdrawal", "amount": amount,
        "date": now_iso(), "to": "PayPal Balance"
    })
    txn_id = f"txn_{state['_nextTransactionId']:03d}"
    state["_nextTransactionId"] += 1
    state["transactions"].insert(0, {
        "id": txn_id, "type": "savings_withdrawal",
        "description": "Transfer from Savings", "amount": amount,
        "currency": "USD", "date": now_iso(), "status": "completed",
        "paymentMethod": "balance", "category": "Savings"
    })


def add_money(state, amount, bank_last_four):
    """Add money from a bank to USD balance."""
    usd = find_balance(state, "USD")
    bank = find_bank(state, bank_last_four)
    usd["amount"] = round((usd["amount"] + amount) * 100) / 100
    txn_id = f"txn_{state['_nextTransactionId']:03d}"
    state["_nextTransactionId"] += 1
    state["transactions"].insert(0, {
        "id": txn_id, "type": "transfer_in",
        "description": f"From {bank['bankName']} ***{bank['lastFour']}",
        "amount": amount, "currency": "USD", "date": now_iso(),
        "status": "completed", "paymentMethod": bank["id"], "category": "Transfer"
    })


def withdraw_money(state, amount, bank_last_four):
    """Withdraw money from USD balance to a bank."""
    usd = find_balance(state, "USD")
    bank = find_bank(state, bank_last_four)
    usd["amount"] = round((usd["amount"] - amount) * 100) / 100
    txn_id = f"txn_{state['_nextTransactionId']:03d}"
    state["_nextTransactionId"] += 1
    state["transactions"].insert(0, {
        "id": txn_id, "type": "transfer_out",
        "description": f"To {bank['bankName']} ***{bank['lastFour']}",
        "amount": -amount, "currency": "USD", "date": now_iso(),
        "status": "completed", "paymentMethod": bank["id"], "category": "Transfer"
    })


def make_credit_payment(state, amount):
    """Make a payment on PayPal Credit."""
    usd = find_balance(state, "USD")
    pc = state["paypalCredit"]
    usd["amount"] = round((usd["amount"] - amount) * 100) / 100
    pc["currentBalance"] = max(0, round((pc["currentBalance"] - amount) * 100) / 100)
    pc["availableCredit"] = round((pc["creditLimit"] - pc["currentBalance"]) * 100) / 100
    pc["lastPaymentAmount"] = amount
    pc["lastPaymentDate"] = now_iso()
    if pc["currentBalance"] <= 0:
        pc["minimumPaymentDue"] = 0


def redeem_rewards(state, points, redeem_type):
    """Redeem reward points."""
    rewards = state["rewards"]
    value = points / 100
    rewards["totalPoints"] -= points
    rewards["pointsValue"] = round(rewards["totalPoints"]) / 100
    rwd_id = f"rwd_{state['_nextRewardId']:03d}"
    state["_nextRewardId"] += 1
    desc = "Redeemed for PayPal Balance" if redeem_type == "balance" else "Redeemed for Gift Card"
    rewards["history"].insert(0, {
        "id": rwd_id, "description": desc, "points": -points,
        "date": now_iso(), "type": "redeemed", "redemptionValue": value
    })
    if redeem_type == "balance":
        usd = find_balance(state, "USD")
        usd["amount"] = round((usd["amount"] + value) * 100) / 100


def purchase_gift_card(state, merchant_name, amount, recipient_email, recipient_name, message):
    """Purchase a gift card."""
    usd = find_balance(state, "USD")
    usd["amount"] = round((usd["amount"] - amount) * 100) / 100
    gc_id = f"gc_{state['_nextGiftCardId']:03d}"
    state["_nextGiftCardId"] += 1
    code = f"{merchant_name[:3].upper()}-TEST-TEST-TEST"
    state["giftCards"].insert(0, {
        "id": gc_id, "merchantName": merchant_name, "amount": amount,
        "remainingBalance": amount, "status": "active",
        "purchasedAt": now_iso(), "recipientEmail": recipient_email,
        "recipientName": recipient_name, "senderName": "Jordan Mitchell",
        "message": message, "redemptionCode": code, "redeemed": False
    })
    txn_id = f"txn_{state['_nextTransactionId']:03d}"
    state["_nextTransactionId"] += 1
    state["transactions"].insert(0, {
        "id": txn_id, "type": "gift_card",
        "description": f"Gift Card - {merchant_name}",
        "amount": -amount, "currency": "USD", "date": now_iso(),
        "status": "completed", "paymentMethod": "balance", "category": "Gift Cards"
    })


# ---------------------------------------------------------------------------
# Solve functions — one per task, derived from verifiers
# ---------------------------------------------------------------------------

# ---- EASY ----

def solve_task_e1(state):
    """Disable cash back on debit card."""
    state["paypalDebitCard"]["cashBackEnabled"] = False


def solve_task_e2(state):
    """Disable weekly digest notification."""
    state["walletPreferences"]["emailNotifications"]["weeklyDigest"] = False


def solve_task_e3(state):
    """Save the DoorDash offer."""
    offer = find_offer(state, "DoorDash")
    offer["status"] = "saved"
    offer["savedAt"] = now_iso()


def solve_task_e4(state):
    """Remove CAD currency (zero balance)."""
    state["balances"] = [b for b in state["balances"] if b["currency"] != "CAD"]


def solve_task_e5(state):
    """Unsave the Uber offer."""
    offer = find_offer(state, "Uber")
    offer["status"] = "available"
    offer["savedAt"] = None


def solve_task_e6(state):
    """Disable auto-accept payments."""
    state["walletPreferences"]["autoAcceptPayments"] = False


def solve_task_e7(state):
    """Enable promotional email notifications."""
    state["walletPreferences"]["emailNotifications"]["promotions"] = True


def solve_task_e8(state):
    """Disable crypto alerts notifications."""
    state["walletPreferences"]["emailNotifications"]["cryptoAlerts"] = False


def solve_task_e9(state):
    """Set currency conversion to card issuer."""
    state["walletPreferences"]["currencyConversionOption"] = "card_issuer"


def solve_task_e10(state):
    """Disable instant transfer preference."""
    state["walletPreferences"]["instantTransferPreference"] = False


def solve_task_e11(state):
    """Disable direct deposit on debit card."""
    state["paypalDebitCard"]["directDeposit"]["enabled"] = False


def solve_task_e12(state):
    """Save the Nike offer."""
    offer = find_offer(state, "Nike")
    offer["status"] = "saved"
    offer["savedAt"] = now_iso()


def solve_task_e13(state):
    """Remove expired Discover card 6221."""
    state["cards"] = [c for c in state["cards"] if c["lastFour"] != "6221"]


def solve_task_e14(state):
    """Unsave the Spotify offer."""
    offer = find_offer(state, "Spotify")
    offer["status"] = "available"
    offer["savedAt"] = None


def solve_task_e15(state):
    """Disable PayPal Credit autopay."""
    state["paypalCredit"]["autopayEnabled"] = False


def solve_task_e16(state):
    """Save the Amazon offer."""
    offer = find_offer(state, "Amazon")
    offer["status"] = "saved"
    offer["savedAt"] = now_iso()


def solve_task_e17(state):
    """Set PayPal Credit autopay to full balance."""
    state["paypalCredit"]["autopayAmount"] = "full"


def solve_task_e18(state):
    """Unsave the Starbucks offer."""
    offer = find_offer(state, "Starbucks")
    offer["status"] = "available"
    offer["savedAt"] = None


def solve_task_e19(state):
    """Disable transfer notifications."""
    state["walletPreferences"]["emailNotifications"]["transfers"] = False


def solve_task_e20(state):
    """Remove Citibank checking 1104."""
    state["bankAccounts"] = [b for b in state["bankAccounts"] if b["lastFour"] != "1104"]


# ---- MEDIUM ----

def solve_task_m1(state):
    """Switch preferred payment to Mastercard 7156."""
    for c in state["cards"]:
        c["isPreferred"] = False
    card = find_card(state, "7156")
    card["isPreferred"] = True
    state["walletPreferences"]["preferredPaymentMethod"] = card["id"]
    state["currentUser"]["preferredPaymentMethodId"] = card["id"]


def solve_task_m2(state):
    """Pay $100 toward PayPal Credit."""
    make_credit_payment(state, 100)


def solve_task_m3(state):
    """Withdraw $300 to Chase checking."""
    withdraw_money(state, 300, "6742")


def solve_task_m4(state):
    """Add $200 from Bank of America."""
    add_money(state, 200, "3891")


def solve_task_m5(state):
    """Deposit $500 to savings."""
    deposit_to_savings(state, 500)


def solve_task_m6(state):
    """Set debit card spending limit to 5000."""
    state["paypalDebitCard"]["dailySpendingLimit"] = 5000


def solve_task_m7(state):
    """Set debit card ATM limit to 200."""
    state["paypalDebitCard"]["dailyATMLimit"] = 200


def solve_task_m8(state):
    """Redeem 500 rewards points for PayPal balance."""
    redeem_rewards(state, 500, "balance")


def solve_task_m9(state):
    """Set Amex 3001 as backup payment."""
    for c in state["cards"]:
        c["isBackup"] = False
    card = find_card(state, "3001")
    card["isBackup"] = True
    state["walletPreferences"]["backupPaymentMethod"] = card["id"]
    state["currentUser"]["backupPaymentMethodId"] = card["id"]


def solve_task_m10(state):
    """Convert $150 USD to GBP."""
    convert_currency(state, "USD", "GBP", 150)


def solve_task_m11(state):
    """Buy $50 of Ethereum."""
    buy_crypto(state, "ETH", 50)


def solve_task_m12(state):
    """Add Mexican Peso currency."""
    state["balances"].append({
        "currency": "MXN", "amount": 0, "isPrimary": False
    })


def solve_task_m13(state):
    """Sell $75 of Litecoin."""
    sell_crypto(state, "LTC", 75)


def solve_task_m14(state):
    """Withdraw $1000 from savings."""
    withdraw_from_savings(state, 1000)


def solve_task_m15(state):
    """Change direct deposit employer to Global Dynamics."""
    state["paypalDebitCard"]["directDeposit"]["employer"] = "Global Dynamics"


def solve_task_m16(state):
    """Pay minimum due on PayPal Credit ($35)."""
    make_credit_payment(state, 35)


def solve_task_m17(state):
    """Set PayPal Credit autopay to statement balance."""
    state["paypalCredit"]["autopayAmount"] = "statement"


def solve_task_m18(state):
    """Set debit card spending limit to 1500."""
    state["paypalDebitCard"]["dailySpendingLimit"] = 1500


def solve_task_m19(state):
    """Redeem 1000 rewards points for gift card."""
    redeem_rewards(state, 1000, "gift_card")


def solve_task_m20(state):
    """Add $750 from Chase checking."""
    add_money(state, 750, "6742")


# ---- HARD ----

def solve_task_h1(state):
    """Convert 200 EUR to JPY."""
    convert_currency(state, "EUR", "JPY", 200)


def solve_task_h2(state):
    """Buy $25 of Solana."""
    buy_crypto(state, "SOL", 25)


def solve_task_h3(state):
    """Purchase $50 Nike gift card for Riley Parker."""
    purchase_gift_card(state, "Nike", 50, "riley.p@email.com", "Riley Parker", "Happy Holidays!")


def solve_task_h4(state):
    """Save all available food & drink offers (DoorDash and Chipotle)."""
    for offer in state["offers"]:
        if offer.get("category") == "Food & Drink" and offer.get("status") == "available":
            offer["status"] = "saved"
            offer["savedAt"] = now_iso()


def solve_task_h5(state):
    """Switch preferred to Amex 3001, backup to Citibank 1104."""
    # Clear preferred
    for c in state["cards"]:
        c["isPreferred"] = False
    card = find_card(state, "3001")
    card["isPreferred"] = True
    state["walletPreferences"]["preferredPaymentMethod"] = card["id"]
    state["currentUser"]["preferredPaymentMethodId"] = card["id"]
    # Clear backup on cards
    for c in state["cards"]:
        c["isBackup"] = False
    # Set bank as backup
    bank = find_bank(state, "1104")
    state["walletPreferences"]["backupPaymentMethod"] = bank["id"]
    state["currentUser"]["backupPaymentMethodId"] = bank["id"]


def solve_task_h6(state):
    """Remove expired Discover 6221 and pending Wells Fargo 5518."""
    state["cards"] = [c for c in state["cards"] if c["lastFour"] != "6221"]
    state["bankAccounts"] = [b for b in state["bankAccounts"] if b["lastFour"] != "5518"]


def solve_task_h7(state):
    """Set PayPal Credit autopay to full and debit card limit to 7000."""
    state["paypalCredit"]["autopayEnabled"] = True
    state["paypalCredit"]["autopayAmount"] = "full"
    state["paypalDebitCard"]["dailySpendingLimit"] = 7000


def solve_task_h8(state):
    """Withdraw $2000 from savings, then withdraw $1000 to Chase."""
    withdraw_from_savings(state, 2000)
    withdraw_money(state, 1000, "6742")


def solve_task_h9(state):
    """Purchase $100 Best Buy gift card for mark.taylor@email.com."""
    purchase_gift_card(state, "Best Buy", 100, "mark.taylor@email.com", "Mark Taylor", "Congrats on the promotion!")


def solve_task_h10(state):
    """Turn off all email notifications except security alerts."""
    notifs = state["walletPreferences"]["emailNotifications"]
    notifs["payments"] = False
    notifs["transfers"] = False
    notifs["securityAlerts"] = True
    notifs["promotions"] = False
    notifs["cryptoAlerts"] = False
    notifs["rewardsUpdates"] = False
    notifs["weeklyDigest"] = False


def solve_task_h11(state):
    """Add CHF and convert $300 into it."""
    state["balances"].append({
        "currency": "CHF", "amount": 0, "isPrimary": False
    })
    convert_currency(state, "USD", "CHF", 300)


def solve_task_h12(state):
    """Deposit $500 to savings and set ATM limit to 1000."""
    deposit_to_savings(state, 500)
    state["paypalDebitCard"]["dailyATMLimit"] = 1000


def solve_task_h13(state):
    """Switch currency conversion to card issuer and make MC 2290 preferred."""
    state["walletPreferences"]["currencyConversionOption"] = "card_issuer"
    for c in state["cards"]:
        c["isPreferred"] = False
    card = find_card(state, "2290")
    card["isPreferred"] = True
    state["walletPreferences"]["preferredPaymentMethod"] = card["id"]
    state["currentUser"]["preferredPaymentMethodId"] = card["id"]


def solve_task_h14(state):
    """Buy $50 BTC and $50 ETH."""
    buy_crypto(state, "BTC", 50)
    buy_crypto(state, "ETH", 50)


def solve_task_h15(state):
    """Save Target, Walmart, and Lyft offers."""
    for name in ["Target", "Walmart", "Lyft"]:
        offer = find_offer(state, name)
        offer["status"] = "saved"
        offer["savedAt"] = now_iso()


def solve_task_h16(state):
    """Remove Citibank 1104 and US Bank 7823."""
    state["bankAccounts"] = [
        b for b in state["bankAccounts"]
        if b["lastFour"] not in ("1104", "7823")
    ]


def solve_task_h17(state):
    """Buy $25 Starbucks gift card for self and redeem 500 rewards for balance."""
    purchase_gift_card(
        state, "Starbucks", 25,
        "jordan.mitchell@outlook.com", "Jordan Mitchell", ""
    )
    redeem_rewards(state, 500, "balance")


def solve_task_h18(state):
    """Add $1000 from Chase, then convert $500 to EUR."""
    add_money(state, 1000, "6742")
    convert_currency(state, "USD", "EUR", 500)


def solve_task_h19(state):
    """Disable cash back, direct deposit, set spending limit to 2000."""
    state["paypalDebitCard"]["cashBackEnabled"] = False
    state["paypalDebitCard"]["directDeposit"]["enabled"] = False
    state["paypalDebitCard"]["dailySpendingLimit"] = 2000


def solve_task_h20(state):
    """Make $200 PayPal Credit payment and set autopay to full."""
    make_credit_payment(state, 200)
    state["paypalCredit"]["autopayAmount"] = "full"


# ---- HARDENING ROUND 1 ----

def solve_task_h21(state):
    """Sell $200 of Chainlink and deposit $200 into savings."""
    sell_crypto(state, "LINK", 200)
    deposit_to_savings(state, 200)


def solve_task_h22(state):
    """Remove all unconfirmed payment methods."""
    state["cards"] = [c for c in state["cards"] if c.get("status") != "pending_confirmation"]
    state["bankAccounts"] = [b for b in state["bankAccounts"] if b.get("status") != "pending_confirmation"]


def solve_task_h23(state):
    """Invest $100 in BTC (highest % return crypto)."""
    buy_crypto(state, "BTC", 100)


def solve_task_h24(state):
    """Save all available Shopping category offers."""
    for offer in state["offers"]:
        if offer.get("category") == "Shopping" and offer.get("status") == "available":
            offer["status"] = "saved"
            offer["savedAt"] = now_iso()


def solve_task_h25(state):
    """Convert all AUD to EUR."""
    aud = find_balance(state, "AUD")
    convert_currency(state, "AUD", "EUR", aud["amount"])


def solve_task_h26(state):
    """Send $50 Amazon gift card and save Amazon offer."""
    purchase_gift_card(state, "Amazon", 50, "sarah.chen@email.com", "Sarah Chen", "Thank you!")
    offer = find_offer(state, "Amazon")
    offer["status"] = "saved"
    offer["savedAt"] = now_iso()


def solve_task_h27(state):
    """Set BofA as backup, MC 2290 as preferred."""
    # Set preferred to MC 2290
    for c in state["cards"]:
        c["isPreferred"] = False
    card = find_card(state, "2290")
    card["isPreferred"] = True
    state["walletPreferences"]["preferredPaymentMethod"] = card["id"]
    state["currentUser"]["preferredPaymentMethodId"] = card["id"]
    # Set backup to BofA
    for c in state["cards"]:
        c["isBackup"] = False
    bank = find_bank(state, "3891")
    state["walletPreferences"]["backupPaymentMethod"] = bank["id"]
    state["currentUser"]["backupPaymentMethodId"] = bank["id"]


def solve_task_h28(state):
    """Withdraw $3000 from savings, buy $100 BTC, buy $100 ETH."""
    withdraw_from_savings(state, 3000)
    buy_crypto(state, "BTC", 100)
    buy_crypto(state, "ETH", 100)


def solve_task_h29(state):
    """Turn off payments & transfers notifications, turn on promotions."""
    state["walletPreferences"]["emailNotifications"]["payments"] = False
    state["walletPreferences"]["emailNotifications"]["transfers"] = False
    state["walletPreferences"]["emailNotifications"]["promotions"] = True


def solve_task_h30(state):
    """Add NOK and convert 100 EUR to NOK."""
    state["balances"].append({"currency": "NOK", "amount": 0, "isPrimary": False})
    convert_currency(state, "EUR", "NOK", 100)


def solve_task_h31(state):
    """Sell $50 of BCH and buy $50 of LTC."""
    sell_crypto(state, "BCH", 50)
    buy_crypto(state, "LTC", 50)


def solve_task_h32(state):
    """Pay off entire PayPal Credit balance, set autopay to full."""
    balance = state["paypalCredit"]["currentBalance"]
    make_credit_payment(state, balance)
    state["paypalCredit"]["autopayAmount"] = "full"
    state["paypalCredit"]["autopayEnabled"] = True


def solve_task_h33(state):
    """Convert all JPY to USD, then remove JPY currency."""
    jpy = find_balance(state, "JPY")
    convert_currency(state, "JPY", "USD", jpy["amount"])
    state["balances"] = [b for b in state["balances"] if b["currency"] != "JPY"]


def solve_task_h34(state):
    """Purchase $25 Starbucks and $50 Nike gift cards for self."""
    user_email = state["currentUser"]["email"]
    user_name = f"{state['currentUser']['firstName']} {state['currentUser']['lastName']}"
    purchase_gift_card(state, "Starbucks", 25, user_email, user_name, "")
    purchase_gift_card(state, "Nike", 50, user_email, user_name, "")


def solve_task_h35(state):
    """Redeem 2000 rewards for balance, then deposit $20 to savings."""
    redeem_rewards(state, 2000, "balance")
    deposit_to_savings(state, 20)


def solve_task_h36(state):
    """Change employer to Apex Industries and ATM limit to 300."""
    state["paypalDebitCard"]["directDeposit"]["employer"] = "Apex Industries"
    state["paypalDebitCard"]["dailyATMLimit"] = 300


def solve_task_h37(state):
    """Save Chipotle offer and buy $25 DoorDash gift card for self."""
    offer = find_offer(state, "Chipotle")
    offer["status"] = "saved"
    offer["savedAt"] = now_iso()
    user_email = state["currentUser"]["email"]
    user_name = f"{state['currentUser']['firstName']} {state['currentUser']['lastName']}"
    purchase_gift_card(state, "DoorDash", 25, user_email, user_name, "")


def solve_task_h38(state):
    """Withdraw $500 to BofA and set spending limit to 4000."""
    withdraw_money(state, 500, "3891")
    state["paypalDebitCard"]["dailySpendingLimit"] = 4000


def solve_task_h39(state):
    """Add INR, convert $100 to INR, set currency conversion to card issuer."""
    state["balances"].append({"currency": "INR", "amount": 0, "isPrimary": False})
    convert_currency(state, "USD", "INR", 100)
    state["walletPreferences"]["currencyConversionOption"] = "card_issuer"


def solve_task_h40(state):
    """Unsave all saved offers, then save Target, Nike, Amazon."""
    for offer in state["offers"]:
        if offer.get("status") == "saved":
            offer["status"] = "available"
            offer["savedAt"] = None
    for name in ["Target", "Nike", "Amazon"]:
        offer = find_offer(state, name)
        offer["status"] = "saved"
        offer["savedAt"] = now_iso()


# ---- HARDENING ROUND 2 ----

def solve_task_h41(state):
    """Sell $50 of best-performing crypto (BTC, 60.22%), deposit $50 to savings."""
    sell_crypto(state, "BTC", 50)
    deposit_to_savings(state, 50)


def solve_task_h42(state):
    """Set preferred payment to only confirmed debit card (MC 7156, card_002)."""
    for c in state["cards"]:
        c["isPreferred"] = False
    card = find_card(state, "7156")
    card["isPreferred"] = True
    state["walletPreferences"]["preferredPaymentMethod"] = card["id"]
    state["currentUser"]["preferredPaymentMethodId"] = card["id"]


def solve_task_h43(state):
    """Deposit partially-used gift card balance ($12.50 Starbucks) into savings."""
    deposit_to_savings(state, 12.50)


def solve_task_h44(state):
    """Save all available offers with percentage-based cashback >= 10%."""
    for offer in state["offers"]:
        if (offer.get("status") == "available"
                and offer.get("cashbackType") == "percent"
                and offer.get("cashbackPercent", 0) >= 10):
            offer["status"] = "saved"
            offer["savedAt"] = now_iso()


def solve_task_h45(state):
    """Withdraw credit minimum ($35) from savings, pay the minimum."""
    withdraw_from_savings(state, 35)
    make_credit_payment(state, 35)


def solve_task_h46(state):
    """Remove unconfirmed checking account (Wells Fargo 5518)."""
    state["bankAccounts"] = [
        b for b in state["bankAccounts"]
        if not (b.get("lastFour") == "5518" and b.get("status") == "pending_confirmation")
    ]


def solve_task_h47(state):
    """Withdraw $1000 from savings, convert $500 to EUR, buy $500 BTC."""
    withdraw_from_savings(state, 1000)
    convert_currency(state, "USD", "EUR", 500)
    buy_crypto(state, "BTC", 500)


def solve_task_h48(state):
    """Sell $100 worst crypto (PYUSD, 0%), buy $100 best (BTC, 60.22%)."""
    sell_crypto(state, "PYUSD", 100)
    buy_crypto(state, "BTC", 100)


def solve_task_h49(state):
    """Send $50 Nike gift card to jamie@email.com, save DoorDash offer."""
    purchase_gift_card(state, "Nike", 50, "jamie@email.com", "Jamie", "Great job!")
    offer = find_offer(state, "DoorDash")
    offer["status"] = "saved"
    offer["savedAt"] = now_iso()


def solve_task_h50(state):
    """Add SEK, convert $200 to SEK, deposit $200 to savings."""
    state["balances"].append({"currency": "SEK", "amount": 0, "isPrimary": False})
    convert_currency(state, "USD", "SEK", 200)
    deposit_to_savings(state, 200)


def solve_task_h51(state):
    """Pay half of credit balance rounded down ($622)."""
    import math
    half = math.floor(state["paypalCredit"]["currentBalance"] / 2)
    make_credit_payment(state, half)


def solve_task_h52(state):
    """Buy $25 gift card from merchant with highest active gift card balance (Home Depot $75)."""
    user_email = state["currentUser"]["email"]
    user_name = f"{state['currentUser']['firstName']} {state['currentUser']['lastName']}"
    purchase_gift_card(state, "Home Depot", 25, user_email, user_name, "")


def solve_task_h53(state):
    """Keep payments, transfers, security alerts on; turn off rest."""
    notifs = state["walletPreferences"]["emailNotifications"]
    notifs["payments"] = True
    notifs["transfers"] = True
    notifs["securityAlerts"] = True
    notifs["promotions"] = False
    notifs["cryptoAlerts"] = False
    notifs["rewardsUpdates"] = False
    notifs["weeklyDigest"] = False


def solve_task_h54(state):
    """Redeem 2000 rewards for balance, buy $10 Solana."""
    redeem_rewards(state, 2000, "balance")
    buy_crypto(state, "SOL", 10)


def solve_task_h55(state):
    """Remove credit cards not set as preferred or backup."""
    state["cards"] = [
        c for c in state["cards"]
        if c.get("type") != "credit" or c.get("isPreferred") or c.get("isBackup")
    ]


def solve_task_h56(state):
    """Add HKD, convert $250 to HKD, set ATM limit to 200."""
    state["balances"].append({"currency": "HKD", "amount": 0, "isPrimary": False})
    convert_currency(state, "USD", "HKD", 250)
    state["paypalDebitCard"]["dailyATMLimit"] = 200


def solve_task_h57(state):
    """Buy $25 DoorDash gift card for self, sell $25 LTC."""
    user_email = state["currentUser"]["email"]
    user_name = f"{state['currentUser']['firstName']} {state['currentUser']['lastName']}"
    purchase_gift_card(state, "DoorDash", 25, user_email, user_name, "")
    sell_crypto(state, "LTC", 25)


def solve_task_h58(state):
    """Redeem 10% of rewards earned this year (2150 * 0.1 = 215) for balance."""
    earned_this_year = state["rewards"]["earnedThisYear"]
    points_to_redeem = int(earned_this_year * 0.1)
    redeem_rewards(state, points_to_redeem, "balance")


def solve_task_h59(state):
    """Sell $100 ETH, sell $100 BTC, pay $200 on credit."""
    sell_crypto(state, "ETH", 100)
    sell_crypto(state, "BTC", 100)
    make_credit_payment(state, 200)


def solve_task_h60(state):
    """Change cashback category to Groceries, buy $25 Uber gift card for self."""
    state["paypalDebitCard"]["cashBackCategory"] = "Groceries"
    user_email = state["currentUser"]["email"]
    user_name = f"{state['currentUser']['firstName']} {state['currentUser']['lastName']}"
    purchase_gift_card(state, "Uber", 25, user_email, user_name, "")


# ---- HARDENING ROUND 3 ----

def solve_task_h61(state):
    """Sell all Chainlink holdings (~$234.38), deposit $200 into savings."""
    link = find_crypto(state, "LINK")
    sell_amount = round(link["quantity"] * link["currentPrice"] * 100) / 100
    sell_crypto(state, "LINK", sell_amount)
    deposit_to_savings(state, 200)


def solve_task_h62(state):
    """Set most recently added confirmed credit card (MC 2290) as preferred,
    remove oldest credit card (Visa 4829)."""
    # Set MC 2290 as preferred
    for c in state["cards"]:
        c["isPreferred"] = False
    card = find_card(state, "2290")
    card["isPreferred"] = True
    state["walletPreferences"]["preferredPaymentMethod"] = card["id"]
    state["currentUser"]["preferredPaymentMethodId"] = card["id"]
    # Remove oldest credit card (Visa 4829)
    state["cards"] = [c for c in state["cards"] if c["lastFour"] != "4829"]


def solve_task_h63(state):
    """Save every available offer with maxCashback >= $15."""
    for offer in state["offers"]:
        if offer.get("status") == "available" and offer.get("maxCashback", 0) >= 15:
            offer["status"] = "saved"
            offer["savedAt"] = now_iso()


def solve_task_h64(state):
    """Convert Nike Pay in 4 next payment ($47.25) from USD to GBP."""
    # Nike has 3 remaining payments (most). Next payment: $47.25.
    convert_currency(state, "USD", "GBP", 47.25)


def solve_task_h65(state):
    """Remove savings-type bank accounts, withdraw $500 from PayPal Savings."""
    state["bankAccounts"] = [
        b for b in state["bankAccounts"]
        if b.get("accountType") != "savings"
    ]
    withdraw_from_savings(state, 500)


def solve_task_h66(state):
    """Set confirmed card expiring soonest (AmEx 3001, 12/2026) as backup."""
    for c in state["cards"]:
        c["isBackup"] = False
    card = find_card(state, "3001")
    card["isBackup"] = True
    state["walletPreferences"]["backupPaymentMethod"] = card["id"]
    state["currentUser"]["backupPaymentMethodId"] = card["id"]


def solve_task_h67(state):
    """Redeem savings interest this month ($43.62 = 4362 points) as PayPal Balance."""
    interest = state["savingsAccount"]["interestEarnedThisMonth"]
    points = int(round(interest * 100))
    redeem_rewards(state, points, "balance")


def solve_task_h68(state):
    """Convert all AUD to USD, remove AUD, buy $100 ETH."""
    aud = find_balance(state, "AUD")
    convert_currency(state, "AUD", "USD", aud["amount"])
    state["balances"] = [b for b in state["balances"] if b["currency"] != "AUD"]
    buy_crypto(state, "ETH", 100)


def solve_task_h69(state):
    """Buy $100 Apple gift card for self, set cashback to Fuel, spending limit to 5000."""
    user_email = state["currentUser"]["email"]
    user_name = f"{state['currentUser']['firstName']} {state['currentUser']['lastName']}"
    purchase_gift_card(state, "Apple", 100, user_email, user_name, "")
    state["paypalDebitCard"]["cashBackCategory"] = "Fuel"
    state["paypalDebitCard"]["dailySpendingLimit"] = 5000


def solve_task_h70(state):
    """Pay $500 on credit (balance > $1000), then disable autopay."""
    make_credit_payment(state, 500)
    state["paypalCredit"]["autopayEnabled"] = False


def solve_task_h71(state):
    """Deposit total gift card remaining balance ($167.50) into savings."""
    total = sum(gc.get("remainingBalance", 0) for gc in state["giftCards"])
    deposit_to_savings(state, total)


def solve_task_h72(state):
    """Buy $75 ETH (2nd-highest return), sell $75 BCH (lowest positive return)."""
    buy_crypto(state, "ETH", 75)
    sell_crypto(state, "BCH", 75)


def solve_task_h73(state):
    """Add PLN, convert $200 to PLN, deposit $300 to savings, ATM limit $500."""
    state["balances"].append({"currency": "PLN", "amount": 0, "isPrimary": False})
    convert_currency(state, "USD", "PLN", 200)
    deposit_to_savings(state, 300)
    state["paypalDebitCard"]["dailyATMLimit"] = 500


def solve_task_h74(state):
    """Buy $30 Netflix gift card for self (matches most recently purchased active gc)."""
    user_email = state["currentUser"]["email"]
    user_name = f"{state['currentUser']['firstName']} {state['currentUser']['lastName']}"
    purchase_gift_card(state, "Netflix", 30, user_email, user_name, "")


def solve_task_h75(state):
    """Withdraw $1500 from savings, add $500 from Chase, convert $1000 to EUR, buy $100 Best Buy gc."""
    withdraw_from_savings(state, 1500)
    add_money(state, 500, "6742")
    convert_currency(state, "USD", "EUR", 1000)
    user_email = state["currentUser"]["email"]
    user_name = f"{state['currentUser']['firstName']} {state['currentUser']['lastName']}"
    purchase_gift_card(state, "Best Buy", 100, user_email, user_name, "")


def solve_task_h76(state):
    """Remove least recently used confirmed bank account (US Bank 7823)."""
    state["bankAccounts"] = [b for b in state["bankAccounts"] if b["lastFour"] != "7823"]


def solve_task_h77(state):
    """Flip all email notifications, but keep security alerts always on."""
    notifs = state["walletPreferences"]["emailNotifications"]
    for key in list(notifs.keys()):
        if key == "securityAlerts":
            notifs[key] = True
        else:
            notifs[key] = not notifs[key]


def solve_task_h78(state):
    """Buy $50 Starbucks gc for self (2 active plans × $25)."""
    user_email = state["currentUser"]["email"]
    user_name = f"{state['currentUser']['firstName']} {state['currentUser']['lastName']}"
    purchase_gift_card(state, "Starbucks", 50, user_email, user_name, "")


def solve_task_h79(state):
    """Sell $150 BTC, pay $100 on credit, deposit $50 into savings."""
    sell_crypto(state, "BTC", 150)
    make_credit_payment(state, 100)
    deposit_to_savings(state, 50)


def solve_task_h80(state):
    """Save all available Food & Drink offers, buy $25 DoorDash gc, set card issuer conversion."""
    for offer in state["offers"]:
        if offer.get("category") == "Food & Drink" and offer.get("status") == "available":
            offer["status"] = "saved"
            offer["savedAt"] = now_iso()
    user_email = state["currentUser"]["email"]
    user_name = f"{state['currentUser']['firstName']} {state['currentUser']['lastName']}"
    purchase_gift_card(state, "DoorDash", 25, user_email, user_name, "")
    state["walletPreferences"]["currencyConversionOption"] = "card_issuer"


# ---- HARDENING ROUND 4 ----

def solve_task_h81(state):
    """Withdraw Nike plan remaining ($141.75) from savings, convert $70 to EUR."""
    # Nike plan has 3 unpaid payments at $47.25 each = $141.75
    withdraw_from_savings(state, 141.75)
    convert_currency(state, "USD", "EUR", 70)


def solve_task_h82(state):
    """Switch autopay to full (seed is minimum), pay $250 on credit."""
    state["paypalCredit"]["autopayAmount"] = "full"
    make_credit_payment(state, 250)


def solve_task_h83(state):
    """Remove expired/pending cards, set earliest-last-used remaining card as preferred."""
    # Remove expired (Discover 6221) and pending (Visa 8834)
    state["cards"] = [
        c for c in state["cards"]
        if c.get("status") not in ("expired", "pending_confirmation")
    ]
    # Earliest last used among remaining: AmEx 3001 (2026-01-15)
    for c in state["cards"]:
        c["isPreferred"] = False
    card = find_card(state, "3001")
    card["isPreferred"] = True
    state["walletPreferences"]["preferredPaymentMethod"] = card["id"]
    state["currentUser"]["preferredPaymentMethodId"] = card["id"]


def solve_task_h84(state):
    """Buy $10 of Solana (matches largest historical redemption of $10)."""
    # Largest redemption: rwd_008 = 1000 pts = $10.00
    buy_crypto(state, "SOL", 10)


def solve_task_h85(state):
    """Remove Citibank 1104 (most recently added confirmed instant-transfer bank)."""
    state["bankAccounts"] = [b for b in state["bankAccounts"] if b["lastFour"] != "1104"]


def solve_task_h86(state):
    """Deposit $359 (5% of positive-return crypto value) into savings."""
    # Positive return: BTC $3066.89 + ETH $3018.47 + LTC $515.28 + BCH $343.97 + LINK $234.38
    # Total = $7178.99, 5% = $358.95, rounded = $359
    deposit_to_savings(state, 359)


def solve_task_h87(state):
    """Redeem 1250 points ($12.50) for balance, deposit $12.50 to savings."""
    # Smallest non-zero gift card balance: Starbucks gc_002 = $12.50
    redeem_rewards(state, 1250, "balance")
    deposit_to_savings(state, 12.50)


def solve_task_h88(state):
    """Sell all PYUSD, pay $200 on credit, set ATM limit to $600."""
    pyusd = find_crypto(state, "PYUSD")
    sell_amount = round(pyusd["quantity"] * pyusd["currentPrice"] * 100) / 100
    sell_crypto(state, "PYUSD", sell_amount)
    make_credit_payment(state, 200)
    state["paypalDebitCard"]["dailyATMLimit"] = 600


def solve_task_h89(state):
    """Convert $500 to JPY (balance > $2500), set cashback to Fuel."""
    # USD = $2847.63 > $2500, so convert directly
    convert_currency(state, "USD", "JPY", 500)
    state["paypalDebitCard"]["cashBackCategory"] = "Fuel"


def solve_task_h90(state):
    """Save available offers with maxCashback >= $15, unsave saved fixed-type offers."""
    # Step 1: Save available offers with maxCashback >= 15
    for offer in state["offers"]:
        if offer.get("status") == "available" and offer.get("maxCashback", 0) >= 15:
            offer["status"] = "saved"
            offer["savedAt"] = now_iso()
    # Step 2: Unsave saved offers with fixed cashback type
    for offer in state["offers"]:
        if offer.get("status") == "saved" and offer.get("cashbackType") == "fixed":
            offer["status"] = "available"
            offer["savedAt"] = None


def solve_task_h91(state):
    """Convert $283.99 (total remaining Pay in 4 payments) to GBP."""
    # Nordstrom: $71.12 + $71.12 = $142.24
    # Nike: $47.25 * 3 = $141.75
    # Total = $283.99
    convert_currency(state, "USD", "GBP", 283.99)


def solve_task_h92(state):
    """Withdraw $2000 from savings, buy $500 BTC, buy $500 ETH, pay $500 credit."""
    withdraw_from_savings(state, 2000)
    buy_crypto(state, "BTC", 500)
    buy_crypto(state, "ETH", 500)
    make_credit_payment(state, 500)


def solve_task_h93(state):
    """Remove savings-type banks, set Citibank 1104 (lowest last four checking) as backup."""
    state["bankAccounts"] = [
        b for b in state["bankAccounts"]
        if b.get("accountType") != "savings"
    ]
    # Set Citibank 1104 as backup
    for c in state["cards"]:
        c["isBackup"] = False
    bank = find_bank(state, "1104")
    state["walletPreferences"]["backupPaymentMethod"] = bank["id"]
    state["currentUser"]["backupPaymentMethodId"] = bank["id"]


def solve_task_h94(state):
    """Sell $200 ETH (highest total cost), convert $100 to EUR, deposit $100 to savings."""
    sell_crypto(state, "ETH", 200)
    convert_currency(state, "USD", "EUR", 100)
    deposit_to_savings(state, 100)


def solve_task_h95(state):
    """Enable only security+crypto alerts, disable rest. Cashback Apparel, limit $4000."""
    notifs = state["walletPreferences"]["emailNotifications"]
    notifs["payments"] = False
    notifs["transfers"] = False
    notifs["securityAlerts"] = True
    notifs["promotions"] = False
    notifs["cryptoAlerts"] = True
    notifs["rewardsUpdates"] = False
    notifs["weeklyDigest"] = False
    state["paypalDebitCard"]["cashBackCategory"] = "Apparel"
    state["paypalDebitCard"]["dailySpendingLimit"] = 4000


def solve_task_h96(state):
    """Send $50 Target gift card to Marcus Williams (matches highest-amount gc)."""
    purchase_gift_card(
        state, "Target", 50,
        "marcus.williams@email.com", "Marcus Williams", "Another one for you!"
    )


def solve_task_h97(state):
    """Add CHF, convert $400, set card issuer, set AmEx preferred, disable weekly digest."""
    state["balances"].append({"currency": "CHF", "amount": 0, "isPrimary": False})
    convert_currency(state, "USD", "CHF", 400)
    state["walletPreferences"]["currencyConversionOption"] = "card_issuer"
    for c in state["cards"]:
        c["isPreferred"] = False
    card = find_card(state, "3001")
    card["isPreferred"] = True
    state["walletPreferences"]["preferredPaymentMethod"] = card["id"]
    state["currentUser"]["preferredPaymentMethodId"] = card["id"]
    state["walletPreferences"]["emailNotifications"]["weeklyDigest"] = False


def solve_task_h98(state):
    """Pay $311 (25% of credit balance rounded) and redeem 1000 rewards for balance."""
    import math
    payment = round(state["paypalCredit"]["currentBalance"] * 0.25)
    make_credit_payment(state, payment)
    redeem_rewards(state, 1000, "balance")


def solve_task_h99(state):
    """Remove non-instant-transfer banks, add $100 from each remaining confirmed checking."""
    state["bankAccounts"] = [
        b for b in state["bankAccounts"]
        if b.get("instantTransferEligible")
    ]
    # Remaining confirmed checking: Chase 6742, Citibank 1104
    # (Wells Fargo 5518 is pending, not confirmed)
    add_money(state, 100, "6742")
    add_money(state, 100, "1104")


def solve_task_h100(state):
    """Sell $300 BTC (portfolio > $7000), set spending limit to $2500."""
    # Crypto total: $7428.99 > $7000
    sell_crypto(state, "BTC", 300)
    state["paypalDebitCard"]["dailySpendingLimit"] = 2500


# ---------------------------------------------------------------------------
# Solver registry
# ---------------------------------------------------------------------------

SOLVERS = {}
for _prefix in ("e", "m", "h"):
    for _i in range(1, 101):
        _task_id = f"task_{_prefix}{_i}"
        _fn_name = f"solve_{_task_id}"
        if _fn_name in globals():
            SOLVERS[_task_id] = globals()[_fn_name]

# ---------------------------------------------------------------------------
# Task loading and verification
# ---------------------------------------------------------------------------


def load_tasks():
    with open(TASKS_FILE) as f:
        return json.load(f)


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
    parser = argparse.ArgumentParser(description="PayPal My Wallet real-task sanity check")
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
