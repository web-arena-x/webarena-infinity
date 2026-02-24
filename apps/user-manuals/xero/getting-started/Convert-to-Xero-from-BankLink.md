# Convert to Xero from BankLink

Source: https://central.xero.com/s/article/Convert-to-Xero-from-BankLink

---

## Overview

- To convert to Xero, import the chart of accounts from BankLink.
- Xero automatically maps BankLink’s accounts to the corresponding accounts in Xero.

Import your chart of accounts from BankLink Practice

Tip

Import your chart of accounts from BankLink into Xero before you start entering transactions in Xero.

### Step one: Make adjustments in BankLink before exporting the file

- Xero uses tracking instead of subcodes. If you have subcodes in your BankLink chart of accounts, make adjustments in BankLink to take into account tracking categories and options you might apply in Xero.
- Change any account in BankLink with an account group of **Not Applicable** or **Unknown**. Xero won't import accounts with these account groups.

### Step two: Export and check BankLink file

Export the chart of accounts from BankLink in comma-separated values (CSV) format.

After you've exported the chart of accounts, check the CSV file.

- All columns must have a header in the first row. Retain the column headers exported from BankLink.
- Your file can have up to 500 rows (1 column heading row + 499 value rows). If you have more than 499 accounts, you'll need to [add the extra accounts to your chart of accounts](Import-a-chart-of-accounts.md) after importing.
- Review how Xero maps BankLink accounts to Xero and make any changes needed. If you need to make changes, we suggest that you make them in the CSV file before you import it into Xero.

### Step three: Import BankLink file into Xero

1. In the **Accounting** menu, select **Chart of accounts**.
2. Click **Import**, then select the **BankLink** system option.
3. Click **Browse** to find and select your saved file on your computer, then click **Import**.
4. [Review the chart of accounts file import](Import-a-chart-of-accounts.md), then click **Confirm**.
5. If your import file includes bank accounts, select your bank account type (**Bank**, **Credit Card**, or **PayPal**) and add your bank account number.
6. **Save** your selection.

Troubleshoot an import error

If you get errors when you import your BankLink chart of accounts, this information will help you troubleshoot.

### Code (BankLink: Account Code)

Your account code in BankLink becomes your account code in Xero. Change the account code in your BankLink CSV file before you import it into Xero if it doesn't meet these criteria:

- The code is unique.
- The code includes letters, numbers or symbols, up to 10 characters. You can use symbols within the code, but not at the start.

### Name (BankLink: Account Description)

Your account description in BankLink becomes your account name in Xero. Change the account description in your BankLink CSV file before you import it into Xero if it doesn't meet these criteria:

- The name is unique.
- The name uses letters, numbers or symbols, up to 150 characters. You can use symbols within the name, but not at the start.
- For bank accounts, the name has fewer than 30 characters so it fits on the [Xero homepage](Your-Xero-dashboard.md).

### Type (BankLink: Account Group)

Xero uses the [account type](Components-of-an-account-in-your-chart-of-accounts.md) to determine where the account appears in your financial reports. Don't change your BankLink account groups in your import file. Xero maps account groups automatically.

Note that Xero has a single GST account. All GST accounts in BankLink are merged into the single account.

Xero maps BankLink account groups as follows:

| BankLink account group | Xero account type |
| --- | --- |
| Debtors | Current Assets |
| Cash on Hand | Bank |
| Current Asset | Current Assets |
| Stock on Hand | Current Assets |
| Creditors | Current Liabilities |
| Current Liability | Current Liabilities |
| Closing Stock | Direct Costs |
| Direct Expense | Direct Costs |
| Opening Stock | Direct Costs |
| Purchases | Direct Costs |
| GST Payable | Current Liabilities |
| GST Receivable | Current Liabilities |
| Equity | Equity |
| Expense | Expenses |
| Other Expense | Expenses |
| Fixed Asset | Fixed Assets |
| Not Applicable | No Xero equivalent - Xero won't import accounts with this account group. Change the account group before you export your BankLink file. |
| Unknown (CR) | No Xero equivalent - Xero won't import accounts with this account group. Change the account group before you export your BankLink file. |
| Unknown (DR) | No Xero equivalent - Xero won't import accounts with this account group. Change the account group before you export your BankLink file. |
| Other Income | Other Income |
| Retained Earnings | Equity |
| Income | Revenue |
| Long Term Liability | Non-current Liabilities |

### Tax rate (BankLink: GST Class)

Xero maps BankLink GST classes to [Xero tax rates](Components-of-an-account-in-your-chart-of-accounts.md). If an account doesn't have a GST class, Xero imports the account with the rate **No GST**, which you can update later.

If you're using a practice solution other than MYOB Accountants Office, Xero won't recognise your GST classes. Rename the GST classes in your import file to the following BankLink GST classes so Xero imports them correctly.

If an account has a GST class in BankLink of **Not Applicable** or **N Unallocated**, Xero won't import the account. Change the GST class in the import file before you import it into Xero.

| BankLink GST class | Xero tax rate |
| --- | --- |
| Not Applicable | Accounts with this GST class won't be imported into Xero. |
| I Expenditure I Purchase % GST Expenditure | 15% GST on Expenses |
| O Income O Sales % GST Income | 15% GST on Income |
| E Exempt % Exempt | No GST |
| Z Zero Rated % Zero Rated | Zero Rated |
| N Unallocated | Accounts with this GST class won't be imported into Xero. |

### System accounts (BankLink: System accounts)

Xero uses some accounts in the chart of accounts, called [system accounts](Locked-and-system-accounts-in-your-chart-of-accounts.md), for special purposes. There are some system accounts in Xero which don't have an equivalent in BankLink, for example, Unpaid Expense Claims and Historical Adjustment. Xero creates these system accounts when you import your BankLink file.

Here's how Xero maps BankLink's system accounts to Xero's system accounts:

| BankLink system account name | Xero system account name | Xero system account type | Xero system account tax rate |
| --- | --- | --- | --- |
| Accounts Receivable Debtors | Accounts Receivable | Current Assets | No GST |
| Accounts Payable Creditors | Accounts Payable | Current Liabilities | No GST |
| GST | GST | Current Liabilities | No GST |
| Retained Earnings | Retained Earnings | Equity | No GST |

## What's next?

You can [add your conversion balances](Enter-conversion-balances.md) to make sure your reporting and bank balances are accurate.