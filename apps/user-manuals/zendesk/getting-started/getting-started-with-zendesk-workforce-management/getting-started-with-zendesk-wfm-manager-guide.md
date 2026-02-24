# Getting started with Zendesk WFM: Manager guide

Source: https://support.zendesk.com/hc/en-us/articles/6514633060634-Getting-started-with-Zendesk-WFM-Manager-guide

---

This guide is recommended for anyone who is responsible for workforce management (WFM) planning and scheduling, managing agent time and activity, and day-to-day monitoring. Common roles include manager, scheduler, analyst, and team lead.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Workforce Management (WFM) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

This guide helps you manage workforce planning and scheduling, handle short-term schedule changes, and monitor daily team performance. Use forecasting tools for long-term planning and adjust schedules as needed. Monitor agent attendance and activity in real time, and access historical reports to identify trends and improve staffing decisions. Customize dashboards to track key metrics like handle time and adherence rate.

This guide is recommended for anyone who is responsible for workforce management (WFM)
planning and scheduling, managing agent time and activity, and day-to-day monitoring. Common roles include manager, scheduler, analyst, and team lead.

Managers work with data in Zendesk WFM to plan, schedule, and monitor agent work. Zendesk WFM's capabilities support a range of planning and management needs, such as long-term planning, forecasting, and scheduling, short-term schedule management, day-to-day monitoring, and historical reporting.

This article contains the following sections:

