# Create a Project Level Punch Item Template

Source: https://v2.support.procore.com/product-manuals/punch-list-project/tutorials/create-a-project-level-punch-item-template

---

## Background

If you're a Punch List tool Admin, you may find it useful to add custom punch list item templates. While Procore provides a default library of common punch list items for all companies, you can add your own custom templates for punch list items specific to your project. These templates can be organized by type and configured to include a default trade, Punch Manager, Assignee, and Final Approver for the item. These templates are only available for use on a mobile device; when a team member creates a new punch list item from a mobile device, they can select one of these templates, which will auto-fill fields with default information. You can then add or edit any information as needed.

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permissions on the project's Punch List tool.
- **Additional Information:**

  - Punch List templates are only available for use on a mobile device.
  - To manage Punch List templates at the Company level so that the template will appear on all projects, see [Create a Company Level Punch Item Template](/product-manuals/admin-company/tutorials/create-a-company-level-punch-item-template).

## Steps

1. Navigate to the project's **Punch List** tool.
2. Click the **Configure Settings**  icon.
3. Click **Punch List Templates**.
4. Scroll to the category under which you would like to create a template.  
   *Note:* If no categories are present, follow the steps in [Create a Quick Punch Category on a Project](/product-manuals/punch-list-project/tutorials/create-a-punch-item-template-category-at-the-project-level).
5. Enter the following information in the empty fields.

   - **Template Name:** Enter the name of the template. This will populate in the subject of the punch list item.
   - **Default Trade:** Select the trade that is associated with the punch list item.
   - **Default Punch** **Item Manager:** Select a default Punch Item Manager who will oversee the item throughout its entire lifecycle.  
     *Note:* If no Punch Item Manager is selected, Procore will default to the Punch Item Manager defined in the Punch List tool's settings. If no Punch Item Manager is defined in the Punch List tool's settings, Procore will list the item's Creator as the Punch Item Manager.
   - **Default Assignee:** Select a default Assignee who will be responsible for resolving these items.
   - **Default Final Approver:** Select a default Final Approver who will have the authority to close the item.  
     *Note:* If no Final Approver is selected, Procore will automatically list the item's Creator as the Final Approver.
   - **Active:** Mark the checkbox to make this template available to team members.
6. Click **Add**.

## Next Steps

- [Create a Punch List Item (iOS)](/product-manuals/punch-list-ios/tutorials/create-a-punch-list-item-ios)
- [Create a Punch List Item (Android)](/product-manuals/punch-list-android/tutorials/create-a-punch-list-item-android)