# Generate Locations Hierarchy From Drawings

Source: https://v2.support.procore.com/product-manuals/admin-project/tutorials/generate-locations-from-drawings

---

##### Â Limited Release

This experience is available in **Australia, Canada, Ireland, United Kingdom, United States,** and **New Zealand**.

## Background

Locations give users the ability to link different Procore items (RFIs, Submittals, and more) to specific locations on a job site. This helps project team members to pinpoint the exact location on a job site where a defect was observed, where equipment will be installed, or where a project change order occurred.

Procore's Locations feature allows you to automatically generate this list from your project's Architectural drawings. Locations generated from drawings are most accurate when they meet the following criteria:

- The drawings are floor plans.
- The locations have four walls and each location/room is labeled within the boundary of the four walls.

 - If characters in the drawing are close to the location/room label, they may be added to the name of the location.
 - Multi-family plans may not be generated correctly if rooms are not labeled within suites/units. However, you can [move sub-locations to the correct parent](/product-manuals/admin-project/tutorials/edit-multi-tiered-locations) after drawings are generated.

Additionally, when you generate locations from Drawings, you have access to a heat map to see what locations have items associated with them.

## Things to Consider

- **Required User Permissions**:

 - 'Admin' level permissions on the project's Admin tool. 
     OR
 - 'Read Only' or 'Standard' level permissions with the 'Manage Locations' granular permission enabled on the project Admin tool. See [Grant Granular Permissions in a Permission Template](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template).
 - Locations must be published to be visible to users with 'Read Only' or 'Standard' level permissions who do not also have the 'Manage Locations' granular permission. Draft locations are only visible to users with 'Admin' level permissions.
- **Additional Information**:

 - If you initially [manually created your locations in the Admin tool](/product-manuals/admin-project/tutorials/manually-create-tiered-locations), you would need to delete them to instead generate your locations from Drawings.
 - You can only generate locations from drawings where the drawing discipline is set to 'Architectural'. See [Configure Default Drawing Disciplines](/product-manuals/drawings-project/tutorials/configure-default-drawing-disciplines).
 - The colors next to the locations indicate the confidence level in creating the location from the drawing. Green indicates the highest level of confidence.
 - Tiers are named based on the following information:

    - Tier 0 is the name of the project.
    - Tier 1 is the drawing name.
    - Tier 2 is the location on the drawing.
- **Limitations**

 - This feature does not currently support projects that have a single drawing sheet that represents multiple floors on the project. If a project has typical floors, do NOT generate locations from drawings.

## Prerequisites

1. [Upload Drawings](/process-guides/user-guide-bidding-and-estimating-integration/upload-drawings)
2. [Review Drawings](/process-guides/user-guide-bidding-and-estimating-integration/review-and-confirm-drawings)
3. [Publish Drawings](/process-guides/user-guide-bidding-and-estimating-integration/publish-drawings)

## Steps

- Generate from the Admin Tool
- Generate from the Drawings Tool

### Generate Locations Hierarchy from the Admin Tool

1. Navigate to the project's **Admin** tool.
2. Under the 'Project Settings' menu, click **Locations.**
3. Click **Create Location Hierarchy**.
4. Select the drawings you want to use to create your list of locations.
5. Click **Submit for Extraction**. 
   A tile appears in the side menu panel to show the progress of your location extraction.
6. If prompted, click **Review Drawings.***Note:* This feature was built to extract locations for Architectural floor plans. If you want to create locations for Architectural drawings without a floor plan, keep the checkbox marked for the drawing, and Procore will generate a placeholder parent location for you to manually manage locations and boundaries.

   1. Clear the checkbox for drawings you wish to NOT extract locations.
   2. Click **Continue Location Extraction**.
7. Once processing is complete, click **Review Locations.** Locations are listed alongside an image of the associated drawing. Check the boundaries shown in the overlay on top of your drawings. Modify the boundaries if needed by clicking the **vertical ellipsis** . Click **Edit**, and select **Boundary**. Click and drag the points around the boundary to reconfigure it.
8. After review, click **Save as Draft** or **Publish Locations**.

### Generate Locations Hierarchy from the Drawings Tool

1. Navigate to the project's **Drawings** tool.
2. Click **Create Locations**.
3. Select the drawings you want to use to create your list of locations.
4. Click **Submit for Extraction**. 
   A tile appears in the side menu panel to show the progress of your location extraction.
5. If prompted, click **Review Drawings.***Note:* This feature was built to extract locations for Architectural floor plans. If you want to create locations for Architectural drawings without a floor plan, keep the checkbox marked for the drawing, and Procore will generate a placeholder parent location for you to manually manage locations and boundaries.

   1. Clear the checkbox for drawings you wish to NOT extract locations.
   2. Click **Continue Location Extraction**.
6. Once processing is complete, click **Review Locations.** Locations are listed alongside an image of the associated drawing. Check the boundaries shown in the overlay on top of your drawings. Modify the boundaries if needed by clicking the **vertical ellipsis** . Click **Edit**, and select **Boundary**. Click and drag the points around the boundary to reconfigure it.
7. After review, click **Save as Draft** or **Publish Locations**.