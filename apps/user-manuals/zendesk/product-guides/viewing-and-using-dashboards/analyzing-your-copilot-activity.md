# Analyzing your Copilot activity

Source: https://support.zendesk.com/hc/en-us/articles/9308443151258-Analyzing-your-Copilot-activity

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Copilot |

Verified AI summary ◀▼

Monitor your Copilot activity with the prebuilt Agent productivity dashboard. Track how agents use AI capabilities like Auto assist, AI suggestions, and generative AI tools. Customize the dashboard or create detailed reports to better understand adoption, performance, and workflow optimization opportunities. Use filters to view metrics and reports by time, agent, ticket group, and more.

Zendesk analytics features a prebuilt dashboard to help you monitor your Copilot
activity. The Zendesk Copilot: Agent productivity dashboard provides a centralized view
of how agents are interacting with Zendesk Copilot AI capabilities across three key
areas: Auto assist, AI suggestions, and generative AI agent tools. This dashboard helps
you understand adoption, track performance, and identify opportunities to optimize
workflows using AI.

You can edit and customize the dashboard by cloning it (see [Cloning dashboards](https://support.zendesk.com/hc/en-us/articles/4408821374362)).

Tip: If you need something more complex, you can write your own reports using a wide
range of metrics and attributes. See [Getting started creating queries](https://support.zendesk.com/hc/en-us/articles/4408839341082).

The information in dashboards is updated on a schedule. The schedule depends on which
Explore plan you're using. See [Data refresh intervals for Explore plans](https://support.zendesk.com/hc/en-us/articles/4408823242778).

This article contains the following topics:

- [Accessing the Zendesk Copilot: Agent productivity dashboard](#topic_dr1_2yr_mfc)
- [Understanding the Zendesk Copilot: Agent productivity dashboard reports](#topic_axh_2yr_mfc)

## Accessing the Zendesk Copilot: Agent productivity dashboard

Use the following procedure to access the Zendesk Copilot: Agent
productivity dashboard.

**To access the Zendesk Copilot: Agent productivity dashboard**

1. In analytics, click the **Dashboard** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dashboard_icon.png)) in the left sidebar.
2. From the list of dashboards, click the **Zendesk Copilot: Agent
   productivity** dashboard.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_copilot_dashboard_new_tab.png)

## Understanding the Zendesk Copilot: Agent productivity dashboard reports

This dashboard contains the following tabs:

- [Auto assist tab](#topic_z5s_jj5_fgc)
- [AI suggestions tab](#topic_uww_nyr_mfc)
- [AI agent tools tab](#topic_ulx_nyr_mfc)

### Auto assist tab

The **Auto assist** tab contains reports about agents' usage and acceptance of
[auto assist](https://support.zendesk.com/hc/en-us/articles/8013454025114) suggestions.

You can filter the reports by time, auto assist procedure, agent name, ticket
group, ticket brand, ticket form, and ticket channel.

#### Auto assist tab headline metrics

This tab displays the following headline metrics (KPIs):

- **Agents accepted auto assists**: The number of agents who accept
  an auto assist suggestion at least once.
- **Tickets with all auto assists accepted**: The number of tickets
  where an auto assist suggestion was accepted at least once.
- **Applied suggestions**: The number of suggestions applied by
  agents.
- **Acceptance rate**: The number of auto assist suggestions that
  were accepted, divided by the total number of auto assist
  suggestions shown.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_auto_assist_KPIs.png)

  See the
  [Auto assist metrics](https://support.zendesk.com/hc/en-us/articles/6961660060186#topic_qsz_4fd_mfc)
  for more information.

#### Auto assist tab reports

This tab displays the following reports:

- **Suggestions by type and status**: A pie chart showing the
  number of auto assist suggestions by type (reply or action) and
  whether they were accepted or not.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_auto_assist_suggestions_type.png)
- **Actions executed by auto assist**: A bar chart showing the
  number of actions that were executed by auto assist.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_auto_assisst_actions_repor.png)
- **Auto assists applied by week and procedure**: A graph showing
  the number of auto assist procedures applied by auto assist by
  week.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_auto_assist_week_procedure.png)
- **Procedure adoption and performance**: A list of procedures,
  with details about their performance.
- **Auto assists usage by agent**: A list of agents that shows
  their auto assist usage.

### AI suggestions tab

The **AI suggestions** tab contains reports about agents' usage and acceptance
of suggestions from AI features including [merging suggestions](https://support.zendesk.com/hc/en-us/articles/8044075423514-Turning-on-merging-suggestions), [quick answers](https://support.zendesk.com/hc/en-us/articles/8079579364250-Turning-on-quick-answers-for-Agent-Workspace), [similar tickets](../setting-up-ai-powered-agent-tools/turning-on-similar-tickets.md), [suggested first replies](../setting-up-ai-powered-agent-tools/turning-on-suggested-first-replies.md), and [suggested macros](../setting-up-ai-powered-agent-tools/turning-on-suggested-macros.md). You can filter the
reports by time, AI suggestion type, ticket group, agent name, ticket brand,
ticket form, and ticket channel.

#### AI suggestions tab headline metrics

This tab displays the following headline metrics (KPIs):

- **Agents accepted AI suggestions**: The number of agents who accepted
  an AI suggestion at least once.
- **Tickets with accepted AI suggestions**: The number of tickets where
  an AI suggestion was accepted at least once.
- **Accepted AI suggestions**: The number of AI suggestions accepted by
  agents.
- **Acceptance rate**: The number of AI suggestions that were accepted,
  divided by the total number of AI suggestions shown.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_copilot_suggestions_headline_metrics.png)

To understand what's considered an accepted suggestion for each feature, see
the [AI - Copilot suggestion
metrics](https://support.zendesk.com/hc/en-us/articles/6961660060186#topic_jf5_1fd_mfc).

#### AI suggestions tab reports

This tab displays the following reports:

- **Tickets with AI suggestions accepted vs ignored**: A pie chart
  showing the number of AI suggestions accepted by agents and the number
  of AI suggestions that were ignored by agents.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_copilot_suggestions_accepted_ignored_report.png)
- **AI suggestions by type**: A bar chart showing the number of
  suggestions accepted or ignored by feature type.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_copilot_suggestions_type_report.png)
- **AI suggestions by date and type**: A graph showing the number of
  tickets with an AI suggestion shown at least once by date and feature
  type.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_copilot_suggestions_date_type.png)
- **AI suggestions usage by agent**: A list of agents that shows the
  number of tickets an agent worked on with AI suggestions shown at least
  once, with accepted AI suggestions, with AI suggestions not accepted,
  and the agent's overall acceptance rate.

  You can change the list to
  show suggestion usage by ticket group, brand, channel, or
  form.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_suggestions_agents_usage_report.png)

