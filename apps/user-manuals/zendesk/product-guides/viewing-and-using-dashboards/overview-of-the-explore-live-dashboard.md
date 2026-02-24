# Overview of the Explore live dashboard

Source: https://support.zendesk.com/hc/en-us/articles/4408843771546-Overview-of-the-Explore-live-dashboard

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

Note: If you’re on a Professional plan, the prebuilt live dashboard is read-only. You can’t [clone](https://support.zendesk.com/hc/en-us/articles/4408821374362), [export](https://support.zendesk.com/hc/en-us/articles/4483481898266), [schedule](https://support.zendesk.com/hc/en-us/articles/4408843602714), or [drill into](https://support.zendesk.com/hc/en-us/articles/4422485166746) the prebuilt live dashboard, nor can you [build custom live dashboards](https://support.zendesk.com/hc/en-us/articles/4408846742042). However, on Professional plans, you can [share](https://support.zendesk.com/hc/en-us/articles/4408827282714) the live dashboard. Customers on the [Explore Legacy plan](https://support.zendesk.com/hc/en-us/articles/4408823356186#topic_pf2_35r_smb) do not have access to the live dashboard.

Explore features a prebuilt live dashboard that displays important information about your Zendesk products in real time, in one place. If you're on an Enterprise plan, this dashboard behaves like any other Explore dashboard in that you can [share it](https://support.zendesk.com/hc/en-us/articles/4408827282714), [schedule it](https://support.zendesk.com/hc/en-us/articles/4408843602714), or [clone it](https://support.zendesk.com/hc/en-us/articles/4408821374362) to [make your own customized version](https://support.zendesk.com/hc/en-us/articles/4408846742042). If you're on a Professional plan, the dashboard is read-only, but you can share it.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_ent_live_dash_1_updated.png)

