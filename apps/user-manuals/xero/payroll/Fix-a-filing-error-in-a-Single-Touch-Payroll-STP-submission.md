# Fix a filing error in a Single Touch Payroll submission

Source: https://central.xero.com/s/article/Fix-a-filing-error-in-a-Single-Touch-Payroll-STP-submission

---

## Overview

- Resolve a Single Touch Payroll (STP) filing error where a submission fails.

How it works

Xero will send you an email if your STP submission fails.

If it's a full file failure, Xero lists the submission’s filing status as **Failed** on either the pay run page or the STP Overview page.

If a pay run is showing as **Partly filed**, this means the ATO has accepted the submission and your payroll reporting obligations have been met. However, the full details could not be retrieved from the ATO, and one or more employee submissions may not have been accepted. **The filing status of individual employees is unknown** (below) has more details on this.

You can continue filing pay runs as normal. Your year-to-date (YTD) information updates when the next submission is sent to the ATO.

Tip

If you've made a non-filing mistake (eg you've overpaid an employee), you can [correct the mistake in a pay run](Correct-a-mistake-in-a-pay-run.md).

Payslips have a combined gross YTD amount less than 0

You see the error message **Payslips containing negative earnings amounts have resulted in a combined gross year-to-date amount less than 0. This must be corrected prior to filing**, when payment types have been included as negative amounts in processed pay runs. This causes the year-to-date balance of the payment type, less salary sacrifice, to be less than $0.00. These payment types include ordinary time earnings, paid leave, allowances, overtime, bonuses and commissions, directors' fees and lump sum type W.

To fix the error:

1. Run the [Payroll Activity Summary report](Payroll-Activity-Summary-report.md) for the relevant financial year to see the total amounts processed against each payment type.
2. Identify which payment type has been over-reduced for the relevant financial year (ie the sum of the payment is less than $0.00).
3. [Process an unscheduled pay run](/s/article/Adjust-previous-payroll-payments-AU) and offset the negative balance with a positive amount against the relevant payment type.
4. [Enter a manual tax adjustment](/s/article/Manually-adjust-tax-for-an-employee-s-pay-AU) if required.
5. Click **File**.
6. Select the checkbox to confirm you’ve read and accepted the authorisation to file.
7. Click **Submit to the ATO**.

Tip

If a payment needs to be reduced, ensure the unscheduled pay run is created for the relevant financial year.

Employee has YTD payment amounts that can’t be reported for their income type

You see the error message **The employee has year-to-date {Payment type} amounts that cannot be reported when their income type is {Payee income type}. Based on ATO rules, the total amount must be $0.00 before this can be filed**, when certain payment types have been processed for a payee with an incompatible income type. These payment types include overtime, bonuses and commissions, directors' fees, lump sum payments, salary sacrifice and ETPs.

Payments processed against an incompatible income type need to be reduced to $0.00 before you can file the pay run successfully.

A payee’s employment relationship, including their employment type and income type, determines what payments can be made to the employee in STP Phase 2 payloads. Not all amounts can be reported for all income types.

To fix the error:

1. Run the [Payroll Activity Summary report](Payroll-Activity-Summary-report.md) for the relevant financial year and employee to see the total amounts processed against each payment type.
2. Identify which payment type has been processed incorrectly for the relevant financial year (ie if bonus and commission payments have been paid to a labour hire employee, the total sum of these will need to be reversed).
3. [Process an unscheduled pay run](/s/article/Adjust-previous-payroll-payments-AU) for the relevant financial year and enter a negative balance against the incompatible payment type previously processed to the employee. For example, if $1000 of bonuses and commissions need to be reversed, enter -$1000.
4. If applicable, add the total amount as a positive to the pay run against the correct pay item. We suggest checking that the pay item in use is compatible with the employee’s income type.
5. [Enter a manual tax adjustment](/s/article/Manually-adjust-tax-for-an-employee-s-pay-AU) if required.
6. Click **File**.
7. Select the checkbox to confirm you’ve read and accepted the authorisation to file.
8. Click **Submit to the ATO**.

Tip

If a payee’s employment type or income type has changed during the year, create a new employee record for the updated employment or income type. Learn more about [changing a payee’s employment status](Change-employment-status.md).

STP Finalisation failed: The employee is missing details that are required for filing with STP 2

You see the error message **The employee is missing details that are required for filing with STP 2, please update the employee's employment and taxes details**, if an employee is missing employment type, income type and tax scale type when reporting with STP 2.

Both active and terminated employees need to be updated for STP 2 to include them in a STP finalisation.

