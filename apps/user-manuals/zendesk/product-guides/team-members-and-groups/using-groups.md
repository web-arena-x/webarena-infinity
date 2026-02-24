# Using groups

Source: https://support.zendesk.com/hc/en-us/articles/4408839035546-Using-groups

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

As described in [About organizations and groups](https://support.zendesk.com/hc/en-us/articles/4408886146842), groups are used to create collections of team members based on criteria those team members have in common. Groups can be used in business rules and to create focused views.

This article covers the following topics:

- [Using groups in business rules](#topic_vdv_snb_wqb)
- [Creating views by group](#topic_cn2_ytm_1rb)

## Using groups in business rules

Groups can be used in automations, macros, and triggers. When creating automations and triggers you can use group as a criterion for making updates to tickets. Using a macro, you can assign a group to tickets as an action.

There are many reasons that you might include group in an automation or trigger.
Here are several examples of how they are commonly used.

### Example: Escalating tickets using group in an automation

In an automation, you can use group as a condition to escalate tickets for a specific group.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/groups_automation_example.png)

The Level 2 support team provides a higher level of service to their customers and promises to solve tickets quickly; this is their service level agreement. This automation helps them manage this commitment by reminding them if their tickets are not updated after 48 hours.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/groups_automation_example_actions.png)

The actions in this automation set the priority to urgent and send an email to the ticket assignee as a reminder to update the ticket. For more information about creating automations, see [Streamlining workflow with time-based events and automations](https://support.zendesk.com/hc/en-us/articles/4408883801626).

### Example: Notifying a group of a ticket assignment with a trigger

Perhaps the most common use of groups in a trigger is to notify a group when a ticket has been assigned to the group (it's one of the default triggers).
You can take a look at this trigger by following these steps:

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. Locate the **Notify group of assignment** trigger and then select **Edit**.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/groups_trigger_example.png)

This trigger fires when a group is assigned to a ticket. The change event could have been triggered manually by an agent or automatically by another business rule (automation or trigger).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/groups_trigger_example_actions.png)

The actions inform everyone in the group about the new ticket assignment.
Note that inborn system rules exist to reduce the number of duplicate email notifications sent to users about a single request. For example, if an agent is a recipient on the group notification but also a CC on the ticket, ticket notifications may be [suppressed](https://support.zendesk.com/hc/en-us/articles/4408843347866) to prevent duplicates.

For more information, see [Creating ticket triggers for automatic ticket updates and notifications](https://support.zendesk.com/hc/en-us/articles/4408886797466).

### Example: Assigning a group to a ticket using a trigger

A group can be used as a condition in a trigger, which allows you to filter incoming requests and assign them to the appropriate group.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/groups_trigger_example2.png)

In this example, the conditions are used to determine if the ticket is a sales inquiry.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/groups_trigger_example2_actions.png)

The actions set the type to Question and then assign the ticket to the Sales group. This example also illustrates that you can extend the use of Zendesk Support to other areas of your business, not just the Support agents.

If only one agent belongs to a group, all tickets assigned to that group will be assigned directly to that agent. The status of the ticket will automatically move from New to Open.

For more information, see [Creating and managing triggers](https://support.zendesk.com/hc/en-us/articles/4408886797466).

## Creating views by group

Your groups can be used to create views. Here's an example.

### Example: Creating a view of tickets by group

One of the default views shows you all the tickets that have been assigned to the groups you belong to. You can take a look at this view by following these steps:

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Views**.
2. From the list of views, hover over the **Unsolved tickets in your groups** view and then select **Open**. Alternatively click the view name.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/groups_view_example.png)

This view displays unsolved tickets that are assigned to your groups. You could of course select one or more specific groups instead if you were to customize this view.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/groups_view_example_results.png)

This is the result, formatted as a table. The tickets are listed by groups.