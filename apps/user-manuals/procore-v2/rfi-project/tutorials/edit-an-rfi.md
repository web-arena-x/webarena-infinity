# Edit an RFI

Source: https://v2.support.procore.com/product-manuals/rfi-project/tutorials/edit-an-rfi

---

## Things to Consider

- [Required User Permissions](/product-manuals/rfi-project/permissions)
- **Additional Information:**

  - Users can only edit the [most recent revision of the RFI](/product-manuals/rfi-project/tutorials/revise-an-rfi).
  - If editing a revised RFI, the RFI's unique identifiers (Prefix, Number, and Revision Number) cannot be edited.
  - If you have a unique situation that requires you to create an RFI with a duplicate number, you must first create the RFI with a unique number. Then use the Steps below to create the duplicate number. See [Can I create an RFI with a duplicate number?](https://support.procore.com/faq/can-i-create-an-rfi-with-a-duplicate-number)
  - Your project may have the RFI Prefix option enabled. To learn more, see [How do I configure a prefix and starting number for a project's RFIs?](/product-manuals/rfi-project/tutorials/configure-a-prefix-and-starting-number-for-rfis)

## Steps

1. Navigate to the project's **RFIs** tool.
2. Click the **Items** tab.
3. You can click within applicable fields to make edits within the list view table.   
   **OR**
4. Locate the desired RFI in the list.

   - To search for or filter the list to locate a specific RFI, see [Search for and Filter RFIs](/product-manuals/rfi-project/tutorials/search-for-and-filter-rfis).
   - You can only edit an RFI's question when the RFI is in the 'Open' status.
   - You cannot edit RFIs that have been sent to the Recycle Bin.
5. Then choose one of these options:

   - Click **Edit**. This opens the RFI in edit mode.   
     **OR**
   - Click **View**. This opens the RFI in view mode. Then click **Edit**.
6. Modify the fields as follows:

   - **Number\***. This is a required field when a user with 'Admin' level permission on the RFI tool creates an RFI in the *Open* status. It is NOT required when users with 'Standard' level permission create a *Draft* RFI (see ).*Notes*:

     - If the RFI Prefix by Project Stage option is enabled, select a stage from the drop-down list (see [How do I configure a prefix and starting number for a project's RFIs?](/product-manuals/rfi-project/tutorials/configure-a-prefix-and-starting-number-for-rfis)).
     - If the option is NOT enabled, Procore will simply assign a number to the RFI in sequential order (see [How does Procore assign numbers to RFIs?](/faq-how-does-procore-assign-numbers-to-rfis)).
     - To learn about the available options for RFI numbering, see [What options do I have for numbering RFIs in Procore?](/faq-what-options-do-i-have-for-numbering-rfis-in-procore)

     Number
   - **Due Date**. Enter or select a date from the calendar for the RFI response to be due. This field is only visible and available to users with 'Admin' level permissions on the project's RFIs tool.*Note*: The 'Due Date' field is automatically populated based on the default number of days specified on the RFIs tool's Configure Settings page. See [Configure Advanced Settings: RFIs](/product-manuals/rfi-project/tutorials/configure-advanced-settings-rfis). The due date also respects which days are set as 'working days' for the project. See [Set Project Working Days](/product-manuals/admin-project/tutorials/set-project-working-days).

     Due Date
   - **Subject**. Provide a descriptive title for the RFI. The RFI's subject is displayed as the RFI's title in the list view.

     Subject
   - **Status**. Shows the status of the RFI (for example, *Draft*, *Open*, *Closed, or Closed-Draft*).

     Status
   - **Assignees**. Select one or more users to be responsible for responding to the RFI. Mark the Make Response Required checkbox next to an Assignee's name to make their response to the RFI required. *Note:* Assignees with the current Ball In Court responsibility on an RFI can add other users as Assignees to the RFI or forward the RFI to another user for their review. See [Add Assignees to an RFI as an Assignee on an RFI](/product-manuals/rfi-project/tutorials/add-assignees-to-an-rfi-as-an-assignee-on-an-rfi) and [Forward an RFI for Review](/product-manuals/rfi-project/tutorials/forward-an-rfi-for-review).

     Assignees
   - **RFI Manager\***. Select an RFI Manager from the drop-down list. See [What is the RFI Manager role?](/faq-what-is-the-rfi-manager-role)*Notes*:

     - By default, the name of designated RFI Manager appears here. See [Designate the Default RFI Manager for a Project's RFIs](/product-manuals/rfi-project/tutorials/designate-the-default-rfi-manager-for-a-projects-rfis).
     - If you are a user with 'Admin' level permission on the RFIs tool, you may select yourself or another user with 'Admin' level permission from the list.
     - If you are a user with 'Standard' level permission, this list only populates with the names of users who have 'Admin' level permission to the RFIs tool. You may only select another user with 'Admin' level permission from the list.

     RFI Manager
   - **Distribution.** Add users with 'Read-Only level permission or higher to the RFI's distribution list. Depending on the user's permission level, they can respond to the RFI using at least one of several methods. For details, see [Respond to an RFI](/product-manuals/rfi-project/tutorials/respond-to-an-rfi).

     DistributionÂ List
   - **Created By**. Shows the name of the user who created the RFI.

     Created By
   - **Date Initiated.** Records the date the RFI was placed into the 'Open' status. This field is blank when an RFI is in 'Draft' status.

     Date Initiated
   - **Received From**. Select the person from whom the RFI question was received from the drop-down list.

     Received From
   - **Responsible Contractor**. This field is automatically prefilled with the company that is associated with the user selected in the 'Received From' field.

     Responsible Contractor
   - **Drawing Number**: You can manually input a drawing number into this field. However, the recommended process to associate an RFI to a drawing is to [Link an RFI to a Drawing](/product-manuals/drawings-project/tutorials/link-items-on-a-drawing).

     Drawing Number
   - **Spec Section**. Select the relevant section from your specification book. See [Where do the selections from the 'Specification Sections' drop-down list come from?](/faq-where-do-the-selections-in-the-spec-sections-drop-down-list-come-from)

     Spec Section
   - **Location**. Select the location pertaining to the RFI from the drop-down list.*Note:* If Procore is configured to allow users to create locations (see [Allow or Disallow Users to Create Locations Within a Tool](/product-manuals/admin-project/tutorials/allow-or-disallow-users-to-create-locations-within-a-tool)), you can click the **Create a New Location** button at the bottom of the list.

     Location
   - **Sub Job\***. Select a sub job from the drop-down list. For this list to be available, the sub jobs feature must be enabled. See [Enable Sub Jobs on Projects for WBS](/process-guides/company-administration-work-breakdown-structure-guide/enable-sub-jobs-for-projects).

     Sub Job
   - **Schedule Impact**. Select one of the following options from the drop-down list.

     - **Yes**. Select this option if you know the number of days by which the schedule will be impacted. Then enter a number in the **Days** box to indicate the total number of calendar days.
     - **Yes (Unknown)**. Select this option if you know the schedule will be impacted, but the number of days is not known.
     - **No**. Select this option if there is no impact to the schedule.
     - **TBD**. Select this option if you have yet to determine if there is a schedule impact.
     - **N/A**. Select this option if an impact to the schedule is not applicable to this RFI.

     Schedule Impact
   - **Cost Code.** Select a [cost code](/glossary-of-terms) for the RFI. This links the RFI to the cost code, which is helpful later, should the RFI's scope of work affect the project's budget and result in a change order. See [Create a Potential Change Order for a Prime Contract](/product-manuals/prime-contracts-project/tutorials/create-a-potential-change-order-for-a-prime-contract).

     Cost Code
   - **Cost Impact**. Select one of the following options from the drop-down list.

     - **Yes**. Select this option if you know the amount by which the cost will be impacted. Then enter a number in the **$** box to indicate the cost impact.
     - **Yes (Unknown)**. Select this option if you know the cost will be impacted, but the amount is not know.
     - **No**. Select this option if there is no impact to the cost.
     - **TBD**. Select this option if you have yet to determine if there is a cost impact.
     - **N/A**. Select this option if the cost impact is not applicable to this RFI.

     Cost Impact
   - **Reference**. An optional field that can serve as a helpful reference tag.

     Reference
   - **Private**. Select *Yes* or *No* from the drop-down list. Yes indicates the RFI(s) will be marked Private. No indicates the RFI(s) will NOT be marked Private.

     Private
   - **Custom Fields**. If a user with 'Admin' level permission on the RFIs tool has configured custom fields to appear in your RFIs tool, those will appear in the creation page as shown. See [Configure Settings: RFIs](/product-manuals/rfi-project/tutorials/configure-advanced-settings-rfis).

     Custom Fields
   - **Question\***. If you are creating the RFI, input the question. If you are editing the RFI, modify it. *Note*: It is recommended that your question always document any additional background information that is required from the person assigned to submit an answer.

     Question
   - **Attach Files**. Click the Attach Files link to upload a file from your computer or select an existing file from one of the supported Procore tools (e.g., Photos, Drawings, Forms, Documents, or [Document Management](/faq-what-is-the-difference-between-document-management-attachments-and-attachments-from-other-tools)). Alternatively, you can also use a drag-and-drop operation to upload attachments from your computer.

     Attach Files
7. Click **Update**.