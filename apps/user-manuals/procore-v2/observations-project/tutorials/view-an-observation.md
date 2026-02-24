# View an Observation

Source: https://v2.support.procore.com/product-manuals/observations-project/tutorials/view-an-observation

---

## Things to Consider

- [Required User Permissions](/product-manuals/observations-project/permissions)
- **Additional Information:**

  - A 'Private' observation is visible to the following users:\* The observation's creator, Assignee, and Distribution List members

    - Users with 'Admin' level permissions on the project's Observations tool
    - Users with 'Read Only' or 'Standard' level permissions on the project's Observations tool with the ['View Private Observations Assigned to Users within Same Company' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on their permissions template (if another user in their company [including them] is designated as the observation's Assignee).

## Steps

1. Navigate to the project's **Observations** tool.
2. Click **View** next to the observation you want to view.  
    This reveals the Observation's General Information and Activity sections.

### View an Observation's Details

The Observation's **General Information** displays the following details:

- **Origin**: If the observation was created from an inspection or from an action linked to an incident, a link to the inspection or incident will be automatically added to this field.
- **Type**: This field displays the observation's type, which is a category that helps you filter and report on observations. It will not have any effect on which fields will appear when creating an observation. See [What are the default Observation types used for?](/faq-what-are-the-default-observation-types-used-for)
- **Title**: This field displays the observation's title, and its general topic.
- **Trade**: This field displays the observation's associated trade. See [Add or Delete Trades](/product-manuals/admin-company/tutorials/add-a-custom-trade).
- **No**: This field displays the observation's number. When an observation is created, this field automatically populates with the next available number; you can edit this number as needed.
- **Location**: This field displays the observation's location. See How do I add a multi-tiered location to an item?
- **Assignee**: This field displays the user responsible for resolving the observation.
- **Due Date:** This field displays the observation's due date.  
  *Note:* The item's Assignee must have 'Standard' or 'Admin' permissions on the Observations tool.
- **Date Notified:** This field displays the date that responsible parties were notified of the observation.
- **Created By:** This field displays the observation's creator.
- **Date Created:** This field displays the date the observation was created.
- **Contributing Condition**: This field displays the Contributing Condition associated with the item.
- **Hazard**: This field displays the Hazard associated with the item.
- **Status**: This field displays the observation's status, which can include any one of the following:

  - **Initiated**: This status indicates that the observation has been created and is awaiting the Assignee's action or response.
  - **Ready for Review**: This status indicates that action on the observation has been performed and the work is awaiting review from the creator.
  - **Not Accepted**: This status indicates that the observation's creator has reviewed and rejected the work. When the observation's creator marks it as 'Not Accepted,' the item becomes the Assignee's responsibility.
  - **Closed**: This status indicates that the observation's creator has reviewed and accepted the work.
- **Priority**: This field displays the observation's priority.  
  *Note:* The observation's priority will not affect how or where the observation displays.
- **Spec Section:** This field displays the Specification (Spec) Section associated with the observation.
- **Distribution**: This field displays the people on the distribution list receive emails when the observation's status changes or when someone leaves a comment.  
  *Note:* You can add default users to an Observation's Distribution list in the tool's settings. See [Configure Advances Settings: Observations](/product-manuals/observations-project/tutorials/configure-advanced-settings-observations)
- **Private**: If this checkbox is marked, the observation will only be viewable by the item's creator, Assignee, users on the item's Distribution list, and 'Admin' level users on the **Observations** tool.
- **Contributing Behavior**: This field displays Contributing Behaviors associated with the item.
- **Description**: This section displays relevant information needed to report on or complete the work.
- **Attachments**: This section includes any relevant files or photos; click the attachment link to download the information.

### Activity Feed

Under **Activity Feed**, you can view the recent activity, comments, and status changes associated with the observation. Within this section, you can add comments and attachments to the observation and change its status. See [Add a Comment to an Observation](/product-manuals/observations-project/tutorials/add-a-comment-to-an-observation) and [Respond to an Observation](/product-manuals/observations-project/tutorials/respond-to-an-observation).

### Related Items

1. Click the **Related Items** sub tab.  
    This reveals a list of all related items added by the **Observations** tool 'Admin' user. See [Add a Related Item to an Observation](/product-manuals/observations-project/tutorials/add-a-related-item-to-an-observation).
2. Click the links next to the item's description to view a related item.

### Emails

1. Click the **Emails** sub tab.  
    This reveals a log of all the emails sent using the **Email** button. You will only view emails that you have permissions to access. See [Email Observations](/product-manuals/observations-project/tutorials/email-observations).

### Change History

1. Click the **Change History** sub tab.  
    This reveals a log detailing when the item was modified, what fields were modified, and who modified the item.