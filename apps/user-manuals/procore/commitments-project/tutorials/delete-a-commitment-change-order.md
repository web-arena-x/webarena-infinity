# Delete a Commitment Change Order

Source: https://v2.support.procore.com/product-manuals/commitments-project/tutorials/delete-a-commitment-change-order

---

## Background

To remove a Commitment Change Order, you can click the red (x) icon on the line item. However, when the icon is grayed out and not available, it means the change order is associated with other items in Procore. The steps below show you how to remove associated items and then permanently delete a PCCO.

##### Â Important

Before you can perform a delete action, you must:

- Change the status of the change order from 'Approved' to another status as described below. If you want to change the status of multiple change orders, you must apply the status changes in reverse order from how they were approved. For example, if you approved the change orders in sequential order (001, 002, and 003), you will need to remove the 'Approved' status in reverse order (003, 002, 001).
- Unlink any Procore items associated with the change order. This may include Potential Change Orders (PCOs), Change Order Requests (CORs), and invoices as described in the Prerequisites below.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the project's Commitments tool.

## Prerequisites

- If the Commitment Change Order is linked to one (1) or more invoices, you must first delete all associated invoices.
- If the Commitment Change Order is linked to one (1) or more Commitment PCOs or CORs, you must first remove them from the change order.

## Steps

- Navigate to the Change Orders Tab
- Change the Status of the Commitment Change Order from 'Approved'
- Delete the Commitment Change Order

### Navigate to the Change Orders Tab

1. Navigate to the project's **Commitments** tool.
2. Locate the commitment to work with. Then click its **Number** link.
3. Click the **Change Orders** tab. Depending on the number of change order tiers configured for the tool, the following tables appears in the tab:

   - Commitment Change Orders
   - Potential Change Orders
   - Change Order Requests

### Change the Status of the Commitment Change Order from 'Approved'

1. In the **Commitment Change Orders** table, locate the 'Approved' change orders.
2. Click **View** to open the change order.
3. Click **Edit**.
4. In the **Status** drop-down list, change the status from 'Approved' to a different status.
5. Click **Save**.

### Delete the Commitment Change Order

1. Click the **Change Orders** tab.
2. In the Commitment Change Orders section, locate the change order to remove.
3. In the confirmation dialog box that appears, click **OK** to confirm the removal action for the selected change order.