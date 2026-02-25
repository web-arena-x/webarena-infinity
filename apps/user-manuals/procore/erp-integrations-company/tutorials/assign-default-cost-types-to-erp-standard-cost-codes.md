# Assign Default Cost Types To ERP Standard Cost Codes

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/assign-default-cost-types-to-erp-standard-cost-codes

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

In the construction industry, *cost types* are often assigned to cost codes to identify the specific work being performed on a construction project. To help project teams better account for their costs (especially their internal costs), it is a common practice to assign multiple cost types to a single cost code.

To understand the relationship between these two objects, keep in mind:

- A *Cost Code* is a code that defines the specific type of work being completed on a construction project. When using an 

 In Procore, the term *integrated ERP System*, is used to refer to *Enterprise Resource Planning (ERP)* software applications that can be configured to exchange data between Procore and a supported application using the Company level ERP Integrations tool. See [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

 Integrated ERP System with Procore, cost codes are synced to individual segment items (a.k.a., 'cost codes' on Procore's 'Cost Code' segment, which is a tiered segment. To learn more, see [What are Procore's default cost codes?](/faq-what-are-procores-default-cost-codes)
- A *Cost Type* is a set of costs identified by a unique abbreviation or label. In Procore's WBS, 'Cost Type' is a flat segment with these default options: *(E) Equipment, (L) Labor, (M) Materials, (O) Other, (OC) Owner Cost, (S) Commitments,* and *(SVC) Professional Services.* See [What are Procore's default cost types?](/faq-what-are-procores-default-cost-types)

You must first add Cost Codes to the ERP standard cost codes list in the company Admin tool before assigning default cost types in the ERP Integrations tool.

## Things to Consider

- **Required User Permissions**:

 - 'Standard' or 'Admin' level permissions on the company's ERP Integrations tool.
- **Additional Information**:

 - You can assign one or more cost type(s) to each standard cost code. For example, both L=Labor and E=Equipment.
- **Not all integrations support the cost type concept.**

## Steps

1. Navigate to the company's **ERP Integrations** tool.
2. Click the **Std. Cost Codes & Cost Types** tab.
3. For each ERP standard cost code in your company's list, mark one (1) or more checkboxes to assign the code to one (1) or more cost types.

##### NOTE

- To apply a specific cost type to all of the cost codes in the list, double-click the desired cost type column.
- You can hover your mouse cursor over the column headings, to reveal a tooltip that shows the full name for the cost type.
- The cost type assignments are automatically saved.