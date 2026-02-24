# Create an RFI

Source: https://v2.support.procore.com/product-manuals/rfi-project/tutorials/create-an-rfi

---

## Background

In the construction industry, RFIs are used to clarify ambiguities, answer questions, and fill information gaps that occur during the construction process. A common scenario for creating an RFI is when a subcontractor or superintendent requires specific information about completing a job or task from the project's architect or engineer. For example, a project drawing might be unclear, a requirement may be vague, or a product specification might be outdated, inaccurate, or incomplete. In such cases, it's important that questions are answered as quickly and succinctly as possible to prevent miscommunication, project delays, and/or rewor

## ThingsÂ to Consider

- [Required User Permissions](/product-manuals/rfi-project/permissions)
- **Prerequisites:**

  - Decide whether or not you want to enable the RFI Prefix by Project Stage Feature. See [How do I configure a prefix and starting number for a project's RFIs?](/product-manuals/rfi-project/tutorials/configure-a-prefix-and-starting-number-for-rfis)
- **Requirements:**

  - To save an RFI in the 'Open' status, the following fields are required: *Number, Subject,* *Assignees, Due Date,* and *Question*.
  - Duplicate RFI numbers are NOT permitted.

## Steps

The steps for creating an RFI vary, depending on the permission level you've been assigned to the project's RFIs tool.

- Create an RFI as a User with 'Admin' Level Permission  
  **OR**
- Create an RFI as a User with 'Standard' Level Permission with the 'Act as RFI Manager' Granular Permission  
  **OR**
- Create an RFI as a User with 'Standard' Level Permission

### Create an RFI as a User with 'Admin' Level Permission

1. Navigate to the project's **RFIs** tool.
2. Click **+** **Create**.
3. In the **General** tab, complete the form with the appropriate information.  
   Required fields are indicated by an asterisk (**\***).

- **Number\***. This is a required field when a user with 'Admin' level permission on the RFI tool creates an RFI in the *Open* status. It is NOT required when users with 'Standard' level permission create a *Draft* RFI (see ).*Notes*:

  - If the RFI Prefix by Project Stage option is enabled, select a stage from the drop-down list (see [How do I configure a prefix and starting number for a project's RFIs?](/product-manuals/rfi-project/tutorials/configure-a-prefix-and-starting-number-for-rfis)).
  - If the option is NOT enabled, Procore will simply assign a number to the RFI in sequential order (see [How does Procore assign numbers to RFIs?](/faq-how-does-procore-assign-numbers-to-rfis)).
  - To learn about the available options for RFI numbering, see [What options do I have for numbering RFIs in Procore?](/faq-what-options-do-i-have-for-numbering-rfis-in-procore)

  Number
- **Due Date**. Enter or select a date from the calendar for the RFI response to be due. This field is only visible and available to users with 'Admin' level permissions on the project's RFIs tool.*Note*: The 'Due Date' field is automatically populated based on the default number of days specified on the RFIs tool's Configure Settings page. See [Configure Advanced Settings: RFIs](/product-manuals/rfi-project/tutorials/configure-advanced-settings-rfis). The due date also respects which days are set as 'working days' for the project. See [Set Project Working Days](/product-manuals/admin-project/tutorials/set-project-working-days).

  Due Date
- **Subject**. Provide a descriptive title for the RFI. The RFI's subject is displayed as the RFI's title in the list view.

  Subject
- **Assignees**. Select one or more users to be responsible for responding to the RFI. Mark the Make Response Required checkbox next to an Assignee's name to make their response to the RFI required. *Note:* Assignees with the current Ball In Court responsibility on an RFI can add other users as Assignees to the RFI or forward the RFI to another user for their review. See [Add Assignees to an RFI as an Assignee on an RFI](/product-manuals/rfi-project/tutorials/add-assignees-to-an-rfi-as-an-assignee-on-an-rfi) and [Forward an RFI for Review](/product-manuals/rfi-project/tutorials/forward-an-rfi-for-review).

  Assignees
- **RFI Manager\***. Select an RFI Manager from the drop-down list. See [What is the RFI Manager role?](/faq-what-is-the-rfi-manager-role)*Notes*:

  - By default, the name of designated RFI Manager appears here. See [Designate the Default RFI Manager for a Project's RFIs](/product-manuals/rfi-project/tutorials/designate-the-default-rfi-manager-for-a-projects-rfis).
  - If you are a user with 'Admin' level permission on the RFIs tool, you may select yourself or another user with 'Admin' level permission from the list.
  - If you are a user with 'Standard' level permission, this list only populates with the names of users who have 'Admin' level permission to the RFIs tool. You may only select another user with 'Admin' level permission from the list.

  RFI Manager
- **Distribution.** Add users with 'Read-Only level permission or higher to the RFI's distribution list. Depending on the user's permission level, they can respond to the RFI using at least one of several methods. For details, see [Respond to an RFI](/product-manuals/rfi-project/tutorials/respond-to-an-rfi).

  Distribution
- **Received From**. Select the person from whom the RFI question was received from the drop-down list.

  Received From
- **Responsible Contractor**. This field is automatically prefilled with the company that is associated with the user selected in the 'Received From' field.

  Responsible Contractor
- **Drawing Number**: You can manually input a drawing number into this field. However, the recommended process to associate an RFI to a drawing is to [Link an RFI to a Drawing](/product-manuals/drawings-project/tutorials/link-items-on-a-drawing).

  Drawing Number
- **Location**. Select the location pertaining to the RFI from the drop-down list.*Note:* If Procore is configured to allow users to create locations (see [Allow or Disallow Users to Create Locations Within a Tool](/product-manuals/admin-project/tutorials/allow-or-disallow-users-to-create-locations-within-a-tool)), you can click the **Create a New Location** button at the bottom of the list.

  Location
- **Spec Section**. Select the relevant section from your specification book. See [Where do the selections from the 'Specification Sections' drop-down list come from?](/faq-where-do-the-selections-in-the-spec-sections-drop-down-list-come-from)

  Spec Section
- **Cost Code.** Select a [cost code](/glossary-of-terms) for the RFI. This links the RFI to the cost code, which is helpful later, should the RFI's scope of work affect the project's budget and result in a change order. See [Create a Potential Change Order for a Prime Contract](/product-manuals/prime-contracts-project/tutorials/create-a-potential-change-order-for-a-prime-contract).

  Cost Code
- **Project Stage**. Select the appropriate project stage for the RFI from the drop-down list. These stages are created by your company's [Procore Administrator](https://support.procore.com/procore-learning-paths/general-contractor/procore-administrator) in the Company level Admin tool. See [Add a Custom Project](/product-manuals/admin-company/tutorials/add-a-custom-project-stage) [Stage](/product-manuals/admin-company/tutorials/add-a-custom-project-stage).

  Project Stage
- **Cost Impact**. Select one of the following options from the drop-down list.

  - **Yes**. Select this option if you know the amount by which the cost will be impacted. Then enter a number in the **$** box to indicate the cost impact.
  - **Yes (Unknown)**. Select this option if you know the cost will be impacted, but the amount is not know.
  - **No**. Select this option if there is no impact to the cost.
  - **TBD**. Select this option if you have yet to determine if there is a cost impact.
  - **N/A**. Select this option if the cost impact is not applicable to this RFI.

  Cost Impact
- **Sub Job\***. Select a sub job from the drop-down list. For this list to be available, the sub jobs feature must be enabled. See [Enable Sub Jobs on Projects for WBS](/process-guides/company-administration-work-breakdown-structure-guide/enable-sub-jobs-for-projects).

  Sub Job
- **Schedule Impact**. Select one of the following options from the drop-down list.

  - **Yes**. Select this option if you know the number of days by which the schedule will be impacted. Then enter a number in the **Days** box to indicate the total number of calendar days.
  - **Yes (Unknown)**. Select this option if you know the schedule will be impacted, but the number of days is not known.
  - **No**. Select this option if there is no impact to the schedule.
  - **TBD**. Select this option if you have yet to determine if there is a schedule impact.
  - **N/A**. Select this option if an impact to the schedule is not applicable to this RFI.

  Schedule Impact
- **Private**. Select *Yes* or *No* from the drop-down list. Yes indicates the RFI(s) will be marked Private. No indicates the RFI(s) will NOT be marked Private.

  Private
- **Reference**. An optional field that can serve as a helpful reference tag.

  Reference
- **Custom Fields**. If a user with 'Admin' level permission on the RFIs tool has configured custom fields to appear in your RFIs tool, those will appear in the creation page as shown. See [Configure Settings: RFIs](/product-manuals/rfi-project/tutorials/configure-advanced-settings-rfis).

  Custom Fields
- **Question\***. If you are creating the RFI, input the question. If you are editing the RFI, modify it. *Note*: It is recommended that your question always document any additional background information that is required from the person assigned to submit an answer.

  Question

#### Send the RFI

1. Click one (1) of these buttons:

- **Create a Draft**. If you want to create a 'Draft' version of the RFI, click this button. This saves the RFI as a 'Draft'. The Ball In Court responsibility remains with the RFI Manager and emails are sent according to the project's settings. See [When does the RFIs tool send email notifications?](/faq-when-does-the-rfis-tool-send-email-notifications)

  Create a Draft  
  **OR**
- **Create as Open**. If you want to create a new RFI as 'Open', click this button. The users designated as the RFI's **Assignees** have the first Ball In Court responsibility. The system shifts the Ball In Court responsibility to the users designated as the RFI's Assignees and emails are sent according to the project's settings. See [When does the RFIs tool send email notifications?](/faq-when-does-the-rfis-tool-send-email-notifications)

  Create as Open

### Create an RFI as a User with 'Standard' Level Permission with the 'Act as RFI Manager' Granular Permission

1. Navigate to the project's **RFIs** tool.
2. Click **+** **Create**.
3. In the 'General Information' section, complete the following:  
   Required fields are indicated by an asterisk (**\***).

- **Number\***. This is a required field when a user with 'Admin' level permission on the RFI tool creates an RFI in the *Open* status. It is NOT required when users with 'Standard' level permission create a *Draft* RFI (see ).*Notes*:

  - If the RFI Prefix by Project Stage option is enabled, select a stage from the drop-down list (see [How do I configure a prefix and starting number for a project's RFIs?](/product-manuals/rfi-project/tutorials/configure-a-prefix-and-starting-number-for-rfis)).
  - If the option is NOT enabled, Procore will simply assign a number to the RFI in sequential order (see [How does Procore assign numbers to RFIs?](/faq-how-does-procore-assign-numbers-to-rfis)).
  - To learn about the available options for RFI numbering, see [What options do I have for numbering RFIs in Procore?](/faq-what-options-do-i-have-for-numbering-rfis-in-procore)

  Number
- **Due Date**. Enter or select a date from the calendar for the RFI response to be due. This field is only visible and available to users with 'Admin' level permissions on the project's RFIs tool.*Note*: The 'Due Date' field is automatically populated based on the default number of days specified on the RFIs tool's Configure Settings page. See [Configure Advanced Settings: RFIs](/product-manuals/rfi-project/tutorials/configure-advanced-settings-rfis). The due date also respects which days are set as 'working days' for the project. See [Set Project Working Days](/product-manuals/admin-project/tutorials/set-project-working-days).

  Due Date
- **Subject**. Provide a descriptive title for the RFI. The RFI's subject is displayed as the RFI's title in the list view.

  Subject
- **Assignees**. Select one or more users to be responsible for responding to the RFI. Mark the Make Response Required checkbox next to an Assignee's name to make their response to the RFI required. *Note:* Assignees with the current Ball In Court responsibility on an RFI can add other users as Assignees to the RFI or forward the RFI to another user for their review. See [Add Assignees to an RFI as an Assignee on an RFI](/product-manuals/rfi-project/tutorials/add-assignees-to-an-rfi-as-an-assignee-on-an-rfi) and [Forward an RFI for Review](/product-manuals/rfi-project/tutorials/forward-an-rfi-for-review).

  Assignees
- **RFI Manager\***. Select an RFI Manager from the drop-down list. See [What is the RFI Manager role?](/faq-what-is-the-rfi-manager-role)*Notes*:

  - By default, the name of designated RFI Manager appears here. See [Designate the Default RFI Manager for a Project's RFIs](/product-manuals/rfi-project/tutorials/designate-the-default-rfi-manager-for-a-projects-rfis).
  - If you are a user with 'Admin' level permission on the RFIs tool, you may select yourself or another user with 'Admin' level permission from the list.
  - If you are a user with 'Standard' level permission, this list only populates with the names of users who have 'Admin' level permission to the RFIs tool. You may only select another user with 'Admin' level permission from the list.

  RFI Manager
- **Distribution.** Add users with 'Read-Only level permission or higher to the RFI's distribution list. Depending on the user's permission level, they can respond to the RFI using at least one of several methods. For details, see [Respond to an RFI](/product-manuals/rfi-project/tutorials/respond-to-an-rfi).

  Distribution
- **Received From**. Select the person from whom the RFI question was received from the drop-down list.

  Received From
- **Responsible Contractor**. This field is automatically prefilled with the company that is associated with the user selected in the 'Received From' field.

  Responsible Contractor
- **Drawing Number**: You can manually input a drawing number into this field. However, the recommended process to associate an RFI to a drawing is to [Link an RFI to a Drawing](/product-manuals/drawings-project/tutorials/link-items-on-a-drawing).

  Drawing Number
- **Location**. Select the location pertaining to the RFI from the drop-down list.*Note:* If Procore is configured to allow users to create locations (see [Allow or Disallow Users to Create Locations Within a Tool](/product-manuals/admin-project/tutorials/allow-or-disallow-users-to-create-locations-within-a-tool)), you can click the **Create a New Location** button at the bottom of the list.

  Location
- **Spec Section**. Select the relevant section from your specification book. See [Where do the selections from the 'Specification Sections' drop-down list come from?](/faq-where-do-the-selections-in-the-spec-sections-drop-down-list-come-from)

  Spec Section
- **Cost Code.** Select a [cost code](/glossary-of-terms) for the RFI. This links the RFI to the cost code, which is helpful later, should the RFI's scope of work affect the project's budget and result in a change order. See [Create a Potential Change Order for a Prime Contract](/product-manuals/prime-contracts-project/tutorials/create-a-potential-change-order-for-a-prime-contract).

  Cost Code
- **Project Stage**. Select the appropriate project stage for the RFI from the drop-down list. These stages are created by your company's [Procore Administrator](https://support.procore.com/procore-learning-paths/general-contractor/procore-administrator) in the Company level Admin tool. See [Add a Custom Project](/product-manuals/admin-company/tutorials/add-a-custom-project-stage) [Stage](/product-manuals/admin-company/tutorials/add-a-custom-project-stage).

  Project Stage
- **Cost Impact**. Select one of the following options from the drop-down list.

  - **Yes**. Select this option if you know the amount by which the cost will be impacted. Then enter a number in the **$** box to indicate the cost impact.
  - **Yes (Unknown)**. Select this option if you know the cost will be impacted, but the amount is not know.
  - **No**. Select this option if there is no impact to the cost.
  - **TBD**. Select this option if you have yet to determine if there is a cost impact.
  - **N/A**. Select this option if the cost impact is not applicable to this RFI.

  Cost Impact
- **Sub Job\***. Select a sub job from the drop-down list. For this list to be available, the sub jobs feature must be enabled. See [Enable Sub Jobs on Projects for WBS](/process-guides/company-administration-work-breakdown-structure-guide/enable-sub-jobs-for-projects).

  Sub Job
- **Schedule Impact**. Select one of the following options from the drop-down list.

  - **Yes**. Select this option if you know the number of days by which the schedule will be impacted. Then enter a number in the **Days** box to indicate the total number of calendar days.
  - **Yes (Unknown)**. Select this option if you know the schedule will be impacted, but the number of days is not known.
  - **No**. Select this option if there is no impact to the schedule.
  - **TBD**. Select this option if you have yet to determine if there is a schedule impact.
  - **N/A**. Select this option if an impact to the schedule is not applicable to this RFI.

  Schedule Impact
- **Private**. Select *Yes* or *No* from the drop-down list. Yes indicates the RFI(s) will be marked Private. No indicates the RFI(s) will NOT be marked Private.

  Private
- **Reference**. An optional field that can serve as a helpful reference tag.

  Reference
- **Custom Fields**. If a user with 'Admin' level permission on the RFIs tool has configured custom fields to appear in your RFIs tool, those will appear in the creation page as shown. See [Configure Settings: RFIs](/product-manuals/rfi-project/tutorials/configure-advanced-settings-rfis).

  Custom Fields
- **Question\***. If you are creating the RFI, input the question. If you are editing the RFI, modify it. *Note*: It is recommended that your question always document any additional background information that is required from the person assigned to submit an answer.

  Question

#### Send the RFI

1. Click one (1) of these buttons:

- **Create a Draft**. If you want to create a 'Draft' version of the RFI, click this button. This saves the RFI as a 'Draft'. The Ball In Court responsibility remains with the RFI Manager and emails are sent according to the project's settings. See [When does the RFIs tool send email notifications?](/faq-when-does-the-rfis-tool-send-email-notifications)

  Create a Draft  
  **OR**
- **Create as Open**. If you want to create a new RFI as 'Open', click this button. The users designated as the RFI's **Assignees** have the first Ball In Court responsibility. The system shifts the Ball In Court responsibility to the users designated as the RFI's Assignees and emails are sent according to the project's settings. See [When does the RFIs tool send email notifications?](/faq-when-does-the-rfis-tool-send-email-notifications)

  Create as Open

### Create an RFI as a User with 'Standard' Level Permission

If you are a foreman, superintendent, or subcontractor on a project, your project manager or engineer may grant you 'Standard' level permission on a project's RFIs tool. This gives you the ability to create an RFI in the 'Draft' status and send it to the person that you designate as the RFI Manager for review. That person can then review your RFI, place it in the 'Open' status, and assign it to the appropriate members of the project team for a response.

**Notes:**

- As a user with 'Standard' level permission, you will NOT see all the fields that are available to users with 'Admin' level permission to the tool.
- ***Important!*** If you have 'Standard' level permission to the RFIs tool and want to be notified of the Official Response to your RFI, you must be added to the RFI's Distribution List. If you are NOT a member of the Distribution list, you will NOT be notified the official response on the RFIs that you create.

1. Navigate to the project's **RFIs** tool.
2. Click **+Create**.
3. In the 'General Information' section, complete the following:  
   **Note:** Required fields are highlighted with an asterisk (**\***).

- **Subject**. Provide a descriptive title for the RFI. The RFI's subject is displayed as the RFI's title in the list view.

  Subject
- **RFI Manager\***. Select an RFI Manager from the drop-down list. See [What is the RFI Manager role?](/faq-what-is-the-rfi-manager-role)*Notes*:

  - By default, the name of designated RFI Manager appears here. See [Designate the Default RFI Manager for a Project's RFIs](/product-manuals/rfi-project/tutorials/designate-the-default-rfi-manager-for-a-projects-rfis).
  - If you are a user with 'Admin' level permission on the RFIs tool, you may select yourself or another user with 'Admin' level permission from the list.
  - If you are a user with 'Standard' level permission, this list only populates with the names of users who have 'Admin' level permission to the RFIs tool. You may only select another user with 'Admin' level permission from the list.

  RFI Manager
- **Distribution.** Add users with 'Read-Only level permission or higher to the RFI's distribution list. Depending on the user's permission level, they can respond to the RFI using at least one of several methods. For details, see [Respond to an RFI](/product-manuals/rfi-project/tutorials/respond-to-an-rfi).

  Distribution
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
- **Custom Fields**. If a user with 'Admin' level permission on the RFIs tool has configured custom fields to appear in your RFIs tool, those will appear in the creation page as shown. See [Configure Settings: RFIs](/product-manuals/rfi-project/tutorials/configure-advanced-settings-rfis).

  Custom Fields
- **Question\***. If you are creating the RFI, input the question. If you are editing the RFI, modify it. *Note*: It is recommended that your question always document any additional background information that is required from the person assigned to submit an answer.

  Question

#### Send the RFi

1. Click 

   **Send for Review**. Click this button to save your new RFI in the 'Draft' status and send it to the person you designated in the **RFI Manager** field. This shifts the Ball in Court responsibility to the RFI Manager.*Note*: As an RFI creator with 'Standard' level permissions on the project's RFIs tool, you can only edit the RFI's 'General Information' and 'Question' sections while the RFI's status is 'Draft'. When the RFI's status shifts to 'Open', only users with 'Admin' level permissions on the project's RFIs tool can edit the RFI.

   Send for Review