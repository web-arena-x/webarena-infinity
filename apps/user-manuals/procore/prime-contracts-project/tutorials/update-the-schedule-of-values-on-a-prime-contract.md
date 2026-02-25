# Update the Schedule of Values on a Prime Contract

Source: https://v2.support.procore.com/product-manuals/prime-contracts-project/tutorials/update-the-schedule-of-values-on-a-prime-contract

---

## Background

After creating a **Prime Contract**, you can choose from three (3) methods to update line items to the SOV:

- **Add Line Items to the SOV**If your contract's SOV only has a few line items or if you want to manually add new line items to the SOV, use the **Add Line** button to manually enter each SOV line item.
- **Create the SOV from the Project's Budget**  
  If your want to structure your contract's SOV to match your budget line items, Procore gives you an option to import your SOV line items directly from the Procore's Budget tool. This method automatically creates the contract's SOV for you using your project's budget line items as its data source.
- **Import the SOV from a CSV File**  
  If you would prefer to build your contract's SOV using a spreadsheet program, such as Microsoft Excel, you can download a blank template that matches your contract's table structure, add your SOV line items to the spreadsheet, save the file to the Comma Separated Values (CSV) file format, and then import your line items. You can also use the import process to replace all existing line items on your contract's SOV or you can keep any existing line items and add additional ones.

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permissions on the project's **Prime Contracts** tool.

    ##### Â Note

    To limit Procore users from viewing your contract data, configure the granular permissions feature when applying permission templates. See [Edit a Project Permissions Template](/product-manuals/permissions-company/tutorials/edit-a-project-permissions-template).

- **Additional Information:**

  - To complete the steps below, the contract will need to be in the '**Draft**' status. However, if the '**Enable Always Editable Schedule of Values**' setting is turned **ON** in this tool, users with the required user permission to [Edit Prime Contracts](/product-manuals/prime-contracts-project/tutorials/edit-prime-contracts) can edit the Schedule of Values when a contract is in any status. To learn more, [What is the 'Enable Always Editable Schedule of Values' setting?](/faq-what-is-the-enable-always-editable-schedule-of-values-setting)

    ##### Â Note

    If you have incoming line items from the project's Budget tool and the amounts in those line item(s) are lower than the amount(s) billed on those line item(s) in a [GC/Client invoice](/glossary-of-terms), [funding invoice](/glossary-of-terms), or [owner invoice](/glossary-of-terms), an error message notifies you that the line items cannot be imported from the project's budget.

- **Limitations:**

  - If you have created multiple prime contracts, please be aware that you can import budget line items to a Prime Contract's Schedule of Values (SOV). However, you do NOT have the ability to choose which budget line items that you want to import. To learn more, see [Are there any system limitations when creating multiple prime contracts?](/faq-are-there-any-system-limitations-when-creating-multiple-prime-contracts)