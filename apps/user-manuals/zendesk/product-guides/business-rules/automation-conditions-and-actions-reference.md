# Automation conditions and actions reference

Source: https://support.zendesk.com/hc/en-us/articles/4408885654298-Automation-conditions-and-actions-reference

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

This article describes the different conditions and actions available when creating
automations. For information on creating new automations, see [Creating and managing automations for time-based
events](creating-and-managing-automations-for-time-based-events.md).

This article contains the following sections:

- [Building automation condition statements](#topic_k3n_zlz_1cb)
- [Building automation action statements](#topic_ezl_zlz_1cb)

## Building automation condition statements

As with triggers, the condition statements you create for automations contain conditions,
operators, and values. These include conditions you’d expect such as priority, status,
assignee and so on. Because automations are based on the hours that have elapsed since a
ticket update was made, Zendesk provides the following time-based conditions:

- Hours since created
- Hours since open
- Hours since pending
- Hours since on-hold
- Hours since solved

  Note: When you [activate custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306), existing automations
  that use an hours since [*system ticket status name*] condition are updated to
  the corresponding hours since status category [*category name*] condition.
- Hours since status category [*category name*]
- Hours since assigned (to an agent)
- Hours since update
- Hours since requester update (for updates made by the requester)
- Hours since assignee update (for updates made by the assignee)
- Hours since due date (for tickets with the type set to Task)
- Hours until due date (for tickets with the type set to Task)
- Hours since last SLA breach
- Hours until next SLA breach
- (Enterprise only) Hours since last Group SLA breach
- (Enterprise only) Hours until next Group SLA breach
- Hours since [*system or custom ticket status name*]

**Note the following restrictions when using time-based conditions:**

- Time-based conditions aren't available from **Meet any of these conditions**
  section of the automation creator (see [Creating and managing automations for time-based
  events](creating-and-managing-automations-for-time-based-events.md)). Automations require a nullifying condition to ensure that they aren't
  running continuously.
- **Due date** refers to 12 PM in your account's timezone on the date
  specified.
- Only whole numbers can be used as the value for these conditions. For example, Hours
  since created = (calendar) is = 1, is valid. Decimals aren't supported. If you set the
  hours since variable to 1.5, it will be interpreted as 1, which means that it was
  rounded down to the whole number.
- **Hours since [status]** conditions, such as **Hours since open**, only fire if
  the ticket remains in that status or status category. For instance, if you create an
  automation that fires when **Hours since open is 2**, it will not fire if the status
  changes from *open* to *pending* before the two hours are up.
- The **is** condition for **Hours since** applies only for a certain timeframe.
  For example, if you create an automation that includes **Hours since solved is 24**,
  but the automation runs after 24 hours have passed, the automation will not fire.
  Consider using **Greater than** or **Less than** for these types of
  conditions.
- **Hours since update** means that any update to the ticket – including an automation
  firing – will update the ticket.
- **Hours until > less than** conditions are inclusive (they include both "less than"
  and "equal to"). For example, **Hours until next SLA breach > less than > 2** can
  fire at *exactly* two hours before the SLA breach time. All other time-based
  conditions are exclusive.
- Because automations can't update or change closed tickets, there isn't an **Hours
  since closed** time-based condition.

The other conditions you can use in your automations are described in the following
table.

Table 1. Automation conditions

| Condition | Description |
| --- | --- |
| Ticket: Status | Note: If you’ve [activated custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306), existing standard ticket statuses become status categories. If you have existing conditions that use Status, they’re updated to the corresponding Status category.  The standard ticket status values are:  **New** is the initial status of a newly created ticket (not assigned to an agent).  **Open** means that the ticket has been assigned to an agent.  **Pending** is used to indicate that the requester has been asked for information and the ticket is therefore on hold until that information has been received.  **On-hold** means that the support request is awaiting a resolution from a third party—someone who is not a member of your support staff and does not have an agent account in your Zendesk account. This status is optional and must be added (see [Adding the On-hold ticket status](https://support.zendesk.com/hc/en-us/articles/4408889282458-Adding-the-On-hold-ticket-status-to-your-Zendesk)).  **Solved** indicates that the customer’s issue has been resolved. Tickets remain solved until they are closed.  **Closed** means that the ticket has been locked and cannot be reopened or updated.  When selecting a status, you can use the field operators **Less Than** and **Greater Than** to specify a range of tickets based on their status. **New** is the lowest value, with values increasing until you get to **Closed** status. For example, a condition statement that returns only New, Open, and Pending tickets looks like this:  **Status is less than Solved**. |
| Ticket: Status category | Note: If you’ve [activated custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306), system ticket statues and any ticket statuses you create are grouped into status categories. Each status category has a default ticket status. See [Managing ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575941402-Managing-ticket-statuses-#topic_zgh_dbh_vrb).  The status category values are:  **New** is the initial status category of a newly created ticket (not assigned to an agent).  The **Open** status category is for grouping ticket statuses that indicate when tickets are ready to be worked on by your support team.  The **Pending** status category is for grouping ticket statuses that are used to indicate that the support team is waiting for the requester to reply. The **On-hold** status category contains ticket statuses used to indicate that the support request is awaiting a resolution from a third party—someone who is not a member of your support staff and does not have an agent account in your Zendesk. This status category is optional and must be added to your Zendesk (see [Adding on-hold ticket status to your Zendesk](https://support.zendesk.com/hc/en-us/articles/4408889282458-Adding-the-On-hold-ticket-status-to-your-Zendesk)). The **Solved** status category contains ticket statuses that indicate that the customer’s issue has been resolved.  The **Closed** status category contains the Closed system ticket status that indicates that the ticket has been locked and cannot be reopened or updated.  When selecting a status category, you can use the field operators **Less Than** and **Greater Than** to specify a range of tickets based on their status category. **New** is the lowest value, with values increasing until you get to **Closed** status category. For example, a condition statement that returns tickets only in the New, Open, and Pending categories looks like this:  **Status category is less than Solved**. |
| Ticket: Brand (not available on Team plans) | Checks whether a ticket is associated with the specified brand. |
| Ticket: Ticket status | If you’ve [activated custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306), you can select system ticket statuses and new ticket statuses you created as conditions. |
| Ticket: Form (Enterprise plans only) | Your ticket forms are available as conditions. Select a specific form. See [Creating ticket forms to support multiple request types](https://support.zendesk.com/hc/en-us/articles/4408846520858) |
| Ticket: Type | The ticket type values are:  **Question**  **Incident** is used to indicate that there is more than one occurrence of the same problem. When this occurs, one ticket is set to Problem and the other tickets that are reporting the same problem are set to Incident and linked to the problem ticket.  **Problem** is a support issue that needs to be resolved. **Task** is used by the support agents to track various tasks. |
| Ticket: Priority | There are four values for priority: **Low**, **Normal**, **High**, and **Urgent**.  As with status, you can use the field operators to select tickets that span different priority settings. For example, this statement returns all tickets that are not urgent: Priority is less than Urgent |
| Ticket: Group | The group values are:   - **(—)** indicates that no group is assigned to the ticket. - **Group name** is the actual name of the group that is assigned to the ticket.   Additional value for views:   - **(current user's group)** is all the groups that the agent belongs to. |
| Ticket: Assignee | The assignee values are:   - **(—)** or leaving the field empty indicates that the ticket is unassigned. - **(requester)** is the ticket requester. You can select   this option to return tickets that were opened by and then assigned to the same   agent, for example. - **Agent name** is the actual name of the person assigned to the   ticket.   Additional value for views:   - **(current user)** is the person who is currently viewing the view. For   example, if the view condition was **Assignee** > **Is** > **(current   user)** then the agent viewing the view would be shown all the tickets for   which they are the assignee. This enables one view to show relevant tickets to   each agent, without having to create a specific view for each individual agent. |
| Ticket: Requester | The requester values are:   - **(assignee)** is the person   assigned to the ticket. The condition statement ‘Requester is Assignee’ is true if   the requester is also the person assigned to the ticket.  This is possible if an   agent created a ticket and was then assigned to it. - **Agent name** is the actual name of the agent.   Additional value for views:   - **(current user)** is the person currently looking at the view. If you are   looking at the view, you will see tickets for which you are the requester. |
| Ticket: Organization | The organization values are:   - **(—)** indicates that no organization has been added to the ticket. If you   have multiple organizations, **(—)** displays for a certain number of   organizations, but is a blank value above that number. If you have a large   number of organizations, start typing the organization name to find a   match. - **Organization name** is the name of an organization. |
| Ticket: Tags | You use this condition to determine if tickets contain a specific tag or tags. You can include or exclude tags in the condition statement by using the operators **Contains at least one of the following** or **Contains none of the following**. More than one tag can be added. Tags must be separated with spaces. |
| Ticket: Description | The description is the first comment in the ticket. It does not include the text from the subject line of the ticket. If you are using the **Contains at least one of the following** or **Contains none of the following** operators, the results will consider words containing part of the entered search terms. For example, using "none" for this condition will return (or exclude) ticket descriptions containing "nonetheless".  The description condition also pulls data contained within the HTML and the original source of a ticket. |
| Ticket: Channel | The ticket channel is where and how the ticket was created. The contents of this list will differ depending on the channels you have active, and any integrations you are using.  For more information about the channels you can configure, see [About Zendesk Support channels](https://support.zendesk.com/hc/en-us/articles/4408824097050-About-Zendesk-Support-channels) and [Understanding ticket channels in Explore](https://support.zendesk.com/hc/en-us/articles/4408836378394). |
| Ticket: Integration account | This condition checks the integration account that the ticket came from, such as a specific Facebook page, X (formerly Twitter) handle, or other channel integration account, like GooglePlay. Select one of your configured integration accounts from the drop-down menu. |
| Ticket: Received at | Checks whether a ticket **Is** or **Is not** received by one or more email addresses.  This condition checks the email address from which the ticket was received and the email address from which the ticket was originally received. These values are often, but not always, the same. The ticket can be received from a Zendesk email domain such as sales@mondocam.zendesk.com, or from an external email domain such as support@acmejetengines.com. The external email domain must be set up as described in [Forwarding incoming email to Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408886828698) or the condition won't work.  This condition only works for valid support addresses. This condition could be met by an email address in the CC field if it's associated with a valid support address. Email configurations like Google Groups, aliases, and distribution groups are [not supported for Zendesk support addresses](https://support.zendesk.com/hc/en-us/articles/4408821055130), and they may not meet this condition.  This condition doesn't check the channel from which the ticket originated and can be true for tickets that weren't received through email. For example, when using the [Select an Address app](https://support.zendesk.com/hc/en-us/articles/4408830888730), you can specify a recipient email address and therefore meet this condition even though the ticket was created in the agent interface.  If you're using an external address that is connected through forwarding, this condition will also be met by a Zendesk support address that received it. For example, if sales@mondocam.com forwards to sales@mondocam.zendesk.com, then both addresses will meet this condition.  If you're using an authenticated connector instead of forwarding, this condition will only be met by the external support address. |
| Ticket: Satisfaction (Not available on Team plans) | Supports the following customer satisfaction rating values: - **Unoffered** means that the survey has not previously been sent - **Offered** means that the survey has already been sent - **Bad** means that the ticket has received a negative rating - **Bad with comment** means that the ticket has received a negative rating   with a comment - **Good** means that the ticket has received a positive rating - **Good with comment** means that the ticket has received a positive   rating with a comment |
| Ticket: Privacy | This condition checks to see if a ticket has public comments or not. You can select either:  - Ticket has public comments - Ticket has no public comments |
| Ticket: *Custom fields* | Date, drop-down, and multi-select custom fields are available as conditions. Checkbox custom fields are available as automation conditions only when the checkbox is configured to set a tag. |
| Requester: Language | The language of the person who submitted the ticket. |
| Requester: *Custom fields* | Custom user fields are available as conditions. |
| Requester: Role | Adds a condition to your triggers to create a different workflow when the requester is an end user versus an agent. |
| Organization: *Custom fields* | Custom organization fields are available as conditions. If the automation has a condition like the following:  **Organization:** *field* > **Is not** > *value*  The statement will be true only if the ticket has an organization and that organization's field doesn't match. If the ticket does not have an organization, this type of condition will not be true. |
| Ticket sharing: Sent to | Checks whether a ticket was shared to another Zendesk via a specific ticket sharing agreement. |
| Ticket sharing: Received from | Checks whether a ticket was shared from another Zendesk via a specific ticket sharing agreement. |
| Ticket: Service catalog form | Used to check that the ticket uses a specific [service request forms](https://support.zendesk.com/hc/en-us/articles/4408836460698#topic_p3b_rwv_dgc). Available only when the [service catalog is turned on](https://support.zendesk.com/hc/en-us/articles/9443951511450). |

## Building automation action statements

Action statements define what occurs if all the condition statements are true and the
trigger fires. You can think of action statements as ‘then’ statements. *If* all of
your conditions are true *then* invoke these actions to update the ticket and
optionally send notifications.

Table 2. Automation actions

| Action | Description |
| --- | --- |
| Ticket: Status | Note: If you’ve [activated custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306), existing system ticket statuses become status categories. If you have existing actions that use Status, they’re updated to the default status of the corresponding Status category.  The system ticket status values can be set to the following:  **New** is the initial status of a newly created ticket (not assigned to an agent).  **Open** means that the ticket has been assigned to an agent.  **Pending** is used to indicate that the requester has been asked for information and the ticket is therefore on hold until that information has been received.  **On-hold** means that the support request is awaiting a resolution from a third party—someone who is not a member of your support staff and does not have an agent account in your Zendesk.  **Solved** indicates that the customer’s issue has been resolved. The ticket is solved even if [required ticket fields](https://support.zendesk.com/hc/en-us/articles/4408846008218#topic_x2s_g5k_1jb) are still blank. Tickets remain solved until they are closed. When tickets are closed is based on business rules you define for this step in the workflow, using automations. **Closed** means that the ticket has been locked and cannot be reopened or updated. |
| Ticket: Status category | Note: If you’ve [activated custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306), system ticket statues and any ticket statuses you create are grouped into status categories. Each status category has a default ticket status. See [Managing ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575941402-Managing-ticket-statuses-#topic_zgh_dbh_vrb).  When you use a status category as an action, the ticket status is set to the category's default ticket status.  The status category values are:  **New** is the initial status category of a newly created ticket (not assigned to an agent).  The **Open** status category is for grouping ticket statuses that indicate when tickets are ready to be worked on by your support team.  The **Pending** status category is for grouping ticket statuses that are used to indicate that the support team is waiting for the requester to reply. The **On-hold** status category contains ticket statuses used to indicate that the support request is awaiting a resolution from a third party—someone who is not a member of your support staff and does not have an agent account in your Zendesk. This status category is optional and must be added to your Zendesk (see [Adding on-hold ticket status to your Zendesk](https://support.zendesk.com/hc/en-us/articles/4408889282458-Adding-the-On-hold-ticket-status-to-your-Zendesk)). The **Solved** status category contains ticket statuses that indicate that the customer’s issue has been resolved.  The **Closed** status category contains the Closed system ticket status that indicates that the ticket has been locked and cannot be reopened or updated. |
| Ticket: Ticket status | If you’ve [activated custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306), you can specify actions that set the ticket status to a new or system status. |
| Ticket: Form (Enterprise plans only) | Your ticket forms are available as actions. Select a specific form. See [Creating ticket forms to support multiple request types](https://support.zendesk.com/hc/en-us/articles/4408846520858) |
| Ticket: Priority | The priority can be set to **Low**, **Normal**, **High** or **Urgent** |
| Ticket: Type | The type can be set to the following:  **Question**  **Incident** indicates that there is more than one occurrence of the same problem. When this occurs, one ticket is set to Problem and the other tickets that are reporting the same problem are set to Incident and linked to the problem ticket.  **Problem** is a support issue that needs to be resolved. **Task** is used by the support agents to track various tasks. |
| Ticket: Group | You can set groups to any of the following:   - **(—)** is used to unassign a group (if one has already been assigned) - **Group name** is the actual name of the group that is assigned to the ticket.   Additional value for macros:   - **(current user’s groups)** is all the groups to which the agent who is updating the ticket belongs. |
| Ticket: Assignee | You can set the assignee to any of the following:   - **(—)** or leaving the field empty is used to set assignee to no one   (unassigned) - **(requester)** is the ticket requester. You can select this option to return   tickets that were opened by and then assigned to the same agent, for   example. - **Agent name** is the agent to be assigned the ticket.   Additional value for triggers and macros:   - **(current user)** is the last person to have updated the ticket, which is   not necessarily the same person who is assigned to the ticket. The current user   (whoever updated the ticket last) changes whenever the ticket is updated. |
| Ticket: Satisfaction | You can set this action to: **offered to requester**. This indicates that the survey request has been sent to the ticket requester. |
| Ticket: Set tags | The tags you want to insert into the ticket. The set tag action deletes all tags currently applied to the ticket, or associated with any ticket fields, and replaces them. Tags must be separated with spaces. |
| Ticket: Add tags | The tags you want to add to the existing list of tags (if any).  Tags must be separated with spaces. |
| Ticket: Remove tags | The tags that you want removed from the existing list of tags contained in the ticket (if any).  Tags must be separated with spaces. |
| Ticket: Add cc | Add an agent on the ticket update. This action is available when you activate CCs on tickets.. |
| Ticket: Add follower | Add an agent or the current user as a follower on the ticket update. This action is available when you activate [CCs and Followers](https://support.zendesk.com/hc/en-us/articles/4408821501338) on tickets. When you activate this feature, the Ticket: Add follower action replaces the Ticket: Add CC action. |
| Ticket: *Custom fields* | Checkbox, drop-down, date, and multi-select custom fields are available as actions. |
| Ticket: Share ticket with (Zendesk Suite Growth and above or Support Professional and above only) | Share the ticket with the specified account. Requires that a ticket sharing agreement be in place. See [Sharing tickets with other Support accounts](https://support.zendesk.com/hc/en-us/articles/4408893967514) and [Using business rules to share tickets](https://support.zendesk.com/hc/en-us/articles/4408887148698). |
| Notifications: Email user | You can set the email user to any of the following:  - **(requester)** is the ticket requester. - **(assignee)** is the agent assigned to the ticket. - **Email user** name is the actual registered name of the agent who will   receive the email.   Additional values for triggers and automations:   - **(current user)** is the last person who updated the ticket. - **(requester and CCs)** is the ticket requester and any users who are   listed as CCs on the ticket. This value is available when [CCs and followers](https://support.zendesk.com/hc/en-us/articles/5179445630234) is enabled. If CCs   and followers is [rolled back](https://support.zendesk.com/hc/en-us/articles/4408834737434#topic_lnx_s2p_gfb), the behavior reverts to   only emailing the requester and this value is not available.   The email notification is sent only if the update includes a public comment. If the update has a private comment or no comment, the trigger or automation can still fire other actions, but it won't send the notification.  There's a known limitation for using the **Email user + (requester and CCs)** action and the **Ticket + is + Updated** conditions in triggers. When used together, Support suppresses emails to a user if the ticket update is from that same user. This is expected behavior to eliminate redundant emails. For more information about suppression, see [Understanding suppression of CCs email notifications](https://support.zendesk.com/hc/en-us/articles/4408843347866).  Adding the email user action allows you to enter the email subject and body text. Body text can be formatted using HTML or placeholders. See [Using placeholders](using-placeholders.md)  for more information on formatting with placeholders.  If you select a different notification destination when editing a trigger or automation, the body text will reset. |
| Notifications: Email group | You can set email group to any of the following:   - **(assigned group)** is a reference to the assign group. - **Email group name** is the actual name of a group.   If you select a different notification destination when editing a trigger, the body text will reset.  See [Understanding how to format email notifications](https://support.zendesk.com/hc/en-us/articles/8407456809754). |
| Notifications: Notify active webhook | Set the active webhook to notify. For more information about using webhooks, see [Creating a webhook](https://support.zendesk.com/hc/en-us/articles/4408839108378). If you select a different notification destination when editing a trigger, the body text will reset. |
| Notifications: Notify target | Set the external email target to notify. For more information about using email targets, see [Notifying external email targets](https://support.zendesk.com/hc/en-us/articles/4408883282458). If you select a different notification destination when editing a trigger, the body text will reset. |
| Notifications: Tweet requester | Respond to the X (formerly Twitter) requester with a tweet. An @mention, and shortened ticket URL are added to the message so make sure to stay within the maximum Tweet length. |
| Requester: Language | Set the requester's language to one of your supported languages. |
| Requester: *Custom fields* | Custom user fields are available as actions. |
| Organization: *Custom fields* | Custom organization fields are available as actions. |