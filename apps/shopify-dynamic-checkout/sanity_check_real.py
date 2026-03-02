#!/usr/bin/env python3
"""
Sanity check for Shopify Dynamic Checkout real tasks.

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

const state = {
    currentUser: JSON.parse(JSON.stringify(CURRENT_USER)),
    themes: JSON.parse(JSON.stringify(THEMES)),
    templates: JSON.parse(JSON.stringify(TEMPLATES)),
    themePages: JSON.parse(JSON.stringify(THEME_PAGES)),
    themeSections: JSON.parse(JSON.stringify(THEME_SECTIONS)),
    paymentMethods: JSON.parse(JSON.stringify(PAYMENT_METHODS)),
    shopPromise: JSON.parse(JSON.stringify(SHOP_PROMISE)),
    products: JSON.parse(JSON.stringify(PRODUCTS)),
    collections: JSON.parse(JSON.stringify(COLLECTIONS)),
    installedApps: JSON.parse(JSON.stringify(INSTALLED_APPS)),
    cartAttributes: JSON.parse(JSON.stringify(CART_ATTRIBUTES)),
    activityLog: JSON.parse(JSON.stringify(ACTIVITY_LOG)),
    availableFonts: JSON.parse(JSON.stringify(AVAILABLE_FONTS)),
    _nextThemeId: INITIAL_NEXT_IDS._nextThemeId,
    _nextTemplateId: INITIAL_NEXT_IDS._nextTemplateId,
    _nextSectionId: INITIAL_NEXT_IDS._nextSectionId,
    _nextProductId: INITIAL_NEXT_IDS._nextProductId,
    _nextAppId: INITIAL_NEXT_IDS._nextAppId,
    _nextLogId: INITIAL_NEXT_IDS._nextLogId,
    _nextCartAttrId: INITIAL_NEXT_IDS._nextCartAttrId,
    _nextCollectionId: INITIAL_NEXT_IDS._nextCollectionId,
    _seedVersion: SEED_DATA_VERSION
};
process.stdout.write(JSON.stringify(state));
"""


# ---- Helpers ----

def find_entity(entities, **kwargs):
    """Find an entity by attribute match. Raises if not found."""
    for e in entities:
        if all(e.get(k) == v for k, v in kwargs.items()):
            return e
    raise ValueError(f"Entity not found: {kwargs}")


def find_theme(state, name):
    return find_entity(state["themes"], name=name)


def find_template(state, theme_name, template_name):
    theme = find_theme(state, theme_name)
    return find_entity(state["templates"], themeId=theme["id"], name=template_name)


def find_default_template(state, theme_name):
    theme = find_theme(state, theme_name)
    return find_entity(state["templates"], themeId=theme["id"], isDefault=True)


def find_product(state, title):
    """Find product by title (supports partial match for em dashes)."""
    for p in state["products"]:
        if p["title"] == title or title in p.get("title", ""):
            return p
    raise ValueError(f"Product not found: {title!r}")


def find_payment_method(state, name):
    return find_entity(state["paymentMethods"], name=name)


def find_app(state, name):
    """Find app by name (supports partial match)."""
    for a in state["installedApps"]:
        if a["name"] == name or name in a.get("name", ""):
            return a
    raise ValueError(f"App not found: {name!r}")


def find_cart_attr(state, name):
    return find_entity(state["cartAttributes"], name=name)


def find_section(state, theme_name, page_type, section_type):
    theme = find_theme(state, theme_name)
    page = find_entity(state["themePages"], themeId=theme["id"], type=page_type)
    return find_entity(state["themeSections"], pageId=page["id"], type=section_type)


# ---- Solve Functions (Easy) ----

def solve_task_e1(state):
    """Switch the store's live theme to Craft."""
    for t in state["themes"]:
        if t["role"] == "main":
            t["role"] = "unpublished"
    find_theme(state, "Craft")["role"] = "main"


def solve_task_e2(state):
    """Turn off accelerated checkout on Dawn's default product template."""
    find_template(state, "Dawn", "Default product")["showAcceleratedCheckout"] = False


def solve_task_e3(state):
    """Enable Amazon Pay."""
    find_payment_method(state, "Amazon Pay")["isActive"] = True


def solve_task_e4(state):
    """Turn off gift wrapping."""
    find_cart_attr(state, "Gift wrapping")["isActive"] = False


def solve_task_e5(state):
    """Disable Currency Converter Plus."""
    find_app(state, "Currency Converter Plus")["isActive"] = False


def solve_task_e6(state):
    """Remove quantity selector from default product template."""
    find_template(state, "Dawn", "Default product")["showQuantitySelector"] = False


def solve_task_e7(state):
    """Bring Heavyweight Hoodie back from archived."""
    find_product(state, "Heavyweight Hoodie")["status"] = "active"


def solve_task_e8(state):
    """Disable the delivery date picker."""
    find_cart_attr(state, "Delivery date")["isActive"] = False


def solve_task_e9(state):
    """Turn on Shop Promise."""
    state["shopPromise"]["isActive"] = True


def solve_task_e10(state):
    """Mark Cashmere Beanie as active."""
    find_product(state, "Cashmere Beanie")["status"] = "active"


def solve_task_e11(state):
    """Turn off Google Pay."""
    find_payment_method(state, "Google Pay")["isActive"] = False


def solve_task_e12(state):
    """Enable terms and conditions."""
    find_cart_attr(state, "Terms and conditions")["isActive"] = True


def solve_task_e13(state):
    """Disable Oberlo Dropshipping."""
    find_app(state, "Oberlo Dropshipping")["isActive"] = False


def solve_task_e14(state):
    """Turn off accelerated checkout on home page's featured product."""
    sec = find_section(state, "Dawn", "home", "featured_product")
    sec["showAcceleratedCheckout"] = False


def solve_task_e15(state):
    """Archive Hand-Poured Soy Candle Set."""
    find_product(state, "Hand-Poured Soy Candle Set")["status"] = "archived"


