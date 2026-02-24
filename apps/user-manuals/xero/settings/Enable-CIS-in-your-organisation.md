# Set up Construction Industry Scheme (CIS) in your organisation

Source: https://central.xero.com/s/article/Enable-CIS-in-your-organisation

---

## Overview

- Set up CIS in your organisation to add CIS account codes to your chart of accounts, then produce CIS invoices, bills and reports.
- Use CIS account codes to create an invoice, bill or credit note that calculates the CIS deduction.

Warning

Once CIS basic features are enabled for an organisation, they can't be disabled. Use the [demo company](Use-the-demo-company.md) to see how CIS in Xero works before you enable it.

##

Set up CIS

Set up CIS in your organisation to add new CIS system accounts to your chart of accounts. You need the advisor or standard + reports user role to set up CIS in the financial settings.

1. In the **Accounting** menu, select **Accounting settings**.
2. Click **Financial settings**.
3. Under **Construction Industry Scheme**, select whether you're a registered contractor, subcontractor or both.
4. Enter your **Unique Taxpayer Reference (UTR)**.
5. If you're a contractor, enter your **Accounts Office Reference** and **Employer's PAYE Reference**.

   If you're a subcontractor, select your **Subcontractor Deduction Rate**.
6. Click **Save**.

If you're a contractor, [add CIS Contractor to your pricing plan](/s/article/Changing-pricing-plan-UK) to access advanced features. You must set up CIS in your organisation using the steps above before you can use the additional features.

##

About the CIS system accounts

Once you've set CIS up in your organisation, Xero automatically creates the relevant CIS account codes to your chart of accounts.

If you select:

- **I am a registered contractor**in **Financial settings**, Xero creates the CIS Labour Expense, CIS Materials Purchased and CIS Liability account codes
- **I am a registered subcontractor** in **Financial settings**, Xero creates the CIS Labour Income and CIS Asset account codes

If you select both options, Xero creates all of the above CIS account codes.

If the account code shown below is being used by another account in your chart of accounts, Xero uses the next available code at the end of your chart of accounts list. For example, if 321 is already used, and the highest number used on your chart of accounts is 980, Xero will use code 981 for the CIS Labour Expense account.

| Account code | Account name | Type | Description |
| --- | --- | --- | --- |
| 210 | CIS Labour Income | Revenue | Use this account to record income from labour construction to be received on invoices. |
| 321 | CIS Labour Expense | Direct Costs | Use this account to record labour charged by subcontractors on bills. |
| 322 | CIS Materials Purchased | Direct Costs | Use this account to record materials charged by subcontractors on bills. |
| 625 | CIS Asset | Current Asset | Use this account to record the CIS withheld from you on invoices. |
| 821 | CIS Liability | Current Liability | Use this account when you pay CIS withheld on bills to HMRC. |

##

Using CIS account codes

CIS account codes are added to your chart of accounts when you enable CIS in your organisation. To create a CIS transaction, add or edit the transaction as usual, then in the **Account** field, select the appropriate CIS account code.

When you add a CIS labour account code to line items in an invoice, bill or credit note, Xero calculates the deduction automatically and displays it at the bottom of the transaction. The deduction shows below the invoice total when a standard invoice template is used, and as a line item on the invoice when an advanced invoice template is used.

CIS deductions are automatically calculated on invoices created on the Xero Accounting for iOS and Xero Accounting for Android apps.

The CIS deduction is only calculated on items that use a CIS labour account code, even if there are other items on the transaction.

If a credit note applies to an existing bill or invoice that doesn't already have CIS labour items on it, you need to edit the transaction to include CIS information before you create the credit note.

You can’t:

- Select CIS account codes when creating repeating bills or invoices.
- Add or edit CIS line items on a transaction where payments are allocated. If you need to do this, void the original transaction and re-enter it.
- Select the CIS Asset or Liability accounts on a transaction.
- Edit a CIS credit note that's already been allocated, partially paid or refunded.

Tip

Use a [third party app](https://apps.xero.com/uk/search?q=data%20entry) (Xero App store) to import or edit CIS bills and invoices in Xero.

## What's next?

If you’re a contractor, [add CIS information](Create-and-verify-a-CIS-contact.md) to your subcontractor contact records.