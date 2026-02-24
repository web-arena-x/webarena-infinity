# Workpapers and Xero Tax explained (BETA)

Source: https://central.xero.com/s/article/Workpapers-and-Xero-Tax-explained

---

## Overview

- Understand how Workpapers and Xero Tax integrate to streamline your tax form preparation.

Tip

The Workpapers and Xero Tax integration is currently in beta and is available to selected practices.

## What you need to know

The integration between Workpapers and Xero Tax helps you to streamline your tax form preparation by automatically exporting data from your client’s workpapers into their tax returns.

From Workpapers, you can export the data into Xero Tax, then use this to submit your client’s tax returns to the Australian Tax Office (ATO). Currently the integration only supports the company tax return (CTR), but more forms will be added over the coming months.

Workpapers maps the data across each workpaper, the Adjusted Working Trial Balance and the Tax Reconciliation workpaper. It then populates the CTR with the resulting values. Xero Tax doesn’t do any calculations – the calculations are done in Workpapers, then Workpapers sends the values to Xero Tax.

When you export data from Workpapers to Xero Tax, details of the export including any errors show in the history and notes section of the related tax return.

You need to have [tax access](Restrict-staff-access-to-a-client-s-tax-returns.md) to a client’s tax return and the [edit level for tax forms](Add-your-staff-to-Xero-Tax-and-set-their-privileges.md) in Xero Tax to export data and edit the return in Xero Tax.

## About the tax mapping

When you create a workpaper pack for a client, Workpapers applies a default mapping template to the pack. This template contains default report code mapping for all the workpapers in the pack, as per the organisation type.

The default template maps all the report codes in the practice across all the workpapers for the client, and identifies the field the value maps to in the tax return.

If there’s both general ledger and workpapers data exported to the same label in Xero Tax, both values appear in the tax return. They show as two source amounts under the label and the label reflects a combined total.

Each report code in the template can have a different mapping status:

- Mapped – The report code in Workpapers is mapped to a label in Xero Tax
- Unmapped – The report code in Workpapers isn’t mapped to a label in Xero Tax
- Excluded – The report code is excluded from mapping to Xero Tax

To view the mapping applied to a client’s workpaper pack:

1. On the **Workpapers** screen, click the client’s workpaper pack.
2. Select the **Tax mapping** tab.

## What's next?

Export data from [Workpapers to Xero Tax](Export-workpaper-data-to-tax.md).