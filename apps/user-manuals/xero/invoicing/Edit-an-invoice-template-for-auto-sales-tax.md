# Edit an invoice template for auto sales tax

Source: https://central.xero.com/s/article/Edit-an-invoice-template-for-auto-sales-tax

---

## Overview

- Update your invoice templates so they work with auto sales tax.

Tip

The information on this page only applies if your organization uses [auto sales tax](How-automatic-sales-tax-works.md).

## Simplify the tax information

If you use a standard template to [customize your invoices](Invoice-templates-explained.md), you might want to make the following changes to make the tax information simpler for your customer. Check that these settings will meet your state’s invoicing requirements if you’re not sure.

1. In the **Sales** menu, click **Sales settings**.
2. Click **Invoice settings**.
3. Next to the standard template you want to update, click **Options**, then select **Edit**.
4. Make sure the **Show tax column** box is cleared.
5. Under **Show tax subtotals by**, make sure **a single tax subtotal** is selected.
6. Click **Save**.

## Check the addresses

You might also need to make changes to your invoice template to ensure the addresses are correct, particularly if you’ve changed the **Ship from/location of sale** or **Ship to address**.

You can preview the invoice after you’ve created it by using either the [preview or print PDF](Print-or-preview-a-customer-invoice.md) option.

If you use a standard template, we recommend:

- The **Ship from/location of sale** is included in the contact details field in the invoice template.
- [Display delivery address on this invoice](Add-a-delivery-address-to-an-invoice.md) is selected under the **Contact**, and the **Ship to address** matches the delivery address in the contact record. The delivery address will automatically update to the ship to address.

If you use an [advanced template](Add-or-edit-advanced-invoices-quotes-templates.md), we recommend:

- The **Ship from/location of sale** is included in the invoice template. You can either add it as static text, or use the OrganisationPhysicalAddress mergefield in the template. If you use the mergefield, make sure the **Ship from/location of sale** matches the physical address in [Organization settings](Update-your-organisation-s-settings-US.md).
- The [ContactPhysicalAddress mergefield](Fields-you-can-insert-into-a-custom-template.md) is included in the invoice template, and the **Ship to address** matches the delivery address in the [contact record](Edit-a-contact.md).

## What's next?

Find out how to add an [auto sales tax invoice](Use-automatic-sales-tax-in-invoices.md).