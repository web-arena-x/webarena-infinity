# Common issues with payday filing

Source: https://central.xero.com/s/article/Common-issues-with-payday-filing

---

## Overview

- Fix issues when filing with Inland Revenue (IR) which could be due to connection errors or user permissions.
- You'll also see how to amend a posted pay run or file negative or nil amounts.

myIR authentication error – email from Xero

If IR can’t process a file, we’ll send you an email to let you know. It could be because:

- You’re not authorised or set up in myIR to process payroll for the organisation or the Xero user role connection to myIR wasn’t established before filing.
- Your myIR account start date hasn't passed before you process a file.
- Your password for myIR was changed.
- Your organisation's IRD number in **Payroll settings** doesn't match the IRD number recorded in myIR.
- You were disconnected between filing the pay run and the file being sent to IR.
- You’ve used a different myIR user ID and password for filing for the organisation. If you're unsure which is the correct user ID for the organisation, [contact IR](https://www.ird.govt.nz/contact-us) for assistance.

Check you’re connected to myIR from Xero and have authorisation to process pay runs for the organisation. If you've been disconnected, go back to the **Pay employees** screen to [reconnect your myIR connection](Set-up-or-reconnect-your-myIR-connection-for-Payday-filing.md).

Once you're connected again, click **File with IR** in the posted pay run to re-send your payday file to myIR.

If you're still having issues after reconnecting to myIR, you’ll need to [contact IR](https://www.ird.govt.nz/contact-us) and get them to confirm the following details:

- Your myIR login name
- The organisation name
- You have full permission for payroll within myIR for this organisation
- The date(s) any pay runs have been submitted to IR but haven't been successful

IR can investigate what is causing the error preventing you from filing. Once this is resolved with IR, click **File with IR** in the posted pay run to re-send your payday file to myIR.

Connect to myIR if you’re a tax agent or third party

### Tax agent

Make sure you have:

- [Payroll admin permission](Payroll-Admin-access.md) for the Xero organisation
- Permission set up in your client’s myIR account to allow you to file on behalf of them
- [Set up your connection](Set-up-or-reconnect-your-myIR-connection-for-Payday-filing.md) to myIR from Xero using your tax agency credentials

### Non-tax agent or third party

You first need [payroll admin permission](Payroll-Admin-access.md) for the Xero organisation. Your client should then log into their business myIR account and grant you third party access or staff user permission.

Once they’ve granted you access, you’ll receive an email with a code to activate your access in myIR. Log into your myIR account within 24 hours of receiving the email, and activate the code.

If you have any issues connecting to myIR, you'll need to [contact IR](https://www.ird.govt.nz/contact-us/contact-us-index.html).

Amend a submitted payday file

Submissions to IR can take between 15–30 minutes to process.

If you submit a payday file but it needs correcting, you can:

- [Revert the pay run to draft](/s/article/Revert-a-pay-run-to-draft-NZ) (if you haven’t yet paid your employees), make the changes, and re-post the pay run. If you amend a file before it’s processed, we won’t send the file to IR until you post the pay run again. Otherwise, we’ll overwrite the existing file.
- Run an [unscheduled pay run](Adjust-previous-payroll-payments.md).
- Include the correction in the next pay run.

Warning

When reverting a pay run to draft, Xero will overwrite the file sent to IR. Don't delete the initial file in myIR. If it's deleted, you'll get an error when you re-post the pay run.

To help IR track the payday file submitted from Xero, you can provide them with the payday filing history of the pay run. You can view a filing history for each posted pay run to see who submitted the pay run, when the file was sent and IR's response. To do this:

1. In the **Payroll** menu, select **Pay employees**.
2. Click the posted pay run.
3. Click **Options**, then select **View Payday Filing History**.

Filing negative or nil amounts in a pay run

### Filing pay runs with a negative amount

If you’ve processed a pay run in Xero where an amount is negative, the amount in myIR shows as a nil value. So that the amounts in myIR match the totals in Xero, you’ll need to edit a previous filing in myIR.

