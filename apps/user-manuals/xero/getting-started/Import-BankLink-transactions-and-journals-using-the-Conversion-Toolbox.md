# Import BankLink transactions using the Conversion Toolbox

Source: https://central.xero.com/s/article/Import-BankLink-transactions-and-journals-using-the-Conversion-Toolbox

---

## Overview

- Use the Conversion Toolbox to import your client’s bank accounts, transactions and manual journals from BankLink.

Warning

Don't make any changes to data in the exported BankLink files before importing them into Xero.

What you need to know

### How it works

Import a precoded, comma-separated values (CSV) bank transactions file from your client's BankLink account to create reconciled bank statement lines and account transactions in Xero.

Any payments coded to more than one account in BankLink show as separate account transactions in Xero.

### Before you start

If you plan to import your client’s chart of accounts, do this first. You can use the [Conversion Toolbox chart of accounts import tool](Import-a-chart-of-accounts-using-the-Conversion-Toolbox.md), or [import your own](Import-a-chart-of-accounts.md).

If the bank accounts are already set up in Xero, [assign them chart of account codes](Add-or-edit-an-account-in-your-chart-of-accounts.md) so they show during the mapping process. If the bank accounts aren't set up in Xero, export a file from BankLink or create a file that contains the account names and numbers, then save it in CSV format.

If the BankLink file uses subaccounts, [add tracking categories](Set-up-tracking-categories.md) in Xero.

Add any [tax rates](Add-or-edit-tax-rates.md) that aren't available in Xero by default.

If you're importing bank transactions for the period before starting a bank feed, check that the start date for the [bank statements](View-bank-statements-and-bank-statement-lines.md) in Xero matches the feed.

Code all transactions in BankLink and use a clearing or suspense account if you plan to reconcile them later in Xero.

If any transactions have purple transfer flags, you'll need to clear them.

Import the files

### Upload the files

1. Open the [Conversion Toolbox](https://conversiontoolbox.xero.com/Member/Login?ReturnUrl=%2f), then click **Ready to connect to Xero**.
2. Click **Allow access**, then select the client organisation.
3. Click **BankLink Transactions & Journals**.
4. Click **Select CSV Files to Upload**, select the import file, then click **Start Conversion**.
5. In the **File Content type** column, select the files you want to import:
   - **Chart of Accounts** for your chart of accounts file
   - **Transactions** for your bank transactions files
   - **Journals** for your journal file
   - (Optional) **Bank Accounts** for your bank accounts list file
6. Click **Start Conversion**.

### Map the import fields

1. Confirm the mapping of the imported tax type to the Xero tax type, click **Next Step**, then click **Next Step** again.
2. Map the **BankLink Account Name** to the **Xero Bank Account**.
3. (Optional) If you're importing reconciled transactions, click **Add Account** and enter or confirm the bank account details. If you're importing unreconciled transactions, don't map the account field.
4. Click **Create Account**, then click **Next Step**.
5. (Optional) Map the import fields:
   - **Account Type** – add or adjust as needed.
   - **Xero Account** – add or adjust as needed. If you add an account, enter **Name**, **Code**, **Account Type** and **Tax Rate**.
   - (Optional) **Tracking** – if the organisation uses tracking, select tracking to apply for each account.

### Review and confirm the import

1. If you see the **Preview** screen, review any items that appear.
2. Click **Next Step**, then click **Next Step** again.
3. (Optional) If you're importing bank transactions, click **Download** to download the coded bank statement CSV file, then click **Next Step**.
4. (Optional) If you're importing journals, select whether to import them as **Draft** or **Posted**, then click **Next Step**.
5. Review the import details and note any issues.
6. Click **Previous step** to make any changes within the toolbox. If you need to make changes to the import file, you'll need to start from step 3 under Upload the files.
7. Click **Next Step**.
8. Review and fix any issues highlighted on the **Preview** screen, then click **Finish**.

## What's next?

Check the other types of [client data](https://central.xero.com/s/topic/0TO1N0000017ldLWAQ/conversion-toolbox) you can import.