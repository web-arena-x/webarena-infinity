# Create and Edit Collections

Source: https://v2.support.procore.com/product-manuals/document-management-project/tutorials/create-and-edit-collections

---

##### Regional availability

The Document Management tool is available in select countries. It is not yet available for Procore accounts in the U.S. To learn more, please reach out to your Procore point of contact.

## Background

A *collection* is a group of saved filters in the Saved Views panel of the Document Management tool. Collections keep saved searches organized so users can quickly find the document revision needed in their specific context. For example, admins can set up a collection for field users that automatically pulls in only the latest *published* version of each drawing for a specific location. Newer revisions of these drawings may exist, but field users should only work from approved (published) versions.

Procore automatically provides two document collections called 'In Review' and 'Published,' and project Admins can create additional collections using filters. Within a Collection, any user can create a saved view that narrows the search results even more. For example, an electrical engineer may want a saved view that shows only electrical drawings. By placing this saved view in the âPublishedâ collection, the engineer makes it easy to access a dynamic list of all the projectâs published electrical drawings.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions to the project's Document Management tool.
- Projects can have up to 10 custom collections.
- New projects automatically include the following collections and saved views, which do not count towards the project's maximum 10 custom collections:

 - **Published** 1 (collection)

    - All Published Documents 2 (saved view)
    - Drawings {3 (saved view)
    - Specifications 3 (saved view)
 - **In Review** 4 (collection)

    - All In Review Documents 4 (saved view)
    - Assigned to Me 4 (saved view)
    - Assigned to Company4 (saved view) 
      *Note:* This filters all documents that have the user or a user at their company listed as a Pending Assignee for that document revision.
 - All Documents 4 (saved view) - Located at the bottom of the Saved Views panel and lists all the project's documents with no filters applied. Saved views cannot be created from it.

1 Admins can rename it and change or add filters as needed but cannot delete or clone.

2 Cannot be deleted, cloned or renamed, and the filters are the ones chosen for the 'Published' collection.

3 Admins can add extra filters as needed but cannot delete, clone, or rename.

4 Cannot be deleted, renamed, or cloned, and the filters cannot be edited in any way.

See [Why can't I edit or delete certain saved views in the Document Management tool?](/faq-why-cant-i-delete-certain-saved-views-in-the-document-management-tool)

- The first collection in the Saved Views panel determines which saved view automatically opens when users open the Document Management tool. See Reorder Collections.

## Steps

##### Â NoteÂ Â

Settings for the **Document Management** tool can also be managed in the project's Admin tool. See [Configure Document Management Settings in the Admin Tool](/product-manuals/admin-project/tutorials/configure-document-management-settings-in-the-admin-tool-beta).

1. Navigate to the project's **Document Management** tool.
2. Click the **Configure Settings** icon.
3. Click the **Views** tab.
4. Choose from the following tasks:

   - Create a Collection
   - Reorder Collections

### Create a Collection

1. Click **Create Collection.**
2. Fill out the following fields to configure the Collection:

   - **Collection Name:** Give your Collection a name that communicates what types of documents users can find within it.
   - **Description:** This is visible when a user clicks the info icon next to the collection name in the breadcrumb above the document list.
   - **Default Display:** Set the default view for the collection--either all revisions of a document show in the list or just the latest revision. Each user can manually switch their view at any time when viewing a Collection. Viewing a document's revisions is also possible after clicking on the document.
   - **Icon:** Choose an icon to appear to the left of the Collection Name in the Saved Views panel.
   - **Select Attributes:** Choose an attribute category and then use the drop down to select which attributes (filters) you want applied to the Collection. 
      For example, if you want the Collection to only contain approved drawings in the pre-construction stage, select the following attributes:

     - Project Stage > Pre-Construction
     - Type > DR - Drawing
     - Status > AP - Approved

*Note:* If you select an attribute category but don't want to choose an attribute for it, you must delete the attribute category to create the Collection.

1. Click **Create**. 
   Your new Collection appears on your View Settings page and in the Saved Views panel in the Documents tab.

### Reorder Collections

1. Hover over the **grip** icon for the collection you want to move. 
    Your pointer will turn into a hand icon.
2. Click and drag the collection up or down to reorder. Release to drop the collection in its new place. 
   *Note:* The collection on top of this list determines what saved view automatically loads when users open the Document Management tool. In the tool, the first saved view in a collection is always the one with all of that collection's documents, and this is the saved view that automatically loads if that collection is listed first in the Admin's 'Views' settings page.