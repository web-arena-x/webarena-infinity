# Proactive messaging conditions and events reference

Source: https://support.zendesk.com/hc/en-us/articles/5511218058650-Proactive-messaging-conditions-and-events-reference

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

Conditional statements define the actions that trigger a proactive message for a user, and when those actions should be evaluated.

Conditional statements for proactive messaging follow this basic configuration:

- An **object** is selected for evaluation.
- A **condition** is created for that object. The condition consists of a condition field, an operator, and a value.
- An **event** is created that defines when the conditonal statement is checked.

This article includes the following sections:

- [Objects](#topic_ad3_n15_wwb)
- [Conditions](#topic_vvc_hk5_wwb)
- [Events](#topic_sws_bp5_wwb)
- [Key points](#topic_avf_rgy_wwb)

## Objects

Choose from the objects in the table below to begin building a condition. The type of object you select determines what [condition fields](#topic_vvc_hk5_wwb) you can choose.

| Object | Description |
| --- | --- |
| Visitor | A customer, or end user, visiting your channel. Selecting this object allows you to look at the location of the customer, or their visit history. |
| Device | The computer or mobile device used to access your channel. Selecting this object allows you to evaluate the device's language settings in the condition. |

## Conditions

Choose from the condition fields in the table below to complete your condition.

| Condition field | Object | Description | Operators | Value |
| --- | --- | --- | --- | --- |
| Page URL | Visitor | The URL of a web page, or screen name on a mobile device, the customer is currently on. The Page URL string is case insensitive. | Contains at least one of Doesn't contain Is Is not | `String` Enter all or part of the page or screen URL to be matched. |
| Page title | Visitor | The title of the web page or mobile device screen the customer is currently on. The Page title string is case insensitive. | Contains at least one of Doesn't contain Is Is not | `String` Enter all or part of the page or screen title to be matched. |
| Visit history | Visitor | Customer visit history – are they coming to the website or app for the first time, or have they visited before? | Is | `Drop-down` Select **New user** or **Returning user**. |
| Language | Device | Language or locale of the customer, as determined by the device's language settings. | Is Is not | `Drop-down` Select the language being matched or skipped. |

## Events

Choose from the events in the table below to define when the conditions should be checked.

| Event | Description |
| --- | --- |
| Visitor loads the page | Checks for the conditions on page load. |
| Visitor is on the page | Checks for the conditions when a customer spends a set amount of time on the page. |

## Key points

- Admins can create proactive messages with multiple conditions using AND or OR operators, and can create nested conditions.
- As an admin if you are planning to use two conditions or less you cannot use nested conditions.