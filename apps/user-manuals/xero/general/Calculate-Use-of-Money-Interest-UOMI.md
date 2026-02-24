# Calculate Use of Money Interest (UOMI)

Source: https://central.xero.com/s/article/Calculate-Use-of-Money-Interest-UOMI

---

## Overview

- The IR3, IR3NR, IR4, IR6, IR8 and IR9 return types support UOMI.
- If Practice Manager automatically calculates UOMI, you can override the calculation or its start date if necessary.
- You can adjust the end date for UOMI calculations.

Warning

You’ll need to manually set the UOMI start date if a client submits an IR provisional tax estimate before the second to last provisional instalment is due, or underpays either of their first two instalment amounts.

Override the default UOMI calculation

Practice Manager reviews your data to suggest whether UOMI applies using Inland Revenue's (IR's) rules. If UOMI does apply, Practice Manager will suggest whether it applies for the whole financial year or just from the last provisional date.

If Practice Manager does make a UOMI calculation, this calculation will display in the return settings.

### View a statement's UOMI calculation

1. In the **Tax** menu, select **Statements**.
2. Open the statement you want to view, then select **UOMI**.

### Override a UOMI calculation

If you disagree with a UOMI calculation, you can override it with one of the following options:

- **Does not apply** – UOMI applies but you don’t want UOMI calculated.
- **Applies from year start** – Updates amount to calculate from start of financial year. If there's been a short payment from P2, it will calculate from this date.
- **Applies from P3** – Updates amount to calculate from final provisional instalment.
- **Estimate method** – Updates amount to calculate from the start of the financial year.

For more information on the menu options above, see [Simplified business tax processes](https://www.taxpolicy.ird.govt.nz/publications/2017/2017-sr-business-tax) (IR website).

To override a UOMI calculation:

1. In the **Tax** menu, select **Returns**.
2. Click on the client's tax return you want to edit UOMI for.
3. Under **Use of Money Interest - Start and End Dates**, select the **Override** checkbox.
4. Under **Use of Money - Start and End Dates**, select the override option you want. By default, the UOMI calculation will always use the client’s terminal tax due date as the final date. If you want the client to pay earlier, enter an alternate date in the **End** **Date** field.
5. For 2017 and earlier returns, select the **Calculate up to** checkbox to calculate any potential UOMI. Practice Manager will calculate whether UOMI applies and work out how much the client owes if so.
6. Click **Update**.

Change the UOMI calculation end date for a payment reminder

You can change the end date to which Practice Manager calculates UOMI when preparing a payment reminder.

1. In the **Tax** menu, select **Payments**.
2. Click the client's terminal tax payment you want to change the UOMI calculation end date for.
3. Next to **Plus Use of Money Interest**, select a date to change the end date to.
4. Click the calculate icon  to view the new UOMI amount.
5. Click **Approve** to save the new calculation and update the payment.

Override the UOMI amount for a payment reminder

You can override the amount of UOMI when preparing a payment reminder.

1. In the **Tax** menu, select **Payments**.
2. Click on the client’s terminal tax payment you want to change the UOMI amount for.
3. Next to **Plus Use of Money Interest**, enter the new UOMI amount. Do not click the calculate icon after entering the new UOMI amount, as this will overwrite the manual amount you’ve entered.
4. Click **Approve** to save the new amount and update the payment.

## What's next?

Learn more [about provisional tax payments](About-tax-payments.md) and how Practice Manager calculates them for your clients.