# Analyzing your Support ticket activity and agent performance

Source: https://support.zendesk.com/hc/en-us/articles/4408835846810-Analyzing-your-Support-ticket-activity-and-agent-performance

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Zendesk Explore features a prebuilt dashboard to help you monitor many details about your tickets, efficiency, and performance with Zendesk Support. The dashboard can help you identify your ticket backlog, customer satisfaction, agent activity, SLAs, and more.

Tip: You can edit and customize the Support dashboard by cloning it (see [Cloning dashboards](https://support.zendesk.com/hc/en-us/articles/4408821374362)). If you need something more complex, you can write your own reports using a wide range of metrics and attributes. For details, see [Creating reports](https://support.zendesk.com/hc/en-us/articles/4408821589530).

This article contains the following topics:

- [Opening the Support dashboard](#topic_nw1_knl_jkb)
- [Understanding the Support dashboard reports](#topic_rql_4nl_jkb)

## Opening the Support dashboard

Use the following procedure to access the Support dashboard.

**To open the Support dashboard**

1. In Explore, click the **Dashboard** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dashboard_icon.png)) in the left sidebar.
2. From the list of dashboards, select the **Zendesk Support** dashboard.

## Understanding the Support dashboard reports

The Support dashboard contains the following tabs:

- [Tickets tab](#topic_hlj_xbj_z3b)
- [Efficiency tab](#topic_zd3_ybj_z3b)
- [Assignee activity tab](#topic_dpf_ybj_z3b)
- [Agent updates tab](#topic_edg_ybj_z3b)
- [Unsolved tickets tab](#topic_f4g_ybj_z3b)
- [Backlog tab](#topic_wyg_ybj_z3b)
- [Satisfaction tab](#topic_ijh_ybj_z3b)
- [SLAs tab](#topic_d5h_ybj_z3b)
- [Group SLAs tab](#topic_lbp_jdx_kxb)

Note: The information in Explore dashboards is updated on a schedule. The schedule depends on which Explore plan you are using. For details, see [Data refresh intervals for Explore reporting](https://support.zendesk.com/hc/en-us/articles/4408823242778).

### Tickets tab

The **Tickets** tab contains reports about tickets created in your Zendesk account. You can filter the reports by time, group, brand, channel, form, submitter role, and requester organization.

On this tab, the time filter is based on the ticket creation date, unless otherwise noted in the report descriptions below.

**To open the Tickets dashboard tab**

1. In Explore, click the **Dashboard** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dashboard_icon.png)) in the left sidebar.
2. From the list of dashboards, select the **Zendesk Support** dashboard.
3. Click the **Tickets** tab.

#### Tickets tab headline metrics

This tab displays the following headline metrics (KPIs):

- **Created tickets:** The number of tickets created in your Support account.
- **Unsolved tickets:** The number of unsolved tickets. These are tickets that do not have a Closed or Solved status.
- **Solved tickets:** The number of solved tickets. These are tickets that have a Solved or Closed status. The time filter for this report is based on the ticket solved date.
- **One-touch tickets:** The percentage of tickets that were solved with one agent reply. The time filter for this report is based on the ticket solved date.
- **Reopened tickets:** The percentage of reopened tickets that were previously marked as Solved. The time filter for this report is based on the ticket solved date.

![Explore support dashboard ticket KPIs](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-3.png)

#### Tickets tab reports

This tab displays the following reports:

- **Tickets created by hour:** The percentage of tickets created each hour (0-23).

 ![Tickets created by hour report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-4.png)
- **Average tickets created by day of week:** The average number of tickets created for each day of the week.

 ![Average tickets created by day of week report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-7.png)
- **Tickets created by date:** The total number of tickets created each day for the date range you choose. You can hover over a data point on the graph to see how many of the created tickets have been solved.

 ![Tickets created by date report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-57.png)
- **Tickets by selected attribute (top 10):** The percentage of tickets for each type of the attribute you select. For example, if you select **Ticket channel**, you'll see the percentage of tickets that were created by each channel during the date range you selected.

 Note: Analytics for service catalog requests are accessible when you filter by the service's name, which is automatically used as the associated form's name, too.

 ![Tickets by selected attribute report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-58.png)
- **Tickets created by date and channel (top 10):** The number of tickets created each day for the date range you chose sliced by the channel from which the ticket was received.

 ![Tickets created by date and selected attribute (top 10)](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-66.png)
- **Tickets created by month/year:** Displays the number of tickets created each month for the years you select. You can overlay data from the last five years to help you compare. The current month's data is not displayed until the end of the month. This report is excluded from the tab's time filter.

 ![Tickets created by month and year report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-5.png)

### Efficiency tab

The **Efficiency** tab contains reports that help you evaluate the efficiency of your agents. You can filter the reports by time, group, brand, channel, form, priority, and requester organization.

On this tab, the time filter is based on the ticket solved date, unless otherwise noted in the report descriptions below.

**To open the Efficiency dashboard tab**

1. In Explore, click the **Dashboard** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dashboard_icon.png)) in the left sidebar.
2. From the list of dashboards, select the **Zendesk Support** dashboard.
3. Click the **Efficiency** tab.

#### Efficiency tab headline metrics

This tab displays the following headline metrics (KPIs):

- **First reply time median:** The median time from when the ticket was first created until an agent first replied. The time filter for this report is based on the ticket created date.
- **First resolution time median:** The median time from the creation of a ticket until it was first closed or solved.
- **Full resolution time median:** The median time from the creation of a ticket until it was fully closed or solved.
- **Group stations average:** The average number of groups a ticket was assigned to.
- **Assignee stations average:** The average number of agents a ticket was assigned to.

![Efficiency tab headline metrics](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-71.png)

#### Efficiency tab reports

This tab displays the following reports:

- **Tickets by first reply time brackets:** A bracketed list showing the percentage of tickets first reply times that fall into various brackets. For example, in the screenshot below, 12% of tickets were replied to in more than 24 hours. The time filter for this report is based on the ticket created date.

 ![Tickets by first reply time brackets report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-83.png)
- **Tickets by full resolution time brackets:** A bracketed list showing the percentage of tickets full resolution times that fall into various brackets. For example, in the screenshot below, 10% of tickets were fully resolved in 5-24 hours.

 ![Tickets by full resolution time brackets report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-84.png)
- **First reply and assignment time median over time:** A comparison between the median first reply time and the median first assignment time over the date range you selected. The time filter for this report is based on the ticket created date.

 ![First reply and assignment time median over time report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-85.png)
- **Full resolution and requester wait time median over time:** A comparison between the amount of time it took to solve a ticket, and the median time a ticket spend in the New, Open, or On-hold status.

 ![Full resolution and requester wait time median over time report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-86.png)
- **Tickets by agent replies brackets:** The bracketed percentage of agent replies for tickets. In the example below, 12% of tickets had 2 agent replies.

 ![Tickets by agent replies brackets report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-87.png)
- **Tickets by group stations brackets:** The bracketed number of groups that were assigned to tickets. In the example below, 56% of tickets were assigned to two or three groups.

 ![Tickets by group stations brackets report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-88.png)
- **Agent replies average and resolutions over time:** The average number of agent replies and the total number of tickets solved on a daily basis. You can hover over a data point to see the exact results for a day.

 ![Agent replies average and resolutions over time](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-73.png)
- **Assignee and group stations average over time:** Displays both the average number of agent tickets were assigned to and the average number of groups associated with a ticket.

 ![Assignee and group stations average over time](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-72.png)

### Assignee activity tab

The **Assignee Activity** tab helps you to see the results when you assign tickets to agents and others. You can filter the reports by time, group, assignee, brand, channel, form, and requester organization.

On this tab, the time filter is based on the ticket solved date.

**To open the Assignee activity dashboard tab**

1. In Explore, click the **Dashboard** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dashboard_icon.png)) in the left sidebar.
2. From the list of dashboards, select the **Zendesk Support** dashboard.
3. Click the **Assignee activity** tab.

#### Assignee activity tab headline metrics

This tab displays the following headline metrics (KPIs):

- **Solved tickets:** The number of solved and closed tickets that were resolved during the selected date range.
- **Requester wait time median:** The median time that tickets spent in the new, open, or on-hold statuses.
- **Assignment to resolution:** The median time from the last agent assignment until the ticket was resolved.
- **One-touch tickets:** The percentage of tickets that were resolved with only one agent reply.
- **Two-touch tickets:** The percentage of tickets that were resolved after two agent replies.

![Assignee activity tab headline metrics](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-6.png)

#### Assignee activity tab reports

This tab displays the following reports:

- **Good vs bad satisfaction tickets:** A pie chart showing the percentage of rated tickets that received a satisfaction rating of good or bad.

 ![Support good vs bad satisfaction tickets](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-14.png)
- **Tickets by requester wait time brackets:** A bracketed list showing the requester wait time for tickets. In this example, 12% of tickets took between 1 and 3 days before the requester received a response.

 ![Tickets by requester wait time brackets report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-89.png)
- **Satisfaction score and requester wait time median by date:** A comparison of the customer satisfaction rating against the amount of time they had to wait for a response from an agent.

 ![Satisfaction score and requester wait time median by date report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-90.png)
- **Assignee activity:** A detailed list of your agents and their activities including the number of tickets they solved, their average reply time, and more.

 ![Support assignee activity report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-13.png)

### Agent updates tab

The **Agent Updates** tab shows comments and updates made to tickets by your agents. You can filter the reports by time, agent, brand, channel, form, group, and requester organization.

On this tab, the time filter is based on the update date.

**To open the Agent updates dashboard tab**

1. In Explore, click the **Dashboard** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dashboard_icon.png)) in the left sidebar.
2. From the list of dashboards, select the **Zendesk Support** dashboard.
3. Click the **Agent updates** tab.

#### Agent updates tab headline metrics

This tab displays the following headline metrics (KPIs):

- **Public comments:** The total number of tickets where public comments from an agent are included.
- **Internal comments:** The total number of tickets where internal comments from an agent are included.
- **Tickets commented:** The number of tickets with an agent comment, whether public or internal.
- **Tickets solved:** The number of tickets that were marked as solved by an agent.
- **Tickets created:** The number of tickets that were created by an agent.

![Agent updates headline metrics](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-29.png)

#### Agent updates tab reports

This tab displays the following reports:

- **Agent comment averages by date:** A comparison of the total number of comments on tickets and the number of those comments that were public or internal.

 ![Agent comment averages by date](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-32.png)
- **Tickets commented, created and solved by date:** A comparison of the number of tickets created, solved, and commented on over the selected date range.

 ![Tickets commented created and solved by date](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-33.png)
- **Agent updates:** For each agent, displays detailed information about updates they made to tickets including comments, solves, creation, and more.

 ![Agent updates report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-31.png)

### Unsolved tickets tab

The **Unsolved Tickets** tab helps you take a detailed look at tickets in your account that are still open and require attention. You can filter the reports by group, assignee, brand, channel, priority, and requester organization.

**To open the Unsolved tickets dashboard tab**

1. In Explore, click the **Dashboard** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dashboard_icon.png)) in the left sidebar.
2. From the list of dashboards, select the **Zendesk Support** dashboard.
3. Click the **Unsolved tickets** tab.

#### Unsolved tickets tab headline metrics

This tab displays the following headline metrics (KPIs):

- **Unsolved tickets:** Tickets that are not in a Solved or Closed status.
- **New and open tickets:** Tickets that are in a New or Open status.
- **Unreplied unsolved tickets:** Unsolved tickets with no agent replies.
- **Time since update median:** The median time since unsolved tickets were updated.
- **Ticket age median:** The median time since unsolved tickets were created.

![Unsolved tickets headline metrics](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-91.png)

#### Unsolved tickets tab reports

This tab displays the following reports:

- **Unsolved tickets by status:** A pie chart showing the percentage of tickets that are in a New, Open, Pending, or On-hold status.

 ![Unsolved tickets by status report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-95.png)
- **New and open tickets by assignment status:** A pie chart showing the percentage of tickets in the Open or New state that are assigned, or unassigned.

 ![New and open tickets by assignment status](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-96.png)
- **Unsolved tickets by selected attribute (top 10):** A stacked chart displaying the percentage of tickets in the new, open, pending and on-hold statuses for the attribute you choose. You can choose from ticket brand, channel, form, group, priority, or type.

 ![Unsolved tickets by selected attribute report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-97.png)
- **Unsolved tickets by creation month:** A stacked chart showing all unsolved tickets over the date range you selected. The stacks indicate whether the ticket is New, Open, Pending, or On-Hold.

 ![Unsolved tickets by creation month report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-98.png)
- **Unsolved tickets:** A detailed list of unsolved tickets sorted by agent name.

 ![Unsolved tickets report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-92.png)

### Backlog tab

The **Backlog** tab helps you look at open ticket activity over a date range you select. You can filter the reports by group, assignee, brand, channel, priority, and type.

This tab contains no headline metrics.

**To open the Backlog dashboard tab**

1. In Explore, click the **Dashboard** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dashboard_icon.png)) in the left sidebar.
2. From the list of dashboards, select the **Zendesk Support** dashboard.
3. Click the **Backlog** tab.

