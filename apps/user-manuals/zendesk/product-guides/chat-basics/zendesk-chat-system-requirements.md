# Zendesk Chat system requirements

Source: https://support.zendesk.com/hc/en-us/articles/4408834409370-Zendesk-Chat-system-requirements

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Live chat and messaging Team, Professional, or Enterprise |

Zendesk Chat is a web-based SaaS (software as a service) application that runs in a web browser.

Zendesk Chat supports the following browsers running in Windows or Mac OS X. Your browser must be a stable release version, not an Alpha/Beta/Nightly/Development build. This applies to all browsers, regardless of operating system.

If you are using live chat inside of Zendesk Support, you should also check the [Zendesk Support system requirements doc](http://support.zendesk.com/hc/en-us/articles/4408893306010).

If you are using a version of live chat integrated with the Web Widget (Classic), check the [Web Widget (Classic) requirements](http://support.zendesk.com/hc/en-us/articles/4408836216218#topic_rzl_q2n_4r) for more information.

Use these links to view the requirements for the following elements:

- [Agent/Administrator dashboard interface](#topic_scm_hqv_m4b)
- [Desktop notifications](#topic_ch4_hqv_m4b)
- [Admin Center](#topic_l54_hqv_m4b)
- [Mobile (agent requirements)](#topic_edp_hqv_m4b)
- [SDK](#topic_ulp_hqv_m4b)
- [Chat emoji](#topic_wtp_hqv_m4b)

 - [Desktop](#topic_aqf_mqv_m4b)
 - [Mobile](#topic_ncm_mqv_m4b)
- [Browser configuration](#topic_ybq_hqv_m4b)
- [Visitor requirements](#topic_zrq_hqv_m4b)

 - [Desktop](#topic_sgm_vqv_m4b)
 - [Mobile](#topic_p5r_vqv_m4b)
- [Firewall configuration](#topic_jt2_hqv_m4b)

## Agent/Administrator dashboard interface

- Google Chrome v.25 and higher
- Mozilla Firefox v.21 and higher
- Apple Safari v.6 and higher
- Microsoft Edge

## Desktop notifications

- Google Chrome v.22 and higher
- Mozilla Firefox v.22 and higher
- Apple Safari v.6 and higher

 Note: Safari v. 11 will automatically block sound notifications. See [Editing your chat notification settings](https://support.zendesk.com/hc/en-us/articles/4408821476378) for information on permitting sound notifications in Safari.
- Microsoft Edge v.14 and higher

## Admin Center

- Google Chrome: latest two versions
- Mozilla Firefox: latest two versions
- Apple Safari: latest two versions
- Microsoft Edge

## Mobile (agent requirements)

- Apple iOS 7 and higher
- Google Android 2.3 and higher

## SDK

- Apple iOS 6.0 and higher
- Google Android 2.3 (API Level 9) and higher

## Chat emoji

### Desktop

- Google Chrome v.10 on Windows
- Mozilla Firefox v.7 and higher on Windows,
- Google Chrome v.10.10 and higher on OS X
- Mozilla Firefox v10.7 and higher on OS X
- Apple Safari v.10.7 and higher
- Microsoft Edge v.10

### Mobile

- Apple Safari v.5 and higher on iOS.
- Google Chrome v.5 and higher on iOS
- Google Chrome v4.4 and higher on Android

## Browser configuration

- JavaScript must be enabled
- Cookies must be enabled
- localStorage must be enabled
- TLS v1.2 or above

## Visitor requirements

### Desktop

- Google Chrome v.25 and higher
- Mozilla Firefox v.21 and higher
- Apple Safari v.6
- Mozilla Firefox v.21 and higher
- Apple Safari v.6 and higher
- Microsoft Edge

### Mobile

- latest two major versions of Safari on iOS
- latest version of Chrome on iOS
- latest two major versions of Chrome on Android
- latest version of Firefox on Android

Note: The overlay mobile widget is not supported for the Android Browser on 4.3 and below. The widget will fall back to the chat popup mode and open in a new tab. Chrome and Firefox on Android 4.3 and below will work as expected (open in overlay).

## Firewall configuration

Zendesk Chat only uses ports 80 and 443, which should be open on all firewalls as they are standard ports. The more important thing to look for is the following:

- Traffic from \*.[zopim.com](http://zopim.com/) is whitelisted on the firewall. (\* is a wildcard and means all subdomains on the [zopim.com](http://zopim.com/) domain).
- Zendesk Chat relies on Amazon for services. If the customer is blocking Amazon IPs, it could negatively impact chat performance.