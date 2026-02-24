# Fix common problems with importing and exporting invoices

Source: https://central.xero.com/s/article/Troubleshoot-importing-and-exporting-invoices

---

## Overview

- Find solutions to errors when you import and export invoices between Practice Manager and Xero.

Error messages when you export an invoice to Xero

### TaxType code error

When you export invoices to Xero, you might get the error message, **Invoice export to Xero completed with errors. The TaxType code [CODE] cannot be used with account code [ACCOUNT].**

This error usually happens when an income or cost of sale account is mapped to the wrong type of account in Xero, eg the income account for a job category is mapped to an expense type account. This might happen if the account type was changed in Xero after it was mapped to an income or cost of sale account in Practice Manager.

To resolve this error:

1. Review the [account mapping at each level](Mapping-account-codes-to-Xero.md) to find the incorrect mapping, and either:
   - Select an account with the correct type
   - Update the [type of the selected account](Components-of-an-account-in-your-chart-of-accounts.md) in Xero
2. [Manually export](Export-invoices-to-Xero.md) any invoices that failed to sync.

### Website must be valid error

When you export invoices to Xero, you might get THE error message, **Invoice failed to export to Xero. Website must be valid.**

This error usually happens when the website address entered for the Practice Manager client or Xero contact isn’t formatted correctly. Website addresses in both Practice Manager and Xero must start with https:// or http://. For example xero.com must be entered as https://www.xero.com/.

Tip

The easiest way to make sure that the website address is formatted correctly is to copy it from the address bar in your browser.

To resolve this error:

1. Review and update:
   - The [client’s website address in Practice Manager](Edit-a-client-in-Practice-Manager.md)
   - The [contact’s website address in Xero](Edit-a-contact.md)
2. [Manually export](Export-invoices-to-Xero.md) any invoices that failed to sync.

Job number allocation error

If you bulk import new jobs or change the number format after you’ve already used Practice Manager for a while, you might see this error.

To resolve it, create a job report in the [report builder](Create-reports-with-Report-Builder.md) to work out what the next number needs to be, then update the next job number. For example, if the last used job number is 000122, then the next number should be 000123.

To update the next number:

1. In the **Business** menu, select **Settings**.
2. Under **Practice**, click **Practice Settings**.
3. On the left, click **Edit Number Sequences**.
4. Under **Job**, for the **Next Number** field, change the job number.
5. Click **Save**.

To prevent this error, [manage the number sequence](Import-data-into-Practice-Manager.md) when you structure your import file.

An invoice from Practice Manager doesn't export to Xero

If Practice Manager can't export an invoice to Xero, the invoice appears on the **Xero Export Failed** tab of the **All Invoices** screen.

This might happen if:

- The [connection between your practice and Xero](Troubleshoot-your-Xero-connection.md) is broken
- The [account codes are mapped](Mapping-account-codes-to-Xero.md) incorrectly between Practice Manager and Xero
- You [set up the export](Export-invoices-to-Xero.md) to use the Practice Manager invoice numbers but the invoice number already exists in Xero

To fix the problem:

1. In the **Business** menu, select **Invoices**.
2. Select the **Xero Export Failed** tab.
3. Select the checkbox next to one or more invoices, then click **Export** to export the invoice to Xero.
4. Practice Manager will either:
   - Export the invoice and remove it from the **Xero Export Failed** tab
   - Show you a message explaining why the invoice couldn’t be exported and help guide you to a solution

An invoice from Xero doesn't import into Practice Manager

If an invoice from Xero doesn’t appear in Practice Manager, check the following.

In Practice Manager:

- Make sure that [importing invoices](Import-invoices-from-Xero.md) is set up correctly.
- Check for an existing invoice with the same invoice number.
- [Review your practice settings](Set-up-your-practice-settings.md) and remove the period lock date if it's been set.

Practice Manager might not automatically import the invoice unless it's been edited in Xero within the last 14 days.

In Xero:

1. If you've [set a lock date](Set-up-and-work-with-lock-dates.md) that's after the creation date of the invoice, remove the lock date.
2. Open the invoice and make a minor change, eg add a space to the description, then save the invoice again.

Invoices from another system don't import into Practice Manager

If you import invoices into Xero from another system, Practice Manager might not automatically [import the invoices](Import-invoices-from-Xero.md) unless they've been edited and saved again in Xero. You must make a change to each imported invoice in Xero to trigger the import process into Practice Manager.

1. Open each invoice in Xero and make a minor change, eg add a space to the description, then save the invoice again.
2. If you're assigning invoices to jobs, check that each job in Practice Manager has a state type of **Standard**.
3. After the invoices have imported overnight into Practice Manager, check that they've imported correctly.

An unpaid invoice from Xero is assigned to the wrong client or job

If an unpaid invoice from Xero is assigned to the wrong client or job in Practice Manager, check the following.

In Practice Manager:

1. [Delete the invoice](Cancel-or-delete-an-invoice.md). This doesn't delete the invoice in Xero.
2. Make sure that [importing invoices](Import-invoices-from-Xero.md) is set up correctly.
3. If the invoice is assigned to the wrong job, make sure that the job you want to assign it to has a state type of **Standard**.

In Xero:

1. Make sure the invoice's **To** field has the client's name exactly the same as in Practice Manager.
2. If the invoice is assigned to the wrong job, make sure the invoice's **Reference** field has the correct Practice Manager job number or client order number. If there's more than one open job with the same client order number, Practice Manager assigns the invoice to the job that was created most recently.
3. Save the invoice.

After the invoice has imported overnight into Practice Manager, check that it's assigned correctly.

Invoices in Practice Manager and Xero have a small difference

Practice Manager calculates tax on invoices on each individual line item, with each amount rounded to the nearest hundredth of a unit. The total tax on the invoice is the sum of the individual line item amounts. The line-by-line calculation of tax is a standard calculation process that enables different tax rates to be used in the same invoice.

If an invoice has multiple lines, the total tax can vary by a small amount when compared with an amount that's calculated on the total taxable amount of the invoice. Adjust for the small variance either in Practice Manager or Xero by making a rounding adjustment.

To adjust the total invoice amount in Practice Manager, [add a cost](Add-costs-to-invoices-apply-markup.md) to the invoice with the following details:

- **Quantity** – either positive or negative 1 (one)
- **Unit Cost** – 0 (zero)
- **Unit Price** – the amount of the adjustment, eg 0.01
- **Tax Rate** – None

Alternatively, you could adjust the invoiced amount for some tasks and costs so that some line items round up and others round down until the accumulated rounding difference is eliminated.

## What's next?

If you're still having difficulties with importing and exporting invoices in Practice Manager, contact Xero support below.