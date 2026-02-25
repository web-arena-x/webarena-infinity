# About Workflows in the Document Management Tool

Source: https://v2.support.procore.com/product-manuals/document-management-project/tutorials/about-workflows-in-the-document-management-tool

---

##### Regional availability

The Document Management tool is available in select countries. It is not yet available for Procore accounts in the U.S. To learn more, please reach out to your Procore point of contact.

## Background

If your organization uses approval processes for document revisions, you can create custom workflow templates in the Workflows tool that can then be assigned to documents that are uploaded to the Document Management tool. Once a workflow has started, workflow participants are notified to review documents, optionally comment on them with markup, and provide an approval outcome.

As a document revision gets reviewed and is either approved or rejected, the revision's status is automatically updated in Procore. This means you don't need to manually change permission settings or move revisions between folders or tools after a document is approved. When a workflow is created for a PDF document, workflow assignees can add markups directly to the PDF during their step in the workflow. After the workflow is complete, all workflow decisions, markups, and additional file attachments are preserved so that they can be referenced later.

## Things to Consider

- **Required User Permissions**:

 - Actions related to workflows within the Document Management tool can require permissions the following areas in Procore (see the [Document Management Permissions Matrix](/product-manuals/document-management-project/permissions) and [How do permissions work in the Document Management tool?](/faq-how-do-permissions-work-in-the-document-management-tool)):

    - General permissions to the project's Document Management tool.
    - General permissions to the Company level Workflows tool.
    - Granular permissions enabled for 'Document Management Workflows' on a project permission template. See [What granular permissions are available for Document Management Workflows?](/faq-what-granular-permissions-are-available-for-document-management-workflows)
    - Permissions set in the Configure Settings page of the Document Management tool. See [Configure Settings: Document Management](/product-manuals/document-management-project/tutorials/configure-settings-document-management) and [View and Manage Workflow Permissions in the Document Management Tool](/product-manuals/document-management-project/tutorials/view-and-manage-workflow-permissions-in-the-document-management-tool).
- **Additional Information**:

 - Your organization must have the Company level Workflows tool enabled in Procore. See [About the Workflows Beta Program](/product-manuals/workflows-company/tutorials/about-the-workflows-tool).
 - If certain types of document errors arise, Project Admin can [resolve them](/faq-how-do-i-resolve-document-errors-in-the-document-management_tool) in the 'Action Required' saved view.

## Steps

### Initial Setup

Follow the steps below when setting up workflows for the Document Management tool. Click to jump to a section:

1. Assign Workflow Permissions
2. Create a Document Management Workflow Template
3. Assign the Workflow to a Project
4. Configure a Workflow for the Project

#### Assign Workflow Permissions

For any users that will be part of an approval workflow, you'll need to assign [granular permissions](/faq-what-granular-permissions-are-available-for-document-management-workflows) for the Workflows tool in your permission templates.

[VIEW THE STEPS](/product-manuals/permissions-company/tutorials/create-a-company-permissions-template)

You can also customize the actions reviewers can take on documents within an active workflow, such as who should be able to mark up documents.

#### Create a Document Management Workflow Template

*Note:* See [Workflows](/product-manuals/workflows-company/) for more resources on the Workflows tool.

1. Navigate to the Company level **Workflows** tool.
2. Add a new workflow with the **Document Management** tool selected.
3. Click **Create**.
4. Build your workflow template. See [Create a Custom Workflow Template](/process-guides/workflows-user-guide/create-a-workflow-template) for detailed steps.
5. When you're ready to publish the workflow, click **Save & Publish**.

#### Assign the Workflow to a Project

After the Document Management workflow template is created, you'll need to assign it to the projects that you want to use it on. Click the link in the 'Assigned Projects' column to assign it to one or more projects.

**VIEW THE STEPS**

##### Â Tip

If you assign the workflow to a template project, each time you use that template to create a new project, it will include the workflow's steps and user assignments. However, you can still review and modify the workflow assignments and days to complete as needed for that project.

#### Configure a Workflow for the Project

Before being able to use workflows in the Document Management tool, you'll need to configure the workflow for the project. If the project was created from a template project with a workflow assigned, it inherits that workflow's user assignments, but it's a good idea to review the assignments. Currently, you can only have one Default workflow set for documents in the project.

1. Navigate to the project's **Document Management** tool.
2. Click the **Configure Settings** icon.
3. Click the **Workflows** tab.
4. In the 'Document Workflows' section, click **Configure** on the workflow that you want to configure for the project.
5. Configure or review the following required workflow elements:

   - **Assign Workflow Manager**
   - **Assign Distribution Group**
   - **Assignee(s)** and **Days to Complete** for each step.

#### Edit a Workflow

If you need to modify the workflow template, visit one of these locations:

- [Configure Settings: Document Management](/product-manuals/document-management-project/tutorials/configure-settings-document-management) in the Document Management tool to modify the assignees or workflow manager of future or in-progress workflows.
- [Edit a Custom Workflow Template](/product-manuals/workflows-company/tutorials/edit-a-workflow-template) in the Workflows tool to make any modifications to the workflow template.

### Using Workflows on Documents

- Start a Workflow for Uploaded Documents
- Review and Respond to a Document in a Workflow

#### Start a Workflow for Uploaded Documents

Documents that require approval workflows will need a workflow selected in the 'Assigned Workflow' column. The workflows will begin at the first step. See [Start a Workflow in the Document Management Tool](/product-manuals/document-management-project/tutorials/start-a-workflow-in-the-document-management-tool).

*Note:* If you bulk submit documents together, reviewers will get a single email with all of the documents requiring their attention, rather than separate emails for individually submitted documents.

#### Review and Respond to a Document in a Workflow

When a workflow for a document starts, a Workflow Assignee can review the document, add markup if necessary, and respond in the workflow. Workflow assignees can mark up documents as necessary as part of the response.

##### DEMO

The image below demonstrates how to access a document that needs to be reviewed.*Note:* Instead of clicking the 'In Review' tab, find the document in one of the saved views within the 'In Review' collection in the main 'Documents' tab.