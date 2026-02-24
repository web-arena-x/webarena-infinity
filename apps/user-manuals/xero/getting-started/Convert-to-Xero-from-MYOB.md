# Convert to Xero from MYOB

Source: https://central.xero.com/s/article/Convert-to-Xero-from-MYOB

---

## Overview

- Import the chart of accounts, invoices, bills, and credit notes from MYOB into Xero.
- If you're not using a supported version of MYOB, you can use Xero’s template files and make the necessary adjustments.

Import your chart of accounts from MYOB

Tip

If you've already entered transactions in Xero, talk to your accountant or bookkeeper before following this process as it might have tax and reporting implications.

### Step one: Check the MYOB file can convert to Xero

You can import files exported from these versions of MYOB:

- MYOB Accounting or AccountRight Standard
- MYOB Accounting Plus or AccountRight Plus
- MYOB Essentials
- MYOB Premier or AccountRight Premier
- MYOB Premier Enterprise or AccountRight Enterprise
- MYOB AccountEdge for Mac editions

If you use a different version of MYOB, use Xero's default chart of accounts and [add or edit accounts as needed](Add-or-edit-an-account-in-your-chart-of-accounts.md).

If you're an accountant or bookkeeper using Xero HQ, you can add [Xero’s chart of accounts templates](Chart-of-accounts-templates-in-Xero-HQ.md) to new client organisations.

### Step two: Make adjustments in MYOB before exporting your file

Xero doesn’t use subaccounts but you can rename accounts, group them in your reports or use tracking instead.

If there are subaccounts in the MYOB chart of accounts, make adjustments in MYOB before exporting your file to account for [how you want to manage them](Ways-to-handle-subaccounts-from-your-previous-chart-of-accounts.md) in Xero.

### Step three: Export and check the MYOB file

Export your chart of accounts from MYOB in comma-separated values (CSV) format. If you want to include account balances, export your chart of accounts from MYOB as at the end of the month before your Xero conversion date.

When you've exported the chart of accounts, check the CSV file on your computer:

- Every column on the file must have a column header in the first row. Retain the column headers exported from MYOB.
- Your file can have up to 700 rows (1 column heading row + 699 value rows). If you have more than 699 accounts, you can [add the extra accounts to your chart of accounts](Add-or-edit-an-account-in-your-chart-of-accounts.md) after importing. However, we don’t recommend having more than 699 accounts as this can affect performance.
- Review how Xero maps MYOB accounts to Xero and make any changes needed to the exported file.

If you make changes to the file, save it in CSV format on your computer.

### Step four: Import and review the MYOB file into Xero

1. In the **Accounting** menu, select **Chart of accounts**.
2. Click **Import** and select **MYOB** as the system you're importing from.
3. Select whether your file includes balances. If **Yes**, enter your [conversion date](Setting-your-conversion-date.md).
4. Locate your saved file on your computer and click **Import**.

If any accounts with balances error during the import process, the accounts won’t import and the total balances for these accounts will be listed as **Adjustments**.

If you have an adjustment amount, you can review the list of errors and go back into MYOB to change the account so it imports correctly and repeats the import. Alternatively, you can leave the amount and reallocate the adjustment to another account from the Conversion Balances screen and add the account manually back into your chart of accounts or correct the adjustment later.

After you've imported a new chart of accounts, you'll need to [review the chart of accounts file import](Import-a-chart-of-accounts.md), making sure to check or re-enter your account balances so they match the new accounts and conversion date for the file imported. Once this is done, click **Confirm**.

You should then see your new chart of accounts in Xero. This will exclude those accounts listed in the summary as errors.

Any accounts already in Xero that weren't updated during the import process will be deleted or archived.

You’ll be returned to the chart of accounts screen. If your file includes a bank account, click the bank account name, select your bank account type (**Bank**, **Credit Card** or **PayPal**) and add your bank account number. Once this is done click **Save**.

If you’ve imported a chart of accounts that contains account balances, you’ll need to [save your conversion balances](Enter-conversion-balances.md).

Import MYOB invoices, bills and credit notes

Import sales invoices, purchase bills and credit notes into Xero that you've exported from MYOB as CSV files. Your import file might include extra information that can't be imported into Xero, for example, notes, journal memos or ship via details. This extra information will be ignored when you import the file.

You need to import sales and purchase transactions separately, on different CSV files.

Invoices, bills and credit notes are imported into Xero as drafts, so you’ll need to approve them after the import.

### Step one: Check we can import your MYOB file

- MYOB Accounts
- MYOB Accounting Plus
- MYOB Premier

If your version of MYOB isn't listed, you can use Xero's CSV template to import [sales invoices](Import-customer-invoices.md) or [credit notes and bills](Import-bills-and-credit-notes.md).

### Step two: Import the MYOB file

