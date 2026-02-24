# Fix automatic superannuation errors

Source: https://central.xero.com/s/article/Fix-problems-with-superannuation-filing

---

## Overview

- Resolve automatic superannuation registration, verification and filing errors.

## What you need to know

- When an auto super batch fails to process, the batch status updates to **Failed** in Xero. It usually takes up to five business days for the status to update but might take longer during peak processing times, such as the end of the quarter.
- An email with the reason why the batch failed is sent to the nominated auto super authoriser and the organisation’s subscriber.

ABN not active/valid

An ABN not active or ABN not valid error indicates the company details entered for your Xero organisation don’t match those registered with the Australian Business Register (ABR).

To resolve the error, [update the ABN](Update-your-organisation-s-settings.md) in your organisation’s settings.

Employer not found/unknown employer

An employer not found or unknown employer error indicates the company details entered for your Xero organisation don’t match those registered with the Australian Business Register (ABR).

To resolve the error, [update the ABN](Update-your-organisation-s-settings.md) in your organisation’s settings.

Invalid bank details

An invalid bank details error means the bank account details in Xero don’t match the bank’s records, or the details don’t meet formatting requirements.

[Update the bank details](Edit-or-merge-a-bank-account.md) in Xero to make sure that:

- The account name in Xero matches the account name on your bank statement.
- The account name and number in Xero doesn’t contain any spaces, dashes or special characters.
- The account details in Xero follow this format: BSB: 000-000 Account Number: 000000000.

If the bank account number contains any letters or exceeds nine digits, contact your bank to get a default number. Once you have the default number, [set up a new bank account](Add-a-bank-account-or-credit-card-account.md) or edit your existing one.

Fund no longer active and cannot accept contributions

An inactive fund cannot accept contributions error means the fund provider has updated its details, such as ABN or USI, or has merged with another fund.

To resolve this, you need to contact the super fund provider to confirm their latest details. Once you have the fund’s new details:

1. [Create a new super fund](/s/article/Set-up-superannuation-AU) using the updated details.
2. [Mark the old super fund as inactive](Inactivate-or-delete-a-super-fund.md).
3. [Update the employee’s existing super membership](Change-superannuation-funds-for-future-or-past-payments.md) to reflect the new details.

Run the [Superannuation Accrual report](Superannuation-Accrual-report.md) to ensure the details have been updated for all outstanding accruals.

Email not recorded

An email not recorded error means an employee included in the batch doesn’t have an email address entered in their employee record in Xero.

To resolve this, you need to enter an email address for each employee:

1. In the **Payroll** menu, select **Employees**.
2. Click the employee's name.
3. Select the **Details** tab.
4. Under **Contact Information**, enter the employee’s email address.
5. Click **Save**.

Run the [Employee Contact Details report](Employee-Contact-Details.md) to identify which employees don’t have an email address entered in Xero.

The organisation's email address is not a valid email address format

An invalid email error occurs when an employee email address has an incorrect domain or contains invalid characters. For example:

- johnsmith@gmaul.com
- johnsmith@gmail,com

To resolve this error:

1. Run the [Employee Contact Details report](Employee-Contact-Details.md).
2. Check the email addresses to identify any with an incorrect domain or invalid character.
3. Correct the email address in the employee record.
4. Resubmit the auto super batch.

SMSF details contain invalid characters

If you receive an error about your self-managed super fund (SMSF) name, bank account name or employer number containing invalid characters, you’ll need to review your SMSF details.

Valid characters are:

- Numerals
- Letters, uppercase and lowercase
- These punctuation symbols: . , ? ( ) { } : ; ' | - \_ = / @ # \$ % \* ! & " "

If your SMSF name, account name or employer number contains invalid characters, update your SMSF details:

1. In the **Payroll** menu, select **Payroll settings**.
2. Select the **Superannuation** tab.
3. Click the menu icon next to the relevant fund, then select **Edit**.
4. Remove any invalid characters.
5. Click **Save**.

Submission failed… Something has gone wrong

If the submission of a batch fails with a ‘Something has gone wrong’ error, this usually means the auto super authoriser's mobile number is invalid.

The authoriser or the organisation’s subscriber will need to [update the authoriser’s mobile number](/s/article/Edit-auto-superannuation-registration-details?userregion=true). We recommend you enter an Australian mobile number to ensure the authoriser is able to approve the payments. Some international numbers aren’t supported by our SMS service provider.

You’ll then need to [delete the payment batch](Delete-a-superannuation-payment.md) and submit a new batch for approval.

Authorisation attempt limit exceeded

An authorisation attempt limit exceeded error occurs when the nominated super authoriser has entered an incorrect code too many times when attempting to approve a payment batch. If the attempt limit is exceeded, the batch is automatically rejected.

To resolve this, you’ll need to create a new payment batch for the authoriser to approve. The authoriser will receive an SMS from Xero with the authorisation code. They must enter this code exactly as it shows in the SMS to approve the batch.

SMS authorisation code not received

It can take up to 24 hours for an SMS to process, depending on the carrier you use and your network connection. If the auto super authoriser hasn’t received the SMS after 24 hours, you can resend the code:

