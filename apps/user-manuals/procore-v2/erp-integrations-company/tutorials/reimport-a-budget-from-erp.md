# Re-Import a Budget from ERP

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/reimport-a-budget-from-erp

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

If your company has previously imported a budget from your ERP system into a Procore project, there are two methods to keep the budget synchronized. Users will typically make budget changes in Procore for most updates. However, if the budget is modified directly in your ERP system, then it must be re-imported into Procore so that the data is synchronized between the two systems.

## Things to Consider

- **Required User Permission**:

 - 'Standard' level permission or higher on the ERP Integrations tool.
- **Requirements**:

 - The project's budget must be unlocked. See [Unlock a Budget](/product-manuals/budget-project/tutorials/unlock-a-budget).
- **Limitations**:

 - The ERP Integrations tool does NOT sync 'Unit of Measure (UOM)' and 'Unit Qty' values between systems (see [Which units of measure are included on Procore's master list?](/faq-which-units-of-measure-are-included-in-procores-master-list)). Currently, the Budget sync is amount-based only. This means you must manually enter the units in both Procore and in your integrated ERP system.

## Steps

1. Navigate to the **ERP Integrations** tool.
2. Click the **Budgets** subtab. 
    This opens the **Ready to Import** page on the Budget tab.
3. Under **Filter Estimates By**, click **Synced**.
4. Locate the desired budget.
5. Click **Re-import**. 
   *Note*: If the **Re-import** button is grayed out and unavailable, the budget must be unlocked before it can be re-imported. See [Unlock a Budget](/product-manuals/budget-project/tutorials/unlock-a-budget).
6. In the 'Please Confirm' box that appears, click **OK** to confirm the re-import action. 
    The system will override the existing value on the Procore budget with the new value from your ERP system. A system message indicates the import is in progress and may take a few minutes. A 'Successfully Re-imported to Procore' message appears when the process is complete.
7. (Optional) To verify that the ERP budget was imported into Procore's Budget tool, click the hyperlink for the item in the **Project Name** column. 
    This opens the Budget tab on the project.