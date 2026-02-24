# Start a Workflow in the Document Management Tool

Source: https://v2.support.procore.com/product-manuals/document-management-project/tutorials/start-a-workflow-in-the-document-management-tool

---

##### Regional availability

The Document Management tool is available in select countries. It is not yet available for Procore accounts in the U.S. To learn more, please reach out to your Procore point of contact.

## Things to Consider

- **Required User Permissions:**

 - 'Standard' or 'Admin' level permissions to the Document Management tool. 
     AND
 - To start a workflow, you need one of the following permissions:

    - The ['Can Start Workflows' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) for Document Management Workflows is enabled on the project permission template. See [How do permissions work in the Document Management tool?](/faq-how-do-permissions-work-in-the-document-management-tool)\* 'Admin' level permissions to the Project level Directory tool.
    - 'Admin' level permissions to the Company level Workflows tool.
 - To restart a workflow, apply a different workflow template, or send items through an additional workflow, you need the following permission:\* 'Admin' level permissions to the Document Management tool.'
- If certain types of document errors arise, Project Admin can [resolve them](/faq-how-do-i-resolve-document-errors-in-the-document-management_tool) in the 'Action Required' saved view.

## Steps

1. Navigate to the project's **Document Management** tool.
2. The following options are available:

   - Start a workflow on uploaded documents
   - Apply a new workflow template to documents

### Start a workflow on uploaded documents

1. Upload documents if necessary. See [Upload Documents to the Document Management Tool](/product-manuals/document-management-project/tutorials/upload-documents-to-the-document-management-tool).
2. Click the **Uploads** tab.
3. Complete required fields for the documents. See [Complete Information for Documents in the Document Management Tool.](/product-manuals/document-management-project/tutorials/complete-information-for-documents-in-the-document-management-tool)
4. Click the **Assigned Workflow** drop-down menu to select a workflow for the documents.   
   *Tip!* You can assign a workflow to multiple documents using the bulk edit feature.
5. Click **Apply** if modifying from the 'Edit Document Attributes' panel.   
    This applies the workflow to the document(s), but does not start the workflow.
6. Click **Submit**. 
    This sends the documents to the first step of the workflow. Current Step Assignees will receive an email notification. 
   *Note:* The Submit button is not available for documents that are missing required fields. See Step 3.

### Apply a new workflow template to documents

Restart, reapply, or apply an additional workflow to a document or group of documents at any point in their lifecycle. Changes to a document's workflow become a time-stamped part of its workflow history.

1. Click the **Documents** tab.
2. Select one or more documents to apply a new workflow template to. 
    Note: If you select a document with a completed workflow, you can send it through an additional workflow approval process.
3. Click the **workflow** icon that appears at the top of the list.
4. Select **Apply New Workflow**.
5. Select the needed workflow template from the list.   
   *Note:* Selecting the same workflow template that is already applied to a document will restart the workflow for that document.
6. Click **Apply**.
7. Click **Apply** again after acknowledging that in-progress workflows will be terminated in order to apply the new workflow template.   
    This sends the documents to the first step of the newly applied workflow. Current Step Assignees will receive an email notification.
8. Navigate back to the **Documents** tab if you want to see the documents with the change applied.   
    Note: A document's current workflow is listed in the 'Assigned Workflow' column. Use the **table settings** to show this column, as needed.