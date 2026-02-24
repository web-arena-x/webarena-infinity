# Displaying the estimated wait time banner in messaging conversations

Source: https://support.zendesk.com/hc/en-us/articles/8945071149210-Displaying-the-estimated-wait-time-banner-in-messaging-conversations

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

When customers are unaware of the amount of time it will take for them to connect with the agents, it results in frustration and abandoned conversations. Managing expectations on wait time, specifically the amount of time it will take to connect customers to an agent, is critical for a good customer experience.

Communicating the expected wait time can provide several benefits, such as:

- **Enhanced user experience**: By informing users of their expected wait times, the banner reduces uncertainty and anxiety, allowing them to better manage their expectations.
- **Increased transparency**: The wait time banner contributes to a clearer support process by keeping users updated on the status of their tickets.

This article describes how a messaging wait time banner works and how to turn it on.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/messaging-wait-banner.png)

This article includes the following sections:

- [Prerequisites for using a wait time banner](#topic_m5w_g32_m2c)
- [Understanding how wait times are calculated and displayed](#topic_efz_s32_m2c)
- [Understanding when the wait time banner is displayed](#topic_jnn_qj2_m2c)
- [Understanding when the banner isn't displayed](#topic_zmk_gk2_m2c)
- [Turning on the messaging wait time banner](#topic_ejq_qk2_m2c)

## Prerequisites for using a wait time banner

Ensure the following is set up:

- [Messaging is turned on](https://support.zendesk.com/hc/en-us/articles/4408827701530) and you are using at least one native messaging channel:
 - Zendesk Web Widget
 - iOS or Android Zendesk SDKs version v2.30.0 or later
 - Unity Zendesk SDK v3.2.0 or later

## Understanding how wait times are calculated and displayed

It’s important to understand that wait times are estimates. There are many factors that influence the accuracy of the calculations.

To understand how the wait times are calculated, you need to know:

- [The primary data used by Zendesk’s statistical model to calculate the wait times](#topic_rm2_z32_m2c)
- [How recent that data is](#topic_u2y_cj2_m2c)
- [How wait times are displayed](#topic_glc_h2q_2fc)
- [Factors that can negatively affect the accuracy of wait time estimates](#topic_r4m_lj2_m2c)

### The primary data used to calculate wait times

Zendesk uses a statistical model to calculate the wait time for a ticket based on two primary data points:

- **Average wait time for the customer’s place in line**: The model calculates the average wait time based on the customer’s position in line. In other words, the model uses historical data to estimate how long customers in similar positions have waited in the past.
- **Historical wait times specific to the group or queue**: The model also considers the historical wait times for the ticket’s assigned group or queue. This allows for a more tailored estimation, as different groups may have different performance metrics based on their staffing levels, ticket types, and operational efficiency.

### The recency of the data used to calculate wait times

Note: Wait time estimates are only provided for queues and groups that have had at least one ticket routed in the last seven days. This ensures that the model has access to relevant and recent data to make accurate predictions.

The model pulls performance data from the most recent periods available:

- **Previous 10 Minutes**: This provides a snapshot of the most current activity and wait times, allowing for short-term estimates.
- **Previous Two Hours**: If no data is present from the previous 10 minutes, use data from the previous two hours.
- **Previous Seven Days**: If no data is present from the previous two hours, use data from the previous seven days.

### How wait times are displayed

Wait times are displayed in a range with a lower and upper value. For example if the range is 5 to 10 minutes, the lower value is 5 minutes and the upper value is 10 minutes.

- If the upper value is less than 60 minutes, both the upper and lower values are displayed in minutes.
- If the upper value is less than 24 hours, but more than 60 minutes, both the upper and lower values are displayed in hours.
- If the upper value is more than 24 hours, both the upper and lower values are displayed in days.

To avoid displaying indistinguishable time ranges, such as 1 to 1 hours, the lower value will be rounded down and the upper value will be rounded up. For example, if the lower estimate is 65 minutes and the upper estimate is 80 minutes, the range will be displayed as 1 to 2 hours.

### Factors that negatively affect the accuracy of wait time estimates

Several factors can affect the accuracy of the estimated wait times provided by the model, including:

- A sudden increase in ticket submissions can impact accuracy in the short-term. This is because the sudden influx can overwhelm the existing resources, leading to longer wait times than reflected in the usual data. However, as more data becomes available, reflecting the increase in tickets and wait times, the system adjusts and the accuracy of the wait times estimates improve.
- Insufficient recent ticket data forces the model to rely more heavily more outdated data, which may not provide an accurate foundation for its current estimates. This can occur in situations where there is a low volume of tickets routed in the recent past, leading to a lack of historical performance data to draw upon.
- Change in agent availability may provide inaccurate data for a short while.
- New queues or groups can lack sufficient historical data for the model to make informed estimates. As the queue processes more tickets over time, the model will gradually accumulate data and provide more accurate predictions.

## Understanding when the wait time banner is displayed

Based on the wait time banner settings, users will see a wait time or a queue position. As they wait, it’s then helpful to reassure them that an agent will be with them soon.

The wait time banner is displayed only when group or queue assignment changes.
Specifically:

- A ticket is assigned to a group or added to a queue for the first time. This initial placement triggers the banner to inform the user of their expected wait time.
- A ticket transfers from one group or queue to another. If there is already a wait time banner displayed, the wait time may be updated. This change is significant because the wait time may vary due to the new queue dynamics, and the business must inform the user of this adjustment.

The data refreshes every minute, displaying the updated wait time if there have been any changes within the last minute.

There may also be situations where the wait time or queue position increases. For example:

- The account uses ticket priority to determine the order of tickets in the queue. Higher priority tickets may displace Normal and Lower priority tickets, leading to an increase in both queue position and wait time.
- If agents are taking longer than usual to resolve issues, the wait time will reflect this by showing a longer duration.

### Displaying "Agent will be with you shortly" in the banner

When an agent begins working on a ticket, the banner is updated to inform the user that “An agent will be with you shortly.” This message appears in the banner when:

- **An agent accepts the ticket**. Tickets associated with messaging conversations are offered to agents. Depending on the account’s settings, these tickets can be accepted manually by the agent or automatically.
- **Omnichannel routing directly assigned the ticket to an agent**. The banner also appears when an admin or team lead manually assigns a ticket to an agent through omni-channel routing.
- **An agent assigns the ticket to themselves**. When an agent views an unassigned ticket and assigns it to themself using the [take it](../../agent-guide/ticket-basics/manually-assigning-a-ticket.md) option.

The banner is hidden as soon as the agent sends their first message.

## Understanding when the banner isn't displayed

The wait time banner isn’t displayed to users in the following situations:

- The group or queue associated with the ticket is offline when the group or queue assignment changed.
- There is no group or queue associated with the ticket, and the account is offline when the group or queue assignment was changed.
- If the ticket is directly assigned to specific agents , no banner with estimated wait time is displayed.
- During agent-to-agent transfers when tickets do not return to the queue. In these situations, the ticket is being handed directly to another agent, and therefore doesn’t have an additional wait time.
- When a ticket has exited the queue. For example, when a messaging session times out.
- If an agent is the only online member of the ticket's group. In this scenario, tickets are assigned directly to the agent without delay even if they might not be able to respond immediately.

## Turning on the messaging wait time banner

To turn on the messaging wait time banner:

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. Select your channel (Android, iOS, Web Widget, or Unity).
3. Click or expand **Wait time**.
4. Click the **Show estimated wait time** checkbox to display the estimated agent response time.
5. Click the **Show queue position** checkbox to allow users to see their position in the queue.
6. Click **Save**.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/messaging-wait-banner-settings.png)