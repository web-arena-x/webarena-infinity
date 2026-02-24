# How are PDFs uploaded to the Submittals tool affected by file restrictions? - Procore

Source: https://support.procore.com/faq/how-are-pdfs-uploaded-to-the-submittals-tool-affected-by-file-restrictions

---

## Answer

Restricted PDF files (also known as locked files) uploaded to the project's Submittals tool function differently than files without security restrictions. When a restricted file is uploaded to a submittal (either when creating or updating the submittal or when responding to the submittal), its functionality may be limited within Procore depending on what security restrictions are on the file.

- If a PDF has viewing restrictions and requires a password to open it, the file cannot be opened or viewed within any tool in the Procore web application.
- If a PDF has copying or editing restrictions, markups (including stamps) and pages in the project's Submittals tool cannot be added to the file. Because these files restrict alterations, adding markups to them within Procore would prevent them from being downloaded or distributed from Procore.

We recommend only uploading files without any security restrictions to Procore to ensure the full functionality of the file in Procore.

### How to Tell if Your PDF Has Copying or Editing Restrictions

If you attach a PDF from your local computer (by dragging and dropping the file into Procore or by clicking **Attach Files**) when responding to a submittal in Procore, Procore checks the PDF for security restrictions.

##### Note

Procore does not check PDF security restrictions when:

- PDFs are uploaded to a submittal's General Information section when creating or editing a submittal.
- PDFs are attached to a submittal response from the Project level Documents tool.

In order to be sure a PDF is not restricted, we recommend that all submittal attachments are uploaded in the Submittal Workflow and from your local computer.

If the PDF has copying or editing restrictions, a warning displays to indicate which file is restricted. You can choose to cancel attaching the file or to proceed. 
 
![submittals-attach-restricted-file.png](https://support.procore.com/@api/deki/files/188663/submittals-attach-restricted-file.png?revision=3) 
 
If you choose to attach a restricted PDF file, markups (including stamps) and pages cannot be added when reviewing that file in Procore. In the PDF Viewer, the file's information panel also indicates if the file has security restrictions that prevent markups and pages from being added to the file in Procore. 
 
![submittals-pdf-viewer-file-restrictions.png](https://support.procore.com/@api/deki/files/202413/submittals-pdf-viewer-file-restrictions.png?revision=2)

##### Important

If a PDF was uploaded to a submittal's General Information when creating or editing a submittal OR was attached to a submittal response from the Project level Documents tool, the submittal PDF viewer may not immediately recognize if the file has security restrictions the first time the file is opened in Procore. Refresh the page or close and reopen the file if you are unsure if the file has security restrictions.

### What to Do if a Restricted File has Existing Markups in Procore

PDF files with these security restrictions cannot be downloaded or distributed from the Submittals tool when one or both of the following statements is true:

- A blank page or a cover page was added to the file in Procore.
- Markup or stamps were added to the file in Procore.

If markups (including stamps) or pages have been added to a restricted PDF in Procore:

- A banner displays in the viewer indicating that the file cannot be downloaded or distributed until any markups or pages added are removed. 
    
 ![submittals-pdf-viewer-restricted-file-banner.png](https://support.procore.com/@api/deki/files/202414/submittals-pdf-viewer-restricted-file-banner.png?revision=2)
- A lock icon displays next to the file name in the Submittal Workflow table. 
    
 ![submittals-submittal-workflow-restricted-file.png](https://support.procore.com/@api/deki/files/202415/submittals-submittal-workflow-restricted-file.png?revision=2)
- The download buttons for the file within the PDF viewer and on the submittal's page will be hidden.
- If 'Download All' is selected, the file is excluded from the download.

For these reasons, we recommend that you remove any markups or pages added in Procore if you see this banner so that the file can be downloaded or distributed.

Markups (including stamps) added in Procore can only be deleted by the user who added the markup by selecting the markup and pressing DELETE (SHIFT + DELETE on Mozilla Firefox) on their keyboard. Pages added in Procore can be deleted by users with 'Admin' level permissions on the project's Submittals tool when they have the current Ball In Court responsibility and there are no markups on the pages. See [Add or Remove a Blank Page or Cover Page](../products/online/user-guide/project-level/submittals/tutorials/review-submittal-pdf-attachments.md#Optional:_Add_or_Remove_a_Blank_Page_or_Cover_Page "Review Submittal PDF Attachments").

## See Also

- [Create a Submittal](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/create-a-submittal "Create a Submittal")
- [Upload and Submit a Submittal](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/upload-and-submit-a-submittal "Upload and Submit a Submittal")
- [Respond to a Submittal as an Approver](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/respond-to-a-submittal-as-an-approver "Respond to a Submittal as an Approver")
- [Review Submittal PDF Attachments](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/review-submittal-pdf-attachments "Review Submittal PDF Attachments")