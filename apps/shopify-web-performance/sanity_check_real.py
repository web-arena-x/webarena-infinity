#!/usr/bin/env python3
"""
Sanity check for Shopify Web Performance Dashboard real tasks.

For each task, directly applies the expected end-state (bypassing the agent),
then runs the verifier and asserts it passes.

Usage:
    python3 sanity_check_real.py                      # All tasks, sequential
    python3 sanity_check_real.py --workers N           # N parallel environments
    python3 sanity_check_real.py --task-id task_e1     # Single task
    python3 sanity_check_real.py --port 9500           # Custom base port
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

# ---------------------------------------------------------------------------
# Seed state generation via Node.js
# ---------------------------------------------------------------------------

_SEED_STATE_JS = r"""
const fs = require('fs');
const vm = require('vm');
const code = fs.readFileSync(process.argv[1], 'utf8');
vm.runInThisContext(code);

const state = {
    _seedVersion: SEED_DATA_VERSION,
    storeInfo: JSON.parse(JSON.stringify(STORE_INFO)),
    currentUser: JSON.parse(JSON.stringify(CURRENT_USER)),
    themes: JSON.parse(JSON.stringify(THEMES)),
    apps: JSON.parse(JSON.stringify(APPS)),
    tagManagerTags: JSON.parse(JSON.stringify(TAG_MANAGER_TAGS)),
    pages: JSON.parse(JSON.stringify(PAGES)),
    pageTypes: JSON.parse(JSON.stringify(PAGE_TYPES)),
    pagePerformance: JSON.parse(JSON.stringify(PAGE_PERFORMANCE)),
    pageTypePerformance: JSON.parse(JSON.stringify(PAGE_TYPE_PERFORMANCE)),
    performanceEvents: JSON.parse(JSON.stringify(PERFORMANCE_EVENTS)),
    sessionsByDevice: JSON.parse(JSON.stringify(SESSIONS_BY_DEVICE)),
    overallPerformance: JSON.parse(JSON.stringify(OVERALL_PERFORMANCE)),
    recommendations: JSON.parse(JSON.stringify(RECOMMENDATIONS)),
    reports: JSON.parse(JSON.stringify(REPORTS)),
    settings: JSON.parse(JSON.stringify(SETTINGS)),
    lcpOverTimeDesktop: JSON.parse(JSON.stringify(LCP_OVER_TIME_DESKTOP)),
    lcpOverTimeMobile: JSON.parse(JSON.stringify(LCP_OVER_TIME_MOBILE)),
    inpOverTimeDesktop: JSON.parse(JSON.stringify(INP_OVER_TIME_DESKTOP)),
    inpOverTimeMobile: JSON.parse(JSON.stringify(INP_OVER_TIME_MOBILE)),
    clsOverTimeDesktop: JSON.parse(JSON.stringify(CLS_OVER_TIME_DESKTOP)),
    clsOverTimeMobile: JSON.parse(JSON.stringify(CLS_OVER_TIME_MOBILE)),
};
process.stdout.write(JSON.stringify(state));
"""


def generate_seed_state():
    """Use Node.js to evaluate data.js and produce the seed state JSON."""
    data_js = str(APP_DIR / "js" / "data.js")
    result = subprocess.run(
        ["node", "-e", _SEED_STATE_JS, data_js],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"Failed to generate seed state:\n{result.stderr}")
    return json.loads(result.stdout)


# ---------------------------------------------------------------------------
# Entity lookup helpers
# ---------------------------------------------------------------------------

def find_app_by_name(state, name):
    for a in state["apps"]:
        if a["name"] == name:
            return a
    raise ValueError(f"App not found: {name!r}")


def find_app_containing(state, fragment):
    for a in state["apps"]:
        if fragment in a["name"]:
            return a
    raise ValueError(f"App containing {fragment!r} not found")


def find_tag_by_name(state, name):
    for t in state["tagManagerTags"]:
        if t["name"] == name:
            return t
    raise ValueError(f"Tag not found: {name!r}")


def find_theme_by_name(state, name):
    for t in state["themes"]:
        if t["name"] == name:
            return t
    raise ValueError(f"Theme not found: {name!r}")


def find_rec_by_title(state, title):
    for r in state["recommendations"]:
        if r["title"] == title:
            return r
    raise ValueError(f"Recommendation not found: {title!r}")


def disable_app(app):
    """Set an app to disabled status."""
    app["status"] = "disabled"
    app["loadsOnStorefront"] = False


def remove_app_by_name(state, name):
    """Remove an app by exact name."""
    state["apps"] = [a for a in state["apps"] if a["name"] != name]


def remove_app_containing(state, fragment):
    """Remove an app by name fragment."""
    state["apps"] = [a for a in state["apps"] if fragment not in a["name"]]


def remove_tag_by_name(state, name):
    """Remove a tag by exact name."""
    state["tagManagerTags"] = [t for t in state["tagManagerTags"] if t["name"] != name]


def publish_theme(state, theme_name):
    """Publish a theme and unpublish the current main."""
    for theme in state["themes"]:
        if theme["name"] == theme_name:
            theme["role"] = "main"
            theme["status"] = "published"
            state["settings"]["selectedThemeId"] = theme["id"]
        elif theme["role"] == "main":
            theme["role"] = "unpublished"
            theme["status"] = "unpublished"


# ---------------------------------------------------------------------------
# Solve functions — one per task
# ---------------------------------------------------------------------------

# ---- Easy tasks ----

def solve_task_e1(state):
    """Disable Klaviyo app."""
    disable_app(find_app_by_name(state, "Klaviyo: Email Marketing & SMS"))


def solve_task_e2(state):
    """Remove Hotjar app."""
    remove_app_containing(state, "Hotjar")


def solve_task_e3(state):
    """Enable SEO Manager app."""
    app = find_app_by_name(state, "SEO Manager")
    app["status"] = "active"
    app["loadsOnStorefront"] = app["scriptsCount"] > 0


def solve_task_e4(state):
    """Deactivate TikTok Pixel tag."""
    find_tag_by_name(state, "TikTok Pixel")["status"] = "inactive"


def solve_task_e5(state):
    """Remove Snapchat Pixel tag."""
    remove_tag_by_name(state, "Snapchat Pixel")


def solve_task_e6(state):
    """Publish Dawn backup theme."""
    publish_theme(state, "Dawn (backup)")


def solve_task_e7(state):
    """Disable animations on Horizon."""
    find_theme_by_name(state, "Horizon - Outdoors")["hasAnimations"] = False


def solve_task_e8(state):
    """Resolve hero image recommendation."""
    find_rec_by_title(state, "Optimize large hero images on homepage")["status"] = "resolved"


def solve_task_e9(state):
    """Dismiss web fonts recommendation."""
    find_rec_by_title(state, "Preload web fonts")["status"] = "dismissed"


def solve_task_e10(state):
    """Change date range to last 30 days."""
    state["settings"]["dateRange"] = "last_30_days"


def solve_task_e11(state):
    """Filter to mobile devices."""
    state["settings"]["deviceFilter"] = "mobile"


def solve_task_e12(state):
    """Disable email alerts."""
    state["settings"]["performanceAlerts"]["emailAlerts"] = False


def solve_task_e13(state):
    """Disable page transitions on Prestige."""
    find_theme_by_name(state, "Prestige")["hasPageTransitions"] = False


def solve_task_e14(state):
    """Activate Pinterest Tag."""
    find_tag_by_name(state, "Pinterest Tag")["status"] = "active"


def solve_task_e15(state):
    """Disable comparison."""
    state["settings"]["comparisonEnabled"] = False


def solve_task_e16(state):
    """Remove Affirm Messaging tag."""
    remove_tag_by_name(state, "Affirm Messaging")


def solve_task_e17(state):
    """Disable Recharge Subscriptions app."""
    disable_app(find_app_by_name(state, "Recharge Subscriptions"))


def solve_task_e18(state):
    """Reopen audit tags recommendation."""
    find_rec_by_title(state, "Audit tag manager for unused tags")["status"] = "open"


def solve_task_e19(state):
    """Enable password protection."""
    state["storeInfo"]["passwordProtected"] = True


def solve_task_e20(state):
    """Hide annotations."""
    state["settings"]["showAnnotations"] = False


# ---- Medium tasks ----

def solve_task_m1(state):
    """Disable Privy and Hotjar."""
    disable_app(find_app_containing(state, "Privy"))
    disable_app(find_app_containing(state, "Hotjar"))


def solve_task_m2(state):
    """Switch percentile to P90 and date grouping to weekly."""
    state["settings"]["reportPercentile"] = "p90"
    state["settings"]["dateGrouping"] = "weekly"


def solve_task_m3(state):
    """Remove all inactive tags."""
    for name in ["Pinterest Tag", "Snapchat Pixel", "Lucky Orange"]:
        remove_tag_by_name(state, name)


def solve_task_m4(state):
    """Publish Dawn and enable its animations."""
    publish_theme(state, "Dawn (backup)")
    find_theme_by_name(state, "Dawn (backup)")["hasAnimations"] = True


def solve_task_m5(state):
    """Lower LCP threshold to 2000, raise CLS to 0.2."""
    state["settings"]["performanceAlerts"]["lcpThreshold"] = 2000
    state["settings"]["performanceAlerts"]["clsThreshold"] = 0.2


def solve_task_m6(state):
    """Disable all analytics category apps."""
    for name in ["Google Analytics (GA4)", "Meta Pixel & Conversions API", "Hotjar Heatmaps & Recordings"]:
        disable_app(find_app_by_name(state, name))


def solve_task_m7(state):
    """Resolve all high-priority recommendations."""
    for title in [
        "Reduce the impact of third-party scripts",
        "Optimize large hero images on homepage",
        "Reserve space for Privy pop-up banner",
    ]:
        find_rec_by_title(state, title)["status"] = "resolved"


def solve_task_m8(state):
    """Turn off all performance alert notifications."""
    alerts = state["settings"]["performanceAlerts"]
    alerts["alertOnPoor"] = False
    alerts["alertOnDegradation"] = False
    alerts["emailAlerts"] = False


def solve_task_m9(state):
    """Reduce homepage sections on current theme (Horizon) to 10."""
    find_theme_by_name(state, "Horizon - Outdoors")["sectionsPerPage"]["home"] = 10


def solve_task_m10(state):
    """Deactivate Hotjar tag and remove Hotjar app."""
    find_tag_by_name(state, "Hotjar Tracking")["status"] = "inactive"
    remove_app_containing(state, "Hotjar")


def solve_task_m11(state):
    """Remove SEO Manager and Infinite Options apps."""
    remove_app_by_name(state, "SEO Manager")
    remove_app_by_name(state, "Infinite Options")


def solve_task_m12(state):
    """Switch to mobile and today."""
    state["settings"]["deviceFilter"] = "mobile"
    state["settings"]["dateRange"] = "today"


def solve_task_m13(state):
    """Dismiss low-priority open recommendations."""
    find_rec_by_title(state, "Enable pagination for large collections")["status"] = "dismissed"
    find_rec_by_title(state, "Preload web fonts")["status"] = "dismissed"


def solve_task_m14(state):
    """Increase Prestige product sections to 14."""
    find_theme_by_name(state, "Prestige")["sectionsPerPage"]["product"] = 14


def solve_task_m15(state):
    """Activate Pinterest and Snapchat tags."""
    find_tag_by_name(state, "Pinterest Tag")["status"] = "active"
    find_tag_by_name(state, "Snapchat Pixel")["status"] = "active"


def solve_task_m16(state):
    """Tighten alert thresholds."""
    alerts = state["settings"]["performanceAlerts"]
    alerts["lcpThreshold"] = 2000
    alerts["inpThreshold"] = 150
    alerts["clsThreshold"] = 0.05
    alerts["degradationPercent"] = 10


def solve_task_m17(state):
    """Disable all high-impact apps."""
    for fragment in ["Recharge", "Privy", "Hotjar"]:
        disable_app(find_app_containing(state, fragment))


def solve_task_m18(state):
    """Turn off animations and page transitions on Prestige."""
    theme = find_theme_by_name(state, "Prestige")
    theme["hasAnimations"] = False
    theme["hasPageTransitions"] = False


def solve_task_m19(state):
    """Remove inactive Pinterest and Snapchat tags."""
    remove_tag_by_name(state, "Pinterest Tag")
    remove_tag_by_name(state, "Snapchat Pixel")


def solve_task_m20(state):
    """Switch to desktop and P50."""
    state["settings"]["deviceFilter"] = "desktop"
    state["settings"]["reportPercentile"] = "p50"


# ---- Hard tasks ----

def solve_task_h1(state):
    """Disable high-impact apps and resolve third-party scripts rec."""
    for fragment in ["Recharge", "Privy", "Hotjar"]:
        disable_app(find_app_containing(state, fragment))
    find_rec_by_title(state, "Reduce the impact of third-party scripts")["status"] = "resolved"


def solve_task_h2(state):
    """Remove non-Shopify high-impact apps."""
    for fragment in ["Recharge Subscriptions", "Privy", "Hotjar"]:
        remove_app_containing(state, fragment)


def solve_task_h3(state):
    """Publish Dawn, set homepage sections to 6, enable animations."""
    publish_theme(state, "Dawn (backup)")
    dawn = find_theme_by_name(state, "Dawn (backup)")
    dawn["sectionsPerPage"]["home"] = 6
    dawn["hasAnimations"] = True


def solve_task_h4(state):
    """Remove apps with >2 scripts."""
    for fragment in ["Klaviyo", "Recharge Subscriptions", "Privy"]:
        remove_app_containing(state, fragment)


def solve_task_h5(state):
    """Publish Prestige, disable transitions/animations, homepage to 15."""
    publish_theme(state, "Prestige")
    prestige = find_theme_by_name(state, "Prestige")
    prestige["hasPageTransitions"] = False
    prestige["hasAnimations"] = False
    prestige["sectionsPerPage"]["home"] = 15


def solve_task_h6(state):
    """Strict monitoring: thresholds + P95."""
    alerts = state["settings"]["performanceAlerts"]
    alerts["lcpThreshold"] = 1500
    alerts["inpThreshold"] = 100
    alerts["clsThreshold"] = 0.05
    alerts["degradationPercent"] = 5
    state["settings"]["reportPercentile"] = "p95"


def solve_task_h7(state):
    """Remove inactive tags, deactivate advertising tags except Meta Pixel."""
    # Remove inactive tags
    for name in ["Pinterest Tag", "Snapchat Pixel", "Lucky Orange"]:
        remove_tag_by_name(state, name)
    # Deactivate advertising tags except Meta Pixel
    find_tag_by_name(state, "Google Ads Conversion")["status"] = "inactive"
    find_tag_by_name(state, "TikTok Pixel")["status"] = "inactive"


def solve_task_h8(state):
    """Disable marketing apps, resolve Privy recs."""
    for name in ["Klaviyo: Email Marketing & SMS", "Back in Stock Alerts"]:
        disable_app(find_app_by_name(state, name))
    disable_app(find_app_containing(state, "Privy"))
    find_rec_by_title(state, "Evaluate Privy pop-up timing")["status"] = "resolved"
    find_rec_by_title(state, "Reserve space for Privy pop-up banner")["status"] = "resolved"


def solve_task_h9(state):
    """Reduce homepage sections by 2 on all 3 themes."""
    find_theme_by_name(state, "Horizon - Outdoors")["sectionsPerPage"]["home"] = 10
    find_theme_by_name(state, "Dawn (backup)")["sectionsPerPage"]["home"] = 6
    find_theme_by_name(state, "Prestige")["sectionsPerPage"]["home"] = 16


def solve_task_h10(state):
    """Remove Hotjar app and tracking tag."""
    remove_app_containing(state, "Hotjar")
    remove_tag_by_name(state, "Hotjar Tracking")


def solve_task_h11(state):
    """Publish Dawn, disable >2 script apps, remove Google Ads tag."""
    publish_theme(state, "Dawn (backup)")
    for fragment in ["Klaviyo", "Recharge Subscriptions", "Privy"]:
        disable_app(find_app_containing(state, fragment))
    remove_tag_by_name(state, "Google Ads Conversion")


def solve_task_h12(state):
    """Disable apps with >300ms LCP impact, resolve third-party rec."""
    for fragment in ["Klaviyo", "Recharge", "Privy", "Hotjar"]:
        disable_app(find_app_containing(state, fragment))
    find_rec_by_title(state, "Reduce the impact of third-party scripts")["status"] = "resolved"


def solve_task_h13(state):
    """Dashboard for daily mobile review."""
    state["settings"]["deviceFilter"] = "mobile"
    state["settings"]["dateRange"] = "today"
    state["settings"]["comparisonEnabled"] = False
    state["settings"]["performanceAlerts"]["degradationPercent"] = 10


def solve_task_h14(state):
    """Slim down current theme (Horizon): animations off, all sections -2."""
    theme = find_theme_by_name(state, "Horizon - Outdoors")
    theme["hasAnimations"] = False
    theme["sectionsPerPage"]["home"] = 10
    theme["sectionsPerPage"]["product"] = 6
    theme["sectionsPerPage"]["collection"] = 4
    theme["sectionsPerPage"]["cart"] = 2
    theme["sectionsPerPage"]["blog"] = 3


def solve_task_h15(state):
    """Remove disabled apps, dismiss low-priority open recs."""
    remove_app_by_name(state, "SEO Manager")
    remove_app_by_name(state, "Infinite Options")
    find_rec_by_title(state, "Enable pagination for large collections")["status"] = "dismissed"
    find_rec_by_title(state, "Preload web fonts")["status"] = "dismissed"


def solve_task_h16(state):
    """Disable TikTok and Meta apps + deactivate their tags."""
    disable_app(find_app_containing(state, "TikTok"))
    disable_app(find_app_containing(state, "Meta Pixel"))
    find_tag_by_name(state, "TikTok Pixel")["status"] = "inactive"
    find_tag_by_name(state, "Meta Pixel")["status"] = "inactive"


def solve_task_h17(state):
    """Publish Prestige, disable transitions, homepage to 12, mobile view."""
    publish_theme(state, "Prestige")
    prestige = find_theme_by_name(state, "Prestige")
    prestige["hasPageTransitions"] = False
    prestige["sectionsPerPage"]["home"] = 12
    state["settings"]["deviceFilter"] = "mobile"


def solve_task_h18(state):
    """Remove Hotjar and TikTok apps + their tags."""
    remove_app_containing(state, "Hotjar")
    remove_app_containing(state, "TikTok")
    remove_tag_by_name(state, "Hotjar Tracking")
    remove_tag_by_name(state, "TikTok Pixel")


def solve_task_h19(state):
    """Resolve all open LCP recs, disable apps with >300ms LCP impact."""
    for title in [
        "Reduce the impact of third-party scripts",
        "Optimize large hero images on homepage",
        "Evaluate Privy pop-up timing",
        "Enable pagination for large collections",
        "Reduce homepage sections",
    ]:
        find_rec_by_title(state, title)["status"] = "resolved"
    for fragment in ["Klaviyo", "Recharge", "Privy", "Hotjar"]:
        disable_app(find_app_containing(state, fragment))


def solve_task_h20(state):
    """Comprehensive alerting setup."""
    alerts = state["settings"]["performanceAlerts"]
    alerts["alertOnPoor"] = True
    alerts["alertOnDegradation"] = True
    alerts["emailAlerts"] = True
    alerts["lcpThreshold"] = 2000
    alerts["inpThreshold"] = 150
    alerts["clsThreshold"] = 0.05
    alerts["degradationPercent"] = 10
    state["settings"]["reportPercentile"] = "p95"


# ---- Hardening round 1 tasks ----

def solve_task_h21(state):
    """Disable worst INP app (Hotjar, 110ms) and resolve JS execution rec."""
    disable_app(find_app_containing(state, "Hotjar"))
    find_rec_by_title(state, "Reduce JavaScript execution on product pages")["status"] = "resolved"


def solve_task_h22(state):
    """Deactivate all-pages advertising tags, keep checkout-only, remove inactive."""
    find_tag_by_name(state, "Meta Pixel")["status"] = "inactive"
    find_tag_by_name(state, "TikTok Pixel")["status"] = "inactive"
    for name in ["Pinterest Tag", "Snapchat Pixel", "Lucky Orange"]:
        remove_tag_by_name(state, name)


def solve_task_h23(state):
    """Publish Prestige (most total sections: 51), set home to Horizon's 12."""
    publish_theme(state, "Prestige")
    find_theme_by_name(state, "Prestige")["sectionsPerPage"]["home"] = 12


