# Seeing live agent status with Explore: Use cases

Source: https://support.zendesk.com/hc/en-us/articles/6358278450202-Seeing-live-agent-status-with-Explore-Use-cases

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Enterprise or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Explore Enterprise |

Using an Explore live dashboard, you can [see the current status and workload of your agents](https://support.zendesk.com/hc/en-us/articles/4422485166746). If
you’ve [turned on omnichannel routing](https://support.zendesk.com/hc/en-us/articles/5866925319962), you can also
see which [unified and custom statuses](https://support.zendesk.com/hc/en-us/articles/4410525357594) agents are in.

Tip: Zendesk now offers [real-time monitoring](https://support.zendesk.com/hc/en-us/articles/9757124462234), which enhances your reporting by
focusing on use cases, offering immediate decision-making insights, and tracking
trends for up to seven days.

This article describes some common use cases for using an Explore live dashboard to
effectively monitor your agents’ statuses. The examples in this article are tailored to
team leads and supervisors who need to know the status of their agents in order to
ensure appropriate staffing levels and workload distribution.

The instructions in this article work for the [prebuilt live dashboard](https://support.zendesk.com/hc/en-us/articles/4408843771546) as well as any live dashboards built
in the beta dashboard builder that have [reports with drill in turned on](https://support.zendesk.com/hc/en-us/articles/4408830235930). To create a custom live
dashboard that shows you unified, custom, and channel-specific agent statuses at a
glance, see [Explore recipe: Creating a dashboard to report on
live agent status](https://support.zendesk.com/hc/en-us/articles/6358231294362).

Tip: You can also use a live dashboard to change an
agent’s status for them. See [Changing agent status](https://support.zendesk.com/hc/en-us/articles/4422485166746#topic_lxc_xpr_31c).

This article contains the following topics:

- [Use case 1: See which agents are online across all channels (Omnichannel routing only)](#topic_l1f_p44_jzb)
- [Use case 2: See which agents are in a custom status (Omnichannel routing only)](#topic_rx5_q44_jzb)
- [Use case 3: See which agents are online for any channel](#topic_rsm_s44_jzb)
- [Use case 4: See which agents are online for a specific channel](#topic_yp1_544_jzb)

Related articles:

- [Seeing live agent status and activities with
  Explore](https://support.zendesk.com/hc/en-us/articles/4422485166746)
- [Overview of the Explore live
  dashboard](https://support.zendesk.com/hc/en-us/articles/4408843771546)

## Use case 1: See which agents are online across all channels (Omnichannel routing only)

As a team lead with access to omnichannel routing, you want to see how many agents
are online across all channels right now. This gives you an overall picture of your
current available staffing, allowing you to make decisions across channels about how
much work can be done based on your available agents.

**To see which agents are online across all channels**

1. In Explore, click the **Dashboard** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dashboard_icon.png)) in the left sidebar.
2. Click the **Live data** dashboard, or select a custom live dashboard.
3. Click any agent status metric and select **Drill in**.
4. In the **Agent workload vs. capacity** window, click **Filter** and select
   **Unified status** > **Online**.

The list shows agents who are online across all channels.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_live_agent_status_use_case_1_nov17.png)

## Use case 2: See which agents are in a custom status (Omnichannel routing only)

As a team lead, you want to see which agents are listed as In training, a custom
status your organization created. Based on the way your organization [created the custom status](https://support.zendesk.com/hc/en-us/articles/4410525357594), you know that agents in
training are available to be assigned Support tickets, but are not available to take
calls or messages. This helps you understand which agents aren’t currently available
to handle time-sensitive work.

**To see which agents are in a custom status**

Tip: If you already have the **Agent workload vs.
capacity** window open, skip to step 4.

1. In Explore, click the **Dashboard** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dashboard_icon.png)) in the left sidebar.
2. Click the **Live data** dashboard, or select a custom live dashboard.
3. Click any agent status metric and select **Drill in**.
4. In the **Agent workload vs. capacity** window, click **Filter** and select
   **Unified status** > **In training** (or whichever custom status
   you’re interested in).

The list shows agents who are in the custom status you selected.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_live_agent_status_use_case_2_nov17.png)

## Use case 3: See which agents are online for any channel

As a team lead without access to omnichannel routing, you want to see how many agents
are online across any channel right now. This gives you an overall picture of your
current available staffing, allowing you to make decisions across channels about how
much work can be done based on your available agents.

**To see which agents are online for any channel**

Tip: If you already have the **Agent workload vs.
capacity** window open, skip to step 4.

1. In Explore, click the **Dashboard** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dashboard_icon.png)) in the left sidebar.
2. Click the **Live data** dashboard, or select a custom live dashboard.
3. Click any agent status metric and select **Drill in**.
4. In the **Agent workload vs. capacity** window, click **Filter** and select
   **Status by channel** > **Online**.

The list shows agents who are online for any channel.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_live_agent_status_use_case_3_nov17.png)

## Use case 4: See which agents are online for a specific channel

As a team lead, you want to see which agents are online for calls, regardless of
their status in other channels. This helps you focus your attention on agents who
are currently available to handle calls, without worrying about availability for
other channels.

**To see which agents are online for a specific channel**

Tip: If you already have the **Agent workload vs.
capacity** window open, skip to step 4. If you followed [use case 3](#topic_rsm_s44_jzb), skip to step
5.

1. In Explore, click the **Dashboard** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dashboard_icon.png)) in the left sidebar.
2. Click the **Live data** dashboard, or select a custom live dashboard.
3. Click any agent status metric and select **Drill in**.
4. In the **Agent workload vs. capacity** window, click **Filter** and select
   **Status by channel** > **Online**.
5. Click **Filter** again and select **Channel** > **Talk**.

The list shows agents who are online for the voice channel.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_live_agent_status_use_case_4_nov17.png)