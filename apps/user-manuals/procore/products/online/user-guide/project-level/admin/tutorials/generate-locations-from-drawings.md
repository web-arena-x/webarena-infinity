# Generate Locations Hierarchy From Drawings - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/generate-locations-from-drawings

---

##### Limited Release

This experience is available in **Australia, Canada, Ireland, United Kingdom, United States,**and **New Zealand**.

## Objective

Use Procore's enhanced Locations feature to automatically generate locations hierarchy from your project's architectural drawings.

## Background

Locations give users the ability to link different Procore items (RFIs, Submittals, and more) to specific locations on a job site. This helps project team members to pinpoint the exact location on a job site where a defect was observed, where equipment will be installed, or where a project change order occurred.

Procore's Locations feature allows you to automatically generate this list from your project's Architectural drawings. Locations generated from drawings are most accurate when they meet the following criteria:

- The drawings are floor plans.
- The locations have four walls and each location/room is labeled within the boundary of the four walls.
 - If characters in the drawing are close to the location/room label, they may be added to the name of the location.
 - Multi-family plans may not be generated correctly if rooms are not labeled within suites/units. However, you can [move sub-locations to the correct parent](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/edit-multi-tiered-locations#Edit_Locations_Generated_from_Drawings "Edit Tiered Locations") after drawings are generated.

Additionally, when you generate locations from Drawings, you have access to a [heat map](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/view-locations-heat-map "View Locations Heat Map") to see what locations have items associated with them.

## Things to Consider

- ********Required User Permissions********:
 - 'Admin' level permissions on the project's Admin tool. 
    OR
 - 'Read Only' or 'Standard' level permissions with the 'Manage Locations' granular permission enabled on the project Admin tool. See [Grant Granular Permissions in a Permission Template](../../../company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#Admin "Grant Granular Permissions in a Permission Template").
 - Locations must be published to be visible to users with 'Read Only' or 'Standard' level permissions who do not also have the 'Manage Locations' granular permission. Draft locations are only visible to users with 'Admin' level permissions.
- ****Additional Information****:
 - If you initially [manually created your locations in the Admin tool](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/manually-create-tiered-locations "Manually Create Tiered Locations"), you would need to delete them to instead generate your locations from Drawings.
 - You can only generate locations from drawings where the drawing discipline is set to 'Architectural'. See [Configure Default Drawing Disciplines](https://support.procore.com/products/online/user-guide/project-level/drawings/tutorials/configure-default-drawing-disciplines "Configure Default Drawing Disciplines").
 - The colors next to the locations indicate the confidence level in creating the location from the drawing. Green indicates the highest level of confidence.
 - Tiers are named based on the following information:
    - Tier 0 is the name of the project.
    - Tier 1 is the drawing name.
    - Tier 2 is the location on the drawing.
- **Limitations**
 - This feature does not currently support projects that have a single drawing sheet that represents multiple floors on the project. If a project has typical floors, do NOT generate locations from drawings.

## Prerequisites

1. [Upload Drawings](https://support.procore.com/products/online/user-guide/project-level/drawings/tutorials/upload-drawings "Upload Drawings")
2. [Review Drawings](https://support.procore.com/products/online/user-guide/project-level/drawings/tutorials/review-and-confirm-drawings "Review and Confirm Drawings")
3. [Publish Drawings](https://support.procore.com/products/online/user-guide/project-level/drawings/tutorials/publish-drawings "Publish Drawings")

## Steps

- [Generate from the Admin Tool](#Generate_Locations_Hierarchy_from_the_Admin_Tool "Generate Locations Hierarchy From Drawings")
- [Generate from the Drawings Tool](#Generate_Locations_Hierarchy_from_the_Drawings_Tool "Generate Locations Hierarchy From Drawings")

### Generate Locations Hierarchy from the Admin Tool

1. Navigate to the project's **Admin** tool.
2. Under the 'Project Settings' menu, click **Locations.**
3. Click **Create Location Hierarchy**.
4. Select the drawings you want to use to create your list of locations.
5. Click **Submit for Extraction**. 
   A tile appears in the side menu panel to show the progress of your location extraction.
6. If prompted, click **Review Drawings.** *Note:* This feature was built to extract locations for Architectural floor plans. If you want to create locations for Architectural drawings without a floor plan, keep the checkbox marked for the drawing, and Procore will generate a placeholder parent location for you to manually manage locations and boundaries.
   1. Clear the checkbox for drawings you wish to NOT extract locations.
   2. Click **Continue Location Extraction**.
7. Once processing is complete, click **Review Locations.** Locations are listed alongside an image of the associated drawing. Check the boundaries shown in the overlay on top of your drawings. Modify the boundaries if needed by clicking the **vertical ellipsis** ![icon-ellipsis-vertical.png](https://support.procore.com/@api/deki/files/158014/icon-ellipsis-vertical.png?revision=2&size=bestfit&width=15&height=15) . Click **Edit**, and select **Boundary**. Click and drag the points around the boundary to reconfigure it.
   ![move-boundary.png](https://support.procore.com/@api/deki/files/484612/move-boundary.png?revision=2&size=bestfit&width=493&height=312)
8. After review, click **Save as Draft** or **Publish Locations**.

### Generate Locations Hierarchy from the Drawings Tool

1. Navigate to the project's **Drawings** tool.
2. Click **Create Locations**.
3. Select the drawings you want to use to create your list of locations.
4. Click **Submit for Extraction**. 
   A tile appears in the side menu panel to show the progress of your location extraction.
5. If prompted, click **Review Drawings.** *Note:* This feature was built to extract locations for Architectural floor plans. If you want to create locations for Architectural drawings without a floor plan, keep the checkbox marked for the drawing, and Procore will generate a placeholder parent location for you to manually manage locations and boundaries.
   1. Clear the checkbox for drawings you wish to NOT extract locations.
   2. Click **Continue Location Extraction**.
6. Once processing is complete, click **Review Locations.** Locations are listed alongside an image of the associated drawing. Check the boundaries shown in the overlay on top of your drawings. Modify the boundaries if needed by clicking the **vertical ellipsis** ![icon-ellipsis-vertical.png](https://support.procore.com/@api/deki/files/158014/icon-ellipsis-vertical.png?revision=2&size=bestfit&width=15&height=15) . Click **Edit**, and select **Boundary**. Click and drag the points around the boundary to reconfigure it.
   ![move-boundary.png](https://support.procore.com/@api/deki/files/484612/move-boundary.png?revision=2&size=bestfit&width=493&height=312)
7. After review, click **Save as Draft** or **Publish Locations**.

## See Also

- [View Locations](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/view-locations "View Locations in the Location Manager (Open Beta)")
- [Add Locations](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/add-multi-tiered-locations-to-a-project "Add Tiered Locations to a Project")
- [Edit Locations](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/edit-multi-tiered-locations "Edit Tiered Locations")
- [Delete Locations](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/delete-multi-tiered-locations "Delete Tiered Locations from a Project")