def solve_task_h24(state):
    """Disable apps with LCP >= 250 and INP >= 40."""
    for fragment in ["Recharge", "Privy", "Hotjar", "Klaviyo", "TikTok"]:
        disable_app(find_app_containing(state, fragment))


def solve_task_h25(state):
    """Disable moderate-impact apps with 2+ scripts, remove product-pages tag."""
    for name in ["Klaviyo: Email Marketing & SMS", "Google Analytics (GA4)",
                  "Meta Pixel & Conversions API", "Yotpo Loyalty & Rewards",
                  "Bold Product Options", "TikTok Channel"]:
        disable_app(find_app_by_name(state, name))
    remove_tag_by_name(state, "Affirm Messaging")


def solve_task_h26(state):
    """Set Prestige collection to Dawn's product (6), blog to 4."""
    prestige = find_theme_by_name(state, "Prestige")
    prestige["sectionsPerPage"]["collection"] = 6
    prestige["sectionsPerPage"]["blog"] = 4


def solve_task_h27(state):
    """Disable non-Shopify storefront apps, turn off comparison."""
    non_shopify = [
        "Klaviyo", "Judge.me", "Google Analytics", "Meta Pixel",
        "Recharge", "Privy", "Yotpo", "Hotjar", "Bold Product",
        "TikTok", "Back in Stock"
    ]
    for fragment in non_shopify:
        disable_app(find_app_containing(state, fragment))
    state["settings"]["comparisonEnabled"] = False