def solve_task_e16(state):
    """Enable Venmo."""
    find_payment_method(state, "Venmo")["isActive"] = True


def solve_task_e17(state):
    """Put Classic Cotton T-Shirt in draft."""
    find_product(state, "Classic Cotton T-Shirt")["status"] = "draft"


def solve_task_e18(state):
    """Deactivate Apple Pay."""
    find_payment_method(state, "Apple Pay")["isActive"] = False


def solve_task_e19(state):
    """Turn on accelerated checkout for Craft default template."""
    find_template(state, "Craft", "Default product")["showAcceleratedCheckout"] = True


def solve_task_e20(state):
    """Activate CartHook Post Purchase Offers."""
    find_app(state, "CartHook")["isActive"] = True


# ---- Solve Functions (Medium) ----

def solve_task_m1(state):
    """Update Dawn heading to Playfair Display, body to Source Sans Pro."""
    typo = find_theme(state, "Dawn")["settings"]["typography"]
    typo["headingFont"] = "Playfair Display"
    typo["bodyFont"] = "Source Sans Pro"


def solve_task_m2(state):
    """Move Leather Crossbody Bag to default product template."""
    tmpl = find_default_template(state, "Dawn")
    find_product(state, "Leather Crossbody Bag")["templateId"] = tmpl["id"]


def solve_task_m3(state):
    """Create alternate template 'Product - Seasonal' on Dawn."""
    theme = find_theme(state, "Dawn")
    tmpl_id = "tmpl_" + str(state["_nextTemplateId"])
    state["_nextTemplateId"] += 1
    state["templates"].append({
        "id": tmpl_id,
        "themeId": theme["id"],
        "name": "Product - Seasonal",
        "handle": "product.product---seasonal",
        "isDefault": False,
        "isAlternate": True,
        "showAcceleratedCheckout": False,
        "showQuantitySelector": True,
        "buyButtonText": "Add to cart",
        "createdAt": "2026-03-02T12:00:00Z"
    })


def solve_task_m4(state):
    """Set Dawn checkout button colors to blue/white."""
    colors = find_theme(state, "Dawn")["settings"]["colors"]
    colors["accentButtonBg"] = "#2563EB"
    colors["accentButtonText"] = "#FFFFFF"


def solve_task_m5(state):
    """Turn off checkout on both Craft templates."""
    find_template(state, "Craft", "Default product")["showAcceleratedCheckout"] = False
    find_template(state, "Craft", "Product - Featured")["showAcceleratedCheckout"] = False


def solve_task_m6(state):
    """Disable all conflicting cart attributes."""
    find_cart_attr(state, "Gift wrapping")["isActive"] = False
    find_cart_attr(state, "Delivery date")["isActive"] = False


def solve_task_m7(state):
    """Deactivate all apps with checkout conflicts."""
    find_app(state, "Currency Converter Plus")["isActive"] = False
    find_app(state, "Oberlo Dropshipping")["isActive"] = False
    find_app(state, "ReConvert Upsell & Cross Sell")["isActive"] = False


def solve_task_m8(state):
    """Update Dawn primary bg to #F0F0F0 and text to #333333."""
    colors = find_theme(state, "Dawn")["settings"]["colors"]
    colors["primaryBg"] = "#F0F0F0"
    colors["primaryText"] = "#333333"


def solve_task_m9(state):
    """Delete 'Product - Gift cards' template from Dawn."""
    tmpl = find_template(state, "Dawn", "Product - Gift cards")
    default_tmpl = find_default_template(state, "Dawn")
    for p in state["products"]:
        if p["templateId"] == tmpl["id"]:
            p["templateId"] = default_tmpl["id"]
    state["templates"] = [t for t in state["templates"] if t["id"] != tmpl["id"]]


def solve_task_m10(state):
    """Set home page featured product to Titanium Watch."""
    sec = find_section(state, "Dawn", "home", "featured_product")
    product = find_product(state, "Titanium Watch")
    sec["productId"] = product["id"]


def solve_task_m11(state):
    """Publish Sense theme and change body font to Roboto."""
    for t in state["themes"]:
        if t["role"] == "main":
            t["role"] = "unpublished"
    find_theme(state, "Sense")["role"] = "main"
    find_theme(state, "Sense")["settings"]["typography"]["bodyFont"] = "Roboto"


def solve_task_m12(state):
    """Archive Merino Wool Sweater, activate Heavyweight Hoodie."""
    find_product(state, "Merino Wool Sweater")["status"] = "archived"
    find_product(state, "Heavyweight Hoodie")["status"] = "active"


def solve_task_m13(state):
    """Disable ReConvert, enable Privy."""
    find_app(state, "ReConvert Upsell & Cross Sell")["isActive"] = False
    find_app(state, "Privy Pop Ups & Email")["isActive"] = True


def solve_task_m14(state):
    """Move Waxed Canvas Backpack and Silk Blend Scarf to Dawn default template."""
    tmpl = find_default_template(state, "Dawn")
    find_product(state, "Waxed Canvas Backpack")["templateId"] = tmpl["id"]
    find_product(state, "Silk Blend Scarf")["templateId"] = tmpl["id"]


def solve_task_m15(state):
    """Update Dawn secondary colors."""
    colors = find_theme(state, "Dawn")["settings"]["colors"]
    colors["secondaryBg"] = "#E5E7EB"
    colors["secondaryText"] = "#374151"


def solve_task_m16(state):
    """Create alternate template 'Product - Express' on Craft."""
    theme = find_theme(state, "Craft")
    tmpl_id = "tmpl_" + str(state["_nextTemplateId"])
    state["_nextTemplateId"] += 1
    state["templates"].append({
        "id": tmpl_id,
        "themeId": theme["id"],
        "name": "Product - Express",
        "handle": "product.product---express",
        "isDefault": False,
        "isAlternate": True,
        "showAcceleratedCheckout": False,
        "showQuantitySelector": True,
        "buyButtonText": "Add to cart",
        "createdAt": "2026-03-02T12:00:00Z"
    })


