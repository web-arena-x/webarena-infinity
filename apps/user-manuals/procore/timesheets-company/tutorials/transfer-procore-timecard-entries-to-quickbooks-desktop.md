# Transfer Procore Timecard Entries to QuickBooksÂ® Desktop

Source: https://v2.support.procore.com/product-manuals/timesheets-company/tutorials/transfer-procore-timecard-entries-to-quickbooks-desktop

---

## Background

If your company processes its payroll using QuickBooksÂ® Desktop, you can transfer the time entries from Procore's Company level Timesheets tool using a simple file export.

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

## Things to Consider

- [Required User Permissions](/product-manuals/timesheets-company/permissions)
- **Supported Versions**:

  - QuickBooksÂ® Desktop (2022 or after)
  - QuickBooksÂ® Desktop (2021 or earlier)

## Steps

1. [Export a Timer List as an IIF file from QuickBooksÂ® Desktop](/product-manuals/timesheets-company/tutorials/export-a-timer-list-as-an-iif-file-from-quickbooks-desktop) *Note:* This step is only required if using QuickBooksÂ® Desktop (2021 or earlier) or QuickBooksÂ® Desktop 2022 or later with QuickbooksÂ® Time.
2. [Configure the Company Timesheets Payroll Settings](/product-manuals/timesheets-company/tutorials/configure-the-company-timesheets-payroll-settings)
3. [Export Time Entries from Procore to Import into QuickBooksÂ® Desktop](/product-manuals/timesheets-company/tutorials/export-timecard-entries-from-procore-to-import-into-quickbooks-software)
4. [Import Procore Time Entries into QuickBooksÂ® Desktop](/product-manuals/timesheets-company/tutorials/import-procore-time-entries-into-quickbooks-desktop)

##### Â Note

Some terms may vary between Procore and QuickBooksÂ® Desktop. The table below is a list of terms as they exist in Procore and in QuickBooksÂ® Desktop

| **Procore** | QuickBooksÂ® Desktop |
| --- | --- |
| Cost Code | Service Item |
| Project Name | Job Name |
| QuickBooks Customer (Project Admin Settings) | Customer |
| Day | Date |
| Time Type | Payroll Item |