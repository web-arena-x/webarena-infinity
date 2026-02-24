# Metrics and attributes for agent state, activity, and productivity

Source: https://support.zendesk.com/hc/en-us/articles/5600290657434-Metrics-and-attributes-for-agent-state-activity-and-productivity

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

This article defines the metrics and attributes you can use to [create reports](https://support.zendesk.com/hc/en-us/articles/4408821589530) based on agent state, activity, and productivity. These datasets are also used for the agent state prebuilt dashboards. See [Analyzing agent productivity](https://support.zendesk.com/hc/en-us/articles/9204214290714).

Important: To get the most value out of these datasets, remind your agents to sign in and out of Zendesk to accurately represent their shifts. This is particularly important for the Support channel, where only two states are reported (Online and Offline). If agents don’t sign out, reports will show them as always online.

This article contains the following topics:

- [Agent state dataset](#topic_vyt_whf_2xb)
- [Agent state daily dataset](#topic_t4m_xhf_2xb)
- [Agent productivity dataset](#topic_v33_zw2_z1c)

## Agent state dataset

The Agent state dataset contains metrics and attributes that relate to when an agent enters a given state and how long they’re in that state. Supervisors can use this information to create timestamp reports that give them an in-depth look at how agents spent their time.

In this dataset, an agent’s time in a given state is recorded only after their state changes. This means that if an agent is in a single state for the entire duration of the report’s time period, their state is not reported, as there have been no changes to it. To report on agent states with or without changes, use the [Agent state daily](#topic_t4m_xhf_2xb) dataset instead.

Note: Due to the volume of data recorded, this dataset retains data from events that completed in the last 90 days. This is regardless of the event start time, which might be older than 90 days.

This section contains the following topics:

- [Agent state metrics](#topic_ey1_d3f_2xb)
- [Agent state attributes](#topic_tg5_d3f_2xb)

### Agent state metrics

This section lists and defines all metrics available in the Agent state dataset.

Table 1. Agent state metrics

| **Metric** | **Definition** | **Explore formula** |
| --- | --- | --- |
| Agent time in state / seconds | The time spent in seconds by the agent in a given state per channel. When you add this metric to a report and slice the results by an agent attribute, you must also add the **Group** attribute. If you don't, an agent's total time is counted for each group they're in. When you add this metric to a report and slice the results by the **State** attribute, you must also add the **Channel** attribute. If you don’t, the time spent in per-channel states is counted multiple times. See [Why is the per-channel agent status time different than the unified agent status time?](https://support.zendesk.com/hc/en-us/articles/6362240787226) | |

### Agent state attributes

This section lists and defines all attributes available in the Agent state dataset.

Table 2. Agent state attributes

| **Attribute** | **Definition** |
| --- | --- |
| Group ID | The ID number of the group. |
| Group name | The name of the assigned group. |
| Channel | The channel that an agent state relates to. Possible values include **Support**, **Talk**, **Messaging**, **Chat**, and **Unified**. |
| State | The state of the agent. Possible values include: - **away**, **invisible**,   **offline**, **online**, and **transfers   only** (for per-channel states) - **unified away**, **unified   offline**, **unified online**, and **unified   transfers only** (for [standard unified   agent statuses](https://support.zendesk.com/hc/en-us/articles/5133523363226)) - **disconnected** (means that the   agent’s connection to the system was interrupted,   which can happen when the agent’s computer is   disconnected from the internet, the internet browser   puts the agent’s tab to sleep, or other   circumstances) - **unknown** (means that Explore was   unable to return a value for the agent’s state) - Any [custom unified   agent statuses you’ve created](https://support.zendesk.com/hc/en-us/articles/4410525357594) in your   account   When you add this attribute to a report, you must also add the **Channel** attribute. If you don’t, the time spent in per-channel states is counted multiple times. See [Why is the per-channel agent status time different than the unified agent status time?](https://support.zendesk.com/hc/en-us/articles/6362240787226) |
| Agent name | The name of the agent. |
| Agent role | The role of the agent. |
| Agent ID | The ID of the agent. |
| Agent email | The email address of the agent. |
| Agent external ID | The external ID of the agent. |
| Agent locale | The locale of the agent. |
| Agent is moderator | Whether the agent is a moderator. |
| Agent status | The status of the agent. Possible values are **Active** or **Suspended**. |
| Agent active | Whether the agent is active. |
| Agent suspended | Whether the agent is suspended. |
| Agent organization ID | The organization ID of the agent. |
| Agent tags | Tags added to the agent. |
| Agent timezone | The time zone of the agent. |
| State start time | A collection of attributes in different units of time that record the time at which an agent entered a state. |
| State end time | A collection of attributes in different units of time that record the time at which an agent exited a state. |

## Agent state daily dataset

The Agent state daily dataset contains metrics and attributes that relate to how groups and agents spend their time across channels. This dataset helps you understand, at a daily level, agents’ total time spent in certain states.

Data in this dataset is aggregated at the end of each day and reported in the viewer's time zone (See [Which time zone does Zendesk use?](https://support.zendesk.com/hc/en-us/articles/4408821092762)). Because this dataset aggregates activity at the daily level and does not provide hourly granularity, the **Date - Hour** attribute will always return a value of 0.

Because the data is aggregated daily, any group membership changes are reflected only in the following day’s data. For example, an agent is moved from Group A to Group B at noon on January 20. The data for January 20 shows them in Group A (even after they were moved), while the data for January 21 shows them in Group B.

Note: In cases where Zendesk needs to reload the data on your account, this dataset retains data only from the previous 90 days due to its reliance on the Agent state dataset.

This section contains the following topics:

- [Agent state daily metrics](#topic_sf5_n3f_2xb)
- [Agent state daily attributes](#topic_imn_43f_2xb)

### Agent state daily metrics

This section lists and defines all metrics available in the Agent state daily dataset.

Table 3. Agent state daily metrics

| **Metric** | **Definition** | **Explore formula** |
| --- | --- | --- |
| Agent daily time in state | The total time per day spent by agents in a given state per channel. This metric is aggregated daily and cannot be broken down into smaller time increments. When you add this metric to a report and slice the results by an agent attribute, you must also add the **Group** attribute. If you don't, an agent's total time is counted for each group they're in. When you add this metric to a report and slice the results by the **State** attribute, you must also add the **Channel** attribute. If you don’t, the time spent in per-channel states is counted multiple times. See [Why is the per-channel agent status time different than the unified agent status time?](https://support.zendesk.com/hc/en-us/articles/6362240787226) | |

### Agent state daily attributes

This section lists and defines all attributes available in the Agent state daily dataset.

Table 4. Agent state daily attributes

| **Attribute** | **Definition** |
| --- | --- |
| Group ID | The ID number of the group. |
| Group name | The name of the assigned group. |
| Channel | The channel that an agent state relates to. Possible values include **Support**, **Talk**, **Messaging**, **Chat**, and **Unified**. |
| State | The state of the agent. Possible values include: - **away**, **invisible**,   **offline**, **online**, and **transfers   only** (for per-channel states) - **unified away**, **unified   offline**, **unified online**, and **unified   transfers only** (for [standard unified   agent statuses](https://support.zendesk.com/hc/en-us/articles/5133523363226)) - **disconnected** (means that the   agent’s connection to the system was interrupted,   which can happen when the agent’s computer is   disconnected from the internet, the internet browser   puts the agent’s tab to sleep, or other   circumstances) - **unknown** (means that Explore was   unable to return a value for the agent’s state) - Any [custom unified   agent statuses you’ve created](https://support.zendesk.com/hc/en-us/articles/4410525357594) in your   account   When you add this attribute to a report, you must also add the **Channel** attribute. If you don’t, the time spent in per-channel states is counted multiple times. See [Why is the per-channel agent status time different than the unified agent status time?](https://support.zendesk.com/hc/en-us/articles/6362240787226) |
| Agent name | The name of the agent. |
| Agent role | The role of the agent. |
| Agent ID | The ID of the agent. |
| Agent email | The email address of the agent. |
| Agent external ID | The external ID of the agent. |
| Agent locale | The locale of the agent. |
| Agent is moderator | Whether the agent is a moderator. |
| Agent status | The status of the agent. Possible values are **Active** or **Suspended**. |
| Agent active | Whether the agent is active. |
| Agent suspended | Whether the agent is suspended. |
| Agent organization ID | The organization ID of the agent. |
| Agent tags | Tags added to the agent. |
| Agent timezone | The time zone of the agent. |
| Time - Agent time in state | A collection of attributes in different units of time that return when the agent’s state was recorded. |

## Agent productivity dataset

The Agent productivity dataset contains metrics and attributes that relate to work items offered and assigned to agents and how agents used their capacity. Supervisors can use this information to create reports that provide an in-depth look at the utilization of their agent capacity.

This dataset reports on the number of work items newly assigned to an agent during a given time period. It doesn’t report on the total number of existing work items where the agent is listed as the assignee. To report on existing work items instead, use the dataset for the channel you’re interested in. For example, use the Support - Tickets dataset to see how many total tickets are assigned to an agent.

Data in this dataset is aggregated hourly, meaning reports can’t be broken down into smaller time increments.

If an agent has no new work items assigned to them for a given hour, no data is recorded for that timeframe. This means reports will include gaps for hours during which an agent wasn’t assigned any work items. In the example report below, no work items were assigned to the agent during the 15:00 hour, so no data was returned.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_agent_productivity_dataset_example_15.png)

Similarly, if an agent wasn’t in the Online state for a given hour, no data is recorded for the Agent average used capacity metric.

Note: Due to the volume of data recorded, this dataset retains data from events that completed in the last 90 days. This is regardless of the event start time, which might be older than 90 days.

This section contains the following topics:

- [Agent productivity metrics](#topic_nsw_1x2_z1c)
- [Agent productivity attributes](#topic_bmv_cx2_z1c)

### Agent productivity metrics

This section lists and defines all metrics available in the Agent productivity dataset.

| | |
| --- | --- |
| **Metric** | **Definition** |
| Agent average used capacity | The average capacity used by an agent for a channel during a period (while they are in the Online state only). A null value means the agent was not online. A **0.00** value means the agent was assigned no work items during that period. Note: The metrics omnichannel\_agent\_productivity\_capacity\_seconds and omnichannel\_agent\_productivity\_agent\_online\_seconds shown in the formula are used only for calculating average used capacity and can't be added directly to a report. Formula: SUM(omnichannel\_agent\_productivity\_capacity\_seconds) /SUM(omnichannel\_agent\_productivity\_agent\_online\_seconds) |
| Agent max used capacity | The maximum capacity used by an agent for a channel during a period. |
| Agent min used capacity | The minimum capacity used by an agent for a channel during a period. |
| Max capacity limit | The maximum capacity assigned to an agent by the admin per channel. |
| Offer count | The number of work items offered to the agent during a specific period. Available only for web and mobile messaging, social messaging, and live chat. Acceptance rate is not available if auto-accept or broadcast mode is used for routing. Offer count is measured at the agent level, meaning this metric returns values for the agent regardless of group filters. |
| Accepted count | The number of work items accepted by the agent during a specific period. Available only for web and mobile messaging, social messaging, and live chat. Acceptance rate is not available if auto-accept or broadcast mode is used for routing. Accepted count is measured at the agent level, meaning this metric returns values for the agent regardless of group filters. |
| Acceptance rate | The ratio of accepted work items to the total work items assigned to an agent during a specific period. Available only for web and mobile messaging, social messaging, and live chat. Acceptance rate is not available if auto-accept or broadcast mode is used for routing. If no work items are offered to or accepted by an agent in the given time period, this metric returns a null value. Acceptance rate is measured at the agent level, meaning this metric returns values for the agent regardless of group filters. Formula: IF (ATTRIBUTE\_ADD(SUM(Offer count),[Agent productivity start time - Date]) > 0) THEN 100\*SUM(Accepted count)/SUM(Offer count) ELSE 0 ENDIF |

### Agent productivity attributes

This section lists and defines all attributes available in the Agent productivity dataset.

| | |
| --- | --- |
| **Attribute** | **Definition** |
| Group ID | The ID number of the group. |
| Group name | The name of the assigned group. |
| Channel | The channel that a capacity value relates to. Possible values include Support, Talk, Messaging, and Chat. |
| Agent name | The name of the agent. |
| Agent role | The role of the agent. |
| Agent ID | The ID of the agent. |
| Agent email | The email address of the agent. |
| Agent external ID | The external ID of the agent. |
| Agent locale | The locale of the agent. |
| Agent is moderator | Whether the agent is a moderator. |
| Agent status | Whether an agent is active or suspended. |
| Agent active | Whether the agent is active. |
| Agent suspended | Whether the agent is suspended. |
| Agent organization ID | The organization ID of the agent. |
| Agent tags | Tags added to the agent. |
| Agent timezone | The time zone of the agent. |
| Time - Agent productivity start time | A collection of attributes in different units of time that return when work item capacity was recorded. The start time is recorded when the work item is assigned to the agent. |
| Time - Agent productivity end time | A collection of attributes in different units of time that return when the end time when work item capacity was recorded. The end time is recorded when the work item is solved or assigned to another agent. |