1. In the **Payroll** menu, select **Superannuation**.
2. Click the batch that’s pending approval.
3. Click **Approve**.
4. Click **Haven’t received it? Resend a new code**.

If needed, the authoriser or the organisation's subscriber can [update the authoriser’s mobile number](/s/article/Edit-auto-superannuation-registration-details?userregion=true). We recommend you enter an Australian mobile number to ensure the authoriser is able to approve the payments. Some international numbers aren’t supported by our SMS service provider.

If you update the authoriser’s number, you’ll need to [delete the payment batch](Delete-a-superannuation-payment.md), then submit a new batch for approval.

You haven’t completed the bank verification yet

Once you approve an automatic superannuation payment batch, you might be required to verify the bank account registered for your auto super payments.

This message indicates that verification wasn’t completed within the specified timeframe.

To continue using automatic superannuation, you need to [verify your bank account](Verify-your-bank-account-for-automatic-superannuation-payments.md). Once verified, your access to automatic superannuation is automatically reinstated and the super payment will continue to process.

Your super payment is cancelled

Once you approve an automatic superannuation payment batch, you might be required to verify the bank account registered for your auto super payments.

This message indicates that verification was unsuccessful. The super payment has been refunded to your bank account.

To continue using automatic superannuation, you need to [verify your bank account](Verify-your-bank-account-for-automatic-superannuation-payments.md). When you verify the account, you need to enter the payment reference number (PRN) from the initial superannuation payment debit transaction.

Once verified, your access to automatic superannuation is automatically reinstated and you can reprocess the payment batch.

Access to automatic superannuation has been locked

Once you approve an automatic superannuation payment batch, you might be required to verify the bank account registered for your auto super payments.

This message indicates that verification wasn’t completed within the specified timeframe, or that the verification attempts were unsuccessful.

If you haven’t attempted to, you need to [verify your bank account](Verify-your-bank-account-for-automatic-superannuation-payments.md).

If you’ve had three failed attempts at verification, please contact Xero support below and include the payment reference number (PRN) in your message. If you’re unsure what the PRN is, Xero support can help you locate it.

Unauthorised user

An unauthorised user error means that the email address you’ve used to log in to Xero doesn’t match the nominated super authoriser’s email address. The registered authoriser is the only user who can enter the code to approve a super payment batch.

If you are the authoriser but have multiple user logins for the organisation, try to log in with your other email address to enter the code.

If you aren’t the registered authoriser, you need to contact the authoriser and ask them to log in to enter the code.

The authoriser or the organisation's subscriber can [update the authoriser's details](/s/article/Edit-auto-superannuation-registration-details?userregion=true) if needed. If you update the authoriser’s details, you’ll need to [delete the old payment batch](Delete-a-superannuation-payment.md), then submit a new batch for approval.

Direct debit failed

Your direct debit might fail if:

- The nominated bank account isn't set up for direct debit purposes.
- The organisation has recently changed bank accounts.
- The bank account is invalid or has insufficient funds.

If your bank account is set up for direct debits and you have sufficient funds, check that the bank account name registered for auto super matches the bank account name on your bank statement.

If needed, the super authoriser or the organisation’s subscriber can [update the bank account registered for super payments](/s/article/Edit-auto-superannuation-registration-details?userregion=true). If you update the bank account details, you’ll need to submit a new batch.

It can take up to five business days for a batch status to change from **Approved, pending processing** to **Failed** in Xero when the direct debit is unsuccessful.

An unexpected error occurred

As a first step to resolve an unexpected error occurred message, please:

1. Wait for the batch status to change from **Approved, pending processing** to **Failed**.
2. Reprocess the contributions in a new auto super batch.

If the batch fails again with the same error, contact Xero support below.

SMSF inactive or invalid

A self-managed super fund (SMSF) ABN inactive or invalid error means that the ABN entered for an SMSF within the batch is incorrect or inactive. You can check the status of a super fund on the [Super Fund Lookup website](https://superfundlookup.gov.au/).

To resolve this, your employee needs to either:

- Update their SMSF status with the ATO
- Provide you with alternative fund details

If your employee provides new fund details:

1. [Create a new super fund](/s/article/Set-up-superannuation-AU) using the new details.
2. [Mark the old super fund as inactive](Inactivate-or-delete-a-super-fund.md).
3. [Update the employee’s existing super membership](Change-superannuation-funds-for-future-or-past-payments.md) to reflect the new details.

You might also like to run the [Superannuation Accrual report](Superannuation-Accrual-report.md) to ensure the details have updated for all outstanding accruals.

Electronic service address invalid

An invalid electronic service address (ESA) error indicates that the ESA entered for the super fund is incorrect.

The ESA is a unique fund identifier and can be up to 16 alpha-numeric characters.

You’ll need to contact the fund provider to confirm their ESA, then update the details for the fund in Xero:

1. In the **Payroll** menu, select **Payroll settings**.
2. Select the **Superannuation** tab.
3. Next to the relevant fund, click the menu icon , then select **Edit**.
4. Make changes if required, then click **Update**.

Super payment returned

Take a look at our support article on [reprocessing returned super payments](Reprocess-failed-or-returned-auto-super-payments.md) for the steps to follow.

## What's next?

Once you’ve resolved the error, [reprocess the super payment](Process-superannuation-payments.md).