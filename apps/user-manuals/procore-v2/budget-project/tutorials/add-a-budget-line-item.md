# Add a Budget Line Item

Source: https://v2.support.procore.com/product-manuals/budget-project/tutorials/add-a-budget-line-item

---

## Background

A *budget line item* is a row in a data table that represents a project expenditure by cost code and cost type. If you want to perform job costing on your project, you can also present your project expenditures by sub job. Depending on your specific project, a budget can have hundreds or even thousands of line items on it. After creating a new Procore project, setting up a budget can be accomplished by adding budget line items to the project's Budget tool. To do this, you use the steps below to manually add each line item to your budget. Alternatively, you can import line items in bulk using the steps in [Import a Budget](/process-guides/resource-tracking-and-project-financials-setup-guide/import-a-budget).

## Things to Consider

- **Required User Permissions:**

 - *To add a new line item to a budget*, 'Standard' level permissions or higher assigned to you on the 'Permissions Table' in the project's Budget tool. *Note*: If 'Standard' permission was assigned using a permission template, the ['Modify Original Budget Amount' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) must be enabled on your permissions template. If the granular permission is NOT enabled, line items can only be created with no value. 
     OR
 - *To edit the original budget amount:*\* 'Admin' level permissions on the project's Budget tool. 
     OR\* 'Read Only' or 'Standard' level permissions on the project's Budget tool with the ['Modify Original Budget Amount' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permissions template.
- **Additional Information:**

 - As an alternative to manual data entry, you can also follow the steps in [Import a Budget](/process-guides/resource-tracking-and-project-financials-setup-guide/import-a-budget).
 - Each line item added to the budget must have a unique budget code. You cannot add two line items that use the same budget code. See [What is a budget code in Procore's WBS?](/faq-what-is-a-budget-code-in-procores-wbs)
- For companies using the ERP Integrations tool: **Show/Hide**

 - If your company is using Procore with an integrated ERP system, see your integration's Things to Know page for additional details.

## Prerequisites

Your company's 

A *Procore Administrator* is a user who has 'Admin' level permissions on all of the Company level Tools in Procore. Granting a user âAdminâ level permissions in the Company level Directory tool automatically assigns that user âAdminâ permissions on all Company level tools. Also called a *Company Administrator*.

ProcoreÂ Administrator must complete these steps:

- Add the Budget tool to the project. See [Add](/product-manuals/admin-project/tutorials/add-and-remove-project-tools) [and Remove Project Tools](/product-manuals/admin-project/tutorials/add-and-remove-project-tools).
- Complete the steps in [Create Your Company's Default Work Breakdown Structure](/product-manuals/admin-company/tutorials/create-your-companys-default-work-breakdown-structure).
- *(Optional)* Complete the steps in [Create Your Project's Work Breakdown Structure](/process-guides/resource-tracking-and-unit-quantity-based-budget-setup-guide/create-your-projects-wbs).

## Steps

1. Navigate to the project's **Budget** tool.
2. In the **Budget** tab, click the **Create** button and choose **Budget Line Item** from the drop-down list.
3. Add your line item in the data entry area as follows:

   ##### Â Note

   Procore's [Work Breakdown Structure](/product-manuals/work-breakdown-structure/) includes two (2) default segments (

   A *Cost Code* identifies a specific type of work on a project to track its associated expenses, such as labor, materials, and equipment.

   Cost Code and 

   A *Cost Type* is a set of costs identified by a unique abbreviation or label. Cost types are typically used in job costing (tracking costs for certain job activities and projects). In Procore's Work Breakdown Structure, 'Cost Type' is a flat segment with these default options: *(E) Equipment, (L) Labor, (M) Materials, (O) Other, (OC) Owner Cost, (S) Commitments,* and *(SVC) Professional Services.*

   Cost Type) and one (1) optional segment (

   In Procore, a *sub job* allows you to compartmentalize job costs within a project. Once they are added to Procore (or imported via an 

   In Procore, the term *integrated ERP System*, is used to refer to *Enterprise Resource Planning (ERP)* software applications that can be configured to exchange data between Procore and a supported application using the Company level ERP Integrations tool. See [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

   Integrated ERP System) you can monitor your project budgets and costs against them to help you better determine if you are making money on your project. For example, if your project is a multi-story commercial building, you might create a separate sub job for the build of each floor. Or, if your project is a multi-unit development, you might create a separate sub job for each individual structure.

   Sub Job). To learn more, see [What are segments and segment items?](/faq-what-are-segments-and-segment-items)

- **Cost Code**. Select a cost code from the drop-down list.
- **Cost Type**. Select a cost type from the drop-down list.
- **Calculation Method**. Choose the option button that corresponds to the desired calculation method for the line item:

 - **Calculate Subtotal Automatically**. Choose this option if you want the system to automatically calculate the *Original Budget* amount based on your *Unit Quantity*, *UOM*, and *Unit Cost* entries.   
     OR
 - **Override Subtotal Manually**. Choose this option if you want to manually enter the Original Budget amount, which overrides the system's automatic calculation.
- **Unit Qty**. Enter a numeric value in this box to indicate the number of units that correspond to the unit of measurement that you specify.
- **Unit of Measure (UOM)**. Select a unit of measure from the drop-down list. To learn about the default selections in this list, see [Which units of measure are included in Procore's master list?](/faq-which-units-of-measure-are-included-in-procores-master-list) and [Add a Unit of Measure to the Unit of Measure Master List](/product-manuals/admin-company/tutorials/update-a-unit-of-measure-on-the-unit-of-measure-master-list).
- **Unit Cost**. Enter the monetary cost in this box to indicate the cost per unit of measurement.
- **Original Budget**. Enter the total amount for the new line item. Do not enter commas and/or currency symbols in this field.

- Click **Add**.
- Repeat the steps above until all of your project's budget line items have been added.