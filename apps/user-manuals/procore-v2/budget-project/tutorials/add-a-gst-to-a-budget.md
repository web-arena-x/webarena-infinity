# Add a Goods & Services Tax (GST) to a Budget

Source: https://v2.support.procore.com/product-manuals/budget-project/tutorials/add-a-gst-to-a-budget

---

## Background

In numerous countries, a *Goods & Services Tax* (*GST*) is a tax that is applied to certain goods or services in that country. Depending on the country, it may also be referred to as a Value Added Tax (VAT). When this type of tax is levied by the government, businesses are responsible for collecting the tax on the required goods and services, as well as for remitting the taxes collected to the government.

##### Examples

The following examples are for illustrative purposes only:

- In Australia, the government levies a 10% tax is added to most goods and services, with some exemptions.
- In Canada, the government levies 5% is added to taxable goods and services. Some provinces may also levy a separate Provincial State Tax (PST) on goods and services and/or combine the GST and PST into a single Harmonized Sales Tax (HST).

To determine your country's specific tax requirements, always consult your government tax authority.

If you work in a country that requires your business to collect and remit this tax to the government, your company's Procore Administrator can create a dedicated cost code in the Company Admin tool at the company and project level. Your administrator can also choose to use the 'Other' cost type (or to create a custom cost type to associate with the GST tax cost code). Project users can then add financial line items with financial markup to associate with the cost code (and chosen cost type), so a GST line item displays on the project's payment applications (a.k.a., claim schedules) and progress claims (a.k.a., tax invoices).

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the project's Budget tool. 
     AND
 - 'Admin' level permissions on the project's Prime Contracts tool.
- **Additional Information:**

 - The GST is NOT displayed in Procore. It only displays on custom PDFs for the Tax Invoices (Claim Schedules).
 - Vertical markupwill display the markup below the budget line items.
 - If you would prefer to enable tax fields throughout the Procore interface, see [How can I use tax codes on a project?](/faq-how-can-i-use-tax-codes-on-a-procore-project)

## Prerequisites

- Add a segment item in the 'Cost Code' segment to use as your dedicated GST code. See [Add Company Cost Codes](/process-guides/company-administration-work-breakdown-structure-guide/add-company-cost-codes).

## Steps

- [Add a Budget Line Item for your GST Cost Code](#add-a-budget-line-item-for-your-gst-cost-code)
- [Enable the Financial Markup Feature on a Contract or Funding](#enable-the-financial-markup-feature-on-a-contract-or-funding)
- [Add Financial Markup for the GST Cost Code to a Contract or Funding](#add-financial-markup-for-the-gst-cost-code-to-a-contract-or-funding)

## Add a Budget Line Item for Your GST Cost Code

After creating the prerequisite GCT cost code in the Company Admin tool, use the steps below to create a budget line item for that code.

1. Navigate to the project's **Budget** tool.
2. In the **Budget** tab, click the **Create** button and choose **Budget Line Item** from the drop-down list.
3. Select your dedicated GST code from the **Cost Code** drop-down list. To learn more about adding line items, see [Add a Budget Line Item](/process-guides/resource-tracking-and-project-financials-setup-guide/add-a-budget-line-item).
4. Select 'Other' from the **Cost Type** drop-down list.

   ##### Â Note

   If you created a custom cost type for your tax, you can also select that cost type. To learn more, see [Add Company Cost Types](/process-guides/company-administration-work-breakdown-structure-guide/add-company-cost-types).

- Enter the remaining information on the line item and click **Add**.

 ##### Â Tip

 **Need to quickly add multiple line items to your budget?** Rather than adding budget line items one by one, you can import your budget line items. To learn more, see [Import a Budget](/process-guides/resource-tracking-and-project-financials-setup-guide/import-a-budget).