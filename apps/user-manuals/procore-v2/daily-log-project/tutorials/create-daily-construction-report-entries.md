# Create Daily Construction Report Entries

Source: https://v2.support.procore.com/product-manuals/daily-log-project/tutorials/create-daily-construction-report-entries

---

## Background

The **Daily Construction Report** section allows you to track the total number of workers and hours worked for each vendor, company, and trade on a project. You can configure additional categories for workforce labor using the company-level Admin tool for use on projects. See [How do I enable additional workforce labor types for the Daily Log?](/product-manuals/admin-company/tutorials/enable-additional-workforce-labor-types-for-the-daily-log)

## Things to Consider

- **Required User Permissions:**

 - *To create entries:* 'Standard' or 'Admin' level permissions on the project's **Daily Log** tool.
 - *To create pending entries as a collaborator:* 'Read Only' or 'Standard' permissions to the Daily Log tool with the ['Collaborator Entry Only' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permission template.   
    See [Create Daily Log Entries as a Collaborator](/product-manuals/daily-log-project/tutorials/create-daily-log-entries-as-a-collaborator).
- **Additional Information:**

 - Entries made by collaborators are marked as 'pending' until approved by an administrator.
 - There are additional workforce labor categories that can be added to the **Daily Construction Report** in the Daily Log tool. For example, Women, Veteran, Minority, First-Year Apprentice, Local (City), and Local (County). In order to track hours for these additional workforce labor types, these fields must first be configured in the Daily Log section of the company level **Admin** tool, and then applied to one or more projects. See [How do I enable additional workforce labor types for the Daily Log?](/product-manuals/admin-company/tutorials/enable-additional-workforce-labor-types-for-the-daily-log) *Note*: Once configured and applied, the *Workforce Hours* column with an *Add Hours* link is visible in the **Daily Construction Report** section.

## Steps

1. Navigate to the project's **Daily Log** tool.
2. Scroll to the Daily Construction Report section.
3. Fill out the following fields as appropriate:

   - **#**: This uneditable field counts the number of entries in a section (e.g. the first entry created will be # 1, and the second entry will be # 2).

     No.
   - **Company**: Select the company name from the drop-down menu.   
     Companies must be added to the Directory tool to be selected in this drop-down menu.   
     See [Add a Company to the Project Directory](/process-guides/set-up-a-project-directory/create-companies).

     Company
   - **Trade**: Select the trade associated with the entry from the drop-down menu. You can only select from the trades already added to the project. See [Add a Custom Trade](/product-manuals/admin-company/tutorials/add-a-custom-trade).

     Trade
   - **Foreman**: Enter the total number of foremen on-site that day followed by the total number of hours worked.

     Foreman
   - **Journeyman**: Enter the total number of journeymen on-site that day followed by the total number of hours worked.

     Journeyman
   - **Apprentice**: Enter the total number of apprentices on-site that day followed by the total number of hours worked.

     Apprentice
   - **Others**: Enter the number of any other workers and the total number of hours worked.

     Others
   - **Comments**: Enter any comments that may help clarify the entry.

     Notes
   - **Attachments**: Attach any additional files to the entry.   
     Click **Attach File(s)** and then drag-and-drop a file from your computer to the **Drag and Drop your File(s)** area, OR click **Upload Files** to select a file from your computer.
     Once you save your item, users will be able to view the attachment in Procore's viewer or download the attachment.

     Attachments

     ##### Â Tip

     Certain fields in the Daily Construction Report log can be configured as required, optional, or hidden in the company level **Admin** tool.

- *Optional:* If additional 'Workforce Hours' fields have been configured in the Company level Admin tool, you will see an 'Add Hours' link.

 1. Click the **Add Hours** link.
 2. Enter the hours for each category you want to track hours for.
 3. Click **Add Hours** to confirm.
- Click **Create**.