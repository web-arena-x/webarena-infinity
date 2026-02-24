# Viewing your CSAT (customer satisfaction) score and ratings

Source: https://support.zendesk.com/hc/en-us/articles/4408846011546-Viewing-your-CSAT-customer-satisfaction-score-and-ratings

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Professional or Enterprise |

If you've [enabled the customer satisfaction (CSAT) survey](https://support.zendesk.com/hc/en-us/articles/7689997846554), you can view details about your overall CSAT (customer satisfaction) results for all tickets on the Zendesk Support dashboard. You can view CSAT results for an individual in a ticket within Agent Workspace.

You can also view results in the dashboard and individual tickets. Additionally, agents can view their personal results in Agent Home.

Note: If you have the Zendesk QA add-on, you can view CSAT results in the Surveys dashboard. See [Using the surveys dashboard](https://support.zendesk.com/hc/en-us/articles/7043759414042).

This article includes the following topics:

- [Viewing overall CSAT results in the Support dashboard](#topic_mgy_kd5_qq)
- [Viewing CSAT results in a ticket](#topic_imh_cwy_vcc)
- [Viewing CSAT results on the agent's dashboard](#topic_jqt_n14_zcc)

## Viewing overall CSAT results in the Support dashboard

You can view details about your overall CSAT (customer satisfaction)
results on the Satisfaction tab of the Zendesk Support dashboard in Explore.

Users with the [Explore role](https://support.zendesk.com/hc/en-us/articles/4408836002970) of Admin or Editor can access the Support dashboard. If a user has the Explore role of Viewer, an Admin or Editor must share the dashboard with them before they can view it.

You must have received at least one response to view data in the dashboard (see [Sending a CSAT survey to your customers](https://support.zendesk.com/hc/en-us/articles/7689997846554)).

The responses for good and bad are mapped to the configured numerical rating scales for the CSAT. For example, for:

- 1-2 rating scales: 1 is bad and 2 is good
- 1-3 rating scales: 1-2 is bad and 3 is good
- 1-5 rating scales: 1-3 is bad and 4-5 is good

**To view CSAT results in the Support dashboard**

1. In [Explore](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the Dashboard icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dashboard_icon.png) ) in the left sidebar.
2. In the list of dashboards, select the **Zendesk Support** dashboard. The Zendesk Support dashboard opens.
3. In the dashboard, click the **Satisfaction** tab.

   ![Explore Satisfaction tab](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_satisfaction_tab.png)

For details of all the reports on this tab, see [Analyzing your Support ticket activity and agent performance](https://support.zendesk.com/hc/en-us/articles/4408835846810#topic_ijh_ybj_z3b).

Tip: If you have Suite Professional and above or Support with Explore Professional, you can expand on the pre-built dashboards to create your own CSAT reports. See [Creating queries](https://support.zendesk.com/hc/en-us/articles/4408821589530) and [Metrics and attributes for Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408827693594).

## Viewing CSAT results in a ticket

You can view the CSAT rating for an individual ticket in the ticket itself.

**To view the rating for a ticket**

- In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), open any ticket that has received a CSAT rating, then view the rating at the top of the ticket.

 To view responses to drop-down and open-ended questions, click **Events**, then scroll to the relevant event.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-csat-agentworkspace.png)

## Viewing CSAT results on the agent's dashboard

The results of customer satisfaction surveys for agents are shown in the agent's dashboard and in a view called **Rated tickets from the last 7 days**.

**To view your agent CSAT results on the agent's dashboard**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the Home (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_dashboard.png)) icon in the sidebar.
2. Use [Agent Home](https://support.zendesk.com/hc/en-us/articles/5064623131418)to view:
   - **Ticket statistics**: The number of your tickets with a **Good** Customer satisfaction (CSAT) rating, a **Bad** CSAT rating, and tickets **Solved** by you this week. See [Sending a CSAT survey to your customers](https://support.zendesk.com/hc/en-us/articles/7689997846554).
   - **Satisfaction statistics**: Satisfaction statistics for you and your team, expressed as the % satisfaction attainment for the past 60 days.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/agent_home_main_page_chat.png)

The calculation of the overall satisfaction rating uses the following simple formula:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/csr_score_calculation.png)

This means that the score is an average of the total positive ratings from the past 60 days. An agent with a score of 90% means that over the past 60 days, 90% of the ratings they received were positive.

Agents, groups, and the account all have scores. The overall account score (in the example above, 95%) is the average for all agents in Zendesk Support. The two ratings provide feedback about individual performance and the average performance of all agents.

Note: An overall rating score will not be shown until 30 tickets are rated. This applies at the agent, group, and account levels. This means that an agent needs 30 ratings, a group (all agents within the group) needs 30 ratings, and the account (all the agents in your Zendesk account) needs 30 ratings.

The view (**Rated tickets from the last 7 days**) gives you a quick overview of the rating activity, with a Satisfaction column containing both Good and Bad ratings. You can clone and modify this view or create your own. This view is inactivate by default.

The following rules apply to agents when using customer satisfaction rating:

- Agents cannot rate tickets.
- All agents see their ratings in their dashboard. This feature is enabled at the account level and applies to all agents in your Zendesk account. You can't exclude individual agents from receiving ratings on the tickets they are assigned to.

Additionally, ratings cannot be moderated. All ratings are shown.