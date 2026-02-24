# Adjust overstated superannuation guarantee contributions

Source: https://central.xero.com/s/article/Adjust-overstated-superannuation-guarantee-contributions

---

## Overview

- Create and adjust an unscheduled pay run to correct your superannuation contribution accrual if they were overstated.

## Create an unscheduled pay run

If you have a [payroll admin permission](Payroll-Admin-access.md), set up a pay run to adjust your Superannuation Guarantee (SG) contributions.

1. In the **Payroll** menu, select **Pay employees**.
2. [Remove any existing draft pay runs](Revert-a-pay-run-to-draft.md) for the periods you want to use. You can only have one pay run for each pay period.
3. Click **Add Pay Run**.
4. From **Select a pay period**, select **Unscheduled pay run**.
5. Select the pay frequency and pay period needing adjustment.
6. Click **Next**.
7. Select **Included** for each employee you want in the pay run, or to include all employees click **Included** then select **Include all**.

You’ll then need to adjust the SG contributions for each of the affected employees.

## Make adjustments to the SG contributions

In the unscheduled pay run, click on each employee to adjust their overstated SG contributions.

1. Remove any earnings, deduction and reimbursement lines not applicable to the adjustment.
2. Under **Superannuation Fund**, click the existing superannuation line and then complete the following:
   - Select the relevant superannuation fund.
   - If you haven’t already, select **Superannuation Guarantee Contribution (SGC)** for the contribution type.
   - Update **Calculation Type** to **Percentage of Earnings**.
3. Click **OK**.
4. For the same superannuation line, in the **Percentage** field, enter zero.
5. Click **Add Superannuation Line**, then complete the following:
   - Select the relevant superannuation fund.
   - Select **Superannuation Guarantee Contribution (SGC)** for the contribution type.
   - Update **Calculation Type** to **Fixed Amount**.
6. Click **OK**.
7. For the same superannuation line, enter the adjustment amount as a negative in the **Amount** field.
8. Click **Save**.
9. Repeat for the relevant employees and then, [post the pay run](/s/article/Process-a-pay-run-and-pay-employees?userregion=true).

The negative amount appears in your [Superannuation Accruals report](Superannuation-Accrual-report.md) to reflect the reduced liability amount for each employee.

## What's next?

If you use [Auto Super](Process-superannuation-payments.md), you can select the negative adjustment line when creating your next batch. This ensures the next batch payment gets reduced by the same adjustment value for each employee.