def solve_task_h28(state):
    """Disable analytics apps, remove matching tags."""
    for name in ["Google Analytics (GA4)", "Meta Pixel & Conversions API",
                  "Hotjar Heatmaps & Recordings"]:
        disable_app(find_app_by_name(state, name))
    for tag in ["Google Analytics 4", "Meta Pixel", "Hotjar Tracking"]:
        remove_tag_by_name(state, tag)


def solve_task_h29(state):
    """Horizon (more recent update): product -2. Dawn (older): blog +2."""
    find_theme_by_name(state, "Horizon - Outdoors")["sectionsPerPage"]["product"] = 6
    find_theme_by_name(state, "Dawn (backup)")["sectionsPerPage"]["blog"] = 6


def solve_task_h30(state):
    """Remove all-pages tags except GA4, disable Privy, resolve banner rec."""
    for name in ["Meta Pixel", "TikTok Pixel", "Hotjar Tracking", "Pinterest Tag",
                  "Snapchat Pixel", "Microsoft Clarity", "Lucky Orange"]:
        remove_tag_by_name(state, name)
    disable_app(find_app_containing(state, "Privy"))
    find_rec_by_title(state, "Reserve space for Privy pop-up banner")["status"] = "resolved"


def solve_task_h31(state):
    """Set Horizon home to half of Prestige's (18/2=9)."""
    find_theme_by_name(state, "Horizon - Outdoors")["sectionsPerPage"]["home"] = 9


