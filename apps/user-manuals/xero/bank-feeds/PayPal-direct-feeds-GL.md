# PayPal direct feeds

Source: https://central.xero.com/s/article/PayPal-direct-feeds-GL

---

## Overview

- Get transactions from PayPal automatically imported into Xero.
- Check your accounts are eligible, and apply online.
- Reconcile gateway payment transactions

What you need to know

Warning

PayPal accounts in Japan and Israel can't connect to a direct feed.

### About PayPal feeds

- Once your feed is connected, bank transactions will import into Xero every 12 hours.
- Refresh feeds to bring in the latest transactions any time.
- Payments made from a bank account or credit card that are processed through PayPal (and aren't PayPal funds) will import into your PayPal account in Xero. You can then reconcile them using transfers from your bank account.
- You need to be a PayPal primary user to set up the feed.
- If you already have a PayPal account connected to your Xero organisation, you need to [set up one account for each currency](PayPal.md) that you accept payment in. If this is the first time you’re connecting a PayPal account, you only need one bank account in Xero.

### Eligible account types

- Business accounts
- Personal accounts

If your account type isn't eligible for direct feeds, you can [manually import](Manually-import-a-PayPal-statement.md) a bank statement.

### Transactions included in the direct feed

The PayPal feed only includes transactions in the same currency of the PayPal account you set up in Xero and that don't have a value of 0.00.

All Balance Affecting Transactions are also included in the direct feed. This helps track the movement between your PayPal funds. Balance Affecting Transactions include:

- Refunds and Fund Reversals.
- Temporary Hold and Release transactions – we will filter out these transactions if they occur within the same refresh period of 12 hours, and correspond to one another, ie a release of a hold.
- Transactions made using funds from a credit card or separate bank account – these are gateway transactions.

How to set up your PayPal direct feed

If you’re connecting a new PayPal account to your organisation for the first time, set up a single PayPal payment service and feed. You’ll then be able to accept payments in any currency.

If you have an existing PayPal account connected to your organisation, add a bank account for each currency you accept payment in, then set up the feed for each account in the currency.

To set up the PayPal feed:

1. In the **Accounting** menu, select **Bank accounts**.
2. Click **Add bank account**.
3. In the **Search** field, start typing PayPal, then select **PayPal** from the list.
4. Click **Continue and log in to bank**.
5. Enter your PayPal email address and password, then click **Log In**.
6. Click **Agree and Connect** to confirm you authorise Xero to search your transactions for items that match specific criteria.
7. Click **Go back to Xero**.
8. If you have an existing account, you’ll have the option to select the bank account from the dropdown to import the feeds into Xero. If you’re unable to see the dropdown, add the currency in Xero first.
9. Check the start date for each bank account to import your transactions. Click the date if you need to change the start date.
10. Click **Finish**.

Once connected, your bank transactions will immediately import into Xero. If you'd like to import earlier transactions after the feed has started, you'll need to [manually import](Manually-import-a-PayPal-statement.md) them.

You can connect extra PayPal currencies at any time. Add a new bank account in Xero and select the new currency you'd like to connect. If you have an existing account you’ll have the option to select that account.

If you’re connecting a new account, you only need one bank account to accept multiple currencies.

How to reconcile gateway transactions

If there’s a gateway payment, three bank statement lines will import into Xero for one transaction. They’re a spend and receive statement line in the PayPal account and a spend statement line in the bank/credit card account.

For example:

- You make a purchase of $100.
- The related bank or credit card account imports a statement line of -$100.
- The PayPal feed imports a statement line of $100 (money received from bank or credit card).
- The PayPal feed imports a statement line of -$100 (money spent).

To reconcile these transactions:

1. Make sure you've set up your bank or credit card as an account in Xero.
2. Create a transfer transaction from your bank account or credit card account to PayPal account.
3. Reconcile the matching statement line in your PayPal account against this bank transfer transaction.

This will leave you with a remaining statement line in your PayPal account which you can reconcile against the actual expense. Use the Invoice ID in the description field to help identify the correct transaction. If the transaction isn't already in Xero, you can create a spend money transaction.

Refresh PayPal feeds

If you don't want to wait until the next automatic import, refresh a bank feed at any time to import the latest transactions into Xero.

1. In the **Accounting** menu, select **Bank accounts**.
2. Find the PayPal account you want to refresh. Click the menu icon , then select **Refresh Bank Feed**.

Alternatively, if the bank account you want to refresh displays on your homepage, click the menu icon , then select **Refresh bank feed**.

## What's next?

You can [set up PayPal as a payment service](PayPal.md), which means customers can pay invoices online.