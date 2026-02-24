# View an Observation (iOS)

Source: https://v2.support.procore.com/product-manuals/observations-ios/tutorials/view-an-observation-ios

---

## Things to Consider

- [Required User Permissions](/product-manuals/observations-project/permissions)
- **Additional Information:**

  - Related Items, Emails, and Change History are only available to view on the desktop app. See [View and Observation](/product-manuals/observations-project/tutorials/view-an-observation).
  - A 'Private' observation is visible to the following users:

    - The observation's creator, Assignee, and Distribution List members
    - Users with 'Admin' level permissions on the project's Observations tool
    - Users with 'Read Only' or 'Standard' level permissions on the project's Observations tool with the ['View Private Observations Assigned to Users within Same Company' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on their permissions template (if another user in their company [including them] is designated as the observation's Assignee or Distribution List member)

## Prerequisites

- [Create an Observation](/product-manuals/observations-project/tutorials/create-an-observation)  
   OR
- [Create an Observation (iOS)](/product-manuals/observations-ios/tutorials/create-an-observation-ios)  
   OR
- [Create an Observation (Android)](/product-manuals/observations-android/tutorials/create-an-observation-android)

## Steps

1. Navigate to the **Observations** tool on an iOS mobile device.
2. Tap the **Observations** tool.
3. Tap the observation you want to view.
4. View the observation summary:

   - **#**: This field displays the observation's number. When an observation is created, this field automatically populates with the next available number.
   - **Title**: This field displays the observation's title, and its general topic.
   - **Due Date:** This field displays the observation's due date.
   - **Assignee**: This field displays the user responsible for resolving the observation.  
     *Note:* The item's Assignee must have 'Standard' or 'Admin' permissions on the Observations tool.
   - **Status**: This field displays the observation's status, which can include any one of the following:

     - **Initiated**: This status indicates that the observation has been created and is awaiting the Assignee's action or response.
     - **Ready for Review**: This status indicates that action on the observation has been performed and the work is awaiting review from the creator.
     - **Not Accepted**: This status indicates that the observation's creator has reviewed and rejected the work. When the observation's creator marks it as 'Not Accepted,' the item becomes the Assignee's responsibility.
     - **Closed**: This status indicates that the observation's creator has reviewed and accepted the work.
   - Tap **Show** in the 'Information' section to see the additional observation details:

     - **Created By:** This field displays the observation's creator.
     - **Origin**: If the observation was created from an inspection or from an action linked to an incident, a link to the inspection or incident will be automatically added to this field.
     - **Distribution**: This field displays the people on the distribution list receive emails when the observation's status changes or when someone leaves a comment.  
       *Note:* You can add default users to an Observation's Distribution list in the tool's settings. See [Configure Advances Settings: Observations](/product-manuals/observations-project/tutorials/configure-advanced-settings-observations)
     - **Spec Section:** This field displays the Specification (Spec) Section associated with the observation.
     - **Type**: This field displays the observation's type, which is a category that helps you filter and report on observations. It will not have any effect on which fields will appear when creating an observation. See [What are the default Observation types used for?](/faq-what-are-the-default-observation-types-used-for)
     - **Location**: This field displays the observation's location. See How do I add a multi-tiered location to an item?
     - **Priority**: This field displays the observation's priority.  
       *Note:* The observation's priority will not affect how or where the observation displays.
     - **Trade**: This field displays the observation's associated trade. See [Add or Delete Trades](/product-manuals/admin-company/tutorials/add-a-custom-trade).
     - **Hazard**: This field displays the Hazard associated with the item.
     - **Contributing Condition**: This field displays the Contributing Condition associated with the item.
     - **Contributing Behavior**: This field displays Contributing Behaviors associated with the item.
     - **Private**: If the observation is private, it will only be viewable by the item's creator, Assignee, users on the item's Distribution list, and 'Admin' level users on theObservations tool.
     - **Description**: This section displays relevant information needed to report on or complete the work.
   - **Attachments**: This section includes any relevant files or photos; click the attachment link to download the information.
   - **Linked Drawings**: This section includes any drawings that are linked to the observation. See [Link Observations to a Drawing (iOS)](/product-manuals/drawings-ios/tutorials/link-observations-to-a-drawing-ios)
   - **Activity**: This section includes the recent activity, comments, and status changes associated with the observation. Within this section, you can add comments to the observation and change its status. See [Add a Comment to an Observation](/product-manuals/observations-project/tutorials/add-a-comment-to-an-observation) and [Respond to an Observation](/product-manuals/observations-project/tutorials/respond-to-an-observation).