def solve_task_m17(state):
    """Switch all three Dawn fonts to Inter."""
    typo = find_theme(state, "Dawn")["settings"]["typography"]
    typo["headingFont"] = "Inter"
    typo["bodyFont"] = "Inter"
    typo["buttonFont"] = "Inter"


def solve_task_m18(state):
    """Turn off PayPal and Google Pay."""
    find_payment_method(state, "PayPal")["isActive"] = False
    find_payment_method(state, "Google Pay")["isActive"] = False


def solve_task_m19(state):
    """Enable terms and conditions, disable gift wrapping."""
    find_cart_attr(state, "Terms and conditions")["isActive"] = True
    find_cart_attr(state, "Gift wrapping")["isActive"] = False


def solve_task_m20(state):
    """Change buy button text on Dawn default template to 'Buy now'."""
    find_template(state, "Dawn", "Default product")["buyButtonText"] = "Buy now"


# ---- Solve Functions (Hard) ----

def solve_task_h1(state):
    """Publish Craft, enable checkout on default, set button bg to Dawn accent."""
    for t in state["themes"]:
        if t["role"] == "main":
            t["role"] = "unpublished"
    find_theme(state, "Craft")["role"] = "main"
    find_template(state, "Craft", "Default product")["showAcceleratedCheckout"] = True
    find_theme(state, "Craft")["settings"]["colors"]["accentButtonBg"] = "#4F46E5"


def solve_task_h2(state):
    """Remove 'No checkout buttons' template from Dawn."""
    tmpl = find_template(state, "Dawn", "Product - No checkout buttons")
    default_tmpl = find_default_template(state, "Dawn")
    for p in state["products"]:
        if p["templateId"] == tmpl["id"]:
            p["templateId"] = default_tmpl["id"]
    state["templates"] = [t for t in state["templates"] if t["id"] != tmpl["id"]]


def solve_task_h3(state):
    """Deactivate conflicting apps + cart attrs, enable Shop Promise."""
    find_app(state, "Currency Converter Plus")["isActive"] = False
    find_app(state, "Oberlo Dropshipping")["isActive"] = False
    find_app(state, "ReConvert Upsell & Cross Sell")["isActive"] = False
    find_cart_attr(state, "Gift wrapping")["isActive"] = False
    find_cart_attr(state, "Delivery date")["isActive"] = False
    state["shopPromise"]["isActive"] = True


def solve_task_h4(state):
    """Create 'Product - Premium' on Dawn with checkout, assign Atelier Goods products."""
    theme = find_theme(state, "Dawn")
    tmpl_id = "tmpl_" + str(state["_nextTemplateId"])
    state["_nextTemplateId"] += 1
    state["templates"].append({
        "id": tmpl_id,
        "themeId": theme["id"],
        "name": "Product - Premium",
        "handle": "product.product---premium",
        "isDefault": False,
        "isAlternate": True,
        "showAcceleratedCheckout": True,
        "showQuantitySelector": True,
        "buyButtonText": "Add to cart",
        "createdAt": "2026-03-02T12:00:00Z"
    })
    for name in ["Leather Crossbody Bag", "Silk Blend Scarf", "Cashmere Beanie", "Waxed Canvas Backpack"]:
        find_product(state, name)["templateId"] = tmpl_id


def solve_task_h5(state):
    """Update Dawn fonts to match Craft, heading scale 110%."""
    typo = find_theme(state, "Dawn")["settings"]["typography"]
    typo["headingFont"] = "Playfair Display"
    typo["bodyFont"] = "Source Sans Pro"
    typo["headingScale"] = 110


def solve_task_h6(state):
    """Disable checkout on all Dawn templates, deactivate all accelerated methods."""
    dawn = find_theme(state, "Dawn")
    for t in state["templates"]:
        if t["themeId"] == dawn["id"]:
            t["showAcceleratedCheckout"] = False
    for name in ["Shop Pay", "Apple Pay", "Google Pay", "PayPal"]:
        find_payment_method(state, name)["isActive"] = False


def solve_task_h7(state):
    """Activate Amazon Pay + Venmo, create Quick Buy template, assign Canvas Sneakers."""
    find_payment_method(state, "Amazon Pay")["isActive"] = True
    find_payment_method(state, "Venmo")["isActive"] = True
    theme = find_theme(state, "Dawn")
    tmpl_id = "tmpl_" + str(state["_nextTemplateId"])
    state["_nextTemplateId"] += 1
    state["templates"].append({
        "id": tmpl_id,
        "themeId": theme["id"],
        "name": "Product - Quick Buy",
        "handle": "product.product---quick-buy",
        "isDefault": False,
        "isAlternate": True,
        "showAcceleratedCheckout": True,
        "showQuantitySelector": True,
        "buyButtonText": "Add to cart",
        "createdAt": "2026-03-02T12:00:00Z"
    })
    find_product(state, "Canvas Sneakers")["templateId"] = tmpl_id


def solve_task_h8(state):
    """Dawn button white/#1A1A1A, featured product to Linen Blend Blazer, disable section checkout."""
    colors = find_theme(state, "Dawn")["settings"]["colors"]
    colors["accentButtonBg"] = "#FFFFFF"
    colors["accentButtonText"] = "#1A1A1A"
    sec = find_section(state, "Dawn", "home", "featured_product")
    product = find_product(state, "Linen Blend Blazer")
    sec["productId"] = product["id"]
    sec["showAcceleratedCheckout"] = False


def solve_task_h9(state):
    """Dawn button white/black, accent color match Taste."""
    colors = find_theme(state, "Dawn")["settings"]["colors"]
    colors["accentButtonBg"] = "#FFFFFF"
    colors["accentButtonText"] = "#000000"
    colors["accentColor"] = "#7C3AED"


