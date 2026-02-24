# SMS Routing (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731450587802-SMS-Routing-Engage-Legacy

---

Local Measure Engage provides full SMS routing capabilities for Amazon Connect. A key benefit is that all messages are routed via Amazon Connect - and not brought into the agent desktop on the side - which means that all queue and agents reports are also available for the SMS channel.

## Attributes and handling mailboxes

Text messages (SMS) are routed as CHAT messages in Amazon Connect, so agents must be skilled for the CHAT channel in order to handle emails.

Once your SMS channel has been setup, SMS can be routed via Amazon Connect. To complete this configuration, the following steps need to be taken:

- Implement contact flow to route text messages
- Ensure that agents have the correct queue in the routing profile and that they are enabled for the SMS channel in that queue.

The below table defined attributes which the Local Measure solution adds to SMS contacts, which can be used as part of the routing logic in the contact flow:

| User Defined Attribute | Value | Description |
| --- | --- | --- |
| user\_type | sms | Indicates messaging platform |
| PhoneNumber | variable | Customer’s phone number |
| \_hidden\_contact\_origin | variable | Customer’s phone number |
| \_hidden\_contact\_destination | variable | Contact Center phone number |
| phone | variable | Customer’s phone number |

The following figures demonstrate the process of identifying SMS contacts (first figure), directing them to a designated contact flow, and placing them in queues (second figure):

![](https://support.zendesk.com/hc/article_attachments/9731467131418)

SMS Contact Identification

![](https://support.zendesk.com/hc/article_attachments/9731499977754)

SMS Contact Queue Placement

‍