#### Backlog tab reports

This tab displays the following reports:

- **Daily historical backlog by status (30 days):** A list of your open ticket backlog over the last 30 days to help you identify trends.

 ![Daily historical backlog by status report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-81.png)
- **Weekly historical backlog by status (12 weeks):** A list of your open ticket backlog over the last 12 weeks to help you identify trends.

 ![Weekly historical backlog by status report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-82.png)
- **Weekly historical backlog by selected attribute (top 10/12 weeks):** The number of unsolved tickets at the end of each week for the last 12 weeks. Choose a tab to display results by ticket brand, group, channel, priority, or type.

 ![Weekly historical backlog by selected attribute (top 10/12 week) report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-49.png)

### Satisfaction tab

The **Satisfaction** tab helps you take a closer look at customer satisfactions (CSAT) scores for your tickets. You can filter the reports by time, group, brand, channel, form, priority, and type.

On this tab, the time filter is based on the ticket solved date, unless otherwise noted in the report descriptions below.

**To open the Satisfaction dashboard tab**

1. In Explore, click the **Dashboard** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dashboard_icon.png)) in the left sidebar.
2. From the list of dashboards, select the **Zendesk Support** dashboard.
3. Click the **Satisfaction** tab.

#### Satisfaction tab headline metrics

This tab displays the following headline metrics (KPIs):

