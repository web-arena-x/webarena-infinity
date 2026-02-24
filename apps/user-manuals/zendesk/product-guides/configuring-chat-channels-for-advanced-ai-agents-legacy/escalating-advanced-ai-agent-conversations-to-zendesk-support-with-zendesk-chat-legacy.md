# Escalating advanced AI agent conversations to Zendesk Support with Zendesk Chat (Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/8357765400986-Escalating-advanced-AI-agent-conversations-to-Zendesk-Support-with-Zendesk-Chat-Legacy

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

Configuring chat channels for advanced AI agents is no longer recommended.
Instead, consider [configuring messaging channels](https://support.zendesk.com/hc/en-us/sections/8264312886554) or [configuring email channels](https://support.zendesk.com/hc/en-us/sections/8264365933210).

To escalate chats that require further assistance from human agents but not immediate attention, the best approach is to utilize [Zendesk tags](../business-rules/about-tags.md) and setup custom escalation in Dialogue Builder in the AI agents - Advanced Dashboard.

There are simple three steps to achieve this.

1. [Turn automatic ticket creation on in Zendesk Chat](#h_01FPD06B138JKNAC7JMPF8TV2T "https://ultimateai.atlassian.net/wiki/spaces/CS/pages/2108949476/Ticket+email+escalation+in+Zendesk+Chat#1.-Turning-automatic-ticket-creation-on")
2. [Set escalation block to Custom Escalation in Dialogue Builder](https://ultimateai.atlassian.net/wiki/spaces/CS/pages/2108949476/Ticket+email+escalation+in+Zendesk+Chat#2.-Setting-escalation-block "https://ultimateai.atlassian.net/wiki/spaces/CS/pages/2108949476/Ticket+email+escalation+in+Zendesk+Chat#2.-Setting-escalation-block")
3. [Test](#h_01FPD20G89482YM28CM3F8FZVM "https://ultimateai.atlassian.net/wiki/spaces/CS/pages/2108949476/Ticket+email+escalation+in+Zendesk+Chat#3.-Managing-tickets-in-Zendesk-Support")
4. [Manage tickets in Zendesk Support](#h_01FPD20A60S0KBYHWK20ZC25JQ)

## Step 1: Turn automatic ticket creation on in Zendesk Chat

By turning this on, every chat will be converted into a ticket and becomes
easily manageable in Zendesk Support.
[Learn more](https://support.zendesk.com/hc/en-us/articles/4408820938138-Setting-up-Zendesk-Chat-in-Zendesk-Support#topic_rll_qgq_sgb).

1. Go to **Zendesk Chat** >
   **Settings** > **Account**
   >
   **Zendesk Support (tab)**
2. Under **Ticket creation - chats**,
   configure the settings as the example below:![zendesk_chat_ticket_creation_setting.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_zendesk_chat_ticket_creation_setting.png)

## Step 2: Set escalation block to Custom Escalation in Dialogue Builder

![custom_escalation_block.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_custom_escalation_block.png)

Since every chat is converted to a ticket automatically, it is crucial to
add tags automatically for easy management in Zendesk Support.

To do so:

1. In the
   AI agents - Advanced
   Dashboard, locate the dialogue path for ticket escalation
2. Add an escalation block
3. Set the method to **Custom Escalation**

#### Custom Escalation doesn't actually escalate to an endpoint. It acts as a way to add a label for analytics purposes to mark escalation traffic to another location, such as webform, hotline.

Add two actions to the escalation block:

- - Add tag - this adds a tag to the ticket in Zendesk Support
  - Add label - this adds the tag in Conversation Logs in the
    AI agents - Advanced
    Dashboard

![custom_escalation_block_actions.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_custom_escalation_block_actions.png)

We suggest to add a generic tag, “ticket\_escalation” to view all escalated
tickets, and an intent/topic specific one like “payment\_refund”.

## Step 3: Test

Finally, after all is set up. Test it and see if everything matches the workflow/process of your customer support team. Monitor how this is working for your team. Add actions to add more tags or adjust the escalation flow to collect more information prior to escalation to adopt to the team and reduce average handling time. 

## Step 4: Manage tickets in Zendesk Support

✅  Success - Start managing tickets in Zendesk Support!

Tags is a powerful tool to manage tickets in Zendesk Support. To lear more,
have a look at:

- [About Tags](https://support.zendesk.com/hc/en-us/articles/4408888664474-About-tags "https://support.zendesk.com/hc/en-us/articles/4408888664474-About-tags")
- [Working with ticket tags](https://support.zendesk.com/hc/en-us/articles/4408835059482-Working-with-ticket-tags "https://support.zendesk.com/hc/en-us/articles/4408835059482-Working-with-ticket-tags")

![](blob:https://ultimateai.atlassian.net/d0b1d901-b1de-416b-a118-690db6809c14#media-blob-url=true&id=33640b6d-0c97-4c92-b020-e38abf4fc2e4&collection=contentId-2108949476&contextId=2108949476&mimeType=image%2Fpng&name=image-20211115-073643.png&size=14711&height=241&width=233&alt=)