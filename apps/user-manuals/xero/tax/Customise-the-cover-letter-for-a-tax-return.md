# Customise the cover letter for a tax return

Source: https://central.xero.com/s/article/Customise-the-cover-letter-for-a-tax-return

---

## Overview

- Create your own cover letter for tax forms in Xero Tax using Microsoft Word.
- Add text, images and placeholders to your cover letter template.

About custom cover letters

- Xero Tax provides standard wording for cover letters and uses the logo and details from your agent profile. Create a custom cover letter to personalise the details.
- Add a logo image for your cover letter directly to the custom cover letter file. Xero won't display the logo from your agent profile if you're using a custom cover letter template.
- Customise cover letters for activity statements, fringe benefit tax returns, individual tax returns, partnership tax returns, trust tax returns, company tax returns and self-managed superannuation fund annual returns.
- Custom templates use the .docx file format. You need Microsoft Word 2007 or later to edit your templates.
- As well as text and images, custom cover letters use placeholders to pull details from the tax return and client record. For example, your client’s name or the total tax due.

Create a cover letter template

1. In the **Business** menu, select **Settings**.
2. Under **Features**, click **Custom Templates**.
3. Select the **Samples** tab.
4. Next to the sample document you want to edit, click **View Template**. The template downloads to your computer in .docx format.
5. Use Microsoft Word to edit the text and add a logo image to the file. Save the file to your computer in .docx format.
6. In the Custom Templates page, select the **Templates** tab.
7. Click **New Tax Return Cover Page**.
8. Add a name for the template, choose the .docx file from your computer and click **Save.**

Apply a cover letter template to your tax returns

1. In the **Business** menu, select **Settings**.
2. Under **Features**, click **Custom Templates**.
3. Select the **Cover Pages** tab.
4. Under **Template**, select the custom template you want to apply to each tax return type. Click **Save** when you're done.

Using placeholders in a template

As well as text and images, templates contain placeholders which they use to pull information from a client's records or tax return. Placeholders are enclosed in chevrons, eg «Name».

Read how to [insert, edit or delete placeholders in your template](Add-or-edit-advanced-invoices-quotes-templates.md).

| **Placeholder name** | **Description** | **Populated from** | **Tax form type** |
| --- | --- | --- | --- |
| Client\_PostalAddress\_Line1 | Client’s postal address line 1 | Client Details | All |
| Client\_PostalAddress\_Line2 | Client’s postal address line 2 | Client Details | All |
| Client\_PostalAddress\_Town/City | Client’s postal address town/city | Client Details | All |
| Client\_PostalAddress\_Postcode | Client’s postal address postcode | Client Details | All |
| Client\_PostalAddress\_State | Client’s postal address state | Client Details | All |
| Client\_PostalAddress\_Country | Client’s postal address country | Client Details | All |
| TaxYear | Tax year | Tax Return | All |
| SAP\_StartDate | Tax return start date | Tax Return | All |
| SAP\_EndDate | Tax return end date | Tax Return | All |
| IsAmendment | True or false flag | Tax Return | All |
| AmendmentSequence | Number of amendment | Tax Return | All |
| DatePrinted | Today’s date | Staff Profile | All |
| Name | Logged in staff name | Staff Profile | All |
| Phone | Logged in staff name | Staff Profile | All |
| Mobile | Logged in staff name | Staff Profile | All |
| Email | Logged in staff name | Staff Profile | All |
| Agent\_Name | Agent’s name | Agent Profile | All |
| Agent\_PostalAddress\_Line1 | Agent’s postal address line 1 | Agent Profile | All |
| Agent\_PostalAddress\_Line2 | Agent’s postal address line 2 | Agent Profile | All |
| Agent\_PostalAddress\_Town/City | Agent’s postal address town/city | Agent Profile | All |
| Agent\_PostalAddress\_Postcode | Agent’s postal address postcode | Agent Profile | All |
| Agent\_PostalAddress\_State | Agent’s postal address state | Agent Profile | All |
| Agent\_PostalAddress\_Country | Agent’s postal address country | Agent Profile | All |
| Agent\_PhoneAreaCode | Agent’s phone area code | Agent Profile | All |
| Agent\_PhoneNumber | Agent’s phone number | Agent Profile | All |
| Agent\_Email | Agent’s email | Agent Profile | All |
| RefundAmount | Dollar amount of tax payable or refund | Tax Return | All |
| TaxableIncomeOrLossAmount | Dollar amount of income or loss | Tax Return | All |
| TaxableIncomeOrLoss | Whether return has taxable income/loss | Tax Return | All |
| TaxDueOrRefundable | Whether return has tax due or refundable | Tax Return | All |
| \*Client\_Contact\_Name | Addressee for cover letter | Client Details | CTR, PTR, TRT, SMSF, AS, FBT |
| FamilyName | Taxpayer’s family name | Client Details | ITR |
| GivenName | Taxpayer’s given name | Client Details | ITR |
| OtherGivenName | Taxpayer’s other name | Client Details | ITR |
| PartnershipName | Name of partnership | Client Details | PTR |
| TrustName | Name of trust | Client Details | TRT |
| CompanyName | Name of company | Client Details | CTR |
| SMSFName | Name of SMSF | Client Details | SMSF |
| SummaryNetAmount | Whether payable or refundable and the amount | Activity Statement | AS |
| DueDate | Due date including agent extension | Cover tab of Activity Statement | AS |
| ClientName | Name of entity | Client Details | AS/FBT |
| PayableOrRefundable | Whether return has tax due or refundable | Tax Return | AS/FBT |
| Payable/RefundAmount | Dollar amount of tax payable or refund | Tax Return | AS/FBT |
| TaxAdjustmentDueAmount | Amount due | Tax Return | FBT |

### \*Client\_Contact\_Name

This merge field is pulled from different areas depending on the type of tax return.

- PTR: Full Name (if non-individual) or Given Name (if individual) of the partner the notices are sent to.
- TRT: Full Name (if non-individual) or Given Name (if individual) of the trustee the notices are sent to.
- CTR: Public Officer's Given Name from Tax Return Cover page under Item 5.
- SMSF: Preferred Contact tab – first name of preferred trustee or director contact details under Section K.
- AS: 'Given name' under the Signatory section of Cover (not populated from client details or client relationships).
- FBT: Given name of Item 9 – name of the person to contact.

Delete a custom template or make inactive

If you no longer need a template, you can delete it. However, you can't restore a deleted template.

Mark a template as inactive if you want to prevent it from being used, but don’t want to delete it permanently.

To delete a custom template:

1. In the **Business** menu, select **Settings**.
2. Under **Features**, click **Custom Templates**.
3. Click on the template you want to delete.
4. Click **Delete Custom Template** in the left hand navigation panel.

To mark a template as inactive:

1. In the **Business** menu, select **Settings**.
2. Under **Features**, click **Custom Templates**.
3. Click on the template you want to remove.
4. Clear the **Active** checkbox.
5. Click **Save**.

## What's next?

Now that you’ve set up your custom cover letter, [print your tax return](Print-a-tax-form.md).