# Create an Observation

Source: https://v2.support.procore.com/product-manuals/observations-project/tutorials/create-an-observation

---

## Things to Consider

- **Required User Permissions:**

  - 'Standard' or 'Admin' level permissions on the Observations tool.  
    *Note:* 'Standard' level users can only assign observations to 'Admin' level users unless the ['Can Assign Standard Users to Observations' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) is enabled on their permission templates.
- **Additional Information:**

  - You can also create a Observations from Inspections, Incidents, Coordination Issues, and Models.
  - When you create an observation, you will get email notifications any time another user [comments](/product-manuals/observations-project/tutorials/add-a-comment-to-an-observation) or [changes the status of the observation](/product-manuals/observations-project/tutorials/respond-to-an-observation).
  - Observation notifications are NOT automatically distributed after they are created. Users will need to send the notification after creating it.   
    *Note:* Notifications can be distributed via web or Procore mobile.
  - Overdue notifications are only emailed when an observation is in the 'Initiated' or 'Not Accepted' status. Overdue emails are NOT sent when an observation is in the 'Ready for Review' or 'Closed' status.
  - If you create an observation without an assignee, no notification will be sent. If you edit the observation and add an assignee and save, an email notification will be sent automatically.

## Steps

1. Navigate to the Project level **Observations** tool.
2. Click **+Create Observation.**
3. Enter the following information:â

   - **Type**: Choose the type that best categorizes the observation. The type will help you filter and report based on the type of observation. It will not have any effect on which fields will appear when creating an observation. See [What are the default Observation types used for?](/faq-what-are-the-default-observation-types-used-for) (*Note*: Users with the appropriate permissions can customize the selections that appear in this list. See [Add Company Level Observation Types](/product-manuals/admin-company/tutorials/add-company-level-observation-types) and [Add Project Level Observation Types](/product-manuals/observations-project/tutorials/add-project-level-observation-types).)
   - **No**: The number of observations will automatically populate with the next number based on the number of observations you and your team have created. You may edit this as needed. This number can be a duplicate of one already assigned to another observation item in your project.
   - **Title**: Title the observation to announce the general topic.
   - â**Status**: Set the status of the observation from the following options:

     - **Initiated**: When you create the observation, it will be set to "initiated." This means that the observation has been established in Procore and is awaiting the assignee to respond.
     - **Ready for Review**: Once the assignee has acted upon the observation (whether by fixing the deficiency, by addressing the safety issue, etc.), they will respond to the observation by changing the status to "Ready for Review." This notifies the creator via email that the observation is ready for the creator to review.
     - **Not Accepted**: Once the creator has reviewed the work, they might mark it as "Not Accepted." This means that the creator has deemed the work as not resolved. The observation is put back into the assignee's court.
     - **Closed**: Once the creator has reviewed the work, they might mark it as "Closed." This means that the creator has deemed the work as resolved and approved, and has closed out the item.
   - **Priority**: Select a priority for the observation from the following options:  
     *Note:* This will not change how or where the observation will display. It will, however, tell the responsible party how urgent the item is.

     - Low
     - Medium
     - High
     - Urgent
   - **Trade**: Select the relevant trade for this observation. It signifies which trade is involved in resolving the observation. Trades are set at the company level admin tab under trade configuration. See [Add or Delete Trades](/product-manuals/admin-company/tutorials/add-a-custom-trade).
   - **Assignee**: Select the user who will complete the work required from the observation.   
     *Notes*:

     - The 'Assignee' must have 'Standard' or 'Admin' permissions on the Observations tool.
     - 'Standard' users can assign observations to an 'Admin' user, or another 'Standard' level user if they have been granted the '[Can Assign Standard Users to Observations](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template)' granular permission.
   - **Due Date**: Enter or select a date from the calendar for the observation to be due.  
     *Note*: The 'Due Date' field is automatically populated based on the default number of days specified on the Observations tool's Configure Settings page. See [Configure Advanced Settings: Observations](/product-manuals/observations-project/tutorials/configure-advanced-settings-observations). The due date also respects which days are set as 'working days' for the project. See [Set Project Working Days](/product-manuals/admin-project/tutorials/set-project-working-days).
   - **Spec Section**: Select the specification section associated with the observation.
   - **Location**: Select the location the observation is found in. [How do I add a multi-tiered location to an item?](/product-manuals/admin-project/tutorials/add-a-multi-tiered-location-to-an-item)
   - **Distribution**: Add people to the distribution list who you would like to receive update emails when the observation's status changes or when someone leaves a comment.  
     *Note*: If there are people who you would like to always be on the distribution list for observations, you can add them to the default distribution list in the configuration settings.
   - **Private**: Mark the checkbox if you would like this observation to be viewable by Observation Admin users, the assignee, and the people on the distribution list.
   - **Contributing Condition**: Select a contributing condition associated with the observation. See [Add Root Cause Analysis Fields](/product-manuals/admin-company/tutorials/add-root-cause-analysis-fields).
   - **Contributing Behavior**: Select a contributing behavior associated with the observation.
   - **Hazard**: Select a hazard associated with the observation.
   - **Description**: Add a description for the observation detailing relevant information needed to report on or complete the work.
   - **Attachments**: Attach relevant information like a photo or a warranty document by clicking **Attach File(s)** to select a file from Procore or your local computer, or by dragging and dropping into the gray box.  
     *Note*: See [Add a Photo to an Observation so that it Populates in the Photos Tool](/product-manuals/observations-project/tutorials/add-a-photo-to-an-observation-so-that-it-populates-in-the-photos-tool).
4. Click **Create**.
5. When you return to the main Observations page, click **Send Item** in the banner above the Observations log page to send a digest email to the assignees, members of the distribution list, and creators of all of the observations that have yet to be sent. The Observation's 'Date Notified' will be set to the date the **Send Item** button was clicked.  
   *Note*: In order to see this banner, the observation must have an assignee.