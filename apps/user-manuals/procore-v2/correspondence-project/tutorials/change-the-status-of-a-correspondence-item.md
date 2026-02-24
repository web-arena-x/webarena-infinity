# Change the Status of a Correspondence Item

Source: https://v2.support.procore.com/product-manuals/correspondence-project/tutorials/change-the-status-of-a-correspondence-item

---

## Background

When editing a correspondence item, you can change its status. If the items associated with the correspondence item have been completed and you want to close it, choose the *Closed* status.

## Things to Consider

- **Required User Permissions:**

 - *To edit any correspondence item:*

    - 'Standard' level permissions on the item's correspondence type.
 - *To edit a 'Draft' correspondence item that you created:*

    - 'Standard' level permissions on the item's correspondence type. 
      OR
    - 'Read Only' level permissions on the item's correspondence type with the ['Create Item' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permissions template.
 - *To edit an 'Open' correspondence item that you created:*

    - 'Standard' level permissions on the item's correspondence type. 
      OR
    - 'Read Only' level permissions on the item's correspondence type with the ['Edit Open Items They Created' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permissions template.
- **Additional Information:**

 - If Procore was asked to enable the 'non-editable' setting at the company level, only 'Draft' correspondence items are editable, regardless of user permissions. Consider [creating and linking a new item](/product-manuals/correspondence-project/tutorials/create-an-link-an-rfi-change-event-or-a-different-correspondence-item-to-an-existing-correspondence-item) instead.
 - If you have been assigned or associated to a correspondence item and you want to add a response to the item, see [Respond to a Correspondence Item](/product-manuals/correspondence-project/tutorials/respond-to-a-correspondence-item).
 - If a workflow is applied to the item, and the item is issued, the following fields are auto-populated with the workflow information: Status, Due Date, Assignees, and Distribution Member. Also, the 'Post Response and Change Status' button is no longer available unless 'Responses' are enabled on the fieldset.
 - Email notification information:

    - Editing an 'Open' correspondence item results in an email notification to the item's creator and anyone in the 'Assignee', 'Distribution Member', or 'Received From' fields, if an admin has enabled 'Updated Item' email notifications for the correspondence type.
    - Email notifications are sent for all correspondence items until their status is changed to 'Closed'. 
      See [Who receives correspondence item emails and push notifications?](/faq-who-receives-correspondence-item-emails-and-push-notifications) for more details.

##### Â Note

- Users who belong to the same companies as the users listed on the item can also view private items if the General Correspondence type has the granular permission of 'View Private Items Accessible to Users within Same Company' enabled.
- Reach out to your Procore point of contact if you wish for Private correspondence items to be hidden from users with 'Admin' level permissions at the company or project level, ensuring they will not have the ability to view or respond to private items unless they are specifically included on the correspondence item. (If your company is based in Australia or New Zealand, this additional level of privacy will be enabled by default).
- You can always see who has permissions to private items via the 'Permissions' tab when viewing a correspondence item.

## Steps

1. Navigate to the project's **Correspondence** tool.
2. Locate the correspondence item you want to change the status of.
3. Click **Edit**.   
   *Note:* If there is no 'Edit' button, Procore was asked to enable the 'non-editable' setting at the company level to keep communication records reliable for all 'Open' and 'Closed' items in the Correspondence tool. Consider [creating and linking a new item](/product-manuals/correspondence-project/tutorials/create-an-link-an-rfi-change-event-or-a-different-correspondence-item-to-an-existing-correspondence-item) instead.
4. Select a status from the **Status** list:

   - **Draft:** Indicates that the correspondence item is in draft mode and has not been issued.
   - **Open:** The correspondence is open.
   - **Closed Successful:** The correspondence is closed and was successful.
   - **Closed Unsuccessful:** The correspondence is closed and was unsuccessful or not approved.
   - **Custom Status:** You can select a custom status if any were created. See [Manage Custom Statuses for Correspondence Types](/product-manuals/admin-company/tutorials/manage-custom-statuses-for-correspondence-types).
5. Click **Save**.