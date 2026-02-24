# What is the difference between Document Management attachments and attachments from other tools? - Procore

Source: https://support.procore.com/faq/what-is-the-difference-between-document-management-attachments-and-attachments-from-other-tools

---

## Answer

Procore accounts that use the [Document Management tool](https://support.procore.com/products/online/user-guide/project-level/document-management/tutorials/about-the-document-management-tool "About the Document Management Tool") have the option to attach Document Management files to items in [other tools](https://support.procore.com/faq/which-tools-can-attach-document-management-files "Which tools can attach Document Management files?"). Document Management files behave differently than attachments from other Procore tools because they are shared as reference links not traditional attachments. Explore these differences below:

- [Document Management Attachments are Reference Links](#Document_Management_Attachments_are_Reference_Links "What is the difference between Document Management attachments and attachments from other tools?")
- [Attaching Reference Links](#Attachment_Reference_Links_to_Documents "What is the difference between Document Management attachments and attachments from other tools?")
- [Attachment Permissions](#Document_Attachment_Permissions "What is the difference between Document Management attachments and attachments from other tools?")
- [Attachment Access Requires Authentication and Authorization](#Document_Attachments_Require_Authentication_and_Authorization "What is the difference between Document Management attachments and attachments from other tools?")
- [Bulk Downloading Attachments](#Bulk_Downloading_Document_Attachments "What is the difference between Document Management attachments and attachments from other tools?")

### Document Management Attachments are Reference Links

Document Management attachments are references to the source document in the Document Management tool and are notpoint-in-time *copies* of the source document. This ensures viewers of the "attachment" see the most up-to-date and complete information relating to that document, including attributes, markups, workflows, change history, access history, and references to other Procore items the document is also attached to. References also ensure that users are downloading the source document from the Document Management tool.

### Attaching Reference Links

When choosing which document to attach from the Document Management tool, you'll see a table of files and their attributes, similar to the table in the Document Management tool. You have the following features and restrictions when searching and selecting these files:

- Filter by keyword or attributes, sort, and reorder the table of documents to find what you're looking for.
- Toggle between viewing only the latest revisions or all revision of documents if you want to attach a previous revision. See more about [the revision toggle](https://support.procore.com/products/online/user-guide/project-level/document-management/tutorials/search-for-and-filter-documents-in-the-document-management-tool#Filter_Documents "Search for and Filter Documents in the Document Management Tool").
- Select documents across multiple pages of the table.
 - The total number of selected files shows at the bottom of the window, and just like other tools allow, you can select files from multiple tools at the same time.
- Attach only specific versions of documents you have access to in the Document Management tool.
- After clicking 'Attach' or 'Cancel', your selections do not persist if you open the 'Attach Files' window again.

### Attachment Permissions

Document Management attachments respect permissions configured in the Document Management tool. A user *without* permission to an attachment sees a lock icon and cannot view or download the document. Document Management admins can add a user to a permission group within the Document Management tool so the user can view and download the document. See [View and Manage Document Permissions](https://support.procore.com/products/online/user-guide/project-level/document-management/tutorials/view-and-manage-document-permissions-for-the-document-management-tool) for more information.

### Attachment Access Requires Authentication and Authorization

When reference links to Document Management files are included in emails and PDF exports, recipients of those emails and PDF exports are required to log into Procore *and* have permission to the document in the Document Management tool in order to view or download the document.

### Bulk Downloading Attachments

When you click the 'Download All' button for Document Management attachments, zip file(s) are downloaded to your device. Depending on what tool the attachments came from, one of the following scenarios occurs:

- 1 zip file if only Document Management files are attached.
- 1 zip file if no Document Management files are attached.
- 2 zip files if both Document Management files and files from other tools are attached. These zip files have (1 of 2) and (2 of 2) appended to the zip file name.

See Also

- [Which tools can attach Document Management files?](https://support.procore.com/faq/which-tools-can-attach-document-management-files "Which tools can attach Document Management files?")
- [About the Document Management Tool](https://support.procore.com/products/online/user-guide/project-level/document-management/tutorials/about-the-document-management-tool "About the Document Management Tool")
- [Edit an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/edit-an-rfi "Edit an RFI")