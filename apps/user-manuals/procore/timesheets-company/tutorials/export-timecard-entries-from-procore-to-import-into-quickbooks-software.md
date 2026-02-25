# Export Timecard Entries from Procore to Import into QuickBooksÂ® Desktop

Source: https://v2.support.procore.com/product-manuals/timesheets-company/tutorials/export-timecard-entries-from-procore-to-import-into-quickbooks-software

---

##### Â Note

This is separate functionality from the [Procore + QuickBooksÂ® Connector](/product-manuals/quickbooks-desktop/).

## Things to Consider

- [Required User Permissions](/product-manuals/timesheets-company/permissions)
- When you export your time entries, you can select to automatically mark the entries as 'Completed' in Procore.
- You cannot re-import the same individual file. However, if you export the same file twice from Procore and import both of those files into QuickBooksÂ© Desktop, the data will be duplicated.
- To safeguard your data, back up your QuickBooksÂ© Desktop company file before you import your IIF file.
- You must be using Service Type Items in QuickBooksÂ© Desktop.
- Workers Compensation will need to be configured for timecard entries created through the IIF file.
- When importing an IIF file, if the 'QuickBooks Customer' field is left blank in the project's Admin tool, QuickBooksÂ© Desktop will create the new job as 'Customer'.
- Employee names must match **exactly** in the IIF file and in QuickBooksÂ© Desktop. If the employee names do not match, QuickBooksÂ© Desktop will create a new employee.
- The 'Use time data to create paychecks' box must be marked when setting up an employee in QuickBooksÂ© Desktop to pull the hour data and cost codes into paychecks.
- **Supported Versions**:

  - QuickBooksÂ® Desktop

##### Â Note

- The IIF file provides the data structure that Procore needs to ensure that transferred data is formatted as required in QuickBooksÂ®. Your IIF file must match this structure:

  - Cost Codes Numbering
  - Cost Codes Format
  - Time Types (QuickBooksÂ® Payroll Item)
  - Employee Names
  - Customer Names
  - Job Names
- We do not provide technical support for creating or importing Intuit Interchange Format (IIF) files. Always back up your IIF file in case you need it later.
- Transferring time entries from Procore does not require the [Procore + QuickBooksÂ® Connector](/product-manuals/quickbooks-desktop/).