# Best practices for creating CRM actions for advanced AI agents in Zendesk Chat (Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/8357720370330-Best-practices-for-creating-CRM-actions-for-advanced-AI-agents-in-Zendesk-Chat-Legacy

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

Configuring chat channels for advanced AI agents is no longer recommended. Instead, consider [configuring messaging channels](https://support.zendesk.com/hc/en-us/sections/8264312886554) or [configuring email channels](https://support.zendesk.com/hc/en-us/sections/8264365933210).

The examples you'll see in this article are perfect for you if ticket creation is set to automatic in Zendesk Chat. Find out more under "Configuring ticket creation options" [here](https://support.zendesk.com/hc/en-us/articles/203661666-Setting-up-Zendesk-Chat-in-Zendesk-Support#topic_rll_qgq_sgb).

Related articles:

- [Actions and Events Explained](https://support.zendesk.com/hc/en-us/articles/8357756651290)
- [Actions Overview - Zendesk Chat](https://support.zendesk.com/hc/en-us/articles/8357750804250)

## Get visitor info for personalized conversations

This allows you to create reply variation
based on location or device to personalized
your copy.

Set this at the AI agent level by going to
**Settings > Actions** then
click **+ New Action**.
Set the fields as below:

![mceclip1.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_mceclip1_eWaGn.png)

If your pre-chat form is enabled and
email is mandatory, the emails entered
there is saved to Zendesk Chat when chat
visitor requests to chat. Utilize this
by using
[conditional blocks](https://support.zendesk.com/hc/en-us/articles/8357733406234)
to avoid asking for the same information
over and over again.

## Create a smart welcome reply

By setting up a welcome reply in the AI agents -
Advanced Dashboard, you will be able to give options
to chat visitors at the very beginning of the conversation
and create a more personalized flow for them. for
example, use
[conditional blocks](https://support.zendesk.com/hc/en-us/articles/8357733406234)
in your welcome reply to greet your customers 
in different languages based on their location.

To use this instead of the
[First Reply trigger in Zendesk Chat](https://support.zendesk.com/hc/en-us/articles/360051545773-What-default-Chat-triggers-come-with-Zendesk-#h_01ECR0502DPWXFFA49GQZB7JYW),
set the action "Trigger reply" at the AI agent level
by going to **Settings > Actions**
then click **+ New Action**. Set
the fields as below:

![Screen_Shot_2021-10-06_at_11.52.58.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_Screen_Shot_2021-10-06_at_11.52.58.png)

## Add tag to all chats coming from the AI agent

Tagging all chats coming from the AI agent helps
you manage your tickets in Zendesk.

Set this up at the AI agent level by going to
**Settings > Actions** then click **+ New Action**.
Set the fields as below:

**![mceclip0.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_mceclip0_OMQH9.png)**

## Add tag to conversations with intent topics

Set this up at content level by locating the
escalation block(s) in the intent that you wish to
add the topic tag to. Select the escalation block(s)
and click **Add / Edit Actions**, in
the drawer on the right.

In the example below, "order\_status" is used as the
topic of the intent, but you can enter anything you
want in the value that would help your agents manage
tickets easier.

![Screen_Shot_2021-10-06_at_11.21.50.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_Screen_Shot_2021-10-06_at_11.21.50.png)

### Adding tags to Conversation Logs

Simply add another action but select
*Conversation Document (Session)* as the target.

![mceclip0.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_mceclip0_zCpcK.png)

You should see two actions like this now:

![Screen_Shot_2021-10-06_at_11.26.10.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_Screen_Shot_2021-10-06_at_11.26.10.png)

## Show queue position to chat visitor

Set this up at the AI agent level by going to
**Settings > Actions** then click **+ New Action**.
Set the fields as below:

![Screen_Shot_2021-10-06_at_11.35.35.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_Screen_Shot_2021-10-06_at_11.35.35.png)

This way, the chat between the user and the AI agent
ends as the AI agent leaves the chat. User sees their
queue position like this:

![Screen_Shot_2021-10-06_at_11.41.47.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_Screen_Shot_2021-10-06_at_11.41.47.png)