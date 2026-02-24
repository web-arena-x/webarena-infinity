# Monitoring real-time chat metrics

Source: https://support.zendesk.com/hc/en-us/articles/4408888768410-Monitoring-real-time-chat-metrics

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Enterprise or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Live chat and messaging Enterprise |

With the Real-Time Monitor, you can see an overview of key chat metrics, including queue
size, customer wait times, and chat satisfaction, on a single screen. Customer service team
leads can get an at-a-glance view of current Chat support demand and update agent assignments
accordingly.

Tip: If your plan includes Zendesk Explore Professional or
above, you can also analyze real-time Chat activity using the prebuilt live dashboard. See
[Overview of the Explore live dashboard](https://support.zendesk.com/hc/en-us/articles/4408843771546).

This article contains the following sections:

- [Understanding the default
  metrics](#topic_d35_433_n3b)
- [Customizing available statistics](#topic_ny4_52q_4y)
- [Filtering by department](#topic_bqy_vdq_4y)
- [Accessing additional real-time activity data
  using the API](#topic_gds_l2q_4y)

## Understanding the default metrics

The Real-Time Monitor dashboard displays a number of constantly-updated metrics.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/newmonitor.png)

Metrics are organized into the following categories:

- [Queue](#topic_b1p_4k3_n3b)
- [Chat Activity](#topic_dbm_rk3_n3b)
- [Agent Activity](#topic_txv_sk3_n3b)
- [Customer Satisfaction](#topic_i32_tk3_n3b)

### Queue

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_monitor_top_row.png)

The top row of the dashboard displays information about the **Queue**. The information
here refers to chats that have not been served by any agent. It is divided into three
subcategories:

- **Queue**: New chats that have not been served by any agent. This is the sum of
  **Incoming Chats** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_monitor_queue_incoming_icon.png))and **Assigned Chats** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_monitor_queue_assigned_icon.png)). Applicable only if [chat routing mode](https://support.zendesk.com/hc/en-us/articles/4408836490138) is set to Assigned.
- **Wait Time**: The **longest** and **average** times visitors have been
  waiting for their requests to be served. Wait time is calculated as duration between
  the first visitor message in the chat and the first agent message. Wait time will be 0
  for agent-initiated or trigger-initiated chats.

  Note: If your agents are serving chats
  in the Agent Workspace, wait time ends some seconds after a chat is initially
  served.
- **Missed Chats**: The number of chats **in the past 30 minutes** where the
  agent does not answer the incoming chat request and the visitor subsequently
  leaves.

### Chat Activity

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_monitor_middle_row.png)

The middle row of the dashboard displays information related to **Chat Activity**, and
is divided into the following subcategtories:

- **Currently Served Chats**: The number of chats your agents are serving right
  now
- **Chats Per Agent**: Average number of chats **per logged in agent**, and
  **per online agent**.
- **Response Time (Average and Longest)**: Average and longest time that visitors
  have been waiting for an agent reply, calculated from each interaction in a chat
  session. Response time is the duration between a message by a visitor and the next
  response by an agent. If multiple messages are left by a visitor before an agent
  responds, response time is measured from the time the visitor leaves the first message
  in the string.
- **Chat Duration**: Longest and average length a current ongoing chat. Chat
  duration is calculated as duration between first message in the chat (visitor message,
  agent message or message sent via triggers) and when the chat ends (visitor ends the
  chat, or last agent leaves the chat, or chat ends due to inactivity timeout).

### Agent Activity

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_monitor_agent_activity.png)

The first box in the bottom row of the dashboard displays information related to **Agent
Activity**, and includes the following metrics:

- **Logged In Agents**: The total number of agents currently logged in
- **Status**: The number of logged in agents broken down by their current status:

  - Online (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_monitor_status_online.png))
  - Away (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_monitor_status_away.png))
  - Invisible (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_monitor_status_invisible.png))

**To check agent messaging status**

1. In the Chat dashboard, click the Monitor icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_monitor_icon_sidebar.png)).
2. Go to **Agent Activity** to view the online agents.

### Customer Satisfaction

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_monitor_satisfaction.png)

The next box in the bottom row of the dashboard displays information related to
**Customer Satisfaction**, and includes the following metrics:

- **Satisfaction (Overall)**: The percentage of chats rated Good over the past 30
  minutes.
- **Ratings**: Total ratings over the past 30 minutes, broken down by their
  satisfaction choice:
  - Good (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_monitor_satisfaction_good.png))
  - Bad (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_monitor_satisfaction_bad.png))

Note: The metrics in this box are only applicable only if [Chat Ratings](https://support.zendesk.com/hc/en-us/articles/4408883190682) are enabled.

## Customizing available statistics

Admins can customize which of these statistics appear in Monitor for the whole account.

**To edit which statistics appear**

1. In the Chat dashboard, click the Monitor icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_monitor_icon_sidebar.png)).
2. At the top of the Monitor edit page, click **Settings**.
3. Select or clear check boxes next to each statistic to determine if it appears in
   Monitor.
4. Click **Save Changes**.

## Filtering by department

Both agents and admins viewing the dashboard can filter the statistics by department.
Select one or more individual departments, **All Departments**, or **No
Department**.

**To filter by department**

1. In the Chat dashboard, click the Monitor icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_monitor_icon_sidebar.png)).
2. At the top of the Monitor edit page, click the **Filter by Department** drop-down
   menu.
3. Select **All Departments**, **No Department**, or an individual department.

## Accessing additional real-time activity data using the API

Get additional insight into your team's acitvity using the Real-Time Chat API. For details,
see our [API documentation](https://developer.zendesk.com/rest_api/docs/chat/apis).