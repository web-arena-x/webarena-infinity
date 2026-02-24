# Fix issues with a pay run

Source: https://central.xero.com/s/article/Troubleshooting-pay-run-errors

---

## Overview

- Understand the different pay run errors and how to resolve them.

Errors when saving a payslip

### Payslip must include a Superannuation Guarantee Contribution line with a calculation type of Percentage or Statutory Rate

This error occurs when an employee aged over 18 years is missing a superannuation line with a **Contribution Type** of **Superannuation Guarantee Contribution (SGC)** and **Calculation Type** of **Statutory Rate** or **Percentage of Earnings** in their payslip.

To fix the error:

1. Click the relevant employee's name within the draft pay run.
2. Select **Add Superannuation Line**.
3. Set the **Contribution Type** to **Super Guarantee Contribution (SGC)** and **Calculation Type** to **Percentage of Earnings** or **Statutory Rate**.
4. Click **OK**.

### Payslips for contractors (Non-employee) may only contain a Super Guarantee Contribution line

This error occurs when the payslip of a contractor (non-employee) contains pay items or fringe benefit amounts. It can also occur when a superannuation line with the following **Contribution Type** is included in their payslip:

- Additional Employer Contribution (RESC)
- Pre-Tax Voluntary Contribution (RESC)
- Post-Tax Voluntary Contribution (Employee)

The payslip of a non-employee payee can only contain a superannuation line with a **Contribution Type** of **Superannuation Guarantee Contribution (SGC)**.

To fix the error:

1. Remove the non-compatible pay items from the affected payee’s draft payslip.
2. (Optional) Update the employee's pay template if required.
3. Review the superannuation line in the affected payee’s draft payslip and change the **Contribution Type** to **Superannuation Guarantee Contribution (SGC)** if required.

### [Pay item] has the category of [Pay item type] and isn’t permitted with the income type of Labour Hire

This error occurs when a payee with an income type of **Labour Hire** has one of the following pay items included in their payslip:

- Allowances
- Overtime
- Bonus and Commissions
- Paid leave
- Employee Termination Payments (ETP’s)
- Salary sacrifice amounts

To fix the error, remove the non-compatible pay items from the affected payee’s draft payslip. If required, update their pay template.

### [Pay item] has the category of Directors’ fees and isn’t permitted with the income type of Working holiday maker

This error occurs when a payee with an income type of **Working holiday maker** has a pay item with an earnings category of **Directors fees** included in their payslip.

To fix the error, remove the non-compatible pay items from the affected payee’s draft payslip. If required, update their pay template.

### Provide a leave category for [Leave pay item]

This error occurs when a paid leave item included in the employee’s payslip is missing a leave category.

To fix the error:

1. In the **Payroll** menu, select**Payroll settings**.
2. Select the **Pay Items** tab.
3. Select **Leave**, then click the pay item with **Missing category** in the **Leave Category** column.
4. Under **Leave Category**, select the category that applies to this leave pay item.
5. Click **Save**.

### Please provide an allowance type for [Allowance]

This error occurs when an allowance type pay item included in an employee’s payslip is missing a type.

To fix the error:

1. In the **Payroll** menu, select **Payroll settings**.
2. Select the **Pay Items** tab.
3. Select **Earnings**, then [add a new pay item](Add-a-custom-pay-item.md) or click an existing pay item with an **Allowance** earnings category. Allowance pay items without an allowance type are identified with an information symbol next to their **Earnings Name**.
4. Under **Type**, select the type that applies to this allowance.
5. Click **Add** if you're creating a new pay item, or **Save** to update an existing one.

Errors when posting the pay run

### Employee income type is missing or invalid

This error occurs when information for the **Income type** is missing or in an invalid format. Xero highlights the affected employee.

To fix the error:

1. In the **Payroll** menu, select **Employees**.
2. Click the employee’s name, then select the **Employment** tab.
3. Review the employee’s **Income type**.
4. Update the **Income type**, then click **Save**.

### Missing or invalid employment basis

This error occurs when information for the **Employment basis** is missing or in an invalid format. Xero highlights the affected employee.

To fix the error:

1. In the **Payroll** menu, select **Employees**.
2. Click the employee’s name, then select the **Employment** tab.
3. Review the employee’s **Employment basis**.
4. Update the **Employment basis** if required, then click **Save**.

### [Employee] is missing tax file number and will be taxed at highest rate

This error occurs when information for the **Tax File Number (TFN)** field is missing or in an invalid format. Xero highlights the affected employee.

To fix the error:

1. In the **Payroll** menu, select**Employees**.
2. Click the employee’s name, then select the **Taxes** tab.
3. Review the employee’s **Tax File Number (TFN)**.
4. Update the **Tax File Number (TFN)** or select a **TFN exemption**, then click **Save** or **Save and file now**.

### Payee’s country of origin [Country] is not valid with the income type Working Holiday Maker

This error occurs for a payee with an income type of **Working holiday maker** when the payee’s country of origin field is entered as:

- Australia
- Norfolk Island
- Christmas Island
- Cocos (Keeling) Islands
- Heard Island
- McDonald Islands

To fix the error:

1. In the **Payroll** menu, select**Employees**.
2. Click the employee’s name, then select the **Employment** tab.
3. Review the **Payee’s country of origin** field and update if required.
4. Click **Save**.

