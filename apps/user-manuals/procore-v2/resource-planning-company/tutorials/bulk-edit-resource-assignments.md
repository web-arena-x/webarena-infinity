# Bulk Edit Resource Assignments

Source: https://v2.support.procore.com/product-manuals/resource-planning-company/tutorials/bulk-edit-resource-assignments

---

## Things to Consider

- [Required User](/product-manuals/resource-planning-company/permissions) [Permissions](/product-manuals/resource-planning-company/permissions)
- You can manage user visibility of assignments with assignment request statuses. See [Configure Assignment Request Statuses for Resource Planning](/product-manuals/resource-planning-company/tutorials/configure-assignment-and-request-statuses-for-resource-planning).
- Assignment alerts are not sent to assignees when bulk editing resource assignments.

## Steps

You can bulk edit assignments from the following places:

- [Assignments Boards](#bulk-edit-assignments-from-the-assignments-boards)
- [Assignments Gantt (Beta)](#bulk-edit-resource-assignments-from-the-assignments-gantt-beta)
- [Assignments List](#bulk-edit-assignments-from-the-assignments-list)

## Bulk Edit Assignments from the Assignments Boards

1. Navigate to the Company level **Resource Planning** tool.
2. Click **Assignments** and select **Boards**.
3. Click **Batch**.
4. Click **Configure**.
5. Update the information for any of the following fields:

   - **Project**. Enter the project that the assignment is for.
   - **Status**. Select the assignment status.
   - **Start Date**. Enter the date the work assignment starts.
   - **End Day**. Enter the date the work assignment ends.

     - **Date**. Enter the specific end date for the assignment.
     - **Weeks**. Enter how many weeks the assignment is for.
     - **TBD**. If the assignment doesn't yet have an end date.
   - **Allocation Type**. Select whether the Allocation Type is in Hours of Percent.

     - **Work Hours Start**. If you selected 'Hours', enter the time of day the assignment begins.
     - **Work Hours Start**. If you selected 'Hours', enter the time of day the assignment ends.
     - **Percent**. If you selected 'Percent', enter the percent allocated to the assignment.
   - **Working Days.** Move the toggle to the ON position to edit the working days. Then mark the checkboxes for the working days for the selected assignments.
   - **Assignment Alerts**. Choose **Send Instantly**, **Save as Draft**, **Schedule** or **Don't Send**.
6. Click **Set**.
7. Click the **Assignments** you want to update with the new information.
8. Click **Apply Changes**.

## Bulk Edit Resource Assignments from the Assignments Gantt (Beta)

##### Â In Beta

This feature is in beta and available for customers using the Resource Planning tool.

##### Â Important

Assignment alerts are not currently sent when changing assignments this way.

1. Navigate to the Company level **Resource Planning** tool.
2. Click **Assignments** and select **Gantt (Beta)**.
3. Follow steps to edit the assignment dates in one of the following ways:

   - **Shorten or Extend Assignments**

     1. On your keyboard, press and hold **CTRL**. Click the **assignment bars** you want to edit.  
        *Note:* Assignments will move in the same direction by the same duration.
     2. Hover over the last day of the **assignment bar** on the Gantt chart until you see the arrows.
     3. Click the **arrows** and move the assignment end date using a drag-and-drop operation.
     4. If there is a scheduling conflict, review the details and take one of the following actions:

        - Click **Proceed** to save the change despite overlapping assignments.
        - Click **Cancel** to disregard your changes.
   - **Move Assignment Dates**

     1. On your keyboard, press and hold **CTRL**. Click the **assignment bars** you want to edit.
     2. Click and hold the **assignment** bar for one of the assignments. Move the assignments to the new date using a drag-and-drop operation.
     3. If there is a scheduling conflict, review the details and take one of the following actions:

        - Click **Proceed** to save the change despite overlapping assignments.
        - Click **Cancel** to disregard your changes.
   - **Move Assignments to new Projects or Categories**

     1. Press and hold the **CTRL/CMD** key on your keyboard and click each **assignment on the list.**
     2. Drag the group to the new category or project and drop it onto the **category** or **project name**.
     3. If there is a scheduling conflict, review the details and take one of the following actions:

        - Click **Proceed** to save the change despite overlapping assignments.
        - Click **Cancel** to disregard your changes.

##### Â Tip

Click the **undo**  icon to undo an action. Click the **redo**  icon redo a previously undone action.