def solve_task_h10(state):
    """Publish Ride, activate Amazon Pay + Venmo, ensure Ride checkout enabled."""
    for t in state["themes"]:
        if t["role"] == "main":
            t["role"] = "unpublished"
    find_theme(state, "Ride")["role"] = "main"
    find_payment_method(state, "Amazon Pay")["isActive"] = True
    find_payment_method(state, "Venmo")["isActive"] = True
    find_template(state, "Ride", "Default product")["showAcceleratedCheckout"] = True


def solve_task_h11(state):
    """Move Digital Gift Card to Gift cards template, enable checkout, activate terms."""
    tmpl = find_template(state, "Dawn", "Product - Gift cards")
    find_product(state, "Digital Gift Card")["templateId"] = tmpl["id"]
    tmpl["showAcceleratedCheckout"] = True
    find_cart_attr(state, "Terms and conditions")["isActive"] = True


def solve_task_h12(state):
    """Deactivate all accelerated except Shop Pay, enable Shop Promise."""
    find_payment_method(state, "Apple Pay")["isActive"] = False
    find_payment_method(state, "Google Pay")["isActive"] = False
    find_payment_method(state, "PayPal")["isActive"] = False
    state["shopPromise"]["isActive"] = True


def solve_task_h13(state):
    """Create 'Product - Limited Edition' on Dawn with checkout, assign Titanium Watch + Silk Blend Scarf."""
    theme = find_theme(state, "Dawn")
    tmpl_id = "tmpl_" + str(state["_nextTemplateId"])
    state["_nextTemplateId"] += 1
    state["templates"].append({
        "id": tmpl_id,
        "themeId": theme["id"],
        "name": "Product - Limited Edition",
        "handle": "product.product---limited-edition",
        "isDefault": False,
        "isAlternate": True,
        "showAcceleratedCheckout": True,
        "showQuantitySelector": True,
        "buyButtonText": "Add to cart",
        "createdAt": "2026-03-02T12:00:00Z"
    })
    find_product(state, "Titanium Watch")["templateId"] = tmpl_id
    find_product(state, "Silk Blend Scarf")["templateId"] = tmpl_id


def solve_task_h14(state):
    """Change home featured product to Organic Denim Jacket, disable section checkout."""
    sec = find_section(state, "Dawn", "home", "featured_product")
    product = find_product(state, "Organic Denim Jacket")
    sec["productId"] = product["id"]
    sec["showAcceleratedCheckout"] = False


def solve_task_h15(state):
    """Deactivate conflicting apps + cart attrs, activate Amazon Pay, enable Shop Promise."""
    find_app(state, "Currency Converter Plus")["isActive"] = False
    find_app(state, "Oberlo Dropshipping")["isActive"] = False
    find_app(state, "ReConvert Upsell & Cross Sell")["isActive"] = False
    find_cart_attr(state, "Gift wrapping")["isActive"] = False
    find_cart_attr(state, "Delivery date")["isActive"] = False
    find_payment_method(state, "Amazon Pay")["isActive"] = True
    state["shopPromise"]["isActive"] = True


def solve_task_h16(state):
    """Publish Taste, enable checkout on default, change button font to Oswald."""
    for t in state["themes"]:
        if t["role"] == "main":
            t["role"] = "unpublished"
    find_theme(state, "Taste")["role"] = "main"
    find_template(state, "Taste", "Default product")["showAcceleratedCheckout"] = True
    find_theme(state, "Taste")["settings"]["typography"]["buttonFont"] = "Oswald"


def solve_task_h17(state):
    """Move all active Stride Lab products to 'No checkout buttons' template."""
    tmpl = find_template(state, "Dawn", "Product - No checkout buttons")
    for p in state["products"]:
        if p["vendor"] == "Stride Lab" and p["status"] == "active":
            p["templateId"] = tmpl["id"]


def solve_task_h18(state):
    """Dawn fonts match Sense, body scale 95%."""
    typo = find_theme(state, "Dawn")["settings"]["typography"]
    typo["headingFont"] = "DM Serif Display"
    typo["bodyFont"] = "DM Sans"
    typo["bodyScale"] = 95


def solve_task_h19(state):
    """Disable checkout on every template that has it enabled."""
    for t in state["templates"]:
        if t.get("showAcceleratedCheckout"):
            t["showAcceleratedCheckout"] = False


def solve_task_h20(state):
    """Enable Amazon Pay + Venmo, deactivate conflicting apps, enable terms."""
    find_payment_method(state, "Amazon Pay")["isActive"] = True
    find_payment_method(state, "Venmo")["isActive"] = True
    find_app(state, "Currency Converter Plus")["isActive"] = False
    find_app(state, "Oberlo Dropshipping")["isActive"] = False
    find_app(state, "ReConvert Upsell & Cross Sell")["isActive"] = False
    find_cart_attr(state, "Terms and conditions")["isActive"] = True


# ---- Solve Functions (Hardening Round 1) ----

def solve_task_h21(state):
    """Featured product = highest variant price product, disable section checkout."""
    max_price = 0
    max_product_id = None
    for p in state["products"]:
        for v in p.get("variants", []):
            price = float(v.get("price", 0))
            if price > max_price:
                max_price = price
                max_product_id = p["id"]
    sec = find_section(state, "Dawn", "home", "featured_product")
    sec["productId"] = max_product_id
    sec["showAcceleratedCheckout"] = False


def solve_task_h22(state):
    """Archive products with compare-at prices, move active Atelier to Dawn default."""
    default_tmpl = find_default_template(state, "Dawn")
    for p in state["products"]:
        has_compare_at = any(v.get("compareAtPrice") is not None for v in p.get("variants", []))
        if has_compare_at:
            p["status"] = "archived"
    for p in state["products"]:
        if p["vendor"] == "Atelier Goods" and p["status"] == "active":
            p["templateId"] = default_tmpl["id"]


