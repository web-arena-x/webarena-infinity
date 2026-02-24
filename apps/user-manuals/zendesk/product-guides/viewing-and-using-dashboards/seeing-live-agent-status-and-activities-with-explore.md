# Seeing live agent status and activities with Explore

Source: https://support.zendesk.com/hc/en-us/articles/4422485166746-Seeing-live-agent-status-and-activities-with-Explore

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Enterprise or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Explore Enterprise |

Using live dashboards in Explore, you can see which agents are online and which open
tickets, conversations or chats, and calls they’re assigned to. This real-time capacity
reporting helps supervisors balance availability and workloads across teams, as well as
monitor individual agent performance, all from a central dashboard.

The instructions in this article work for the [prebuilt live dashboard](https://support.zendesk.com/hc/en-us/articles/4408843771546) as well as any live dashboards built
in the beta dashboard builder that have [reports with drill in enabled](https://support.zendesk.com/hc/en-us/articles/4408830235930).

Tip: Zendesk now offers [real-time monitoring](https://support.zendesk.com/hc/en-us/articles/9757124462234), which enhances your reporting by
focusing on use cases, offering immediate decision-making insights, and tracking
trends for up to seven days.

This article includes the following topics:

- [Viewing agent status and workload](#topic_rsp_zhc_psb)
- [Seeing which open work items are assigned to an agent](#topic_ckg_x3c_psb)
- [Changing agent status](#topic_lxc_xpr_31c)

Related articles:

- [Seeing live agent status with Explore: Use
  cases](https://support.zendesk.com/hc/en-us/articles/6358278450202)
- [Overview of the Explore live
  dashboard](https://support.zendesk.com/hc/en-us/articles/4408843771546)

## Viewing agent status and workload

You can drill into a live dashboard to see which statuses agents are in and what
their workloads are across channels.

If you’ve [turned on omnichannel routing](https://support.zendesk.com/hc/en-us/articles/5866925319962), you can
also see which [custom statuses](https://support.zendesk.com/hc/en-us/articles/4410525357594) agents are in and what their [workload capacity](https://support.zendesk.com/hc/en-us/articles/4776409839770) is across channels.

Important: If you don't use omnichannel routing,
get the most value out of this information by reminding your agents to sign in
and out of Zendesk to accurately represent their shifts. This is particularly
important for the Support channel, where only two default agent states are
reported (Online and Offline). If agents don’t sign out, Explore will show them
as always online. For more information, see [Why does the Explore dashboard show too many
online agents?](https://support.zendesk.com/hc/en-us/articles/5516998359450)

**To view agent status and workload**

1. In Explore, click the **Dashboard** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dashboard_icon.png)).
2. Open a live dashboard.
3. (Optional) Filter the dashboard based on the specific groups or brands you want
   to see. You can choose up to five attribute values per filter.
4. Click any agent status metric and select **Drill in**. Agent status metrics
   include **Agents online**, **Agents offline**, **Agents away**,
   **Agents invisible**, and **Agents transfer only**, as well as custom
   statuses created as part of omnichannel routing.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_live_metric_agents_online_drill_in.png)

   Note: If you drill into a live agent status metric
   with more than 100 agents, you won't see the list of agents in that
   status. Use dashboard filters to lower the number of agents that a live
   metric reflects. When you do, you'll be able to see the list of agents
   when you drill into the metric.

   The **Agent workload vs. capacity** window opens, showing a list of
   agents and the following columns:

   - **Status**: Which default or custom status each agent is
     currently in. If you use omnichannel routing, this column is called
     **Unified status**
   - **Time in status**: How long each agent has been in their current
     status
   - **Emails**: How many tickets each agent is assigned to
   - **Messages**: How many active messaging conversations each agent
     has
   - **Chats**: How many chats each agent is currently handling
   - **Calls**: How many calls each agent is currently
     handling

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_live_dashboard_workload_capacity_nov17.png)

     If you use
     omnichannel routing, hover over the **Emails**,
     **Messages**, **Chats**, or **Calls** column to see
     the number of work items assigned to an agent compared to their
     set capacity. A dash (-) in the **Emails**, **Messages**,
     **Chats**, or **Calls** column means the agent does
     not have access to that channel (if you're filtering by unified
     status), or the agent is not in the status for that channel (if
     you're filtering by a channel-specific status).

     If you
     don't use omnichannel routing, a dash always appears in these
     columns because capacity information is not available without
     omnichannel routing.
5. (Optional) Click **Filter** to filter the list by the following options:
   - **Channel**: Includes **Email**, **Messaging** or **Chat**,
     and **Talk**.
   - **Status by channel**: Includes the agent statuses that apply to
     individual channels.
   - **Group**: (Appears only if you filtered the dashboard by group in
     step 3 above) Includes the groups in your account.
   - **Unified status**: (Appears only if you use omnichannel routing)
     Includes the [default unified agent statuses and
     any custom statuses](https://support.zendesk.com/hc/en-us/articles/4410525357594) you've created.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_live_dashboard_uas_filters_nov17.png)

     You can filter by
     multiple channels and statuses at the same time. When filtering,
     note that some channel-specific statuses (like Invisible for Chat)
     are not reflected by the default unified statuses. Additionally,
     custom statuses can be mapped to different statuses for each
     channel. If you don't see the results you expect, check the filters
     to make sure you're not unintentionally excluding agents based on
     channel or custom status.

     Depending on which live agent status
     metric you drilled into in step 4, filters might already be applied
     to the list. For example, if you drilled into the **Support -
     Agents online** metric, the results are pre-filtered by the
     **Email** channel and the **Online** status.

     Tip: If you’ve [turned on omnichannel
     routing](https://support.zendesk.com/hc/en-us/articles/5866925319962), you have access to unfiltered [unified agent status live
     metrics](https://support.zendesk.com/hc/en-us/articles/4408843357210#topic_cg5_4x5_zyb).

     When you filter by channel, the list shows only the workload
     columns that apply to the selected channels. For example, if you
     filter by **Talk**, you'll see the **Calls** column, but not
     the **Emails**, **Messages**, or **Chats**
     columns.

Note that the **Agent workload vs. capacity** window doesn't update in real time
when it's open and no actions are being performed. When you take an action (such as
updating an agent status or changing your filters) or close and reopen the window,
the data is refreshed.

Tip: For more about effectively monitoring agent
status with an Explore live dashboard, see [Seeing live agent status with Explore: Use
cases](https://support.zendesk.com/hc/en-us/articles/6358278450202).

## Seeing which open work items are assigned to an agent

After opening the list of agents, you can select a specific agent to see which open
work items are assigned to them.

**To see which open work items are assigned to an agent**

1. [Open the Agent workload vs.
   capacity window.](#topic_rsp_zhc_psb)
2. Search for a specific agent in the search bar at the top. Search results are
   limited to 50 results. Make sure your search is as specific as possible so you
   can find the agent you want.

   Use a caret (^) to specify that the agent's name
   must start with your exact search term. (For example, ^Alex will return
   "Alex Jensen," but not "Maria Alexander.")

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/explore_workload_vs_capacity_searching_agent.png)
3. Select the agent you want to see work items for.

   The **Agent work items**
   window appears and shows the agent's overall status and status for each
   channel, along with details about the tickets, messaging conversations or
   chats, and calls the agent is working on.

   The **Time in status**
   shown is the time for the channel you selected when you first drilled in.
   For example, if you drilled into this screen from a Support metric, the time
   in status shown is the time active for the Support channel.

   If you use
   omnichannel routing, this window also shows the agent’s capacity underneath
   their status for each channel. See [Creating capacity rules to balance agent
   workload](https://support.zendesk.com/hc/en-us/articles/4776409839770) for more information on setting agent
   capacity.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_live_metric_work_item_drill_in_nov17.png)
4. (Optional) Use the **Filter** drop-down to select a channel and see only work
   items for that channel.
5. Select a work item to see more details.

   For each ticket, the window shows the
   following details:

   - **Requester**: The user who is asking for support through a
     ticket
   - **Ticket ID**: The unique ID number of the ticket
   - **Status**: What status the ticket is currently in (New, Open,
     Pending, On-hold, Closed)
   - **Account name**: The Zendesk account name (described in [Branding the Support
     interface](https://support.zendesk.com/hc/en-us/articles/4408842817434#topic_j34_xj2_4nb))
   - **Date requested**: The date the ticket was submitted
   - **Priority**: How urgent the ticket is
   - **Group**: What group the ticket is currently assigned to
   - **Last updated**: The date the ticket was last updated

   For each messaging conversation, the window shows the following
   details:

   - **Requester**: The name of the user the agent is messaging
     with
   - **Ticket ID**: The unique ID number of the ticket
   - **Originating channel**: The channel that the conversation
     started on. Possible values include Email and Messaging.
   - **Duration**: How long the agent has been working on the ongoing
     conversation

   For each chat, the window shows the following details:

   - **Requester**: The name of the user the agent is chatting
     with
   - **Chat ID**: The unique ID number of the chat
   - **Originating channel**: The channel that the message came from.
     Possible values include Facebook Messenger and Chat.
   - **Duration**: How long the chat has been active

   For each call, the window shows the following details:

   - **Caller**: The phone number of the caller
   - **Call ID**: The unique ID number of the ticket associated with
     the call
   - **Call type**: The type of call (described in [Metrics and attributes for
     Zendesk Talk](https://support.zendesk.com/hc/en-us/articles/4409156145434#topic_w5f_xdh_5bb))
   - **Duration**: How long the call has been going on

## Changing agent status

From the list of agents, users with permission can change the status of a single
agent or multiple agents. To change agent status, you must be a Support admin (all
plans) or have a custom role with the Change agent status setting (Enterprise plans
only). See [Giving users access to Explore](https://support.zendesk.com/hc/en-us/articles/4408836002970).

For example, you might change an agent's status if they completed their shift but
forgot to sign out to mark themselves unavailable.

**To change agent status**

1. [Open the Agent workload vs.
   capacity window](#topic_rsp_zhc_psb).
2. Select the check box to the left of each agent you want to change the status of.
   You may select up to 500 agents at a time.

   If you search for an agent, search
   results are limited to 50 results. Make sure your search is as specific as
   possible so you can find the agent you want.
3. In the bottom bar, click **Change status** and select the status you want to
   set for the agent.

   To select a custom status, click **Other statuses** and
   then select the appropriate custom status.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_workload_vs_capacity_change_status.png)

   When you select a status, the
   agent’s status is immediately updated. You don’t need to save or confirm.

Note: Currently, when a manager or supervisor changes an
agent’s status for them, that change isn’t reflected in the [Account status](https://support.zendesk.com/hc/en-us/articles/4408842880282-Zendesk-Chat-triggers-conditions-and-actions-reference#:~:text=Online%20statuses-,Account%20status,-Status%20of%20your) or [Department status](https://support.zendesk.com/hc/en-us/articles/4408842880282-Zendesk-Chat-triggers-conditions-and-actions-reference#:~:text=trigger%20will%20fire.-,Department%20status,-Status%20of%20the) condition in Chat
triggers for the [“Messaging” and “Chat and messaging”
channels](https://support.zendesk.com/hc/en-us/articles/4408822204698-About-messaging-triggers-in-the-Chat-dashboard#:~:text=Updated%20action%20options-,The%20Channel%20menu,-The%20new%20Channel). However, these conditions work correctly when the agent
[updates their own status](https://support.zendesk.com/hc/en-us/articles/4410545721114).