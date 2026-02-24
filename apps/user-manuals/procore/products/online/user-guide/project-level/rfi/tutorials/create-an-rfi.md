# Create an RFI - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/create-an-rfi

---

## Objective

To create an RFI using the project's RFIs tool.

## Background

In the construction industry, RFIs are used to clarify ambiguities, answer questions, and fill information gaps that occur during the construction process. A common scenario for creating an RFI is when a subcontractor or superintendent requires specific information about completing a job or task from the project's architect or engineer. For example, a project drawing might be unclear, a requirement may be vague, or a product specification might be outdated, inaccurate, or incomplete. In such cases, it's important that questions are answered as quickly and succinctly as possible to prevent miscommunication, project delays, and/or rework.

In Procore, RFIs are comprised of the following components:

- ****General Information****. To make sure that a question is interpreted properly, it's important to include any additional information that provides related background information and context about the specific question, issue, or ambiguity.
- ****Question****. A formal question related to the construction project that requires a response from another person. For example, a subcontractor might submit the question on an RFI because a construction document or product specification is ambiguous. Questions can also be asked on behalf of another person/vendor.
- ****Replies****: A reply sent by an assignee on the RFI. For example, a project engineer might provide a reply to a subcontractor's question to clarify an ambiguous specification.
- ****Official Response****: A reply (or multiple replies) that have been designated as the 'Official Response' for the RFI. The 'RFI Manager' typically chooses the official response.

