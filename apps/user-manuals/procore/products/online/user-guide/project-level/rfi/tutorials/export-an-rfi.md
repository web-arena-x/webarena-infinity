# Export an RFI - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/export-an-rfi

---

## Objective

To export an RFI.

## Background

Individual RFIs can be exported in two ways: from the list on the **Items** tab (PDF summary only) or from the RFI's **General**tab (with options for which type of response and which attachments to include). To export all of a project's RFIs as a CSV or PDF, see [Export the RFIs List to CSV or PDF](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/export-rfis "Export the RFIs List to CSV or PDF").

## Things to Consider

- **Required User Permissions:**
 - 'Read Only' level permissions or higher on the project's RFIs tool.
- **Additional Information:**
 - If the 'Only Show Official Responses to Standard and Read-Only Users' checkbox is marked (see [Configure Settings: RFIs](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/configure-advanced-settings-rfis "Configure Settings: RFIs")):
    - RFI exports done by a user with 'Read Only' or 'Standard' level permissions on the project's RFIs tool can only include responses marked as 'Official' unless the user is the RFI's creator with the ['Act as RFI Manager' granular permission](../../../company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#RFIs "Grant Granular Permissions in a Project Permissions Template") ('Standard' only), the RFI Manager, an Assignee, or Distribution List member on the RFI.
 - If the 'Only Show Official Responses to Standard and Read-Only Users' checkbox is cleared:
    - RFI exports done by users with 'Read Only' level permissions or higher on the project's RFIs tool can either include all responses or only responses marked as 'Official'.

## Steps

- [View and Download a PDF Summary of an RFI from the Items Tab](#View_and_Download_a_PDF_Summary_of_an_RFI_from_the_Items_Tab "Export an RFI to PDF"): This method only includes the PDF summary of the RFI with links to download any attachments separately.
- [Export an RFI with Response and Attachment Options](#Export_an_RFI_with_Response_and_Attachment_Options "Export an RFI to PDF"): This method includes the PDF summary of the RFI, with additional options for which type of response and which attachments to include in the export.

### View and Download a PDF Summary of an RFI from the Items Tab

1. Navigate to the project's **RFIs** tool.
2. Locate the RFI you want to view the PDF summary for and click the page icon at the end of its row. 
     
   ![pdf-icon2.png](https://support.procore.com/@api/deki/files/73290/export-rfi-to-pdf.png?revision=2) 
     
   The system opens the RFI in a separate browser window.
3. If you want to download the PDF to your computer, click the **Download** icon in the top right corner of the page.

### Export an RFI with Response and Attachment Options

1. Navigate to the project's **RFIs** tool.
2. Click **View** next to the RFI you want to export.
3. Click **Export**.
4. Select **All Responses** to include all responses to the RFI. 
   OR Select **Official Responses Only**to only include responses marked 'Official'.
5. Mark the **Attachments** checkbox to include all attachments in the export. 
   OR Mark the checkbox next to the name of one or more attachments to include them in the export.
6. Rearrange the attachments by clicking the vertical grip (⋮⋮) icons and using a drag-and-drop operation.
7. Click **zip** to export a summary of the RFI's information and any attachments you selected as separate files in a .zip folder.
8. Click **PDF** to export a summary of the RFI's information in one PDF file, along with any attachments you selected. 
   *Note:* This option is only available if all attachments selected are PDF files.

A "Success" banner displays to confirm the export has started. If you clicked **PDF** and did not select any attachments to include, the file will automatically open in your web browser. If you clicked **zip** or you clicked **PDF** and selected one or more attachments to include, the system will send you an email when the export is complete with a link for you to download the file.

## See Also

- [Export the RFIs List to CSV or PDF](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/export-rfis "Export RFIs")

## 

If you would like to learn more about Procore's RFI software and how it can help your business, please visit our [request for information (RFI) construction software product page ![icon-external-link.png](https://support.procore.com/@api/deki/files/186764/icon-external-link.png?revision=2&size=bestfit&width=14&height=14)](https://www.procore.com/project-management/rfis "https://www.procore.com/project-management/rfis").