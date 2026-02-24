# Reconcile your bank account

Source: https://central.xero.com/s/article/Reconcile-your-bank-account

---

## Overview

- Review imported bank statement lines and match them to transactions in Xero.

Tip

Try out bank reconciliation in the [Xero demo company](Use-the-demo-company.md). It has most of the features of an actual Xero organisation so you can explore Xero without entering your own data.

Web iOS Android

## Step 1: Prepare to reconcile

1. Understand [how bank reconciliation in Xero works](Bank-reconciliation-in-Xero.md) before you reconcile any transactions.
2. Make sure you've entered all the transactions into Xero. These might include invoices, bills, credit notes, expense claims, or cash transactions.
3. Check the [opening balance of the bank account](Add-your-opening-bank-balances-in-Xero.md) is correct and the statement balance in Xero matches the balance in your actual bank account.

## Step 2: Review the bank account

### View unreconciled statement lines

When a bank statement is imported, the bank account widget on the homepage shows the number of bank statement lines ready to be reconciled. If a bank account doesn’t show on your homepage, in the **Accounting** menu, select **Bank accounts**.

For the bank account you want to reconcile, click **Reconcile [number] items**.

If **Reconcile [number] items** doesn’t display, it indicates there are no bank statement lines to reconcile. If you think there should be statement lines to reconcile but there aren’t any, it might be because:

- The statement lines relate to dates before a bank feed was connected, or a bank feed isn’t available. If this is the case, you need to [manually import the bank statement lines](About-manually-importing-bank-statements.md).
- The [bank feed is delayed](Check-if-your-bank-feed-is-late.md).

The bank statement lines display on the left hand side of the **Reconcile** tab. For each individual bank statement line, work through the steps below to reconcile it against an account transaction.

Your aim is to match each statement line in the bank account to an existing transaction in Xero, or create a transaction during the reconciliation process.

### Filter or search for statement lines

You can filter the list of statement lines by date or amount. Use search to find specific statement lines to reconcile.

1. For the bank account you want to reconcile, click **Reconcile [number] items**.
2. On the reconciliation screen:

   - To search for a statement line, enter its details into the search bar.
   - To filter the list, click **Filter**, select a **Start date** or **End date,** or enter an **Amount range**, then click **Apply.**

Filters are cumulative and work together. To remove all filters, click **Filter [number]**, then click **Reset filters**.

## Step 3: Match to an existing transaction in Xero

If an existing transaction has already been created in Xero that relates to the statement line, the bank reconciliation process is simply matching the two.

Existing transactions might include sales and purchase documents such as invoices, bills, expense claims, payment transactions or spend and receive money transactions.

If the bank statement line relates to a transfer of funds from one bank account to another, you only need to create the transfer transaction in one account. If you’ve already created the transaction in the other account, just click **OK** to reconcile it.

### Accept a matched transaction

Tip

You can change how your transactions display during bank reconciliation. Select the **Compact view** switch to see a more condensed view that displays more transactions per page.

Xero first generates a list of possible account transactions to match against the statement line. These matches are made by comparing all the information in the statement line against all the information in the account transaction. The account transaction that has the most similarities to the bank statement line is offered as the suggested match. If there are multiple transactions that match, Xero looks for the one with the closest due date.

Sometimes there are multiple transactions that match, so the most likely transaction is suggested and a link is provided to the other alternatives.

- If the correct transaction is suggested, click **OK** to accept the match and reconcile.
- If you don’t want to accept the match, click **[number] other possible matches found** to see other options.

### Find and match

If you know a transaction has been created in Xero but it’s not showing up as a suggested match, [use find & match](Reconcile-a-bank-statement-line-using-Find-Match.md) to search for the correct transaction.

## Step 4: Create a new account transaction

Where a transaction doesn’t already exist in Xero that relates to the statement line, create the transaction during the bank reconciliation process.

Transactions can be created by accepting suggestions or using the **Create** or **Transfer** tabs.

### Accept a suggested transaction

To help you reconcile, Xero suggests account transactions to match with the bank statement lines. The suggestions are based on bank rules you’ve set up, similar transactions you've previously reconciled or details in the statement line.

#### Suggested by a bank rule

If Xero can’t match an existing account transaction to the statement line, it looks at your bank rules. If the bank statement line matches the conditions of a bank rule, Xero suggests a new transaction in line with the rule.

- If the correct bank rule is applied, click **OK** to accept the match and reconcile. If you need to update any of the transaction details first, click **View details**.
- Click **Don’t apply rule** to reconcile another way.

If a bank rule has been set up but it wasn’t suggested for the bank statement line, [check the rule conditions](About-bank-rules.md) are set correctly.

#### Based on a transaction previously reconciled

If there’s no existing account transaction or bank rule to apply and you’ve selected **Suggest previous entries**, Xero uses memorisation to suggest a transaction to create. Xero suggests to create a spend money, receive money, or a transfer transaction.