### AI agent tools tab

The **AI agent tools** tab contains reports about agents’ use of [generative AI tools](https://support.zendesk.com/hc/en-us/articles/5608712782362), including expand,
summarize, custom prompt, make more friendly, make more formal, rewrite in your
tone, and simplify. You can filter the reports by time, ticket group, agent
name, AI usage type, ticket brand, ticket channel, and ticket assignee.

#### AI agent tools tab headline metrics

This tab displays the following headline metrics (KPIs):

- **AI tools usage events**: The number of times an AI tool was used by
  an agent.
- **Tickets with AI tools usage**: The number of tickets where an agent
  used AI tools.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_agent_tools_headline_metrics_2.png)

#### AI agent tools tab reports

This tab displays the following reports:

- **Tickets with AI tools usage**: A pie chart showing the total number
  of tickets split up by whether any of the AI tools were used. This
  report is not filterable by agent name.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_copilot_reports_AI_agents_tools_usage.png)
- **AI tools usage by type**: A bar chart showing the number of times
  an AI tool was used by feature type.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_ai_tools_type_report_2.png)
- **AI tools usage over time**: A graph showing the number of times the
  AI tools were used by feature type.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_ai_tools_over_time_report_2.png)
- **AI tools agent usage (top 10)**: A bar chart showing the top ten
  agents who've used the AI tools.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_copilot_tools_top_ten_agents.png)
- **Requester wait time by AI tool usage**: A bar graph showing the
  average requester wait time by day for tickets where an AI tool was
  used. This report is not filterable by agent name.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_ai_tools_wait_time_report_2.png)
- **Full resolution time on tickets with AI tool usage**: An area graph
  showing the average full resolution time by day for all tickets, split
  out by tickets where no AI tool was used (black) and tickets where an AI
  tool was used (blue). This report is not filterable by agent
  name.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_copilot_tools_full_resolution_report.png)