# Map report codes to your client's chart of accounts

Source: https://central.xero.com/s/article/Report-codes-for-practices-using-report-templates

---

## Overview

- Learn how to use report codes to map your clients’ chart of accounts to your practice’s report templates.
- Edit and review your report code mapping to make it as accurate as possible.

How it works

You can map the chart of accounts in your client's organisation to your practice's report codes to get the most out of using report templates.

Xero uses the report code mapping to know where you want your client’s account codes to appear when report templates are run within their organisation. Report codes also ensure that your report templates and advanced business performance ratios are detailed and accurate.

The account type of the client account code must match the account type of the report code you're mapping it to. For example, you should map expense accounts to a profit and loss report code like EXP. Mismatches can cause errors in reports.

You can map your client's chart of accounts to report codes one account at a time, or import their complete chart with the mapping applied.

You can view which report code is mapped to each account from the chart of accounts in your client’s organisation.

You can't add new report codes or change the details of existing codes. However, you can map multiple accounts to the same report codes and further customise the reports at the client level.

Tip

If you want to use a template rather than map accounts individually, use the [chart of accounts templates in Xero HQ](Chart-of-accounts-templates-in-Xero-HQ.md). These accounts are pre-mapped to report codes.

Import a complete chart of accounts with mapping applied

You can import a complete chart of accounts with mapping applied into a client organisation. The process for doing this is:

1. Export the existing chart of accounts from the organisation.
2. Map the accounts in a CSV file.
3. Re-import the file to apply the mapping.

To export the existing chart of accounts:

1. Open the client organisation you want to export report codes from.
2. In the **Reporting** menu, select **Reporting settings**.
3. Click **Report codes**.
4. Click **Export**.
5. Open or save the downloaded CSV file from your browser.

Enter the report codes for each account into the **Report Code** column on the exported file.

To import the chart back into Xero:

1. Open the client organisation you want to import report codes into.
2. In the **Reporting** menu, select **Reporting settings**.
3. Click **Report codes**.
4. Click **Import**.
5. Click **Browse**, then find and select the CSV file from your computer.
6. Click **Open**, then click **Import**.

When you import report codes, Xero looks for a match between the account code and the account name. If a match is found, Xero updates the mapping for that report code.

Edit report code mapping

On the **All Accounts** tab, view the mapping for each account and edit any that need to change. The deeper the mapping you choose, the more flexible your reporting will be.

To map accounts to a different report code:

1. Open the client organisation.
2. In the **Reporting** menu, select **Reporting settings**.
3. Click **Report codes**.
4. Select the checkboxes for each account you want to map to a single report code.
5. Click **Edit Mapping**.
6. Select a report code to view the codes underneath it, one level at a time. Review the report code descriptions on the right-hand pane.
7. Once you've selected the report code that best matches the accounts you're mapping, click **OK**.

Tip

You can click **Edit Report Code Mappings** from your client’s Chart of accounts screen to go to the Report codes screen.

Review report code mapping

### About the For Review tab

Report codes appear on the **For Review** tab if:

- The client's chart of accounts hasn't been mapped to report codes
- There's a new account in this client's chart of accounts
- Xero has introduced new report codes

If an account hasn’t been mapped to a report code, Xero assigns a high level report code to the account. These are highlighted for your review with a yellow dot.

Reviewing the report codes for these accounts gives you the opportunity to map accounts to a more detailed level. Accounts keep their existing report code mappings unless you change them.

### What happens when Xero adds new report codes

We'll flag for review any accounts with an existing report code that's the parent of a new report code.

For example, if your account is mapped to the Expense (EXP) report code and Xero introduces a report code EXP.TRA.PLA for Travel - Interplanetary, the EXP account will show on the **For Review** tab.

Accounts mapped to report codes at the same level as the new code won't appear on the **For Review** tab.

For example, if the account is mapped to EXP.TRA.INT, it won't show on the **For Review** tab when we release our hypothetical new report code, EXP.TRA.PLA.

To ignore new report codes that aren't relevant to your practice, you can export your existing report codes and re-import them.

## What's next?

With the report code mapping complete, you're ready to [use a report template in a client's organisation](Use-a-report-template-in-a-client-s-organisation.md).