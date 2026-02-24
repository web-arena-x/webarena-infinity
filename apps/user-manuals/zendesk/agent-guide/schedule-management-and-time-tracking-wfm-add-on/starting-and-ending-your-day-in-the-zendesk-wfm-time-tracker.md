# Starting and ending your day in the Zendesk WFM time tracker

Source: https://support.zendesk.com/hc/en-us/articles/6443354661402-Starting-and-ending-your-day-in-the-Zendesk-WFM-time-tracker

---

Depending on your account settings, your day may start automatically when you begin working, or you may need to start it manually.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Workforce Management (WFM) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Start and end your workday using the WFM time tracker. If auto-tracking is off, manually track your activities to ensure accurate time management. Begin your day by clocking into tasks, track activities like tickets or breaks, and end your day to avoid untracked time. Use the time tracker to manage your work efficiently and provide valuable data for reporting.

Note: If [unified agent status synchronization](https://support.zendesk.com/hc/en-us/articles/10114746509978) is turned on for WFM, you should [set your unified agent statuses](https://support.zendesk.com/hc/en-us/articles/4410545721114#topic_xvw_ytp_m5b) in the Agent Workspace. When you start working on a ticket, Zendesk WFM automatically tracks your time and attendance. However, if your day starts with a status that doesn’t include working on tickets, you must still manually start your day by clicking **Start day** using the WFM time tracker.

Depending on your account settings, your day may start automatically when you begin working, or you may need to start it manually.

If [auto-tracking](https://support.zendesk.com/hc/en-us/articles/7446325512730) is activated for you, then Zendesk WFM takes care of time and attendance management for most of your workflows. When you begin working on a ticket, chat, or call, your day automatically starts and you're clocked in.
However, if your day starts with a [general task](https://support.zendesk.com/hc/en-us/articles/7069811858586), for example a meeting, then you must [manually start your day in the Zendesk WFM time tracker](#starting_your_day) by clocking into the task.

If auto-tracking has been deactivated for you then, you must manually start and end your day and track your activities in the Zendesk WFM time tracker. In this case, moving between tabs and views in Zendesk Support will not automatically trigger a new [activity event](https://support.zendesk.com/hc/en-us/articles/6443347506970#topic_evy_c2d_tzb).

This article contains the following topics:

- [Starting your day](#starting_your_day)
- [Tracking your activity](#topic_sph_j1l_pdc)
- [Ending your day](#ending_your_day)

Related articles

- [Accessing agent schedule](https://support.zendesk.com/hc/en-us/articles/6443374353434)

## Starting your day

Manually start your day if your schedule begins with non-ticketing work, such as a meeting, or if [auto-tracking](https://support.zendesk.com/hc/en-us/articles/7446325512730) has been deactivated for you. If your day begins with ticketing work and auto-tracking is activated, you do not need to clock in.
Zendesk WFM automatically starts tracking your time as soon as you begin working on a ticket.

When transitioning from ticketing to a general task, such as a break or a team meeting, clock into the general task or status from the time tracker. Your input helps inform your managers’ data and reporting, ensuring they have a complete view of how your time is spent.

**To manually start your day**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **Zendesk Workforce Management** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_logo_icon.png)) in the top right to access the time tracker.
2. Select a general task from the menu, or click **Start day** if your task is not listed.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_agent_app_clock_in.png)

## Tracking your activity

Zendesk WFM uses three main activity types to [record and track activities in a timeline](https://support.zendesk.com/hc/en-us/articles/6443347506970):

- [Ticket activity](https://support.zendesk.com/hc/en-us/articles/6443347506970): Time spent on a ticket page.
- [Untracked](https://support.zendesk.com/hc/en-us/articles/6443376913818#topic_xwv_3n4_52c__untracked_time): Time spent on any non-ticket page.
- [General tasks](https://support.zendesk.com/hc/en-us/articles/7069811858586): Time spent on general tasks. These are the custom WFM activities that you can create and that can be used manually by your agents or by [WFM automations](https://support.zendesk.com/hc/en-us/articles/6443374423066). Examples include breaks, lunch times, meetings, or any other tasks you create for your teams.

When [auto-tracking](https://support.zendesk.com/hc/en-us/articles/7446325512730) is activated, moving between tabs and views in Zendesk Support automatically triggers a new activity event and you don’t need to manually track your activity.

For example, if you open ticket #3 in tab 1, ticket #4 in tab 2, and an untracked page such as a [customer's page](https://support.zendesk.com/hc/en-us/articles/4408828129946) in tab 3, the system tracks you as working on those tickets whenever you open tab 1 or tab 2, or as untracked when you access tab 3. It depends on which tab you have in focus at any given time.

I you're viewing a customer's page on your tab 3 and select a general task such as “Break” using the WFM time tracker, your activity is now tracked as "Break".

If [task lock](https://support.zendesk.com/hc/en-us/articles/6443329257114) is also activated, you can remain clocked into a single ticket or task while opening other tickets.

Using task lock also prevents new activities from starting automatically. This means that if you select the task "Break" to start counting time on the break activity and then open ticket #4, your activity does not change and remains locked in "Break".

If an admin has deactivated auto-tracking, you must track your activities manually using the WFM time tracker.

**To manually track your activity**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **Zendesk Workforce Management** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_logo_icon.png)) in the top right to access the time tracker.
2. Select a general task from the menu, or click **Start day** if your task is not listed.
3. When moving between tickets, you can manually select to start tracking a specific ticket by using the **Track this ticket** button.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_agent_app_manual_tracking.png)

When your activity is either a general task or a ticket, you will see the option to stop tracking right below the activity name. Clicking this will change your activity status to [Untracked](https://support.zendesk.com/hc/en-us/articles/6443345024538#Untracked%20Time).

## Ending your day

It's important to end your day to prevent untracked time from being recorded at the end of your shift. Closing or logging out of Zendesk doesn't clock you out or end your day.

**To end your day**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **Zendesk Workforce Management** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_logo_icon.png)) in the top right to access the time tracker.
2. Click **End day**.

Admins can also end your day by [using automations](https://support.zendesk.com/hc/en-us/articles/6443314435610).