def solve_task_h23(state):
    """Shop Promise: min=active accelerated count, max=2x, threshold=$100."""
    count = sum(
        1 for m in state["paymentMethods"]
        if m.get("type") == "accelerated" and m.get("isActive") is True
    )
    state["shopPromise"]["isActive"] = True
    state["shopPromise"]["estimatedDeliveryDays"]["min"] = count
    state["shopPromise"]["estimatedDeliveryDays"]["max"] = count * 2
    state["shopPromise"]["freeShippingThreshold"] = 100


def solve_task_h24(state):
    """Copy Vintage Revival heading/body fonts and accent color to Dawn."""
    vintage = find_theme(state, "Vintage Revival")
    dawn = find_theme(state, "Dawn")
    dawn["settings"]["typography"]["headingFont"] = vintage["settings"]["typography"]["headingFont"]
    dawn["settings"]["typography"]["bodyFont"] = vintage["settings"]["typography"]["bodyFont"]
    dawn["settings"]["colors"]["accentColor"] = vintage["settings"]["colors"]["accentColor"]


def solve_task_h25(state):
    """Move products from vendor with exactly 2 active products to No checkout buttons."""
    from collections import Counter
    vendor_counts = Counter(
        p["vendor"] for p in state["products"] if p.get("status") == "active"
    )
    target_vendor = next(v for v, c in vendor_counts.items() if c == 2)
    tmpl = find_template(state, "Dawn", "Product - No checkout buttons")
    for p in state["products"]:
        if p["vendor"] == target_vendor and p["status"] == "active":
            p["templateId"] = tmpl["id"]


def solve_task_h26(state):
    """Draft the current featured product, set Bamboo Socks as new featured, disable section checkout."""
    sec = find_section(state, "Dawn", "home", "featured_product")
    current_featured = next(p for p in state["products"] if p["id"] == sec["productId"])
    current_featured["status"] = "draft"
    bamboo = find_product(state, "Bamboo Fiber Socks")
    sec["productId"] = bamboo["id"]
    sec["showAcceleratedCheckout"] = False


def solve_task_h27(state):
    """Swap active/inactive status of two apps sharing same conflict reason."""
    find_app(state, "ReConvert Upsell & Cross Sell")["isActive"] = False
    find_app(state, "CartHook")["isActive"] = True


def solve_task_h28(state):
    """Publish Ride, set button bg to Dawn accent, activate Amazon Pay, buy button text."""
    dawn_accent = find_theme(state, "Dawn")["settings"]["colors"]["accentColor"]
    for t in state["themes"]:
        if t["role"] == "main":
            t["role"] = "unpublished"
    find_theme(state, "Ride")["role"] = "main"
    find_theme(state, "Ride")["settings"]["colors"]["accentButtonBg"] = dawn_accent
    find_payment_method(state, "Amazon Pay")["isActive"] = True
    find_template(state, "Ride", "Default product")["buyButtonText"] = "Buy it now"


def solve_task_h29(state):
    """Create 'Product - Active Gear' on Dawn, assign Activewear products."""
    theme = find_theme(state, "Dawn")
    tmpl_id = "tmpl_" + str(state["_nextTemplateId"])
    state["_nextTemplateId"] += 1
    state["templates"].append({
        "id": tmpl_id,
        "themeId": theme["id"],
        "name": "Product - Active Gear",
        "handle": "product.product---active-gear",
        "isDefault": False,
        "isAlternate": True,
        "showAcceleratedCheckout": True,
        "showQuantitySelector": True,
        "buyButtonText": "Get moving",
        "createdAt": "2026-03-02T12:00:00Z"
    })
    for p in state["products"]:
        if p["productType"] == "Activewear":
            p["templateId"] = tmpl_id


def solve_task_h30(state):
    """Activate draft Atelier products, move all Atelier to Gift cards, enable checkout."""
    gift_cards = find_template(state, "Dawn", "Product - Gift cards")
    for p in state["products"]:
        if p["vendor"] == "Atelier Goods":
            if p["status"] == "draft":
                p["status"] = "active"
            p["templateId"] = gift_cards["id"]
    gift_cards["showAcceleratedCheckout"] = True


def solve_task_h31(state):
    """Move gift card product to Dawn default, disable checkout on default."""
    gc_product = next(p for p in state["products"] if p.get("hasGiftCardRecipientFields") is True)
    default_tmpl = find_default_template(state, "Dawn")
    gc_product["templateId"] = default_tmpl["id"]
    default_tmpl["showAcceleratedCheckout"] = False


def solve_task_h32(state):
    """Update Craft heading/body fonts, publish Craft."""
    craft = find_theme(state, "Craft")
    craft["settings"]["typography"]["headingFont"] = "Oswald"
    craft["settings"]["typography"]["bodyFont"] = "Nunito"
    for t in state["themes"]:
        if t["role"] == "main":
            t["role"] = "unpublished"
    craft["role"] = "main"


def solve_task_h33(state):
    """Shop Promise 2-7 days, deactivate PayPal, activate Amazon, Dawn button red/white."""
    state["shopPromise"]["isActive"] = True
    state["shopPromise"]["estimatedDeliveryDays"]["min"] = 2
    state["shopPromise"]["estimatedDeliveryDays"]["max"] = 7
    find_payment_method(state, "PayPal")["isActive"] = False
    find_payment_method(state, "Amazon Pay")["isActive"] = True
    colors = find_theme(state, "Dawn")["settings"]["colors"]
    colors["accentButtonBg"] = "#DC2626"
    colors["accentButtonText"] = "#FFFFFF"


