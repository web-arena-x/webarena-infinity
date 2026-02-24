# Email: Attributes and Handling Mailboxes (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731498758298-Email-Attributes-and-Handling-Mailboxes-Engage-Legacy

---

Local Measure Engage provides full email routing capabilities for Amazon Connect. A key benefit is that all emails are routed via Amazon Connect - and not brought into the agent desktop on the side - which means that all queue and agents reports are also available for the email channel.

Prerequisites

- Amazon Simple Email Services (SES) being configured correctly
- The Local Measure Engage CloudFormation stack having been deployed with the required information specified
- A Distribution flow having been specified in Local Measure Engage

## Email routing

Two key aspects of email routing:

1. Emails are routed as CHAT messages in Amazon Connect, so agents must be skilled for the CHAT channel in order to handle emails. [.callout-critical--alert-message]It must be noted that chat sessions can last for a maximum of 7 days, so email must be delivered to an agent within 7 days of being queued. After 7 days the email will be terminated by Amazon Connect if not yet delivered to and handled by an agent. [.callout-critical--alert-message]
2. 'Play prompt' blocks should never be included in Contact Flows for email. Any attempt to play a message to an email will result in a lost email. This includes the 'customer queue flow' which is often used to play comfort messages or music on hold. It is important to either specify a customer queue flow that does not play prompts at all, or to add logic to the existing customer queue flow to check the channel before playing prompts. [.callout-critical--alert-message]The Contact Flow for email should **NEVER** contain a 'Play prompt' block. [.callout-critical--alert-message]

Once the above prerequisites are in place, email can be routed via Amazon Connect.

## Configuration

To complete the configuration, the following steps need to be taken:

- Implement contact flow to route email
- Ensure that agents have the correct queue in the routing profile and that they are enabled for the CHAT channel in that queue.

The below table defined attributes which the Local Measure solution adds to Email contacts, which can be used as part of the routing logic in the contact flow:

| User Defined Attribute | Value | Description |
| --- | --- | --- |
| user\_type | ses | Used to identify email contacts |
| \_hidden\_contact\_origin | variable | Contains the email address the email was sent from |
| \_hidden\_contact\_destination | variable | The email address the email was sent to |
| subject | variable | The subject or the email |
| EmailAddress | variable | Customer’s email address |

Local Measure recommends setting the following two contact attributes to ensure that agents can see the ‘To’ and ‘Subject’ fields with Engage:

| User Defined Contact Attribute | Type | Key |
| --- | --- | --- |
| agt\_To | Dynamic | \_hidden\_contact\_destination |
| agt\_Subject | Dynamic | subject |

The below figure illustrates how this would look in the contact flow:

![](https://support.zendesk.com/hc/article_attachments/9731462282522)

‍

‍