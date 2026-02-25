# Configure Settings: Budget

Source: https://v2.support.procore.com/product-manuals/budget-project/tutorials/configure-settings-budget

---

## Background

Users with the appropriate permissions can configure a variety of advanced settings for the project's Budget tool.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the project's Budget tool.
- **Additional Information:**

 - There are additional configuration steps for the budget and forecast views in the Company Admin tool. See [Set Up a New Budget View](/process-guides/project-equipment-user-guide/assign-the-budget-view-to-a-procore-project) and [Set Up a New Forecasting View](/product-manuals/admin-company/tutorials/set-up-a-new-forecasting-view).

## Steps

1. Navigate to the project's **Budget** tool.
2. Click **Configure Settings** .
3. Click **Budget Settings**.
4. In the Budget Settings page, configure each setting:

   - To turn a feature ON, mark the check box.
   - To turn a feature OFF, remove the check mark from the box.
5. Click **Update**.

#### Budget Line Formatting

This table details the settings under 'Budget Line Formatting' in the 'Budget Settings' page.

| **Setting** | Element | Description |
| --- | --- | --- |
| Display all values in red text on rows where any calculated column value is negative | Check box | Mark this check box to have all values in a line show as red when any column in the row is negative. |

#### Forecasting

This table details the settings under 'Forecasting' in the 'Budget Settings' page.

| **Setting** | Element | Description |
| --- | --- | --- |
| Autocalculate Forecast to Complete by Default | Check box | Mark the check box to automatically calculate the forecast to complete for new budget items. Procore does NOT retroactively calculate the 'Forecast to Complete' value on existing budget items. |
| Enable Advanced Forecasting | Check box | Mark the check box to add the following features to Procore:   - The Forecasting tab in the project's Budget tool. - The Procore Standard Forecast View in the Company Admin tool. See - The ability to create customized forecasting views and assign them to projects in the Company Admin tool. |

#### Budget Changes

This table details the settings under 'Budget Changes' in the 'Budget Settings' page.

| **Setting** | | **Description** |
| --- | --- | --- |
| Require a Budget Change Adjustment to Change Event association | Yes/No | YES: Prevents the movement of funds between budget codes without a change event association. *Optional:* Check the box to automatically create a change event for all unassigned adjustments. Each unassigned adjustment will be added as change event line items on the new change event. NO: Budget change adjustments do NOT require a change event association. However, it is still possible to link them together when necessary. |
| Require Net Zero Budget Change Amounts | Check box | Mark the check box to require net zero budget change amounts when creating budget changes. This requires the user creating the budget change to move the full amount of an adjustment to another line item before allowing them to click **Save**. See [Create Budget Changes](/process-guides/resource-tracking-and-project-financials-setup-guide/record-changes-on-an-internal-budget-change). |
| Allow Budget Changes to be Billed on Owner Invoices | Check box | Mark this check box to allow users to add newly approved budget changes to the most recent owner invoice: *Note: Selected budget changes must have a net zero balance.* ââââââ |

#### Budget

This table details the settings under 'Budget' in the 'Budget Settings' page.

| **Setting** | Element | Description |
| --- | --- | --- |
| Display Grand Total on Last Page of Budget PDF Export Only. | Check box | Mark the check box to display the Budget Grand Total only on the last page of the Budget PDF Export. |

##### Â Legacy Content

This setting is only available to Procore customers who have not completed migration to the budget changes feature. See [About Budget Changes](https://support.procore.com/products/online/user-guide/project-level/budget/tutorials/about-budget-changes) and [Migrating to Budget Changes from Budget Modifications](/product-manuals/budget-project/tutorials/migrating-to-budget-changes-from-budget-modifications).

| **Setting** | | **Description** |
| --- | --- | --- |
| **Allow Budget Modifications Which Modify Grand Total** | Check box | Mark the check box to turn this setting ON to:   - Perform addition/subtraction to increase/decrease totals when creating budget modifications. |

### Set User Permissions for the Budget Tool

Instead of the steps below, Procore recommends that you set user access permissions to your project tools using a permission template. See [Create a Project Permission Template](/product-manuals/permissions-company/tutorials/create-a-project-permissions-template).

1. Navigate to the project's **Budget** tool.
2. Click **Configure Settings** .
3. Click **Permissions Table**.
4. Under **User Permissions for Budget**, set the user's access permission level by clicking the icon in the column so a GREEN checkmark appears.

   The color-coded icons in the user permissions area denotes the user's access permission level to the tool. To learn more, see [What are the default permission levels in Procore?](/faq-what-are-the-default-permission-levels-in-procore)

   | Icon | Color | Definition |
   | --- | --- | --- |
   | | **GREEN** | The user has been granted this access permission level to the tool. |
   | | **RED** | The user has NOT been granted this access permission to the tool. |
   | | **GREY** | The user is either a Procore Administrator or has been granted permissions to the Procore tools on this project using a permissions template (see [What is a permissions template?](/faq-what-is-a-permissions-template)). |