### Contractor’s ABN needs to be valid and different from the organisation’s ABN

This error occurs when the information entered in the **Australian Business Number (ABN)** field for a payee with a **Non-employee** income type is invalid, or is the same as the organisation’s ABN.

To fix the error:

1. In the **Payroll** menu, select **Employees**.
2. Click the contractor’s name, then select the **Employment** tab.
3. Review the **Australian Business Number (ABN)** field. The number entered here shouldn’t be the same as the organisation’s ABN. It should also be an active and valid ABN on the Australian Business Register (ABR).
4. Update the **Australian Business Number (ABN)** field.
5. Click **Save**.

### Employee limit exceeded

You can only process pay runs for the number of employees your pricing plan allows during a calendar month.

Xero counts the total number of employees paid in a calendar month based on the payment date of the pay run. This includes terminated employees who receive their final pay midway through the month.

You can increase the limit by [changing your pricing plan](/s/article/Changing-pricing-plan-AU).

### The chart of account code used for the pay item [pay item name] has been archived or deleted

The error **The chart of account code used for the pay item [pay item name] has been archived or deleted. Select a new account for this pay item in your Payroll Settings**occurs if an account that is affecting earnings, deductions, reimbursement, super expense and super payable pay items has been archived or overwritten by importing a new chart of accounts. You’ll also receive this error message if the pay item is linked to a [system account](Locked-and-system-accounts-in-your-chart-of-accounts.md).

To [fix the error](/s/article/Fix-an-inactive-account-error-in-your-pay-run-AU), you can either update the pay item to an active account or restore the account code causing the issue before returning to post your pay run.

Error with leave for a contractor

### Paid leave isn’t valid payment type for contractor

The error message **Paid leave isn’t a valid payment type for a contractor. Review their employment type or remove the leave request**, occurs if a leave request has been included in a contractor’s payslip. Under STP Phase 2, it’s not possible to report paid leave for a contractor.

If the **Employment type** has been set correctly as **Contractor**, remove the contractor from the pay run then delete the leave request. To do this:

1. Navigate to the pay run summary screen
2. Locate the contractors name in the list, then uncheck the green tick in the **Included** column

You’ll then be able to delete the leave request.

Once the leave request has been deleted, navigate to the pay run and include the contractor to continue processing the pay run.

Error with cashed out leave in the payslip

### Cashed out leave can’t be processed

The error message **Cashed out leave included in this payslip can’t be processed. Review the cashed out leave request or check the leave category in Payroll settings**, occurs when a cashed out leave request is included in a payslip, but the category assigned to the pay item doesn’t allow cashed out leave.

To resolve this error, either review the leave category assigned to the pay item in your organisation’s Payroll settings, or delete the leave request.

To delete the leave request, remove the employee from the pay run. To do this:

1. Navigate to the pay run summary screen.
2. Locate the employees name in the list of employees, then uncheck the green tick in the **Included** column.

You’ll then be able to delete the leave request.

Once the leave request has been deleted, navigate back to the pay run and include the employee to continue processing the pay run.

Error with leave loading in the payslip

### Leave loading can only be applied to Annual Leave

The error message **Leave loading can only be applied on leave types categorised as Annual Leave. Reset the payslip to remove leave loading, or check the leave category in Payroll settings**, can occur if your leave pay item category was changed while the pay was in draft status. Review your leave pay item settings, then reset the payslip to prompt the correct details to appear. To do this:

1. In the **Payroll** menu, select **Payroll settings**.
2. Select the **Pay Items** tab.
3. Review the category assigned to each leave type included in the pay run.

If a category was changed while the pay was in **Draft** status, update the category assigned to the leave type. To do this:

1. Select the type of pay item, eg. **Earnings** or **Leave**.
2. Click the menu icon next to the pay item you want to edit.
3. Select **Edit**.
4. Review the category selected, and correct it if required.
5. Click **Save**.

Once the leave category has been reviewed or updated, reset the employee’s payslip to ensure that the updated details will be reflected in the pay run. To do this, navigate back into the employees payslip and select **Reset Payslip**.

Error when leave can’t be included as an ETP

The error message **Leave that has been categorised as Annual Leave or Long Service Leave is unable to be included in a final pay as an ETP. Please reset the payslip or review the category selected for your leave pay items from within the Payroll Settings**,occurs if your leave pay item category was changed while the final pay was in **Draft** status. Review your leave pay item settings, then reset the final payslip to prompt the correct details to appear. To do this:

1. In the **Payroll** menu, select **Payroll settings**.
2. Select the **Pay Items** tab.
3. Review the category assigned to each leave type included in the final pay run.

If a category was changed while the final pay was in **Draft** status, update the category assigned to the leave type. To do this:

1. Select the type of pay item, eg. **Earnings** or **Leave**.
2. Click the menu icon next to the pay item you want to edit.
3. Select **Edit**.
4. Review the category selected, and correct it if required.
5. Click **Save**.

Once the leave category has been reviewed or updated, you’ll need to reset the employee’s payslip to ensure that the updated details will be reflected in the pay run. To do this, navigate back into the employees payslip and select **Reset Payslip**.

## What's next?

If you’ve received a filing error, learn how to [fix the error in your STP submission](Fix-a-filing-error-in-a-Single-Touch-Payroll-STP-submission.md).