To resolve the error, check the employee’s details are updated, and then resubmit your STP finalisation. To do this:

1. In the **Payroll** menu, select **Employees**.
2. Click the employee’s name. If the employee has been terminated, select the **Past** tab then click their name.
3. Select the **Employment** tab, then click **Update**.
4. Update the required fields, then click **Save & continue**.
5. Click **Back to employees**.
6. Select the **Taxes** tab, then click **Update**.
7. Update any necessary details, then click **Save**.

Once you’ve updated the employee record, resubmit the STP finalisation for the affected financial year.

STP Finalisation failed: No pay runs have been filed

To resolve the error message **CMN.ATO.PAYEVNT.EM92168 - Your finalisation for the financial year was declined because no pay runs have been filed during that year**, you'll need to [file the last pay run](File-your-employees-pay-and-super-with-Single-Touch-Payroll-STP.md) processed for the financial year.

If no pay runs have been processed yet for the financial year, you'll first need to [post a pay run](/s/article/Process-a-pay-run-and-pay-employees?userregion=true). Due to ATO reporting requirements for STP, this needs to be a scheduled pay run. You'll also need to post and file a pay run if you’ve recently used the reset tool.

Once you’ve successfully posted and filed a pay run, you can resubmit the STP finalisation.

Tip

When you file a pay run or finalise your STP data, it can take up to 72 hours for the status in Xero to update.

Authentication failed ({Error Code})

If you receive the error message **Authentication failed ({Error Code}). It looks like you're not set up with the ATO. Please call the ATO to get connected**, it's important to check the user filing pay runs has set up the correct permissions in the STP settings. The Software ID (SSID) also needs to be registered with the ATO via phone or Access Manager (registered tax/BAS Agents).

If you are an employer, check the organisation’s SSID has been registered with the ATO. To do this:

1. In the **Payroll** menu, select **Pay employees**.
2. Click **Single Touch Payroll Settings**.
3. On the **Review organisation details** page, click **Continue**.
4. (Practice managers) On the **Review agent details** page, ensure the organisation’s ABN and branch number are correct, then click **Continue**.
5. Connect to the ATO.
6. Select the checkbox to confirm you've contacted the ATO.
7. Click **Register**.
8. [Refile the pay run](File-your-employees-pay-and-super-with-Single-Touch-Payroll-STP.md).

If you're a registered tax/BAS agent, check you’re set up to lodge on behalf of the client, and the organisation’s SSID has been registered against your practice's ABN. To do this:

1. In the **Payroll** menu, select **Pay employees**.
2. Click **Single Touch Payroll Settings**.
3. On the **Review organisation details** page, click **Continue**.
4. In the **File STP as** field, select the practice to lodge on behalf of your client. Alternatively, select the organisation to lodge under the organisation’s SSID.
5. On the **Review agent details** page, ensure the agent and practice details are correct, then click **Continue**.
6. Connect to the ATO.
7. Select the checkbox to confirm you've contacted the ATO.
8. Click **Register**.
9. [Refile the pay run](File-your-employees-pay-and-super-with-Single-Touch-Payroll-STP.md).

If the error occurs again when you refile the pay run, refer to the ATO's page on [authentication errors](https://www.ato.gov.au/Tax-professionals/Digital-services/In-detail/Practitioner-lodgment-service-user-guide/?anchor=Authenticationerrors).

Invalid ABN or branch number

To resolve the error message **The branch number for your organisation is incorrect or invalid and needs to be updated**, you need to fix the error, then refile the pay run. To do this:

1. Click on the organisation name, select **Settings**, then click **Organisation details**.
2. Under **Basic Information**, update the **Branch** field with the correct code.
3. Click **Save**.
4. [Refile the pay run](File-your-employees-pay-and-super-with-Single-Touch-Payroll-STP.md).

To resolve the error message **The ABN for your organisation is required**:

1. Click on the organisation name, select **Settings**, then click **Organisation details**.
2. Under **Basic Information**, update the **Australian Business Number** field with a valid ABN for the organisation.
3. Click **Save**.
4. [Refile the pay run](File-your-employees-pay-and-super-with-Single-Touch-Payroll-STP.md).

To resolve the error message **The ABN for the Xero HQ practice is invalid and needs to be updated**:

1. Click on the organisation name, select **Settings**, then click **Organisation details**.
2. Under **Basic Information**, update the **Australian Business Number field**. This should be the ABN for your practice, rather than your client's ABN.
3. Click **Done**.
4. [Refile the pay run](File-your-employees-pay-and-super-with-Single-Touch-Payroll-STP.md).

