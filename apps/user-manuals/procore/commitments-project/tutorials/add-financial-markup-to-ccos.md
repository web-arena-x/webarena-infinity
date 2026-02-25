# Add Financial Markup to Commitment Change Orders

Source: https://v2.support.procore.com/product-manuals/commitments-project/tutorials/add-financial-markup-to-ccos

---

## Background

To learn about markup, see [What is the difference between horizontal and vertical financial markup?](/faq-what-is-the-difference-between-horizontal-and-vertical-markup)

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the project's Commitments tool.
- **Additional Information:**

 - Financial markup is distributed proportionally on each line item in a change order's [Schedule of Values](/glossary-of-terms) (SOV).
 - Financial markup is applied to the cost codes and categories on those SOV lines in the budget.
 - Horizontal markup is included in the SOV's subtotal and is included in the vertical calculation when the markups are used in conjunction.
- **Limitations:**

 - After you apply financial markup to a commitment change order, the change order cannot be added to a [subcontractor invoice](/glossary-of-terms).

## Prerequisites

- [Enable Financial Markup on a Commitment](/product-manuals/commitments-project/tutorials/enable-financial-markup-on-a-commitment)

## Steps

1. Navigate to your project's **Commitments** tool.
2. Click the **Contracts** tab.
3. Locate the purchase order or subcontract to work with. Then click its **Number** link to open it.
4. Click **Financial Markup**.

   ##### Â Notes

   - If the 'Financial Markup' tab is NOT visible, check the **More** menu to see if it is listed.
   - If 'Financial Markup' is not available in the **More** menu, the feature is likely disabled on your project. To learn more, see [Enable Financial Markup on a Commitment](/product-manuals/commitments-project/tutorials/enable-financial-markup-on-a-commitment).

- Under **Financial Markup Settings**, you have these options:
- **Add Horizontal Markup**. Click this button to display the markup in the same row as the line items.
- **Add Vertical Markup**. Click this button to display the markup below the line items.

 ##### Â Notes

 - To learn about the differences between markup types, see [What is the difference between horizontal and vertical financial markup?](/faq-what-is-the-difference-between-horizontal-and-vertical-markup)
 - You can apply financial markup settings on a per-change order basis.

This opens a page when you can then create your markup.

Enter information in the **Add Horizontal Markup** or **Add Vertical Markup** window as follows:

- **Markup Name**. Enter a name for the financial markup.
- **Markup Percentage**. Enter the percentage for the markup.
- **Calculation Type**. Select the calculation type for the financial markup you are creating.

 - **Basic Calculation**. Percentage is multiplied by the line items that meet the application criteria.
 - **Compounds all Above**. Percentage is multiplied by the line items that meet the application criteria and all the markups above in the markup table.
 - **Selective Compounding**. Percentage is multiplied by the line items that meet the application criteria and any individually selected markups. Once you choose 'Selective Compounding', you will select which of the existing financial markups to include in the calculation.
 - **Iterative Calculation (Margin)**. Percentage is multiplied by the line item total, including all markups.
- **Application Criteria**. These conditions determine how the markup will apply to your change orders and change events.

 - **Apply to all line items**. Financial markup will apply to each line item on a Prime Contract Change Order.
 - **Apply to specific line items**. Financial markup will apply only to specific line items on a Prime Contract Change Order or Potential Change Order. Markup estimates on change events will also only apply to the selected line items. You will be given the following options to determine which line items the markup will apply.\* **Segment**. Choose between 'Cost Code' or 'Cost Type'.\* **Conditional Logic**. Choose between 'Includes' or 'Excludes'\* **Values**. If 'Cost Code' is selected, click **Select Values** to choose which cost codes will apply towards the financial markup. If 'Cost Type' is selected, choose one or more cost types from the drop-down menu.
- Under 'Applies To' in the **Cost Types** box, all available cost types are listed by default. See [What are Procore's default cost types?](/faq-what-are-procores-default-cost-types) and [Add Company Cost Types](/process-guides/company-administration-work-breakdown-structure-guide/add-company-cost-types). To remove one or more cost types, click the 'x' next to the desired selections.
- Click **Save**.