# Create and Link an RFI, Change Event, or a Different Correspondence Item to an Existing Correspondence Item

Source: https://v2.support.procore.com/product-manuals/correspondence-project/tutorials/create-an-link-an-rfi-change-event-or-a-different-correspondence-item-to-an-existing-correspondence-item

---

## Background

Correspondence items are often used as precursor business processes to an RFI, Change Event, or a different correspondence type. A common example of this is where an NOD (Notification of Delay) is approved and converted into an EOT (Extension of Time) to extend the project duration. The **Create & Link** **New Item** action on correspondence items enables users to quickly create new items, carry over any essential information and attachments from the originating correspondence item, and then link the items so users can easily reference the origin event as well as any other business processes linked to an individual correspondence item.

## Things to Consider

- **Required User Permissions:**

 - *To create and link a 'Draft' RFI:*

    - 'Read Only' level permissions or higher on the source item's correspondence type *with* 'Create Item' granular permission *and* 'Standard' level permissions or higher on the project's RFIs tool.
 - *To create and link an 'Open' or 'Closed' RFI:*

    - 'Read Only' level permissions or higher on the source item's correspondence type *with* 'Create Item' granular permission *and* 'Admin' level permissions on the project's RFIs tool. 
      OR
    - 'Read Only' level permissions or higher on the source item's correspondence type *with* 'Create Item' granular permission *and* 'Standard' level permissions on the project's RFIs tool *with* the 'Act as RFI Manager' granular permission enabled on your permissions template.
 - *To create and link a change event:*

    - 'Read Only' level permissions or higher on the source item's correspondence type *and* 'Standard' level permissions or higher on the project's Change Events tool.
 - *To create and link a correspondence item:*

    - 'Read Only' level permissions or higher on the source item's correspondence type *and* 'Read Only' level permissions on the new item's correspondence type *with* the 'Create Item' granular permission enabled on your permissions template. 
      OR
    - 'Read Only' level permissions or higher on the source item's correspondence type *and* 'Standard' level permissions or higher on the new item's correspondence type.
- Once an item is linked to a correspondence item, this action cannot be undone.

## Steps

- Create and Link an RFI
- Create and Link a Change Event
- Create and Link a Correspondence Item

### Create and Link an RFI

1. Navigate to the project's **Correspondence** tool.
2. Click the **List** tab.
3. Click the **Number** next to the correspondence item that you want to create and link an RFI to.
4. Click **Link**
5. Select **Create & Link New Item**
6. Select **RFI**. 
   You are redirected to the **New RFI** page. 
   The following fields automatically include the following information:

   - The **Location** field matches the **Location** field from the source correspondence item.
   - The **Question** field matches the **Description** field from the source correspondence item.
   - The **Attachments** includes attachments that were uploaded to the source correspondence item (not including attachments added to any responses in the correspondence item's **Activity** section).
7. *Optional:* Update the information in the **Location**, **Question**, and **Attachments** fields as necessary.
8. Finish creating the RFI. See [Create an RFI](/product-manuals/rfi-project/tutorials/create-an-rfi) for more information. 
   After the RFI is created, the **Links** section is added to the source correspondence with a link to the RFI.

### Create and Link a Change Event

1. Navigate to the project's **Correspondence** tool.
2. Click the **List** tab.
3. Click the **Number** next to the correspondence item that you want to create and link a change event to.
4. Click **Link**
5. Select **Create & Link New Item**
6. Select **Change Event**. 
   You are redirected to the **New Change Event** page. 
   The following fields automatically include the following information:

   - The **Origin** field includes the source correspondence item's **Number** and **Subject**.
   - The **Title** field matches the **Subject** field from the source correspondence item.
   - The **Description** field matches the **Description** field from the source correspondence item.
   - The **Attachments** includes attachments that were uploaded to the source correspondence item (not including attachments added to any responses in the correspondence item's **Activity** section).
7. *Optional:* Update the information in the **Origin**, **Title**, **Description**, and **Attachments** fields as necessary.
8. Finish creating the change event. See [Create a Change Event](/product-manuals/change-events-project/tutorials/create-a-change-event) for more information. 
   After the change event is created, the **Links** section is added to the source correspondence with a link to the change event.

### Create and Link a Correspondence Item

1. Navigate to the project's **Correspondence** tool.
2. Click the **List** tab.
3. Click the **Number** next to the correspondence item that you want to create and link another correspondence item to.
4. Click **Link**
5. Select **Create & Link New Item**
6. Select the correspondence type you want to use. 
   You are redirected to the **New [Correspondence Type]** page. 
   The following fields automatically include the following information:

   - The **Subject** field matches the **Subject** field from the source correspondence item.
   - The **Assignees** field matches the **Assignees** field from the source correspondence item.
   - The **Location** field matches the **Location** field from the source correspondence item.
   - The **Received From** field matches the **Received From** field from the source correspondence item.
   - The **Distribution** field matches the **Distribution** field from the source correspondence item.
   - The **Description** field matches the **Description** field from the source correspondence item.

     ##### Â Note

     If the correspondence type used for the new correspondence item has a **Default Description** configured (see [Configure Advanced Settings: Correspondence](/product-manuals/correspondence-project/tutorials/configure-advanced-settings-correspondence)), the new correspondence item's **Description** will match the correspondence type's **Default Description** instead of the **Description** from the source correspondence item.

- **Attachments** uploaded in the source correspondence item are included as attachments to this new correspondence. However, attachments added to any Responses in the source correspondence item's **Activity** section are not included. The attachment maximum for each correspondence item is 2,500 attached files.

 ##### Â Note

 If the same custom fields were added to the configurable fieldsets for the correspondence types used for the source correspondence item and the new correspondence item (or if the correspondence items use the same configurable fieldset with custom fields), the custom fields and their data from the source correspondence item will be added to the new correspondence item.

- *Optional:* Update the information in the **Subject**, **Assignees**, **Location**, **Received From**, **Distribution**, **Description**, and **Attachments** fields as necessary.
- Finish creating the correspondence item. See [Create a Correspondence Item](/product-manuals/correspondence-project/tutorials/create-a-correspondence-item) for more information. 
 After the new correspondence item is created, the **Links** section is added to the origin (source) correspondence with a link to the new correspondence item. The **Links** section is also added to the new correspondence item with a link to the origin correspondence.

*Note*:

- **Existing Items (Origin Tool):** When you link an existing item, it appears in the top section. You can 'edit' or 'unlink' these at any time.
- **New Items (Tool):** When you use 'Create and Link,' the link appears in the bottom section. This action is permanent; once created, these items cannot be unlinked or edited.