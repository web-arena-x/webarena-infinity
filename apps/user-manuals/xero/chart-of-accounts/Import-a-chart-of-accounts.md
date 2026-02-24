# Import a chart of accounts

Source: https://central.xero.com/s/article/Import-a-chart-of-accounts

---

## Overview

- Import your own chart of accounts to replace the Xero default accounts or to update multiple accounts in bulk.
- Follow these steps if it's your first time using Xero or if you’re importing a new set of accounts.

Tip

See [BankLink](Convert-to-Xero-from-BankLink.md) or[MYOB](Convert-to-Xero-from-MYOB.md) if you're converting from one of those accounting systems.

**1** Before you start

When you import a chart of accounts, Xero updates the existing accounts exactly as per the import file.

- If you don't want to make changes to an account and want it to remain in the organisation, keep it in the import file. If you delete the account from the file, Xero archives the account when you import the file.
- You can import a maximum of 1000 rows, including the column header. If you've got more than 999 accounts, add the other accounts manually. We recommend a limit of 699 accounts per organisation to avoid page loading and slowness issues in Xero.
- If the file includes account balances, these import as [conversion balances](Enter-conversion-balances.md) and overwrite any existing conversion balances in the organisation. If you don’t want to overwrite them or if you're unsure, leave the **Balance** column in the import file blank. Once you've imported the file, you need to save the balances on the **Conversion Balances** screen.
- You can't import balances in other currencies. If the organisation uses foreign currencies, import the accounts in the organisation's base currency, then add accounts for the foreign currency balances later. Talk to your accountant or bookkeeper if you’re unsure.
- If you change both the **Code** and **Name** of an account in the import file at the same time, Xero archives the account codes and creates new ones. To change both of these fields, export the file, modify it, then import them separately.
- ​​​Check the tax rates in the file also exist in Xero. If the rates on an import file aren't in Xero, they default to **No GST (0%)**.

**2** Download a file and prepare the data

Import your own chart of accounts, or choose a file from your old accounting system or another Xero organisation. We recommend using the template file that can be downloaded from a Xero organisation.

To download the template file and populate it:

1. Log in to your Xero organisation, or the demo company.
2. In the **Accounting** menu, select **Chart of accounts**.
3. Click **Import**.
4. Under **Example files**, click the link to download a GST-registered or non-GST registered file.
5. Find the downloaded file on your computer and open it.
6. Complete all the compulsory fields – they're marked with an asterix (\*) on the column header in the file.

| Field | Description |
| --- | --- |
| **Code\*** | Use letters, numbers or symbols, up to 10 characters. You can use symbols within the code, but not at the start. The account code must be unique. Xero uses [tracking categories](Set-up-tracking-categories.md) instead of sub-accounts. |
| **Name\*** | Use letters, numbers or symbols, up to 150 characters. You can use symbols within the name, but not at the start. The name must be unique. |
| **Type\*** | You must use one of [these account types](Components-of-an-account-in-your-chart-of-accounts.md) (spelled and formatted the same). Xero only uses one accounts receivable system (control) account and one accounts payable system (control) account. If you previously used multiple control accounts, you need to merge them in Xero. |
| **Tax Code\*** | [Add a tax rate](/s/article/Add-or-edit-tax-rates-NZ) for each account. If you don't select a tax rate, Xero imports the account with the rate **No GST**, which you can update later. For bank accounts, you must use the code **No GST**. If you use a custom tax rate, include the rate value in brackets. For example, 'Tax on Expenses (8.5%)'. |
| **Reporting Name** | (Advisor role only) If you're a practice user, you can add a reporting name to an account. The reporting name appears on reports if they’re in a [report template](Get-started-with-report-templates.md) and **Edit layout** is available. The reporting name option is available for all accounts except those with the account type **Bank**. The name doesn't have to be unique. |
| **Description** | You can add a description to all accounts except bank accounts. For bank accounts, leave the field blank. Consider adding descriptions to accounts your users can choose when they enter receipts into expense claims. This helps users who are unfamiliar with the chart of accounts. |
| **Dashboard** | Specify if the account should appear in the [account watchlist](Set-up-the-dashboard-account-watchlist.md) on your dashboard. Enter only **Yes** or **No**. For bank accounts, this field must be **No** or left blank. |
| **Expense claims** | Specify if the account should appear in the drop-down list of accounts when entering an [expense claim](Create-a-new-expense.md) receipt. Enter only **Yes** or **No**. For bank accounts, this field must be **No** or left blank. |
| **Enable Payments** | Specify if the account you're creating should [appear in the drop-down list of accounts](Enable-payments-to-an-account.md) when you're entering a payment directly on an invoice, bill or expense claim. Enter only **Yes** or **No**. For bank accounts, this field must be **No** or left blank. |
| **Balance** | If you want to import account balances, enter the balances immediately prior to your [conversion date](Setting-your-conversion-date.md). Xero imports positive balances as debits, and negative balances as credits. Xero ignores symbols and non-numeric data, other than negative signs and brackets (showing a negative balance). If you don't want to import balances, leave the **Balance** column blank. |

