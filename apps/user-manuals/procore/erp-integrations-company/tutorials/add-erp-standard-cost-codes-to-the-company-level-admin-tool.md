# Add ERP Standard Cost Codes to the Company Level Admin Tool

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/add-erp-standard-cost-codes-to-the-company-level-admin-tool

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

If you have added new cost codes to the 'ERP Standard Cost Codes' segment in the company's Admin tool, those codes will need to be synced with your integrated ERP system. The way in which new cost codes are synced with your ERP system will depend on which ERP integration you're using.

## Things to Consider

- **Required User Permissions**:

 - 'Admin' user permissions on the company's Admin tool.
- **Prerequisites**:

 - Prerequisites will vary depending on the ERP system your Procore account is integrated with.

## Steps

1. Navigate to the company's **Admin** tool.
2. Under **Company Settings**, click **Work Breakdown Structure**.
3. Under **Segments** select **Cost Code**.
4. Choose one of the following options:

   - If your company only has a **ERP Standard Cost Code** list, it appears in this page. Continue with the next step.
   - If your company has multiple cost code lists, locate the **ERP Standard Cost Code** list in the table and click **Edit**. *Notes*: The ERP Standard Cost Codes list shows all of the codes that are available for use on your company's ERP-integrated projects.
5. Perform one of the following options depending on the tier of cost code you would like to add. See [What is the difference between a flat and tiered segment in Procore's WBS?](/faq-what-is-the-difference-between-a-flat-and-tiered-segment-in-procores-wbs):

   - To add a Tier-1 cost code, select **Cost Code** at the top of the hierarchy tree, then click **Add Item** and fill in a name and/or description.
   - To add a Tier 2 cost code, select the Tier 1 cost code that it belongs to from the hierarchy tree, then click **Add Item** and fill in a name and/or description.