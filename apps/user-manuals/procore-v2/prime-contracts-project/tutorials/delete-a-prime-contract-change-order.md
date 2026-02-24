# Delete a Prime Contract Change Order

Source: https://v2.support.procore.com/product-manuals/prime-contracts-project/tutorials/delete-a-prime-contract-change-order

---

## Background

To remove a PCCO, you can click the red (x) icon on the line item. However, when the icon is grayed out and not available, it means the PCCO is associated with other items in Procore. The steps below show you how to remove associated items and then permanently delete a PCCO.

##### Â Important

Before you can perform a delete action, you must:

- Change the status of the PCCO from 'Approved' to another status as described below. If you want to change the status of multiple PCCOs, you must apply the status changes in reverse order from how they were approved. For example, if you approved the PPCOs in sequential order (001, 002, and 003), you will need to remove the 'Approved' status in reverse order (003, 002, 001).
- Unlink any Procore items associated with the PCCO. This may include Potential Change Orders (PCOs), Change Order Requests (CORs), and invoices as described in the Prerequisites below.

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permissions on the project's **Prime Contracts** tool.

## Prerequisites

- If the PCCO is linked to one (1) or more invoices, you must first delete all associated invoices.
- If the PCCO is linked to one (1) or more Prime PCOs or CORs, complete the steps in [Remove a Change Order from a Prime Contract](/product-manuals/prime-contracts-project/tutorials/remove-a-change-order-from-a-prime-contract).

## Steps

- Navigate to the Change Orders Tab
- Change the Status of the Prime Contract Change Order from 'Approved'
- Delete the Prime Contract Change Order

### Navigate to the Change Orders Tab

1. Navigate to the project's **Prime Contracts** tool.
2. Locate the prime contract to work with. Then click its **Number** link.
3. Click the **Change Orders** tab. Depending on the number of change order tiers configured for the tool, the following tables appears in the tab:

   - Prime Contract Change Orders
   - Potential Change Orders
   - Change Order Requests

### Change the Status of the Prime Contract Change Order from 'Approved'

##### Â Important

Before changing the status of multiple PCCOs from 'Approved' to another status, be aware that you must apply the status changes in reverse order from how they were approved. For example, if you approved the PPCOs in sequential order (001, 002, and 003), you will need to remove the 'Approved' status in reverse order (003, 002, 001).

1. In the **Prime Contract Change Orders** table, locate the 'Approved' PCCOs.
2. Click **View** to open the PCCO.
3. Click **Edit**.
4. In the **Status** drop-down list, change the status from 'Approved' to a different status.
5. Click **Save**.

##### Â Note

- If the PCCO is linked to one (1) or more Prime PCOs or CORs, complete the steps in Delete a Prime Contract Change Order (PCCO).