def solve_task_h34(state):
    """Move earliest No-checkout product to Gift cards, newest to default."""
    no_checkout = find_template(state, "Dawn", "Product - No checkout buttons")
    gift_cards = find_template(state, "Dawn", "Product - Gift cards")
    default_tmpl = find_default_template(state, "Dawn")
    nc_products = [p for p in state["products"] if p["templateId"] == no_checkout["id"]]
    nc_products.sort(key=lambda p: p["createdAt"])
    earliest = nc_products[0]
    newest = nc_products[-1]
    earliest["templateId"] = gift_cards["id"]
    newest["templateId"] = default_tmpl["id"]


def solve_task_h35(state):
    """Copy colors from unpublished theme with highest heading scale to Dawn."""
    unpublished = [t for t in state["themes"] if t.get("role") == "unpublished"]
    highest = max(unpublished, key=lambda t: t["settings"]["typography"]["headingScale"])
    dawn = find_theme(state, "Dawn")
    for key in ["accentButtonBg", "accentButtonText", "primaryBg", "primaryText",
                "secondaryBg", "secondaryText", "accentColor"]:
        dawn["settings"]["colors"][key] = highest["settings"]["colors"][key]


def solve_task_h36(state):
    """Activate most recent Atelier product, move earliest to Gift cards."""
    atelier = [p for p in state["products"] if p["vendor"] == "Atelier Goods"]
    atelier.sort(key=lambda p: p["createdAt"])
    earliest = atelier[0]
    newest = atelier[-1]
    newest["status"] = "active"
    gift_cards = find_template(state, "Dawn", "Product - Gift cards")
    earliest["templateId"] = gift_cards["id"]


def solve_task_h37(state):
    """Disable Craft Featured checkout, set button font Montserrat, publish Craft."""
    craft = find_theme(state, "Craft")
    find_template(state, "Craft", "Product - Featured")["showAcceleratedCheckout"] = False
    craft["settings"]["typography"]["buttonFont"] = "Montserrat"
    for t in state["themes"]:
        if t["role"] == "main":
            t["role"] = "unpublished"
    craft["role"] = "main"


def solve_task_h38(state):
    """Enable checkout + change text on No checkout template, disable home section checkout."""
    tmpl = find_template(state, "Dawn", "Product - No checkout buttons")
    tmpl["showAcceleratedCheckout"] = True
    tmpl["buyButtonText"] = "Quick add"
    sec = find_section(state, "Dawn", "home", "featured_product")
    sec["showAcceleratedCheckout"] = False


def solve_task_h39(state):
    """Deactivate restricted accelerated methods, activate unrestricted, threshold $50."""
    for m in state["paymentMethods"]:
        if m.get("type") != "accelerated":
            continue
        has_restriction = (
            m.get("browserRestrictions") is not None or
            (m.get("regionRestrictions") is not None and len(m.get("regionRestrictions", [])) > 0)
        )
        if has_restriction:
            m["isActive"] = False
        else:
            m["isActive"] = True
    state["shopPromise"]["freeShippingThreshold"] = 50


def solve_task_h40(state):
    """Swap: Dawn primaryText → Sense accentButtonBg, Sense accentColor → Dawn accentColor."""
    dawn = find_theme(state, "Dawn")
    sense = find_theme(state, "Sense")
    dawn_primary_text = dawn["settings"]["colors"]["primaryText"]
    sense_accent_color = sense["settings"]["colors"]["accentColor"]
    sense["settings"]["colors"]["accentButtonBg"] = dawn_primary_text
    dawn["settings"]["colors"]["accentColor"] = sense_accent_color


# ---- Solve Functions (Hardening Round 2) ----

def solve_task_h41(state):
    """Copy typography from theme with DM Sans body font (Sense) to Craft."""
    sense = find_theme(state, "Sense")
    craft = find_theme(state, "Craft")
    src = sense["settings"]["typography"]
    craft["settings"]["typography"]["headingFont"] = src["headingFont"]
    craft["settings"]["typography"]["bodyFont"] = src["bodyFont"]
    craft["settings"]["typography"]["buttonFont"] = src["buttonFont"]
    craft["settings"]["typography"]["headingScale"] = src["headingScale"]
    craft["settings"]["typography"]["bodyScale"] = src["bodyScale"]


def solve_task_h42(state):
    """Create 'Product - Sale Items' on Dawn, assign products with compare-at prices."""
    theme = find_theme(state, "Dawn")
    tmpl_id = "tmpl_" + str(state["_nextTemplateId"])
    state["_nextTemplateId"] += 1
    state["templates"].append({
        "id": tmpl_id,
        "themeId": theme["id"],
        "name": "Product - Sale Items",
        "handle": "product.product---sale-items",
        "isDefault": False,
        "isAlternate": True,
        "showAcceleratedCheckout": True,
        "showQuantitySelector": True,
        "buyButtonText": "Buy on sale",
        "createdAt": "2026-03-02T12:00:00Z"
    })
    for p in state["products"]:
        has_compare = any(
            v.get("compareAtPrice") is not None
            for v in p.get("variants", [])
        )
        if has_compare:
            p["templateId"] = tmpl_id


def solve_task_h43(state):
    """Enable Shop Promise 2-4/$50, deactivate requiresSetup methods, enable terms."""
    state["shopPromise"]["isActive"] = True
    state["shopPromise"]["estimatedDeliveryDays"]["min"] = 2
    state["shopPromise"]["estimatedDeliveryDays"]["max"] = 4
    state["shopPromise"]["freeShippingThreshold"] = 50
    for m in state["paymentMethods"]:
        if m.get("type") == "accelerated" and m.get("requiresSetup") is True:
            m["isActive"] = False
    find_cart_attr(state, "Terms and conditions")["isActive"] = True


def solve_task_h44(state):
    """Archive Home & Gather products, move No checkout products to default."""
    default_tmpl = find_default_template(state, "Dawn")
    no_checkout = find_template(state, "Dawn", "Product - No checkout buttons")
    for p in state["products"]:
        if p["vendor"] == "Home & Gather":
            p["status"] = "archived"
    for p in state["products"]:
        if p["templateId"] == no_checkout["id"]:
            p["templateId"] = default_tmpl["id"]


