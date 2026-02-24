# Create and Issue an Instruction

Source: https://v2.support.procore.com/product-manuals/instructions-project/tutorials/create-and-issue-an-instruction

---

## Background

Using the project's Instructions tool, you can create instructions that include attachments from other Procore tools (for example, Documents, Drawings, Photos, and more). You can also upload files from your computer to attach them to an instruction. Once your instruction is created, you can then issue it your recipients--which are typically one or more subcontractors on the project. All of this information is captured and stored in your Procore project in a log that resides in the Instructions tool. This historical record is also available in Procore for auditing purposes.

## Things to Consider

- **Required User Permission**:

 - *To create an instruction*, 'Standard' or 'Admin' level permission on the project's Instructions tool.
- **Prerequisites**:

 - *To add a person as a recipient in the 'Attention' or 'Distributionâ fields*, the person must exist in the Project Directory and have 'Read Only' permissions or higher to the Instructions tool.   
    See [Add a User Account to the Project Directory](/product-manuals/directory-project/tutorials/add-user-account-to-project-directory).
 - *To select a group as a recipient in the 'Attention' or 'Distribution' fields*, the group must exist in the Project Directory.   
    See [Add a Distribution Group to the Project Directory](/process-guides/set-up-a-project-directory/invite-users-to-procore).
- **Additional Information**:

 - The Instructions tool has been developed specifically for Procore clients in Australia, New Zealand, and Canada.
 - If you create an instruction and place it in the 'Draft' status, you will need to edit the instruction at a later time and then click '**Update & Issue**' in order to send it to your recipients.
 - Some image attachments may include the option to view them in a map view based on the files' GPS coordinates.   
    See [Which Procore tools let me view digital image attachments in a map view?](/faq-which-procore-tools-let-me-view-a-digital-image-attachment-in-a-map-view)

## Steps

1. Navigate to the project's Instructions tool.
2. Click **Create**.
3. Under **General Information**, complete the required data entry as follows: 
   *Note*: An asterisk (\*) denotes a required field.

   - \* **#**. Procore automatically assigns numbers to instructions in sequential order. 
     *Notes*:

     - If the **Number Instructions by Type** option is enabled, the prefix is applied to the new instruction number and the number cannot be edited.
     - If the **Number Instructions by Type** option is disabled, the prefix is applied to the new instruction number and users can edit the number. Duplicate numbers are NOT permitted.
   - \* **Type**. Select the desired instruction type from the list.
   - \* **Title**. A descriptive subject the instruction.
4. Continue adding information as needed:

   - **Instruction From.** Select the name of the person from whom the instruction originated.
   - **Date Received**. Select the date on which the instruction was received from the originator (i.e., the originator is the person named in the âInstruction Fromâ field)
   - **Attention**. Select the desired people or distribution groups from the Project Directory. These are the recipients to whom you will issue the instruction. 
     *Notes*:

     - If you click **Create and Issue**, the system will automatically send an email a notification about the instruction to all designated recipients.
     - If you click **Save as Draft**, the system will not send an email to the recipients).
   - **Distribution**. Select people or distribution groups from the Project Directory to copy the instruction to the named individuals. 
     *Note*: If you click **Create and Email** or **Save and Email** (which is available only to users with 'Admin' level permissions), Procore automatically sends an email notification to alert recipients about the instruction.
   - **Trade(s)**. Select the applicable trade from the drop-down menu. Trades are configured at the Company level.
   - **Schedule Impact**: Select one of the following to indicate if the instruction will affect the project's schedule (i.e. delay the project's planned schedule): *Yes*, *Yes (Unknown)*, *No*, *To Be Determined (TBD)*, and *N/A*.
   - **Private**. Mark this checkbox to hide the instruction from everyone except users with 'Admin' level permission to the Instructions tool, designated users in the 'Attention' field, and members of the default distribution group.
   - **Cost Impact**. Select one of the following to indicate if the punch list item will affect the project's cost (i.e. add costs to the project): *Yes*, *Yes (Unknown)*, *No*, *To Be Determined (TBD)*, and *N/A*.
   - **Description**. Enter a more detailed description for the instruction.
   - **Attachments**. To attach a file, click **Attach Files**. Then select the desired file.
5. Do one of the following:

   - If you do not want to issue the instruction (i.e., if you are NOT ready to send it out to recipients by email), click **Save As Draft**. This saves the instruction in the *Draft* status in the List view.
   - If you want to issue the instruction to recipients by email, click **Create & Issue**. This saves the instruction in the *Issued* status in the List view. (*Note*: If you have previously saved the instruction in the *Draft* status and have updated it in order to issue it now, the button's label will read **Update & Issue**).