- **Satisfaction score:** The percentage of tickets rated as good from the total number of rated tickets.
- **Good satisfaction tickets:** The number of tickets rated as good.
- **Bad satisfaction tickets:** The number of tickets rated as bad.
- **Bad to good ratings:** The number of tickets with a rating that changed from bad to good. The time filter for this report is based on the update date.
- **Satisfaction rated ratio:** The percentage of tickets that received either good or bad from the total number of surveyed tickets.

![Satisfaction tab headline metrics](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-50.png)

#### Satisfaction tab reports

This tab displays the following reports:

- **Good vs bad satisfaction tickets:** A pie chart showing the percentage of good and bad satisfaction rated tickets both with and without comments.

 ![Good vs bad satisfaction tickets report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-74.png)
- **Rated tickets funnel:** A funnel chart showing the percentage of surveyed and rated tickets against all tickets.

 ![Rated tickets funnel](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-75.png)
- **Satisfaction score and rated tickets by date:** The number of rated tickets against the percentage satisfaction score they received over the selected date range.

 ![Satisfaction score and rated tickets by date report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-76.png)
- **Satisfaction score by selected attribute (top 10 by volume):** The average satisfaction percentage for the attribute you select. For example, if you select **Ticket Channel**, you'll see the average satisfaction score for each of the ticket channels like Chat, Email, etc. You can select from Ticket brand, channel, form, group, priority, and type.

 ![Satisfaction score by selected attribute report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-77.png)
