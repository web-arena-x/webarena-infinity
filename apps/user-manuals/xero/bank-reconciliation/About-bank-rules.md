# About bank rules

Source: https://central.xero.com/s/article/About-bank-rules

---

## Overview

- Understand when to use bank rules in Xero, how they work and the different types available.

Warning

Set up bank rules to reconcile statement lines that you won’t create a bill, invoice, or other type of transaction for. If a bank statement line relates to an existing transaction, [use find & match to reconcile](Reconcile-a-bank-statement-line-using-Find-Match.md).

What you need to know

### When to use bank rules

Bank rules save you manually creating a new transaction each time you get a recurring or similar type of bank statement line. You tell Xero how these statement lines should be coded so that Xero can suggest the right type of transaction and complete some of the details for you. This saves you time, helps to reduce human error and ensures consistent coding, which leads to more efficient reporting.

### How bank rules work

When a bank statement line imports into your Xero bank account, Xero checks the details to see if it meets the conditions of your bank rules. You can see what details import and what fields they import into when you reconcile your bank account. Click **More details** next to any statement line to see all fields.

Xero checks the rules in the order they appear on the bank rules screen. If the statement line does meet the conditions you specified in one of your bank rules, Xero suggests either a new spend money, receive money or transfer money transaction as you reconcile. Xero completes the transaction details from the information specified in the rule, so all you need to do is check the details and click **OK** to approve the match. When you approve the match, Xero creates the transaction.

If the transaction Xero suggests isn't quite right, you can edit it, create a new one, or find an existing transaction in Xero to match with the statement line.

If you have multiple bank accounts, you can set a bank rule to apply only to a specific bank account, or to all the bank accounts in your organisation.

Types of bank rules

There are three types of bank rules you can create:

- **Spend money rule** – Applies to bank statement lines where money is going out of your bank account. The rule creates a spend money account transaction.

 Spend money bank rules are useful for regular cash transactions such as parking, bank fees, pensions and regular travel costs.
- **Receive money rule** – Applies to bank statement lines where money is coming into your bank account. The rule creates a receive money account transaction.

 Receive money bank rules are useful if you make regular cash deposits for daily takings or bank interest payments.
- **Transfer money rule** – Applies to bank statement lines where money is being transferred between bank accounts. The rule creates a bank transfer between the two accounts.

 Transfer money rules are useful if you regularly transfer funds between your bank accounts, like a monthly transfer into a savings account.

Setting bank rule conditions

### What you need to know

Bank rules are split into two parts. Set what conditions the statement line must meet, then add transaction details to tell Xero what to do when a transaction meets those conditions.

The bank rule conditions contain information Xero looks for in the bank statement line to know when to suggest the rule. You can tell Xero to look at the payee, description, amount, reference, analysis code or bank account.

### All and Any

The first part of your rule allows you to decide if the details in a statement line must meet all of the conditions you set, or just some of them, in order for Xero to suggest the rule.

For example, you include conditions for the **Payee**, **Amount** and **Reference** fields in your new rule. Choose whether Xero should suggest the rule if any of those three fields in the statement line match the conditions in your rule, or only when all three fields match.

To do this, choose **All conditions match**or **Any conditions match** in the first part of your rule.

- **All conditions match** – Xero only suggests the rule when every condition is met. If one condition isn’t met, the rule isn't suggested.

 This makes the rule more restrictive, which is useful if you have several similar statement lines that you want to reconcile differently.
- **Any conditions match** – Xero suggests the rule if only one of the conditions is met. The rule doesn’t fail just because one or more conditions aren't met.

 This makes the rule less restrictive, which is useful if you have several similar statement lines, for example from the same supplier, that you want to reconcile differently.

####

### Rule conditions

You can restrict each condition to apply to only one of the five individual fields that show on the bank statement line in the **Reconcile** tab, such as the payee, description or reference fields. Select **Any text field** if you want Xero to suggest the rule if any part of the bank statement line meets the condition.

You can also set whether the details on the bank statement line must equal what you enter in the condition exactly, or whether they can contain or start with the details you enter. You can set a rule to apply when the specified field is blank.

### Tips for effective bank rule conditions