Once you’ve submitted the pay run to Inland Revenue, log into myIR and edit the relevant previous pay run that the negative amounts relate to, to reduce those amounts by the negative value.

For example, Employee X had no tax code so the pay run for the pay period that ended on 27 June and was paid on 28 June showed earnings of $1,000, and tax of $450. On 29 June the employee provided the correct tax code.

To correct the tax deducted from the previous pay, the payroll admin needs to [create an unscheduled pay run](Adjust-previous-payroll-payments.md) for the period ended 27 June with a payment date of 29 June. Add a manual PAYE adjustment of negative $150 to result in a net pay of $150 paid to the employee.

When the unscheduled pay run is filed with IR, the filing shows as $0 earnings, and $0 PAYE for the employee. To correct this, the payroll admin needs to log in to myIR, locate the original pay for the period ended 27 June, manually edit the tax for Employee X to $300 and then save the changes.

### Filing a nil value pay run

If you’re not paying any employees in a pay period, you still need to file a nil value pay run with Inland Revenue.

If you revert a pay run to draft, then delete it, the return previously sent to Inland Revenue is automatically replaced with a nil return.

If you’re a seasonal business and won’t be paying staff during the off-season, [contact IR](https://www.ird.govt.nz/contact-us/contact-us-index.html) to let them know.

Error 173 Employment account closed – email from Xero

IR hasn’t been able to process your file because the Employment (EMP) account was closed for the pay period filed. This can happen if:

- You haven’t opened an Employment (EMP) account with IR when you file a pay run
- You’ve registered with a start date that's later than the pay run you’re filing for
- You’ve stopped the EMP account with IR and filed a pay run for a period after that date

We’ll send you an email to let you know. Contact Inland Revenue via your myIR account or call the Contact Centre on 0800 377 772 to fix the issue.

Information with IR doesn't match Xero

When employee details are filed with IR, a validation is made to check the details in Xero match with IR's details. If there are any differences, you'll receive a **The information with IR for [employee name] does not match what has been recorded in Xero** error message.

To successfully file employee details, check that the following fields in myIR match the employee record in Xero:

- First name
- Last name
- Date of birth
- Employee start date
- IRD number
- Employee name – made up of [Last name] then [First name]

If there are any differences, update the employee's details in myIR and save the changes.

The next time a payday file is submitted to IR, the updated details are re-filed automatically. If you want to file again manually, open the posted pay run and click **File with IR**.

Pay run not filed status

When a pay run has a status of **Not Filed**, this might be because:

- Your myIR connection isn’t established yet for this organisation. [Reconnect to myIR login](Set-up-or-reconnect-your-myIR-connection-for-Payday-filing.md) before you try to file with IR again.
- You don’t have the permissions in myIR to file for this organisation. You can get the right permissions, reconnect to myIR then go into the posted pay run and click **File with IR** orask another payroll administrator with the right permissions to file the pay run.

Payday filing missing in IR

If your pay run has a **Filed** status in Xero, we recommend you contact IR directly.

To help IR track the payday file submitted from Xero, you can provide them with the submission ID from the payday filing history of the pay run. You can view a filing history for each posted pay run to see who submitted the pay run, when the file was sent and IR's response. To do this:

1. In the **Payroll** menu, select **Pay employees**.
2. Click the posted pay run.
3. Click **Options**, then select **View Payday Filing History**.

Treatment of regional holidays and the Christmas break

Regional holidays are considered working days by IR. You need to take these days into account when working out when to file employment information.

Weekends, national public holidays, and the days between and including 25 December and 15 January aren’t considered working days.

If your business closes over the December/January holidays, you can pay your employees by [processing pay runs in advance](Process-holiday-pay-runs-in-advance.md). Payday filing is due 17 January.

## What's next?

If you’re still having trouble filing employment information through to myIR, [contact Xero support](https://central.xero.com/s/contact-support).