def solve_task_h45(state):
    """Featured product to Titanium Watch, disable section checkout, default template text+checkout."""
    sec = find_section(state, "Dawn", "home", "featured_product")
    product = find_product(state, "Titanium Watch")
    sec["productId"] = product["id"]
    sec["showAcceleratedCheckout"] = False
    tmpl = find_default_template(state, "Dawn")
    tmpl["buyButtonText"] = "Shop now"
    tmpl["showAcceleratedCheckout"] = False


def solve_task_h46(state):
    """Activewear to No checkout, Accessories to default."""
    default_tmpl = find_default_template(state, "Dawn")
    no_checkout = find_template(state, "Dawn", "Product - No checkout buttons")
    for p in state["products"]:
        if p["productType"] == "Activewear":
            p["templateId"] = no_checkout["id"]
        elif p["productType"] == "Accessories":
            p["templateId"] = default_tmpl["id"]


def solve_task_h47(state):
    """Activate archived Heavyweight Hoodie, archive same-vendor Outerwear products."""
    hoodie = find_product(state, "Heavyweight Hoodie")
    hoodie["status"] = "active"
    vendor = hoodie["vendor"]
    for p in state["products"]:
        if p["vendor"] == vendor and p["productType"] == "Outerwear" and p["id"] != hoodie["id"]:
            p["status"] = "archived"


def solve_task_h48(state):
    """Activate Amazon Pay + Venmo, publish Ride, enable checkout, button font Oswald."""
    find_payment_method(state, "Amazon Pay")["isActive"] = True
    find_payment_method(state, "Venmo")["isActive"] = True
    for t in state["themes"]:
        if t["role"] == "main":
            t["role"] = "unpublished"
    find_theme(state, "Ride")["role"] = "main"
    find_template(state, "Ride", "Default product")["showAcceleratedCheckout"] = True
    find_theme(state, "Ride")["settings"]["typography"]["buttonFont"] = "Oswald"


def solve_task_h49(state):
    """Swap checkout button colors between Dawn and Ride."""
    dawn = find_theme(state, "Dawn")
    ride = find_theme(state, "Ride")
    dawn_bg = dawn["settings"]["colors"]["accentButtonBg"]
    dawn_text = dawn["settings"]["colors"]["accentButtonText"]
    ride_bg = ride["settings"]["colors"]["accentButtonBg"]
    ride_text = ride["settings"]["colors"]["accentButtonText"]
    dawn["settings"]["colors"]["accentButtonBg"] = ride_bg
    dawn["settings"]["colors"]["accentButtonText"] = ride_text
    ride["settings"]["colors"]["accentButtonBg"] = dawn_bg
    ride["settings"]["colors"]["accentButtonText"] = dawn_text


def solve_task_h50(state):
    """Delete Dawn template with fewest products, disable checkout on remaining + section."""
    dawn = find_theme(state, "Dawn")
    dawn_templates = [t for t in state["templates"] if t["themeId"] == dawn["id"] and not t["isDefault"]]
    # Count products per template
    min_count = float("inf")
    min_tmpl = None
    for tmpl in dawn_templates:
        count = sum(1 for p in state["products"] if p["templateId"] == tmpl["id"])
        if count < min_count:
            min_count = count
            min_tmpl = tmpl
    # Reassign products from deleted template to default
    default_tmpl = find_default_template(state, "Dawn")
    for p in state["products"]:
        if p["templateId"] == min_tmpl["id"]:
            p["templateId"] = default_tmpl["id"]
    state["templates"] = [t for t in state["templates"] if t["id"] != min_tmpl["id"]]
    # Disable checkout on all remaining Dawn templates
    for t in state["templates"]:
        if t["themeId"] == dawn["id"]:
            t["showAcceleratedCheckout"] = False
    # Disable on home section
    sec = find_section(state, "Dawn", "home", "featured_product")
    sec["showAcceleratedCheckout"] = False


def solve_task_h51(state):
    """Shop Promise: min=conflicting app count, max=2x, threshold=$80."""
    count = sum(1 for a in state["installedApps"] if a.get("conflictsWithCheckout") is True)
    state["shopPromise"]["isActive"] = True
    state["shopPromise"]["estimatedDeliveryDays"]["min"] = count
    state["shopPromise"]["estimatedDeliveryDays"]["max"] = count * 2
    state["shopPromise"]["freeShippingThreshold"] = 80


def solve_task_h52(state):
    """Find unpublished theme with headingScale 110% (Craft), publish, heading→body font."""
    craft = find_theme(state, "Craft")
    body_font = craft["settings"]["typography"]["bodyFont"]
    craft["settings"]["typography"]["headingFont"] = body_font
    for t in state["themes"]:
        if t["role"] == "main":
            t["role"] = "unpublished"
    craft["role"] = "main"


def solve_task_h53(state):
    """Move current featured (prod_1) to No checkout + draft, set Waxed Canvas as featured."""
    sec = find_section(state, "Dawn", "home", "featured_product")
    current = next(p for p in state["products"] if p["id"] == sec["productId"])
    no_checkout = find_template(state, "Dawn", "Product - No checkout buttons")
    current["templateId"] = no_checkout["id"]
    current["status"] = "draft"
    backpack = find_product(state, "Waxed Canvas Backpack")
    sec["productId"] = backpack["id"]
    sec["showAcceleratedCheckout"] = False


def solve_task_h54(state):
    """Publish Sense, apply Dawn's button colors to Sense, heading=Montserrat, enable checkout."""
    dawn = find_theme(state, "Dawn")
    dawn_bg = dawn["settings"]["colors"]["accentButtonBg"]
    dawn_text = dawn["settings"]["colors"]["accentButtonText"]
    for t in state["themes"]:
        if t["role"] == "main":
            t["role"] = "unpublished"
    sense = find_theme(state, "Sense")
    sense["role"] = "main"
    sense["settings"]["colors"]["accentButtonBg"] = dawn_bg
    sense["settings"]["colors"]["accentButtonText"] = dawn_text
    sense["settings"]["typography"]["headingFont"] = "Montserrat"
    find_template(state, "Sense", "Default product")["showAcceleratedCheckout"] = True


