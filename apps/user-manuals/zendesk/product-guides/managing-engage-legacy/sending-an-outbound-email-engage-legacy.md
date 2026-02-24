# Sending an Outbound Email (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731467027610-Sending-an-Outbound-Email-Engage-Legacy

---

Outbound email for Engage has been specifically designed to address the needs of agents when communicating with customers outside of current contacts. This includes the ability to add attachments, use snippets, reply to existing threads, manage customer profiles more efficiently, and use generative AI via Engage’s Smart Tools, to assist our customer service personnel in writing outgoing emails more effectively.

The aim of this feature is to allow agents to email new customers outside of an active call.  
**Key Benefits Include:**

- Ability for agents to start new email contacts with an easy-to-use interface.
- Standardised approach by using Utilities.
- Attachments and snippets support for outbound emails.
- Capability to reply to existing threads, maintaining context for the customer.
- Integration of customer profile lookup or creation during the email composition process.
- Give customer support representatives access to generative AI's email composition capabilities by using Engage’s Smart Tools.

**Prerequisites**

- Amazon Simple Email Services (SES) being configured correctly
- New Slate email editor

Please note that the cost of sending out an outbound email is 2 units, which is 1 unit more than a standard email reply

## Implementation Steps

Setting up the outbound email functionality follows the same basic configuration as creating any Utility type in Engage. Outbound emails are triggered via a Utility, therefore making it easy to use as all agents are currently using Utilities for various tasks.

Skip steps 2 to 4 if you want to send an outbound email to an existing profile.

1. Select the profile search icon within Engage and the search window will be displayed.
2. Click the "Create new profile" button. The profile creation form will be displayed.
3. To create a new profile, enter the mandatory form information, which includes the email address of the new contact to whom you intend to deliver an outbound email.
4. The "Create" button will generate a new profile containing the email address that will be used to communicate with the consumer.
5. To send an email to a contact, use their entire name to look them up in the profile search window.
6. After selecting the desired profile, the "Outbound Email" utility icon will become available in the center and right panel along with the profile's details.
7. When you click on the icon, the email editor will open, allowing you to email the newly created contact.
8. Incorporate all pertinent email information that you wish to include, such as CC, BCC, Snippets, Signatures, Attachments, and Smart Tools.
9. Click the "Send email" button once the email you wish to send is completed.
10. Upon sending the message, a notification will appear to validate the successful delivery of the email.
11. Emails sent successfully may be seen in the client's contact history, which includes all of the correspondence between the customer and the agent.
12. An agent will be able link an outgoing email to a Case that may be active for a customer. To do so, simply select an case from the dropdown list found below the email editor, label "Assign to a Case".  
    [.callout-critical]Please note that the TO: address should only contain the email address linked to the customer profile. But you can add more than one email address to the CC and BCC.[.callout-critical]

![__wf_reserved_inherit](https://support.zendesk.com/hc/article_attachments/9731450521370)

![__wf_reserved_inherit](https://support.zendesk.com/hc/article_attachments/9731475898010)

![__wf_reserved_inherit](https://support.zendesk.com/hc/article_attachments/9731450559130)

![__wf_reserved_inherit](https://support.zendesk.com/hc/article_attachments/9731467114138)