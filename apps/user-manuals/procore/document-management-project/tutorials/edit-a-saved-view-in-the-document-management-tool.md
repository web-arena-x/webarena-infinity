# Edit a Saved View in the Document Management Tool

Source: https://v2.support.procore.com/product-manuals/document-management-project/tutorials/edit-a-saved-view-in-the-document-management-tool

---

##### Regional availability

The Document Management tool is available in select countries. It is not yet available for Procore accounts in the U.S. To learn more, please reach out to your Procore point of contact.

## Backgroundâ

A *saved view* is a saved set of search filters for quick access to documents in the Document Management tool. Saved views visually organize your documents while also meeting the needs of a particular context, such as the saved view 'Published Electrical Drawings' for electricians who only want to see the latest approved versions of a specific document type. Unlike traditional folders, saved views don't require users to specify an upload location; they automatically absorb past, present, and future revisions of the same document.

Admins can create saved views for everyone on the project, and individual users can create saved views that are only visible to them. Each saved view is kept inside a collection, which is a parent category with its own set of filters determined by project Admins.

A collection's filters affect which filters can be chosen for any saved view within it. For example, when building an 'Electrical' saved view within the 'In Review' collection, the collection already filters out all documents except those with the *IR-In Review* status\_,\_ so the saved view only needs to add the filter *E-Electrical* from the discipline drop-down menu. A user cannot add the *DR-Draft* status because the 'In Review' collection excludes those. In other words, collections and saved views have a parent-child relationship. Saved views (children) adopt the filters of their collection (parent).

## Things to Consider

- **Required User Permissions:**

 - *To edit your own saved view,* 'Standard' or 'Admin' level permissions to the Document Management tool
 - *To edit a project saved view,* 'Admin' level permissions to the Document Management tool.
- **Additional Information**:

 - Saved views that were created for âEveryone in the Projectâ can't be changed to personal views.

## Steps

1. Navigate to the project's **Document Management** tool.
2. Make sure you're in the **Documents** tab.
3. In the Saved Views panel, click the view that you want to update.   
   *Note:* If the Saved View panels is hidden, click the **Show Saved Views** icon at the top of the table.
4. The following actions are available:

   - Update Saved View Filters
   - Update Saved View Columns
   - Edit the Name or Description of a Saved View

### Update Saved View Filters

Follow the steps below if you want to make changes to the documents that show in a saved view you created. You can also modify the filters of a saved view an Admin created, but to save your new filters, you must create a new saved view.

1. Click the name of the saved view.
2. From the **More Filters** menu, add or remove filters to change which documents show in the view.

   - After a change is made, an 'Update' button appears next to the name of the saved view, and the 'Create' button becomes active in case you want to create a whole [new saved view](/product-manuals/document-management-project/tutorials/create-a-saved-view-in-the-document-management-tool) instead.
   - If you do not see the 'Update' button, the saved view was not created by you, and you cannot edit it.
   - See [Search for and Filter Documents](/product-manuals/document-management-project/tutorials/search-for-and-filter-documents-in-the-document-management-tool) to learn more about filtering, including where the Latest Revision/All Revision filter is located.
3. Click **Update** next to the name of the saved view. The changes are automatically applied to the saved view.

### Update Saved View Columns

You can save column preferences so they are part of a saved view. Make column changes and then click the 'Update' button that appears next to the saved view's name. You can save settings such as which columns are visible, their order, and whether any are pinned to the left or right. Follow detailed instructions, see [Configure Your View in the Document Management Tool](/product-manuals/document-management-project/tutorials/configure-your-view-in-the-document-mangement-tool).

### Edit the Name or Description of a Saved View

Follow the steps below if you want to make changes to the name or description of a saved view. You can also change a saved view to be visible to everyone on the project if you have 'Admin' permissions to the Document Management tool.

1. In the 'Saved Views' section, click the **vertical ellipsis** icon next to the saved view you want to edit details for. 
   *Note:* You must be the creator of the saved view or an Admin on the project to see this icon and edit a saved view's details.
2. Click **Edit name and description**.   
    This opens the 'Update Saved View' window.
3. Update the Name and Description fields as necessary.   
   *Note:* If you have 'Admin' permissions to the Document Management tool, you can also choose to change your personal saved view to one that everyone on the project can see by selecting 'Everyone in the Project' in the 'View Access' field. However, project views can't be changed back to personal views.
4. Click **Update**.