- [Planning, forecasting, and scheduling](#topic_jwm_qkf_d1c)
- [Managing short-term schedule changes](#topic_xjl_drf_d1c)
- [Monitoring daily team performance](#topic_mnh_4yk_d1c)
- [Accessing historical trends with reports](#topic_ohq_33l_d1c)
- [More resources and next steps](#topic_vdb_fnl_d1c)

## Planning, forecasting, and scheduling

Zendesk WFM’s tools are built for long-term forecasting and scheduling that assist you with the WFM planning you perform as a manager. You can plan your resourcing needs based on different scenarios and data sets. Additionally, you can revisit your staffing throughout your fiscal cycle and adjust plans based on the trends you observe.

You must have admin permission in Zendesk WFM to access the features described in this article.

### Forecast

Zendesk WFM's forecast takes your historical ticket data and your workstreams to create inbound volume estimates for up to a year in the future.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_forecast_historical_volume.png.png)

At installation, the past six months of your Zendesk ticket data is brought over to build an initial forecast.

Note: When capturing ticket volume, Zendesk WFM also includes spam tickets, which may be different from how you capture ticket volume in Zendesk Explore. See [Understanding and managing suspended tickets and spam](https://support.zendesk.com/hc/en-us/articles/4408889141146).

When a ticket is created, it's automatically assigned to a workstream to create a forecast. Your forecast includes a full-time equivalent (FTE) calculation, which shows how many staff members are required to handle the estimated workload.

If you're responsible for long-term forecasts, your planning will likely begin several months out. Otherwise, it's recommended that you review the Forecast page regularly to help plan your schedule. See [Viewing your active forecasts](https://support.zendesk.com/hc/en-us/articles/9940054229402).

### Schedules

Your forecast serves as the basis for your schedule. When you generate a schedule in Zendesk WFM, select the time frame the schedule should cover.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_schedule_date_view.png)

You have two options for creating your team’s schedule:

- Generate a schedule for your team’s workstreams. Zendesk WFM builds a schedule based on the hours and shift parameters established by an admin in your organization structure.
- Import your own schedule. You may need to change shifts to reconcile differences between forecasted staffing needs and available staffing.

After you have a schedule, you‘ll see a heat map that shows whether you’re adequately staffed to support the volume of inbound work forecasted, including general tasks (non-ticket work) and approved time-off.

Regularly review your forecast and schedule to see how many agents are scheduled compared to those forecasted. This will help ensure that you have an appropriate amount of agents to handle the workload.

WFM schedules aren't automatically synced with Zendesk schedules or business hours. You should work with your admin to plan for and correct any scheduling conflicts that may arise.

For more information about scheduling, see [Generating and publishing your workforce management schedule](https://support.zendesk.com/hc/en-us/articles/6443348279194) and [Importing schedules](https://support.zendesk.com/hc/en-us/articles/6443377641754).

## Managing short-term schedule changes

Zendesk WFM provides a number of features that assist you in managing your short-term schedule changes. You can make adjustments to your team's schedule as needed, allow your agents to trade shifts with each other, and manage their time off requests.

### Schedules

Schedules serve as a helpful starting point for assessing short-term staffing needs or making weekly or daily adjustments. This is known as intraday management. From the Schedule page, click an agent's name to view their shifts.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_gs_edit_agent_schedule_daily.png)

You can then edit an agent's schedule or edit schedules in bulk by shortening, lengthening, or splitting shifts.

For more information about managing schedule changes, see [Editing your schedule](https://support.zendesk.com/hc/en-us/articles/6443365957274).

### Shift trade management

Shift trades allow agents to request to trade shifts with each other. An admin must turn on shift trades and can make a manager's approval required or not. Agents can request shift trades from their [Agent Schedule](https://support.zendesk.com/hc/en-us/articles/6443374353434) in Zendesk Support. If a manager's approval is required, you’ll want to view and act on these requests quickly as they may impact your overall staffing.

For more information, see [Activating shift trades for agents](https://support.zendesk.com/hc/en-us/articles/6443354721178).

### Time off management

Agents can request time off from their [Agent Schedule](https://support.zendesk.com/hc/en-us/articles/6443374353434) in Zendesk Support. You'll receive an email notification for each request and can view the request details from the Time off management page. The page displays a summary of all your agents’ requests, including the date, time, and reason. It’s up to you to approve, deny, or comment on the request.

Tip: You may want to view the Schedule page and your heat map as you assess your agents’ time off requests to ensure that you have adequate coverage.

For more information about managing time off requests, see [About the Time off management page](https://support.zendesk.com/hc/en-us/articles/6443393050394).

## Monitoring daily team performance

While Zendesk WFM’s scheduling tools help you manage your staffing, its agent-centered tools give you real time insight into agents’ work and allow your involvement when necessary.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_agent_status_access.png)

Additionally, you can customize dashboards for a quick visual overview of performance in real time.

### Agent attendance

The Agent attendance page gives you a quick view of your team's daily attendance. Details include who's scheduled for the day, how long they are scheduled for, how much time they have logged, if they were late, planned and unplanned time off, and their [occupancy rate](https://support.zendesk.com/hc/en-us/articles/6443331680538#Occupancy%20Rate).

For more information about how to filter and drill down on this data, see [About the Agent attendance page](https://support.zendesk.com/hc/en-us/articles/6443347522074).

### Agent status

After you've checked agent attendance, use the Agent status page to view what each agent is working on in real time and their adherence to what's scheduled. Prior inputs, such as workstreams and agents’ time entries, inform these views.

Adherence is important for long-term planning, but focusing on it too much can suggest to agents that WFM tools are mainly for monitoring their time. Instead, emphasize that Zendesk WFM helps build a predictable and accurate staffing model. Coordinate with other stakeholders on how to talk to your agents about this. It'll help ensure successful change management and product adoption.

For more information, see [About the Agent status page](https://support.zendesk.com/hc/en-us/articles/6443331637018).

### Agent activity

If you need a more detailed view of agents' activity, schedule adherence, and productivity, use the Agent activity page. This page gives you a real time view of each agent’s activity compared to their planned schedule.

For example, if you see that an agent is stuck on a ticket, you can access the ticket they’re working on and offer help, assess its complexity, and so on.

For more information, see [About the Agent activity page](https://support.zendesk.com/hc/en-us/articles/6443347506970).

### Dashboards

Dashboards provide a quick visual overview of how your team is performing in real time.
In contrast to Zendesk Explore dashboards, which show real-time ticket and channel-specific data, Zendesk WFM’s dashboards show you how your team is handling their workload at the moment.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_gs_dashboards_overview.png)

Customize dashboards by selecting metrics to measure your team's performance against.
Common metrics managers seek out include:

- Average handle time
- Adherence rate
- Occupancy rate

Your dashboards update throughout the day, with Zendesk data refreshing every 30 seconds.

Your organization can create up to three dashboards. It's recommended that you align with other stakeholders on the metrics and performance indicators that should be included on your dashboards. You may want to consider that a number of different users will be using dashboards for views that are relevant to their roles.

For more information, see [About dashboards](https://support.zendesk.com/hc/en-us/articles/6443376866074).

## Accessing historical trends with reports

WFM reports gives managers insight into historical staffing trends and agent activity.

With WFM reports, you can monitor agent performance, attendance, and time-off requests with pre-defined system report templates. These reports help you identify patterns and gain insight into agent activity and attendance.

The system report templates include:

- **Agent activity**: Displays agents' adherence rate and a breakdown of the points that make up their productivity.
- **Agent attendance**: Shows categories such as attendance and attendance rate, occupancy rate, and so on.
- **Time-off**: Provides a historical view of agents’ approved time-off requests.

System report templates can't be edited. However, you can copy the system templates and use them to create custom reports. Custom reports can be modified to suit your needs. You can select productivity metrics and general tasks, such as paid, unpaid, productive, unproductive, and more.

For example, create or customize a report to view how many tickets one agent worked, solved, or re-opened.

As a manager, you can export reports as well as schedule and send recurring reports.

For more information, see [About system report templates](https://support.zendesk.com/hc/en-us/articles/6443363334810) and [About custom report templates](https://support.zendesk.com/hc/en-us/articles/6443331692698).

Tip: Reviewing reports and noting patterns can help you recommend automations for your admin to set up. For more information, see [About Zendesk WFM automations](https://support.zendesk.com/hc/en-us/articles/6443314435610).

See our [Getting started with Zendesk WFM: Agent guide](https://support.zendesk.com/hc/en-us/articles/6514645504282) to learn about the agent experience in Zendesk WFM and understand how your agents interact with it.