# Turning on reply time SLAs for live chat

Source: https://support.zendesk.com/hc/en-us/articles/6670155267994-Turning-on-reply-time-SLAs-for-live-chat

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

You must have the [Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930) to reply time SLAs for live chat.

A service level agreement ([SLA](https://support.zendesk.com/hc/en-us/articles/5600997516058)) is a policy you define that
specifies and measures the reply and resolution times that your Chat agents
deliver to your customers.You can configure live chat to record the First reply
time and Next reply time in a conversation, and then use the data in your SLAs.
The [reply time metrics](https://support.zendesk.com/hc/en-us/articles/4408821871642) help you understand
how quickly your team is responding to customers and can be [analyzed in Explore](https://support.zendesk.com/hc/en-us/articles/4408835846810#topic_d5h_ybj_z3b).

For live chat, reply time SLAs is turned off by default. Agent reply times are
measured after the live chat conversation ends and a ticket is created from that
exchange. The agent’s public replies to the ticket are used to calculate reply
times.

When the Reply time SLAs setting for live chat is turned *on*,
all agent responses in a live chat conversation as well as public agent replies to
the ticket created from that conversation, are used to calculate reply times.

When using live chat conversations, consider the following:

- Responses sent via triggers are excluded from the First reply and
  Next reply time SLA calculations.
- Responses sent via Chat Conversations API are counted towards
  First reply and Next reply time SLAs. Agent replies on the ticket generated
  from the chat conversation are included in the calculations.
- SLA reporting for live chat conversations is available in Explore
  as part of the SLA reports for Support. It isn’t part of the Chat prebuilt
  dashboard.

**To turn on reply time SLAs for live chat**

1. In your Chat dashboard, go to **Settings > Account**.
2. Click the **SLAs** tab.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_SLA_tab.png)
3. Set **Reply time SLAs for live chat** to **On**.
4. Click **Save**.