When you're formatting the file, please consider the following:

- Every column on the import file has a column header.
- If you don't want to include an optional field, delete the column or leave all cells in the column blank.
- The **Code** column is formatted as text.
- Microsoft Excel removes the leading zeros from account codes in an exported chart of accounts CSV file.
- If your file has non-English characters, save as a text file in Microsoft Excel. This ensures any non-Roman (UTF8) characters aren't removed from the file. You can then import the text file into Xero using the CSV import process.

If an existing account in Xero is locked, it can't be updated. If you want to update the existing account using the file, the name and description fields will update, but not the account code. Instead, Xero creates a new account. If you don't want both accounts, make the changes directly in Xero, rather than using the import template.

If the existing accounts in Xero have balances, they'll be updated or archived. You can still view archived accounts in Xero and restore them. You also need to update the account balances after importing a new chart of accounts.

**3** Import the file into Xero

Once you've formatted the file, save it to your computer in CSV format, then import it into Xero:

1. In the **Accounting** menu, select **Chart of accounts**.
2. Click **Import**.
3. Select the system you're importing from. If you're using a Xero template file, select **Xero**.
4. Select whether the file includes balances. If **Yes**, enter your [conversion date](Setting-your-conversion-date.md).
5. Click **Browse** to locate the file.
6. Click **Import** to view a summary of the accounts to import.

When you import your chart of account, the Import Summary shows the accounts in the file for you to review.

**4** Review your imported accounts

The summary shows the accounts in the file that are included and excluded from the import.

Includes:

- **[Number of] new accounts** – includes updating the code of an existing account, as Xero treats this as a new account
- **[Number of] updated accounts** – the number of existing accounts that will be updated, including changing the account name or description
- **[Number of] system accounts** – will automatically be added if needed
- No existing bank accounts will be changed

Excludes:

- **[Number of] accounts** **that didn't import due to errors** – includes those that were duplicates or missing mandatory information
- **[Number of] accounts** **that were deleted or archived** –any existing accounts in Xero that aren’t in the file you're importing will be archived or deleted

Click **View** next to each summary item to see the accounts included or excluded and why.

If any accounts, including bank accounts, couldn't import due to errors, review the imported accounts before saving the file. If all the accounts import successfully, click **Confirm** to accept the import.

**4** Review errors in your imported accounts

Accounts with errors or changes are listed in the **Import Summary**. You can still confirm the import without addressing any of these errors, but these accounts won't import.

- Click **View descriptions of all errors and changes** to see why the listed accounts didn't import.
- The line number refers to the line in the file that has an error and the **Description** field explains why it didn't import. **Line 1** is the mandatory first line containing the Xero column headings in the file.
- If the error is on an account that already exists in Xero, the existing account will remain unchanged when you confirm the import.
- If the error is on a new account that you've included in your file, it won't be included when you confirm the import and won't be in the new chart of accounts in Xero.
- You can either go back to your original file and change the accounts and re-import them, or confirm the import without the accounts that cause an error. You can manually add later.
- If you're working with a text (TXT) file in the Notepad program, line numbers will display if you've set up the program to show the status bar (do this from the **View** menu).

**5** Confirm your imported bank and credit card accounts

When you import a chart of accounts, Xero recognises certain accounts as bank accounts and requests extra information. The type of information needed depends on whether the account is a bank account, credit card account or PayPal account.

If your chart of accounts import file includes accounts with the account type **Bank**, Xero requests further information during the import process.

- Select the correct account type for each account. If you don't want to set up a bank feed or import bank statements for the account, select **Current Asset**.
- If multicurrency is set up in the organisation, you can choose a non-base currency for your account.
- Ensure that you enter the account number correctly so if you set up a bank feed, Xero can match it up.
- If you don't know the account number, leave the **Account Number** field blank. You can add the account number later.

**Save** the information you enter.

## What's next?

If you didn't include balances in the import file, [add conversion balances](Enter-conversion-balances.md) to the accounts.