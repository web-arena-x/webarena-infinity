# Automatically routing tickets from advanced AI agents to human agents

Source: https://support.zendesk.com/hc/en-us/articles/8357734509466-Automatically-routing-tickets-from-advanced-AI-agents-to-human-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

Automatically routing or assigning tickets to agents can save you and your team time. This can be easily achieved by adding the Update Ticket Info action in our Dashboard. This article shows you how to set it up in your email AI agent.

First, obtain the assignee ID of the agent you'd like to assign the ticket to. Read [this](https://support.zendesk.com/hc/en-us/articles/8357765446554) if you don't know how to.

Second, go to the email AI agent in our dashboard by selecting it in the top right corner.

- Go to **Content > Intents**
- Select the intent that you would like to have the tickets be assigned to automatically
- Click the pencil icon > **Go To Detail Page > Actions**
- Click **+ New Action**, and set the three fields below as follow:
 - Target: Zendesk Support
 - Action: Update Ticket Info
 - Assignee ID: Enter the assignee ID from Zendesk Support

These three are mandatory in this use case but feel free to update other fields by selecting the dropdown menu. In the example below I would also like to set the **Type** to be `task`, **Priority** to be `high`, and **Status** to be `new`.

![mceclip1.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_mceclip1_f5brP.png)

Here's what the result looks like in Zendesk Support:

![mceclip0.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_mceclip0_lCbtW.png)