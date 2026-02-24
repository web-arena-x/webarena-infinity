# Configure Dynamic Grouping on an Estimate

Source: https://v2.support.procore.com/product-manuals/estimating-project/tutorials/configure-dynamic-grouping-on-an-estimate

---

##### Â In Beta

This is feature is currently in beta for Procore customers.

## Background

The **Dynamic Grouping** feature in Procore's Estimating tool provides a powerful way to quickly reorganize and analyze your estimate data. This functionality helps estimators fine-tune and review estimates by providing a quick overview based on user defined criteria. Within Dynamic Grouping, you can also enable the **Split Assemblies** feature, which allows you to view the individual components of multiple assemblies within your estimate.

## Things to Consider

- [Required User Permissions](/product-manuals/bid-board-company/permissions) for the Bid Board tool.
- [Required User Permissions](/product-manuals/estimating-project/permissions) for the Estimating tool.
- [Required User Permissions](/product-manuals/portfolio-planning-company/permissions) for the Portfolio Planning tool.
- **Additional Information**:

 - The Dynamic Grouping filters come from 3 main sources:

    - Filters available by default: Budget Code, Taxable, Tag , Cost Catalog Item, Cost Code and Cost Type.
    - Custom fields from the **Cost Catalog** tool.
    - Custom Segment Items from the Project level WBS Budget Code Segments tab that are in the **Budget Code Structure**.

## Steps

1. Navigate to the **Bid Board** or **Portfolio Planning** tool and select the **project**. 
   OR Navigate to the project's **Estimating** tool.
2. Click the **Estimating** tab.
3. Click the **vertical ellipsis** on the Estimate.
4. Move the **toggle** for **Dynamic Grouping** to the **ON** position.
5. A drop down menu will appear next to the Configure Columns button.
6. Select the drop down menu and group your estimate by:

   - Budget Code
   - Taxable
   - Tab
   - Cost Catalog Item
   - Cost Code
   - Cost Type

     - In the **Cost Catalog** tool, add custom material properties to create more grouping options. See [Configure Settings: Cost Catalog](/product-manuals/cost-catalog-company/tutorials/configure-settings-cost-catalog).
     - In the Company level **Admin** tool, add *new* custom segment items to create more grouping options. See [Add Custom Segments](/product-manuals/admin-company/tutorials/add-custom-segments).

       - The new custom segment item is added to the project level WBS automatically. Then [Add Custom Segments to the Project Budget Code Structure](/product-manuals/admin-project/tutorials/add-custom-segments-to-the-project-budget-code-structure).
7. *Optional*: Drag the menu items to the desired position by clicking and holding the **grip icon (ââ)** next to the item name.
8. Click outside the menu to **save** your selection.
9. **Edit and make changes** as needed directly within the new, organized view.

#### Enable Split Assemblies

1. Navigate to the **Bid Board** or **Portfolio Planning** tool and select the **project**. 
   OR Navigate to the project's **Estimating** tool.
2. Click the **Estimating** tab.
3. Click the **vertical ellipsis** on the Estimate.
4. When Dynamic Grouping is turned on, the split assemblies item appears in the list.
5. Move the **toggle** for **Split Assemblies** to the **ON** position.