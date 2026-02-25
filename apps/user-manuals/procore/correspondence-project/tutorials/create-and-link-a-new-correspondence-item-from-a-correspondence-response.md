# Create and Link a New Correspondence Item from a Correspondence Response

Source: https://v2.support.procore.com/product-manuals/correspondence-project/tutorials/create-and-link-a-new-correspondence-item-from-a-correspondence-response

---

## Things to Consider

- **Required User Permissions:**

 - 'Read Only' or 'Standard' level permissions on the correspondence type used to create the new item with the ['Create Item' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permissions template. 
    OR
 - 'Admin' level permissions on the correspondence type used to create the new item.
- **Additional Information:**

 - Some information from the source correspondence item is automatically included when a new correspondence item is created from its response.
 - Correspondence items created from responses on 'Private' correspondence items are not automatically set as 'Private'.

## Prerequisites

[Respond to a Correspondence Item](/product-manuals/correspondence-project/tutorials/respond-to-a-correspondence-item)

## Steps

1. Navigate to the project's **Correspondence** tool.
2. Click the **List** tab.
3. Click the **Number** next to the correspondence item with the response you want to create and link a new correspondence item to.
4. In the **Activity** section, locate the response you want to create and link a new correspondence item to.
5. Click **Link** and select '**Create & Link New Item'**.
6. Select the correspondence type from the 'Correspondence Types' section of the list.   
   You are redirected to the **New [Correspondence Type]** page for your new correspondence item. 
   These fields automatically include the following information:

   - The **Subject** field includes the source correspondence item number and the source response number.
   - The **Assignee** field includes the person who posted the source response.
   - The **Description** field includes the source response number, the name of the person who posted the source response, the timestamp of the source response, and the full text of the source response.

     ##### Â Note

     If the correspondence type used for the new correspondence item has a **Default Description** configured (see [Configure Advanced Settings: Correspondence](/product-manuals/correspondence-project/tutorials/configure-advanced-settings-correspondence)), the new correspondence item's **Description** will match the correspondence type's **Default Description** instead of the additional information from the source response.

- **Attachments** uploaded in the source response are included as attachments to this new correspondence item. The attachment maximum for each correspondence item is 2,500 files. Attachments included in future Responses to this new correspondence item do not count toward this maximum.
- *Optional:* Update the information in the **Subject**, **Assignee**, and **Description** fields as necessary.
- Finish creating the correspondence item. See [Create a Correspondence Item](/product-manuals/correspondence-project/tutorials/create-a-correspondence-item). 
 The **Links** section is visible when viewing the newly created correspondence item and includes a link to the source correspondence item. The **Links** section on the source correspondence item includes a link to the new correspondence item.