# Add 3D Model Takeoffs Using Auto-Mapping

Source: https://v2.support.procore.com/product-manuals/estimating-project/tutorials/add-3d-model-takeoff-using-automapping

---

## Background

A takeoff extracts quantities from a drawing or model and associates with items in your cost catalog to create estimates. Using the Takeoffs tab in Procore's Estimating tool, can add and manage a wide variety of takeoffs for different trades. As you might have both drawings and models on a project, you can use a combination of takeoffs from 2D drawings and 3D models to create estimates. This documentation shows the steps to perform takeoffs from 3D models.

The auto-mapping functionality auto-detects materials used in 3D models and connects them to materials and assemblies in your cost catalog, to quickly create multiple takeoffs at once.

## Things to Consider

- [Required User Permissions](/product-manuals/estimating-project/permissions)
- The following quantities are available for 3D takeoffs at this time: Count, Linear, Area, and Volume.
- You cannot change the unit of measure when using auto-count.
- 3D takeoffs have a **model** icon next to them in the 'Takeoffs' list.
- You can use assemblies to create more detailed estimates from the model. See [Create Assemblies for a Cost Catalog](/product-manuals/cost-catalog-company/tutorials/create-assemblies-for-a-cost-catalog).

## Prerequisites

- Your organization must have the Procore BIM product, since this feature uses the model viewer from the Models tool.
- RevitÂ® files must exist in the project's Documents tool. See [Upload Files or Folders to the Project Level Documents Tool](/product-manuals/documents-project/tutorials/upload-files-or-folders-to-the-project-level-documents-tool).

## Steps

1. Navigate to the project's **Estimating** tool. 
   *Note:* The Estimating tool automatically opens to the Takeoff page.
2. Click the **drawing** drop-down menu.
3. Click the **Models** tab and select the model you want to add takeoff for. 
   *Note:* This pulls model files from the project's Documents tool. See [Upload Files or Folders to the Project Level Documents Tool](/product-manuals/documents-project/tutorials/upload-files-or-folders-to-the-project-level-documents-tool).
4. Mark the checkboxes for the model objects you want to auto-map and create takeoffs for.
5. Click **Auto-Map Selected Materials**.
6. Select how to map item to your cost catalog.

   1. To auto map the objects to items in your cost catalog, move the **Model Objects Maps to Catalog Items** toggle to the **ON** position.

      - Click the **replace item** **icon** to replace the item with another item in your cost catalog
      - Click the **warning** **icon** to see model objects without a cost catalog item. Click **Browse Catalog** to select an item or add a new one.
   2. To manually select the cost catalog items, move the **Model Objects Maps to Catalog Items** toggle to the **OFF** position.

      - Next to the item, click **Browse Catalog**.
      - Select the item in your cost catalog, then click **Select**.
7. Click **Create Takeoffs** to create takeoffs for each model object type.