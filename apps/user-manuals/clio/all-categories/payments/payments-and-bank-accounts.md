# Payments and Bank Accounts

Source: https://help.clio.com/hc/en-us/articles/9285631748507-Payments-and-Bank-Accounts

---

Accounts in Clio Manage are designed to mirror your real-life bank accounts at your financial institution for collecting payment on bills and retaining trust funds. You can create two types of accounts in Clio—operating and trust accounts. Trust accounts retain funds in trust for clients. Operating accounts are for daily transactions.

**Note:** Only users with accounts or administrator permissions can manage bank accounts.

## Create new accounts

When creating a new bank account in Clio Manage, you can select whether the account is an operating or trust account. All non-trust accounts are operating accounts. Once transactions have been applied to an account, account types should not be changed since this can cause account balancing inaccuracies.

**Note:** The **Accounts** tab in Clio Manage is used for creating internal records of your firm’s bank accounts (e.g., Operating and Trust accounts) for managing client payments, trust requests, and default settings. It is distinct from the Banking section in Clio Accounting, which is used for connecting to a live bank feed (via Plaid) to reconcile transactions and manage your firm's General Ledger.

1. Go to **Accounts**.
2. Click **New account**.
3. Name your account and select the account type.
4. Choose the **Currency** and enter the account’s opening balance.

   **Important:** Once a transaction appears in the account, the currency cannot be changed.
5. *Optional:* Check the box for **Connect this bank account to online payments** and add financial details to connect the account to Clio Payments to accept payments directly from clients. You can only connect bank accounts that are in your local currency.
6. Click **Create bank account**.

**Note:** You can also connect your bank account to the online payments platform after creating the account.

## Connect or disconnect accounts from online payments

When creating or editing a bank account in Clio, you will need to connect the account to [Clio Payments](https://help.clio.com/hc/en-us/articles/9285740132379). If you are setting up Clio Payments for the first time, you are required to connect at least one Clio Manage operating account to online payments once your application is approved. This allows you to collect payment for bills and sync transaction records with your accounting platform. You can also disconnect any bank accounts that you do not want connected to online payments.

**Note:** Each payout account can only be connected to one Clio Manage bank account. This means that you cannot connect one payout account to multiple Clio Manage bank accounts.

**Connect bank accounts to payments:**

1. Go to **Accounts**.
2. For the relevant account, click **Connect to payments**. You can also click the down arrow next to **Edit** and select **Connect to online payments**.
3. Select from your list of account(s) that you connected when [signing up for Clio Payments](https://help.clio.com/hc/en-us/articles/9285740132379-Clio-Payments-Get-Started-with-Clio-Payments#h_01HAAG9C4XRNC59059VWHXRQP1). Or, click **Add payout account** to connect to a different payout account.
   - If you do not have the option to choose a payout account, your payout account may still be pending verification. Once it is verified, you can connect it.
4. Click **Connect**.

**Disconnect bank accounts from payments:**

1. Go to **Accounts**.
2. Click the down arrow next to **Edit** and select **Disconnect from online payments**.
3. When the warning prompt appears, select **Disconnect**.

## Edit accounts

You can edit basic details of a bank account at any time. Once transactions have been recorded in an account, the account type should not be changed since this can cause account balancing inaccuracies.

1. Go to **Accounts**.
2. Click **Edit**.
3. Make your changes.
4. Click **Update Bank Account**.

## Delete accounts

**Important:** You can only delete accounts that do not have recorded transactions. If you need to delete an account with transactions, delete all the transactions first.

1. In Clio Manage, select **Accounts**.
2. For the relevant bank account, click the down arrow next to **Edit** and select **Delete**.
3. When the warning prompt appears, check the confirmation box and click **Delete**.

## Record vendor transactions

You can manually record funds out of your operating accounts to track payments to non-clients, such as payments to vendors related to your clients' cases. Once recorded, your operating account balance will show the deducted amount.

1. Go to **Accounts**and select an operating account. You can also go to the **Transactions** subtab in a contact or matter.
2. Click **New transaction**.
3. Complete the required fields.
   - Under **Amount**, enter the amount that will be paid to the vendor as a negative number (e.g. -200).
   - Under **Date**, select the transaction date.
   - Under **Account**, check that the appropriate operating account is selected. The funds will be deducted from this account.
4. Complete the remaining fields as necessary. Adding information to these fields can be useful when viewing transactions and when generating relevant reports.
   - **Client and matter fields:** You are not required to select a client or matter, but completing these fields will allow you to track which client and matter the vendor payment is connected to.
   - **Source/Destination:** Enter information about the source or destination of the payment (e.g. information about the vendor's bank account).
   - **Payer/Payee:** Enter the vendor's name.
   - **Description:** Enter information about the purpose of the transaction (e.g. "Payment for bill [bill number]").
5. Click **Record transaction**.

## Export transactions

Once you have recorded transactions on your bank accounts, you can export transactions from a single bank account. You can also export transactions specific to a single matter or contact from the matter or contact’s **Transactions** subtab.

**Note** : Bank account transactions can be exported in two QuickBooks formats. Transactions exported for a single contact or matter are exported in PDF or CSV format.

Single bank account Single matter or contact

1. Go to **Accounts**.
2. Select **Export transactions**.
3. Select the bank account, date range, and export format.
4. Click **Export Transactions**.

1. Go to the contact or matter’s **Transactions** subtab.
2. Select the operating or trust account.
3. *Optional:* Select a date range.
4. Scroll to the bottom of the page and click **Export**.
5. Select the file output and click **Export**.

## Transfer funds between accounts

Each contact and matter in Clio have a **Transactions** subtab where you can record transactions and transfer funds between a contact and any of the contact’s matters or from one bank account to another.

**Important:** In order to stay IOLTA compliant, be careful when transferring funds in trust accounts.

Between accounts Between matters

**Note:** Clio cannot move funds between your actual bank accounts. When recording a transfer in Clio, you will need to manually move the funds in your real bank accounts to reflect the transaction.

1. Go to the contact or matter’s **Transactions** subtab.
2. Click **Transfer funds**.
3. Select **Between bank accounts**.
4. Complete the transfer information.
5. Click **Record transfer**.

1. Go to the contact or matter’s **Transactions** subtab.
2. Click **Transfer funds**.
3. Select **Between matters**.
4. Complete the transfer information.
5. Click **Record transfer**.