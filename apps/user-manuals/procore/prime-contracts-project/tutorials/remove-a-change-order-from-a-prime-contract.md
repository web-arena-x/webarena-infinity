# Remove a Change Order from a Prime Contract

Source: https://v2.support.procore.com/product-manuals/prime-contracts-project/tutorials/remove-a-change-order-from-a-prime-contract

---

## Background

Before you can remove a Prime Contract Change Order (PCCO) from Procore (as described in [Delete a Prime Contract Change Order](/product-manuals/prime-contracts-project/tutorials/delete-a-prime-contract-change-order)), you must use the Steps below to remove any PCOs or CORs linked to that PCCO.

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permissions on the project's Prime Contracts tool.

## Prerequisites

- Before changing the status of multiple PCCOs from 'Approved' to another status, be aware that you must apply the status changes in reverse order from how they were approved. For example, if you approved the PPCOs in sequential order (001, 002, and 003), you will need to unapproved them in reverse order (003, 002, 001).
- If any change orders have been added to your project's invoices, you must delete those invoices before you can use the steps below.

## Steps

- Navigate to the Change Orders Tab
- Change the Status of the Prime Contract Change Orders from 'Approved'
- Unlink Potential Change Orders and Change Order Requests
- Delete the Potential Change Orders and Change Order Requests

### Navigate to the Change Orders Tab

1. Navigate to the project's **Prime Contracts** tool.
2. Locate the prime contract to work with. Then click its **Number** link.
3. Click the **Change Orders** tab. Depending on the number of change order tiers configured for the tool, the following tables appears in the tab:

   - Prime Contract Change Orders
   - Potential Change Orders
   - Change Order Requests

### Change the Status of the Prime Contract Change Orders from 'Approved'

##### Â Important

Before changing the status of multiple PCCOs from 'Approved' to another status, be aware that you must apply the status changes in reverse order from how they were approved. For example, if you approved the PPCOs in sequential order (001, 002, and 003), you will need to remove the 'Approved' status in reverse order (003, 002, 001).

1. In the **Prime Contract Change Orders** table, locate the 'Approved' PCCOs.
2. Click **View** to open the PCCO.
3. Click **Edit**.
4. In the **Status** drop-down list, change the status from 'Approved' to a different status.
5. Click **Save**.

### Unlink the Potential Change Orders and Change Order Requests

1. Scroll to the **Potential Change Orders Included in this PCCO** section.
2. Locate the COR or PCO to work with. Then click **View**.
3. Click **Edit**.
4. Scroll to the **Prime Contract Change Order** drop-down list as shown below.
5. Choose **None**.
6. In the **Potential Change Orders** list, remove all of the existing PCOs from the list:
7. Click **Save**.

### Delete the Potential Change Orders and Change Order Requests

1. Return to the **Change Orders** tab.
2. Locate the PCO or COR to remove.
3. Click the red (X) next to each PCO or COR to remove.
4. In the confirmation dialog box that appears, click **OK** to confirm the removal action for the selected PCO or COR.

## Next Step

- [Delete a Prime Contract Change Order](/product-manuals/prime-contracts-project/tutorials/delete-a-prime-contract-change-order)