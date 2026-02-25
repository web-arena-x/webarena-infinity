# Configure Advanced Settings: Instructions

Source: https://v2.support.procore.com/product-manuals/instructions-project/tutorials/configure-advanced-settings-instructions

---

## Things to Consider

- **Required User Permissions:**

 - 'Admin' permission on the project's Instructions tool.
- **Additional Information:**

 - The Instructions tool has been developed specifically for Procore clients in Australia, New Zealand, and Canada.

## Steps

1. Navigate to the project's Instructions tool.
2. Click **Configure Settings** .
3. Configure the advanced settings as follows:

   - Instructions **Private by Default**: This setting is disabled by default (i.e. instructions are not private by default).

     - Mark the checkbox if you want all new instructions created to be marked 'Private' by default.
   - **Number Instructions by Type**: This setting is enabled by default. When this setting is enabled, users cannot edit instruction numbers. Duplicate numbers are not permitted.

     - Unmark the checkbox if you want to allow instruction numbers to be edited. 
       *Note*: Changing the setting later will affect instruction number sequencing.
   - **Default Distribution**: Users and groups added to the Default Distribution list will be included on all correspondence for new instructions.

     - Select people or groups from this drop-down menu to add them to the Default Distribution. 
       *Note*: To appear as a selection on this list, the users and groups must exist in the project's Directory, and users must have 'Read Only' or higher permissions to the Instructions tool.   
       See [Add a User Account to the Project Directory](/product-manuals/directory-project/tutorials/add-user-account-to-project-directory) and [Add a Distribution Group to the Project Directory.](/process-guides/set-up-a-project-directory/invite-users-to-procore)
   - **Instruction Types**: Instruction types are used to organize instructions in the tool. Types from this page appear in the **Type** field when creating an instruction, and you can also filter by Type in the list view.   
     See [Create and Issue an Instruction](/product-manuals/instructions-project/tutorials/create-and-issue-an-instruction). You will soon have the ability to create multiple instruction types with a numbering prefix (e.g., architect instructions, site instructions, and so on) to this list.
   - **To add a new instruction type**:

     - Enter a name for the instruction type in the 'Type' column.
     - Enter a prefix for the instruction type in the 'Prefix' column. For example, you might want the system to apply the prefix "AI" to the "Architect Instruction" type. For each type, the system starts numbering new instructions as follows: *AI-1*, *AI-2*, *AI-3*, and so on.
     - Click **+ Add**.
   - **To edit an instruction type**: Click into the Type or Prefix column to edit, and click out of the field to save the changes.
   - **To delete an instruction type**: Click the RED 'x' across from the instruction type you want to remove. 
     *Note*: You can only delete instruction types that are not currently in use. However, you can always edit the type name or prefix.
4. Click **Update**.   
   This saves all updated settings.