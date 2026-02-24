# Import a chart of accounts template into Xero HQ

Source: https://central.xero.com/s/article/Import-a-chart-of-accounts-template-into-Xero-HQ

---

## Overview

- Import your own chart of accounts template into Xero HQ to use for your clients.
- Review and fix errors when importing your chart of accounts template.

## What you need to know

- Importing a chart of accounts into Xero HQ creates a new template for you to use in the chart of accounts library.
- You can import a chart of accounts using a CSV file. You can only import one CSV file at a time.
- The CSV file import only supports set fields in a specific column order with case sensitive headings. Any additional information in your file won't be imported.
- Any tax rates you include in your CSV file need to match the tax rates that exist in Xero HQ. If you’ve included tax rates that aren’t in Xero HQ, you’ll receive an error message when you try to import the chart of accounts. You can only import a chart of accounts that uses the tax codes for the region your practice is based in.
- Xero automatically adds system accounts when you upload a chart of accounts template, and puts a label under the account name to help identify them.
- You need the edit chart of accounts and report templates permission to import a chart of accounts.

Tip

You can also access report templates from Practice Manager. Click **Reports**, then select **Report Templates**.

**1** Download a file and prepare the data

You can use any of the following methods to create your import file:

- Download and customise [our CSV template](https://xero.my.salesforce.com/sfc/p/o0000000biwC/a/3m000000PyrQ/97WocE2d3U92YOoVlf8ak1iJdem1vLFTBZwYpWFwN.c).
- [Export the chart of accounts](Export-a-chart-of-accounts-template-from-Xero-HQ.md) from another Xero organisation and update it to suit your needs.
- Export a file from your previous accounting system and customise it to meet the Xero requirements.
- Create a file from scratch.

If you choose to create your file from a non-Xero source, we recommend using our CSV template or an export from another Xero organisation as a guide.

Find the downloaded file on your computer and open it, then complete all the required fields. Fields with an asterisk (\*) on the column header in the CSV file indicates the compulsory ones.

The file must only contain the support fields in the order listed in the table below, and the headings are case sensitive.

| Field | Description |
| --- | --- |
| Code\* | Use letters, numbers or symbols, up to 10 characters. The account code must be unique. |
| Report Code | Xero uses the report code to know where you want your accounts to appear when [report templates](Report-codes-for-practices-using-report-templates.md) are run within client organisations. |
| Name\* | Use letters, numbers or symbols, up to 150 characters. The name must be unique. |
| Type\* | You must use one of [these account types](/s/article/Tax-codes-and-account-types-for-chart-of-accounts-in-Xero-HQ?userregion=true) (spelled and formatted the same). Xero only uses one Accounts Receivable system (control) account and one Accounts Payable system (control) account. If you previously used multiple control accounts, you'll need to merge them in Xero. |
| Tax Code\* | [Add a tax rate](Chart-of-accounts-templates-in-Xero-HQ.md) for each account. |
| Description | You can add a description to all accounts. Consider adding descriptions to accounts your users can choose when they enter receipts into expense claims. This helps users who are unfamiliar with the chart of accounts. |
| Reporting name | You can add reporting names to give your accounts a different display name in reports. This name only appears on reports if they're in a report template and contain the Edit layout button. The option is available for all accounts except those with the account type ‘Bank’. |

**2** Import the chart of accounts template

1. In Xero HQ, click **Practice** and select **Chart of accounts**.
2. Click **Import template**.
3. Enter a **Template name**.
4. (Optional) Enter a description for the template.
5. Click **Select file** to locate your saved file on your computer.
6. Click **Open**.
7. Click **Save**.

**3** Review errors in your imported accounts

If you’re missing information, review the column headings which are case sensitive and must exactly match the wording and the order in the table above.

If there's anything wrong with the file, Xero will list the errors for you to review. You can’t import the file and create a chart of accounts template until all errors are fixed.

- Any errors found are listed below the **Upload.csv** section.
- Each error message shows the number of the line in the CSV file containing the error, as well as a description of the error that explains why the line failed to import.
- If you're using a text editor, such as Notepad, we recommend turning on line numbering to help you locate an error. Note that Line 1 is the mandatory first line containing the Xero column headings in your file.
- You'll need to update your CSV file to resolve any errors before re-importing your template.

## What's next?

Learn more about how to use [chart of accounts templates in Xero HQ](Chart-of-accounts-templates-in-Xero-HQ.md).