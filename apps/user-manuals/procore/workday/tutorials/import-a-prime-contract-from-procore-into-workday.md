# Import a Prime Contract into Procore from WorkdayÂ®

Source: https://v2.support.procore.com/product-manuals/workday/tutorials/import-a-prime-contract-from-procore-into-workday

---

## Background

A Prime Contract must be imported from WorkdayÂ® to Procore before financial data for that contract can be synced between the two systems. Importing a Prime Contract from WorkdayÂ® creates a Prime Contract in Procore, but does not create any financial information within that contract. Because the contract's financial data will export to WorkdayÂ® as a single, summarized line item, you must create the schedule of values for your contract within Procore.

## Things to Consider

- **Required User Permissions:**

  - 'Standard' level permission or higher on the ERP Integrations tool.
- **Considerations:**

  - A Prime Contract is imported to Procore from WorkdayÂ® in the **Approved** status.
- Requirements

  - Enable the 'Always Editable Schedule of Values' setting in the Prime Contract tool's configuration settings. To learn more, see [What is the 'Enable Always Editable Schedule of Values' setting?](/faq-what-is-the-enable-always-editable-schedule-of-values-setting)
- **Prerequisites:**

  - Create a Prime Contract Shell on the project in WorkdayÂ® as a Customer Contract. Approve the Customer Contract with at least one line dedicated to the Procore Prime Contract. The line must have a Revenue Category of 'Contract Revenue' and of Line Type 'Value-Based Project' with a $0.00 amount.
  - The integration will pick up this customer contract line item and import that into Procore to create a synced $0.00 Prime Contract.

## Steps

1. Navigate to the Company level **ERP Integrations** tool.
2. Click the **Prime Contracts** tab.
3. Click the **Ready to Import** link in the right sidebar.
4. Locate the desired project's prime contract in the **Prime Contracts Ready to be Imported** list.
5. Click **Add to Procore**.   
    A message in GREEN text confirms when your prime contract has been added to Procore.
6. Line items added to the contract SOV in Procore will automatically sync to WorkdayÂ® as a single, summarized line item.