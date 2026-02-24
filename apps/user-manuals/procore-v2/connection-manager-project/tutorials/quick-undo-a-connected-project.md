# Quick Undo a Connected Project

Source: https://v2.support.procore.com/product-manuals/connection-manager-project/tutorials/quick-undo-a-connected-project

---

## Background

The Quick Undo feature for the Procore Connection Manager tool lets you immediately reverse accidental or mistaken connection creations.

- [Required User Permissions](/product-manuals/connection-manager-project/permissions)
- Both upstream and downstream users can utilize the quick undo feature.
- **Downstream Project:**

 - The undo button is active for 5 minutes after a project connection is initialized.
- **Upstream Project:**

 - The undo button is active for 5 minutes after a project connection request is approved.
 - When the Automatic Connection feature is enabled, only the downstream account can undo a connection.

##### Â Important

To use the Quick Undo feature, you must stay on the Connection Manager connection screen. Navigating away or refreshing the page will disable the undo option.

### Downstream Project

1. Navigate to the **Connection Manager** tool.
2. Create a connection.
3. While the project connection is being initialized, a banner will appear that says: **Connected to the wrong Company or Project?**
4. Click **Undo** to cancel the project connection request.
5. A **Please Confirm Connection Undo** window will pop up.

   - To cancel the undo, click **Cancel**.
   - To stop project data from being shared, click **Undo Connection**.

### Upstream Account

1. Navigate to the **Connection Manager** tool.
2. Approve an awaiting connection request.
3. A banner will appear that says: **Connected to the wrong Company or Project?**
4. Click **Undo** to cancel the project connection request.
5. A **Please Confirm Connection Undo** window will pop up.

   - To cancel the undo, click **Cancel**.
   - To stop project data from being shared, click **Undo Connection**.
6. The project status will revert to **Awaiting Approval**. From here, you can choose to either **Reject** or **Approve** the project again.