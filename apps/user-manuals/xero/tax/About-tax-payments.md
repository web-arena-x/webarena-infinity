# About tax payments

Source: https://central.xero.com/s/article/About-tax-payments

---

## Overview

- Find out how Practice Manager calculates provisional tax totals and payments.
- Learn about the different provisional tax payment statuses.

Calculations for provisional tax payments

Tip

Tax payments which fall on a weekend, public holiday or provincial anniversary day can be paid on the next business day without incurring penalties. Find out more on [when to pay](https://www.ird.govt.nz/managing-my-tax/make-a-payment/when-to-pay) (Inland Revenue website).

- Practice Manager uses the Residual Income Tax (RIT) uplift method as its standard method of calculating provisional tax payments.
- Practice Manager can also calculate provisional tax using the estimate method, or overrides.

### Provisional tax calculation sources

Practice Manager uses the following data when calculating provisional tax totals and payments.

From an approved tax return from the year prior to the provisional tax year:

- RIT
- Provisional basis

From an approved tax return two years prior to the provisional tax year:

- RIT

From a statement for the provisional tax year:

- Provisional basis
- Estimate amount (from the Statement screen)
- Estimate amount (from Inland Revenue statement, if different)
- Provisional assessment (from Inland Revenue statement, if different to RIT uplift amount)
- Voluntary amount
- 50-50 split
- Six-monthly GST setting
- Period end month

Practice Manager decides which data to use based on the state of the client’s returns when it calculates provisional tax. Practice Manager displays the sources it uses for the calculations on the Tax Payments and Tax Statements pages.

### Student loans

Student loan balances aren’t tracked in Practice Manager. This means Practice Manager isn’t able to determine if the student loan has been paid in full.

Practice Manager calculates a student loan obligation based on what is entered into the current year tax return and generates a payment letter based on this information.

You should confirm the student loan balance using myIR when creating a new tax return and delete the student loan schedule if the loan has been paid in full.

When preparing payment letters that include a student loan amount, it’s important to check that the payment amount generated isn’t more than the remaining balance owing on the student loan.

### Working for Families

Practice Manager includes payments for Working for Families (FAM) in the income tax amount (INC).

If you make a payment for INC (including FAM) before the due date for FAM, the [START connection](Set-up-your-practice-s-START-connection-with-Inland-Revenue.md) won’t automatically transfer the excess credit to offset the FAM assessment. Instead, the excess FAM credit will refund as the INC account is paid and the period is finalised.

### Provisional tax calculation examples

Example 1

You are preparing your client's 2022 provisional payment and they have a:

- 2021 draft return in Practice Manager
- 2020 return assessed by Inland Revenue

Practice Manager calculates 2022 provisional tax payments using 2020 RIT + 10%.

Example 2

Your client has a:

- 2021 return approved in Practice Manager
- 2020 return assessed by Inland Revenue

Practice Manager calculates 2022 provisional tax payments using 2021 RIT + 5%.

Tax payment due date

Tax payment information can be seen in Practice Manager for up to 90 days after the payment date has passed. For example, if the payment due date is 7 February 2023, you can assess payment letters until 8 May 2023.

Other things to note:

- Payments made after the due date will be applied to the next installment.
- If no payment obligation existed before the due date, new ones won't be created.
- Changes to the payment letter calculation after the due date won't automatically show on the **Changed** tab.

How tax payment statuses work

To view the status of your tax payments, in the **Tax** menu, select **Payments**. The status appears in the tabs.

The statuses that a tax payment can have are:

| Status | Description |
| --- | --- |
| Waiting Approval | Payments are awaiting your review to approve or ignore. Approve or ignore every payment on this tab before the payment due date so that Practice Manager saves a record of the payment. If you don't approve or ignore a payment before its due date, you won't be able to view or change the payment amount later, or print a payment letter after that date. |
| Approved | Payments you've approved. You can now send payment letters to your clients. |
| Changed | Approved payments where the client's tax position has changed after being approved as the result of another action in Practice Manager. For example, Practice Manager might have imported a new client payment transaction from Inland Revenue, or you might have amended your client's tax return. Click **Ignore Change** to clear the alert for the selected payments and move the payments back to the **Approved** tab. You can also ignore the change from the **Payment Calculation** in **Tax Payments**. You can't print a letter for a changed payment unless you approve the new amount. |
| Ignored | Payments you've selected on the Waiting Approval or Changed tab and marked as Ignore. You might ignore zero balance payments or payments where you are no longer the tax agent for the client. |
| Sent | Payments for which payment letters have been printed or emailed. A sent payment can have one of the following statuses:   - **Queued** - the email is processing and is in the queue to be sent (might take several hours depending on email volumes). - **Emailed** - the email has been sent. - **Printed** - the payment was printed and mailed to the client, or emailed individually. |

## What's next?

You might need to [change a tax payment](/s/article/Change-a-tax-payment), or [ignore a tax payment](Ignore-a-tax-payment.md). Or if you're happy with a payment, [approve the tax payment](Approve-a-tax-payment.md).