Tip: Zendesk now offers [real-time monitoring](https://support.zendesk.com/hc/en-us/articles/9757124462234), which enhances your reporting by focusing on use cases, offering immediate decision-making insights, and tracking trends for up to seven days.

The live dashboard itself requires at least Suite Professional. If you don't have Suite Professional, but are a Support Professional customer with Explore Professional, the data within the dashboard requires additional product versions. If you don't have a Professional plan for a particular product, it won't be displayed in the dashboard.

Additionally, the name of the live dashboard in the Dashboard library depends on whether you use live chat or messaging:

- **Live data**: Name of the live dashboard if you use neither live chat nor messaging. Includes the Support and Talk sections.
- **Live data (including Chat)**: Name of the dashboard if you use live chat.
 Includes the Support, Talk, and Chat sections, but not the Messaging section.
- **Live data (including Messaging)**: Name of the dashboard if you use messaging.
 Includes the Support, Talk, and Messaging sections, but not the Chat section.

 Note: If you recently turned on messaging, you might not see this dashboard yet. See [Why don’t I see the Live data (including Messaging) dashboard?](https://support.zendesk.com/hc/en-us/articles/6096510202394) for details.

If your account was created before November 3, 2021 and you migrated from chat to messaging, you’ll see both dashboards in the Dashboard library.

Tip: The dashboard displays data in near real time, but its update interval might be affected by other factors like network speed and ticket volume. For information about how often Explore refreshes data, see [Data refresh intervals for Explore reporting](https://support.zendesk.com/hc/en-us/articles/4408823242778).

This article contains the following topics:

- [Accessing the live dashboard](#topic_mlm_hkp_5mb)
- [Messaging reports](#topic_iqf_vfv_fvb)
- [Chat reports](#topic_yjc_jty_q3b)
- [Voice reports](#topic_l23_vty_q3b)
- [Support reports](#topic_cxj_vty_q3b)

Related articles:

- [Overview of the Explore live performance data by channel dashboard](https://support.zendesk.com/hc/en-us/articles/7431948845082)
- [Overview of the omnichannel routing queues live monitoring dashboard](https://support.zendesk.com/hc/en-us/articles/7568858834202)

## Accessing the live dashboard

**To access the live dashboard**

1. In Explore, click the **Dashboard** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dashboard_icon.png)) in the left sidebar.
2. From the list of dashboards, select the **Live data** dashboard.

   If you use live chat, select **Live data (including Chat)**. If you use messaging, select **Live data (including Messaging)**. If you use both, select whichever option you want to view metrics for.

## Support reports

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_ent_live_dash_support_updated.png)

The **Support** section of the real-time dashboard displays the following information:

- **New tickets (30 min)**: The number of tickets that changed to **New** status in the last 30 minutes.
- **Open tickets (30 min)**: The number of tickets that changed to an **Open** status in the last 30 minutes.
- **Tickets created and solved per hour**: (Non-live data) A chart showing the number of tickets created (column) and solved (line) each hour for the last 8 hours. This report is based on historical data that syncs once per hour.
 Depending on when you load the dashboard and when the sync occurs, you might not see data for the past hour. For details, see [Data refresh intervals for Explore reporting](https://support.zendesk.com/hc/en-us/articles/4408823242778).
- **Agents online**: The number of agents who are online and available to work tickets. If you're on an Enterprise plan, click this metric to drill into specific information about agent status and current tickets. For more information, see [Seeing live agent status and activities](https://support.zendesk.com/hc/en-us/articles/4422485166746).
- **Agents offline**: The number of agents who are offline and unavailable to work tickets. If you're on an Enterprise plan, click this metric to drill into specific information about agent status. For more information, see [Seeing live agent status and activities](https://support.zendesk.com/hc/en-us/articles/4422485166746).
- **Solved tickets (30 min)**: The number of tickets that changed to a **Solved** status in the last 30 minutes.
- **Satisfaction (today)**: The percentage of customers who rated a ticket as "Good" today. The number below the satisfaction percentage indicates the change in satisfaction since yesterday. A negative result indicates a drop in customer satisfaction which you might need to investigate.

You can filter the reports in the **Support** section by **Ticket group** or **Ticket brand**. You can select up to five attribute values for each filter.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_live_dashboard_multi-filter.png)

Important: To get the most value out of this dashboard, remind your agents to sign in and out of Zendesk to accurately represent their shifts. This is particularly important for the Support channel, where only two agent states are reported (Online and Offline). If agents don’t sign out, Explore will show them as always online.

## Voice reports

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_ent_live_dash_talk_updated.png)

The **Voice** section of the real-time dashboard displays the following information:

- **Calls in queue**: The number of calls in the queue.
- **Ongoing calls**: The number of currently connected calls.
- **Calls started and completed per hour**: (Non-live data) A chart showing the number of calls started (column) and completed (line) each hour for the last 8 hours. This report is based on historical data that syncs once per hour.
 Depending on when you load the dashboard and when the sync occurs, you might not see data for the past hour. For details, see [Data refresh intervals for Explore reporting](https://support.zendesk.com/hc/en-us/articles/4408823242778).
- **Agents online**: The number of agents who are online and available to take calls. This includes agents who are in a wrap-up state from a previous call. If you're on an Enterprise plan, click this metric to drill into specific information about agent status. For more information, see [Seeing live agent status and activities](https://support.zendesk.com/hc/en-us/articles/4422485166746).
- **Agents offline:** The number of agents who are offline and unavailable to take calls. If you're on an Enterprise plan, click this metric to drill into specific information about agent status. For more information, see [Seeing live agent status and activities](https://support.zendesk.com/hc/en-us/articles/4422485166746).
- **Average wait time**: The average time customers wait for their call to be answered.
- **Longest wait time**: The maximum time a customer waited for their call to be answered.

The wait time metrics are refreshed each time a new call is answered.

You can filter the reports in the **Voice** section by **Call group**. You can select up to five attribute values for each filter.

Note: You might sometimes see differences in results between the Explore live dashboard and the live calls dashboard. To learn why these can occur, see [Discrepancies between the live calls dashboard and the Explore Enterprise live dashboard](https://support.zendesk.com/hc/en-us/articles/4408828509210).

## Messaging reports

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_ent_live_dash_messaging_updated-new.png)

The **Messaging** section of the real-time dashboard displays the following information:

- **Active conversations in queue**: The number of active conversations that have not yet been answered by an agent.
- **Active assigned conversations**: The number of conversations being addressed by an agent.
- **Inactive conversations in the queue**: Unassigned conversations without a reply from the end user for 10 minutes.
- **Inactive assigned conversations**: Assigned conversations without a reply from the end user for 10 minutes.

 Note: There are differences in how we count towards Inactive conversations for customers participating in the [Conversation Inactivity Timer beta](https://support.zendesk.com/hc/en-us/community/posts/6048030564250). Learn more in [Live data widgets for Explore dashboards](https://support.zendesk.com/hc/en-us/articles/4408843357210#topic_mq4_yxb_n4b).
- **Average concurrency:** The average number of conversations assigned to agents whose status is Online.
- **Average and longest requester wait time**: The average and longest time end users are waiting for an agent’s response across all active conversations only.
- **Average and longest handle time**: The average and longest time that an agent has spent interacting with an end user across all active conversations only. Learn more about when the counter resets for live reporting in [How is the Handle time metric calculated?](https://support.zendesk.com/hc/en-us/articles/5940001113754)
- **Agents online**: The number of agents who are online and available to work on conversations. If you're on an Enterprise plan, click this metric to drill into specific information about agent status and current chats. For more information, see [Seeing live agent status and activities](https://support.zendesk.com/hc/en-us/articles/4422485166746).
- **Agents away**: The number of agents who are away and not available to work on conversations. If you're on an Enterprise plan, click this metric to drill into specific information about agent status. For more information, see [Seeing live agent status and activities](https://support.zendesk.com/hc/en-us/articles/4422485166746).
- **Satisfaction (today)**: The percentage of customers who rated a conversation as "Good" in the last 30 minutes. The number below the satisfaction percentage indicates the change in satisfaction since the previous 30 minutes. A negative result indicates a drop in customer satisfaction which you might need to investigate.
- **Average time in queue for active conversations**:
 The average time customers wait for their conversation request to be answered by an agent.
- **Longest time in queue**: The maximum time a customer waited for their chat request to be answered by an agent.
- **Tickets created and solved per hour**: (Non-live data) A chart showing the number of conversations started (column) and completed (line) each hour for the last 8 hours. This report is based on historical data that syncs once per hour.
 Depending on when you load the dashboard and when the sync occurs, you might not see data for the past hour. For details, see [Data refresh intervals for Explore reporting](https://support.zendesk.com/hc/en-us/articles/4408823242778).

The wait time metrics are refreshed each time a new conversation request is answered.

You can filter the reports in the **Messaging** section by **Group** or **Channel**. You can select up to five attribute values for each filter.

When you activate a new social channel, refresh your browser to ensure that new tickets created from that channel are reflected on the dashboard.

If there has been no activity in any channel for seven days, channel values no longer appear in the filter drop-down. When tickets are created from any channel again, refresh your browser to see the channel values in the filter drop-down.

Note: The messaging metrics in this section calculate values using only the 1000 most recently updated New or Open tickets. To get the most value out of this dashboard, move messaging tickets into On-Hold, Pending, or Solved as needed to best reflect their status and more accurately evaluate your agents’ incoming and currently assigned workloads.

## Chat reports

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_ent_live_dash_chat_updated.png)

The **Chat** section of the real-time dashboard displays the following information:

- **Active chats**: The number of currently connected chats.
- **Chats in queue**: The number of chats in the queue.
- **Chats started and completed per hour**: (Non-live data) A chart showing the number of chats started (column) and completed (line) each hour for the last 8 hours. This report is based on historical data that syncs once per hour.
 Depending on when you load the dashboard and when the sync occurs, you might not see data for the past hour. For details, see [Data refresh intervals for Explore reporting](https://support.zendesk.com/hc/en-us/articles/4408823242778).
- **Agents online**: The number of agents who are online and available to chat.
 If you're on an Enterprise plan, click this metric to drill into specific information about agent status and current chats. For more information, see [Seeing live agent status and activities](https://support.zendesk.com/hc/en-us/articles/4422485166746).
- **Agents away**: The number of agents who are away and not available to chat.
 If you're on an Enterprise plan, click this metric to drill into specific information about agent status. For more information, see [Seeing live agent status and activities](https://support.zendesk.com/hc/en-us/articles/4422485166746).
- **Satisfaction (30 min)**: The percentage of customers who rated a chat as "Good" in the last 30 minutes. The number below the satisfaction percentage indicates the change in satisfaction since the previous 30 minutes. A negative result indicates a drop in customer satisfaction which you might need to investigate.
- **Average wait time**: The average time customers wait for their chat request to be answered.
- **Longest reply time**: The maximum time a customer waited for their chat request to be answered.

The wait time metrics are refreshed each time a new chat request is answered.

You can filter the reports in the **Chat** section by **Department**. You can select up to five attribute values for each filter.