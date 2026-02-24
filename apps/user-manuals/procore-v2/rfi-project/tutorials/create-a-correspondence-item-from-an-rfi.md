# Create a Correspondence Item from an RFI

Source: https://v2.support.procore.com/product-manuals/rfi-project/tutorials/create-a-correspondence-item-from-an-rfi

---

## Things to Consider

- **Required User Permissions:**

  - 'Read Only' level permissions on the correspondence type with the ['Create Item' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permissions template and 'Read Only' level permissions or higher on the project's RFIs tool.  
     OR
  - 'Standard' level permissions or higher on the correspondence type and 'Read Only' level permissions or higher on the project's RFIs tool.

## Steps

1. Navigate to the project's **RFIs** tool.
2. Click the **Items** tab.
3. Click **View** next to the RFI that you want to create a correspondence item from.
4. Click the vertical ellipsis  at the top of the page.
5. Click **Create Correspondence** and select a correspondence type.  
    The following fields automatically include the following information:

   - The **Subject** field matches the **Subject** of the source RFI.
   - The **Location** field matches **Location** from the source RFI.
   - The **Specification Section** field matches the **Spec Section** field from the source RFI.
   - The **Schedule Impact** field is based on the **Schedule Impact** field from the source RFI.  
     *Note:* If **Yes** was selected in the source RFI's **Schedule Impact** field, the data from the source RFI's **Days** field will display in the **Schedule Impact** field on the new correspondence item.
   - The **Cost Impact** field is based on the **Cost Impact** field from the source RFI.  
     *Note:* If **Yes** was selected in the source RFI's Cost Impact field, the data from the source RFI's **$** field will display in the **Cost Impact** field on the new correspondence item.
   - The **Cost Code** field matches the **Cost Code** from the source RFI.
   - The **Description** field includes the **Question** from the source RFI.
   - The **Attachments** field includes any attachments that were uploaded to the source RFI.
   - *Optional:* Update the information in the **Subject**, **Location**, **Specification Section**, **Schedule Impact**, **Cost Impact**, **Cost Code**, **Description**, and **Attachments** fields as necessary.
6. Finish creating the correspondence item. See [Create a Correspondence Item](/product-manuals/correspondence-project/tutorials/create-a-correspondence-item).  
    The **Links** section is visible when viewing the newly created correspondence item and includes a link to the source RFI.