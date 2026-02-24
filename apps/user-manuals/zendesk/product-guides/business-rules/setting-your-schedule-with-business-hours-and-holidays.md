# Setting your schedule with business hours and holidays

Source: https://support.zendesk.com/hc/en-us/articles/4408842938522-Setting-your-schedule-with-business-hours-and-holidays

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Professional or Enterprise |

Location:  Admin Center > Objects and rules > Business rules >
Schedules

Account admins and owners can set a schedule for your Zendesk Support instance by selecting a
time zone, defining business hours, and setting up holidays.

If you don't provide 24/7 support to your customers, you can acknowledge your availability and give customers a better sense of when they can expect a personal response to their support requests. Even if you do provide 24/7 support, you can enhance your workflow by setting up views, triggers, automations, and reports based on your business hours set in your schedule.

Zendesk Support schedules do not apply to Chat operating hours. See [Creating a schedule with operating
hours](https://support.zendesk.com/hc/en-us/articles/4408822398106-Creating-a-schedule-with-operating-hours-Professional-and-Enterprise-).

Watch the video below to learn how schedules can impact customer experience and
team reporting.

This article covers the following topics:

- [Setting a schedule
  for your Zendesk](#topic_5tx_m3d_np)
- [Deleting a
  schedule](#topic_hnx_fpz_ls)
- [Managing your
  holidays](#topic_m5t_mt2_jq)
- [Applying your
  schedules to tickets](#topic_1ly_q4h_ms)
- [Creating business
  rules based on business hours](#topic_hnx_43d_np)
- [Creating triggers
  based on multiple schedules](#topic_vbx_jky_dt)
- [Reporting based on
  business hours](#topic_rzp_p3d_np)

## Setting a schedule for Zendesk Support

Note: On Suite Growth and Professional or Support Professional, you can set
only one schedule. On Enterprise plans you can set multiple
schedules.

Your schedule includes a time zone and specific business hours each day
in a weekly schedule for Zendesk Support.

You can also set up holidays as exceptions to the business hours set in
your schedule. You can add as many holidays as you like up to two
years in advance. They will be treated as outside of business hours
and not count toward any metrics you measure in business hours.

After you set a schedule, you can create business rules based on the
business hours in your schedule. You can also use business hours in
reporting.

Note: When you set a schedule, the schedule is used for all tickets in your
account. All business hour metrics and rules will use your default
schedule after it's set.

**To set your schedule**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Schedules**.
2. Click **Add schedule** to create a new schedule. Or,
   click an existing schedule to modify it.
3. On the schedules page, enter a **Schedule name** and
   choose a **Time zone**.

   ![Enterprise schedules](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/schedules_1.png)
4. In the **Weekly schedule** section, keep the preset
   business hours or modify them.
   - Each business interval must be at least 1 hour
     long. You can extend your business hours in 15
     minute increments.
   - You can adjust the interval start time in 15
     minute increments.
   - A schedule interval can't overlap a date
     boundary. If your business hours span midnight,
     you must define this as two separate intervals,
     divided by calendar day.
   - To move a block of time, drag the time block
     up or down on that day.
   - To change the start or end time, drag the top
     or bottom of the time block.
   - To remove hours from a day, click the X in the
     upper-right corner of the time block. The day
     displays **Closed**.
   - To add hours to a closed day, click anywhere
     on the closed day. A time block appears where you
     clicked.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/schedules_to_nearest_15_min.png)

   The hours you set are relative
   to the time zone set for your Zendesk account
   (unless you are on an Enterprise plan, and you
   selected another time zone for your schedule). See
   [Setting the
   time zone and format for Zendesk
   Support](https://support.zendesk.com/hc/en-us/articles/4408887059866#topic_dil_hnc_xe).

   Note: If you need to
   define shorter business hour intervals or more
   flexible start times, you can use the [Schedules
   API](https://developer.zendesk.com/api-reference/ticketing/ticket-management/schedules/).
5. When you are finished, click **Save**.
6. If you want to set any holidays as exceptions to your
   scheduled business hours, select **Holidays**
   and then click **Add holiday**.

   You can schedule holidays up to two years in
   advance.
7. Enter a **Name** for the holiday, then click in the
   first date field to pick a start date and click in
   the second date field to pick an end date.

   You can
   choose a single day (by picking the same start and
   end date) or a date range (by picking different
   start and end dates). You cannot set a partial day
   holiday.

   ![Support holiday scheduling](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/schedules_2.png)
8. Click **Confirm**. You can add multiple holidays by
   clicking **Add holiday** again.

   The holidays
   you add appear in your list of holidays in
   chronological order.
9. Click **Save**.
10. (Enterprise plans only) Click the back arrow to return
    to the **Schedules** admin page, then click
    **Add schedule** if you want to set multiple
    schedules.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/business_hours_back_arrow.png)

    Note: If you set up multiple schedules, the first
    schedule in the list is your default schedule and
    applies to all tickets. You can create triggers to
    apply different schedules to tickets (see [Applying your schedules to
    tickets](#topic_1ly_q4h_ms)).

    Now you can use business hours in business
    rules, reports, Talk, and Liquid markup:
    - For more information about business rules and
      reporting based on business hours, see [Creating business rules based
      on business hours](#topic_hnx_43d_np) and [Reporting based on business hours](#topic_rzp_p3d_np).
    - For information on assigning Zendesk Support
      schedules to individual Talk numbers, see [Using multiple schedules for
      Talk](https://support.zendesk.com/hc/en-us/articles/4408845919002). Talk numbers with a Zendesk Support
      schedule will only route calls during Zendesk
      Support scheduled business hours.

    Tip: If you added holidays, be sure
    to check out Liz Rosen's community tip, [Holiday auto-responses made
    easy](https://support.zendesk.com/hc/en-us/community/posts/115000420128).

## Deleting a schedule

You can delete your schedule if needed. When you do so, it's immediately
removed and your account uses calendar hours instead. This applies
to all of your tickets.

For customers on Enterprise plans with multiple schedules, your account
uses the next schedule in the list when you delete the default
schedule. That schedule becomes your new default schedule. Delete
all schedules if you want to stop using business hours in your
account and use calendar hours instead.

Note: (Enterprise only) If
you applied a schedule to tickets with a trigger, the
tickets will continue to use the schedule even after it's
deleted. Make sure to check your triggers before deleting a
schedule.

**To delete a schedule**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Schedules**.
2. Hover over the schedule you want to delete.
3. From the schedule options menu, click **Delete**.

   ![Schedules option menu](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/schedules_3.png)

## Managing your holidays

Your scheduled holidays appear in chronological order in your holidays list. You can click
any holiday to expand it and show details or to collapse it and hide details.

Your upcoming holidays are shown by default, but you can filter by past holidays. You can edit or
delete, any upcoming holidays.

**To edit a holiday**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Schedules**.
2. (Enterprise plans only) Click the name of a schedule on the **Schedules** admin page.
3. Click the **Holidays** tab.
4. From the list of schedules, hover over the schedule you want to edit.
5. From the holiday options menu, click **Edit**.

   ![Editing a holiday schedule](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/schedules_4.png)
6. Make any changes you need.
7. When you are finished, click **Confirm**.

**To delete a holiday**

1. In the **Holidays** tab of your schedule, click the options menu beside the holiday you want
   to delete, then select **Delete**.
2. Click **Delete holiday** to confirm the deletion.

   The holiday is removed from
   your list of holidays.

## Applying your schedules to tickets (Enterprise plans only)

If you're on an Enterprise plan and create multiple schedules, the first schedule in the list is
your default schedule and is used for all tickets. You can create
triggers to apply different schedules to tickets.

You need to create a trigger for each schedule you want to use for your tickets.

**To set a schedule for tickets**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. Click **Add trigger**.
3. On the Add new trigger page, enter a name and optional
   description for your trigger.
4. Add conditions for your trigger.

   The conditions will determine *which* tickets
   get the schedule you set in the next step. For example, you might chose the condition
   **ticket group is** to set a schedule for a specific group. Or you might decide
   to set the schedule based on the ticket's brand or status. It's up to you.
5. Add the action **Ticket: Set schedule**, then select one of your schedules from the dropdown
   list.

   ![Ticket schedule trigger](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/schedules_5.png)
6. Click **Create**.

If you need to find out which schedule is applied to a ticket, you can view that ticket's
events (see [Viewing a ticket's audit trail](https://support.zendesk.com/hc/en-us/articles/4408829602970-Viewing-a-ticket-s-audit-trail)).

## Creating business rules based on business hours and holidays

You can create views, SLA policies, triggers, and automations based on
your business hours. You can create triggers based on holidays.

Any views, triggers, or automations based on business hours also take
scheduled holidays into account, and consider them as outside of
your business hours, unless you have set up a holidays trigger.

Note: If you are on an Enterprise plan and have multiple schedules,
triggers, SLA policies, views, and automations based on
business hours will use the schedule applied to the ticket.

You can also use the Liquid placeholder for business hours in macros,
triggers, and automations.

```
ticket.in_business_hours
```

For information see [Using Liquid markup](https://support.zendesk.com/hc/en-us/articles/4408883291290).

This section covers the following topics:

- [Views based
  on business hours](#topic_v51_lz2_4p)
- [Triggers
  based on business hours](#topic_bh1_mz2_4p)
- [Automations
  based on business hours](#topic_knv_31f_4p)
- [Triggers
  based on holidays](#topic_rv2_5hy_dt)

### Views based on business hours

You can create views based on business hours by using any of the
"Hours since" conditions:

- Hours since created
- Hours since open
- Hours since pending
- Hours since on-hold
- Hours since solved
- Hours since closed
- Hours since assigned
- Hours since update
- Hours since requester update
- Hours since assignee update
- Hours since due date (for tickets with the type
  set to Task)
- Hours until due date (for tickets with the type
  set to Task)
- Hours since last SLA breach
- Hours until next SLA breach

Then, select one of the "(business)" options to calculate time
based on your business hours.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/business_hours_views.png)

If you are on an Enterprise plan and have multiple schedules,
views based on business hours will use the schedule applied
to the ticket.

For information about creating views, see [Using views to
manage ticket workflow](https://support.zendesk.com/hc/en-us/articles/4408888828570).

### Triggers based on business hours

You can create triggers based on business hours using the
"Ticket: Within business hours" condition.

This enables you to build triggers that fire based on whether an
event occurs during business hours or outside of business
hours. For example, you might create a trigger to escalate a
ticket filed by a VIP customer outside of business
hours.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/business_hours_triggers.png)

If you are on an Enterprise plan and have multiple schedules,
triggers based on business hours will use the schedule
applied to the ticket.

For information about creating triggers, see [Creating
triggers for automatic ticket updates and
notifications](https://support.zendesk.com/hc/en-us/articles/4408886797466).

### Automations based on business hours

You can create automations based on business hours by using any
of the "Hours since" conditions:

- Hours since created
- Hours since open
- Hours since pending
- Hours since on-hold
- Hours since solved
- Hours since closed
- Hours since assigned
- Hours since update
- Hours since requester update
- Hours since assignee update
- Hours since due date (for tickets with the type
  set to Task)
- Hours until due date (for tickets with the type
  set to Task)
- Hours since last SLA breach
- Hours until next SLA breach

Then, select one of the "(business)" options to calculate time
based on your business hours.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/business_hours_automation.png)

If you are on an Enterprise plan and have multiple schedules,
automations based on business hours will use the schedule
applied to the ticket.

For information about creating automations, see [Streamlining
workflows with time-based events and
automations](https://support.zendesk.com/hc/en-us/articles/4408883801626).

### Triggers based on holidays

You can create triggers based on holidays using the "Ticket: On a holiday?" condition.
This enables you to build triggers that fire based on whether an event occurs during a
holiday.

This condition is set to yes for the full day of the holiday, not just during your normal
business hours that day. For example, if you have a Monday holiday and your normal
business hours on Mondays are 9am to 5pm, the holiday is considered the full calendar day,
including hours outside of your normal hours, such as 10pm.

If you are on an Enterprise plan and have multiple schedules, this condition respects the list of
holidays set in the schedule applied to the ticket.

## Creating triggers based on multiple schedule (Enterprise plans only)

If you are on an Enterprise plan and have created multiple schedules, you
can create triggers based on multiple schedules.

Use the "Ticket: Schedule" condition to build triggers that fire based on
the schedule applied to a ticket.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/business_hours_multiple_trigger.png)

Use "Ticket: Within schedule" condition to build triggers that fire based
on a selected schedule.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/business_hours_trigger_within_sched.png)

You can use the "Ticket: Set schedule" action to apply a schedule to a
ticket. For more information, see [Applying your
schedules to tickets](#topic_1ly_q4h_ms).

## Reporting based on business hours

You can use Zendesk Explore to build reports based on business hours set in your schedule.

If you are on an Enterprise plan and have set up multiple schedules, reports based on business
hours use the schedule that is set for the ticket (see [Applying a schedule to your tickets](#topic_1ly_q4h_ms)). To find out which schedule is
applied to a ticket, you can view that ticket's events (see [Viewing a ticket's audit trail](https://support.zendesk.com/hc/en-us/articles/4408829602970-Viewing-a-ticket-s-audit-trail)).

Note: Any report based on business hours also take scheduled holidays into account, and
consider them as outside of your business hours. You cannot build reports based solely on
holidays.

You can build reports based on business hours using any of the following Explore metrics:

- **First reply time - Business hours** - The duration between when the ticket was created and
  the first public agent reply on the ticket within
  business hours.
- **First resolution time - Business hours** - The duration between when the ticket was created
  and its first resolution within business hours.
- **Full resolution time - Business hours** - The duration in minutes between when the ticket
  was created and its latest resolution within
  business hours.
- **Requester wait time - Business hours** - The number of minutes a ticket spends in the New,
  Open, or On-hold status during business hours. This
  number is only measured after a ticket's status is
  changed from New/Open/On-hold to
  Pending/Solved/Closed
- **On-hold time - Business hours** - The total combined time in minutes that the ticket was in
  the on-hold status during business hours.
- **Agent wait time - Business hours** - The total
  combined time that the ticket was in the pending
  status within business hours. It measures how long
  agents were waiting for the customer replies within
  business hours.

Note: To learn about all of the metrics you can use with Zendesk Support, see [Metrics and
attributes for Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408827693594).

For information about Explore see [Zendesk Explore
resources](https://support.zendesk.com/hc/en-us/articles/4408846357018).