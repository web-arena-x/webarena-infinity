# Setting up WFM general tasks for non-ticketing work

Source: https://support.zendesk.com/hc/en-us/articles/6443329426330-Setting-up-WFM-general-tasks-for-non-ticketing-work

---

Zendesk Workforce management (WFM) general tasks are tasks that you set up to track agent activities or tasks that take place outside of Zendesk. General tasks are also sometimes known asAUX codesorAUX statesin a call center.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Workforce Management (WFM) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Set up general tasks to track non-ticketing work like breaks and meetings. As an admin, you can create tasks, assign team permissions, and set voice statuses to optimize agent time. Customize tasks to log as paid or productive time, and connect workstreams for schedule adherence. These tasks help manage agent activities outside of ticketing, improving overall workflow management.

Note: The information in this article applies only when using general tasks to track agent
activity. If you’ve turned on unified agent status synchronization in WFM, see [Mapping unified agent statuses](https://support.zendesk.com/hc/en-us/articles/10117789027610).

Zendesk Workforce management (WFM) general tasks are tasks that you set up to track
agent activities or tasks that take place outside of Zendesk. General tasks are also sometimes
known as [AUX codes](https://cxcentral.com.au/glossary/auxiliary-codes/#:~:text=Glossary%20Auxiliary%20Codes-,Auxiliary%20Codes,employee%20isn't%20being%20productive.) or [AUX states](https://www.callcentrehelper.com/auxiliary-work-state-90793.htm) in a call center.

For example, you may want to set up general tasks to track time for necessary
activities such as lunch, breaks, meetings, training, and so on. By setting up general tasks,
you can track agents’ time spent on non-ticketing work.

This article contains the following topics:

- [Creating WFM general tasks](#topic-1)

Related articles

- [About WFM general tasks](https://support.zendesk.com/hc/en-us/articles/7069811858586)

## Creating WFM general tasks

Before creating general tasks, it’s recommended to align with other stakeholders
in your organization on what types of general tasks you’ll need.

You must be a WFM admin to create general tasks.

Admins can also define whether the general task is counted as [paid time](https://support.zendesk.com/hc/en-us/articles/6443376913818#topic_xwv_3n4_52c__paid_time) or [productive time](https://support.zendesk.com/hc/en-us/articles/6443376913818#topic_xwv_3n4_52c__productive_time).

If the general task is counted as paid or productive time, it’s included when
calculating the [occupancy rate](https://support.zendesk.com/hc/en-us/articles/6443376913818#topic_xwv_3n4_52c__occupancy_rate_ocr).

There are certain scenarios where you’ll want to define a general task as
productive time. For example, if an agent works on social media management outside of
Zendesk, you can create a task for that type of work and track it as productive time.

Note that all productive time tasks are included in paid time.

However, not all general tasks need to be defined as productive time.
Unproductive time is a standard part of customer support work. Tasks such as attending
training or meetings could be considered unproductive but still count as paid time. While
they’re necessary activities, they aren’t the core focus of an agent’s job. You may also
want to define a “lunch” task as unpaid time. To learn more, see [About paid time and productive time general
tasks](about-wfm-general-tasks.md#topic_g5y_dw1_cbc).

**To create general tasks**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_admin_icon.png)
   **Settings** in the navigation bar, then select **General tasks**.
2. Click the **Add** icon ( ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_plus_icon.png)).
3. Enter a **Name**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_generaltasks_create.png)

   Choose a descriptive name so that agents know what it
   is when they see it on their schedule, or clock into it from the WFM time tracker app in
   Zendesk Support.
4. (Optional) Enter a **Description** to describe the purpose of the task.
5. Set the **Team permissions**. By default, a new task is available to all of your
   teams, but you can restrict the task to certain teams only.
6. Select a color for the new task. The color you select will appear on the Agent activity
   page and to agents in Zendesk Support.

   A preview of the color you select appears, and you
   can adjust it as needed.
7. (Optional) Under **Occupancy settings**, click the **Log this general task as paid
   time** toggle to include the task in paid time when calculating agents’ occupancy
   rates.
8. (Optional) When logging the task as paid time, click the **Log this general task as
   productive time** toggle to include it as productive time when calculating agents’
   occupancy rates.
9. Under **Talk status settings**, set the status for the voice channel the agent will
   appear in when they clock in to this general task.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_general_task_schedule_adherence.png)

   For example, if the general task
   is for a meeting or lunch break and the agent will be away from Zendesk, select the Away
   status. Setting the voice status associated with a general task helps you optimize your
   agent's time, by reducing the number of actions they need to perform efficiently, as
   they won't need to update their voice status manually.

   Note: General tasks currently synchronize with your [agents’ voice states](https://support.zendesk.com/hc/en-us/articles/4408829114138) only when [omnichannel routing is turned off](https://support.zendesk.com/hc/en-us/articles/5095079121690). When [omnichannel routing is turned on](https://support.zendesk.com/hc/en-us/articles/5866925319962), general tasks do not
   synchronize with your [agents’ unified agent statuses](https://support.zendesk.com/hc/en-us/articles/4410545721114).

   You can select between the following options:

   - No change
   - Online
   - Away
   - Transfers only
   - Offline
10. (Optional) Under **Schedule adherence customization** select workstreams. By
    connecting workstreams to this general task you can ensure that the workstreams’
    activities are also taken into consideration when calculating the agent’s schedule [adherence](../reporting-on-workforce-performance-wfm-add-on/wfm-custom-report-metrics.md#In%20Adherence%20Time).
11. Click **Save**.