- **Satisfaction score and rated tickets by month (12 months):** The number of rated tickets, and the average satisfaction score over a 12-month period. This report is excluded from the tab's time filter.

 ![Satisfaction score and rated tickets by month (12 months) report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-52.png)
- **Satisfaction rated ratio and surveyed tickets by month (12 months):** The percentage of all tickets that were rated against the number of tickets that were surveyed over a 12-month period. This report is excluded from the tab's time filter.

 ![Satisfaction rated ratio and surveyed tickets by month (12 months)](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-51.png)

### SLAs tab

The **SLAs** tab helps you measure your results against SLAs you configured.
You can filter the reports by time, SLA policy, SLA metric, group, brand, form, priority, and requester organization.

On this tab, the time filter is based on the SLA update date, unless otherwise noted in the report descriptions below.

Note: When no data filters are selected, the SLA metrics include data for deleted tickets. This happens because historic data isn't changed for SLA metrics and events. When any data filters are applied, however, data for deleted tickets is excluded because the applied data filter attributes and values don't exist for deleted tickets.

**To open the SLAs dashboard tab**

1. In Explore, click the **Dashboard** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dashboard_icon.png)) in the left sidebar.
2. From the list of dashboards, select the **Zendesk Support** dashboard.
3. Click the **SLAs** tab.

#### SLAs tab headline metrics

This tab displays the following headline metrics (KPIs):

- **SLA achievement rate:** The percentage of tickets that met the SLA from the total number of SLA tickets.
- **SLA breached tickets:** The number of tickets that have at least one SLA target breach.
- **SLA achieved tickets:** The number of tickets that did not have an SLA target breach.
- **SLA active tickets:** The number of tickets with an active SLA policy.
- **SLA active breached tickets:** The number of active tickets with at least one SLA target breach.

