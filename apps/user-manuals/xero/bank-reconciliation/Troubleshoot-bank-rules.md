# Fix problems with bank rules

Source: https://central.xero.com/s/article/Troubleshoot-bank-rules

---

## Overview

- If Xero doesn't suggest your bank rule as expected, use this article to help you resolve the issue before you contact support.

An existing bank rule stops working

If Xero doesn't suggest a bank rule as you expect it to, it might be because the format of the imported bank statement lines has changed, or because Xero is suggesting your bank rules in a different order.

When a bank rule isn't suggested in the way you expect, we recommend you check:

- How the statement line imports into Xero – Check if the payee name has changed or if key information comes through in a different field to what’s set in your conditions. These sorts of changes can happen when the bank or payee changes the format of the data they send to Xero. Click **More details** next to any statement line to see all the fields.
- The transaction amount – If your rule conditions are set to look for a fixed amount, or to code a fixed amount to a particular account, the rule might not apply if the value of the transaction has changed. This might happen if a regular subscription has increased in price or your bank fee changes slightly.
- The order of your rules – Xero checks the conditions of your bank rules in the order the rules are listed in the bank rules screen. If the order of your rules has changed, or a new rule has been added to the list, Xero might suggest a different rule to the one you expect. You might need to adjust your rule or change the order of your rules.

A rule suggests more or fewer transactions than expected

Check the condition you've selected for step 1 of the rule:

- If you want fewer but more specific suggestions – select the condition **All conditions match**. For example, this bank rule will provide suggestions for all bank statement lines that have 'ABC Stationery' listed as the payee, and the word 'Print' in the **Reference** field.
- If you want a wider range of less specific suggestions – select the condition **Any conditions match**. For example, this bank rule will provide suggestions for bank statement lines that either have 'ABC Stationery' as the payee, or the word 'Print' in the **Reference** field.

Similar rules suggest different transactions

If you've created more than one rule for a payee, check the order of the bank rules. You'll want to put the most restrictive rules at the top of the list, and the less restrictive rules further down the list. This ensures you'll see the right number of suggested transactions for each bank statement line.

For example:

- You have a less restrictive bank rule that allocates payments made to ABC Stationery to the Office Expenses account.
- You also have a more restrictive rule that allocates payments made to ABC Stationery with the word 'Print' in the description to the Printing & Stationery account.

If you run the less restrictive rule first – all payments to ABC Stationery allocate to Office Expenses, even if they have the word 'Print' in the description.

If you run the more restrictive rule first – payments to ABC Stationery with the word 'Print' in the description allocate to Printing & Stationery, then any remaining payments to ABC Stationery allocate to Office Expenses.

A rule containing a hyphen doesn't suggest any transactions

Xero doesn't recognise hyphens in conditions, so if your bank rule contains a hyphen, Xero can't find statement lines and suggest transactions for them.

If you have a field or value in a statement line that contains a hyphen, create a rule set to **All conditions match**, then split the hyphenated word into two conditions. For example, you want to set up a bank rule that looks for the payee 'Print-Man'.

- Set your first condition to look for a payee that contains 'Print'.
- Set your second condition to look for a payee that contains 'Man'.

Because you've set your rule to **All conditions match**, Xero will find all transactions where the **Payee** field contains the words 'Print' and 'Man'.

Bank account isn't available for a transfer money rule

When using a bank rule to transfer money to or from a foreign currency bank account, the **Select a bank account** drop down only shows bank accounts that match the base currency of the organisation.

To use a bank rule to transfer money to or from a foreign currency bank account, you need to create the rule to apply to all bank accounts. Then [select the bank account during bank reconciliation](Create-a-transfer-money-rule-with-foreign-currency.md).

## What's next?

If you need more help, reach out to Xero support below.