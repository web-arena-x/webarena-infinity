# Add Items to a Cost Catalog

Source: https://v2.support.procore.com/product-manuals/cost-catalog-company/tutorials/add-items-to-a-cost-catalog

---

## Background

The Cost Catalog tool in Procore is where all material information and values, ranging from individual parts to assembled items, are stored. Procore offers a gallery of predefined materials that you can use, and you can also add and customize parts or assembly. Materials in the catalog can be quickly accessed during takeoff. When adding items to the Cost Catalog in Procore, you can also choose to create a new *catalog* or *group* to organize items under. See [What is the difference between a catalog, group, and item in the Cost Catalog?](/faq-what-is-the-difference-between-a-catalog-group-and-item-in-the-cost-catalog-for-estimating) for more information.

## Things to Consider

- [Required User Permissions](/product-manuals/cost-catalog-company/permissions)
- When you create a catalog item in Procore Estimating, the *catalog item type* acts as a *cost type*.

 - If you already have cost types added in Procore (in the Company level Admin tool), these cost types will be available to select in the 'Cost Type' field when creating or editing a catalog item.
 - You can also create new custom cost types to in the 'Custom Type' field when creating or editing a catalog item.
- If your company is integrated with ERP, you can add cost codes from your ERP system

## Steps

1. Navigate to the **Cost Catalog** tool in Procore.
2. Select the catalog that you want to add an item to. 
   *Note:*

   - If you want to add a new *catalog* to add the item to, see [Add a New Catalog to the Cost Catalog](/product-manuals/cost-catalog-company/tutorials/add-a-new-catalog-to-the-cost-catalog).
   - If you want to add a new *group* to add the item to, see [Add a Group to the Cost Catalog](/product-manuals/cost-catalog-company/tutorials/add-a-group-to-the-cost-catalog).
3. Click **Add Catalog Item**.
4. In the Create New Catalog Item window, select the type of item you want to add in the **Catalog Item Type** drop-down menu:

   - **Part**
   - **Assembly***Note:* If you are creating an assembly item, see [Create Assemblies for a Cost Catalog](/product-manuals/cost-catalog-company/tutorials/create-assemblies-for-a-cost-catalog).
   - **Custom**
   - **Equipment**
   - **Subcontractor**
   - **Travel**
   - **Labor**
5. Choose an item from the **Cost Catalog to include this item to** dropdown menu.

   - Assign **Masterformat to include this item to** as needed.
   - Assign **Uniformat to include this item to** as needed. [What is the difference between Uniformat and Masterformat?](/faq-what-is-the-difference-between-uniformat-and-masterformat)
6. Enter the catalog name (required).
7. Complete the remainder of the fields as necessary. 
   *Note:* The fields that are shown are specific to the catalog item type that you selected.
8. To add an attachment, select **+ Add PDF.** *Note:* The attachment field is only a placeholder for files. Attachments do NOT carry over to the proposal.
9. Click **Save**.