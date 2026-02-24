# Upload Documents to the Document Management Tool

Source: https://v2.support.procore.com/product-manuals/document-management-project/tutorials/upload-documents-to-the-document-management-tool

---

##### Regional availability

The Document Management tool is available in select countries. It is not yet available for Procore accounts in the U.S. To learn more, please reach out to your Procore point of contact.

## Background

When you upload documents to the Document Management tool, Procore can recognize and populate document attributes with the use of machine learning, naming standards, and project settings. See [What are the different fields in the Document Management tool?](/faq-what-are-the-different-fields-in-the-document-management-tool) and [What data can Procore automatically populate when uploading files to the Document Management tool?](/faq-what-data-can-procore-automatically-populate-when-uploading-files-to-the-document-management-tool)

After documents have been uploaded and processed, you'll quickly fill out any remaining required fields on the 'Uploads' tab before the documents can be submitted to the project and visible from the 'Documents' tab. See [Submit Documents in the Document Management Tool](/product-manuals/document-management-project/tutorials/submit-documents-in-the-document-management-tool).

## Things to Consider

- **Required User Permissions:**

 - You must be part of a Document Management tool permission group that has the 'Upload New Files' permission enabled. See [How do permissions work in the Document Management tool?](/faq-how-do-permissions-work-in-the-document-management-tool) 
    *Note:* If you have 'Admin' level permissions to the Document Management tool, you can view all files that have been added to the 'Uploads' tab. Otherwise, you can only view the files that you have uploaded.
- **Additional Information**:

 - Folders cannot be uploaded to the Document Management tool.
 - Procore will scan and detect information based on document filenames and contents. See [What data can Procore automatically populate when uploading files to the Document Management tool?](/faq-what-data-can-procore-automatically-populate-when-uploading-files-to-the-document-management-tool)
 - Uploaded documents remain on the 'Uploads' tab until all required information has been completed and the documents have been submitted. See [Complete Document Information in the Document Management Tool](/product-manuals/document-management-project/tutorials/complete-information-for-documents-in-the-document-management-tool).
 - Upload requirements can be set and managed in the tool's Configure Settings page. See [Edit the Upload Requirements for the Document Management Tool](/product-manuals/document-management-project/tutorials/edit-upload-requirements-for-the-document-management-tool).
 - If you are uploading a restricted or locked PDF file, note that there may be limitations for the file in Procore. See [How are locked or restricted PDF files handled in the Document Management tool?](/faq-how-are-locked-or-restricted-pdf-files-handled-in-the-document-management-tool)
 - If a [workflow](/product-manuals/document-management-project/tutorials/about-workflows-in-the-document-management-tool) is applied to a document, the status field is not editable because the workflow controls the document's status.
 - You can *upload* the following file types to the Document Management tool, though Procore does not currently support viewing them within the Procore application:

    - .dxf (AutoCad Drawing Exchange Format)
    - .step, .stp (STEP)
    - .obj (Wavefront)
    - .glb, .gltf (GL Transmission Format)
    - .rvm (AVEVA)
    - .pts (point cloud)
    - .las, .laz (LIDAR)
    - .e57 (vendor-neutral for LIDAR/laser scan data)
    - .kof (typically Trimble/Topcon)

## Steps

##### Â Note

If you are uploading revisions of documents, Procore will identify revisions based off the Name and Format fields of existing documents. The value in the Revision field will automatically be updated with the next available character. See [What data can Procore automatically populate when uploading files to the Document Management tool?](/faq-what-data-can-procore-automatically-populate-when-uploading-files-to-the-document-management-tool)

1. Navigate to the project's **Document Management** tool.
2. Click **Upload**.
3. Select the files that you want to upload. 
   ***Tip!*** If you want to upload files in bulk, the following actions are available:

   - To select multiple files individually: Hold down the CONTROL key on your keyboard and click each file that you want to select.
   - To select a group of files at one time:

     1. Click the first file that you want to select.
     2. Hold down the SHIFT key on your keyboard and click the last file you want to select. 
         This selects all files in between the first and last file.
4. In your computer's file explorer window, click **Open** to confirm the upload. 
    The status of the upload is shown in an Uploads window at the bottom of the screen.

   - This window can be accessed from any tab and will remain open until you close it.
   - If you want to review a document in the viewer, you can hover over the **green check** icon in the Uploads window and click **Review**.
5. After documents have been uploaded, you can view them on the **Uploads** tab. 
    Documents are shown as 'Processing' in the 'Ready to Submit' column while the system detects and populates information. You can start to review and fill out information as needed from the table or viewer. The system will not override any information that you enter manually. 
   *Note:* If a [workflow](/product-manuals/document-management-project/tutorials/about-workflows-in-the-document-management-tool) is applied to a document, the status field is not editable because the workflow controls the document's status.