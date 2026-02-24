# Overview of the Explore live performance by channel dashboard

Source: https://support.zendesk.com/hc/en-us/articles/7431948845082-Overview-of-the-Explore-live-performance-by-channel-dashboard

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

Note: If you’re on a Professional plan, the prebuilt live performance dashboard is read-only. You can’t [share](https://support.zendesk.com/hc/en-us/articles/4408827282714), [clone](https://support.zendesk.com/hc/en-us/articles/4408821374362), [export](https://support.zendesk.com/hc/en-us/articles/4483481898266), [schedule](https://support.zendesk.com/hc/en-us/articles/4408843602714), or [drill into](https://support.zendesk.com/hc/en-us/articles/4422485166746) the prebuilt live performance dashboard, nor can you build custom live dashboards. Customers on the Explore Legacy plan do not have access to the live performance dashboard.

Explore features a prebuilt **Live performance by channel** dashboard that displays important information about your Zendesk products in real time, including agent status and other activity.
This dashboard is similar to the [Explore live dashboard](https://support.zendesk.com/hc/en-us/articles/4408843771546), except information is split out into different tabs, allowing you to focus on each channel individually.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_live_performance_by_channel_dashboard.png)

The live performance dashboard itself requires a Professional plan or higher, but the data within the dashboard may require additional product plans. If you don't have a particular product, it won't be displayed in the dashboard.

The dashboard displays data in near real time, but its update interval might be affected by other factors like network speed and ticket volume. For information about how often Explore refreshes data, see [Data refresh intervals for Explore reporting](https://support.zendesk.com/hc/en-us/articles/4408823242778).

Tip: Zendesk now offers [real-time monitoring](https://support.zendesk.com/hc/en-us/articles/9757124462234), which enhances your reporting by focusing on use cases, offering immediate decision-making insights, and tracking trends for up to seven days.

This article contains the following topics:

- [Accessing the live performance dashboard](#topic_pzs_4cn_zbc)
- [Understanding the live performance dashboard reports](#topic_qjs_pcn_zbc)

Related articles:

- [Overview of the Explore live dashboard](https://support.zendesk.com/hc/en-us/articles/4408843771546)
- [Overview of the omnichannel routing queues live monitoring dashboard](https://support.zendesk.com/hc/en-us/articles/7568858834202)

## Accessing the live performance dashboard

You can access the live performance dashboard in the Dashboards library.

**To access the live performance dashboard**

1. In Explore, click the **Dashboard** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dashboard_icon.png)) in the left sidebar.
2. From the list of dashboards, select **Live performance by channel**.

## Understanding the live performance dashboard reports

The live performance dashboard includes the following tabs:

- [Support tab](#topic_drz_qcn_zbc)
- [Messaging tab](#topic_uxk_rcn_zbc)
- [Voice tab](#topic_nfd_scn_zbc)
- [Chat tab](#topic_uzp_scn_zbc)

### Support tab

The Support tab contains the reports below. You can filter the live data (but not historical data) by **Support - Ticket brand** and **Support - Tickets group**.

#### Agent status (Live data)

If you're on an Enterprise plan, click these metrics to [drill into specific information about agent status and current tickets](https://support.zendesk.com/hc/en-us/articles/4422485166746).

- **Support - Agents online**: The number of agents in the Online status.
- **Support - Agents offline**: The number of agents in the Offline status. If you're on an Enterprise plan, click this metric to drill into specific information about agent status.

#### Ticket activity (Live data)

- **Support - New tickets (30min)**: The number of tickets that changed to the New status in the last 30 minutes. The red or green triangle indicates the change in the number of tickets from the 30 minutes before the last 30 minutes.
- **Support - Open tickets (30min)**: The number of tickets that changed to the Open status in the last 30 minutes. The red or green triangle indicates the change in the number of tickets from the 30 minutes before the last 30 minutes.
- **Support - Solved tickets (30min)**: The number of tickets that changed to the Solved status in the last 30 minutes. The red or green triangle indicates the change in the number of tickets from the 30 minutes before the last 30 minutes.
- **Support - Pending tickets (30min)**: The number of tickets that changed to the Pending status in the last 30 minutes. The red or green triangle indicates the change in the number of tickets from the 30 minutes before the last 30 minutes.

#### Ticket volume, efficiency, and satisfaction (Historical data)

These reports are based on historical data that syncs once per hour, not live data. Depending on when you load the dashboard and when the sync occurs, you might not see data for the past hour.

- **Tickets: Tickets created and solved per hour (8 hrs)**: A chart showing the number of tickets created (column) and solved (line) each hour for the last 8 hours.
- **Efficiency: First reply time (8 hrs)**: A KPI showing the median first reply time for tickets over the last 8 hours.
- **Satisfaction: Satisfaction score and rated tickets by month (12 months)**: A column chart showing the percentage of rated satisfaction tickets over the last 12 months, with an overlaid line graph showing the percentage satisfaction score.

### Messaging tab

The Messaging tab contains the reports below. You can filter the live data (but not historical data) by **Messaging - Channel** and **Messaging - Group**.

#### Agent status (Live data)

If you're on an Enterprise plan, click these metrics to [drill into specific information about agent status and current conversations](https://support.zendesk.com/hc/en-us/articles/4422485166746).

- **Messaging - Agents online**: The number of agents in the Online status.
- **Messaging - Agents away**: The number of agents in the Away status.

#### Conversation activity (Live data)

- **Messaging - Active assigned conversations**: The number of ongoing conversations (related to tickets with Open status) that have a new message from the end user or agent. This metric displays data for both online and offline agents.
- **Messaging - Inactive assigned conversations**: The number of assigned conversations without a reply from the end user for more than 10 minutes.
- **Messaging - Active conversations in queue**: The number of new conversations waiting for an agent to respond.
- **Messaging - Inactive conversations in the queue**: The number of unassigned conversations without a reply from the end user for more than 10 minutes.

#### Ticket volume (Historical data)

This report is based on historical data that syncs once per hour, not live data. Depending on when you load the dashboard and when the sync occurs, you might not see data for the past hour.

- **Tickets created and solved per hour (8 hrs)**: A column chart showing the number of tickets created over the last 8 hours, with an overlaid line graph showing the number of tickets solved.

#### Queue times (Live data)

- **Messaging - Longest time in queue for active conversations**: The longest time spent for new conversations waiting for an agent to respond.
- **Messaging - Average time in queue for active conversations**: The average time spent for new conversations waiting for an agent to respond.

### Voice tab

The Voice tab contains the reports below. You can filter the live data (but not historical data) by **Voice - Call group**.

#### Agent status (Live data)

If you're on an Enterprise plan, you can click any of these metrics to [drill into specific information about agent status and current calls](https://support.zendesk.com/hc/en-us/articles/4422485166746).

- **Voice - Agents online**: The number of agents in the Online status.
- **Voice - Agents offline**: The number of agents in the Offline status.
- **Voice - Agents away**: The number of agents in the Away status.
- **Voice - Agents transfer only**: The number of agents in the Transfer only status.

#### Wait times (Live data)

- **Voice - Longest wait time**: The maximum time a caller is waiting for a response.
- **Voice - Average wait time**: The average time a caller is waiting for a response.

#### Call activity (Live data)

- **Voice - Ongoing calls**: The number of calls currently in progress.
- **Voice - Calls in queue**: The number of calls waiting for a response.
- **Voice - Callbacks in queue**: The number of callback requests waiting for a response.

#### Call activity (Historical data)

These reports are based on historical data that syncs once per hour, not live data. Depending on when you load the dashboard and when the sync occurs, you might not see data for the past hour.

- **Calls by date**: An area chart showing the number of inbound calls, voicemail calls, forwarded calls, overflow calls, callback calls, text back calls, and outbound calls for the last 30 days.
- **Calls started and completed per hour (8 hrs)**: A column graph showing the number of calls started over the last 8 hours, with an overlaid line graph showing the number of completed calls.
- **Calls - Completion rate**: A KPI showing the percentage of calls completed out of all calls for the last 30 days.
- **Calls - Inbound calls**: A KPI showing the number of inbound calls for the last 30 days.
- **Calls - Outbound calls**: A KPI showing the number of outbound calls for the last 30 days.

### Chat tab

The Chat tab contains the reports below. You can filter the live data (but not historical data) by **Chat - Department**.

#### Agent status (Live data)

If you're on an Enterprise plan, you can click any of these metrics to [drill into specific information about agent status and current chats](https://support.zendesk.com/hc/en-us/articles/4422485166746).

- **Chat - Agents online**: The number of agents in the Online status.
- **Chat - Agents away**: The number of agents in the Away status.
- **Chat - Agents invisible**: The number of agents in the Invisible status.

#### Chat activity (Historical data)

This report is based on historical data that syncs once per hour, not live data. Depending on when you load the dashboard and when the sync occurs, you might not see data for the past hour.

- **Chats: Chats started and completed per hour (8 hrs)**: A column chart showing the number of chats started over the last 8 hours, with an overlaid line graph showing the number of completed chats.

#### Chat workflow (Live data)

- **Chat - Chats in queue**: The number of new chats created during current business hours and waiting for a response.
- **Chat - Active chats**: The number of chats that have at least one message sent by the agent or the end user in the last 10 minutes.

#### Chat satisfaction (Live data)

- **Chat - Satisfaction score (30min)**: The percentage of chats rated as Good in the last 30 minutes.
- **Chat - Good satisfaction (30min)**: The number of resolved chats rated as Good in the last 30 minutes.
- **Chat - Bad satisfaction (30min)**: The number of resolved chats rated as Bad in the last 30 minutes.

#### Wait times, reply times, and duration (Live data)

- **Chat - Longest wait time**: The longest wait time for new chats created during current business hours.
- **Chat - Average wait time**: The average wait time for new chats created during current business hours.
- **Chat - Longest reply time**: The longest time for an agent to reply to a new chat during current business hours.
- **Chat - Average reply time**: The average time for an agent to reply to a new chat during current business hours.
- **Chat - Longest duration**: The longest duration from the first to the last chat message.
- **Chat - Average duration**: The average duration from the first to the last chat message.