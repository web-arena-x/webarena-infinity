# Configure Advanced Settings: Specifications

Source: https://v2.support.procore.com/product-manuals/specifications-project/tutorials/configure-advanced-settings-specifications

---

## Background

You can configure your Specification tool settings, such as configuring your number ordering scheme, adding users to receive updates for Specification updates, or managing the names of your specification divisions and sets.

### Things to Consider

- [Required User Permissions](/product-manuals/specifications-project/permissions)
- 'Admin' on the project's Specifications tool.
- For a person to be added as a subscriber, they must be added to the project's Directory and be granted 'Read Only' permissions to the Specifications tool.
- The blue caret in the corner of a cell indicates that you can edit the value in line.

## Steps

1. Navigate to the project's **Specifications** tool.
2. Click the **Configure Settings**  icon.
3. Under Specifications Settings, click one of the following to configure or update your settings:

   1. General
   2. Divisions
   3. Sets
   4. Permissions

#### GENERAL

1. Navigate to the Specifications Settings page, click **General,** and configure the following settings:

       
   - **Revision Number Ordering Scheme**: Select your numbering or lettering scheme.  
     *Note:* If your revision ordering system uses a numbers-only or letters-only scheme, the setting you select here will have no impact.

     - **Letters first, then numbers** (Default). List revisions in order; first by letter and then by number (e.g., a, b, c, 1, 2, 3) where 'a' is the oldest revision and '3' is the current revision.
     - **Numbers first, then letters**. Lists revisions in order; first by number and then by letter (e.g., 1, 2, 3, a, b, c) where '1' is the oldest revision, and 'c' is the current revision.
   - **Enable Specifications by Area**: Select the Specifications by Area feature.

     - Click **Yes** to enable
     - Click **No** to disable  
       *Note:* You can't disable specifications by area if more than one area exists. Once this feature is disabled, you can directly navigate to the tool's landing page.  
       See the following articles for more information:

       - [What are Specifications Areas?](https://v2.support.procore.com/faq-what-are-specification-areas/)
       - [Enable or Disable Specification Areas](enable-or-disable-specification-areas.md)
       - [Add a Specification Area](add-a-specification-area.md)
   - **Specifications Subscribers**: Add subscribers to the tool's distribution list.

     - Navigate to **Communications.**
     - Click 'Select Subscribers' drop-down to add subscribers to the tool's distribution list.  
       *Note:* Procore will send an email notification to these users whenever a new revision or set is uploaded or added to the Specifications tool. See [Manually Create Specification Sections](/products/online/user-guide/project-level/specifications/tutorials/manually-create-spec-sections)
     - Click **+Add Recipients** and select any 'Distribution Groups' or 'Users' from the drop-down list.'
     - Click **Add.**
2. Click **Save.***Note:* If you try to switch tabs in the settings menu without saving your changes, a confirmation window will appear, with the option to either save your changes or leave without saving.

#### DIVISIONS

1. Navigate to the Specifications Settings page, click **Divisions,** and configure the following settings:

   - **Edit Divisions**: Edit an existing field.

     - Click **Edit Field** button.
     - Edit the existing 'Code' or 'Description' columns as required in the fields present.
   - **Add Divisions**: Add a new field.

     - Click **Edit Field** button.
     - Click **+Add Division** to add a new row to the division table.  
       *Note:* Both the code and description fields are required.
   - **Delete Divisions**: Delete an existing field.

     - Click **Edit Field** button.
     - Click  to delete a field.   
       *Note:* You cannot delete a set if it consists of specification revisions, sections, or uploads.
2. Click **Save.**

   *Note:* If you try to switch tabs in the settings menu without saving your changes, a confirmation window will appear, with the option to either save your changes or leave without saving.

#### SETS

1. Specifications Settings page, click **Sets,** and configure the following settings:

   - **Edit Sets**: Edit an existing field.

     - Click **Edit Field** button.
     - Edit the existing 'Name' or 'Date' columns as required in the fields present.
   - **Edit Set Date**: Edit the date of an existing set.

     - Click the date row for an existing set.
     - Select the date using the calendar.
   - **Add Sets**: Add a new field.

     - Click **Edit Field** button.
     - Click **+Add Set** to add a new row to the sets table.  
       *Note:* Both the code and description fields are required.
   - **Delete Sets**: Delete an existing field.

     - Click **Edit Field** button.
     - Click  to delete a field.   
       *Note:* You cannot delete a set if it consists of specification revisions, sections, or uploads.
2. Click **Save.**  
   *Note:* If you try to switch tabs in the settings menu without saving your changes, a confirmation window will appear, with the option to either save your changes or leave without saving.

#### PERMISSIONS

1. Navigate to the Specifications Settings page, click **Permissions,** and configure the following settings:

   - To change a user's permission level for the Specifications tool, click the circleicon in the respective row.
   - Once the permission is updated, it will be marked as icon.  
     *Note:* If a row is gray and unclickable, it means that the user has already been assigned the permission, and it is set by a permissions template that cannot be changed. See

     [Specification Permissions](/products/online/user-guide/project-level/specifications/permissions).