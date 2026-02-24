# Create a Saved View in the Document Management Tool

Source: https://v2.support.procore.com/product-manuals/document-management-project/tutorials/create-a-saved-view-in-the-document-management-tool

---

##### Regional availability

The Document Management tool is available in select countries. It is not yet available for Procore accounts in the U.S. To learn more, please reach out to your Procore point of contact.

## Backgroundâ

A *saved view* is a saved set of search filters for quick access to documents in the Document Management tool. Saved views visually organize your documents while also meeting the needs of a particular context, such as the saved view 'Published Electrical Drawings' for electricians who only want to see the latest approved versions of a specific document type. Unlike traditional folders, saved views don't require users to specify an upload location; they automatically absorb past, present, and future revisions of the same document.

Admins can create saved views for everyone on the project, and individual users can create saved views that are only visible to them. Each saved view is kept inside a collection, which is a parent category with its own set of filters determined by project Admins.

Since saved views are created *within* [collections](/faq-what-is-a-collection-in-the-document-management-tool), a collection's filters affect which filters can be chosen for any saved view within it. For example, when building an 'Electrical' saved view within the 'In Review' collection, the collection already filters out all documents except those with the *IR-In Review* status, so the saved view only needs to add the filter *E-Electrical* from the discipline drop-down menu. A user cannot add the *DR-Draft* status because the 'In Review' collection excludes those. In other words, collections and saved views have a parent-child relationship. Saved views (children) adopt the filters of their collection (parent).

## Things to Consider

- **Required User Permissions:**

 - *To create a personal saved view that only you can see,* 'Standard' level or higher permissions to the project's Document Management tool.
 - *To create a saved view for everyone in the project,* 'Admin' level permission to the project's Document Management tool.
- **Additional Information**:

 - All saved views must be in a [collection](/faq-what-is-a-collection-in-the-document-management-tool).
 - The 'Create' button will not show until you apply at least one new filter to the list of documents.
 - A personal saved view (with 'Me' selected as the access level) can only be seen by the individual who created it.
 - Project saved views ('Everyone in the Project' access level) can't be changed to a personal view later. However, if you have 'Admin' permission to the tool, you can change a personal saved view to a project view later. See [Edit a Saved View in the Document Management Tool](/product-manuals/document-management-project/tutorials/edit-a-saved-view-in-the-document-management-tool).

## Steps

1. Navigate to the project's **Document Management** tool.
2. Make sure you're in the **Documents** tab.
3. In the Saved Views panel, click on a saved view listed under a bolded collection name. For example, click on 'All Published Documents' in the collection called 'Published.' *Note:* If the Saved View panels is hidden, click the **Show Saved Views** icon at the top of the table.
   *Tip:* To decide which collection's saved view to choose as a starting point, consider the filters it uses. Learn how to view a collection's filters using the info icon in this [collections](/faq-what-is-a-collection-in-the-document-management-tool) article.
4. Use the **Filters** menu to make at least one change to the filters in the current saved view. Consider these tips:

   - If you want only the latest revision of each document, click the **Latest Revision** button. Otherwise choose **All Revisions.**

     - 'Latest Revision' is context dependent. User permissions, the collection's filters, and how the [revisions are ordered](/product-manuals/document-management-project/tutorials/edit-revisions-in-the-document-management-tool) all intelligently affect which revision shows in the saved view.
   - If you want to add a filter that includes documents that the collection itself already filtered out, you need to find a more appropriate collection for your desired saved view.\* Find out what a collection's filters are by clicking the info icon.
5. *Optional:* Configure the columns in your new saved view by following the steps in [Configure Your View in the Document Management Tool](/product-manuals/document-management-project/tutorials/configure-your-view-in-the-document-mangement-tool). You can save preferences such as which columns are visible, the order they appear, and whether any are pinned to the left or right.
6. When you're ready to create the saved view, click **Create**. 
   *Note:* If the Create button is inactive, your filters are outside the parameters of the collection, or you have not yet selected filters that are different from the saved view you are in.
7. Fill out the following information: 
    Fields with an asterisk (\*) are required.

   - **Name\***: Enter a name for the saved view. This name will show in the Saved Views list.
   - **Description**: Enter a description for the saved view.
   - **View Access**: Select an access option for the saved view. 
     *Note:* Only users with 'Admin' permissions to the Document Management tool can create views for everyone in the project.

     - To create a personal saved view that only you can see, select **Me**.
     - To create a saved view that everyone on the project can see, select **Everyone in the Project**.
8. Click **Create**.   
    The new saved view is added to the Saved Views panel. Click the name of the saved view at any time to view the filtered list of documents.