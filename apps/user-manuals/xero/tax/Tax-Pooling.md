# Record tax pooling arrangements

Source: https://central.xero.com/s/article/Tax-Pooling

---

## Overview

- Record tax pooling arrangements for your clients in Xero Tax so they can be automatically included in payment reminder calculations and return summaries.
- ​Create unlimited tax pooling arrangements against each tax statement.
- Keep track of outstanding tax pooling transfers.

Tax pooling with Xero explained

### Before you start

If your clients use tax pooling to help manage their tax obligations, you can create and record tax pooling arrangements for them in Xero Tax.

Before you set up any tax pooling arrangements, there are four key pieces of information to consider.

- The client **Statement** the arrangement relates to.
- The **Tax Effective Date**, which determines how an incomplete arrangement will be treated.

 For instance, an arrangement with a tax effective date of 15 January and a remaining amount of $20,000 is treated as a payment dated 15 January and reduces the client's P2 payment by $20,000. If it’s still incomplete by 7 May, it also reduces the P3 payment by the same amount.

- The **Expected Tax Amount** the client expects to see on their Inland Revenue (IR) statement when the tax pooling is finally transferred.
- The **Remaining** amount, which is the net of the expected tax amount and the accumulated tax pool transfers for that date from the IR transaction feeds. If the remaining amount is greater than zero, then the arrangement is incomplete and will be included in [Use of Money Interest (UOMI)](Calculate-Use-of-Money-Interest-UOMI.md), tax returns, and payment reminder calculations. The **Remaining** amount is always less than the **Expected** amount.

### How tax pooling works in Xero

- Provisional and terminal tax reminders include remaining tax pooling amounts in their calculations. For calculation purposes, these remaining amounts are treated as payments dated the effective date of the arrangement. The payment status won’t affect how they’re included in calculations.
- When **Auto update from statements** is selected, tax returns will include any remaining tax pooling amounts for the year of the tax return in the provisional tax paid amount. On the payment schedule, the description shows as **Payments (includes tax pooling)**.
- Remaining tax pooling amounts available for the following year show in the provisional instalment return summary payment schedule for that year. If the amount is more than the instalment due, a credit balance will show. Any remaining tax pooling amounts will also be included in any UOMI calculations.
- If a payment reminder includes remaining tax pooling amounts, you’ll see an **INCLUDES TAX POOLING** [alert message](Approve-a-tax-payment.md) in the **Waiting Approval** tab on the Tax Payments screen.
- Tax pooling funds are applied to a specific client statement as at their effective date. However, the actual funds transfer by IR won't take place until later.

Set up an arrangement for your client

1. In the **Tax** menu, select **Statements**.
2. Next to **Client/IRD Number**, enter the client's name or IRD number, then click **Search** to find the income tax statement you want to create the tax pooling agreement for.
3. Click the client name, then open the relevant income tax statement.
4. Under **Tax Pooling Transfers**, click **New**.
5. (Optional) In the **Provider** field, enter the details of the tax pooling provider.
6. In the **Expected Tax Amount** field, enter the transfer amount that the client expects to see on their IR statement when the tax pooling is transferred.
7. Next to **Tax Effective Date**, click on the calendar to select the ‘as at’ date for the tax pooling transfer. If there are arrangements for different tax due dates (eg P1, P2, P3), you need to create a separate arrangement for each one. This updates the amount owing in the relevant payment reminder.
8. **Actual Amount transferred** will show as 0.00. Actual transactions will update this amount automatically when they’re received via IR transaction downloads.
9. **Remaining** will initially show as the expected amount and updates automatically. This field is the expected tax amount less the actual amount transferred. The remaining amount will never be a negative value.
10. Next to **Status**, select a payment status:

    - **Paid** – The client has paid the full amount to the tax pooling provider, eg tax deposit.
    - **Part paid** – The client has paid part of the tax amount to the tax pooling provider.
    - **Unpaid** – The client hasn’t paid the tax amount to the tax pooling provider, eg tax finance.
11. Click **Save**.

Edit or delete the arrangement

If the amount you expect to be transferred on the effective date changes, you need to edit the arrangement. You might also want to delete an arrangement if the client has missed the due date to pay it by.

1. In the **Tax** menu, select **Statements**
2. Next to **Client/IRD Number**, enter the client's name or IRD number, then click **Search** to find the income tax statement you want to edit the tax agreement for.
3. Click the client name, then open the relevant income tax statement.
4. Under **Tax Pooling Transfers**, click the date of the arrangement.
5. Either:
   - Edit the **Expected Tax Amount**, then click **Save**. This recalculates payment reminders and triggers the system to reassess the reconciliation status of the agreement.
   - Click **Delete**, then click **Yes** if the client has missed the payment due date and the arrangement is no longer in place.

Mark an arrangement or transfer as paid

1. In the **Tax** menu, select **Statements**.
2. Next to **Client/IRD Number**, enter the client's name or IRD number, then click **Search** to find the income tax statement with the arrangement you want to mark as paid or transfer.
3. Click the client name, then open the relevant income tax statement.
4. Under **Tax Pooling Transfers**, click the date of the arrangement.
5. Next to **Status**, select **Paid**.
6. (Optional) To show when a client has partially paid tax to the tax pooling provider, change the status to **Part paid**. In cases where IR transactions show it's been partially transferred, Xero automatically marks it as part paid.
7. Click **Save**.

Mark multiple tax pooling transfers as paid

If a client deposits the funds with the tax pooling provider, update the status to paid on the arrangement in Xero. Note that this change of status doesn’t affect any payment or return calculations.

1. In the **Tax** menu, select **Statements**.
2. Select the **Tax Pooling** tab.
3. Next to **Client/IRD Number**, enter the client’s name or IRD number, then click **Search**.
4. Select the checkbox next to the arrangement that has been paid. You can select more than one arrangement at a time.
5. Click **Mark as Paid**.

You’ll then see the message **[Number] tax poolings were successfully marked as paid**. Note, this has no effect on the client’s tax reminder calculations. When the money has been transferred at IR, the status automatically changes to **Complete**.

Automatic reconciliation of transfers

Xero automatically updates the transferred amount for an arrangement from IR transaction downloads.

- Expected tax pooling transfers are marked as **Complete** when the relevant transfer transactions equal or exceed the expected amount of the arrangement.
- If there are multiple transfers or multiple arrangements with the same effective date, Xero reconciles those with matching amounts first. Any remaining entries for the same date are allocated on a first in, first out (FIFO) basis.
- If a transfer is subsequently reversed, the arrangement automatically reverts to being incomplete.
- If the transferred amount is less than the expected amount, Xero automatically updates the status to **Part paid**.
- Each time a tax pooling transaction is received or an arrangement is updated, Xero re-reconciles all arrangements with the same effective date.

View arrangements for your practice

To view all incomplete arrangements for your practice:

1. In the **Tax** menu, select **Statements**.
2. Select the **Tax Pooling** tab.
3. (Optional) If you want to filter your list, select the **Account Manager** or **Job Manager**, then click **Search**.

To view all completed arrangements for your practice:

1. In the **Tax** menu, select **Statements**.
2. Next to **Client/IRD Number**, enter the client's name or IRD number, then click **Search** to find the income tax statement with the arrangement you want to view.
3. Click the client name, then open the relevant income tax statement.
4. Under **Tax Pooling Transfers**, click on the date of the arrangement to see the details.

## What's next?

Calculate [Use-Of-Money Interest (UOMI)](Calculate-Use-of-Money-Interest-UOMI.md), understand [provisional tax](The-Provisional-Tax-Return.md), and create an [income tax return](Create-a-tax-return.md) for your client.