def solve_task_h32(state):
    """Remove Yotpo/Bold, resolve medium recs, deactivate Clarity."""
    remove_app_by_name(state, "Yotpo Loyalty & Rewards")
    remove_app_by_name(state, "Bold Product Options")
    for title in [
        "Reduce JavaScript execution on product pages",
        "Set explicit dimensions for product images",
        "Evaluate Privy pop-up timing",
        "Reduce homepage sections",
    ]:
        find_rec_by_title(state, title)["status"] = "resolved"
    find_tag_by_name(state, "Microsoft Clarity")["status"] = "inactive"


def solve_task_h33(state):
    """Reduce Horizon home to 8, resolve homepage rec."""
    find_theme_by_name(state, "Horizon - Outdoors")["sectionsPerPage"]["home"] = 8
    find_rec_by_title(state, "Reduce homepage sections")["status"] = "resolved"


def solve_task_h34(state):
    """Remove marketing apps, remove tags, dismiss Privy recs."""
    for fragment in ["Klaviyo", "Privy", "Back in Stock"]:
        remove_app_containing(state, fragment)
    remove_tag_by_name(state, "TikTok Pixel")
    remove_tag_by_name(state, "Meta Pixel")
    find_rec_by_title(state, "Evaluate Privy pop-up timing")["status"] = "dismissed"
    find_rec_by_title(state, "Reserve space for Privy pop-up banner")["status"] = "dismissed"


