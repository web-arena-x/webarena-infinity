# Add Adjustments to an Estimate

Source: https://v2.support.procore.com/product-manuals/estimating-project/tutorials/add-adjustments-to-an-estimate

---

## Background

You can add adjustments to your estimates by creating your own calculations for different pre and post-tax markups. Currently these adjustments are shown in the proposal, without an option to hide them.

##### Example

You want to tax the cost of materials only (not including profit) at 5%, you would create a **pre-tax** mark up with the following settings:

- **Type**: Basic Calculation
- **Percent**: 5
- **Application Criteria**: Cost Type Includes Materials

You want to add 10% margin for the total final cost of the estimate, you would create a **post-tax** mark up with the following settings:

- **Type**: Iterative Calculation Margin
- **Percent**: 10

Things to Consider

- [Required User Permissions](/product-manuals/bid-board-company/permissions) for the **Bid Board** tool.
- [Required User Permissions](/product-manuals/estimating-project/permissions) for the **Estimating** tool.
- [Required User Permissions](/product-manuals/portfolio-planning-company/permissions) for the **Portfolio Planning** tool.
- Currently adjustments are shown in the proposal, without an option to hide them.
- Only pre-tax adjustments can have taxes applied to the markup.

## Steps

- Pre-Tax Markups
- Post-Tax Markups

### Pre-Tax Markups

1. Navigate to the **Bid Board** or **Portfolio Planning** tool and select the **project**. 
    OR Navigate to the project's **Estimating** tool and click the **Estimating** tab.
2. Click the **add** icon for 'Pre-tax Markups' in the 'Summary' section.
3. Enter the name of the markup.
4. Select the type of mark up.

   - **Lump Sum**
   - **Basic Calculation**
   - **Selective Compounding**
   - **Compounds All Above** *Note:* You can decide which existing markups are compounded from by clicking and holding the **reorder** icon next to the existing mark up. Drag the existing mark up above this mark up to include it, or below to exclude from this mark up's calculation.
   - **Legacy Discount** *Note:* If available, the calculation is: (Total Sales + Overhead $) x -Discount %.
   - **Legacy Overhead** *Note:* If available, the calculation is: Overhead % x Total Sales, and is taxed based on the labor tax rate.
5. Enter the **amount** or **percent** for the markup.
6. If you selected 'Selective Compounding', select the **markup** you want the current mark up to compound from.
7. For 'Cost Category', select how the markup should be taxed and summarized. 
   *Note:* If you select 'All Categories,' tax rates are applied to the related cost types in the estimate. For example, the 'Labor Tax' rate is applied to all labor costs, and the 'Materials Tax' rate is applied to all materials costs.
8. Select the application criteria.

   - Select **Applies to Entire Estimate** to apply the markup to the entire estimate.
   - Select **Apply to Specific Selections** to apply the mark up to specific segments of your estimate.

     1. Select the **segment**.

        - **Cost Code**
        - **Cost Type**
        - **Catalog Item Type**
        - **Group or Layer**
        - **Sub Job**
        - **Tag**
     2. Select whether to **Include** or **Exclude** selected values for the segment.
     3. Select the **values** to which the mark up should be applied to, or excluded from.
     4. Click **Add.**
     5. Repeat steps a-c to create additional conditions to apply your mark up.
9. Under 'Budget Mapping', select the **cost code** for the estimate's markup in your budget.
10. Click **Create**.

##### Â Tip

After you have added an adjustment, you can make the following changes by clicking the **vertical ellipsis** for the adjustment.

- Select **Copy** to copy the adjustment.
- Select **Edit** to edit the adjustment.
- Select **Delete** to delete the adjustment.

### Post-Tax Markups

1. Navigate to the **Bid Board** or **Portfolio Planning** tool and select the **project**. 
    OR Navigate to the project's **Estimating** tool and click the **Estimating** tab.
2. Click the **add** icon for 'Post-tax Markups' in the 'Summary' section.
3. Enter the name of the markup.
4. Select the type of mark up.

   - **Lump Sum**
   - **Basic Calculation**
   - **Selective Compounding**
   - **Compounds All Above** *Note:* You can decide which existing markups are compounded by clicking and holding the **reorder** icon next to the existing mark up. Drag the existing mark up above this mark up to include it, or below to exclude from this mark up's calculation.
   - **Iterative Calculation Margin** *Note:* You can only create this adjustment type once per estimate.
5. Add the **amount** or **percent** for the markup.
6. If you selected 'Selective Compounding', select the **markup** you want the current mark up to compound from.
7. *Optional:* For 'Cost Category', select the **cost category** to see the mark up in summaries and reporting.
8. If available, select the application criteria.

   - Select **Applies to Entire Estimate** to apply the markup to the entire estimate.
   - Select **Apply to Specific Selections** to apply the mark up to specific segments of your estimate.

     1. Select the **segment**.

        - **Cost Code**
        - **Cost Type**
        - **Catalog Item Type**
        - **Group or Layer**
        - **Sub Job**
        - **Tag**
     2. Select whether to **Include** or **Exclude** selected values for the segment.
     3. Select the **values** to which the mark up should be applied to, or excluded from.
     4. Click **Add.**
     5. Repeat steps a-c to create additional conditions to apply your mark up.
9. Under 'Budget Mapping', select the **cost code** for the estimate's markup in your budget.
10. Click **Create.**