# Using the "Hours since" condition in automations

Source: https://support.zendesk.com/hc/en-us/articles/4408836495130-Using-the-Hours-since-condition-in-automations

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

[Automations](https://support.zendesk.com/hc/en-us/articles/4408832701850) enable you to set up time-based actions to modify tickets or send email notifications. One popular use of automations is to perform an action a certain amount of time after the ticket is created or changed. There are two ways to define time-based conditions.

This article covers the following topics:

- [Understanding how hours are counted](#topic_gbj_5yz_sqb)
- [Using "Hours since...greater than" and "Hours since...less than" conditions](#topic_ssx_rd1_tqb)
- [Using "Hours since...is" conditions](#topic_ld3_5d1_tqb)
- [Understanding how the automations ticket limit works with "Hours since" conditions](#topic_khk_rdh_tsb)

Note: On Professional and Enterprise plans, you can [configure business hours and holidays](https://support.zendesk.com/hc/en-us/articles/4408842938522). Then you can set automations to run based on business hours or calendar hours.

## Understanding how hours are counted

When you specify the number of hours that should be met or exceeded for an automation to fire, it's important to understand these four things:

- You can only specify whole hours, not days or fractional hours
- The clock doesn't start until the automation runs
- Automations run hourly, not immediately after a condition is met
- Automations can only act on 1000 tickets per cycle. See [Understanding how the automations ticket limit works with "Hours since" conditions](#topic_khk_rdh_tsb).

Because automations run hourly, each run counts towards the hours since a condition was met. The first time an automation runs after conditions are met, which could be 1-59 minutes later, counts as "zero" hours and starts the clock. Then, each subsequent automation run counts as one additional hour. After the number of hours has elapsed or been exceeded, then the automation fires and executes the action.
It's also important to note that you can only specify time in whole hours.

Let's use the default automation **Close ticket 4 days after status is set to solved** as an example. This automation changes the status of a ticket after 96 hours *or more* have passed since its status was set to *Solved*.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/automation_close_after_4days.png)

Given this automation, let's say a ticket is solved at 9:15 am on August 20. The first time the automations runs after the status condition is met is 10:03 am (48 minutes later). The count increases by one with every subsequent automation run. The ticket reaches the 96 hour mark when the automation runs at 10:11 am on August 24, at which point the automation fires and changes the ticket's status to *Closed*. The action to change the ticket's status prevents the automation from being valid more than once per ticket.

## Using "Hours since...greater than" and "Hours since...less than" conditions

When creating conditions based on elapsed time, we recommend using *greater than* and *less than* whenever possible. This operator gives the automation a bigger window in which it's true and can fire, which reduces the possibility of missing the window. However, automations need to be defined so that they are only true for a ticket once. That means automations that use the greater than and less than operators must include a nullifying condition or action. One easy way to cancel a condition is to add a tag. For example, you can define two conditions that must be met (the time elapsed and the absence of the tag) and an action to add the tag when the automation fires on the ticket.

In the following example, the automation checks for tickets without the *pending-reminder-sent* tag that have been pending for 120 hours (5 days)
or more. When a ticket meets these conditions, a notification is sent and the *pending-reminder-sent* tag is added. The addition of the tag prevents the ticket from meeting the automation's conditions again.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/automation_pending_5days.png)

For more information, see [Ensuring your automation only runs once](https://support.zendesk.com/hc/en-us/articles/4408832701850#topic_mbl_q4f_tm).

## Using "Hours since...is" conditions

Note: In almost every instance that you may want to use an *is* operator, it is possible to use *greater than*.

You can also use the *is* operator when defining automations based on the time elapsed. When you define an "Hours since...is" condition, the automation fires only during the brief window in which it's true. Because time-elapsed automations with the *is* operator are only valid for an hour or less, a nullifying action isn't required because there is no possibility of the conditions being true more than once.

The downside to having such a narrowly defined and brief state of being true is that if, for some reason, your automation doesn't run during that hour, the condition can't be met on subsequent runs. Because of the slight variation of run times for automations in any given hour, it is unlikely but possible for an *is* condition to never evaluate to true. For example, if you define a condition in which tickets were created one hour ago and you create a ticket at 10:03. If the automation fires is at 11:01, the ticket was only created 58 minutes ago and therefore the automation isn't yet true. However, if the next time the automation fires is at 12:06, the ticket was created 2 hours and 3 minutes ago, and the condition fails to be met all together.

Additionally, all automations typically run in order every hour and fire on all tickets where conditions are met, but there are some scenarios that may result in some but not all automations running within an hour. This is only likely to be an issue if you have a lot of automations or a high volume of tickets.

## Understanding how the automations ticket limit works with "Hours since" conditions

Because automations can only act on 1000 tickets per cycle, if you have more than 1000 tickets that meet your automation conditions, some will be missed in the hour the automation runs. In this case, use the "Hours since... greater than" condition.
This enables the the automation to fire for the rest of the tickets in the next hour. If you use the "Hours since... is" condition, the automation cannot fire again on those extra tickets. They will be missed completely.