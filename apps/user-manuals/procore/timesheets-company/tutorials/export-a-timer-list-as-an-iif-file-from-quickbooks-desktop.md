# Export a Timer List as an IIF file from QuickBooksÂ® Desktop

Source: https://v2.support.procore.com/product-manuals/timesheets-company/tutorials/export-a-timer-list-as-an-iif-file-from-quickbooks-desktop

---

## Background

To transfer Procore Timesheets data to QuickBooksÂ® Desktop you must first complete a few setup steps. This tutorial covers the first requirement: exporting a preformatted Intuit Interchange Format (IIF) file from your QuickBooksÂ® Desktop system. This file prepares the connection for your Procore time entry data.

##### Â Notes

- The IIF file provides the data structure that Procore needs to ensure that transferred data is formatted as required in QuickBooksÂ®. Your IIF file must match this structure:

  - Cost Codes Numbering
  - Cost Codes Format
  - Time Types (QuickBooksÂ® Payroll Item)
  - Employee Names
  - Customer Names
  - Job Names
- Technical support or assistance for creating or importing an Intuit Interchange Format (IIF) file is NOT provided. It is recommended that you always create a backup of your IIF file in case you need to reference it later.
- Transferring time entries from Procore is a separate function and does NOT require the [Procore + QuickBooksÂ® Connector](/product-manuals/quickbooks-desktop/).

## Things to Consider

- **Required User Permissions:**

  - Administrator permissions to QuickBooksÂ® Desktop.
  - You must log into QuickBooksÂ® Desktop in Single-user mode. For details about Single-user mode, visit [QuickBooksÂ® Help](https://quickbooks.intuit.com/learn-support/en-us/product-preferences/features-available-and-tasks-you-can-perform-in-single-or-multi/00/203342).
- **Supported Versions**:

  - QuickBooksÂ® Desktop (2021 or earlier)
  - QuickBooksÂ® Desktop (2022) with QuickBooksÂ® Time

## Prerequisites

- Review the process defined in [Transfer Procore Time Entries to QuickBooksÂ® Desktop](/product-manuals/timesheets-company/tutorials/transfer-procore-timecard-entries-to-quickbooks-desktop).

## Steps

1. Log in to QuickBooksÂ® Desktop as an Administrator in Single-user mode.
2. Click **File**.
3. Click **Utilities**.
4. Click **Export**.
5. Click **Timer Lists**.
6. In the **Export** window, complete the following:

   - In the **Save In** drop-down menu, select the location where you want to save the .IIF file.
   - In the **File Name** field, type in the file name you want to use (such as 'timer list').
   - In the **File Type** drop-down menu, select ***IIF Files (\*.IIF)****.*
   - Click **Save**.
7. Click **OK**.

## Next Steps

- [Configure the Company Timesheets Payroll Settings](/product-manuals/timesheets-company/tutorials/configure-the-company-timesheets-payroll-settings)