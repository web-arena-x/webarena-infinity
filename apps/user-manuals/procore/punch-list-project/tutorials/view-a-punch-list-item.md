# View Punch List Items

Source: https://v2.support.procore.com/product-manuals/punch-list-project/tutorials/view-a-punch-list-item

---

## Background

Punch items are project-specific and will be listed in the project's Punch List tool.

## Things to Consider

- **Required User Permissions:**

  - *To view non-private punch list items*, âRead Onlyâ and above on the projectâs Punch List tool.   
    *Note:* 'Standard' and 'Read Only' users can only view these items after they have been sent to the Assignee.
  - *To view private punch list items,* you must meet one of the following requirements:\*

    - Admin' on project's Punch List tool.
    - 'Standard' level users can view Private punch list items if you are:

      - The item's Creator.
      - An Assignee on the Punch List Item.
      - A member of the itemâs distribution list.
    - Granted permission to act as Punch Item Manager and you are listed as the Itemâs Punch Item Manager.

      - *To view private and non-private Punch List items assigned to colleagues within that user's same company:*
      - 'Read Only' or 'Standard' level permissions on the project's Punch List tool with the ['View Private Punch List Items Assigned to Users Within Same Company' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permissions template.
- **Additional Information:**

  - The Punch List default view is set to only show your open punch list items.

## Steps

1. Navigate to the project's **Punch List** tool.
2. Locate the punch item to work with and click **View**.
3. Click one of the following tabs:

   - [General](#steps)
   - [Comments](#steps)
   - [Related Items](#steps)
   - [Emails](#steps)
   - [Change History](#steps)

### General

This tab displays general information about the punch list item, including:

- **Item Information:** This section provides an overview of the punch list item's details.
- **Item Workflow:** This section displays the item's progress as well as the item's Creator, Punch Manager, and Ball in Court.
- **Assignee Responses:** This section logs all Assignee responses, comments, and attachments related to the item.
- **Activity:** This section provides a detailed historical record of all modifications made to the punch list item.

### Comments

View any comments associated with the punch list item. See [Add Comments to Punch List Items](/product-manuals/punch-list-project/tutorials/add-comments-to-punch-list-items).

### Related Items

View and add related items to the punch list item from the **Related Items** tab. If the related item is an item in Procore (observation, RFI, and so on.) you will be able to view the item and all its information by clicking on the link in the "Description" column. To add a related item, click **Edit**.

### Emails

Manage any emails related to this punch list item from this tab. Each punch list item has a unique email address (for example, [procore-1234abcd@procoretech.com](mailto:procore-1234abcd1234abcd1234abcd@procoretech.com)) that can be used to send an email from your personal email client into Procore. For example, you might have an email thread in your personal email account that should be logged in Procore. In such cases, you might want to import that thread into Procore by simply forwarding an email to the related punch list item's unique email address. See [Email Punch Items to Any User](/product-manuals/punch-list-project/tutorials/email-punch-items-to-any-user).

### Change History

This tab shows a history log that summarizes all of the changes made to the punch list item throughout its lifecycle. The full change history in the Change History tab is only visible to users with 'Admin' level permissions to the Punch List tool. 'Read-only' users can see how many changes were made to the tool, but they cannot view details about the actions performed.