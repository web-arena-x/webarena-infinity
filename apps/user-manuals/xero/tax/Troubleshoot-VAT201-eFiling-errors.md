# Resolve VAT201 eFiling errors

Source: https://central.xero.com/s/article/Troubleshoot-VAT201-eFiling-errors

---

## Overview

- Learn more about the submission status of a VAT201 return.
- Troubleshoot errors when filing tax returns with the South African Revenue Service (SARS).

Submission status explained

### Pending

The **Pending** status indicates that the submitted return is waiting to be processed by SARS. This status remains until SARS begins processing the submitted return.

When a submission is Pending, you won’t be able to revert your finalised return to draft or submit your return again.

### Filed

Successfully submitted returns have a **Filed** status. This indicates SARS has successfully received the return and is now processing it.

You can’t submit your tax return through Xero again once a return has been successfully filed. If you need to submit another return for the same tax period, you’ll need to do it manually through the SARS eFiling portal.

### Submission Failed

If a return hasn't been filed successfully, it will have the **Submission Failed** status. To troubleshoot this, see the information below.

Resolve Submission Failed errors

If your submission fails, you might get one of the following errors on a **Submission Failed** banner.

### VAT201 return already submitted

If you’ve already submitted a tax return manually through the SARS eFiling portal or through Xero and you try to file a tax return through Xero for the same period, you’ll see an error saying that the tax return has already been filed.

If you want to resubmit your tax return, you’ll need to do it manually through the SARS eFiling portal.

### Incorrect SARS ISV login name and ISV login key

You might get this error if you enter your normal SARS eFiling login details. You’ll need to enter the new login name and key SARS generated when you [added Xero as an Independent Software Vendor (ISV)](Set-up-eFiling-for-VAT-in-Xero.md).

### SARS ISV login name or ISV login key is not recognised for this VAT number

One SARS account can be registered to submit on behalf of multiple organisations. You’ll need to check the VAT registration number is correct and registered under the SARS account you’re using.

### Invalid tax period submission

You might get this error if you’re trying to submit a return for a period that doesn’t match what SARS is expecting. For example, the period may have the incorrect start date or the incorrect frequency. You’ll need to check you’re filing for the correct period.

You can only file your tax return from Xero on a monthly or bi-monthly frequency. If you want your filing frequency to be different, you’ll need to check with SARS that it’s the correct filing frequency for you and file your return outside of Xero.

You should also check the return has been filed for your previous tax period. If the previous return hasn’t been filed, SARS will be expecting a previous tax return.

### Return cannot be submitted before the tax period has ended

You might get this error message if you try to submit your tax return before the tax period has ended. You’ll need to wait for the end of the tax period before submitting the return.

### Return not filed

You might get this error message if the return couldn't be filed due to an authorisation error. Please [disconnect the SARS Integrator app](Access-review-or-disconnect-app-connections.md) in the Connected apps screen, then reconnect using the CloudConvert authorisation process in [VAT settings](Set-up-eFiling-for-VAT-in-Xero.md).

If the error persists, please get in touch and let us know.

### An unexpected error has occurred during processing

You might get this error message if you have negative values on your VAT201 return. Field 20 is the only exception, as the negative value will determine if you're entitled to a refund.

If you get this error message, check your transactions are entered correctly then try and file the return again. If there are no negative transactions and the error persists after 24 hours, please get in touch and let us know.

### Customs Code is mandatory if specific fields are set

If any of the following fields have a non-zero value, you must provide a customs code to SARS:

- **Field 2A** – Zero rated (only exported goods)
- **Field 14A** – Capital goods imported
- **Field 15A** – Other imported goods

You'll need to enter your customs code in [VAT](Set-up-eFiling-for-VAT-in-Xero.md) [settings](Set-up-eFiling-for-VAT-in-Xero.md) and try filing the return again.

### Customs Code is invalid

You might get this error if you've entered an incorrect customs code or if the code you've entered isn't registered with your organisation. You'll need to check you're using the correct customs code that has been assigned to your organisation.

If no customs code is required, you can leave this field blank.

Resolve a failed submission without error message

If you see a **Submission Failed** status but no banner, this may be caused by a connection error. We recommend trying to file the return again later.

If issues persist, please let us know. We also recommend filing your return manually through the SARS eFiling portal.

## What's next?

If you need more help, contact Xero support below.