The way you set up the conditions of a bank rule determines how loose or restrictive the rule is. When you set up a rule, think about how frequently you want Xero to suggest it and how many statement lines will match the conditions you specify.

- **Restrictive rules** – Xero will only suggest a restrictive rule when very specific criteria are met. You might use **All** or **equals** in your conditions so they only apply to a small number of statement lines.

 It might mean that Xero will suggest the rule less frequently during reconciliation, which is useful if you want a particular statement line to be treated differently to any similar statement lines. However, if a bank feed changes which fields information appears in, a very restrictive rule might stop working.
- **Loose rules** – Xero might suggest a loose rule when a transaction meets any of the conditions you specify or when any part of the bank statement line matches your conditions. You might use **Any** or **contains** in your conditions so they apply to a wider range of statement lines.

 Xero will probably suggest this rule more frequently because more of your statement lines will match the criteria. This is useful if you receive statement lines from different suppliers that you want to code in the same way, for example, for fuel. It’s also useful if the information in the statement line changes frequently, for example, if the statement line sometimes displays “ABC Fuel” and sometimes only “ABC”.

For example, if you have several statement lines that might contain similar words, such as "fuel", but you want to reconcile fuel from one supplier differently, you could select a specific payee name and use **equals** to make a more restrictive rule. However, if you want Xero to suggest the rule for lots of bank statement lines, you might set up several conditions in one rule, choose **Any text field** and use **contains** to make a loose rule that could apply when a bank statement line contains words like “fuel”, “petrol” or the name of your regular suppliers.

Remember, when Xero suggests a rule, you choose whether to apply it, edit the details suggested or ignore the suggestion completely. You can create a loose rule to begin with, then make it more restrictive if Xero suggests it too often.

After you create or edit a bank rule, check the order of your bank rules. Xero suggests the rules in the order they show on the bank rules screen which might affect the suggestions it offers.

Adding account transaction details

When you set up a bank rule, you need to tell Xero what details to include in the new account transaction it suggests.

- **The contact** – This can be an existing or new contact, the contact name as per the Payee field on the bank statement, or you can enter the contact name manually when you're reconciling.
- **The reference** – The reference on the transaction can be set to pull from a specific field in the bank statement line, or you can set it manually when you reconcile the bank account.
- **Allocating and coding amounts**– Allocate either a fixed amount or a portion of the transaction to an individual account in your chart of account, or split the total over different account codes, with different descriptions and tax rates.

 For example, if you make personal calls on your business phone, you might want to allocate the regular monthly fee to one account code and separate out the personal and business calls when you reconcile the transaction each month.

 To do this for the example above, you would set up the bank rule as a fixed value line item for the monthly fee, coded to the relevant expense code with the remainder allocated as a percentage to one or more account codes.

Tip

If you use the **Discuss** tab during bank reconciliation, you can set your bank rules to suggest your comments as the transaction’s description. Add the placeholder **[Comments]** into the **Description** field in part 3 of the rule.

Ordering and searching bank rules

### Order your bank rules correctly

Xero checks the rules in the order they show on the bank rules screen. To help bank rules provide the right suggestions, order your most restrictive rules at the top of the list so that Xero checks your most specific conditions first. Only when a transaction hasn’t met the conditions of your first rule will Xero check your other rules further down the list.

For example, you might make regular payments for vehicle leasing. Most of these payments are coded in exactly the same way, but one of them, "ABC vehicle leasing", needs to be coded to a different account code because a specific department pays for it.

You create two rules to help you reconcile these transactions - one to deal with statement lines from "ABC vehicle leasing" and one to deal with any other statement lines related to leasing.

If the generic vehicle lease rule is top of the list, Xero will apply it to your "ABC vehicle leasing" statement line. Since the statement line matches the first rule on the list, Xero won’t check any of your other bank rules and won’t suggest the more specific rule you want it to. In this example, put your more restrictive rule for "ABC vehicle leasing" above your generic rule.

### Search existing bank rules

If you want to check if similar rules are in the right order or if you already have a rule for one of your recurring transactions, use the search bar at the top of the screen. Search results include partial matches in case you’re not sure what phrases to search for.

## What's next?

Now you know how they work, [create a bank rule](Create-a-bank-rule.md) for a recurring cash transaction.