1. Either:
   - In the **Sales** menu, select **Sales overview** to import sales invoices and credit notes.
   - In the **Purchases** menu, select **Purchases** **overview** to import purchase bills and credit notes.
2. Click **Import** and select the MYOB format you're importing from.
3. Locate your saved CSV file on your computer and click **Import**.
4. Review the import message in Xero. If you're happy with the message, click **Complete Import**.

Once you've imported the draft invoices and credit notes into Xero, you can approve them.

Review how Xero maps MYOB accounts to Xero

If you get errors when you import your chart of accounts from MYOB, this information will help you troubleshoot.

### Code (MYOB: Account number)

Your account number in MYOB becomes your account code in Xero. Change the account number in your MYOB CSV file before you import it into Xero if it doesn't meet these criteria:

- The code is unique.
- The code includes letters, numbers or symbols, up to 10 characters. You can use symbols within the code, but not at the start.

### Name (MYOB: Account name)

Ensure your account names meet these criteria:

- The name is unique.
- The name uses letters, numbers or symbols, up to 150 characters. You can use symbols within the name, but not at the start.
- For bank accounts, the name has fewer than 30 characters so it fits on the [homepage](Your-Xero-dashboard.md).

### Type (MYOB: Account type)

Xero uses the [account type](Components-of-an-account-in-your-chart-of-accounts.md) to determine where the account appears in your financial reports. Don't change your MYOB account types in your import file. Xero maps them automatically.

Xero maps MYOB account types as follows:

| MYOB account type | Xero account type |
| --- | --- |
| Accounts Payable | Current Liability |
| Accounts Receivable | Current Asset |
| Asset | Current Asset |
| Bank | Current Asset (Select Bank, Credit Card or PayPal account during the import process) |
| Cost of Sales | Direct Costs |
| Credit Card | Current Liability (Select Credit Card account during the import process) |
| Current Asset | Current Asset |
| Current Liability | Current Liability |
| Depreciation | Depreciation |
| Direct Cost | Direct Costs |
| Equity | Equity |
| Expense | Expense |
| Expenses | Expense |
| Fixed Asset | Fixed Asset |
| Income | Sales |
| Liability | Current Liability |
| Other Asset | Non-current Asset |
| Other Expense | Expense |
| Other Income | Other Income |
| Other Liability | Current Liability |
| Other Revenue | Other Income |
| Overhead | Overhead |
| Prepayment | Current Asset |
| Revenue | Revenue |
| Sale | Sales |
| Term Liability | Non-current Liability |

In addition, if you've used any of the following account names to group accounts in MYOB, Xero imports the accounts within the group and assigns them the Xero account type shown:

| Account name used to group in MYOB | Xero account type |
| --- | --- |
| Current Assets | Current Asset |
| Fixed Assets | Fixed Asset |
| Current Liabilities | Current Liability |
| Long Term Liability | Non-current Liability |
| Other Current Liabilities | Current Liability |
| Other Long Term Liabilities | Non-current Liability |

### Tax rate (MYOB: GST code)

Xero maps MYOB GST codes to [Xero tax rates](Components-of-an-account-in-your-chart-of-accounts.md). If an account doesn't have a GST code, Xero imports the account with the rate **No GST**, which you can update later.

| MYOB GST code | Xero tax rate |
| --- | --- |
| E | No GST |
| None | No GST |
| N-T | No GST |
| RRR | Zero Rated |
| S15 | 15% GST on Income (where account category is revenue or liability) |
| S15 | 15% GST on Expenses (where account category is expense, asset or equity) |
| Zero Rated | Zero Rated |

### System accounts (MYOB: System accounts)

Xero uses [system accounts](Locked-and-system-accounts-in-your-chart-of-accounts.md) for specific reporting or accounting purposes. One of these accounts, Tracking Transfers, doesn't have a corresponding system account in MYOB, so Xero creates it when you import your MYOB file.

Here's how Xero maps MYOB's system accounts to Xero's system accounts:

| MYOB system account name | Xero system account name | Xero system account type | Xero system account tax rate |
| --- | --- | --- | --- |
| Accounts Receivable Trade Debtors | Accounts Receivable | Current Asset | No GST |
| Accounts Payable Trade Creditors | Accounts Payable | Current Liability | No GST |
| Unpaid Expense Claims | Unpaid Expense Claims | Current Liability | No GST |
| GST | GST | Current Liability | No GST |
| Historical Balancing Historical Adjustment | Historical Adjustment | Current Liability | No GST |
| Rounding | Rounding | Current Liability | No GST |
| Retained Earnings | Retained Earnings | Equity | No GST |

## What's next?

If there are errors, or fewer invoices are listed than in your file, we suggest you use our CSV template to import [sales invoices](Import-customer-invoices.md) or [credit notes and bills](Import-bills-and-credit-notes.md) into Xero.