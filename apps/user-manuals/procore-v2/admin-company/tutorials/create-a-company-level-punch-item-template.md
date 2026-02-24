# Create a Company Level Punch Item Template

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/create-a-company-level-punch-item-template

---

## Background

If you're a Punch List tool Admin, you may find it useful to add custom punch list item templates. While Procore provides a default library of common punch list items for all companies, you can add your own custom templates for punch list items specific to your project. These templates can be organized by type and configured to include a default trade, Punch Manager, Assignee, and Final Approver for the item. These templates are only available for use on a mobile device; when a team member creates a new punch list item from a mobile device, they can select one of these templates, which will auto-fill fields with default information. You can then add or edit any information as needed.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the Company level Admin tool.
- **Additional Information:**

 - Punch item templates created at the Company level will be dynamically added to all projects in the company.
 - Users with 'Admin' level permission to the Punch List tool can deactivate templates at the Project level if a certain template does not apply.

## Steps

1. Navigate to the Company level **Admin** tool.
2. Under 'Tool Settings', click **Punch List**.
3. Choose from these options:

   - To configure a punch item template for a category, do the following:

     - **Category**. Select the category for which the punch item template will apply. This is only for organizational purposes.

       Category (Punch Item Template)*Note*: If no categories are present, follow the steps in [Create a Punch Item Template Category at the Company Level](/product-manuals/admin-company/tutorials/create-a-punch-item-template-category-at-the-company-level).
     - **Template Name**. Enter the name of the punch item template. When a user chooses to add this punch item to a punch list, this defines the item name.

       Template (Punch Item Template Name)
     - **Trade**: Select the trade to apply to the punch item. Trades can be added to this list using the Admin tool. See [Add a Custom Trade](/product-manuals/admin-company/tutorials/add-a-custom-trade).

       Trade (Punch Item Template)
   - To apply a trade to an entire category, complete the following:

     - **Trade**. Next to the desired category, select the trade that you want to apply to all the Punch item templates in that category. Trades can be added to this list using the Admin tool. See [Add a Custom Trade](/product-manuals/admin-company/tutorials/add-a-custom-trade).
     - When the 'Apply Trade to Category' box appears, click **Continue** to apply that trade to the all of the Punch item templates in that category.
4. Click **Submit**.

## Next Steps

- *Optional:* Navigate to the Project level Punch List tool and add a default assignee. See [Configure Advanced Settings: Punch List](/product-manuals/punch-list-project/tutorials/configure-advanced-settings-punch-list).
- [Create a Punch List Item (iOS)](/product-manuals/punch-list-ios/tutorials/create-a-punch-list-item-ios)
- [Create a Punch List Item (Android)](/product-manuals/punch-list-android/tutorials/create-a-punch-list-item-android)