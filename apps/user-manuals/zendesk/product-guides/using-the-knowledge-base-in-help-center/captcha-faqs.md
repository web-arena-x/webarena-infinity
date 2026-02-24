# CAPTCHA FAQs

Source: https://support.zendesk.com/hc/en-us/articles/4408839088794-CAPTCHA-FAQs

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

To keep customers safe from bad bots when accessing your help center content, Zendesk uses CAPTCHA. A CAPTCHA form renders whenever a bot is detected.

CAPTCHA is a Cloudflare rule that uses the [Cloudflare Bot management features](https://www.cloudflare.com/products/bot-management/). The rule prompts requesters for a CAPTCHA if the request matches certain criteria, such as:

- Having a BotScore that is lower than the threshold
- Excluding verified bots (such as search crawlers)
- A /hc path exists

 - For your login: [https://*yoursubdomain*.zendesk.com/auth/v2/login/](https://z3ncfblock1.zendesk.com/auth/v2/login/)
 - For your sign up: [https://*yoursubdomain.zendesk*.com/auth/v2/login/registration](https://z3ncfblock1.zendesk.com/auth/v2/login/registration)
 - For ticket submissions: [https://*yoursubdomain*.zendesk.com/hc/en-us/requests/new](https://z3ncfblock1.zendesk.com/hc/en-us/requests/new)

This article covers the following frequently asked questions and scenarios:

- [Why do I only see CAPTCHA sometimes?](#topic_wyr_fdg_dpb)
- [Why am I facing an error when rendering a CAPTCHA?](#topic_kzh_gdg_dpb)
- [I want to run an automation application or a good bot and not get blocked](#topic_e5n_gdg_dpb)
- [What does Cloudflare bot management track?](#topic_wft_gdg_dpb)
- [I have a host mapped account, what should I know?](#topic_qcg_hdg_dpb)
- [What is Cloudflare bot management?](#topic_aqr_hdg_dpb)
- [Something has gone wrong, what do I do?](#topic_cd1_3dg_dpb)

## Why do I only see CAPTCHA sometimes?

Cloudflare’s Bot Management tool analyzes all Zendesk traffic and scores it based on how likely it is to come from a human or a bot. CAPTCHAs appear when traffic is scored within a certain threshold, as it is mostly meant for bots. A bot score of <5 emphasizes just how strict we are on bots in particular.

It is extremely rare that traffic from an actual human is misclassified as bot traffic by Cloudflare.

## Why am I facing an error when rendering a CAPTCHA?

Ad blockers can turn off CAPTCHAs in certain browsers and older browsers may experience issues displaying CAPTCHAs (see [Frequently asked questions about Cloudflare bot products](https://support.cloudflare.com/hc/en-us/articles/360035387431#5KX8t3C6SObnoWs5F6YOlU)).

## I want to run an automation application or a good bot and not get blocked

If you are running a good bot and it's still being blocked, [contact Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850).

## What does Cloudflare bot management track?

- Scenario: You are running a good automation or a good bot on the request form or the anonymous [requests API](https://developer.zendesk.com/api-reference/ticketing/tickets/ticket-requests/#create-request).

 Cloudflare bot management does not track traffic on the API. It does track traffic on the form, even though it is not expected that the form has any traffic.
- Scenario: You have a custom web form for ticket submission.

 Cloudflare bot management tracks the traffic for all custom web forms going through ticket submission.

## I have a host mapped account, what should I know?

Cloudflare bot management tracks the traffic for host mapped accounts. This is not an option that you can disable in the CAPTCHA settings. CAPTCHA is enabled by default when you allow anybody to submit tickets and can't be disabled.

## What is Cloudflare bot management?

Zendesk uses the [Cloudflare Bot management](https://www.cloudflare.com/products/bot-management/) feature. It prompts requesters for a CAPTCHA if the request matches certain criteria. For example, if you set a bot score threshold, the feature will prompt a CAPTCHA for all traffic that matches the bot score threshold value (see [What is the difference between the threat score and bot management score?](https://support.cloudflare.com/hc/en-us/articles/360027519452-Understanding-Cloudflare-Bot-Management)).

A bot score is a value that ranges from 1 (a bot) to 99 (a human). The CAPTCHA page displays a 403 status code if this is triggered.

## Something has gone wrong, what do I do?

If you care experiencing issues, contact [Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850).