# Configure Settings: Bid Board

Source: https://v2.support.procore.com/product-manuals/bid-board-company/tutorials/configure-settings-bid-board

---

## Background

You can configure the default profit accounting model, measurement system, currency symbol, cost codes, cost types, and cover pages to use in the Bid Board or Portfolio Planning tool across your projects.

## Things to Consider

- [Required User Permissions](/product-manuals/bid-board-company/permissions) for the **Bid Board** tool.
- [Required User Permissions](/product-manuals/portfolio-planning-company/permissions) for the **Portfolio Planning** tool.
- When saved, cost code and cost type settings are only applied to new projects.

## Steps

1. Navigate to the **Bid Board** or **Portfolio Planning** tool.
2. Click the **Configure Settings** icon.
3. See the sections below for details on the settings that you can configure for projects:

   - Estimating
   - Units
   - Cost Codes and Types
   - Cover Pages
   - Project Stages
   - Custom Fields
   - Estimate Views
4. When you are done making changes, click **Save**.

#### Estimating

- Select your accounting model and profit structure:

 - **Profit Margin**: Sales minus the cost of goods sold. See [What is the difference between markup and margin?](/faq-what-is-the-difference-between-markup-and-margin)

    - To use **Minimum Margin Profit**, click the **toggle** to the ON position.
    - Enter the '**Minimum Material Margin Percentage**' and '**Minimum Labor Margin Percentage**.

      ##### Â Note

      If a 'Minimum Margin Profit' is set, users creating estimates cannot set a markup or margin in an estimate that is **lower** than the value configured here, unless they have 'Admin' level permissions to the tool.

- **Profit Markup**: The amount by which the cost is increased on a product to arrive at the selling price. See [What is the difference between markup and margin?](/faq-what-is-the-difference-between-markup-and-margin)

 - To use **Minimum Markup Profit**, click the **toggle** to the ON position.

    - Enter the **Minimum Markup Margin Percentage** and **Minimum Labor Markup Percentage**

      ##### Â Note

      If a 'Minimum Markup Profit' is set, users creating estimates cannot set a markup or margin in an estimate that is **lower** than the value configured here, unless they have 'Admin' level permissions to the tool.

- **Unit Cost Pricing**: When using unit cost pricing for labor, labor is set at a flat rate. See [What is the difference between individual labor rates and unit cost pricing for labor?](/faq-what-is-the-difference-between-individual-labor-rates-and-unit-cost-pricing-for-labor)

 - If you want to enable **Unit Cost pricing** for labor, click the **toggle** to the ON position.

    ##### Â Note

    - When **Unit Cost Pricing** is enabled, labor is set at a flat rate. It calculates labor as Quantity x Labor Cost.
    - If disabled, labor is set as a **Labor Rate**. When using labor rates, you set the labor rate as the cost per hour/minute, and then indicate how many minutes or hours are needed. You can also include a 'difficulty' multiplier that indicates how many people are needed to perform the work.