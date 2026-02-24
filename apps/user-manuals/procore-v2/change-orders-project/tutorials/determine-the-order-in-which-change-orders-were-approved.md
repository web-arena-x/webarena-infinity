# Determine the Order in Which Change Orders were Approved

Source: https://v2.support.procore.com/product-manuals/change-orders-project/tutorials/determine-the-order-in-which-change-orders-were-approved

---

## Background

If you need to delete a change order after it is placed in the 'Approved' status, you must remove the 'Approved' status from all 'Approved' change orders that have been approved since that particular change order. To do this, find the most recently approved change order. Then, update each change order's status to 'Draft' working backward until you locate the change order that you want to edit.

##### Example

If you approved change orders in this order: 001, 002, 003

You must remove the 'Approved' status from change orders in reverse order: 003, 002, 001.

## Steps

1. Navigate to the **Client Contracts**, **Commitments**, **Funding**, or **Prime Contracts** tool.
2. Locate the item to work with and click its **Number** link to open it.
3. In the item, click the **Change Orders** tab.
4. Locate the change orders in the 'Approved' status.
5. Open each change order.

   ##### Â Tip

   **Want to view all the 'Approved' change orders in separate browser tabs?** This lets you compare the change orders tab-by-tab. To do this, right-click the **View** button and choose **Open Link in New Tab**.

- Locate the last approved change order by looking at the labels next to the 'Status' field and finding the one labeled 'Approved' in ORANGE.
- Change the status of the last approved change order by clicking the ORANGE 'Approved' label and choosing any other status.
- Refresh the open browser tabs. Then, repeat the steps above to locate the last approved change order.
- Repeat the steps above until you reach the change order that you want to edit or delete.