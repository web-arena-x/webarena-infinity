# Add an End Step (Unsuccessful)

Source: https://v2.support.procore.com/product-manuals/workflows-company/tutorials/add-an-end-step-unsuccessful

---

Configure the 'End Step (Unsuccessful)' in the Workflow Builder to formally mark a workflow's unsuccessful termination. Add the step, define its name and status (e.g., 'Rejected,' 'Not Approved'), and set up optional notifications to inform relevant stakeholders of the outcome.

### Steps

#### Add an End Step (Unsuccessful)

An unsuccessful end step concludes the workflow and signifies that the desired outcome was not achieved. For example, a project item was 'Rejected' or 'Not Approved.

1. In the Workflow Builder, click  in an existing step and choose **End** **Step (Unsuccessful)**.
2. Under **General Information**, do the following:

   - **Step Name**. Enter a name for the workflow step.
   - **Item Status**. Select the status that shows the item was unsuccessful. Status options vary for each item in the Procore tool.
   - *Optional:* **Notification Recipients** **.** Select which groups or roles Procore will automatically notify when the step is complete. The selections include:

     - **Workflow Manager**. A workflow manager is a designated role in a Procore project. See [What are the different roles associated with the Workflows tool?](/faq-what-are-the-different-roles-associated-with-workflows)
     - **Item Creator**. An item creator is the Procore user who created the item on a project. See [What are the different roles associated with the Workflows tool?](/faq-what-are-the-different-roles-associated-with-workflows)
     - **Distribution Group**. After publishing this workflow template and assigning it to a project, you can define different group members when configuring the workflow on the Project level. See [What is the difference between a distribution group and distribution list in Procore?](/faq-what-is-the-difference-between-a-distribution-group-and-a-distribution-list)
     - **All Project Users from the Company**. All project users from the item creator's company who are assigned to the project are automatically notified when you select **Item Creator's Company** from the notification recipient list.

#### Save the Template

##### Â Important

Procore strongly recommends saving your progress using the **Save as Draft** option as you build your workflow template. This is a standard best practice to help minimize data loss due to accidental closure, browser issues, or other unforeseen interruptions.

- **Cancel**. Discards any changes made.
- **Save as Draft**. Saves a 'Draft' version with a minor version number (e.g., 0.1, 0.2, 0.3, and so on). Select this option if the workflow template is still under development.
- **Save and Publish**. Creates a major version number for the workflow (e.g., 1.0, 2.0, 3.0, and so on). Choose this option when the workflow is ready for implementation and project assignment.