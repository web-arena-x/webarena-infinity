# Move Coordination Issues to Observations

Source: https://v2.support.procore.com/product-manuals/coordination-issues-project/tutorials/move-coordination-issues-to-observations

---

## Background

Some design issues are best resolved on-site. The Move to Observation feature creates a seamless handoff for these items to field teams. Rather than closing an issue and risking it might be forgotten, this function formally transfers it by closing the original coordination issue and creating a linked observation in the Observations tool. You can also move multiple coordination issues in bulk. This improves accountability, connects office and field teams, and ensures all items are tracked through to resolution, providing a clear record for model sign-off.

## Things to Consider

- **Required User Permissions:**

 - Users need both permissions:

    - 'Admin' permissions on the project's Coordination Issues tool.
    - 'Standard' or 'Admin' permissions on the project's Observations tool.
- **Additional Information**:

 - Users can only move issues in the *Open* or *Released* status.
 - Users can also bulk-edit the Type, Description, Assignee, Private (checkbox), and Attachments fields. To learn more, see [Bulk Edit Coordination Issues](/product-manuals/coordination-issues-project/tutorials/bulk-edit-coordination-issues).
 - Procore automatically copies the Title, Location, and Trade entries for each issue to the new observation.
 - Procore links new observations to each issue's General tab.

## Steps

### From the Procore BIM Plugin

1. Open NavisworksÂ® and a model on your computer. See [Getting Started Using the Procore Plugin](/product-manuals/coordination-issues-project/tutorials/getting-started-procore-plugin-for-coordination-issues).
2. With the **Procore** tab selected, click **Issues List**.
3. Hover over the desired issue.
4. Click **Info**.
5. Click the **vertical ellipsis** icon.
6. Click **Move to Observation**.
7. Complete the remaining fields for the observation. See [Create an Observation](/product-manuals/observations-project/tutorials/create-an-observation).
8. Click **Create**. The Procore BIM Plugin adds the coordination issue to the Observations tool, and its status changes from 'Moved to Observation'.

### From the Coordination Issues Tool ââââââ

#### Move Issues in Bulk

1. Navigate to the project's **Coordination Issues** tool in Procore.
2. In the table on the **All Issues** tab, select the checkboxes for the coordination issue(s) to move.   
   This opens a Bulk Edit side panel.
3. From the **Status** drop-down list, select **Move to Observation**. To learn about the fields you can bulk edit, see [Bulk Edit Coordination Issues](/product-manuals/coordination-issues-project/tutorials/bulk-edit-coordination-issues).
4. Click **Update** to save your changes. Procore creates a linked observation and updates the issue's status to 'Moved to Observation.'

#### Move a Single Issue

1. Navigate to the project's **Coordination Issues** tool in Procore.
2. Click the **Issue** link to view its details in the side panel.
3. Click the icon to open the **More Options** menu and choose **Move to Observation**.
4. Complete the fields for the observation. See [Create an Observation](/product-manuals/observations-project/tutorials/create-an-observation).
5. Click **Create**. Procore creates a linked observation and updates the issue's status to 'Moved to Observation.'