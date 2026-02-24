# Fix a declined RTI submission

Source: https://central.xero.com/s/article/Fix-a-declined-RTI-submission

---

## Overview

- Find out why your Real Time Information (RTI) submission declined.
- You can then fix the issue using the steps on this page, and resubmit your RTI file.

Find out why your submission declined

When you post a pay run, Xero submits a Full Payment Submission (FPS) or an Employer Payment Summary (EPS) to HMRC.

If HMRC declines your submission, you (the payroll admin) will get an email notifying you of the error. Log on to Xero to check why the submission declined.

1. In the **Payroll** menu, select **RTI filings**.
2. Click the declined submission line.
3. Review the decline reason for the submission. You can also click **HMRC response** to open the RTI file. Near the bottom of the file, you’ll find a text line with the error message. In the image below, you can see a snippet of the file with a typical error message.
4. Once you've seen what the error is, you can fix it using the instructions below.

You can also download the submission file and HMRC response for any previous submissions for the pay run:

1. Click the menu icon next to the submission.
2. Select **Download Submission XML** or **Download HMRC response**.

HMRC declined this submission due to validation errors

Error message: HMRC declined this submission due to validation errors.

Review the payee information we've listed to confirm what caused the declined submission. Adjust the payee details as needed then resubmit the RTI submission:

1. In the **Payroll** menu, select **RTI filings**.
2. Click the declined submission line, then click **Resubmit**.

HMRC credentials entered in Xero not accepted by HMRC

Error message: The HMRC credentials entered into Xero have not been accepted by HMRC. Please check your HMRC credentials under the Payroll Settings > HMRC tab.

Check the credentials you've entered in the **HMRC** tab within **Payroll settings**. Please also ensure you’ve activated the credentials with HMRC. You can then resubmit your RTI submission.

1. Click **Payroll**, then select **Payroll settings**.
2. Select the **HMRC** tab.
3. Under **Employer PAYE Reference**, check the **Office Number**, **Reference Number** and **Accounts Office Reference**. These fields are case sensitive.
4. Under **Government Gateway credentials**, re-enter your **User ID** and **Password**.
5. Click **Save**.
6. In the **Payroll** menu, select **RTI filings**.
7. Click the declined submission line, then click **Resubmit**.

Tip

If you find an error message on the HMRC tab, [use our Xero Central instructions to fix it](Fix-errors-when-connecting-payroll-to-HMRC.md).

This submission cannot be accepted (filing period)

Error message: This submission cannot be accepted as it does not fall within the eligible filing period

[Contact HMRC](https://www.gov.uk/government/organisations/hm-revenue-customs/contact/employer-enquiries) (Gov.uk website) to check you’re set up for RTI filing for the current tax year. Once set up, you can resubmit your RTI submission.

1. In the **Payroll** menu, select **RTI filings**.
2. Click the declined submission line, then click **Resubmit**.

You have not been invited to submit this submission type

Error message: You have not been invited to submit this submission type

[Contact HMRC](https://www.gov.uk/government/organisations/hm-revenue-customs/contact/employer-enquiries) (Gov.uk website) to check it has the correct RTI filing details for your business. Once you’ve checked your details, you can resubmit your RTI submission.

1. In the **Payroll** menu, select **RTI filings**.
2. Click the declined submission line, then click **Resubmit**.

This submission cannot be accepted (after 19 April)

Error message: This submission cannot be accepted as the date of submission is after 19 April following the tax year to which it relates

After 19 April, HMRC no longer accepts an EPS or FPS for the previous tax year (ie pay runs with a payment date after 5 April).

Check the payment date of your last pay run. If the pay period falls in the previous tax year, you can [post a past year correction](/s/article/Adjust-previous-payroll-payments-UK) instead.

Value '-XX' is too small (YTD)

Error message: Value '-XX' is too small / Invalid content found at element '...YTD'

This error occurs if you refund an amount through a pay run, but the amount is greater than the year-to-date total. Eg if an employee’s pension year-to-date total is £20, but you refund them £30 in a pay run, HMRC won't accept a value of -£10.

Check the year-to-date totals in your last pay run, and ensure you’re not submitting a negative amount. If you find a negative amount, [revert the pay run to draft](/s/article/Revert-a-pay-run-to-draft-UK) and remove the refund. You can then re-post the pay run. Xero will send an updated RTI submission to HMRC.

Tip

If you need to refund amounts relating to a previous tax year, you can [post a past year correction](/s/article/Adjust-previous-payroll-payments-UK).

This submission cannot be accepted (employer scheme cancelled)

Error message: This submission cannot be accepted as this employer scheme has been cancelled

[Contact HMRC](https://www.gov.uk/government/organisations/hm-revenue-customs/contact/employer-enquiries) (Gov.uk website) to fix this error. You can’t fix the error without HMRC’s help. You can then resubmit your RTI submission.

1. In the **Payroll** menu, select **RTI filings**.
2. Click the declined submission line, then click **Resubmit**.

Invalid content found at element "AtLEYTD"

Error message: Invalid content found at element "AtLEYTD"

This error occurs if an employee’s Lower Earnings Limit (LEL) balance exceeds HMRC’s threshold.

An employee's balance might exceed the threshold if:

- They're set up as a director on the annual calculation method, but this changes during the tax year.
- The opening balances entered for the employee are too high.

 If you receive this error message, please contact Xero Support below.

The NI Letter cannot be B or T if (GENDER) is shown as male

Error message: The NI Letter cannot be B or T if (GENDER) is shown as male. Please check.

You can only select certain NI categories based on an employee's gender. Check you’ve entered the correct NI category for each employee. You can then revert the pay run to draft, reset applicable payslips, and repost the pay run.

1. In the **Payroll** menu, select **Employees**.
2. Click an employee’s name to open their details.
3. Select the **Employment information** section, and check the employee’s **NI Category**.
4. Click **Save**, then repeat the steps above for other employees.
5. [Revert the pay run to draft](/s/article/Revert-a-pay-run-to-draft-UK).
6. If you edited an employee’s NI Category, click their name to open their payslip, then click **Reset Payslip**.
7. Click **Save** or **Save & Close**, then repeat the steps above for other employees.
8. Repost the pay run. Xero will send an updated RTI submission to HMRC.

Value 'XXXXX' doesn't have the correct format (AccountNo)

Error message: Value 'XXXXX' doesn't have the correct format / Invalid content found at element 'AccountNo'

Check you’ve entered the correct bank account number for payroll. You can then resubmit your RTI submission.

1. In the **Accounting** menu, select **Bank accounts**.
2. Next to the bank account you use for payroll, click the menu icon .
3. Click **Edit account details**.
4. Update the **Bank Account Number**, then click **Save**.
5. In the **Payroll** menu, select **RTI filings**.
6. Click the declined submission line, then click **Resubmit**.

## What's next?

If you can’t fix an RTI filing error, please contact Xero support below.