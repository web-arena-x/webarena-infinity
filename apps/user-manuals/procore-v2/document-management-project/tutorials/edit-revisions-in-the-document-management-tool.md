# Edit Revisions in the Document Management Tool

Source: https://v2.support.procore.com/product-manuals/document-management-project/tutorials/edit-revisions-in-the-document-management-tool

---

##### Regional availability

The Document Management tool is available in select countries. It is not yet available for Procore accounts in the U.S. To learn more, please reach out to your Procore point of contact.

## Background

In the Document Management tool, the Revision field is an editable and flexible way to track document revisions, while the Version field provides a more reliable historical record of a documentâs evolution since it is not editable. However, you can re-order document versions to change which file appears for users when their 'Latest Version' toggle is enabled by them or a Saved View filter.

This tutorial explains how to view and modify attributes of versions and their order.

## Things to Consider

- **Required User Permissions:**

 - 'Standard' or 'Admin' level permissions to the Document Management tool with the ['Edit Attributes' document permission](/faq-how-do-permissions-work-in-the-document-management-tool) enabled.   
    *Note:* You can only edit revisions for documents that you have access to. See [How do permissions work in the Document Management tool?](/faq-how-do-permissions-work-in-the-document-management-tool)

## Steps

1. Navigate to the project's **Document Management** tool.
2. Make sure you are in the **Documents** tab.
3. Click **See All** in the 'Version' or 'Revision' column next to the document that needs edits.
4. The following actions are available in the Versions panel:

   - Edit Attributes
   - Reorder Versions

### Edit Attributes

1. Click into the field that you want to edit and change the value. Editable fields include:

   - **Revision**: Edit the revision number or letter.
   - **Status**: Select a different status for the version.
   - **Date Authored**: Click to edit the date that the version was authored.
2. Click **Save**.

### Reorder Versions

1. Hover over the **grip** icon for the version that you want to move.
2. Click and drag the version up or down to reorder, and release to drop the version in its new place. 
    This automatically updates the order of the versions. The version on top of the list will show '(Latest in Collection)' after the version number to indicate that it is the most current version that fits the filters of that collection.

##### Â Note

Changing which version is the 'Latest in Collection' affects a user's list of documents anytime they enable the 'Latest Version' button or view a saved view with that filter enabled. Users can still [access other versions](/product-manuals/document-management-project/tutorials/view-documents-in-the-document-management-tool) intentionally, but if they click on the document's name, they view whatever version is set as 'Latest in Collection'.

See more about how [Procore decides the latest version](/faq-how-does-procore-decide-which-document-version-is-the-latest-in-the-document-management-tool).