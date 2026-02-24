# Lesson 4: Business rules

Source: https://support.zendesk.com/hc/en-us/articles/4408885959066-Lesson-4-Business-rules

---

- [Introduction: Getting started with Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408884056346)
- [Lesson 1: Ticket Basics](https://support.zendesk.com/hc/en-us/articles/4408881925786)
- [Lesson 2: Viewing and Organizing](https://support.zendesk.com/hc/en-us/articles/4408883609370)
- [Lesson 3: Solving Tickets](https://support.zendesk.com/hc/en-us/articles/4408882997530)
- [Lesson 4: Business Rules](https://support.zendesk.com/hc/en-us/articles/4408885959066)
- [Where to go next](https://support.zendesk.com/hc/en-us/articles/4408883043226)

Topics covered in this lesson:

[Triggers and automations](#triggers-automations) [The building blocks: conditions and actions](#conditions-actions) [Standard Zendesk Support notification triggers](#standard-notif-triggers) [Automations](#automations)

## Triggers and automations

We've now arrived at the area of Zendesk that many people find a little harder to understand—at least initially. This lesson describes automated business rules. This means predefined actions that are automatically applied to tickets. There are two types of automated business rules: *automations* and *triggers*.

Let's start with what's common to both before we explain how they are different. Automations and triggers define a set of *actions* that will occur when a ticket matches specific *conditions*. For example, if a ticket is created by an end user who belongs to a specific organization (this is the condition), it can be automatically assigned to the agent group that provides support to that organization (this is the action).

To make this even simpler to understand, it boils down to this easy formula: if *x* is true, then do *y*.

So what's the difference between automations and triggers? Each contains a set of conditions and a set of actions. Each modifies a ticket's data. Each affects tickets when specific events occur. The difference is the kind of events that cause the ticket to be modified. Automations act on tickets based on an event in time (for example, four hours after a ticket update). Triggers act on a ticket when a ticket is created or updated (the create and update events). If a ticket doesn't meet the conditions contained in your automations or triggers nothing will happen.

The purpose of creating automated business rules is so that your agents no longer need to do these types of repetitive tasks manually. In the next few sections of this lesson, we'll dig a little deeper into both automations and triggers.

### Who can create automations and triggers?

Only admins can create and manage automations and triggers. This is because these business rules might affect every ticket, and it's the responsibility of an admin to define your custom automations and triggers as part of the overall support workflow they set up.

## The building blocks: conditions and actions

Automations and triggers consist of sets of conditions and actions. If a ticket meets the conditions then the actions are applied. Let's take a closer look at conditions to get started.

Conditions are references to ticket and user fields and the data contained in those fields.

There are two types of conditions – *all* conditions and *any* conditions. The *all* conditions, as you've probably already figured out, must all be true. If any of the condition statements fail (are not true), the automation or trigger will not act on the ticket.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_intro_action3.png)

Additionally at least one of the *any* conditions must also be true. For example, you might want an automation or trigger to act only on tickets that are submitted from a list of specific email addresses, as in this example:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_intro_action2.png)

If either of these conditions is true, the automation or trigger will act on the ticket. If you use only one condition in the *any* section, it will behave like an *all* condition and therefore must be true for the automation or trigger to act on the ticket.

Action statements follow the same format, but rather than testing for conditions to be true or not, actions set ticket properties and send email notifications, as in this example:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_intro_action1.png)

Conditions, unlike actions, contain operators that you can use to build condition statements. For example, using the Is not operator allows you to single out a value to exclude from a condition, just as we did in this example (Ticket: Status is not Solved). You'll also use other operators, such as Less than, Greater than, Changed to, and Changed from.

## Standard notification ticket triggers

Zendesk comes with a number of helpful triggers that are used to notify ticket requesters, agents, and groups when certain events occur. They are all activated by default and are ready to take action on any tickets that meet the conditions.

You can review these triggers on the Triggers page admin page (in [Admin Center](https://support.zendesk.com/hc/en-us/articles/4408838272410) > Objects and rules > Business rules > Triggers).

Let's look at the Notify requester of received request trigger. This trigger sends an email message to the ticket requester when a new ticket is received. Here are the conditions:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_intro_trigger1.png)

The Ticket > Is condition is used to capture the two trigger events that we discussed earlier: *created* and *updated*. If you only want a trigger to act on new tickets, you select Created. This is the choice we want for this trigger because we only want the ticket requester to receive the new ticket confirmation email once, when the ticket is created. There are other triggers for notifying the requester when an agent has added a comment and when the ticket has been solved. Each of those triggers uses Ticket > Is > Updated.

The second condition, Status > is not > Solved, is used because we only want the trigger to apply to active tickets—not our solved tickets.

Now let's look at the actions contained in this trigger and what will happen when the trigger is applied to a ticket.

The purpose of this trigger is to notify the requester that their support request was received and a ticket was created. To do that, we create an email notification using the combination of actions shown here:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_intro_trigger2.png)

Take a quick look at each of the notification triggers and you can see how they all work.

This video will give you a quick introduction to how triggers work:

Automating notifications with triggers (2:02)

## Using placeholders in automations and triggers

Just like macros, you use placeholders in automations and triggers to dynamically insert user and ticket-specific data into ticket replies and the email notifications that are sent to the ticket requester.

Try it yourself: Build an escalation trigger

### Build an escalation trigger

To exercise a little bit of what you've just learned, let's create a simple but very useful trigger. This trigger will escalate all tickets from VIP customers. If you recall from a previous lesson, you can add tags to user and organization profiles and those tags are automatically added to every ticket from those users or users within those organizations. In this example, we'll use a tag to identify the incoming tickets that need to be escalated.

If you'd like to try creating an escalation trigger, follow these steps:

1. In[Admin Center](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **Objects and rules** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)) in the sidebar, then select **Business rules > Triggers.**
2. Click **Add Trigger**.
3. Enter the title *Escalate VIP tickets*.
4. Add the **Status** condition and then select **Less than** as the condition operator and then **Solved**.
5. Click **Add condition** and then select **Tags**. The condition operator is **Contains at least one of the following**, which is what we want. Now, enter *vip* as the tag.
6. Now we need to add the actions. When a ticket contains the *vip* tag, we want it to be assigned to the Advanced support group that we created in a previous lesson. In the actions section, select **Group** then select **Advanced support**.
7. We also want to set the ticket's priority to **Urgent**. Add a new action by clicking the + button and selecting **Priority,** then selecting **Urgent**.
8. Save the trigger by clicking **Create**.

Whenever a ticket contains the *vip* tag, this trigger will act on it.

## Automations

As you learned in a previous section, both automations and triggers are built with conditions and actions. However, since automations are based on events in time, they contain additional conditions that allow you to make ticket updates a certain number of hours after certain events occur. For example, you can create an automation that sets a ticket's priority to Urgent after some number of hours have passed since it was created.

That's one example of how an automation might be used. In Zendesk, tickets are closed by automation, not manually. This is one of the standard automations. It's called Close ticket 4 days after status is set to solved. You can review it in the Automations admin page (in [Admin Center](https://support.zendesk.com/hc/en-us/articles/4408838272410) > Objects and rules > Business rules > Automations). We've found that closing tickets four days after they have been solved is a best practice; however, you can of course change this automation and set it to as many days as you'd like, up to 28 days. After that, Zendesk will automatically close the ticket.

Time-based conditions provide you with the flexibility to craft automations based on specific events in the ticket lifecycle. Here are the common uses of automations:

- Notifying agents when an assigned ticket remains unresolved for *x* number of hours
- Notifying agent groups when a new ticket remains unassigned for *x* number of hours
- Increasing a ticket's priority if a certain amount of time has passed without the ticket being touched
- Notifying the assigned agent after *x* number of hours when a pending ticket has been updated by the requester
- Closing tickets *x* number of days after they have been set to solved

### A safe place for testing your business rules

As we mentioned earlier, only admins can create automations and triggers because these business rules potentially affect all of tickets. On Enterprise plans, you can also create a test version of your account, referred to as a *sandbox*, that you can use to test and fine-tune, new automations, triggers, or anything else without actually making changes to your actual tickets.

Try it yourself: Build an escalation automation

### Build an escalation automation

As a companion to our escalation trigger, let's build an automation that alerts the assigned group and agent that the VIP ticket hasn't been handled in the amount of time we've promised.

This automation will escalate all VIP tickets that have not been responded to within 1 day. In this case, escalation means raising the priority from High to Urgent. We'll also send an email notification to the agent to make sure that they're aware of the Urgent status.

Watch this video to see how an escalation automation is created:

Building an Automation (1:34)

If you'd like to try creating an escalation automation, follow these steps:

1. In[Admin Center](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **Objects and rules** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)) in the sidebar, then select **Business rules > Automations.**
2. Click **Add Automation**.
3. Enter the title *Escalate unsolved VIP tickets to Urgent*.
4. Add the **Ticket: Status** condition and then select **Less than** as the operator and then **Solved**.
5. Add another condition by clicking the + button and then select **Ticket: Hours since created** and then **(calendar) Is** as the operator and **24** for the number of hours that have passed since the ticket was created.
6. Add another condition by clicking the + button and then selecting **Tickets: Tags**. The condition operator is **Contains at least one of the following** and the tag is *vip*.
7. Finally, we add the actions. The way we have our VIP trigger from a previous section of this lesson set up is that when a ticket is received from a VIP customer, the tag is detected and the ticket's priority is set to **High**. To escalate this ticket, we now want to set the ticket's priority to **Urgent**. Add the action **Ticket: Priority = Urgent**.
8. Our last action is to email the assigned agent. We do this by adding **Notifications: Email user = (assignee)**. We then enter a subject and a description for the email notification.
9. Save the automation by clicking **Create automation**.