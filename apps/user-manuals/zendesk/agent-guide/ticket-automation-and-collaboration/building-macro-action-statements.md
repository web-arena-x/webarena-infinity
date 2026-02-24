# Building macro action statements

Source: https://support.zendesk.com/hc/en-us/articles/4408832783642-Building-macro-action-statements

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

The table below describes the actions available when creating macros for your support
tickets.

Using macros, you can set ticket properties, add or modify tags, and add comments. Select an
action using the drop-down menu, then select or enter specifics in the associated drop-down
menu or text entry box.

Related articles:

- [Using macros to update tickets](https://support.zendesk.com/hc/en-us/articles/4408887656602)
- [Creating macros for tickets](https://support.zendesk.com/hc/en-us/articles/4408844187034)
- [Creating macros from existing tickets](https://support.zendesk.com/hc/en-us/articles/4408886850586)
- [Organizing and managing your macros](https://support.zendesk.com/hc/en-us/articles/4408884166554)

| Actions | Description |
| --- | --- |
| Set subject | You can use this action to replace the ticket's current subject. |
| Status | Note: If you’ve [activated custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306), existing system ticket statuses become status categories. If you have existing actions that use Status, they’re updated to the default ticket status of the corresponding Status category.  The ticket status can be set to the following:  **Open** indicates that the ticket has been assigned to an agent.  **Pending** indicates that the requester has been asked for information and the ticket is therefore on hold until that information has been received.  **On-hold** means that the support request is awaiting a resolution from a third party, someone who is not a member of your support staff and does not have an agent account. This status is optional and must be added (see [Adding the On-hold ticket status to Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408889282458) in the Administrator Guide). **Solved** indicates that the customer's issue has been resolved. Tickets remain solved until they are closed. |
| Status category | Note: If you’ve [activated custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306), system ticket statues and any ticket statuses you create are grouped into status categories. Each status category has a default ticket status. See [Managing ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575941402-Managing-ticket-statuses-#topic_zgh_dbh_vrb).  The status category values are:  The **Open** status category is for grouping ticket statuses that indicate when tickets are ready to be worked on by your support team.  The **Pending** status category is for grouping ticket statuses that are used to indicate that the support team is waiting for the requester to reply. The **On-hold** status category contains ticket statuses used to indicate that the support request is awaiting a resolution from a third party—someone who is not a member of your support staff and does not have an agent account in your Zendesk. This status category is optional and must be added to your Zendesk (see [Adding on-hold ticket status to your Zendesk](https://support.zendesk.com/hc/en-us/articles/4408889282458-Adding-the-On-hold-ticket-status-to-your-Zendesk)). The **Solved** status category contains ticket statuses that indicate that the customer’s issue has been resolved. |
| Ticket status | If you’ve [activated custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306), you can select system ticket statuses and new ticket statuses you created in macros. |
| Form | Your ticket forms are available as actions. Select a specific form. See [Creating ticket forms to support multiple request types](https://support.zendesk.com/hc/en-us/articles/4408846520858). |
| Brand | Add a brand to the ticket. |
| Priority | The priority can be set to **Low**, **Normal**, **High** or **Urgent**. |
| Type | The type can be set to the following:  **Question**  **Incident** indicates that there is more than one occurrence of the same problem. When this occurs, one ticket is set to Problem and the other tickets that are reporting the same problem are set to Incident and linked to the problem ticket.  **Problem** is a support issue that needs to be resolved.  **Task** is used by the Support agents to track various tasks. **Note**: It's currently not possible to link incident tickets to problem tickets or set task due dates using the task action in macros. |
| Group | You can set groups to any of the following:  **(—)** is used to unassign a group (if one has already been assigned)  **(current user’s groups)** is the group to which the agent who is updating the ticket belongs. If the user belongs to multiple groups, the macro makes a series of checks to determine which group should be used. Group priority is determined as follows:  - The group currently assigned to the ticket, if the agent is in that   group. - The agent's default group, if one is available. - The first group the agent belongs to, if no default group is set. **Group name** is the actual name of the group that is assigned to the ticket. |
| Assignee | You can set assignee to any of the following:  **(current user)** is the last person to have updated the ticket, which is not necessarily the same person who is assigned to the ticket. The current user (whoever updated the ticket last) changes whenever the ticket is updated. **Assignee name** is the actual name of the person assigned to the ticket. |
| Set tags | The tags you want to insert into the ticket. The set tag action *replaces* the current tags. Tags must be separated with spaces. Multi-word tags must be joined with an underscore (for example, about\_sales). |
| Add tags | The tags you want to add to the existing list of tags (if any). Tags must be separated with spaces. Multi-word tags must be joined with an underscore (for example, about\_sales). |
| Remove tags | The tags that you want removed from the existing list of tags contained in the ticket (if any). Tags must be separated with spaces. |
| Comment/description | The text of ticket comment, and email notification. |
| Comment mode | Public or Private. Only agents can view private comments. |
| Side conversation | Use this action to start side conversations and ensure that key information is included automatically when conversations are started. See [Using macros to start side conversations](https://support.zendesk.com/hc/en-us/articles/4408829558938). |
| *Custom fields* | Custom fields that set tags (drop-down list, multi-select, and checkbox) are available as actions. You can select the drop-down list values, multi-select options, and Yes or No for checkboxes. |
| Add follower | You can use this action to automatically copy a specific agent to the ticket or the **(current user)**. You can't use this action to copy an end user. This action is **Add CC** if you have not [migrated to new CCs and followers experience](https://support.zendesk.com/hc/en-us/articles/4408839371418). |