def solve_task_h35(state):
    """Reduce all Prestige sections by 3."""
    prestige = find_theme_by_name(state, "Prestige")
    prestige["sectionsPerPage"]["home"] = 15
    prestige["sectionsPerPage"]["product"] = 9
    prestige["sectionsPerPage"]["collection"] = 6
    prestige["sectionsPerPage"]["cart"] = 2
    prestige["sectionsPerPage"]["blog"] = 4


def solve_task_h36(state):
    """Deactivate analytics tags, disable analytics apps, P90 weekly."""
    for name in ["Google Analytics 4", "Hotjar Tracking", "Microsoft Clarity"]:
        find_tag_by_name(state, name)["status"] = "inactive"
    for name in ["Google Analytics (GA4)", "Meta Pixel & Conversions API",
                  "Hotjar Heatmaps & Recordings"]:
        disable_app(find_app_by_name(state, name))
    state["settings"]["reportPercentile"] = "p90"
    state["settings"]["dateGrouping"] = "weekly"


def solve_task_h37(state):
    """Dawn: home=10, cart=5. Prestige: home=15, cart=8."""
    dawn = find_theme_by_name(state, "Dawn (backup)")
    dawn["sectionsPerPage"]["home"] = 10
    dawn["sectionsPerPage"]["cart"] = 5
    prestige = find_theme_by_name(state, "Prestige")
    prestige["sectionsPerPage"]["home"] = 15
    prestige["sectionsPerPage"]["cart"] = 8


