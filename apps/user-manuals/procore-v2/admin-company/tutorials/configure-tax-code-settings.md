# Configure Tax Code Settings

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/configure-tax-code-settings

---

## Background

In Procore's Project Financials tools, you can set up one or more *tax codes* in Procore's Company Admin tool. This provides your Project Financials users with the ability to apply a specific tax to line items on a Schedule of Values (SOV). To turn this feature ON in your company's Procore account, your company's Procore Administrator uses the steps below.

After creating your company's tax codes, project users can apply the code to the SOV line items on a contract, funding, change order, and invoice. To calculate the tax amount, Procore applies the tax code to the line item amount, including financial markup, to determine the tax amount. Procore then adds the tax amounts from each line item to determine an unrounded sum and then rounds that sum to determine the total tax amount.

Tax code fields appear in the schedule of values and on PDF forms. You can also see the total tax amount on these PDF forms, broken out from the grand total. In addition, you can set up multiple tax codes that can be applied to line items that require different tax rates.

Invoice PDFs also reflect the tax. The Summary page of the PDF will add:

- Tax applicable to this payment
- Current payment due including tax

## Things to Consider

- **Required User Permissions**:

 - 'Admin' level permissions on the Company level Admin tool.
- **Additional Information**:

 - Enabling the tax codes feature in the Company Admin tool makes the feature available on all of your company's Procore projects. By default, tax codes are disabled on projects.
 - To enable the feature on a per-project basis, see [Update General Project Information](/product-manuals/admin-project/tutorials/update-general-project-information).
- **Limitations**:

 - You can only create one (1) tax type. Multiple tax types are NOT permitted.
- For companies using the ERP Integrations tool: Not all integrations support tax codes.

## Steps

Complete these steps:

1. Enable the Tax Codes Setting
2. Set the Tax Type
3. Add a Tax Code

### Enable the Tax Codes Setting

1. Navigate to the Company level **Admin** tool.
2. Under **Tool Settings**, click **Tax Codes**.
3. Under **Tax Code Settings**, place a checkmark in the **Use tax codes** box.
4. Click **Save**.

### Set the Tax Type

1. Navigate to the Company level **Admin** tool.
2. Under **Tool Settings**, click **Tax Codes**.
3. Under **Tax Type**, click **Add a New Type** and enter the following information:

   - **Name**. Enter the name of the tax type. For example, enter GST (for Goods & Services Tax) or VAT (for Value-Added Tax). After you click Save, the name you enter here is updated on the [Tax Type] in the **Tax Codes** section of this page.
   - **Description**. Enter a descriptive name for the tax type. Typically, the name of the tax type will be abbreviated, so the description field lets you provide more information about the tax type. For example, enter Goods & Services Tax or Value-Added Tax.
4. Click **Add a New Type**.
5. If you want to delete the tax type, click the delete icon next to the tax type line item.

### Add a Tax Code

1. Navigate to the Company level **Admin** tool.
2. Under **Tool Settings**, click **Tax Codes**.
3. Under **Tax Codes**, click **Add a New Code** and add details as follows:

   - **Code**. Enter the name of the tax code in the box. Type the name as you want it to appear in the 'Tax Code' field in the Change Orders, Commitments, and Prime Contract tools.
   - **Description**. Enter a brief description of the tax code. Typically, the name of the tax code is abbreviated, so use this field to provide more detail for end users about the tax code.
   - **[Tax Type Name]**. The name of this field matches the name you assigned to the tax type. Enter a number in this field, which will be the percentage rate used for this tax code.
4. Click **Add** next to the line item to save the tax code.
5. *Optional:* To select a default tax code, toggle the switch under the 'Default' column next to the tax code in the list to the 'On' position. This tax code will be selected by default in the Tax Code field on prime contracts, commitments, and change orders.
6. If you want to archive a tax code, click the delete icon next to the tax code line item. You cannot archive tax codes that are currently assigned to a contract or change order line item.