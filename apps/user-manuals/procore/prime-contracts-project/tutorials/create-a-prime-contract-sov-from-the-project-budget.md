# Create a Schedule of Values on a Prime Contract using the Project's Budget

Source: https://v2.support.procore.com/product-manuals/prime-contracts-project/tutorials/create-a-prime-contract-sov-from-the-project-budget

---

## Background

After your construction project's original budget is finalized in the project's Budget tool, it is recommended that you lock the budget. Once locked, you can use the steps below to quickly import your budget line items to your prime contract's SOV. With this action, each line item on the project's budget creates a line item on the contract's SOV.

##### Example

The example below shows you the line items on a budget that can be used to create corresponding line items on the contract's SOV. For example, *01-000-Purpose*: Labor, *01-002-Instructions: Labor*, *01-010 Project Manager: Labor*, and so on.

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permissions on the project's Prime Contracts tool.

    ##### Â Note

    To limit Procore users from viewing your contract data, configure the granular permissions feature when applying permission templates. See [Edit a Project Permissions Template](/product-manuals/permissions-company/tutorials/edit-a-project-permissions-template).

- **Additional Information:**

  - To complete the steps below, the contract will need to be in the 'Draft' status. However, if the 'Enable Always Editable Schedule of Values' setting is turned ON in this tool, users with the required user permission to [Edit a Prime Contract](/product-manuals/prime-contracts-project/tutorials/edit-a-prime-contract) can edit the Schedule of Values when a contract is in any status. To learn more, [What is the 'Enable Always Editable Schedule of Values' setting?](/faq-what-is-the-enable-always-editable-schedule-of-values-setting)

    ##### Â Note

    If you have incoming line items from the project's Budget tool (see [Create the SOV from the Project's Budget](/product-manuals/prime-contracts-project/tutorials/update-the-schedule-of-values-on-a-prime-contract) below) and the amounts in those line item(s) are lower than the amount(s) billed on those line item(s) in a [GC/Client invoice](/glossary-of-terms), [funding invoice](/glossary-of-terms), or [owner invoice](/glossary-of-terms), an error message notifies you that the line items cannot be imported from the project's budget.