# Add Financial Markup to Prime Contract Change Orders (Beta)

Source: https://v2.support.procore.com/product-manuals/prime-contracts-project/tutorials/beta-add-financial-markup-to-prime-contract-change-orders

---

## Background

In Procore, the term *financial markup* is used to refer to an increase that is applied to the cost of a product or service in order to arrive at its final cost. You can set two types of markup on change order line items.

1. **Horizontal Markup**. A *horizontal markup* calculates the markup amount on an individual line item.
2. **Vertical Markup**. A *vertical markup* calculates the markup amount as a subtotal on all of the line items on a change order.

In addition, you can associate your financial markup settings to cost codes, categories, and sub-jobs. This ensures that the financial markup on your project's change orders is reflected accurately on your project's budget.

## Things to Consider

- **Required User Permissions:**

  - *To add financial markup*, 'Admin' level permissions on the project's Prime Contracts tool.
  - *To view financial markup on the change order's Schedule of Values (SOV)*, 'Standard' level permission on both the project's Change Orders and Prime Contracts tools.
- **Additional Information:**

  - If you do NOT select a cost code or cost type for the financial markup to map to, it will appear on the project's budget as:\* Budget Code = None
- For companies using the  ERP Integrations tool: **Show/Hide**

  - Some ERP integrations do NOT support the sync of horizontal markups, vertical markups, or both. See [Things to Know About your ERP Integration](https://support.procore.com/products/online/user-guide/company-level/erp-integrations/things-to-know-about-your-erp-integration) for details.

## Steps

1. Navigate to the project's **Prime Contracts** tool.
2. Locate the prime contract to work with. Then click its **Number** link.
3. Click **Financial Markup**.

   ##### Â Note

   This tab is only available if it has been enabled in the appropriate tool's Advanced Settings tab.

- Under **Financial Markup Settings**, you have these options:

  - **Add Horizontal Markup**. Click this button to display the markup in the same row as the line items.
  - **Add Vertical Markup**. Click this button to display the markup below the line items.

    ##### Â Notes

    - To learn about the differences between markup types, see [What is the difference between horizontal and vertical financial markup?](/faq-what-is-the-difference-between-horizontal-and-vertical-markup)
    - You can apply financial markup settings on a per-change order basis.

This opens a page when you can then create your markup.- Enter information in the **Markup List** as follows:

  - **Markup Name**. Enter a name for the financial markup.
  - **Maps To**. Select the budget code that the markup percentage will be applied to on your project's budget.
  - **Markup Percentage**. Enter the percentage for the markup.
  - **Calculation Type**. Select the calculation type for the financial markup you are creating.

    - **Basic Calculation**. Percentage is multiplied by the line items that meet the application criteria.
    - **Compounds all Above**. Percentage is multiplied by the line items that meet the application criteria and all the markups above in the markup table.
    - **Selective Compounding**. Percentage is multiplied by the line items that meet the application criteria and any individually selected markups. Once you choose 'Selective Compounding', you will select which of the existing financial markups to include in the calculation.
    - **Iterative Calculation (Margin)**. Percentage is multiplied by the line item total, including all markups.
  - **Application Criteria**. These conditions determine how the markup will apply to your change orders and change events.

    - **Apply to all line items**. Financial markup will apply to each line item on a Prime Contract Change Order.
    - **Apply to specific line items**. Financial markup will apply only to specific line items on a Prime Contract Change Order or Potential Change Order. Markup estimates on change events will also only apply to the selected line items. You will be given the following options to determine which line items the markup will apply.
    - **Segment**. Choose between 'Cost Code' or 'Cost Type'.
    - **Conditional Logic**. Choose between 'Includes' or 'Excludes'
    - **Values**. If 'Cost Code' is selected, click **Select Values** to choose which cost codes will apply towards the financial markup. If 'Cost Type' is selected, choose one or more cost types from the drop-down menu.
    - Click **And** to add additional application conditions.
- **For companies using the**    
  **ERP Integrations tool:**

  - **ERP Prime Contract Item**. Select the desired Schedule of Values (SOV) line item from the projectâs Prime Contract. This ensures that the estimated value (the SOV value without vertical markup) and the revenue value (the SOV value with vertical markup) are synced to the line item that you specify in the integrated ERP system.

    ##### Â Notes

    This field is only visible when:

    - Your company account has enabled the ERP Integrations tool.
    - The ERP Integrations tool is configured to use either the Integration by Procore or Sage 300 CREÂ®.
    - You are creating vertical markup on a prime contract change order.