![Support SLA headline metrics (kpis)](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-22.png)

#### SLAs tab reports

This tab displays the following reports:

- **Achieved vs breached completed SLA policies by date:** Shows the number of tickets that breached or achieved your SLA targets over the date range you chose.

 ![Achieved vs breached completed SLA policies by date report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-43.png)
- **Achieved and breached completed SLA policies by selected attribute (top 10 breached):** A stacked bar chart showing the percentage of tickets that achieved, or breached an SLA policy for the attribute you select. You can select from ticket brand, channel, form, or group.
 Additionally, you can select the SLA policy name.

 ![Achieved and breached completed SLA policies by selected attribute (top 10 breached)](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-44.png)
- **SLA target breaches by hour:** A chart showing the average percentage of breaches that happened each hour over a 24 hour period.

 ![SLA target breaches by hour report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-45.png)
- **SLA target breaches by day of week:** A bar chart showing the average percentage of SLA breaches that happened each day of the week.

 ![SLA target breaches by day of week report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-46.png)
- **Achieved and breached SLA targets by metric:** The percentage of time that each SLA target was achieved or breached.

 ![Achieved and breached SLA targets by metric report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-24.png)
- **SLA target achievement rate by month (12 months):** The percentage of instances per month where SLA targets where achieved. This report is excluded from the tab's time filter.

 ![SLA target achievement rate by month report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-23.png)

### Group SLAs tab

The **Group SLAs** tab helps you measure your results against group SLAs you configured. You can filter the reports by time, group SLA policy, group SLA metric, group, brand, form, priority, and requester organization.

On this tab, the time filter is based on the group SLA update date, unless otherwise noted in the report descriptions below.

Note: When no data filters are selected, the group SLA metrics include data for deleted tickets. This happens because historic data isn't changed for group SLA metrics and events. When any data filters are applied, however, data for deleted tickets is excluded because the applied data filter attributes and values don't exist for deleted tickets.

**To open the Group SLAs dashboard tab**

1. In Explore, click the **Dashboard** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dashboard_icon.png)) in the left sidebar.
2. From the list of dashboards, select the **Zendesk Support** dashboard.
3. Click the **Group SLAs** tab.

#### Group SLAs tab headline metrics

This tab displays the following headline metrics (KPIs):

- **Achievement rate:** The percentage of tickets that met the group SLA from the total number of SLA tickets.
- **Breached tickets:** The number of tickets that have at least one group SLA target breach.
- **Achieved tickets:** The number of tickets that did not have a group SLA target breach.
- **Active tickets:** The number of tickets with an active group SLA policy.
- **Breached tickets:** The number of active tickets with at least one group SLA target breach.

![Support group SLA headline metrics (kpis)](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_group_sla_dashboard_kpis.png)

#### Group SLAs tab reports

This tab displays the following reports:

- **Group SLA: Achieved vs breached completed Group SLA policies by date:** Shows the number of tickets that breached or achieved your group SLA targets over the date range you chose.

 ![Achieved vs breached completed group SLA policies by date report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_groups_slas_dashboard_1.png)
- **Group SLA: Achieved and breached completed Group SLA policies by selected attribute (top 10 breached):** A stacked bar chart showing the percentage of tickets that achieved, or breached a group SLA policy for the attribute you select. You can select from ticket brand, channel, form, or group. Additionally, you can select the group SLA policy name.

 ![Achieved and breached completed group SLA policies by selected attribute (top 10 breached)](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_group_slas_dashboard_2.png)
- **Group SLA target breaches per hour:** A chart showing the average percentage of breaches that happened each hour over a 24 hour period.

 ![Group SLA target breaches by hour report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_group_slas_dashboard_3.png)
- **Group SLA target breaches by day of week:** A bar chart showing the average percentage of group SLA breaches that happened each day of the week.

 ![Group SLA target breaches by day of week report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_group_slas_dashboard_4.png)
- **Group SLAs: Achieved and breached Group SLA targets by metric:** The percentage of time that each group SLA target was achieved or breached.

 ![Achieved and breached group SLA targets by metric report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_group_slas_dashboard_5.png)
- **Group SLAs: Group SLA target achievement rate by month (12 months):** The percentage of instances per month where group SLA targets where achieved. This report is excluded from the tab's time filter.

 ![Group SLA target achievement rate by month report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_group_slas_dashboard_6.png)