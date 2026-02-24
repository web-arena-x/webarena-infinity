# Analyzing call activity with the Talk dashboard 

Source: https://support.zendesk.com/hc/en-us/articles/4408831823514-Analyzing-call-activity-with-the-Talk-dashboard

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Talk Professional or Enterprise |

With the Zendesk Talk dashboard, you can view details about current queue activity,
account-wide activity for the current day, and individual agent activity. Filter by numbers
and agent groups or compare graphs of two metrics to get further insight.

This article covers the dashboard for Professional plan and above. If you're on the Team
plan, see [Analyzing call activity with the Talk Team
dashboard](https://support.zendesk.com/hc/en-us/articles/4408821396762).

This article contains the following sections:

- [Accessing and viewing the Talk dashboard](#topic_xmn_wxx_fv)
- [Viewing current queue activity](#topic_bys_vxw_fv)
- [Viewing an overview of account call data](#topic_pys_jyw_fv)
- [Viewing agent activity](#topic_vqs_vgx_fv)

Related article:

- [Analyzing your Talk activity](https://support.zendesk.com/hc/en-us/articles/4408836253338)

## Accessing and viewing the Talk dashboard

Admins and agents with permission can view the Talk dashboard.

Any user with a Talk admin or team lead role can view the dashboard and edit the state of
other agents. A Talk agent can view it, but can't change agent status. However, if the Talk
agent is also a Support admin, they can view the dashboard and edit the state of other
agents. See [Giving agents access to Talk](https://support.zendesk.com/hc/en-us/articles/4408882966170).

Enterprise agents can access the dashboard if they are in a [custom role](https://support.zendesk.com/hc/en-us/articles/4408882153882) with the View Talk dashboard permission. To interact
with the dashboard, they'll also need the permission to Manage channels and extensions.

**To view the Talk dashboard**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Talk**.
2. Click the **Dashboard** tab.
3. Select the number or numbers you want to view data for.

   ![](http://zen-marketing-documentation.s3.amazonaws.com/docs/en/voice_selectnumbers.png)

## Viewing current queue activity

In the **Current queue activity** section, you can see real-time details about your call
queue. For details on each metric, see [Zendesk Talk dashboard metrics reference](https://support.zendesk.com/hc/en-us/articles/4408883025690).

![](http://zen-marketing-documentation.s3.amazonaws.com/docs/en/current_queue.png)

## Viewing an overview of account call data

The **Overview** section displays additional metrics on your account's call activity
from midnight to midnight for the current day. The time zone is based on your Zendesk
Support account settings. For details on each metric, see [Zendesk Talk dashboard metrics reference](https://support.zendesk.com/hc/en-us/articles/4408883025690).

![](http://zen-marketing-documentation.s3.amazonaws.com/docs/en/Zendesk_Support_-_Agent.png)

- Select two metrics to compare from the drop-down menus above the graph.

  ![](http://zen-marketing-documentation.s3.amazonaws.com/docs/en/voice_adv_dashboard_compare.png)
- Click the **-** symbol to remove the second metric.

  ![](http://zen-marketing-documentation.s3.amazonaws.com/docs/en/voice_adv_dashboard_remove.png)
- Hover over part of the graph to see details for a specific time increment.

  ![](http://zen-marketing-documentation.s3.amazonaws.com/docs/en/voice_adv_dashboard_hover.png)

## Viewing agent activity

The **Agent Activity** section shows a summary of call activity and current availability
status for each agent. If you have selected a number, the section will list all agents in
every group the number is routed to. For details on the metrics in this section, see [Zendesk Talk dashboard metrics reference](https://support.zendesk.com/hc/en-us/articles/4408883025690).

![](http://zen-marketing-documentation.s3.amazonaws.com/docs/en/voice_agentactivity.png)

You can perform any of the following tasks in this section:

- **Change an agent's availability status** by selecting a status next to their name.

  If you've [turned on omnichannel routing](https://support.zendesk.com/hc/en-us/articles/5866925319962), this option is
  not available.

  ![](http://zen-marketing-documentation.s3.amazonaws.com/docs/en/voice_dashboard_agentactivity_changestatus.png)

  When [IVR is configured](https://support.zendesk.com/hc/en-us/articles/4408885628698) for a line, it indicates that the line is
  not assigned to any group. As a result, agents will not be displayed as online for
  this line. However, they can still make outbound calls and receive inbound
  calls.
- **Filter groups** using the drop-down menu.

  ![](http://zen-marketing-documentation.s3.amazonaws.com/docs/en/voice_dashboard_agentactivity_filtergroups.png)
- **See additional agent details** by clicking more.

  ![](http://zen-marketing-documentation.s3.amazonaws.com/docs/en/voice_dashboard_agentactivity_more.png)