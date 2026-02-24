# Import a Budget from ERP

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/import-a-budget-from-erp

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

If your integration supports budget syncing from your ERP system to Procore, you can import budget data into the Budget tool in your Procore project. After the budget is successfully imported, you can then modify and update your budget in Procore.

After importing, it's best to make changes to your project's budget within Procore. If changes are made to the budget in your ERP system, you will need to follow the steps in [Re-import a Budget from ERP](/product-manuals/erp-integrations-company/tutorials/reimport-a-budget-from-erp) to sync the new budget information with Procore.

## Things to Consider

- **Required User Permission**:

 - 'Standard' permission or higher on the ERP Integrations tool.
- **Requirements**:

 - The project in your ERP system must be synced with your Procore project.
 - The project's budget must be unlocked. See [Unlock a Budget](/product-manuals/budget-project/tutorials/unlock-a-budget).
- **Limitations**:

 - The ERP Integrations tool does NOT sync 'Unit of Measure (UOM)' and 'Unit Qty' values between systems (see [Which units of measure are included on Procore's master list?](/faq-which-units-of-measure-are-included-in-procores-master-list)). Currently, the Budget sync is amount-based only. This means you must manually enter units in both Procore and in your integrated ERP system.

## Steps

1. Navigate to the company's **ERP Integrations** tool.
2. Click the **Budgets** tab.
3. Locate the desired project's budget in the **Ready To Be Imported** list.
4. Click **Import**. 
   *Note*: If this button is grayed out and unavailable, you must unlock the budget first. See [Unlock a Budget](/product-manuals/budget-project/tutorials/unlock-a-budget).
5. Choose from these options:

   - The system begins the import.   
      OR
   - If a **Warning** message appears, the project already has existing line items. Choose one of these options to respond:
   - **Keep Existing Line Items And Additional Cost Estimates** Choose this option to keep all of the existing budget lines in the project's Budgets tool, and add any additional cost estimates from your ERP system (which have been assigned to cost code/categories and do not yet exist in your Procore budget).
      OR
   - **Override Existing Line Items** Choose this option to override the line items that exist in the Budget tool with the line items being imported into Procore from your ERP system.
      OR
   - **View Existing Procore Budget As PDF** If you want to review the existing budget to help you decide which option to choose, click the **PDF** button.
6. Click **Import**.

## Next Step

After the import is complete, you can navigate to the project's Budget tool and verify that the data import was successful.