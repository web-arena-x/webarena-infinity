# Create a Correspondence Item from an RFI - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/create-a-correspondence-item-from-an-rfi

---

## Objective

To create a new correspondence item from an existing RFI.

## Things to Consider

- **Required User Permissions:**
  - 'Read Only' level permissions on the correspondence type with the ['Create Item' granular permission](../../../company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#Correspondence "Grant Granular Permissions in a Project Permissions Template") enabled on your permissions template and 'Read Only' level permissions or higher on the project's RFIs tool.  
    OR
  - 'Standard' level permissions or higher on the correspondence type and 'Read Only' level permissions or higher on the project's RFIs tool.

## Steps

1. Navigate to the project's **RFIs** tool.
2. Click the **Items** tab.
3. Click **View** next to the RFI that you want to create a correspondence item from.
4. Click the vertical ellipsis ![icon-ellipsis-vertical.png](https://support.procore.com/@api/deki/files/158014/icon-ellipsis-vertical.png?revision=2&size=bestfit&width=27&height=26) at the top of the page.
5. Click **Create Correspondence**and select a correspondence type.  
   The following fields automatically include the following information:
   - The **Subject** field matches the **Subject** of the source RFI.
   - The **Location** field matches **Location** from the source RFI.
   - The **Specification Section** field matches the **Spec Section** field from the source RFI.
   - The **Schedule Impact** field is based on the **Schedule Impact** field from the source RFI.  
     *Note:* If **Yes** was selected in the source RFI's **Schedule Impact** field, the data from the source RFI's **Days** field will display in the **Schedule Impact** field on the new correspondence item.
   - The **Cost Impact** field is based on the **Cost Impact** field from the source RFI.  
     *Note:*If **Yes** was selected in the source RFI's Cost Impact field, the data from the source RFI's **$** field will display in the **Cost Impact** field on the new correspondence item.
   - The **Cost Code** field matches the **Cost Code** from the source RFI.
   - The **Description** field includes the **Question** from the source RFI.
   - The **Attachments** field includes any attachments that were uploaded to the source RFI.
   - *Optional:* Update the information in the **Subject**, **Location**, **Specification Section**, **Schedule Impact**, **Cost Impact**, **Cost Code**, **Description**, and **Attachments** fields as necessary.
6. Finish creating the correspondence item. See [Create a Correspondence Item](https://support.procore.com/products/online/user-guide/project-level/correspondence/tutorials/create-a-correspondence-item "Create a Correspondence Item").  
   The **Links** section is visible when viewing the newly created correspondence item and includes a link to the source RFI.

## See Also

- [Create an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/create-an-rfi "Create an RFI")
- [Create a Correspondence Item](https://support.procore.com/products/online/user-guide/project-level/correspondence/tutorials/create-a-correspondence-item "Create a Correspondence Item")