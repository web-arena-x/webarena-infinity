# Manage Custom Statuses for Correspondence Types

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/manage-custom-statuses-for-correspondence-types

---

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the Company level Admin tool.

## Prerequisites

- [Create a New Correspondence Type](/product-manuals/admin-company/tutorials/create-a-new-correspondence-type)

## Steps

- Create a Custom Status
- Delete a Custom Status

### Create a Custom Status

1. Navigate to the Company level **Admin** tool.
2. Under **Tool Settings** in the sidebar, click **Correspondence**.
3. Click the **Statuses** tab.
4. Click **Add Status** and select the correspondence type that you want to add a custom status for.
5. In the **Create Custom Status** window, complete the following:

   - **Status Name:** Enter a name for the status.
   - **Map to Default Status:** Select the default status that your custom status is associated with. 
     *Note:* For customers with the Workflows tool, this allows the custom status to be used with certain workflow steps. See [Create a Custom Workflow Template](/process-guides/workflows-user-guide/create-a-workflow-template).
6. Click **Create**.

##### Â Note

- Statuses created for a correspondence type will be available on all of your company's projects that the correspondence type was added to.
- Email notifications are sent for all correspondence items until their status is changed to 'Closed'. See [Who receives correspondence item emails and push notifications?](/faq-who-receives-correspondence-item-emails-and-push-notifications)

### Delete a Custom Status

1. Navigate to the Company level **Admin** tool.
2. Under **Tool Settings** in the sidebar, click **Correspondence**.
3. Click the **Statuses** tab.
4. Click the arrow icon next to the correspondence type with the custom status that you want to delete.
5. Click the delete icon next to the custom status that you want to delete. 
   *Note:* Custom statuses that are in use by a correspondence item or correspondence workflow have a gray delete icon and cannot be deleted.
6. In the **Delete Status** window, review the information and then click **Delete**.