Memorisation is based on previously reconciled transactions with similar payee, particulars and reference details. Xero suggests the **Who**, **What** and **Why** for a spend or receive money transaction, or the bank account for a transfer transaction. The transaction is then ready to reconcile on the **Create** or **Transfer** tab.

- Click **OK** to accept the suggestion and reconcile. You can edit the details first if you need to.
- Click **Add details** if you want to add extra information to the suggested transaction before you create it.

#### Based on the details in the statement line

If there's no existing account transaction, bank rule to apply or similar past transaction to suggest, Xero uses machine learning algorithms to make a prediction. Predictions are based on the details in the statement line.

Xero predicts a contact and chart of account code for the **Who** and **What** fields. These are taken from the existing contacts and account codes available in your organisation. If there’s no existing contact that fits the details in the statement line, Xero suggests a new contact to create.

Predictions display in italics so you can identify them as predictions rather than memorisation-based suggestions.

- Add or edit details if required, then click **OK** to accept the prediction and reconcile.
- Click **Add details** if you want to add extra information to the suggested transaction before you create it.

To turn memorisation and predictions on or off, select or clear the **Suggest previous entries** checkbox at the bottom of the bank reconciliation screen.

### Create a cash transaction

Create a [spend money](Add-a-spend-money-transaction.md) or [receive money](Add-a-receive-money-transaction.md) transaction to record a new cash transaction during bank reconciliation.

### Create a transfer transaction

[Create a transfer money transaction](/s/article/Transfer-money-between-your-bank-accounts-in-Xero?userregion=true) to record the movement of funds between your bank accounts in Xero.

You only need to create a transfer transaction in one bank account. Xero creates the transaction in the corresponding account, so you just need to click **OK** to reconcile it.

## Step 5: Discuss it with your advisor

If you're unsure what a bank statement line relates to, start a conversation with your advisor or other users in your organisation. When reconciling, [enter a comment](Add-a-comment-to-a-bank-statement-line.md) in the **Discuss** tab to start a discussion.

Your aim is to match each statement line in the bank account to an existing transaction in Xero, or create a transaction during the reconciliation process.

Each bank statement line shows a money in icon for money received, or a money out icon for money spent.

Search for a specific statement line, or scroll up and down to navigate through them. You can sort the statement lines in order of date, payee or amount.

Tap **View all** to see a list of all the reconciled and unreconciled statement lines for the bank account.

To reconcile the bank account:

1. On the **Dashboard**, tap on a bank account that shows **[Number] to match**.
2. (Optional) Tap the contact's name to view more information imported with the statement line.
3. For each bank statement line, tap **OK** to accept the suggested match or prediction, or tap **Create new** to create a new transaction.
4. If Xero suggests a match but it's the wrong transaction, tap **See other matches [number]** to view the other possible transactions to match the statement line to.
5. If a suggestion or prediction is wrong, tap the menu icon , then tap:
   - **Create new** to add a new [spend money](Add-a-spend-money-transaction.md) or [receive money](Add-a-receive-money-transaction.md) transaction
   - **Find and match** to [search for an existing transaction](Reconcile-a-bank-statement-line-using-Find-Match.md)
   - **Transfer** to [transfer funds](/s/article/Transfer-money-between-your-bank-accounts-in-Xero?userregion=true) to or from another bank account
   - **Add a note** to add a note to the bank statement line

Your aim is to match each statement line in the bank account to an existing transaction in Xero, or create a transaction during the reconciliation process.

Each bank statement line shows a money in icon for money received, or a money out icon for money spent.

Search for a specific statement line, or scroll up and down to navigate through them. You can sort the statement lines in order by date, payee or amount.

Tap the list icon to see a list of all the reconciled and unreconciled statement lines for the bank account.

To reconcile the bank account:

1. On the **Dashboard**, tap on a bank account that shows **[Number] to match**.
2. (Optional) Tap the contact's name to view more information imported with the statement.
3. For each bank statement line, tap **OK** to accept the suggested match or prediction, or tap **Create new** to create a new transaction.
4. If Xero suggests a match but it's the wrong transaction, tap **See other matches [number]** to view the other possible transactions to match the statement line to.
5. If a suggestion or prediction is wrong, tap the menu icon , then tap:
   - **Create new** to add a new [spend money](Add-a-spend-money-transaction.md) or [receive money](Add-a-receive-money-transaction.md) transaction
   - **Find and match** to [search for an existing transaction](Reconcile-a-bank-statement-line-using-Find-Match.md)
   - **Transfer** to [transfer funds](/s/article/Transfer-money-between-your-bank-accounts-in-Xero?userregion=true) to or from another bank account
   - **Add a note** to add a note to the bank statement line

## What's next?

Once you’ve reconciled the bank account, the statement balance in Xero and the balance in Xero should be the same. If they’re not, [find out why there’s a difference](Why-are-the-statement-balance-and-balance-in-Xero-different.md).