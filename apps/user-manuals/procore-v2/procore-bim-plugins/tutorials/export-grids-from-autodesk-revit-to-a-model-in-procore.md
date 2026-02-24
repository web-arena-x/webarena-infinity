# Export Grids from AutodeskÂ® RevitÂ® to a Model in Procore

Source: https://v2.support.procore.com/product-manuals/procore-bim-plugins/tutorials/export-grids-from-autodesk-revit-to-a-model-in-procore

---

## Background

Use the Procore BIM Plugin to export grid lines from your AutodeskÂ® RevitÂ® model. These grids help mobile users orient themselves within the model by displaying it correctly in the 2D View of the Models tool on the Procore for Mobile app.

## Things to Consider

- **Required User Permissions**:

  - 'Admin' level permissions on the Models tool.
- **Additional Information**:

  - To export grids, your WindowsÂ® computer must be running a supported version of AutodeskÂ® RevitÂ®. See

    The **Procore BIM Plugin** integrate with **Show/Hide Details**

    ##### Support Lifecycle Policy

    Procore aligns its support lifecycle with Autodeskâs active versioning to ensure the best possible experience. While its plugins may function on older versions (e.g., 2019), official support is categorized as follows:

    - **Active Support (Versions 2022â2026)** Procore offers comprehensive support for these versions, covering everything from plugin-specific inquiries to fixes for underlying AutodeskÂ® dependencies.
    - **Limited Support (Versions 2020â2021)** Procore provides support for issues specific to the Procore BIM plugin, but cannot address stability issues caused by the AutodeskÂ® platform itself.

    #### Supported Applications

    *Compatible with versions 2020â2026 unless otherwise noted.*

    - **AutodeskÂ® NavisworksÂ®**

      - Manage
      - Simulate
    - **AutodeskÂ® RevitÂ®**
    - **AutodeskÂ® CivilÂ®**
    - **AutodeskÂ® AutoCADÂ® Specialized Toolsets**:

      - AutoCADÂ®
      - Architecture
      - Electrical
      - Map 3D
      - Mechanical
      - MEP
      - Plant 3D
      - OEM
    - **AutodeskÂ® InventorÂ®**

      - Professional
  - To prevent misalignment in the 2D View, the Coordinate System selected in the Procore BIM Plugin during the export must match the coordinate system used when the 3D model was published to Procore. See [Why aren't my grids aligned in the Models tool?](#answer)

## Steps

1. Open the RevitÂ® model that contains the grid line you want to export. Typically, this is an *Architectural* or *Structural* model.
2. In RevitÂ®, click the **Procore** tab to use the Procore BIM Plugin.
3. In the ribbon, click **Export Grids**.
4. In the **Export Grids** page:

   - Confirm that the Procore Company and Project are correct.
   - Under **Coordinate System**, select *Internal* or *Shared*.

     ##### Important

     To prevent misalignment in the 2D View, the Coordinate System selected in the Procore BIM Plugin during the export must match the coordinate system used when the 3D model was published to Procore. See [Why aren't my grids aligned in the Models tool?](#answer)

- Under **Export To:**

  - Find the correct **Model Name.**
  - Click **Add Grids**.

When successful, a checkmark and an Added message appears where the button once did.