# Perform Bulk Actions on RFIs - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/perform-bulk-actions-on-rfis

---

## Objective

To use the Bulk Actions menu in the RFIs tool to perform bulk edits on a batch of RFIs.

## Background

Use the Bulk Actions > Edit option when you want to apply the same edits on multiple RFIs.

## Things to Consider

- **Required User Permissions:**
 - 'Admin' level permissions on the project's RFIs tool.
- **Supported Views:**
 - The Bulk Actions menu is supported in the RFIs tool's Items view.

## Steps

1. Navigate to the project's **RFIs** tool.
2. Click the **Items** tab. 
   This reveals a list of all the RFIs on the project. It does NOT include RFIs sent to the Recycle Bin. See [Delete an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/delete-an-rfi "Delete an RFI").
3. Locate the RFIs that you want to modify in the Items list.
   - To select all of the RFIs in the list, mark the checkbox at the top of the left column. 
     OR
   - To select one or more of the RFIs in the list, mark the check box to the left of each desired RFI.
4. Click the **edit** ![icon-edit2.png](https://support.procore.com/@api/deki/files/295064/icon-edit2.png?revision=1) icon. 
   ![rfi-bulk-edit.png](https://support.procore.com/@api/deki/files/535784/rfi-bulk-edit.png?revision=1) 
   This reveals a side panel where you can make your necessary edits.
5. Choose from these options to edit the selected RFIs:
   - **RFI Manager\***. Select an RFI Manager from the drop-down list. See [What is the RFI Manager role?](https://support.procore.com/faq/what-is-the-rfi-manager-role "What is the RFI Manager role?") 
     *Notes*:

     - By default, the name of designated RFI Manager appears here. See [Designate the Default RFI Manager for a Project's RFIs](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/designate-the-default-rfi-manager-for-a-projects-rfis "Designate the Default RFI Manager for a Project's RFIs").
     - If you are a user with 'Admin' level permission on the RFIs tool, you may select yourself or another user with 'Admin' level permission from the list.
   - **Responsible Contractor**. This field is automatically prefilled with the company that is associated with the user selected in the 'Received From' field.
   - **Received From**. Select the person from whom the RFI question was received from the drop-down list.
   - **Location**. Select the location pertaining to the RFI from the drop-down list.  
     *Note:* If Procore is configured to allow users to create locations (see [Allow or Disallow Users to Create Locations Within a Tool](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/allow-or-disallow-users-to-create-locations-within-a-tool "Allow or Disallow Users to Create Locations within a Tool")), you can click the **Create a New Location** button at the bottom of the list.
   - **Private**. Select *Yes* or *No* from the drop-down list. Yes indicates the RFI(s) will be marked Private. No indicates the RFI(s) will NOT be marked Private.
   - **Cost Impact**. Select one of the following options from the drop-down list.

     - ****Yes****. Select this option if you know the amount by which the cost will be impacted. Then enter a number in the ****$**** box to indicate the cost impact.
     - ****Yes (Unknown)****. Select this option if you know the cost will be impacted, but the amount is not know.
     - ****No****. Select this option if there is no impact to the cost.
     - ****TBD****. Select this option if you have yet to determine if there is a cost impact.
     - ****N/A****. Select this option if the cost impact is not applicable to this RFI.
   - **Schedule Impact**. Select one of the following options from the drop-down list.

     - **Yes**. Select this option if you know the number of days by which the schedule will be impacted. Then enter a number in the **Days** box to indicate the total number of calendar days.
     - **Yes (Unknown)**. Select this option if you know the schedule will be impacted, but the number of days is not known.
     - **No**. Select this option if there is no impact to the schedule.
     - **TBD**. Select this option if you have yet to determine if there is a schedule impact.
     - **N/A**. Select this option if an impact to the schedule is not applicable to this RFI.
   - **Due Date**. Enter or select a date from the calendar for the RFI response to be due. This field is only visible and available to users with 'Admin' level permissions on the project's RFIs tool. 
     *Note*: The 'Due Date' field is automatically populated based on the default number of days specified on the RFIs tool's Configure Settings page. See [Configure Advanced Settings: RFIs](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/configure-advanced-settings-rfis "Configure Advanced Settings: RFIs"). The due date also respects which days are set as 'working days' for the project. See [Set Project Working Days](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/set-project-working-days "Set Project Working Days").
6. Click **Apply**.  
   This applies the specified edits to all the selected RFIs. A GREEN banner appears to confirm the total number of RFIs that were successfully edited. A RED banner will appear in the event that the edits were not successfully saved.

## See Also

- [Create an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/create-an-rfi "Create an RFI")
- [Edit an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/edit-an-rfi "Edit an RFI")
- [Delete an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/delete-an-rfi "Delete an RFI")

## 

If you would like to learn more about Procore's RFI software and how it can help your business, please visit our [request for information (RFI) construction software product page ![icon-external-link.png](https://support.procore.com/@api/deki/files/186764/icon-external-link.png?revision=2&size=bestfit&width=14&height=14)](https://www.procore.com/project-management/rfis "https://www.procore.com/project-management/rfis").