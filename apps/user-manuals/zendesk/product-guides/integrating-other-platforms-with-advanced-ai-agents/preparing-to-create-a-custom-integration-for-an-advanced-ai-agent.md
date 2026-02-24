# Preparing to create a custom integration for an advanced AI agent

Source: https://support.zendesk.com/hc/en-us/articles/8357756827674-Preparing-to-create-a-custom-integration-for-an-advanced-AI-agent

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

## What is a custom integration?

A custom integration is an API connection to your own or a different backend system, used to enrich the data within a conversation for customization, personalization and/or automation purposes.

Example API 1: getOrder

- An end-user triggers a “where is my order” type intent. Their {{email}} is automatically passed from your CRM to the integration, we look up their past data in your backend and a carousel of their past orders is generated so the end-user can easily choose the order they’d like to know more about.
- Once selected, the AI agent outputs the chosen order’s last known {{status}} and {{trackingLink}}.

Example API 2: updateAddress

- An end-user triggers a “change my address” type intent. They provide their {{email}} and {{orderReference}} as authentication as well as their updated address details - the correct input format is validated through entities.
- The new address is updated in your backend system.

## Integration technical requirements

Available in another [article here](https://support.zendesk.com/hc/en-us/articles/8357749781274).

## Reading list

To get the most out of your custom integration, the team should be familiar with the conversation design features listed below:

- [Conditional blocks](https://support.zendesk.com/hc/en-us/articles/8357733406234)
- [Entities](https://support.zendesk.com/hc/en-us/articles/8357749740698)
- [Actions](https://support.zendesk.com/hc/en-us/articles/8357756651290-Actions-and-Events-explained)