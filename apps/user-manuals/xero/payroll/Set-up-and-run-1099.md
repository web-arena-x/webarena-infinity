# Set up and run the 1099 report

Source: https://central.xero.com/s/article/Set-up-and-run-1099

---

## Overview

- Add, copy or edit 1099 rules.
- Use rules to check which contacts and payments are listed to prepare a 1099.

About 1099 rules

- Xero uses rules to search for transactions to include in the 1099 report.
- To make creating 1099 rules easier, use the **W-9 management** tab to [identify and mark your 1099 contacts](Prepare-for-1099-in-Xero.md).
- You can either use the same rules as last year, or create new ones from scratch. If you re-use last year’s rules, you can edit them.
- You need the advisor or standard + reports user role. If you're the subscriber or have the manage users permission, you can [change your own user role](Change-a-user-s-role-or-permissions-US.md).
- The 1099 report includes suggested rules based on common rules for some of the accounts you use. You can review and make changes to the suggested rules or make your own.

Set up 1099 rules

1. In the **Tax**menu, select **1099**.
2. Select the report year.
3. Click:
   - **Set up rules** if this is the first time running the 1099 report in Xero
   - **Copy last year's rules** or **Set up rules from scratch** if you ran the report in Xero last year
4. Click **New rule**. For each rule you must select a:
   - **Contact group** – select a contact group or **All contacts**. If you used the **W-9 management** tab to mark your 1099 contacts, select **1099 contact group**.
   - **Accounts** – select the account you coded the payment to. You can select as many accounts as you need to.
   - **Reporting box**– select the 1099 box you want the dollar amount in.
5. Click **Save and view report**.

Edit a 1099 rule

1. In the **Tax**menu, select **1099**.
2. Select the report year.
3. Click **Manage reporting rules**.
4. Click the dropdown and make your edits.
5. Click **Save and view report**.

Check contacts and payments

Tip

[Use the Cash payments by vendor report](Prepare-for-1099-in-Xero.md) to identify the contacts and payments you should see on the 1099 report.

### Check form overview

The form overview lists the contacts included in each 1099 report and summarizes the payments included.

If you're not already viewing the 1099 report, you can view this by clicking the Tax menu and selecting 1099.

We recommend you check:

- Both the 1099-MISC and 1099-NEC forms include the contacts you expect, and that those contacts are included in the correct 1099 report, or in both if required.
- Contacts with missing details listed in the **Alerts** column. To enter missing details, click the contact’s name then **Edit contact details**. Edited details automatically update in the contact record.
- Created rules and transaction details for each contact to confirm that the correct payments are listed.

Payments are displayed as excluded from the report if they:

- Don't meet the IRS threshold
- Are manually excluded by a user
- Are made from a credit card type account
- Are third party payments such as Stripe, Venmo and Paypal

The totals for each contact don’t include refunds processed via receive money transactions. If you need to include these types of transactions, finish checking the other payments included, then export the report to make the necessary edits. If you do edit the report, make sure you save a copy for audit purposes.

### Review transaction and contact details

1. From the report overview, click **Review** for a particular contact.
2. Click **1099 contact details** to review key information for the contact.
3. Click **1099 transactions** to review the individual transactions for the contact.

We recommend you check:

- Contact details are correct, including the email address if you plan to email copies to contacts, and the Tax ID number. Edit details if required, then click **Save and exit**. Users with the standard + reports user role can edit all details, but only users with the advisor user role see the full Tax ID number.
- Payments and amounts are as expected, and only the correct payments have been included. Select the checkbox next to any non-credit card payments to exclude them. Click **Save and exit** to save any changes you make.
- Payments are reported in the correct box. If necessary, change the **Reported as** field, then click **Save and exit**.
- Payments from third-party processors are excluded. Check the **Paid from** column to identify any third party payments not yet excluded. Payments made from a credit card type bank account are already excluded and are listed underneath the report.

If you need to edit a payment, click the account or reference to open the transaction in a new window. Make the changes required, then save the transaction. Return to the report and refresh the screen.

To add back the payments you've manually excluded and return all payments to their original boxes:

1. Return to the rules screen.
2. Select **Reset overrides and exclusions**.
3. Click **Save and view report**.

### Contact groups

If you need to populate both NEC and MISC forms, you can use the same contact group or two separate contact groups for each form. If you use the same contact group, use different accounts to separate NEC and MISC payments. For example, use the Contract Labor account for NEC box 1, and the Rent account for MISC box 1.

When using two separate contact groups, you don’t need to use specific accounts in your rules, and can just use ‘All accounts’. Note that if a contact belongs to both groups, all their payments will show in the NEC form. You need to manually move any payments that should be in the MISC form.

Check overpayments

Overpayments are reported in the 1099 based on the first rule that includes the relevant contact group in its conditions. For example, if a contact is part of the 1099 contact group and has an overpayment, that overpayment will be reported based on the first rule that uses the 1099 contact group.

To move overpayments to a different 1099 box, or remove them altogether:

1. From the form overview, click **View** for each contact who had an overpayment during the year.
2. Check which box the overpayment is being reported as. Overpayments will show as **Accounts Payable** under the **Account** column.
3. To move the overpayment to a different box, change the **Reported as** field. To remove the overpayment, clear the checkbox.
4. Click **Save and exit**.

## What's next?

If the report isn't as you expect it [follow the troubleshooting steps](Troubleshoot-1099-reports.md), otherwise file your 1099 form.