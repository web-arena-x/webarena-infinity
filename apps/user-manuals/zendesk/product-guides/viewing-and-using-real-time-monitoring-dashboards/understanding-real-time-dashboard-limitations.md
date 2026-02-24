# Understanding real-time dashboard limitations

Source: https://support.zendesk.com/hc/en-us/articles/9757137259546-Understanding-real-time-dashboard-limitations

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

The following limitations currently apply when using the real-time monitoring dashboards:

- To see the incoming tickets dashboard, [omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4409149119514) must be turned on.
- You can't change agent state from the dashboards. This is planned for a future update.
- The ticket progress dashboard displays data for tickets created during the last seven days.
- Tickets that entered a queue and haven’t been updated since, might not appear in the list of current tickets in standard and custom queues.
- The real-time monitoring dashboards are read-only. You can't customize the dashboards beyond applying filters and drilling into data. Customization is planned for a future update.
- Certain filter options might be limited to the agent attributes in the dashboard. These filters can be identified with a tooltip indicating when that is the case. For example, groups on the ticket progress dashboard, agents in the agent efficiency dashboard.
- Data retention for these dashboards are subject to change depending on performance and scalability:
 - The ticket progress dashboard reports on activity related to tickets created in the past seven days.
 - The agent efficiency dashboard reports on tickets created in the past 30 days.
 - The agent productivity dashboard reports on all used capacity, regardless of the assignment time.
- SLA reports are only applicable to accounts with one or more policies enabled.
- KPIs and tables have a refresh rate of 20 seconds. Charts showing data over the last several hours or days have a refresh rate of one minute.
- Tables are limited to 100 rows of data, while drill-in tables are limited to 500 rows.
- If no maximum capacity is assigned to an agent, no data will be shown in the capacity used KPIs in the agent availability dashboards for customers with omnichannel routing enabled.
- The agent capacity is not displayed if the agent name filter is selected and an agent name contains special characters.
- If an agent initiates a call from an email ticket, this will use the agent's voice capacity. However, this will be shown in the drill-in for the agent used capacity for voice as an email ticket. Therefore, there might be instances where not all capacity in use for voice is shown by only filtering for Voice under the channel type filter.
- When you refresh a dashboard, the table sorting configuration is also reset.
- For agent efficiency metrics, proactive agent messages do not count as a reply within the agent reply time metric. Therefore, this may result in a zero metric value.
- For agent efficiency metrics, actions done on the ticket while it was not actively assigned to an agent do not count towards that agent. For example, replies made or tickets solved which are not already assigned to the agent will not count towards the metrics.
- Tickets that are marked as solved and retrospectively assigned will not count towards agents solved tickets in the Agent efficiency dashboard.
- Agent efficiency metrics are only calculated on active tickets, meaning tickets that are in an open state. Metric calculation is paused when tickets go into the pending or on-hold state.
- On the customer wait times dashboard, metrics are calculated only on new, open, pending, and solved tickets.
- It might take up to 24 hours for a dashboard reporting on custom queues to appear in your account after creating your first custom queue.
- Real-time monitoring does not report on deleted agents or deleted and closed tickets.
- Agent names are not decipherable for accounts with the [advanced encryption add-on](https://support.zendesk.com/hc/en-us/articles/5043582015898) turned on.
- Voice reports only show data from phone-inbound, callbacks and group transfers in engagements. Phone-outbound, consultations, and voicemail are not currently supported.