To view a common workflow of the RFI process, view the [Workflow Diagram](https://support.procore.com/products/online/user-guide/project-level/rfi/workflow "Workflow").

## Things to Consider

- ****Required User Permissions:****
  - **To create an RFI in the 'Draft' or 'Open' status:**
    - 'Admin' level permissions on the project's RFIs tool.  
      OR
    - 'Standard' level permissions on the project's RFIs tool with the ['Act as RFI Manager' granular permission](../../../company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#RFIs "Grant Granular Permissions in a Project Permissions Template") enabled on your permissions template.
  - **To create an RFI in the 'Draft' status:**
    - 'Standard' level permissions on the project's RFIs tool.

##### Important

- The 'Only Show Official Responses to Standard and Read-Only Users' configuration setting must be turned OFF in order for a user with 'Standard' level permissions on the project's RFIs tool to view all responses to an RFI that they created. See [Configure Advanced Settings: RFIs](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/configure-advanced-settings-rfis "Configure Advanced Settings: RFIs").
- Users with the ['Act as RFI Manager' granular permission](../../../company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#RFIs "Grant Granular Permissions in a Project Permissions Template") enabled on their permissions templates can view all responses to RFIs that they create ('Standard' only) or that they are designated as RFI Manager for even if this setting is turned ON.

- ****Prerequisites:****
  - Decide whether or not you want to enable the RFI Prefix by Project Stage Feature. See [How do I configure a prefix and starting number for a project's RFIs?](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/configure-a-prefix-and-starting-number-for-rfis "How do I configure a prefix and starting number for a project's RFIs?")
- ****Requirements:****
  - To save an RFI in the 'Open' status, the following fields are required: **Number, Subject,** *Assignees*, Due Date,** and **Question**.
  - Duplicate RFI numbers are NOT permitted. See [Can I create an RFI with a duplicate number?](https://support.procore.com/faq/can-i-create-an-rfi-with-a-duplicate-number "Can I create an RFI with a duplicate number?")
- ****Additional Information**:**
  - To learn about 'Draft' RFIs, see [What is a 'Draft' RFI?](https://support.procore.com/faq/what-is-a-draft-rfi "What is a 'Draft' RFI?") and [Who can view a 'Draft' RFI?](https://support.procore.com/faq/who-can-view-a-draft-rfi "Who can view a 'Draft' RFI?")
  - To learn about the 'Number' field, see [How does Procore assign numbers to RFIs?](https://support.procore.com/faq/how-does-procore-assign-numbers-to-rfis "How does Procore assign numbers to RFIs?")
  - To learn about automated email notifications, see [When does the RFIs tool send email notifications?](https://support.procore.com/faq/when-does-the-rfis-tool-send-email-notifications "When does the RFIs tool send email notifications?")

## Steps

The steps for creating an RFI vary, depending on the permission level you've been assigned to the project's RFIs tool.

- [Create an RFI as a User with 'Admin' Level Permission](#Create_an_RFI_as_a_User_with_'Admin'_Level_Permission "Create an RFI")  
  OR
- [Create an RFI as a User with 'Standard' Level Permission with the 'Act as RFI Manager' Granular Permission](#Create_an_RFI_as_a_User_with_'Standard'_Level_Permission_with_the_'Act_as_RFI_Manager'_Granular_Permission "Create an RFI")  
  OR
- [Create an RFI as a User with 'Standard' Level Permission](#Create_an_RFI_as_a_User_with_'Standard'_Level_Permission "Create an RFI")

### Create an RFI as a User with 'Admin' Level Permission

1. Navigate to the project's **RFIs** tool.
2. Click **+****Create**.
3. In the **Request** section, enter the following information:
   - ****Subject\*****. Provide a descriptive title for the RFI.
   - ****Question\*****. If you are creating the RFI, input the question. If you are editing the RFI, modify it. **Note**: It is recommended that your question always document any additional background information that is required from the person assigned to submit an answer.
   - *(Optional)* **Attachments**.
4. In the **General** tab, complete the form with the appropriate information.  
   Required fields are indicated by an asterisk (**\***).

- **Number\***. This is a required field when a user with 'Admin' level permission on the RFI tool creates an RFI in the *Open*status. It is NOT required when users with 'Standard' level permission create a *Draft* RFI (see [What is a 'Draft' RFI?](https://support.procore.com/faq/what-is-a-draft-rfi "What is a 'Draft' RFI?")).  
  *Notes*:

  - If the RFI Prefix by Project Stage option is enabled, select a stage from the drop-down list (see [How do I configure a prefix and starting number for a project's RFIs?](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/configure-a-prefix-and-starting-number-for-rfis "How do I configure a prefix and starting number for a project's RFIs?")).
  - If the option is NOT enabled, Procore will simply assign a number to the RFI in sequential order (see [How does Procore assign numbers to RFIs?](https://support.procore.com/faq/how-does-procore-assign-numbers-to-rfis "How does Procore assign numbers to RFIs?")).
  - To learn about the available options for RFI numbering, see [What options do I have for numbering RFIs in Procore?](https://support.procore.com/faq/what-options-do-i-have-for-numbering-rfis-in-procore "What options do I have for numbering RFIs in Procore?")
- **Due Date**. Enter or select a date from the calendar for the RFI response to be due. This field is only visible and available to users with 'Admin' level permissions on the project's RFIs tool.  
  *Note*: The 'Due Date' field is automatically populated based on the default number of days specified on the RFIs tool's Configure Settings page. See [Configure Advanced Settings: RFIs](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/configure-advanced-settings-rfis "Configure Advanced Settings: RFIs"). The due date also respects which days are set as 'working days' for the project. See [Set Project Working Days](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/set-project-working-days "Set Project Working Days").
- **Assignees**. Select one or more users to be responsible for responding to the RFI. Mark the Make Response Required checkbox next to an Assignee's name to make their response to the RFI required. *Note:* Assignees with the current Ball In Court responsibility on an RFI can add other users as Assignees to the RFI or forward the RFI to another user for their review. See [Add Assignees to an RFI as an Assignee on an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/add-assignees-to-an-rfi-as-an-assignee-on-an-rfi "Add Assignees to an RFI as an Assignee on an RFI") and [Forward an RFI for Review](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/forward-an-rfi-for-review "Forward an RFI for Review").
- **RFI Manager\***. Select an RFI Manager from the drop-down list. See [What is the RFI Manager role?](https://support.procore.com/faq/what-is-the-rfi-manager-role "What is the RFI Manager role?")  
  *Notes*:

  - By default, the name of designated RFI Manager appears here. See [Designate the Default RFI Manager for a Project's RFIs](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/designate-the-default-rfi-manager-for-a-projects-rfis "Designate the Default RFI Manager for a Project's RFIs").
  - If you are a user with 'Admin' level permission on the RFIs tool, you may select yourself or another user with 'Admin' level permission from the list.
- **Distribution.**Add users with 'Read-Only level permission or higher to the RFI's distribution list. Depending on the user's permission level, they can respond to the RFI using at least one of several methods. For details, see [Respond to an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/respond-to-an-rfi "Respond to an RFI").
- **Received From**. Select the person from whom the RFI question was received from the drop-down list.
- **Responsible Contractor**. This field is automatically prefilled with the company that is associated with the user selected in the 'Received From' field.
- **Drawing Number**: You can manually input a drawing number into this field. However, the recommended process to associate an RFI to a drawing is to [Link an RFI to a Drawing](https://support.procore.com/products/online/user-guide/project-level/drawings/tutorials/link-items-on-a-drawing "Link an RFI to a Drawing in the Drawings Tool").
- **Location**. Select the location pertaining to the RFI from the drop-down list.   
  *Note:* If Procore is configured to allow users to create locations (see [Allow or Disallow Users to Create Locations Within a Tool](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/allow-or-disallow-users-to-create-locations-within-a-tool "Allow or Disallow Users to Create Locations within a Tool")), you can click the **Create a New Location** button at the bottom of the list.
- **Spec Section**. Select the relevant section from your specification book. See [Where do the selections from the 'Specification Sections' drop-down list come from?](https://support.procore.com/faq/where-do-the-selections-in-the-spec-sections-drop-down-list-come-from "Where do the selections in the 'Spec Section' drop-down list come from?")
- **Cost Code.** Select a [cost code](../../../../../../references/construction-management/glossary-of-terms.md#Cost_Code "Glossary of Terms") for the RFI. This links the RFI to the cost code, which is helpful later, should the RFI's scope of work affect the project's budget and result in a change order. See [Create a Potential Change Order for a Prime Contract](https://support.procore.com/products/online/user-guide/project-level/prime-contracts/tutorials/create-a-potential-change-order-for-a-prime-contract "Create a Potential Change Order for a Prime Contract").
- **Project Stage**. Select the appropriate project stage for the RFI from the drop-down list. These stages are created by your company's [Procore Administrator](https://support.procore.com/procore-learning-paths/general-contractor/procore-administrator "Procore Administrator") in the Company level Admin tool. See [Add a Custom Project](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/add-a-custom-project-stage "Add a Custom Project Stage") [Stage](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/add-a-custom-project-stage "Add a Custom Project Stage").
- **Cost Impact**. Select one of the following options from the drop-down list.

  - ****Yes****. Select this option if you know the amount by which the cost will be impacted. Then enter a number in the ****$**** box to indicate the cost impact.
  - ****Yes (Unknown)****. Select this option if you know the cost will be impacted, but the amount is not know.
  - ****No****. Select this option if there is no impact to the cost.
  - ****TBD****. Select this option if you have yet to determine if there is a cost impact.
  - ****N/A****. Select this option if the cost impact is not applicable to this RFI.
- **Sub Job\***. Select a sub job from the drop-down list. For this list to be available, the sub jobs feature must be enabled. See [Enable Sub Jobs on Projects for WBS](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/enable-sub-jobs-on-projects-for-wbs "Enable Sub Jobs on Projects for WBS").
- **Schedule Impact**. Select one of the following options from the drop-down list.

  - **Yes**. Select this option if you know the number of days by which the schedule will be impacted. Then enter a number in the **Days** box to indicate the total number of calendar days.
  - **Yes (Unknown)**. Select this option if you know the schedule will be impacted, but the number of days is not known.
  - **No**. Select this option if there is no impact to the schedule.
  - **TBD**. Select this option if you have yet to determine if there is a schedule impact.
  - **N/A**. Select this option if an impact to the schedule is not applicable to this RFI.
- **Private**. Select *Yes* or *No* from the drop-down list. Yes indicates the RFI(s) will be marked Private. No indicates the RFI(s) will NOT be marked Private.
- **Reference**. An optional field that can serve as a helpful reference tag.
- **Custom Fields**. If a user with 'Admin' level permission on the RFIs tool has configured custom fields to appear in your RFIs tool, those will appear in the creation page as shown. See [Configure Settings: RFIs](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/configure-advanced-settings-rfis "Configure Settings: RFIs").

4. Click one (1) of these buttons:

   - **Create a Draft**. If you want to create a 'Draft'version of the RFI, click this button. This saves the RFI as a 'Draft'. The Ball In Court responsibility remains with the RFI Manager and emails are sent according to the project's settings. See [When does the RFIs tool send email notifications?](https://support.procore.com/faq/when-does-the-rfis-tool-send-email-notifications "When does the RFIs tool send email notifications?")
   - OR
   - **Create as Open**. If you want to create a new RFI as 'Open', click this button. The users designated as the RFI's **Assignees** have the first Ball In Court responsibility. The system shifts the Ball In Court responsibility to the users designated as the RFI's Assignees and emails are sent according to the project's settings. See [When does the RFIs tool send email notifications?](https://support.procore.com/faq/when-does-the-rfis-tool-send-email-notifications "When does the RFIs tool send email notifications?")

### [Back to Steps](#Steps "Create an RFI")

---

### Create an RFI as a User with 'Standard' Level Permission with the 'Act as RFI Manager' Granular Permission

1. Navigate to the project's **RFIs** tool.
2. Click **+****Create**.
3. In the 'General Information' section, complete the following:  
   Required fields are indicated by an asterisk (**\***).

- **Number\***. This is a required field when a user with 'Admin' level permission on the RFI tool creates an RFI in the *Open*status. It is NOT required when users with 'Standard' level permission create a *Draft* RFI (see [What is a 'Draft' RFI?](https://support.procore.com/faq/what-is-a-draft-rfi "What is a 'Draft' RFI?")).  
  *Notes*:

  - If the RFI Prefix by Project Stage option is enabled, select a stage from the drop-down list (see [How do I configure a prefix and starting number for a project's RFIs?](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/configure-a-prefix-and-starting-number-for-rfis "How do I configure a prefix and starting number for a project's RFIs?")).
  - If the option is NOT enabled, Procore will simply assign a number to the RFI in sequential order (see [How does Procore assign numbers to RFIs?](https://support.procore.com/faq/how-does-procore-assign-numbers-to-rfis "How does Procore assign numbers to RFIs?")).
  - To learn about the available options for RFI numbering, see [What options do I have for numbering RFIs in Procore?](https://support.procore.com/faq/what-options-do-i-have-for-numbering-rfis-in-procore "What options do I have for numbering RFIs in Procore?")
- **Due Date**. Enter or select a date from the calendar for the RFI response to be due. This field is only visible and available to users with 'Admin' level permissions on the project's RFIs tool.  
  *Note*: The 'Due Date' field is automatically populated based on the default number of days specified on the RFIs tool's Configure Settings page. See [Configure Advanced Settings: RFIs](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/configure-advanced-settings-rfis "Configure Advanced Settings: RFIs"). The due date also respects which days are set as 'working days' for the project. See [Set Project Working Days](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/set-project-working-days "Set Project Working Days").
- **Assignees**. Select one or more users to be responsible for responding to the RFI. Mark the Make Response Required checkbox next to an Assignee's name to make their response to the RFI required. *Note:* Assignees with the current Ball In Court responsibility on an RFI can add other users as Assignees to the RFI or forward the RFI to another user for their review. See [Add Assignees to an RFI as an Assignee on an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/add-assignees-to-an-rfi-as-an-assignee-on-an-rfi "Add Assignees to an RFI as an Assignee on an RFI") and [Forward an RFI for Review](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/forward-an-rfi-for-review "Forward an RFI for Review").
- **RFI Manager\***. Select an RFI Manager from the drop-down list. See [What is the RFI Manager role?](https://support.procore.com/faq/what-is-the-rfi-manager-role "What is the RFI Manager role?")  
  *Notes*:

  - By default, the name of designated RFI Manager appears here. See [Designate the Default RFI Manager for a Project's RFIs](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/designate-the-default-rfi-manager-for-a-projects-rfis "Designate the Default RFI Manager for a Project's RFIs").
  - If you are a user with 'Admin' level permission on the RFIs tool, you may select yourself or another user with 'Admin' level permission from the list.
- **Distribution.**Add users with 'Read-Only level permission or higher to the RFI's distribution list. Depending on the user's permission level, they can respond to the RFI using at least one of several methods. For details, see [Respond to an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/respond-to-an-rfi "Respond to an RFI").
- **Received From**. Select the person from whom the RFI question was received from the drop-down list.
- **Responsible Contractor**. This field is automatically prefilled with the company that is associated with the user selected in the 'Received From' field.
- **Drawing Number**: You can manually input a drawing number into this field. However, the recommended process to associate an RFI to a drawing is to [Link an RFI to a Drawing](https://support.procore.com/products/online/user-guide/project-level/drawings/tutorials/link-items-on-a-drawing "Link an RFI to a Drawing in the Drawings Tool").
- **Location**. Select the location pertaining to the RFI from the drop-down list.   
  *Note:* If Procore is configured to allow users to create locations (see [Allow or Disallow Users to Create Locations Within a Tool](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/allow-or-disallow-users-to-create-locations-within-a-tool "Allow or Disallow Users to Create Locations within a Tool")), you can click the **Create a New Location** button at the bottom of the list.
- **Spec Section**. Select the relevant section from your specification book. See [Where do the selections from the 'Specification Sections' drop-down list come from?](https://support.procore.com/faq/where-do-the-selections-in-the-spec-sections-drop-down-list-come-from "Where do the selections in the 'Spec Section' drop-down list come from?")
- **Cost Code.** Select a [cost code](../../../../../../references/construction-management/glossary-of-terms.md#Cost_Code "Glossary of Terms") for the RFI. This links the RFI to the cost code, which is helpful later, should the RFI's scope of work affect the project's budget and result in a change order. See [Create a Potential Change Order for a Prime Contract](https://support.procore.com/products/online/user-guide/project-level/prime-contracts/tutorials/create-a-potential-change-order-for-a-prime-contract "Create a Potential Change Order for a Prime Contract").
- **Project Stage**. Select the appropriate project stage for the RFI from the drop-down list. These stages are created by your company's [Procore Administrator](https://support.procore.com/procore-learning-paths/general-contractor/procore-administrator "Procore Administrator") in the Company level Admin tool. See [Add a Custom Project](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/add-a-custom-project-stage "Add a Custom Project Stage") [Stage](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/add-a-custom-project-stage "Add a Custom Project Stage").
- **Cost Impact**. Select one of the following options from the drop-down list.

  - ****Yes****. Select this option if you know the amount by which the cost will be impacted. Then enter a number in the ****$**** box to indicate the cost impact.
  - ****Yes (Unknown)****. Select this option if you know the cost will be impacted, but the amount is not know.
  - ****No****. Select this option if there is no impact to the cost.
  - ****TBD****. Select this option if you have yet to determine if there is a cost impact.
  - ****N/A****. Select this option if the cost impact is not applicable to this RFI.
- **Sub Job\***. Select a sub job from the drop-down list. For this list to be available, the sub jobs feature must be enabled. See [Enable Sub Jobs on Projects for WBS](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/enable-sub-jobs-on-projects-for-wbs "Enable Sub Jobs on Projects for WBS").
- **Schedule Impact**. Select one of the following options from the drop-down list.

  - **Yes**. Select this option if you know the number of days by which the schedule will be impacted. Then enter a number in the **Days** box to indicate the total number of calendar days.
  - **Yes (Unknown)**. Select this option if you know the schedule will be impacted, but the number of days is not known.
  - **No**. Select this option if there is no impact to the schedule.
  - **TBD**. Select this option if you have yet to determine if there is a schedule impact.
  - **N/A**. Select this option if an impact to the schedule is not applicable to this RFI.
- **Private**. Select *Yes* or *No* from the drop-down list. Yes indicates the RFI(s) will be marked Private. No indicates the RFI(s) will NOT be marked Private.
- **Reference**. An optional field that can serve as a helpful reference tag.
- **Custom Fields**. If a user with 'Admin' level permission on the RFIs tool has configured custom fields to appear in your RFIs tool, those will appear in the creation page as shown. See [Configure Settings: RFIs](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/configure-advanced-settings-rfis "Configure Settings: RFIs").

4. Click one (1) of these buttons:

   - **Create a Draft**. If you want to create a 'Draft'version of the RFI, click this button. This saves the RFI as a 'Draft'. The Ball In Court responsibility remains with the RFI Manager and emails are sent according to the project's settings. See [When does the RFIs tool send email notifications?](https://support.procore.com/faq/when-does-the-rfis-tool-send-email-notifications "When does the RFIs tool send email notifications?")
   - OR
   - **Create as Open**. If you want to create a new RFI as 'Open', click this button. The users designated as the RFI's **Assignees** have the first Ball In Court responsibility. The system shifts the Ball In Court responsibility to the users designated as the RFI's Assignees and emails are sent according to the project's settings. See [When does the RFIs tool send email notifications?](https://support.procore.com/faq/when-does-the-rfis-tool-send-email-notifications "When does the RFIs tool send email notifications?")

### [Back to Steps](#Steps "Create an RFI")

---

### Create an RFI as a User with 'Standard' Level Permission

If you are a foreman, superintendent, or subcontractor on a project, your project manager or engineer may grant you 'Standard' level permission on a project's RFIs tool. This gives you the ability to create an RFI in the 'Draft' status and send it to the person that you designate as the RFI Manager for review. That person can then review your RFI, place it in the 'Open' status, and assign it to the appropriate members of the project team for a response.

*Notes*:

- As a user with 'Standard' level permission, you will NOT see all the fields that are available to users with 'Admin' level permission to the tool.
- ***Important!*** If you have 'Standard' level permission to the RFIs tool and want to be notified of the Official Response to your RFI, you must be added to the RFI's Distribution List. If you are NOT a member of the Distribution list, you will NOT be notified the official response on the RFIs that you create.

1. Navigate to the project's **RFIs** tool.
2. Click **+Create**.
3. In the 'General Information' section, complete the following:  
   *Note*: Required fields are highlighted with an asterisk (**\***).

- **RFI Manager\***. Select an RFI Manager from the drop-down list. See [What is the RFI Manager role?](https://support.procore.com/faq/what-is-the-rfi-manager-role "What is the RFI Manager role?")  
  *Notes*:

  - By default, the name of designated RFI Manager appears here. See [Designate the Default RFI Manager for a Project's RFIs](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/designate-the-default-rfi-manager-for-a-projects-rfis "Designate the Default RFI Manager for a Project's RFIs").
  - If you are a user with 'Admin' level permission on the RFIs tool, you may select yourself or another user with 'Admin' level permission from the list.
- **Distribution.**Add users with 'Read-Only level permission or higher to the RFI's distribution list. Depending on the user's permission level, they can respond to the RFI using at least one of several methods. For details, see [Respond to an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/respond-to-an-rfi "Respond to an RFI").
- **Received From**. Select the person from whom the RFI question was received from the drop-down list.
- **Responsible Contractor**. This field is automatically prefilled with the company that is associated with the user selected in the 'Received From' field.
- **Drawing Number**: You can manually input a drawing number into this field. However, the recommended process to associate an RFI to a drawing is to [Link an RFI to a Drawing](https://support.procore.com/products/online/user-guide/project-level/drawings/tutorials/link-items-on-a-drawing "Link an RFI to a Drawing in the Drawings Tool").
- **Spec Section**. Select the relevant section from your specification book. See [Where do the selections from the 'Specification Sections' drop-down list come from?](https://support.procore.com/faq/where-do-the-selections-in-the-spec-sections-drop-down-list-come-from "Where do the selections in the 'Spec Section' drop-down list come from?")
- **Location**. Select the location pertaining to the RFI from the drop-down list.   
  *Note:* If Procore is configured to allow users to create locations (see [Allow or Disallow Users to Create Locations Within a Tool](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/allow-or-disallow-users-to-create-locations-within-a-tool "Allow or Disallow Users to Create Locations within a Tool")), you can click the **Create a New Location** button at the bottom of the list.
- **Sub Job\***. Select a sub job from the drop-down list. For this list to be available, the sub jobs feature must be enabled. See [Enable Sub Jobs on Projects for WBS](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/enable-sub-jobs-on-projects-for-wbs "Enable Sub Jobs on Projects for WBS").
- **Schedule Impact**. Select one of the following options from the drop-down list.

  - **Yes**. Select this option if you know the number of days by which the schedule will be impacted. Then enter a number in the **Days** box to indicate the total number of calendar days.
  - **Yes (Unknown)**. Select this option if you know the schedule will be impacted, but the number of days is not known.
  - **No**. Select this option if there is no impact to the schedule.
  - **TBD**. Select this option if you have yet to determine if there is a schedule impact.
  - **N/A**. Select this option if an impact to the schedule is not applicable to this RFI.
- **Cost Code.** Select a [cost code](../../../../../../references/construction-management/glossary-of-terms.md#Cost_Code "Glossary of Terms") for the RFI. This links the RFI to the cost code, which is helpful later, should the RFI's scope of work affect the project's budget and result in a change order. See [Create a Potential Change Order for a Prime Contract](https://support.procore.com/products/online/user-guide/project-level/prime-contracts/tutorials/create-a-potential-change-order-for-a-prime-contract "Create a Potential Change Order for a Prime Contract").
- **Cost Impact**. Select one of the following options from the drop-down list.

  - ****Yes****. Select this option if you know the amount by which the cost will be impacted. Then enter a number in the ****$**** box to indicate the cost impact.
  - ****Yes (Unknown)****. Select this option if you know the cost will be impacted, but the amount is not know.
  - ****No****. Select this option if there is no impact to the cost.
  - ****TBD****. Select this option if you have yet to determine if there is a cost impact.
  - ****N/A****. Select this option if the cost impact is not applicable to this RFI.
- **Reference**. An optional field that can serve as a helpful reference tag.
- **Custom Fields**. If a user with 'Admin' level permission on the RFIs tool has configured custom fields to appear in your RFIs tool, those will appear in the creation page as shown. See [Configure Settings: RFIs](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/configure-advanced-settings-rfis "Configure Settings: RFIs").

4. **Send for Review**. Click this button to save your new RFI in the 'Draft' status and send it to the person you designated in the **RFI Manager** field. This shifts the Ball in Court responsibility to the RFI Manager.  
   *Note*: As an RFI creator with 'Standard' level permissions on the project's RFIs tool, you can only edit the RFI's 'General Information' and 'Question' sections while the RFI's status is 'Draft'. When the RFI's status shifts to 'Open', only users with 'Admin' level permissions on the project's RFIs tool can edit the RFI.

### [Back to Steps](#Steps "Create an RFI")

---

## See Also

- [Create and View a Custom RFI Report](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/create-and-view-an-rfi-report "Create and View a Custom RFI Report")
- [Add a Related Item to an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/add-a-related-item-to-an-rfi "Add a Related Item to an RFI")
- [Edit an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/edit-an-rfi "Edit an RFI")
- [Close an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/close-an-rfi "Close an RFI")

##