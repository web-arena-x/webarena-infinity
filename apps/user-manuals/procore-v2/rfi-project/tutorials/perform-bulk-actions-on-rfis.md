# Perform Bulk Actions on RFIs

Source: https://v2.support.procore.com/product-manuals/rfi-project/tutorials/perform-bulk-actions-on-rfis

---

## Background

Bulk Editing of RFIs allows Project Admins to manage project transitions and perform data cleanup at scale, eliminating the need to edit records one-by-one.

## Things to Consider

- [Required User Permissions](/product-manuals/rfi-project/permissions)
- **Supported Views:**

  - The Bulk Actions menu is supported in the RFIs tool's Items view.

## Steps

1. Navigate to the project's **RFIs** tool.
2. Click the **Items** tab.
3. Locate the RFIs you want to modify in the Items list.

   - To select all of the RFIs in the list, mark the checkbox at the top of the left column **OR** To select one or more of the RFIs in the list, mark the check box to the left of each desired RFI.
4. Click the **edit** icon.
5. Choose from these options to edit the selected RFIs:

   - **Responsible Contractor**. This field is automatically prefilled with the company that is associated with the user selected in the 'Received From' field.

     Responsible Contractor
   - **Received From**. Select the person from whom the RFI question was received from the drop-down list.

     Received From
   - **RFI Manager\***. Select an RFI Manager from the drop-down list. See [What is the RFI Manager role?](/faq-what-is-the-rfi-manager-role)*Notes*:

     - By default, the name of designated RFI Manager appears here. See [Designate the Default RFI Manager for a Project's RFIs](/product-manuals/rfi-project/tutorials/designate-the-default-rfi-manager-for-a-projects-rfis).
     - If you are a user with 'Admin' level permission on the RFIs tool, you may select yourself or another user with 'Admin' level permission from the list.
     - If you are a user with 'Standard' level permission, this list only populates with the names of users who have 'Admin' level permission to the RFIs tool. You may only select another user with 'Admin' level permission from the list.

     RFI Manager
   - **Due Date**. Enter or select a date from the calendar for the RFI response to be due. This field is only visible and available to users with 'Admin' level permissions on the project's RFIs tool.*Note*: The 'Due Date' field is automatically populated based on the default number of days specified on the RFIs tool's Configure Settings page. See [Configure Advanced Settings: RFIs](/product-manuals/rfi-project/tutorials/configure-advanced-settings-rfis). The due date also respects which days are set as 'working days' for the project. See [Set Project Working Days](/product-manuals/admin-project/tutorials/set-project-working-days).

     Due Date
   - **Location**. Select the location pertaining to the RFI from the drop-down list.*Note:* If Procore is configured to allow users to create locations (see [Allow or Disallow Users to Create Locations Within a Tool](/product-manuals/admin-project/tutorials/allow-or-disallow-users-to-create-locations-within-a-tool)), you can click the **Create a New Location** button at the bottom of the list.

     Location
   - **Schedule Impact**. Select one of the following options from the drop-down list.

     - **Yes**. Select this option if you know the number of days by which the schedule will be impacted. Then enter a number in the **Days** box to indicate the total number of calendar days.
     - **Yes (Unknown)**. Select this option if you know the schedule will be impacted, but the number of days is not known.
     - **No**. Select this option if there is no impact to the schedule.
     - **TBD**. Select this option if you have yet to determine if there is a schedule impact.
     - **N/A**. Select this option if an impact to the schedule is not applicable to this RFI.

     Schedule Impact
   - **Cost Impact**. Select one of the following options from the drop-down list.

     - **Yes**. Select this option if you know the amount by which the cost will be impacted. Then enter a number in the **$** box to indicate the cost impact.
     - **Yes (Unknown)**. Select this option if you know the cost will be impacted, but the amount is not know.
     - **No**. Select this option if there is no impact to the cost.
     - **TBD**. Select this option if you have yet to determine if there is a cost impact.
     - **N/A**. Select this option if the cost impact is not applicable to this RFI.

     Cost Impact
   - **Sub Job**. Select a sub job from the drop-down list.

     Sub Job
   - **Private**. Select *Yes* or *No* from the drop-down list. Yes indicates the RFI(s) will be marked Private. No indicates the RFI(s) will NOT be marked Private.

     Private
   - **Add to Distribution List**. Select a person to add to the distribution list.

     Add to Distribution List
   - **Remove from Distribution List**. Select users to remove from the distribution list.

     Remove from Distribution List
   - **Add to Assignees.** Select a new user to add as an assignee. You can click the 'Make Assignee Required' checkbox for assignees within this menu to reinforce response requirements at the point of assignment.

     Add to Assignees
   - **Remove from Assignees.** Select a current user to remove as an assignee.

     Remove from Assignees
6. Click **Apply**.

##### Beta

The ability to bulk edit Assignees and the Distribution List is currently in open beta and can be enabled via Procore Explore. Here are a few considerations:

- When updating Open RFIs, remove the old assignee and add the new one in the **same motion**. This ensures active RFIs never lose their owners during the transition.
- Always perform bulk edits **before** downgrading a userâs permissions or removing them from the project to ensure a smooth transfer of responsibilities.
- **To edit Assignees:** RFIs must be in *Open*, *Closed*, or *Draft* status.
- **To edit Distribution Lists:** RFIs must be in *Open*, *Closed*, *Draft*, or *Closed Draft* status.