def solve_task_h55(state):
    """Deactivate all accelerated except PayPal, create PayPal Only template, assign gift card."""
    for m in state["paymentMethods"]:
        if m.get("type") == "accelerated" and m["name"] != "PayPal":
            m["isActive"] = False
    find_payment_method(state, "PayPal")["isActive"] = True
    theme = find_theme(state, "Dawn")
    tmpl_id = "tmpl_" + str(state["_nextTemplateId"])
    state["_nextTemplateId"] += 1
    state["templates"].append({
        "id": tmpl_id,
        "themeId": theme["id"],
        "name": "Product - PayPal Only",
        "handle": "product.product---paypal-only",
        "isDefault": False,
        "isAlternate": True,
        "showAcceleratedCheckout": True,
        "showQuantitySelector": True,
        "buyButtonText": "Add to cart",
        "createdAt": "2026-03-02T12:00:00Z"
    })
    find_product(state, "Digital Gift Card")["templateId"] = tmpl_id


def solve_task_h56(state):
    """Dawn primaryBg→Ride's, secondaryBg→Ride's, fonts to Inter."""
    ride = find_theme(state, "Ride")
    dawn = find_theme(state, "Dawn")
    dawn["settings"]["colors"]["primaryBg"] = ride["settings"]["colors"]["primaryBg"]
    dawn["settings"]["colors"]["secondaryBg"] = ride["settings"]["colors"]["secondaryBg"]
    dawn["settings"]["typography"]["headingFont"] = "Inter"
    dawn["settings"]["typography"]["bodyFont"] = "Inter"


def solve_task_h57(state):
    """Threshold $100 (no enable), deactivate Apple+Google Pay, disable default+section checkout."""
    state["shopPromise"]["freeShippingThreshold"] = 100
    find_payment_method(state, "Apple Pay")["isActive"] = False
    find_payment_method(state, "Google Pay")["isActive"] = False
    find_default_template(state, "Dawn")["showAcceleratedCheckout"] = False
    sec = find_section(state, "Dawn", "home", "featured_product")
    sec["showAcceleratedCheckout"] = False


def solve_task_h58(state):
    """Activate draft product (Cashmere Beanie), create Curated template, assign vendor products."""
    beanie = find_product(state, "Cashmere Beanie")
    beanie["status"] = "active"
    vendor = beanie["vendor"]  # Atelier Goods
    theme = find_theme(state, "Dawn")
    tmpl_id = "tmpl_" + str(state["_nextTemplateId"])
    state["_nextTemplateId"] += 1
    state["templates"].append({
        "id": tmpl_id,
        "themeId": theme["id"],
        "name": "Product - Curated",
        "handle": "product.product---curated",
        "isDefault": False,
        "isAlternate": True,
        "showAcceleratedCheckout": True,
        "showQuantitySelector": True,
        "buyButtonText": "Add to collection",
        "createdAt": "2026-03-02T12:00:00Z"
    })
    for p in state["products"]:
        if p["vendor"] == vendor:
            p["templateId"] = tmpl_id


def solve_task_h59(state):
    """Dawn secondary #E8E8E8/#444444, publish Taste, apply same to Taste."""
    dawn = find_theme(state, "Dawn")
    dawn["settings"]["colors"]["secondaryBg"] = "#E8E8E8"
    dawn["settings"]["colors"]["secondaryText"] = "#444444"
    for t in state["themes"]:
        if t["role"] == "main":
            t["role"] = "unpublished"
    taste = find_theme(state, "Taste")
    taste["role"] = "main"
    taste["settings"]["colors"]["secondaryBg"] = "#E8E8E8"
    taste["settings"]["colors"]["secondaryText"] = "#444444"


def solve_task_h60(state):
    """Disable conflicting cart attrs + apps, activate Amazon+Venmo, Shop Promise 1-3/$50, publish Craft."""
    for attr in state["cartAttributes"]:
        if attr.get("conflictsWithCheckout") is True:
            attr["isActive"] = False
    for app in state["installedApps"]:
        if app.get("conflictsWithCheckout") is True:
            app["isActive"] = False
    find_payment_method(state, "Amazon Pay")["isActive"] = True
    find_payment_method(state, "Venmo")["isActive"] = True
    state["shopPromise"]["isActive"] = True
    state["shopPromise"]["estimatedDeliveryDays"]["min"] = 1
    state["shopPromise"]["estimatedDeliveryDays"]["max"] = 3
    state["shopPromise"]["freeShippingThreshold"] = 50
    for t in state["themes"]:
        if t["role"] == "main":
            t["role"] = "unpublished"
    find_theme(state, "Craft")["role"] = "main"


# ---- Solver registry ----

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
}


# ---- Server management ----

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


# ---- Task runner ----

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


def run_single_task(task, server_url, seed_state):
    """Reset → solve → verify for a single task."""
    task_id = task["id"]
    solver = SOLVERS.get(task_id)
    if not solver:
        return task_id, False, f"No solver defined for {task_id}"

    try:
        # 1. Write seed state (reset)
        resp = requests.put(
            f"{server_url}/api/state",
            json=seed_state,
            headers={"Content-Type": "application/json"},
        )
        if resp.status_code != 200:
            return task_id, False, f"Reset failed: HTTP {resp.status_code}"

        time.sleep(0.1)

        # 2. Read seed state back from server
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
            result = run_single_task(task, server_url, seed_state)
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
            return run_single_task(task, server_url, seed_state)
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


def main():
    parser = argparse.ArgumentParser(description="Shopify Dynamic Checkout real-task sanity check")
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
