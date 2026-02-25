# View a Correspondence Item

Source: https://v2.support.procore.com/product-manuals/correspondence-project/tutorials/view-a-correspondence-item

---

## Things to Consider

- **Required User Permissions:**

 - *To view a correspondence item not marked as 'Private':*

    - 'Read Only' level permissions or higher on the correspondence type. 
      *Note:* Users may require specific roles on a correspondence item (or granular permissions) to view the item depending on the item's status and privacy settings.

      **What user roles can view which types of correspondence items?** **Show/Hide**

      In the table below, the icon indicates which user roles can view a correspondence item based on its status and privacy settings, and the icon indicates which user roles cannot view a correspondence item based on its status and privacy settings.

      | | | | | | | | | | |
      | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
      | User Role | Correspondence Item Settings | | | | | | | | |
      | Draft | Draft and 'Private' | Draft and 'Super Private' | Open | Open 'Private' | Open and 'Super Private' | Closed | Closed and 'Private' | Closed and 'Super Private' | |
      | Creator | | | | | | | | | |
      | Assignee | | | | | | | | | |
      | Distribution List Member | | | | | | | | | |
      | Received From | | | | | | | | | |
      | No Role | | | | | 1 | 1 | | 1 | 1 |
      | Correspondence Type Admin | | | | | | 2 | | | 2 |

      1 Users with the ['View Private Items Accessible to Users within Same Company' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on their permissions template can view 'Open' or 'Closed' correspondence item marked 'Private' or 'Super Private' if another user in their company (including them) is the correspondence item's creator, an Assignee, a Distribution List member, or added in the Received From field on the item.

      2 Users with 'Admin' level permissions on the correspondence type can view 'Super Private' correspondence items ('Open' or 'Closed') if they are (or another user in their company is) the correspondence item's creator, an Assignee, a Distribution List member, or added in the Received From field on the item.
- **Additional Information:**

 - Some image attachments may include the option to view them in a map view based on the files' GPS coordinates. See [Which Procore tools let me view digital image attachments in a map view?](/faq-which-procore-tools-let-me-view-a-digital-image-attachment-in-a-map-view)

## Steps

1. Navigate to the project's **Correspondence** tool.
2. Click the **Number** link for the correspondence item you want to view.
3. Click the tab with the information you want to view:

   - **General tab:** Shows the correspondence item's **General Information**, **Links**, and **Activity** sections.

     - The Links section provides links to the following:

       - Items that were added to the correspondence item's Origin Correspondence, Origin RFI, and Schedule Tasks fields.
       - Correspondence items, RFIs, and change events that were created from the correspondence item. See [Create and Link an RFI, Change Event, or a Different Correspondence Item to an Existing Correspondence Item](/product-manuals/correspondence-project/tutorials/create-an-link-an-rfi-change-event-or-a-different-correspondence-item-to-an-existing-correspondence-item).
       - Drawings that the correspondence item was linked to. See [Link a Correspondence Item on a Drawing](/product-manuals/correspondence-project/tutorials/link-a-correspondence-item-on-a-drawing).
   - **Related Items tab:** View or link related items and notes to the correspondence item. See [Add a Related Item to a Correspondence Item](/product-manuals/correspondence-project/tutorials/add-a-related-item-to-a-correspondence-item).
   - **Emails tab:** View, reply to, and send emails connected to and summarizing this particular correspondence item.

     - Emails connected with the correspondence item you are viewing show up here. Click on an email to see more details and access the **Reply** button. 
       To return to the main screen of the Emails tab, click the **All Emails** subtab.
     - To create a new email about the correspondence item, click **Compose Email**. See [Forward a Correspondence Item by](/product-manuals/correspondence-project/tutorials/forward-a-correspondence-item-by-email) [Email](/product-manuals/correspondence-project/tutorials/forward-a-correspondence-item-by-email).
   - **Change History tab:** This tab includes a summary of all of the changes made to the correspondence item throughout its lifecycle. Only users with 'Admin' level permissions on the correspondence type can access this tab.
   - **Permissions tab:** When the correspondence item is marked as 'Private', this tab includes a list of the users (along with their associated company) that have access to the correspondence item.