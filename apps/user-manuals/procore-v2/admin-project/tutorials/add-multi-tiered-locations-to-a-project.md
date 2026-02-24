# Add Locations to a Project

Source: https://v2.support.procore.com/product-manuals/admin-project/tutorials/add-multi-tiered-locations-to-a-project

---

## Background

Locations give you the ability to link different Procore items (RFIs, Submittals, and more) to specific locations on a job site. This helps project team members to identify the exact location on a job site where a defect was observed, where materials are to be installed, or where a project change order occurred.

You can manually create your locations hierarchy, import locations, or [generate your locations hierarchy from drawings](/product-manuals/admin-project/tutorials/generate-locations-from-drawings). In all cases, you can continue adding locations as your project changes.

## Things to Consider

- **Required User Permissions**:

 - You need one of the following:

    - 'Admin' on the project's Admin tool.
    - 'Read Only' or 'Standard' permissions on the project's Admin tool with the ['Manage Locations' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permission template.

## Prerequisites

Create your locations hierarchy in one of the following ways:

- [Generate Locations Hierarchy From Drawings](/product-manuals/admin-project/tutorials/generate-locations-from-drawings)
- [Manually Create Locations Hierarchy](/product-manuals/admin-project/tutorials/manually-create-tiered-locations)
- [Import Locations Using the Procore Plug-In for RevitÂ®](/product-manuals/admin-project/tutorials/import-locations-using-the-procore-plug-in-for-revit)
- [Perform a Multi-tiered Locations Import (Procore Imports)](/product-manuals/procore-imports/tutorials/import-locations-into-your-project-level-admin-tool-procore-imports)
- [Request a Multi-tiered Locations Import](/product-manuals/admin-project/tutorials/request-a-multi-tiered-locations-import)

## Steps

Take the following steps based on how your locations were created and which tool you are using:

- [Manually Created or Imported (Admin Tool)](#add-locations-to-manually-created-or-imported-locations)
- [Generated from Drawings (Admin Tool)](#add-locations-generated-from-drawings-from-the-admin-tool)
- [Generated from Drawings (Drawings Tool)](#add-locations-generated-from-drawings-from-the-drawings-tool)

## Add Locations to Manually Created or Imported Locations

1. Navigate to the project's **Admin** tool.
2. Under the 'Project Settings' menu, click **Locations**.
3. If you generated locations from drawings and want to manually add new locations, click **Edit Location Hierarchy** and select **Skip Drawings and Edit.**
4. Add a location as follows:

   - ***To add the first tier***, click **+Add 1st Tier**. Then type a name for the location (e.g., *Parking Lot A)* and click the checkmark or press ENTER (*Note*: If you make a mistake, you can alternatively click the RED 'x' to remove your entry).
   - ***To add a second tier***, click **+Add 2nd Tier**. Then type a name for the sub-location (e.g., *Level Three*).
   - ***To add a third tier***, click **+Add 3rd Tier**. Then type a name for the sub-location (e.g., *West*).
   - ***If you want to continue adding sub-locations***, click **+Add 4th Tier**, **+Add 5th Tier**, and so on. You can create an unlimited number of tiers.
5. *Optional:* Adjust Location Settings

   - **Only allow locations to be created in the location manager above.** If this box is checked, users can only create locations in the Location Manager, and are not allowed to create locations from other Procore tools within the project.
   - **Include Optional Code.** If this box is checked, a prefix containing a code will be added to all locations for use with the naming standard for Procore's Document Management tool. This code will only be visible in the Document Management tool. If you are not using the Document Management tool, do not mark this checkbox.

## Add Locations Generated from Drawings from the Admin Tool

##### Â Limited Release

This experience is available in **Australia, Canada, Ireland, United Kingdom, United States,** and **New Zealand**.

1. Navigate to the Project level **Admin** tool.
2. Under the 'Project Settings' menu, click **Locations.**
3. **C**lick **Edit Location Hierarchy**.
4. Do one of the following:

   - Select **Add Drawings** to generate locations for one (1) or more new drawings or revisions.
   - Select **Skip Drawings and Edit** to edit existing locations.
5. Proceed with the steps for your selection:

   - **Add Drawings**

     1. Mark the checkboxes next to the drawing(s) you want to submit for location extraction. 
        *Note: Each drawing can only have one revision selected for use with locations. Selecting a different revision of a drawing that has already been used to extract locations will replace the existing drawing with the selected revision and update the related locations.*
     2. Click **Submit for Extraction.***Note:* This can take several minutes. You can navigate away from this page and check back later to proceed with the next step.
     3. If prompted, click **Review Drawings.***Note:* This feature was built to extract locations for Architectural floor plans. If you want to create locations for different type of Drawing, keep the checkbox marked for the drawing, and Procore will generate a placeholder parent location for you to manually manage locations and boundaries.

        1. Clear the checkbox for drawings you wish to NOT extract locations.
        2. Click **Continue Location Extraction**.
        3. Once processing is complete, click **Review Locations** to review the suggested location hierarchy.
        4. When review is complete, click **Update Locations** to publish your updated location hierarchy.

           ##### Â Tip

           Locations must have a unique name under a parent location. To resolve duplicates, scroll down the list to the location with the warning icon. Assign each location under a common parent a unique name. If needed, delete any duplicate location. See [Edit Locations](/product-manuals/admin-project/tutorials/edit-multi-tiered-locations) and [Delete Locations](/product-manuals/admin-project/tutorials/delete-multi-tiered-locations).

- **Skip Drawings and Edit**

 - Select a location from the list to view the associated drawing, location boundaries, and heat map.
 - Add a location in one of the following ways: From the List:

    - Click the **vertical ellipsis**next to a location and select Add. Then click **Sub Location**. 
      *Note:* You cannot add boundaries around sub locations.
    - Enter the **name** of the location.
    - Click the **checkmark** to confirm.

      1. Drag and Drop.
      2. Click and hold the **add location**icon.
      3. Move the pin to the location on the drawing using a drag and drop operation.
      4. Enter the **name** of the location.
      5. Under 'Sub Location of', select the parent location from the drop-down menu.
      6. Click **Save**.