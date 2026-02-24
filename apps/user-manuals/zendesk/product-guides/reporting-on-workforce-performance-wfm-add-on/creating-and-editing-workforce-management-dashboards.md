# Creating and editing workforce management dashboards

Source: https://support.zendesk.com/hc/en-us/articles/6866245012378-Creating-and-editing-workforce-management-dashboards

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Workforce Management (WFM) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

As a WFM admin, you can create and edit up to 10 workforce management dashboards to monitor team performance. Add up to 12 widgets per dashboard to display key metrics like resolution rate, first response time, and ticket reopen rate. Customize dashboards by rearranging widgets and editing names to align with your organization's goals.

Workforce management (WFM) dashboards give you a quick visual overview of how your
team or organization is performing. You can create and edit dashboards to focus on the metrics
and performance indicators that are most relevant to your organization.

You must be a [WFM admin](https://support.zendesk.com/hc/en-us/articles/6443374440090) to access dashboards.

This article contains the following sections:

- [Creating WFM dashboards](#topic_hdw_y44_s1c)
- [Adding widgets to WFM dashboards](#topic_xjx_qp4_s1c)
- [Editing WFM dashboards](#topic_m4w_rr4_s1c)
- [WFM dashboard-specific metrics](#topic_ryz_st4_s1c)

Related articles

- [About workforce management dashboards](https://support.zendesk.com/hc/en-us/articles/6443376866074)

## Creating WFM dashboards

You can create up to 10 dashboards for your organization. When you first create your
organization’s dashboards, it’s recommended that you align with other stakeholders on the
metrics and performance indicators to include.

**To create a WFM
dashboard**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_dashboards_icon.png)
   **Dashboards** in the navigation bar.
2. Click the dashboards menu, the select **+ Create dashboard**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_dashboards_create.png)
3. Enter a **Dashboard name** and click **Create dashboard**.

   Next, [add widgets](#topic_xjx_qp4_s1c) to your new
   dashboard.

## Adding widgets to WFM dashboards

Widgets are the building blocks that make up dashboards. They display the metrics that you
choose in layouts that you select. See [dashboard widgets](https://support.zendesk.com/hc/en-us/articles/6443376866074#topic_ttv_fj4_s1c).

You can add widgets to new and existing dashboards. Each dashboard can have up to 12
widgets.

The Agents widget is being discontinued. View the [Agent status](https://support.zendesk.com/hc/en-us/articles/6443331637018) page to see what your agents are working on in real
time.

**To add a widget to a WFM
dashboard**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_dashboards_icon.png)
   **Dashboards** in the navigation bar.
2. To add a widget to a new dashboard or a dashboard without any widgets, click **Add your
   first widget**.

   To add another widget to an existing dashboard, click the
   **Customize dashboard** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_pencil.png)), then click the plus sign (**+**) icon.
3. In the Add widget dialog, select a **Metric**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_dashboard_widget.png)

   Note: Some metrics are specific to dashboards. See [WFM dashboard-specific
   metrics](#topic_ryz_st4_s1c).
4. Choose a **Workstream**.
5. Pick a **Layout** to display the data in.

   If you select one of the goal layouts,
   then enter the **Goal** values.
6. Click **Add**.
7. Continue to add additional widgets as needed.
8. To rearrange how the widgets appear on your dashboard, click a widget and drag it to the
   desired location.
9. Click **Save layout**.

## Editing WFM dashboards

You can edit or delete your existing WFM dashboards.

**To edit or delete a WFM
dashboard**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_dashboards_icon.png)
   **Dashboards** in the navigation bar.
2. Select a dashboard.
3. To change the dashboard's name, click the gear (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_admin_icon.png)) icon.

   Enter or edit the name, then click **Done**.
4. To delete a dashboard, click the gear (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_admin_icon.png)) icon.

   Click **Delete dashboard**, then confirm that you
   want to delete it.
5. To edit or rearrange your widgets, click the **Customize dashboard** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_pencil.png)) icon. See [Adding widgets to WFM dashboards](#topic_xjx_qp4_s1c).

## WFM dashboard-specific metrics

Most dashboard metrics are sourced from [Explore datasets](https://support.zendesk.com/hc/en-us/articles/4408839218842) and are not directly measured by Zendesk WFM.

The following metrics are specific to WFM dashboards:

| Metric | Definition |
| --- | --- |
| Resolution rate | This metric is commonly used to understand the ratio of tickets being assigned to an agent compared to how many tickets an agent solved. **Formula**:  *Solved Tickets / Tickets Received x 100* |
| Median first response time (FRT) | Median FRT represents the median time between when a ticket is initially created and when the first public reply is sent. **Formula**: *Time of first public reply - Time ticket is created* |
| First assigned time | The First assigned time is the time when a ticket is first assigned to an agent or a group. This metric is used to measure the efficiency of the ticket assignment process and to ensure that tickets are being assigned in a timely manner. |
| Ticket reopen rate | The reopened rate is a metric that measures the percentage of tickets that are reopened after being marked as solved. **Formula**:  *Reopened Tickets / Solved Tickets x 100* |
| Assigned points | Assigned points refers to the number of tickets assigned to an agent. An agent receives an Assigned point when a ticket is assigned to them in any of the following ways: the agent assigns the ticket to themselves, another person assigns the ticket to the agent, or an automation or routing rule assigns the ticket to the agent. Note that each agent can receive only one Assigned point per ticket regardless of how many times the ticket is assigned to them. |