# Streamlining your support workflow

Source: https://support.zendesk.com/hc/en-us/articles/4408889268378-Streamlining-your-support-workflow

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Managing your customers’ support issues and your ticket workflow requires tools to help
create as many efficient processes as possible. The best way to understand how Zendesk
Support helps you manage your support workflow is to look at how a typical ticket
workflow can be streamlined with the tools that Zendesk Support provides.

Tip: **Fine Tuning:** Learn more about how you can optimize your Zendesk
to best support your workflow in Don Newton's Brick-by-brick: How to piece together
your ideal Zendesk,
[Part 1](https://support.zendesk.com/hc/en-us/articles/4408886987546) and
[Part 2](https://support.zendesk.com/hc/en-us/articles/4408882066202).

This article discusses the following tools:

- [Ticket handling shortcuts](#id113ND0H60Y4)
- [`Triggering actions when tickets are
  created or updated](#id113ND0NF0HS)
- [Using time-based events to activate
  actions](#id113ND0S06UI)
- [Notifying external targets about
  ticket events](#id113ND0XL0HT)
- [Using tags to manage
  workflow](#id113ND0V08YK)

## Ticket handling shortcuts

It's common to get support requests for issues that affect more than one person and
can be answered with a single, standard response. To do this, you use
macros to create the standard responses, that agents can apply to
tickets. Macros can also be used to update tickets without also notifying the
requester. For example, you can use macros to change the agent or group assignment.
See [Using macros to update tickets](../../agent-guide/ticket-automation-and-collaboration/using-macros-to-update-tickets.md) and [Creating macros for tickets](https://support.zendesk.com/hc/en-us/articles/4408844187034) for more information.

Below is an example of a macro that sends an email notification to the requester in
response to an issue that affects many people in an organization:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macro_intranet.png)

This macro adds a public comment to the ticket, sets the status to solved, and adds a
relevant tag. You will see included in the comment the text
"{{ticket.requester.first\_name}}". This is called a *placeholder* and is used
for automatically inserting data into an email notification. For this example, the
placeholder would automatically insert the first name of the ticket requester in the
email notification. For more information about placeholders and how they are used,
see [Using placeholders](zug_placeholders.html#topic-1).

Macros can also be used as shortcuts to streamline repetitive ticket handling tasks.
See [Building macro action statements](https://support.zendesk.com/hc/en-us/articles/4408832783642) for
information on the different macro actions available.

## Triggering actions when tickets are created or updated

When a ticket is created or updated, you can automatically respond by modifying
ticket properties and sending email notifications to the requester using
*triggers*.

Triggers are built off of conditions and actions. Conditions define the criteria, and
if the criteria is true, trigger the actions. In other words, if a ticket condition
is true then perform actions, such as make changes or notify a customer or agent.
For example, you can use triggers to automatically assign tickets based on a
requester's email domain or keywords in the ticket description. See [About triggers and how they work](https://support.zendesk.com/hc/en-us/articles/4408822236058-About-triggers-and-how-they-work).

Zendesk Support provides a set of [standard triggers](https://support.zendesk.com/hc/en-us/articles/4408828984346) as best practices in a typical ticket
workflow. You can view the default triggers and create or edit new triggers in Admin
Center by clicking the **Objects and rules** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)) in the sidebar, then selecting **Business rules >
Triggers** One available default trigger is "Notify requester of received
request". On the Triggers admin page, you can click Notify requester of received
request to view all the conditions and actions it uses.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/trigger_notify_requester_new.png)

As you can see the conditions require the ticket to be created and the status to not
be Solved. If those two conditions are true, the action sends an email notification
to the requester informing them the request has been received and is now a ticket.
You can use this trigger as is or clone it to make copies that you can modify and
repurpose. If you need to, you can deactivate these default triggers or you can
create entirely new triggers. See [Creating triggers](https://support.zendesk.com/hc/en-us/articles/4408886797466) for more information.

Note: Zendesk
Support automatically runs through all of your triggers (from first to last) to
see if each trigger's criteria is met. Whenever the ticket matches the
conditions the trigger is fired. This means the actions of one trigger might
affect the actions of other triggers. See  [Reordering triggers](https://support.zendesk.com/hc/en-us/articles/4408886797466#topic_vnl_zpy_tb) for information
on selecting the order of triggers fired.

## Using time-based events to activate actions

While triggers enable you to automatically act on tickets when they are created or
updated, you can also modify tickets and send email notifications based on events in
time. For example, you might want agents to be alerted if tickets remain unassigned
after 24 hours. To do this in Zendesk Support, you can use [*automations*](https://support.zendesk.com/hc/en-us/articles/4408832701850). Zendesk Support provides a set of
 [standard automations](https://support.zendesk.com/hc/en-us/articles/4408835051546) which administrators
can edit or they can create new automations. You can access your automations in
Admin Center by clicking the **Objects and rules** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)) in the sidebar, then selecting **Business rules >
Automations**

Automations, like triggers, contain conditions and actions. The image below shows an
example automation that will automatically close a ticket four days after the ticket
is solved.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/automation_close_4days.png)

As you can see the conditions require the ticket to be solved and will activate after
96 hours, or four days, after the ticket has been solved. The action then changes
the status from Solved to Closed. Four days is a best estimate for the minimum
amount of time a ticket should remain in the Solved state before it is closed.

Unlike triggers, which are based on ticket events and run immediately after tickets
are created or updated, automations only run once every hour and only on tickets
that have been created or updated in the last 28 days.

For more information about using automations, see [Streamlining workflow with time-based events and
automations](https://support.zendesk.com/hc/en-us/articles/4408883801626).

## Notifying external targets about ticket events

There may be times when you want to notify an external target about a new ticket or
an important state change to a ticket. For example, you might want to send a text
message or post a notification to a company-wide stream. By setting up external
targets you can communicate with many cloud-based applications and
services (such as X, formerly Twitter, and Twilio) as well as HTTP and email.

After you've defined a target you can add it to automations and triggers. For
instructions on adding and managing external targets, see [Notifying external targets](https://support.zendesk.com/hc/en-us/articles/4408883282458-Notifying-external-targets).

## Using tags to manage workflow

To help you categorize, act on, or search for tickets, you can add tags.
Tags can be added to tickets automatically based on the words in the request,
manually by agents, or via triggers, automations, and macros. Once added, you can
create views by tags, search for tags and the tickets in which they are included,
and use tags in your triggers, automations, and macros. See [Using tags](https://support.zendesk.com/hc/en-us/articles/4408888664474-Using-tags) for more information about
tags.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/tags.png)

Tags are helpful throughout the entire support workflow, but are especially for the
following support tasks:

- Locating answers to support requests that have already been answered. Agents
  can search for tickets by tags. See [Searching for tickets by tags](https://support.zendesk.com/hc/en-us/articles/4408888664474-Using-tags#topic_ntk_ina_vb).
- Creating ticket reports using tags. This provides you with a way to monitor
  hot issues and trends, for example. See
  [Reporting on ticket tags
  (Explore)](https://support.zendesk.com/hc/en-us/articles/4408838151450).
- Creating custom workflows. Perhaps you want to add a custom field to your
  support request form and then act on that data. Custom fields contain tags
  that can then be added to triggers to, for example, route a request for a
  specific product to a specific support group or agent. See  [Understand tags and ticket fields](https://support.zendesk.com/hc/en-us/articles/4408881943194)
  for more information on custom fields and tags and [Using tags in macros, triggers, and
  automations](https://support.zendesk.com/hc/en-us/articles/4408888664474-Using-tags#topic_umd_ona_vb) for more information on incorporating tags into your
  business rules.