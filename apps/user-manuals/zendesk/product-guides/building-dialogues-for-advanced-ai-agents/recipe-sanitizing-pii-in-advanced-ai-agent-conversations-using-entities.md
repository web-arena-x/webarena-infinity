# Recipe: Sanitizing PII in advanced AI agent conversations using entities

Source: https://support.zendesk.com/hc/en-us/articles/8357749756442-Recipe-Sanitizing-PII-in-advanced-AI-agent-conversations-using-entities

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

Common personally identifiable information (PII) can be identified and sanitized before imported to the AI agents - Advanced database. The sanitization is applied according to *GDPR compliancy* to sanitize any *Personal Identifiable Information (PII) data*. [Learn more](https://support.zendesk.com/hc/en-us/articles/8357751648666 "https://support.ultimate.ai/hc/en-us/articles/360020109699").

Every advanced AI agent comes with the presets below:

- IBANs
- Emails
- Credit cards
- US Social Security Number
- Personal identity code (Austrian, Chilean, Danish, Estonian, Finnish, French, Icelandic, Italian, Latvian, Norwegian, Polish, Romanian, Slovakian, Spanish, Swedish, Swiss)

## Examples

- Our model detects "[info@ultimate.ai](mailto:info@ultimate.ai "mailto:info@ultimate.ai")" in a chat text where the customer would like to reset their account password and classify it as an "Email" named entity. The detected Email is then used in the context of the conversation to email the customer a password reset link.
- Our model detects "Berlin" in a chat text where the customer asks about your branches in Berlin and classify it as a "City" named entity. The detected city is then used in the context of the conversation to provide the customer with information about your active branches in Berlin.
- A customer asks about their "order number 736513" status. Our model detects that "736513" is the customer's order number and categorizes it as an entity named "**Order** **Number**". The detected order number is then used in the context of the conversation to provide the customer with useful information about their order.

## How to set this up

To ensure historical conversation data is sanitized, follow the steps below:

1. [Create an entity](https://support.zendesk.com/hc/en-us/articles/8357749740698)
2. [Import historical data](https://support.ultimate.ai/hc/en-us/sections/360005783079-Data-import)