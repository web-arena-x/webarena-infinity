# Distribute a Submittal

Source: https://v2.support.procore.com/product-manuals/submittals-project/tutorials/distribute-a-submittal

---

## Background

Users who have been assigned 'Admin' level permissions to the Submittals tool have the ability to distribute reviewed submittals to the responsible contractor and other pertinent stakeholders (e.g., subcontractor, superintendent, project manager, etc.). By electronically distributing copies of reviewed submittals to key team members (who may or may not be an approver on the 

**Submittal Workflow**. The people assigned to complete the [submittal workflow](/glossary-of-terms). In Procore, the submittal workflow includes two roles: a [submitter](/glossary-of-terms) and the approvers who are responsible for performing/completing the [approval process](/glossary-of-terms). Typically, approvers are members of the design team.

Submittal Workflow), you provide your project teams with communications that enable them to move forward.

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permissions on the project's Submittals tool.
- **Prerequisites:**  
   The minimum requirements for a submittal to be distributed are as follows:

  - The submittal must have a minimum of one (1) approver added to the submittal workflow.
  - The submittal must have at least one (1) approver response.
- **Additional Information:**

  - You cannot distribute submittals in the Recycle Bin.

## Video

## Steps

### Close and Distribute a Submittal

1. Navigate to the project's **Submittals** tool.
2. Click the **Items** tab.
3. Click **View** next to the submittal you want to distribute.
4. If at least one required member of the submittal workflow has submitted their response, click **Close and Distribute**.
5. Enter the information you want to include in the distribution.

   ##### Â Note

   - The distribution list and the user roles selected in the Submittals tool configuration settings to receive a notification for the action 'Submittal Distributed', are automatically added as recipients.
   - The 'To' field is automatically populated by the submitter role.
   - the 'CC' field is automatically populated with users belonging to roles selected to receive the 'Submittal Distributed' notification in the Submittals configuration settings notification matrix.

- Mark the checkbox if you want to automatically **Create a Revision Upon Close and Distribution**.
- Mark the checkboxes for what General Information to include in the distribution.
- Mark the checkboxes to select which Workflow Responses to include in the distribution.
- Click **Distribute**  
   OR  
  **Distribute and Create Revision** to distribute the submittal.

##### Â Note

The following events occur when a submittal is distributed:

- Procore generates a PDF of the submittal and sends it by email to the chosen recipients.
- The PDF shows the name and company of the person who distributed the submittal.
- The submittal's status is set to *Closed.*
- The date, action, and timestamp are logged in the Change History tab of the submittal.
- The 'Submittal Distributed' banner appears (as illustrated below) showing the date and time the submittal was distributed.