Tip

Updating your ABN or branch number partway through a financial year can have reporting implications. [Correct your STP data](Correct-your-STP-data-after-a-change-in-ABN.md) after a change in ABN or branch number.

Organisation address issues

If your organisation's address isn't correctly entered, you might see the following error messages:

- The state for your organisation’s address is required.
- The postal / zip code for your organisation’s address is invalid and needs to be updated.
- The postal / zip code for your organisation’s address is required.

You need to fix the error, then refile the pay run. To do this:

1. Click on the organisation name, select **Settings**, then click **Organisation details**.
2. Under **Contact Information**, update the appropriate field. When the organisation's address is in Australia, you must supply a postcode in the range of 0200-9999.
3. Click **Save**.
4. [Refile the pay run](File-your-employees-pay-and-super-with-Single-Touch-Payroll-STP.md).

Invalid email address for user

To resolve the error message **The email address of the user who filed the pay run is invalid and needs to be updated**, you need to fix the error, then refile the pay run. To do this:

1. [Log in to Xero and change your email address](Change-Xero-login-password-or-email.md#LogintoXeroandchangeyouremailaddress).
2. [Refile the pay run](File-your-employees-pay-and-super-with-Single-Touch-Payroll-STP.md).

To resolve the error message **The email for the employee is invalid and needs to be updated**, you need to either [revert the pay run to draft](Revert-a-pay-run-to-draft.md) to fix the error, or fix the error in the next scheduled pay run. To do this:

1. In the **Payroll** menu, select **Employees**.
2. Click the employee’s name.
3. Select the **Details** tab.
4. In the **Contact Information** section, update the **Email** field.
5. Click **Save**.
6. (Optional) If you reverted the pay run to draft, you can now re-post it.

To re-post the pay run:

1. In the **Payroll** menu, select **Pay employees**.
2. Click the draft pay run to open it.
3. [Post the pay run](/s/article/Process-a-pay-run-and-pay-employees#3Postapayrun).

Invalid tax file number (TFN)

If the employee's TFN hasn't been entered or has been entered incorrectly, you might see one of the following error messages:

- The employee's TFN is invalid and needs to be updated.
- The employee's TFN is required.

To resolve the error, review and update the employee’s TFN:

1. In the **Payroll** menu, select **Employees**.
2. Click the employee’s name.
3. Select the **Taxes** tab.
4. Enter or update the employee’s TFN, or select an exemption reason.
5. Click **Save**.

The updated tax details will automatically report to the ATO the next time you file a pay run for the employee.

Invalid date of birth for employee

If the employee's date of birth has been entered incorrectly, you might see one of the following error messages:

- The date of birth for the employee is invalid and needs to be updated.
- The date of birth for the employee can’t be in the future.

You need to either [revert the pay run to draft](Revert-a-pay-run-to-draft.md) to fix the error, or fix the error in the next scheduled pay run. To do this:

1. In the **Payroll** menu, select **Employees**.
2. Click the employee’s name to open their details.
3. In the **Details** tab under **Basic Information**, update the **Date of Birth** fields.
4. Click **Save**.
5. (Optional) If you reverted the pay run to draft, you can now re-post it.

To re-post the pay run:

1. In the **Payroll** menu, select **Pay employees**.
2. Click the draft pay run to open it.
3. [Post the pay run](/s/article/Process-a-pay-run-and-pay-employees#3Postapayrun).

The filing status of individual employees is unknown

Depending on the details of the error message, you can either continue filing pay runs as normal, or you need to submit a new finalisation with the ATO.

You see the error message **Your STP reporting obligations have been met, but the full details could not be retrieved from the ATO. You can continue to file pay runs as normal. No further action is required**, if the ATO has accepted your filing but the individual status of each employee isn't confirmed. You can still continue filing pay runs, however the status of this pay run will remain partly filed.

You see the error message **The status of each employee couldn't be retrieved from the ATO. Please submit a new finalisation that includes all employees from this one**, if the ATO has declined your filing and so the individual status of each employee isn't confirmed. You need to submit a new finalisation that includes all employees from the failed filing.

Filing for a transaction from over 350 days ago

To resolve the error message **CMN.ATO.PAYEVNT.000215 - This filing is for a transaction that occurred over 350 days ago. This filing will not be accepted by the ATO and no further action is required**, you can either:

- Revert the pay run to draft and change the payment date to be within 350 days of today’s date
- Resubmit the STP finalisation for the affected financial year to ensure year-to-date amounts are reported to the ATO

## What's next?

If your filing error still isn't fixed, contact Xero support below.