# Add an ERP Company to the Procore Company Directory

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/add-an-erp-company-to-the-company-directory

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

Companies that exist in your ERP system can be added to the Procore Directory tool using the steps below. This process takes the company data from your ERP system and automatically creates a new company record in your company's Directory tool. It also creates a link between the two records.

***Important!*** Before using these steps to add a company, always check your company's Directory tool to ensure a matching record doesn't already exist.

## Things to Consider

- **Required User Permissions**:

 - 'Standard' or 'Admin' on the company's ERP Integrations tool.
- **Additional Information:**

 - Companies in an ERP system must be marked 'Active' to appear on the 'Companies Only in ERPâ page. Companies marked 'Inactive' or 'Not Used' will not be imported.
 - If a company that has an 'Active' status in an ERP system is changed to 'Inactive' or 'Not Used' after it has already been listed on the 'Companies Only in ERPâ page, refreshing the company list will not remove it from this page. To remove the company from this list, you must archive it in Procore. For details, see [Archive an ERP Company in Procore](/product-manuals/erp-integrations-company/tutorials/archive-an-erp-company-in-procore).

## Steps

1. Navigate to the company's **ERP Integrations** tool.
2. Click the **Companies** subtab.
3. In the 'Filters' menu, click **Ready to Import** link.
4. Review the list in the 'Company Only in ERP' page.
5. For each company in the list, check to see if there is a matching company record in Procore's Company Directory. Then choose from these options:

   - *If a match exists*, follow the steps in [Link an ERP Company to a Procore Company](/product-manuals/erp-integrations-company/tutorials/link-erp-companies-to-procore-companies). 
      OR
   - *If no match exists*, click the **Add to Procore** button.
6. Repeat the previous step for every company in the list.