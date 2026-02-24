# Analyzing agent state and activity

Source: https://support.zendesk.com/hc/en-us/articles/5600298255770-Analyzing-agent-state-and-activity

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

You must have  [the Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930) to use the dashboard described
in this article.

Zendesk Explore features a prebuilt dashboard to help you monitor your agents’ states
across channels. This dashboard gives supervisors the information they need to
understand how their agents are spending their time.

Tip: You can [clone this dashboard](https://support.zendesk.com/hc/en-us/articles/4408821374362) and [customize it](https://support.zendesk.com/hc/en-us/articles/4408819770906) to meet more specific scenarios. If you
need something more complex, you can [create your own reports](https://support.zendesk.com/hc/en-us/articles/4408821589530) using [metrics and attributes for agent state and
activity](https://support.zendesk.com/hc/en-us/articles/5600290657434).

This article contains the following topics:

- [Opening the omnichannel agent state and activity dashboard](#topic_a2r_2lf_2xb)
- [Understanding the reports](#topic_a5q_flf_2xb)

## Opening the omnichannel agent state and activity dashboard

The omnichannel agent state and activity dashboard is available in the Dashboards
library in Explore.

**To open the omnichannel agent state and activity dashboard**

1. In Explore, click the **Dashboard** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dashboard_icon.png)) in the left sidebar.
2. From the list of dashboards, select one of the following dashboards:
   - (If you don't use [omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4409149119514))
     **Zendesk Omnichannel: Agent State and Activity**
   - (If you use omnichannel routing) **Zendesk Omnichannel: Unified and
     Custom Agent State and Activity**

The two dashboards are similar in layout and purpose, but the dashboard for
omnichannel routing customers includes information about unified and custom states
in addition to channel-specific states. Any differences between the dashboards are
called out in the descriptions below.

## Understanding the reports

The dashboard contains the following tabs:

- [Summary tab](#topic_qgk_rlf_2xb)
- [State Detail tab](#topic_lry_rlf_2xb)
- [Assigned work tab](#topic_tng_nz2_z1c)

Note: When filtering any of the tabs in this dashboard, make
sure to filter by both group and agent. If you filter only by agent, data is
duplicated if the selected agent is in multiple groups.

Note: When exporting this dashboard, duration data in the
export is always calculated in seconds.

### Summary tab

The Summary tab contains reports that give you an overall look at what state
groups or agents were in over a specified period of time. You can filter the
reports on the dashboard by **Date**, **Channel**, **Group**, **Agent
name**, and **Agent state**. If you use omnichannel routing, the
**Channel** filter doesn’t appear, and the reports are automatically
filtered by the **Unified** channel value.

#### Summary tab headline metrics

This tab displays the following headline metrics (KPIs):

- **Online time**: The total amount of time that the filtered groups or
  agents were in the Online state.
- **Offline time**: The total amount of time that the filtered groups
  or agents were in the Offline state.
- **Away time**: The total amount of time that the filtered groups or
  agents were in the Away state.
- **Transfers only time**: The total amount of time that the filtered
  groups or agents were in the Transfers only state.
- **Invisible time**: The total amount of time that the filtered groups
  or agents were in the Invisible state.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_omnichannel_db_summary_kpis.png)

#### Summary tab reports

This tab displays the following reports:

- **Time in state by day (online and offline)**: The total number of
  hours spent in the Offline and Online states by the selected groups or
  agents.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_omnichannel_db_time_in_state_day.png)

  If you use
  omnichannel routing, this report is called **Time in unified states
  by day** and shows the total number of hours spent in the
  Away, Offline, Online, and Transfers Only states by the selected
  groups or agents.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_omnichannel_db_time_in_unified_state_day.png)
- **Time in custom states by day (top used).** (Appears only if you use
  omnichannel routing.) The total number of hours spent in the top five
  custom states by the selected groups or agents.

### State Detail tab

The State Detail tab contains a single report that lets you dig further into how
agents spent their time. You can filter the reports on the dashboard by
**Date**, **Channel**, **Group**, **Agent name**, and **Agent
state**.

By default, the report is filtered to include only the **Online**,
**Away**, **Transfer only**, **Invisible**, and **Offline** states
(if you don’t use omnichannel routing), or **unified online**, **unified
away**, **unified transfers only**, and **unified offline** states
(if you do use omnichannel routing).

If you see gaps in your agents’ state information, you can update the **Agent
state** filter to include the **Disconnected** and **Unknown**
states, as well as custom states (if you use omnichannel routing). The
**Disconnected** value means that the agent’s connection to the system
was interrupted, which can happen when the agent’s computer is disconnected from
the internet, the internet browser puts the agent’s tab to sleep, or other
circumstances. The **Unknown** value means that Explore was unable to return
a value for the agent’s state.

Additionally, if you use omnichannel routing, the report is filtered to include
only the **Unified** channel by default, but you can update the filter to
include other channels as needed.

If you apply a multi-day time filter to this report, the filter applies to both
the start time and the end time of an agent state. This means that the
**Duration** column might show more than 24 hours in a given state for a
single day. For an explanation of how this can happen, see [Why does the State Detail dashboard show a
duration of more than 24 hours for a single day?](https://support.zendesk.com/hc/en-us/articles/7679506638362)

#### State Detail tab report

This tab displays the following report:

- **Total time in state**: A table that shows, for each agent and each
  day, how long the agent spent in each state (including start time, end
  time, and duration) for each channel.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_omnichannel_db_details_report.png)

  If you use
  omnichannel routing, you can filter this report by both a specific
  channel (for example, **Messaging**) as well as the
  **Unified** channel. If you do, it’s important to note that
  the duration of time spent in a per-channel status equals the
  duration of time spent in a unified status plus any custom statuses
  that are mapped to that per-channel state. For details, see [Why is the per-channel agent
  status time different than the unified agent status
  time?](https://support.zendesk.com/hc/en-us/articles/6362240787226)

  Tip: To see per-channel status
  each custom status is mapped to, see [Viewing unified agent
  statuses](https://support.zendesk.com/hc/en-us/articles/5133588225690#topic_og3_1ms_bvb).

### Assigned work tab

The Assigned work tab contains reports that tell you the average work items
assigned to each agent for all channels and offer and acceptance counts for Chat
and Messaging only. You can filter the reports by **Date**, **Channel**,
**Group**, or **Agent name**.

#### Assigned work tab reports

The tab displays the following reports:

- **Average work items assigned (when online)**: A table that shows
  agents’ average used capacity while in an Online state per day.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_omnichannel_dashboard_avg_work_assigned.png)
- **Max and min work items assigned.** The maximum and minimum capacity
  used by agents each day for the past week.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_agent_state_activities_min_max.png)
- **Acceptance rate**: A table that shows the offer count, accepted
  count, and acceptance rate for each agent per day, broken out by
  channel. Available only for web and mobile messaging, social messaging,
  and live chat. Acceptance rate is not available if auto-accept or
  broadcast mode is used for routing, or if no work items were offered to
  or accepted by the agent.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_omnichannel_dashboard_acceptance_rate.png)