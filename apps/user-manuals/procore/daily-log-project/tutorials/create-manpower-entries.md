# Create Manpower Entries

Source: https://v2.support.procore.com/product-manuals/daily-log-project/tutorials/create-manpower-entries

---

## Background

The **Manpower** section lets you track people on site who performed work on the project that day. It allows for the collection of data, including companies on site, number of workers, hours worked, cost codes associated with the work.

You can configure the **Manpower** section so that the values of *Hours* and *workers* on a copied manpower entry are automatically set to zero. See [Configure Daily Log Advanced Settings](/product-manuals/daily-log-project/tutorials/configure-advanced-settings-daily-log).   
*Note*: If the *Set Hours and Workers values to 0 on copy* setting is not enabled in the **Daily Log Settings** > **Manpower** screen, the copied manpower entry will retain the number of hours and workers from the previous entry.

## Things to Consider

- **Required User Permissions:**

 - *To create entries:* 'Standard' or 'Admin' level permissions on the project's **Daily Log** tool.
 - *To create pending entries as a collaborator*: 'Read Only' or 'Standard' permissions to the project's **Daily Log** tool with the ['Collaborator Entry Only' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permissions template.
- **Additional Information:**

 - Certain fields in the **Manpower** section can be configured as required, optional, or hidden in the company level **Admin** tool. See [Which fields in the Daily Log tool can be configured as required, optional, or hidden?](/faq-which-fields-in-the-daily-log-tool-can-be-configured-as-required-optional-or-hidden)
 - If you want to select individual contacts from the **Company** dropdown menu in the **Manpower** section, enable the *Include Employees in 'Company' Dropdown* setting on the Daily Log tool's **Settings** page. See [Configure Advanced Settings: Daily Log](/product-manuals/daily-log-project/tutorials/configure-advanced-settings-daily-log).
 - Entries made by collaborators are marked as 'pending' until approved by an administrator.

## Steps

1. Navigate to the project's **Daily Log** tool.
2. Scroll to the Manpower section.
3. Fill out the following fields as appropriate: 
   ***Tip!*** Certain fields in the Manpower log can be configured as required, optional, or hidden in the Company level Admin tool.

   - **#**: This uneditable field counts the number of entries in a section (e.g. the first entry created will be # 1, and the second entry will be # 2).

     No.
   - **Company**: Select the company or individual performing the work from the drop-down menu.*Note*: Companies and users must exist in the project's Directory tool to be selected in this drop-down menu. See [Add a Company to the Project Directory](/process-guides/set-up-a-project-directory/create-companies). In addition, a user must be marked as an employee of your company to appear in the list. See [How do I add someone as an employee of my company?](/product-manuals/directory-company/tutorials/add-someone-as-an-employee-of-your-company)

     Contact / Company
   - **Workers**: Enter the number of workers from the selected company on the job for the day.

     #Workers
   - **Hours**: Enter the total number of hours *each* worker within the selected company performed on the job that day. If workers from the same company worked different hours, Procore recommends creating a separate entry.

     #Hours
   - **Total Hours**: This field will display the product of #Workers and #Hours.E.g. 3 (#Workers) x 7 (#Hours) = 21 (Man Hours).

     Total Hours
   - **Cost Code**: Select from the drop-down menu the cost code associated with the entry.

     Cost Code *Note:* This field is not enabled by default, so it may not be available on your entry. Company Admins can add the field through a [configurable fieldset](/product-manuals/admin-company/tutorials/create-new-configurable-fieldsets) applied to the project.
   - **Location**: Select a location from the Location drop-down menu.*Note*: If the project allows for locations to be created from other tools, you can also create a new location to select. See [How do I add a multi-tiered location to an item?](/product-manuals/admin-project/tutorials/add-a-multi-tiered-location-to-an-item)

     Location
   - **Trade**: Select the trade associated with the entry from the drop-down menu. You can only select from the trades already added to the project. See [Add a Custom Trade](/product-manuals/admin-company/tutorials/add-a-custom-trade).

     Trade *Note:* This field is not enabled by default, so it may not be available on your entry. Company Admins can add the field through a [configurable fieldset](/product-manuals/admin-company/tutorials/create-new-configurable-fieldsets) applied to the project.
   - **Comments**: Enter any comments that may help clarify the entry.

     Notes
   - **Attachments**: Attach any additional files to the entry.   
     Click **Attach File(s)** and then drag-and-drop a file from your computer to the **Drag and Drop your File(s)** area, OR click **Upload Files** to select a file from your computer.
     Once you save your item, users will be able to view the attachment in Procore's viewer or download the attachment.

     Attachments
4. Click **Create**.

## Next Step

- [Mark a Daily Log as Complete](/product-manuals/daily-log-project/tutorials/mark-a-daily-log-as-complete)