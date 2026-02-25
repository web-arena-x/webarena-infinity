# Configure Advanced Settings: Punch List

Source: https://v2.support.procore.com/product-manuals/punch-list-project/tutorials/configure-advanced-settings-punch-list

---

## Background

If you're a Project Administrator, you may find it useful to customize a project's punch list options by using the Punch List's advanced configuration settings.

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permissions on the project's Punch List tool.
- **Additional Information:**

  - Any changes to the Punch List tools settings are project-wide. This means that any changes will affect how the Punch List tool is used by other users in your project.

## Steps

- Punch List Settings

  - [Configure the default Punch Manager Role](#configure-the-punch-listsettings)
  - Grant a Standard User Permissions to Act as Punch Item Manager
  - Configure the default Final Approver Role
  - Configure Emails
  - [Create Punch Item Types](#configure-the-punch-listsettings)
- Punch List Templates
- Permissions Table

## Configure the Punch ListÂ Settings

1. Navigate to the project's **Punch List** tool.
2. Click the **Configure Settings**icon. This reveals the tool's Settings page.
3. From here, you can configure the following settings:

- **Standard** **Permission** **Punch** **Item Manager:** Grant permissions to specific 'Standard' level users to act as a Punch Item Manager.   
  See Grant a Standard User Permissions to Act as a Punch List Manager.
- **Default** **Punch Item Manager:** Select the user you want to designate as the project's default Punch List Manager.   
  See [Configure the Default Punch Item Manager Role.](#configure-the-punch-listsettings)  
  *Note*: Only 'Admin' level users on the Punch List tool can be selected as Punch Manager. However, 'Standard' level users can also be selected if they have specifically been granted permission to act as a Punch Manager. See [Grant a Standard User Permissions to Act as a Punch Item Manager.](#configure-the-punch-listsettings)
- **Default** **Final Approver:** Select the user you want to designate as the project's default Final Approver for punch list items.   
  See [Configure the Default Final Approver Role](#configure-the-punch-listsettings).
- *Note:* Only 'Standard' and 'Admin' level users can be selected from this drop-down menu.
- *Note:* When creating a new punch list item, Procore prioritizes the default Punch Item Managers and the Final Approver in the following order:

  - *When creating an item from a template*, the Punch Item Manager and the Final Approver defined in a Punch List template will take precedence.
  - *If no Punch Item Manager and Final Approver are selected in a Punch List template*, then Procore will default to the Punch Item Manager and Final Approver defined in the Punch List toolâs Configure Settings.
  - *If no Punch Item Manager and Final Approver are selected in the Punch List toolâs Configure Settings and the item was created by an 'Admin' level user on the project's Punch List,* then Procore will default to the item's creator.
  - *If no Punch Item Manager is selected in the Punch List toolâs Configure Settings and the item was created by a 'Standard' level user on the project's Punch List tool*, then the item's creator must manually select a Punch Item Manager from the dropdown list.
- **Default Distribution**: Select people from your directory to be included in your default distribution for all punch list items.
- **Punch List Items Private By Default**: Check this box to make punch list items private by default. Items marked as 'Private' are only visible to the item's creator, assignee(s), punch item manager, final approver, members of the distribution list, and all users with 'Admin' level permissions on the Punch List tool. This box is unselected by default.
- **Punch Item Response Will Be Due**: Enter a number to signify how many days after the item's creation it will be due. The date will automatically populate in the "Due Date" field when creating a punch list item, but you will be able to change the date.  
  *Note:* The due date respects which days are set as 'working days' for the project.   
  See [Set Project Working Days](/product-manuals/admin-project/tutorials/set-project-working-days).

#### Configure the Default Punch Item Manager Role

When you create a new punch list item in Procore, the system will automatically select the designated 'Default Punch Manager' on all new items. The item's Creator (or another user with the appropriate permissions) will have the option to edit the item's assigned Punch Manager.   
See [Create a Punch List Item](/product-manuals/punch-list-project/tutorials/create-a-punch-list-item) and [Edit a Punch List Item](/product-manuals/punch-list-project/tutorials/edit-a-punch-list-item).

Select a default Punch Item Manager for your project.  
*Note:* If no Punch Item Manager is selected, Procore will automatically list the item's Creator as the Punch Manager if the Creator is an 'Admin' level user or a 'Standard' level who has been granted the appropriate permissions to act as Punch Item Manager.

1. Select the user you want to designate as the Punch List Item Manager from the 'Default Punch Item Manager' drop-down menu.
2. Click **Update**.  
   This action automatically sets the default Punch Item Manager for all new created punch list items.

#### Grant a 'Standard' User Permission to act as a Punch Item Manager

Users with 'Standard' level permission on the Punch List tool can also act as a Punch Item Manager if they have been granted permission.

1. Select the 'Standard' level user from the 'Standard permission users who can act as a Punch Item Manager' drop-down menu.
2. Click **Update** to save your changes.  
   *Note*: This action adds the 'Standard' level user's name to the 'Punch Manager' drop-down menu when a punch list item is being created.

#### Configure the Default Final Approver Role

When you create a new punch list item in Procore, the system will automatically select the designated 'Default Final Approver' on all new items. The item's Creator, or another user with the appropriate permissions, can edit the individual item's default Final Approver.   
See [Create a Punch List Item](/product-manuals/punch-list-project/tutorials/create-a-punch-list-item) and [Edit a Punch List Item](/product-manuals/punch-list-project/tutorials/edit-a-punch-list-item).

Select a default Final Approver for your project's punch list items.  
*Note:* If no Final Approver is selected, Procore will automatically list the item's Creator as the Final Approver.

1. Select the user you want to designate as the Final Approver from the **Default** **Final Approver** pick list:
2. Click **Update** to save your changes.

#### Configure Emails

1. Mark the 'Enable overdue emails for assignees' checkbox to send email reminders to assignees for their overdue punch list items.
2. To edit the default email configuration, choose from the following options:

   - *To exclude a role from receiving an email associated with a specific action,* click into the corresponding checkbox to clear the selection.
   - *To include a role in receiving an email associated with a specific action,* click into the corresponding checkbox to mark the selection.  
     *Note*: Dimmed checkboxes indicate that associated roles that cannot receive this notification. Actions marked with a warning icon () indicate that associated notifications cannot be turned off.

#### Create Punch Item Types

Add custom types to help categorize your project's punch list items.

1. Enter a name in the **Type** text box under **Punch** **Types.**
2. Click **+Add.**This action adds the type as a selectable option when you create a new punch list item. These types cannot be created on demand; as a best practice, Procore recommends adding all punch list item types to your project *before* you create a new item.

## Punch List Templates

Procore and/or your Company Administrator has populated your project with default punch list templates. To view and/or manage these templates follow the steps below:

1. Navigate to the project's **Punch List** tool.
2. Click **Configure Settings**icon.  
   This reveals the tool's Settings page.
3. Click the **Punch List Templates** subtab. This reveals the Punch List templates added to your project.  
   *Note:* Company level templates are marked with a key icon.
4. From here, you can configure the following options:

   - **Template Name:** Enter a Name for your template.
   - **Default Trade:** Select a Default Trade that will be associated with your template.
   - **Default Punch Item Manager:** Select a Default Punch Item Manager who will be associated with your template.
   - **Default Assignee:** Select a Default Assignee who will be associated with your template.
   - **Default Final Approver:** Select a Default Final Approver who will be associated with your template.
   - **Active:** Mark the checkbox to set your template to active; team members can only select active templates.
5. To create a new template category:

   1. Click **Create Category** in the right panel.
   2. Enter a name for the category in the Name field.
   3. Click **Create**. The new category is added to the end of the list.

For more information on Punch List Templates, see the related articles in the See Also section below:

## Permissions Table

1. Click **Permissions Table** in the right sidebar.
2. Set each user's permission for the Punch List tool according to your preferences.

   - Access
   - No Access
3. For a list of what users can do at each permission level in the Punch List, see [Punch List Permission Matrix](/product-manuals/punch-list-project/permissions).
4. In the example screenshot below, the user has 'Standard' level permissions.