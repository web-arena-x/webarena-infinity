# Import Commitment SOV Line Items from a CSV File

Source: https://v2.support.procore.com/product-manuals/commitments-project/tutorials/import-commitment-sov-line-items-from-a-csv-file

---

## Background

To save time from manually adding line items to a commitment's SOV, you can download a CSV file from your project, add your line items to that file, and then import it into Procore.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the project's Commitments tool.   
     OR
 - 'Read Only' or 'Standard' level permissions on the project's Commitments tool with the ['Update Purchase Order Contract'](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) and '['Update Work Order Contract'](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) granular permissions enabled on your permission template.

## Prerequisites

- Before importing, it's important to know how the [Enable Always Editable Schedule of Values setting](/faq-what-is-the-enable-always-editable-schedule-of-values-setting) works:

 - **When this setting is OFF (Default).** The commitment must be in *Draft* status to import.
 - **When this setting is ON.** The commitment can be in any status to import. However, you cannot replace line items if they have been invoiced.
- To learn more about imports, see [What are the requirements for importing SOV Line items from CSV?](/faq-what-are-the-requirements-for-importing-sov-line-items-from-csv)
- **For companies using the** **ERP Integrations tool:** Prerequisites, requirements, limitations, and considerations might apply depending on the ERP system your Procore account is integrated with. Visit [Things to Know about your ERP Integration](https://support.procore.com/products/online/user-guide/company-level/erp-integrations/things-to-know-about-your-erp-integration) for details.

## Steps

### Download a CSV Template

Choose to delimit your CSV template with a comma or a semicolon before downloading it. You also have the option to download a blank CSV template or one with the selected commitment's existing line item data.

1. Navigate to the **Commitments** tool.
2. On the **Contracts** tab, click a **Number** link to open a commitment.
3. Under the **General** tab, click **Schedule of Values**.
4. In the **Schedule of Values** card, click **Edit**. 
   This places the SOV into edit mode.
5. Below the table, click **Import SOV from CSV**.   
   This opens the Import Schedule of Values from CSV window.
6. Expand **Customize CSV Delimiter**.
7. Choose a delimiter for the template file: *Comma* or *Semicolon*. 
   The system's default option is *Comma*.
8. Click **Download CSV Template** and choose: *Blank Template* or *Template with Existing Line Items*.   
   The downloads the selected template to your web browser's configured location.

### Add Line Items to a CSV Template

1. Open the downloaded template in a spreadsheet editor.
2. Enter the line item data using the appropriate accounting method for the commitment. See [How do I set the accounting method for a contract or funding?](/faq-how-do-i-set-the-accounting-method-for-a-contract-or-funding)

- How to enter data for amount-based accounting: **Show/Hide**

 - To import a subcontract using the amount-based accounting method, enter data as follows:
 - **Sub Job**. Enter a sub-job code for the line item. This only appears when sub-jobs are enabled. See [Enable Sub Jobs for WBS](/process-guides/company-administration-work-breakdown-structure-guide/enable-sub-jobs-for-projects) and [Which integrated ERP systems support the sub job concept?](https://support.procore.com/tc/procore/Legacy/ERP%5FArchives/Legacy%5FGeneral%5FERP%5FTutorials/Which%5Fintegrated%5FERP%5Fsystems%5Fsupport%5Fthe%5F'Sub%5FJob'%5Fconcept?)
 - **Cost Code**. Enter a cost code for the line item. To learn more, see [What are Procore's default cost codes?](/faq-what-are-procores-default-cost-codes)
 - **Cost Type**. Enter a cost type for the line item. See [What are Procore's default cost types?](/faq-what-are-procores-default-cost-types)

    ##### Â Important Information about Cost Types

    - If you leave this cell blank, Procore classifies it as *Other*.
    - This list might be customized for your company. See [Add Company Cost Types](/process-guides/company-administration-work-breakdown-structure-guide/add-company-cost-types) or ask your [Company Admin](/faq-what-is-a-company-admin) for a list of valid cost types.
    - Data entry is required if your integrated ERP system syncs data with Procore. See [Which integrated ERP systems support the 'Cost Type' concept?](/faq-which-integrated-erp-systems-support-the-category-concept)

 - **Description**. Enter a statement to describe the line item.
 - **Tax Code**. Enter the tax code for the line item.

    ##### Â Important Information About Tax Codes

    - This list might be customized for your company. See [Configure Tax Code Settings](/product-manuals/admin-company/tutorials/configure-tax-code-settings) or ask your [Company Admin](/faq-what-is-a-company-admin) for a list of valid tax codes.
- **Amount**. Enter a numeric amount without commas or the dollar sign (e.g., 15000); enter '0.00' if there is no dollar amount, as blank cells are not accepted.

- How to enter data for unit/quantity-based accounting: **Show/Hide**

 - To import a purchase order using the amount-based accounting method, enter data as follows:
 - **Sub Job**. Enter a sub-job code for the line item. This only appears when sub-jobs are enabled. See [Enable Sub Jobs for WBS](/process-guides/company-administration-work-breakdown-structure-guide/enable-sub-jobs-for-projects) and [Which integrated ERP systems support the sub job concept?](https://support.procore.com/tc/procore/Legacy/ERP%5FArchives/Legacy%5FGeneral%5FERP%5FTutorials/Which%5Fintegrated%5FERP%5Fsystems%5Fsupport%5Fthe%5F'Sub%5FJob'%5Fconcept?)
 - **Cost Code**. Enter a cost code for the line item. To learn more, see [What are Procore's default cost codes?](/faq-what-are-procores-default-cost-codes)
 - **Cost Type**. Enter a cost type for the line item. See [What are Procore's default cost types?](/faq-what-are-procores-default-cost-types)

    ##### Â Important Information about Cost Types

    - If you leave this cell blank, Procore classifies it as *Other*.
    - This list might be customized for your company. See [Add Company Cost Types](/process-guides/company-administration-work-breakdown-structure-guide/add-company-cost-types).
    - Data entry is required if your integrated ERP system syncs data with Procore. See [Which integrated ERP systems support the 'Cost Type' concept?](/faq-which-integrated-erp-systems-support-the-category-concept)

 - **Description**. Enter a statement to describe the line item.
 - **Quantity**. Enter a numeric value representing the quantity of the unit.
 - **UOM**. Enter a UOM abbreviation. See [Which units of measure are included on Procore's master list?](/faq-which-units-of-measure-are-included-in-procores-master-list)
 - **Unit Price**. Enter the unit price for the line item.
 - **Subtotal**. Enter the subtotal for the line item.
 - **Override**. You have these options, choose one (1) option:

    - To override the automatic subtotal calculation, enter a value here and leave the **Quantity**, **Unit Description**, and **Unit Price** fields blank. 
       OR
    - To use Procore's automatic calculation, enter values in the **Quantity**, **Unit Description**, and **Unit Price** fields, leaving the **Override** field blank.

      ##### Â Important information about automatic calculation

      - If your integrated ERP system syncs data with Procore, data entry in the **Quantity**, **Unit Description**, and **Unit Price** fields is required. See [Which integrated ERP systems support the 'Cost Type' concept?](/faq-which-integrated-erp-systems-support-the-category-concept)
- **Tax Code**. Enter the tax code for the line item. See [Configure Tax Code Settings](/product-manuals/admin-company/tutorials/configure-tax-code-settings).
- **Amount**. Enter a numeric amount without commas or the dollar sign (e.g., 15000); enter '0.00' if there is no dollar amount, as blank cells are not accepted.