def solve_task_h38(state):
    """Comprehensive audit prep."""
    for fragment in ["Recharge", "Privy", "Hotjar"]:
        disable_app(find_app_containing(state, fragment))
    for name in ["Pinterest Tag", "Snapchat Pixel", "Lucky Orange"]:
        remove_tag_by_name(state, name)
    for title in [
        "Reduce the impact of third-party scripts",
        "Optimize large hero images on homepage",
        "Reserve space for Privy pop-up banner",
    ]:
        find_rec_by_title(state, title)["status"] = "resolved"
    state["settings"]["dateRange"] = "last_30_days"
    state["settings"]["deviceFilter"] = "mobile"
    state["settings"]["reportPercentile"] = "p95"
    state["settings"]["comparisonEnabled"] = False


def solve_task_h39(state):
    """Publish Dawn (fewest sections: 26), enable animations, home=12."""
    publish_theme(state, "Dawn (backup)")
    dawn = find_theme_by_name(state, "Dawn (backup)")
    dawn["hasAnimations"] = True
    dawn["sectionsPerPage"]["home"] = 12


def solve_task_h40(state):
    """Disable non-analytics 2+ script apps, remove Affirm, INP threshold 100."""
    for fragment in ["Klaviyo", "Recharge", "Privy", "Yotpo", "Bold Product", "TikTok"]:
        disable_app(find_app_containing(state, fragment))
    remove_tag_by_name(state, "Affirm Messaging")
    state["settings"]["performanceAlerts"]["inpThreshold"] = 100


# ---------------------------------------------------------------------------
# Solver registry
# ---------------------------------------------------------------------------

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

# ---------------------------------------------------------------------------
# Task loading
# ---------------------------------------------------------------------------

def load_tasks():
    with open(APP_DIR / "real-tasks.json") as f:
        return json.load(f)


def load_verifier(verify_path):
    full_path = APP_DIR / verify_path
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
    raise RuntimeError(f"No free port found in range {start}-{start + 200}")


def seed_server(server_url, seed_state):
    resp = requests.put(
        f"{server_url}/api/state",
        json=seed_state,
        headers={"Content-Type": "application/json"},
    )
    if resp.status_code != 200:
        raise RuntimeError(f"Failed to seed server: HTTP {resp.status_code}")


def start_server(port):
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


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Shopify Web Performance real-task sanity check"
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
