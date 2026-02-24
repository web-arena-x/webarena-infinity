# Accessing and understanding your WFM schedule page

Source: https://support.zendesk.com/hc/en-us/articles/6443348256794-Accessing-and-understanding-your-WFM-schedule-page

---

From the Zendesk Workforce management (WFM) Schedule page, admins can generate, edit, and publish agent schedules.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Workforce Management (WFM) or Workforce Engagement Management (WEM) |

Location: Zendesk WFM > Schedule

From the Zendesk Workforce management (WFM) Schedule page, admins can generate, edit, and publish agent schedules.

This page lists the schedules for all agents, but you can filter the list or search for agents by name. From this page, you can also view past and future schedules by day, week, and month and use the staffing panels to identify gaps in your staffing and scheduling.

This article contains the following topics:

- [Accessing the Schedule page](#topic_azy_b5l_y1c)
- [Understanding the schedule](#topic_p5v_n5l_y1c)
- [Navigating the schedule](#topic_qnd_2sl_k2c)
- [Identifying unpublished shifts](#topic_qym_fsl_k2c)
- [Accessing staffing panels, menus, and charts](#topic_i1n_gsl_k2c)

Related articles

- [Generating and publishing your WFM schedule](https://support.zendesk.com/hc/en-us/articles/6443348279194)
- [Editing your WFM schedule](https://support.zendesk.com/hc/en-us/articles/6443365957274)
- [Zendesk Workforce management (WFM) resources](https://support.zendesk.com/hc/en-us/articles/6457209788442)

## Accessing the schedule page

You must be an admin to access the Schedule page.

**To access the Schedule page**

- In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_calendar.png)
 **Schedule** in the navigation bar, then select **Schedule**.

## Understanding the schedule

The Schedule page lists all agents sorted by their default Zendesk groups. You can quickly change agents’ schedules from this page without having to edit the structure of your [shifts](https://support.zendesk.com/hc/en-us/articles/6443345205402). When you change agents’ shifts, the page provides an overview of which shifts are published and which aren’t.

Additionally, the Schedule page displays various staffing panels, menus, and charts that help you highlight gaps in your staffing.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_schedule_overview.png)

## Navigating the schedule

There are numerous ways you can interact with the Schedule page to find information about past, present, and future schedules. Specifically, you can sort, filter, and search the schedule in the following ways:

- Use the search box above the agents list to search for a specific agent by name or email address.
- Use the date picker to view the schedule for a specific date.
- Use the view menu, next to the date picker, to switch between viewing schedules for a specific day (default), week, or month.
- Use the filter menu above the agent list to filter agents by group (default), [team](https://support.zendesk.com/hc/en-us/articles/6443329411994), [location](https://support.zendesk.com/hc/en-us/articles/6443329411994), or to list all agents. When filtering by group, agents are organized by their default Zendesk groups.
- Use the Sort Agents button to list agents by name or shift start time.

 The *Sort by shift start time* option applies only to the Day view of the schedule, as shifts can start at different times each day.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_schedule_sort.png)

 This selection is saved and applies to all folders. When you leave and return to the Schedule page, your last saved sorting selection is applied.

## Identifying unpublished shifts

When you edit shifts in your schedule, the updates are saved, but you must [publish them](https://support.zendesk.com/hc/en-us/articles/6443348279194#topic_jtc_ds5_zzb) for agents to be able to see the changes.

Unpublished shifts are highlighted and a yellow dot appears next to the agent's name to indicate they have unpublished shift updates.

- **Day** view:

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_schedule_unpublished_day.png)
- **Week** view:

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_schedule_unpublished_week.png)
- **Month** view:

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_schedule_unpublished_month.png)

## Accessing staffing panels, menus, and charts

The staffing panel week and month views are currently in an early access program (EAP). You can [sign up for the EAP here](https://docs.google.com/forms/d/e/1FAIpQLScyeTnJSIhVLA2EPAZRCabS8TQAKrAJ3aHONps_1BA0CnQx_w/viewform).

The Schedule page provides a comprehensive overview of daily staffing needs through various panels, menus, and charts. This makes it easier for admins to identify gaps in staffing for specific days and enhances their ability to manage staffing efficiently, with balanced workloads and resources allocation.

In the schedule day view, the staffing panel displays the Full-Time Equivalent (FTE)
prediction as the number of staff members required to handle the estimated workload. This allows for a clear understanding of the expected daily staffing requirements based on historic ticket volume.

(EAP only) The staffing panels for the week and month views display staffing needs in hours, which provides a broader perspective on resource allocation over time. The Agents column shows how many people are scheduled for the workstream at least once in the corresponding period. For example, if an agent has a task scheduled that takes 5 minutes, they are counted as +1 in the Agents column for that period. Regardless of an agent’s tasks within the schedule, agents are only counted once per period in the staffing panel.

**To access staffing panels, menus, and charts**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_calendar.png)
   **Schedule** in the navigation bar, then select **Schedule**.
2. Use the date picker to view schedules for a specific **Day**.

   If you're participating in the [staffing panel week and month view EAP](https://support.zendesk.com/hc/en-us/community/topics/9015877275930), use the date picker to switch to a week or month view.
3. Click the **General tasks panel** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_general_tasks_icon.png)) icon in the upper left corner of the page.

   The panel opens at the bottom of the page, where you can view detailed information about scheduled general tasks and time off reasons.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/wfm_staffingpanel_general_tasks_1.png)
4. Click the **Workstreams staffing panel** ( ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_trend_chart_icon.png)) icon in the upper left corner of the page.

   The panel opens at the bottom of the page, where you can view a detailed list of your [workstreams](https://support.tymeshift.com/hc/en-us/articles/10679984897043).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_staffingpanels_workstreams1.png)
5. From the Workstreams staffing panel, click the **Scheduled staffing** menu located in the bottom right corner.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_schedule_staffing_menu.png)

   From this menu, you can view your schedule with the following options:
   - **Scheduled staffing**: Displays the number of agents scheduled for each workstream and general task per day.

     If you're participating in the [staffing panel week and month view EAP](https://support.zendesk.com/hc/en-us/community/topics/9015877275930), this option also displays the total hours per week and month depending on which date view you've selected.
   - **Required staffing**: Displays the number of agents [forecasted](https://support.zendesk.com/hc/en-us/articles/9858048119194) for each workstream.
   - **Net staffing**: Displays the difference between the number of agents forecasted compared to the number of agents scheduled. A positive (+) value indicates overstaffing of scheduled agents, while a negative (-) value indicates understaffing compared to the forecasted FTE.
   - **Charts**: Provides a more comprehensive chart view of how many agents are scheduled, how many agents are forecasted to work, and your shrinkage per day.
   - **Smart highlighting**: Highlights cells where there are fewer agents scheduled than needed or where there are too many scheduled.