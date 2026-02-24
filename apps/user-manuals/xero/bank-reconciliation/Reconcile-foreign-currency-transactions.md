# Reconcile foreign currency transactions

Source: https://central.xero.com/s/article/Reconcile-foreign-currency-transactions

---

## Overview

- Reconcile transactions when the currency of the statement line in your bank account differs from the currency of the invoice or bill in Xero.

Reconcile a base currency statement line with a foreign currency transaction

Follow these steps if the statement line is in your organisation’s base currency bank account, but the invoice or bill in Xero is in a foreign currency. For example, you’ve received a payment into your USD bank account for an invoice entered in EUR.

1. In the **Accounting**menu, select **Bank accounts**.
2. For the bank account you want to reconcile, click **Reconcile [number] items**.
3. For the relevant bank statement line, click **Find & Match**.
4. Clear the **Show [currency] items only** checkbox to display both base currency and foreign currency invoices or bills.
5. Select the checkbox for the foreign currency transaction. To help you find it, click any column header to change the transaction order, or search by name, reference or amount.
6. Click **Reconcile**.

Reconcile a foreign currency statement line with a base currency transaction

Follow these steps if the bank statement line is in a foreign currency bank account, but the invoice or bill in Xero is in your organisation’s base currency. For example, you’ve received a payment into an EUR bank account for an invoice entered in USD.

1. In the **Accounting**menu, select **Bank accounts**.
2. For the bank account you want to reconcile, click **Reconcile [number] items**.
3. For the relevant bank statement line, click **Find & Match**.
4. Clear the **Show [currency] items only** checkbox to display both base currency and foreign currency invoices or bills.
5. Select the checkbox for the base currency transaction. To help you find it, click any column header to change the transaction order, or search by name, reference or amount.
6. If the payment includes a bank fee for the foreign currency exchange, click **Adjustments**, select **Bank fee**, then add the fee details.
7. Click **Reconcile**.

Reconcile a foreign currency transaction paid in the same foreign currency

Follow these steps if neither the statement and transaction in Xero are in your organisation’s base currency, and both are in the same foreign currency. For example, your organisation’s base currency is USD, but you’ve received a payment into an EUR bank account for an invoice entered in EUR.

1. In the **Accounting** menu, select **Bank accounts**.
2. For the foreign currency bank account you want to reconcile, click **Reconcile [number] items**.
3. For the relevant bank statement line, click **Find & Match**.
4. Find and select the checkbox for the relevant transaction. To help you find it, click any column header to change the transaction order or search by name, reference or amount.
5. If the payment includes a bank fee for the foreign currency exchange, click **Adjustments**, select **Bank fee**,then add the fee details.
6. Click **Reconcile**.

Reconcile a foreign currency bill paid in another foreign currency

### How it works

If both the bank statement line and the bill are in different currencies and neither is the organisation’s base currency, you need to reconcile these through a clearing account. For example, you have an EUR dollar bill that you’ve paid in USD, but the organisation’s base currency is NZD.

### Add a clearing account in your chart of accounts

Because the bill and payment are in different currencies, you need to use a clearing account in order to convert them both to the organisation’s base currency.

If you don't already have a clearing account, add one:

1. In the **Accounting** menu, select **Chart of accounts**.
2. Click **Add Account**, then fill out the relevant fields. Make sure you enter a descriptive name for the account. If you’re not sure what account type to select, talk to your accounting advisor.
3. Select the **Enable payments to this account** checkbox.
4. Click **Save**.

### Reconcile the statement line with a spend money transaction

Because the statement line is in a foreign currency, you need to create a spend money transaction to convert it to the organisation’s base currency.

1. In the **Accounting**menu, select **Bank accounts**.
2. For the bank account you want to reconcile, click **Reconcile [number] items**.
3. For the relevant bank statement line, select the **Create** tab.
4. Fill in the transaction details. In the **What** field, select the clearing account.
5. (Optional) To add more details to the transaction, click **Add details**, enter the details, then click **Save Transaction**.
6. Click **OK** to create the transaction and reconcile it.

### Check the Account Transactions report

Run the [Account Transactions report](Account-Transactions-report-New.md) to see the base currency value the foreign currency payment converts to.

1. In the **Reporting** menu, select **All reports**.
2. Under **Transactions**, click **Account Transactions**.
3. Under **Accounts**, select the clearing account.
4. Set a date range that includes the date of the bank statement line, then click **Update**.
5. Make a note of the base currency value the statement line amount converts to.

### Record payment on the bill

Record payment on the [purchase bill](Record-payment-of-a-bill.md) using the following details:

- Confirm the amount in the **Amount Paid [currency]** field is correct. Xero defaults to paying the bill in full.
- In the **Date Paid** field, enter the same date as on the spend money transaction.
- In the **Paid From** field, select the clearing account you set up earlier.
- Enter the exchange rate to apply to the bill. To calculate the exchange rate, divide the bill's **Amount Paid** value by the base currency value recorded in the clearing account, as per the Account Transactions report.

The payment transaction is now reconciled, and the clearing account should offset to 0.00. You can re-run the Account Transactions report to check this.

Reconcile a foreign currency invoice paid in another foreign currency

### How it works

If both the bank statement line and the invoice are in different currencies and neither is the organisation’s base currency, you need to reconcile these through a clearing bank account for the same currency as the invoice. For example, you have an EUR dollar invoice that’s been paid in USD, but the organisation’s base currency is NZD.

### Add a clearing bank account in the currency of the invoice

If you don't already have a clearing bank account, add one:

1. In the **Accounting** menu, select **Bank accounts**.
2. Click **Add bank account**.
3. In the top right hand corner of the screen, click **Add without bank feed**, then click **Continue**.
4. Under **Bank name** and **Account name**, enter a name for the clearing account, such as **[Currency] clearing bank account**.
5. Under **Account Type**, select **Other**.
6. Under **Account number**, enter a placeholder number, such as **00000**.
7. Under **Currency**, select the currency of the invoice.
8. Click **Add account**.

### Record payment on the invoice

Record payment on the [sales invoice](Record-payment-of-a-sales-invoice.md) using the following details:

- Confirm the amount in the **Amount Paid [currency]** field is correct. Xero defaults to paying the invoice in full.
- In the **Paid To** field, select the clearing bank account.

### Reconcile the invoice payment

1. In the **Accounting**menu, select **Bank accounts**.
2. For the bank account you want to reconcile, click **Reconcile [number] items**.
3. For the relevant bank statement line, select the **Transfer** tab.
4. Select the clearing bank account and enter the invoice number as a reference.
5. Under **Currency Conversion**, in the **Amount [currency]** field, enter the amount of the invoice.
6. Click **Reconcile**.

The payment transaction is now reconciled, and the clearing bank account balance should offset to 0.00. If you want to, [manually mark the transactions as reconciled](Reconcile-an-account-transaction-without-an-imported-bank-statement.md) in the clearing account or [archive the account](Delete-or-archive-a-bank-account.md).

## What's next?

Now you've reconciled your foreign currency transaction, run the [Foreign Currency Gains and Losses report](Foreign-Currency-Gains-and-Losses-report.md).