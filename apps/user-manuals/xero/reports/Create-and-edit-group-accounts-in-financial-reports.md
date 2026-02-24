# Create and edit account groups in financial reports

Source: https://central.xero.com/s/article/Create-and-edit-group-accounts-in-financial-reports

---

## Overview

- Use the layout editor on financial reports to add, edit or remove account groups.
- Use switch rules to move accounts from one report group to another.

How it works

Financial reports contain accounts from your chart of accounts. These are shown in groups – for example, Assets and Liabilities on the Balance Sheet. You can use the layout editor on financial reports to add, edit or remove account groups.

You can add a switch rule to move an account from one group to another if the balance is negative. For example, a switch rule could be used to move accounts from Assets to Liabilities if they have a negative balance.

You can either move accounts into groups manually, or set rules to automatically group accounts based on their account code.

Some reports have switch rules in them by default. You can edit or delete these.

Xero doesn’t update formulas when you change a report’s structure. You might need to [edit a formula](Create-or-edit-formulas-in-financial-reports.md) if you’ve created or shifted a group of accounts in a report.

The following reports contain the layout editor:

- Balance Sheet
- Blank Report
- Budget Variance report
- Cash Summary
- Profit and Loss report (Income Statement)
- Movements in Equity report (Statement of Changes in Equity/Owners’ Equity Summary)
- Statement of Cash Flows (Business Cash Flow Summary)

Create an account group

Group accounts with related information together on the report:

1. In the **Reporting** menu, select **All reports**.
2. Find and open the financial report to edit. You can use the search field in the top right corner.
3. Click **Edit layout**.
4. To select the accounts to group, either:

   - Hold down the Ctrl key (PC) or Command key (Mac) on your keyboard, click the account rows, then click **Group selection**
   - Click the rows icon , select **Group**, then drag account rows into the new group
5. In the **Group** panel, select options for the group. See the table below for info on each option.
6. To shift the group to another section of the report, click the group row, then drag and drop the group.
7. Click **Update layout** to exit the layout and view the updated report.

To save the updated report as a draft, click **Save as**, then select **Draft**. To reuse the report's layout and formulas in future reports, click **Save as**, then select **Custom**.

Depending on the report, you can select the following options when creating a group:

| Option | Description |
| --- | --- |
| Row heading | Add or edit the heading for the group. You can also change the headings of the opening balance or total rows by clicking them, then editing the **Row heading** field. |
| Display balance | Choose whether debit or credit balances display as positive. If you select credit positive, negative balances show in brackets. |
| Group selection | Add a group of accounts to a larger group. When you click **Group selection**, Xero creates a new group with a sub-group beneath it. |
| Include accounts by code | Automatically add accounts to the group based on their account code. You can use either the code prefix or a range of codes as the condition for including accounts in the group. |
| Move negative balances (switch) | When the balance is negative, move items to another section of the report. You can choose between moving either individual accounts or the entire group. |
| Opening balance | Xero calculates and shows the group balance at the beginning of the reporting period. When this option is chosen, the individual accounts show the movement during the period, rather than their closing balance. The opening balance plus account movements will equal the group total. This means that owner/beneficiary accounts don't need to be cleared out at the end of the financial year. Opening and closing balances, account movements for the period, are automatically calculated and changes made to these accounts will be reflected without needing to post manual journals. The option to show the opening balance is not available for all reports. |
| Total | Show the group total with the individual account totals. |

Edit an account group

To edit an existing group:

1. In the **Reporting** menu, select **All reports**.
2. Find and open the report to edit. You can use the search field in the top right corner.
3. Click **Edit layout**.
4. Click the group row, then edit the options in the **Group** panel.
5. To shift the group to another section of the report, click the group row, then drag and drop the group.
6. To summarise the group so it shows as a single line, click the arrow on the group row. Click the arrow again to expand the group.
7. Click **Update layout** to exit the layout and view the updated report.

To save the updated report as a draft, click **Save as**, then select **Draft**. To reuse the report's layout and formulas in future reports, click **Save as**, then select **Custom**.

Tip

If you show the opening balance for a Balance Sheet group, keep the group expanded.

Remove an account group

You can remove an account group without deleting the accounts from the report. When you remove an account group, you ungroup the accounts or move them to another group:

1. In the **Reporting** menu, select **All reports**.
2. Find and open the report to edit. You can use the search field in the top right corner.
3. Click **Edit layout**.
4. Click the group row to remove, then click the ungroup icon :

   - If the group is part of a formula, you get a warning message. You can click **Proceed anyway**, but you should [edit the affected formula](Create-or-edit-formulas-in-financial-reports.md).
   - If the rows need to be set elsewhere, Xero asks where to move them before removing the group.
5. Click **Update layout** to exit the layout and view the updated report.

To save the updated report as a draft, click **Save as**, then select **Draft**. To reuse the report's layout and formulas in future reports, click **Save as**, then select **Custom**.

Add, edit or delete a switch rule

### Add a switch rule

Add a switch rule to move accounts on a financial report if the balance is negative:

1. In the **Reporting** menu, select **All reports**.
2. Find and open the report to edit. You can use the search field in the top right corner.
3. Click **Edit layout**.
4. Click the group row you want to edit.
5. In the **Group** panel, click **Move negative balances (switch)**.
6. Select to switch if items are negative or the entire group is negative, and which group to switch to, then click **Done**.
7. Click **Update layout** to exit the layout and view the updated report.

To save the updated report as a draft, click **Save as**, then select **Draft**. To reuse the report's layout and formulas in future reports, click **Save as**, then select **Custom**.

### Edit or delete a switch rule

Account groups containing a switch rule are marked with an arrow icon . To edit or delete an existing switch rule:

1. In the **Reporting** menu, select **All reports**.
2. Find and open the financial report to edit. You can use the search field in the top right corner.
3. Click **Edit layout**.
4. Click the group row containing the switch rule.
5. In the **Group** panel, click **Move negative balances (switch)**, then:

   - Change the rule, then click **Done**
   - Click **Delete** to delete the switch rule
6. Click **Update layout** to exit the layout and view the updated report.

To save the updated report as a draft, click **Save as**, then select **Draft**. To reuse the report's layout and formulas in future reports, click **Save as**, then select **Custom**.

## What's next?

You can further [edit the layout of the financial report](Edit-layout-of-a-new-financial-report.md), or [publish it](Save-or-publish-a-report.md) when you're ready.