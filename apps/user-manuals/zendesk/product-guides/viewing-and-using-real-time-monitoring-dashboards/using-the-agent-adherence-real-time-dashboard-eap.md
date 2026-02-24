# Using the agent adherence real-time dashboard (EAP)

Source: https://support.zendesk.com/hc/en-us/articles/10115130172826-Using-the-agent-adherence-real-time-dashboard-EAP

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

Verified AI summary ◀▼

The agent adherence real-time dashboard helps you track agent schedule compliance, take quick corrective actions, and optimize resource allocation. It offers an overview of agent adherence and detailed insights into agent activity, including current status and adherence duration. Use this tool to monitor performance, improve accountability, and support coaching conversations without navigating complex steps.

The agent adherence real-time dashboard helps workforce managers, supervisors, and admins
track whether agents are working according to their planned schedules. By integrating
[Zendesk Workforce Management (WFM)](https://support.zendesk.com/hc/en-us/articles/6514644101914) data with
real-time analytics, the dashboard provides a single view of how your team is performing
against adherence goals.

WFM determines agent activity by monitoring work on tickets, attendance to general tasks,
or from agent status (if [Unified Agent Status](../setting-up-workforce-management-wfm-add-on/turning-on-unified-agent-status-synchronization-for-zendesk-wfm.md) is turned on in WFM).
Whenever an agent's activity matches their scheduled workflow, general task, or status,
the agent is considered in adherence. For more information, see [About the Agent activity page](https://support.zendesk.com/hc/en-us/articles/6443347506970).

The agent adherence dashboard helps you:

- **Monitor schedule compliance in real time**: Spot which agents are not following
  their planned schedules.
- **Take corrective action quickly**: Identify unplanned offline time or gaps in
  activity before they impact service levels.
- **Optimize resource allocation**: Balance workloads across agents by tracking who
  is available, who is working, and who might need coaching or adjustments.
- **Improve reporting and accountability**: Use drill-down reports and activity
  details for coaching conversations, compliance audits, or operational reviews.

This dashboard contains the following sections:

- [Accessing the agent adherence dashboard](#topic_fld_w55_whc)
- [Understanding the agent adherence reports](#topic_ykt_gbv_whc)
- [Signing up for the agent adherence dashboard EAP](#topic_skg_v4w_b3c)

## Accessing the agent adherence dashboard

If you've signed up for the EAP, you'll find this dashboard as a tab in the [Agent productivity real-time dashboard](https://support.zendesk.com/hc/en-us/articles/9757103842458).

**To access the agent adherence dashboard**

1. In the Zendesk product tray, click **Analytics**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/rtm_zra_19.png)

   Analytics opens to the dashboards library
   page.
2. Click the real-time monitoring home icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/rtm_zra_icon.png)).

   The real-time monitoring home page
   opens.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zra_rob_22.png)
3. In the Agent productivity section, click **View**.
4. In the agent productivity dashboard, click the **Agent adherence** tab. The
   agent adherence dashboard opens.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/real-time_adherence_500.png)

## Understanding the agent adherence reports

This tab gives you information about whether agents are working according to their
planned schedules. The reports can be filtered by brand, group, agent, agent status,
activity, and adherence status. The reports you'll see depend on whether or not
you're using [omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4409149119514).

The tab contains the following reports:

- **Agent adherences:** A pie chart displaying the number of agents in and out
  of adherence. Click one of the chart sections to view each agent in or out of
  adherence.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/real-time_adherence_502.png)
- **Top 10 agents by out of adherence duration:** Displays the ten agents who
  have been out of adherence for the longest time in the last 60 minutes. Red bars
  indicate periods where an agent was out of adherence, while gray bars show when
  they were in adherence. This view helps you quickly identify opportunities to
  improve your agents’ overall performance and schedule adherence.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/real-time_adherence_503.png)
- **Agent activity and adherence:**

  In this table, you’ll find a detailed
  table of all agents and their adherence status, including:

  - **Agent, Group, and Brand**: The agent’s name and organizational
    attributes.
  - **Activity**: Current real-time status tracked in WFM, such as a
    general task or a ticket workstream
  - **Activity duration**: The length of time spent in the current
    adherence status.
  - **Current ticket**: If an agent is working on a ticket, you’ll see
    the ticket ID and how long they’ve been on it.
  - **Adherence status**: Indicates whether the agent is in or out of
    adherence.![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/real-time_adherence_504.png)

The following report is displayed if you are not using omnichannel routing:

- **Clocked-in agents by activity:** A pie chart showing the number agents
  working on the following activities:
  - On a ticket
  - In a paid [general task](https://support.zendesk.com/hc/en-us/articles/7069811858586)
  - In an unpaid general task
  - [Untracked](https://support.zendesk.com/hc/en-us/articles/6443376913818#topic_xwv_3n4_52c__untracked_time)

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/real-time_adherence_501.png)

The following reports are displayed if you are using omnichannel routing:

- **Out of adherence: Offline:** Displays the number of agents who are out of
  adherence and currently offline.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/real-time_adherence_506.png)
- **In adherence: Not on a ticket:** Displays the number of agents who are in
  adherence and are not working on a ticket.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/real-time_adherence_507.png)

## Signing up for the agent adherence dashboard EAP

You can sign up for the agent adherence dashboard EAP right from Zendesk Admin
Center.

**To sign up for the agent adherence dashboard EAP**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Roles**.
   **Workspaces** > **Analytics**.
2. On the Analytics page, select **WFM agent adherence in real-time monitoring
   (EAP)**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/eap_sign_up.png)

The EAP will be activated in your account. It might take up to an hour before you see
the new dashboard.