# Configure Advanced Settings: Daily Log

Source: https://v2.support.procore.com/product-manuals/daily-log-project/tutorials/configure-advanced-settings-daily-log

---

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the project's Daily Log tool.
- **Additional Information:**

 - Some areas of the Daily Log tool can be customized through the use of [configurable fieldsets](/faq-what-are-configurable-fieldsets-and-which-procore-tools-support-them) that are managed in the Company level Admin tool. See [Which fields in the Daily Log tool can be configured as required, optional, or hidden?](/faq-which-fields-in-the-daily-log-tool-can-be-configured-as-required-optional-or-hidden)
 - With configurable fieldsets, you can mark certain fields in the project's Daily Log tool as required, optional, or hidden.
 - You can also create your own custom fields for the **Manpower** log that can then be added to a fieldset to use on the project.
 - The **Scheduled Work** log pulls live data from the projectâs uploaded schedule and updates automatically.

    - If the schedule changes, even after a day has been marked complete, those updates may be reflected in the log when that day is revisited.
    - This ensures the log stays aligned with the most current version of the schedule.

## Steps

1. Navigate to the project's **Daily Log** tool.
2. Click the **Configure Settings**icon.
3. Click on the tab you want to edit:

   - General
   - Log Types
   - Permissions

### General

The following settings are available to edit:

- **Show Created By On Log Entries**: Toggle the switch to the 'on' position to add a column that displays the name of the person who created each entry.
- **Show âMissing Companiesâ Banner for Manpower and Daily Construction Report**: Toggle the switch to the 'on' position to enable a banner that shows which companies might be missing from the day's log based on the prior day's entries.   
 *Note*: Disabling this setting only removes the banner, it does not remove the Missing Companies feature from the project.
- **Default Distribution**: Use the drop-down menu to add users to the Daily Log's default distribution list.   
 *Notes*:

 - These members will be notified when a daily log is marked as 'Complete' and distributed.
 - Users with the 'Collaborator Entry Only' granular permission are not eligible to be added to the default distribution list.

### Log Types

- Most log types are enabled by default on a new project, however, you can configure which logs you want to use for your project by toggling the switch next to the log type in the list.
- Log types that have further configuration options will have a 'Configure' button next to the log in the list.
- The logs will appear on the Daily Log tool page in the order in which they appear in this list. You can change the order of these logs by dragging them into a new order.

#### Available Log Type Settings

The following settings are available for the different log types:

- **Collaborator Entry (Available for multiple log types).** Click 'Configure' next to a log type and toggle the switch to activate the 'Collaborator Entry' feature.

 - 'Collaborator Entry' allows users with the appropriate granular permissions to create entries for that log.   
    See [Grant Granular Permissions in a Permission Template](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) and [Create Daily Log Entries as a Collaborator](/product-manuals/daily-log-project/tutorials/create-daily-log-entries-as-a-collaborator).   
    *Note*: The granular permission for 'Collaborator Entry' must be enabled on at least one global permission template OR a project permission template before the option enable the feature is available in the Daily Log configuration settings. Collaborator entry is not available for all log types.
- **Delays Log**

 - **Enable or disable delay categories.** Toggle the switch next to a delay category to enable or disable it.
 - **Create new delay categories.** Click '**Create**', type the name of the new category, then press '**Enter**'.
- **Manpower Log**

 - **Default hours**: Enter a number that will be automatically populated in the Manpower Log's Hours field. 
    *Note*: The 'Hours' field is editable, so it is recommended that you add the number of hours that most people will be working on the jobsite for faster daily log entry.
 - **Set Manpower Logs Hours to Zero on Copy:** Mark the checkbox so that the 'Hours' and 'Workers' values on a copied manpower log are set to zero (0). 
    *Note*: If this setting is not enabled, the copied manpower log entry will include the number of hours and workers from the previous entry.
 - **Include Employees in 'Company' Dropdown**: Mark the checkbox if you want to be able to select individual employees to add to Manpower entries. In order for users to be displayed on this list, they must be marked as an employee of your company.   
    See [How do I add someone as an employee of my company?](/product-manuals/directory-company/tutorials/add-someone-as-an-employee-of-your-company)
 - **Manpower categories.** You will be able to filter your results for these categories in the Daily Log Manpower Log Report.

    - To create a new category, click 'Create', then give the category a name and assign it a color.
    - If you want to associate one or more companies with the manpower category, select a the company name from the drop-down list.
    - To delete a category, click the trash can icon.
- **Observed Weather Log**

 - **Hide Weather Data.** Mark the checkbox if you do not want to include weather data from the National Weather Service in the [PDF exports](/product-manuals/daily-log-project/tutorials/export-a-daily-log-as-pdf) for the logs.

### Permissions

##### Tip - Managing User Permissions

By default, user permissions are applied by the permission template assigned to the user during account creation. Permissions for users who have permission templates applied are NOT editable from the Permissions tab.

As a best practice, Procore recommends managing all user permissions with permission templates. See[Create a Project Permission Template](/product-manuals/permissions-company/tutorials/create-a-project-permissions-template).

- General user permission levels (None, Read Only, Standard, or Admin) to the Daily Log tool are visible on the Permissions tab, however, granular permissions are not visible on this screen.
- Permission selections for users whose permissions are assigned through a permission template appear grayed out and ineditable.
- Permissions that are assigned directly to a user (either from the Project level Directory or a tool permission tab, NOT using a permission template) ARE editable. Click the radio button for the desired permission level next to a user's name in the table to edit that user's permissions. You cannot assign granular permissions using this method. Granular permissions can only be assigned by using permission templates.
- For a complete list of tasks associated with each permission level, see the [Daily Log Permissions Matrix](/product-manuals/daily-log-project/permissions).