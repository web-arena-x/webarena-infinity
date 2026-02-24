# Create Manpower Entries - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/daily-log/tutorials/create-manpower-entries

---

## Objective

To create Manpower entries in the project's Daily Log tool.

## Background

The Manpower section tracks the people on site who have completed work on the project for that day. You are able to collect information on the companies on site, the number of workers, the number of hours they worked, and the cost code associated with their work.  
  
You can configure your Manpower section so that the 'Hours' and 'Workers' values on a copied manpower entry are set to zero (0). See [Configure Advanced Settings: Daily Log](https://support.procore.com/products/online/user-guide/project-level/daily-log/tutorials/configure-advanced-settings-daily-log "Configure Advanced Settings: Daily Log").  
*Note*: If this setting is not enabled, the copied manpower entry will include the number of hours and workers from the previous entry.

## Things to Consider

- **Required User Permissions:**
  - *To create entries:*
    - 'Standard' or 'Admin' level permissions on the project's Daily Log tool.
  - **To create pending entries as a collaborator**:
    - 'Read Only' or 'Standard' permissions to the Daily Log tool with the ['Collaborator Entry Only' granular permission](../../../company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#Daily_Log "Grant Granular Permissions in a Permission Template") enabled on your permissions template. See [Create Daily Log Entries as a Collaborator](https://support.procore.com/products/online/user-guide/project-level/daily-log/tutorials/create-daily-log-entries-as-a-collaborator "Create Daily Log Entries as a Collaborator").
- **Additional Information:**
  - Certain fields in the Daily Log's Manpower section can be configured as required, optional, or hidden in the Company level Admin tool. See [Which fields in the Daily Log tool can be configured as required, optional, or hidden?](https://support.procore.com/faq/which-fields-in-the-daily-log-tool-can-be-configured-as-required-optional-or-hidden "Which fields in the Daily Log tool can be configured as required, optional, or hidden?")
  - If you want to allow individual contacts to be selected in the Company field, you will need to enable the *Include Employees in 'Company' Dropdown*setting in the Daily Log tool's configure settings. See [Configure Advanced Settings: Daily Log](https://support.procore.com/products/online/user-guide/project-level/daily-log/tutorials/configure-advanced-settings-daily-log "Configure Advanced Settings: Daily Log").
  - Entries made by collaborators are marked as 'pending' until approved by an administrator.

## Steps

1. Navigate to the project's **Daily Log** tool.
2. Scroll to the Manpower section.
3. Fill out the following fields as appropriate:  
   ***Tip!***Certain fields in the Manpower log can be configured as required, optional, or hidden in the Company level Admin tool. See [Create New Configurable Fieldsets](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/create-new-configurable-fieldsets "Create New Configurable Fieldsets").
   - **#**: This uneditable field counts the number of entries in a section (e.g. the first entry created will be # 1, and the second entry will be # 2).
   - **Company**: Select the company or individual performing the work from the drop-down menu.   
     *Note*: Companies and users must exist in the project's Directory tool to be selected in this drop-down menu. See [Add a Company to the Project Directory](https://support.procore.com/products/online/user-guide/project-level/directory/tutorials/add-a-company-to-the-project-directory "products/online/user-guide/project-level/directory/tutorials/add-a-company-to-the-project-directory"). In addition, a user must be marked as an employee of your company to appear in the list. See [How do I add someone as an employee of my company?](https://support.procore.com/products/online/user-guide/company-level/directory/tutorials/add-someone-as-an-employee-of-your-company "How do I add someone as an employee of my company?")
   - **Workers**: Enter the number of workers from the selected company on the job for the day.
   - **Hours**: Enter the total number of hours *each* worker within the selected company performed on the job that day. If workers from the same company worked different hours, Procore recommends creating a separate entry.
   - **Total Hours**: This field will display the product of #Workers and #Hours.  
     E.g. 3 (#Workers) x 7 (#Hours) = 21 (Man Hours).
   - **Cost Code**: Select from the drop-down menu the cost code associated with the entry.

     *Note:* This field is not enabled by default, so it may not be available on your entry. Company Admins can add the field through a [configurable fieldset](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/create-new-configurable-fieldsets "Create New Configurable Fieldsets") applied to the project.
   - **Location**: Select a location from the Location drop-down menu.  
     *Note*: If the project allows for locations to be created from other tools, you can also create a new location to select. See [How do I add a multi-tiered location to an item?](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/add-a-multi-tiered-location-to-an-item "How do I add a multi-tiered location to an item?")
   - **Trade**: Select the trade associated with the entry from the drop-down menu. You can only select from the trades already added to the project. See [Add a Custom Trade](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/add-a-custom-trade "Add a Custom Trade").

     *Note:* This field is not enabled by default, so it may not be available on your entry. Company Admins can add the field through a [configurable fieldset](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/create-new-configurable-fieldsets "Create New Configurable Fieldsets") applied to the project.
   - **Comments**: Enter any comments that may help clarify the entry.
   - **Attachments**: Attach any additional files to the entry. Click **Attach File(s)** and then drag-and-drop a file from your computer to the **Drag and Drop your File(s)** area, or click **Upload Files** to select a file from your computer. Once you save your item, users will be able to view the attachment in Procore's viewer or download the attachment.
4. Click **Create**.

## Next Step

- [Mark a Daily Log as Complete](https://support.procore.com/products/online/user-guide/project-level/daily-log/tutorials/mark-a-daily-log-as-complete "Mark a Daily Log as Complete")

##