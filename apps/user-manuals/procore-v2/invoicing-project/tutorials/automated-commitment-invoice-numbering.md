# Automated Commitment Invoice Numbering

Source: https://v2.support.procore.com/product-manuals/invoicing-project/tutorials/automated-commitment-invoice-numbering

---

## Background

Automated Commitment Invoice Numbering allows companies to define a company-level numbering scheme for all newly created Commitment/Subcontractor Invoices. This automation reduces manual entry, ensures consistency, and streamlines financial operations across all invoices.

## Things to Consider

- [Required User Permissions](/product-manuals/invoicing-project/permissions)

 - 'Admin' level permissions on the **Company level** Admin tool.
- **Additional Information:**

 - This process allows you to access the Invoicing toolâs settings page.
 - You will be modifying the company-level configuration for invoice numbering.

## Steps

1. Log in to your Procore account with Admin permissions.
2. Navigate to **Admin** tool.
3. Under **Tool Settings.** click **Invoicing**.
4. In the Invoicing settings, click the **Settings** tab.
5. Under the **Subcontractor Invoicing** section, find the **Invoice Numbering** setting and **Format Preview** panel.
6. Click **Edit** to open the **Invoice Number Format**.
7. Preview the Invoice Number. Use **Preview** to verify the format. The number appears in sequential order in the preview based on the starting value.
8. Configure the Invoice number format by adding and arranging the required components in the desired order, using the first or last five characters of each component. Select the components you want to include in your invoice numbers. The options include:

   - **Invoice Position** - You cannot delete the position number.
   - **Commitment Number** -Â  Uses the commitment number.
   - **Billing Period** - Uses the billing period.
   - **Billing Period End Date** - Uses the Invoice billing end date.
   - **Billing Period Number** - Uses the Invoice billing period number.
   - **Custom Text** - Type any fixed text ( For example, INV, BILL or Code).
   - **Retainage Conditional** - Will be based on the selected property format.
   - **Project Number** - Uses the Project number.
9. Configure component separator to define how each component is separated. Select the **Component Separator** from the drop-down list.

   - Dash (-)
   - Point (.)
   - Forward slash (/)
   - Underscore (\_)
   - None
10. Configure the characters for each component. Select the components you want to include in your invoice numbers. Options may include:

    - FormatÂ
    - LengthÂ

      - Invoice Position
      - Characters

    *Note: Arrange the components and set formatting options as desired.*
11. The system will validate the total character count for the invoice number.

    - *Note: If your ERP system specifies a maximum character count, Procore will enforce it. Otherwise, the default limit is 100 characters.*
12. Review the format preview to ensure it meets your requirements.
13. Click **Save** to apply the numbering scheme. 
    Note:

    - *Invoice numbers for these invoices will be auto-generated and non-editable.*
    - *The new numbering scheme will now be enforced for all newly created Commitment/Subcontractor Invoices.*